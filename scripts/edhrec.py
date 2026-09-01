"""What the community actually plays, from EDHREC.

EDHREC answers one question well: out of every deck registered with this
commander, what fraction run this card, and how much more often than a random
deck in these colours?  That is popularity, not quality -- see
``.claude/skills/mtg-deck-advisor/references/data-sources.md`` -- but it is a
useful check on a recommendation reached by reasoning alone.  If this script says
a card is in 4% of Edgar Markov decks and the argument for it was "obvious
include", one of the two is wrong and it is worth finding out which.

The commander page is ~100 KB of JSON.  Nothing here prints raw payloads; every
command reduces it to rows an agent can read in one pass.

Endpoints (verified):
    https://json.edhrec.com/pages/commanders/<slug>.json
    https://json.edhrec.com/pages/commanders/<slug>/<theme>.json
    https://json.edhrec.com/pages/cards/<slug>.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deck_meta
from build_card_details import parse_deck, resolve_decks
from scryfall import DELAY, HEADERS, LookupFailed, fetch, normalize_name

BASE = "https://json.edhrec.com/pages"

#: The lists worth reading by default; the rest are long type dumps.
HEADLINE = ("highsynergycards", "topcards", "gamechangers", "newcards", "highliftcards")


class NotOnEdhrec(Exception):
    """EDHREC has no page under that slug."""


# ----------------------------------------------------------------------
# slugs and transport
# ----------------------------------------------------------------------


def slug(name: str) -> str:
    """EDHREC's URL form: accents folded, punctuation dropped, spaces hyphenated.

    ``Clavileno, First of the Blessed`` -> ``clavileno-first-of-the-blessed``.
    This differs from ``scryfall.slugify``, which leaves an accented letter in
    place as a separator.  A double-faced card is keyed on its front face.
    """
    name = name.split("//")[0].split(" / ")[0].strip().lower()
    folded = unicodedata.normalize("NFKD", name)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    out = "".join(c if c.isalnum() else "-" for c in folded)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def get(path: str) -> dict:
    url = f"{BASE}/{path}.json"
    request = urllib.request.Request(url, headers={"User-Agent": HEADERS["User-Agent"]})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            raise NotOnEdhrec(f"EDHREC has no page at {url}") from error
        raise
    except (urllib.error.URLError, TimeoutError) as error:
        raise LookupFailed(f"EDHREC unreachable: {error}") from error
    time.sleep(DELAY)
    return payload


def commander_slug(deck: str) -> tuple[str, list[str]]:
    """The EDHREC slug for a deck's commander(s); a partner pair is joined."""
    commanders = deck_meta.load(deck)["commander"]
    return "-".join(slug(c) for c in commanders), commanders


# ----------------------------------------------------------------------
# reducing the payload
# ----------------------------------------------------------------------


def cardlists(payload: dict) -> list[dict]:
    return payload.get("container", {}).get("json_dict", {}).get("cardlists", []) or []


def inclusion(view: dict) -> float | None:
    """Share of registered decks running this card, 0-1."""
    num, pot = view.get("num_decks"), view.get("potential_decks")
    if not num or not pot:
        return None
    return num / pot


def row(view: dict, owned: set[str]) -> str:
    name = view.get("name", "?")
    share = inclusion(view)
    pct = f"{share * 100:5.1f}%" if share is not None else "    ?"
    synergy = view.get("synergy")
    syn = f"synergy {synergy:+.2f}" if isinstance(synergy, (int, float)) else "synergy ?"
    counts = f"{view.get('num_decks', '?')}/{view.get('potential_decks', '?')} decks"
    mark = "  [IN DECK]" if slug(name) in owned else ""
    return f"  {pct}  {syn}  {counts:>17}  {name}{mark}"


def deck_slugs(deck: str) -> set[str]:
    return {slug(name) for _, name in parse_deck(resolve_decks([deck])[0])}


def print_lists(payload: dict, owned: set[str], *, tags: list[str] | None,
                limit: int, diff: bool) -> None:
    for card_list in cardlists(payload):
        tag = card_list.get("tag")
        if tags and tag not in tags:
            continue
        views = card_list.get("cardviews", [])
        header = f"{card_list.get('header')} ({tag}, {len(views)})"

        if not diff:
            print(f"\n### {header}")
            for view in views[:limit]:
                print(row(view, owned))
            continue

        runs = [v for v in views if slug(v.get("name", "")) in owned]
        missing = [v for v in views if slug(v.get("name", "")) not in owned]
        print(f"\n### {header} -- runs {len(runs)}, missing {len(missing)}")
        if runs:
            print("  -- already in the deck --")
            for view in runs[:limit]:
                print(row(view, owned))
        if missing:
            print("  -- not in the deck --")
            for view in missing[:limit]:
                print(row(view, owned))


def print_context(payload: dict) -> None:
    panels = payload.get("panels", {}) or {}
    # EDHREC lists ~100 themes, most with only a handful of decks behind them.
    # The head of the list is ordered by popularity and is the part worth reading.
    themes = [t.get("value") for t in panels.get("taglinks", []) if t.get("value")]
    if themes:
        shown = ", ".join(themes[:20])
        rest = f" (+{len(themes) - 20} more)" if len(themes) > 20 else ""
        print(f"\nThemes (pass one as the `theme` argument): {shown}{rest}")
    for key, label in (("bracket_counts", "Brackets"), ("budget_counts", "Budgets")):
        counts = payload.get(key)
        if counts:
            print(f"{label}: {json.dumps(counts)}")


# ----------------------------------------------------------------------
# commands
# ----------------------------------------------------------------------


def cmd_commander(args: argparse.Namespace) -> int:
    name, commanders = commander_slug(args.deck)
    path = f"commanders/{name}"
    if getattr(args, "theme", None):
        path += f"/{slug(args.theme)}"
    payload = get(path)

    print(f"# EDHREC: {payload.get('header') or ', '.join(commanders)}")
    print(f"Source: {BASE}/{path}.json")
    print("Inclusion % is how many registered decks run the card; synergy is how much")
    print("more often than a deck in these colours generally. Popularity, not quality.")
    print_context(payload)

    tags = args.tags.split(",") if args.tags else (None if args.all else list(HEADLINE))
    print_lists(payload, deck_slugs(args.deck), tags=tags, limit=args.limit, diff=args.diff)
    return 0


def cmd_card(args: argparse.Namespace) -> int:
    # Resolve through Scryfall first, so a typo fails here rather than as a 404.
    cards, missing = fetch([args.name], log=lambda *_: None)
    if missing:
        print(f"Scryfall does not know {args.name!r}", file=sys.stderr)
        return 1
    card = cards[normalize_name(args.name)]

    path = f"cards/{slug(card['name'])}"
    payload = get(path)
    print(f"# EDHREC: {card['name']}")
    print(f"Source: {BASE}/{path}.json")
    if card.get("edhrec_rank"):
        print(f"Overall EDHREC rank: {card['edhrec_rank']}")

    owned = deck_slugs(args.deck) if args.deck else set()
    tags = args.tags.split(",") if args.tags else (None if args.all else ["topcommanders", *HEADLINE])
    print_lists(payload, owned, tags=tags, limit=args.limit, diff=False)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    # Shared, and attached to each subparser rather than the root, so the flags
    # may follow the subcommand where a caller naturally types them.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--limit", type=int, default=15)
    common.add_argument("--tags", help="comma-separated cardlist tags to print")
    common.add_argument("--all", action="store_true", help="every cardlist, not just headline ones")

    commander = sub.add_parser("commander", parents=[common], help="the deck's commander page")
    commander.add_argument("deck")
    commander.add_argument("--diff", action="store_true", help="split into runs / missing")

    theme = sub.add_parser("theme", parents=[common], help="a commander page narrowed to one archetype")
    theme.add_argument("deck")
    theme.add_argument("theme")
    theme.add_argument("--diff", action="store_true")

    card = sub.add_parser("card", parents=[common], help="one card's own page")
    card.add_argument("name")
    card.add_argument("--deck", help="mark cards this deck already runs")

    args = parser.parse_args(argv)
    try:
        return cmd_card(args) if args.command == "card" else cmd_commander(args)
    except (NotOnEdhrec, LookupFailed, deck_meta.MetaMissing) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
