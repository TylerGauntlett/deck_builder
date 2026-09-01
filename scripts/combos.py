"""Which combos a deck actually has, from Commander Spellbook.

"This card combos with X" is the single easiest claim to get wrong from memory,
and the most persuasive when it lands.  So it gets checked: the whole decklist
goes to Commander Spellbook, which answers with the combos the deck already
assembles (``included``) and the ones it is one or two cards short of
(``almostIncluded``).

``--add`` is the interesting mode.  It runs the query twice -- once as the deck
stands, once with the candidates shuffled in -- and prints only the difference.
A combo that shows up in the second run and not the first is a combo the
candidate genuinely enables.  Anything else is a story.

Note this reports what a deck *can* do, not what it *should*.  A deck whose
meta.json bars early infinite combos wants this output as a warning, not as a
selling point; the rubric decides, this script only finds.

Endpoint (verified):
    POST https://backend.commanderspellbook.com/find-my-combos/
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deck_meta
from build_card_details import parse_deck, resolve_decks
from scryfall import HEADERS, LookupFailed, normalize_name

ENDPOINT = "https://backend.commanderspellbook.com/find-my-combos/"


def post(payload: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"User-Agent": HEADERS["User-Agent"], "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise LookupFailed(f"Commander Spellbook returned {error.code}: {error.reason}") from error
    except (urllib.error.URLError, TimeoutError) as error:
        raise LookupFailed(f"Commander Spellbook unreachable: {error}") from error


# ----------------------------------------------------------------------
# building the request
# ----------------------------------------------------------------------


def deck_payload(deck: str, extra: list[str]) -> dict:
    """The decklist as Spellbook wants it, commanders split out from the rest."""
    data = deck_meta.load(deck)
    commanders = [normalize_name(c) for c in data["commander"]]
    lowered = {c.lower() for c in commanders}

    main = []
    for _, name in parse_deck(resolve_decks([deck])[0]):
        full = normalize_name(name)
        if full.lower() in lowered:
            continue
        main.append(full)
    main.extend(normalize_name(name) for name in extra)

    return {
        "commanders": [{"card": c} for c in commanders],
        "main": [{"card": c} for c in main],
    }


# ----------------------------------------------------------------------
# reading the response
# ----------------------------------------------------------------------


def combo_id(variant: dict) -> str:
    return str(variant.get("id"))


def pieces(variant: dict) -> list[str]:
    return [u.get("card", {}).get("name", "?") for u in variant.get("uses", []) or []]


def produces(variant: dict) -> list[str]:
    return [f.get("feature", {}).get("name", "?") for f in variant.get("produces", []) or []]


def describe(variant: dict, owned: set[str]) -> str:
    used = pieces(variant)
    missing = [name for name in used if name.lower() not in owned]
    lines = [f"  [{combo_id(variant)}] {' + '.join(used)}"]
    results = produces(variant)
    if results:
        lines.append(f"      produces: {', '.join(results[:6])}")
    if missing:
        lines.append(f"      MISSING: {', '.join(missing)}")
    lines.append(f"      https://commanderspellbook.com/combo/{combo_id(variant)}/")
    return "\n".join(lines)


def variants(results: dict, key: str) -> list[dict]:
    return results.get(key) or []


def owned_names(payload: dict) -> set[str]:
    names = {c["card"].lower() for c in payload["commanders"]}
    names |= {c["card"].lower() for c in payload["main"]}
    return names


def run(deck: str, extra: list[str]) -> tuple[dict, dict]:
    payload = deck_payload(deck, extra)
    return post(payload).get("results", {}), payload


# ----------------------------------------------------------------------
# cli
# ----------------------------------------------------------------------


def report(results: dict, owned: set[str], *, limit: int, near: bool) -> None:
    included = variants(results, "included")
    print(f"\n## Combos the deck already assembles ({len(included)})")
    if not included:
        print("  none")
    for variant in included[:limit]:
        print(describe(variant, owned))

    if not near:
        return
    almost = variants(results, "almostIncluded")
    print(f"\n## One or more pieces short ({len(almost)}, showing {min(limit, len(almost))})")
    if not almost:
        print("  none")
    for variant in almost[:limit]:
        print(describe(variant, owned))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("deck")
    parser.add_argument("--add", action="append", default=[], metavar="CARD",
                        help="candidate to test; repeatable. Prints only what it changes.")
    parser.add_argument("--limit", type=int, default=15)
    parser.add_argument("--near", action="store_true",
                        help="also list combos the deck is short a piece of")

    args = parser.parse_args(argv)
    try:
        base, base_payload = run(args.deck, [])

        if not args.add:
            print(f"# Commander Spellbook: {args.deck}")
            print(f"Colour identity {base.get('identity', '?')}.")
            report(base, owned_names(base_payload), limit=args.limit, near=args.near)
            return 0

        after, after_payload = run(args.deck, args.add)
        owned = owned_names(after_payload)

        before_ids = {combo_id(v) for v in variants(base, "included")}
        gained = [v for v in variants(after, "included") if combo_id(v) not in before_ids]

        print(f"# Commander Spellbook: {args.deck} + {', '.join(args.add)}")
        print(f"Baseline: {len(variants(base, 'included'))} combos already assembled.")
        print(f"\n## New combos these cards complete ({len(gained)})")
        if not gained:
            print("  none -- the candidate does not complete any known combo in this deck.")
        for variant in gained[:args.limit]:
            print(describe(variant, owned))

        if args.near:
            before_near = {combo_id(v) for v in variants(base, "almostIncluded")}
            newly_near = [v for v in variants(after, "almostIncluded")
                          if combo_id(v) not in before_near]
            print(f"\n## Newly within reach, still missing a piece ({len(newly_near)})")
            for variant in newly_near[:args.limit]:
                print(describe(variant, owned))
        return 0
    except (LookupFailed, deck_meta.MetaMissing) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
