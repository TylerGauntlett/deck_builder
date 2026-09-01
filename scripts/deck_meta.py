"""The stable context for a deck -- commander, bracket, budget, house rules.

A decklist says what the deck *is*; it never says what the deck is *for*.  Whether
a card is good is only answerable against a power target, a budget and a pod, so
those live in ``decks/<deck>/meta.json`` and are written once rather than asked
for every session.

Nothing here invents a value.  A missing or malformed field is reported so the
caller can ask a human, because a guessed bracket silently grades every later
recommendation against the wrong deck.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_card_details import DECKS, resolve_decks

#: Everything a review needs before it can judge anything.
REQUIRED = ("commander", "format", "bracket")
OPTIONAL = ("budget", "goals", "meta", "constraints", "preferences", "updated")

BRACKETS = {
    1: "Exhibition -- theme over winning",
    2: "Core -- precon level, no Game Changers",
    3: "Upgraded -- tuned, up to 3 Game Changers, no early infinites",
    4: "Optimized -- high power, no restrictions short of cEDH",
    5: "cEDH -- tournament, win as fast as possible",
}

TEMPLATE = {
    "commander": [],
    "format": "commander",
    "bracket": None,
    "budget": {"per_card_max_usd": None},
    "goals": "",
    "meta": "",
    "constraints": [],
    "preferences": [],
    "updated": "",
}


class MetaMissing(Exception):
    """No meta.json, or one that cannot be trusted to judge a card against."""


def meta_path(deck: str) -> Path:
    """Beside the decklist, whether the deck is a folder or a loose file."""
    list_path = resolve_decks([deck])[0]
    if list_path.parent == DECKS:  # decks/<deck>.txt
        return DECKS / list_path.stem / "meta.json"
    return list_path.parent / "meta.json"


def load(deck: str, *, strict: bool = True) -> dict:
    """The deck's context, or ``MetaMissing`` naming exactly what to go ask for."""
    path = meta_path(deck)
    if not path.exists():
        raise MetaMissing(
            f"no {path} -- ask the user for commander, format and bracket, "
            f"then run: python scripts/deck_meta.py init {deck}"
        )
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise MetaMissing(f"{path} is not valid JSON: {error}") from error

    if strict:
        blank = [f for f in REQUIRED if not data.get(f)]
        if blank:
            raise MetaMissing(f"{path} is missing {', '.join(blank)} -- ask the user, do not guess")
        if data["bracket"] not in BRACKETS:
            raise MetaMissing(f"{path}: bracket {data['bracket']!r} is not one of {sorted(BRACKETS)}")
        if isinstance(data["commander"], str):
            data["commander"] = [data["commander"]]
    return data


def per_card_cap(data: dict) -> float | None:
    """The price above which a card needs an unusually strong case, if any."""
    return (data.get("budget") or {}).get("per_card_max_usd")


# ----------------------------------------------------------------------
# rendering
# ----------------------------------------------------------------------


def render(deck: str, data: dict) -> str:
    lines = [f"# {deck} -- deck context", ""]
    lines.append(f"- Commander: {', '.join(data['commander'])}")
    lines.append(f"- Format: {data['format']}")
    bracket = data["bracket"]
    lines.append(f"- Bracket: {bracket} ({BRACKETS.get(bracket, 'unknown')})")

    cap = per_card_cap(data)
    lines.append(f"- Budget: {'no cap' if cap is None else f'${cap:g} per card'}")
    if data.get("goals"):
        lines.append(f"- Goals: {data['goals']}")
    if data.get("meta"):
        lines.append(f"- Meta: {data['meta']}")

    if data.get("constraints"):
        lines += ["", "## Hard constraints (vetoes)", ""]
        lines += [f"- {c}" for c in data["constraints"]]
    if data.get("preferences"):
        lines += ["", "## Preferences (tiebreakers only)", ""]
        lines += [f"- {p}" for p in data["preferences"]]
    if data.get("updated"):
        lines += ["", f"Last updated {data['updated']}."]
    return "\n".join(lines)


# ----------------------------------------------------------------------
# cli
# ----------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    show = sub.add_parser("show", help="print a deck's context")
    show.add_argument("deck")
    show.add_argument("--json", action="store_true", help="raw JSON instead of prose")
    show.add_argument("--loose", action="store_true", help="do not fail on missing fields")

    init = sub.add_parser("init", help="write a blank meta.json to fill in")
    init.add_argument("deck")
    init.add_argument("--force", action="store_true", help="overwrite an existing file")

    args = parser.parse_args(argv)

    if args.command == "init":
        path = meta_path(args.deck)
        if path.exists() and not args.force:
            print(f"{path} already exists; pass --force to replace it", file=sys.stderr)
            return 1
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(TEMPLATE, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {path}")
        print("Fill in commander, format and bracket from the user -- do not guess them.")
        print("Brackets: " + "; ".join(f"{k} {v}" for k, v in BRACKETS.items()))
        return 0

    try:
        data = load(args.deck, strict=not args.loose)
    except MetaMissing as error:
        print(error, file=sys.stderr)
        return 1

    print(json.dumps(data, indent=2, ensure_ascii=False) if args.json else render(args.deck, data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
