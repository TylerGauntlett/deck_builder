"""What a card actually says, fetched now.

The point of this script is that an agent should never argue from what it
remembers a card doing.  Oracle text gets errata'd, prices move daily, and a
half-remembered card is the fastest way to a confident wrong recommendation.

So ``lookup`` always goes to the network -- ``fetch(..., refresh=True)`` -- and
prints the fetch time beside every price.  The on-disk cache under
``data/cache/scryfall/`` is fetch-once and never expires, which is fine for
building a reference sheet and useless for quoting a price; the refresh updates
it as a side effect, so ``cards.md`` gets fresher too.

``search`` is the other half: when a proposed card is the wrong answer to a real
question, Scryfall's search syntax finds the better one instead of settling.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# The Windows console defaults to cp1252, which mangles the em dash in every
# type line.  An agent reading garbled oracle text is exactly what this script
# exists to prevent.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deck_meta
from build_card_details import parse_deck, resolve_decks
from scryfall import API, DELAY, HEADERS, LookupFailed, fetch, normalize_name

MAX_SEARCH_ROWS = 60


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _get(url: str) -> dict | None:
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise
    except (urllib.error.URLError, TimeoutError) as error:
        raise LookupFailed(f"Scryfall unreachable: {error}") from error


# ----------------------------------------------------------------------
# rendering one card
# ----------------------------------------------------------------------


def price_line(card: dict) -> str:
    prices = card.get("prices") or {}
    parts = []
    for label, key in (("USD", "usd"), ("foil", "usd_foil"), ("etched", "usd_etched")):
        if prices.get(key):
            parts.append(f"{label} ${prices[key]}")
    return ", ".join(parts) if parts else "no price listed"


def _face_block(face: dict, indent: str = "") -> list[str]:
    lines = []
    cost = face.get("mana_cost") or "--"
    lines.append(f"{indent}{face.get('name', '?')}  {cost}")
    lines.append(f"{indent}  {face.get('type_line', '?')}")
    for para in (face.get("oracle_text") or "").split("\n"):
        lines.append(f"{indent}  {para}" if para else "")
    pt = None
    if face.get("power") is not None:
        pt = f"{face['power']}/{face['toughness']}"
    elif face.get("loyalty") is not None:
        pt = f"loyalty {face['loyalty']}"
    if pt:
        lines.append(f"{indent}  [{pt}]")
    return lines


def deck_identity(deck: str) -> tuple[set[str], list[str]]:
    """The colours the deck may legally play, from its commander(s)."""
    data = deck_meta.load(deck)
    commanders = data["commander"]
    cards, missing = fetch(commanders, log=lambda *_: None)
    if missing:
        raise LookupFailed(f"could not resolve commander(s): {', '.join(missing)}")
    identity: set[str] = set()
    for name in commanders:
        identity.update(cards[normalize_name(name)].get("color_identity") or [])
    return identity, commanders


def render(card: dict, *, asked_as: str, rulings: list[dict] | None, fetched: str,
           identity: set[str] | None = None, commanders: list[str] | None = None) -> str:
    lines = [f"## {card.get('name')}", ""]
    if normalize_name(asked_as).lower() != (card.get("name") or "").lower():
        lines.append(f"(asked as {asked_as!r})")
        lines.append("")

    faces = card.get("card_faces")
    if faces:
        lines.append(f"Mana value {card.get('cmc')}  |  layout {card.get('layout')}")
        lines.append("")
        for face in faces:
            lines += _face_block(face)
            lines.append("")
    else:
        lines += _face_block(card)
        lines.append("")
        lines.append(f"Mana value {card.get('cmc')}")

    own = set(card.get("color_identity") or [])
    lines.append(f"Color identity: {''.join(sorted(own)) or 'colorless'}")
    if identity is not None:
        illegal = own - identity
        if illegal:
            lines.append(
                f"   <-- ILLEGAL IN THIS DECK: {''.join(sorted(illegal))} is outside "
                f"{''.join(sorted(identity)) or 'colorless'} ({', '.join(commanders or [])}). "
                f"No further evaluation is needed; the verdict is NO."
            )

    legal = (card.get("legalities") or {}).get("commander", "unknown")
    flag = "" if legal == "legal" else "   <-- NOT LEGAL IN COMMANDER"
    lines.append(f"Commander legality: {legal}{flag}")

    if card.get("game_changer"):
        lines.append("Game Changer: yes  (counts against a bracket 1-3 deck's allowance)")
    if card.get("edhrec_rank"):
        lines.append(f"EDHREC rank: {card['edhrec_rank']}")
    if card.get("reserved"):
        lines.append("Reserved List: yes")

    lines.append(f"Price (fetched {fetched}): {price_line(card)}")
    lines.append(f"Scryfall: {card.get('scryfall_uri')}")

    related = [p.get("name") for p in card.get("all_parts") or [] if p.get("name") != card.get("name")]
    if related:
        lines.append(f"Related: {', '.join(related)}")

    if rulings:
        lines += ["", "Official rulings:"]
        for ruling in rulings:
            lines.append(f"  [{ruling.get('published_at')}] {ruling.get('comment')}")
    elif rulings is not None:
        lines += ["", "Official rulings: none"]

    return "\n".join(lines)


# ----------------------------------------------------------------------
# commands
# ----------------------------------------------------------------------


def cmd_lookup(args: argparse.Namespace) -> int:
    identity = commanders = None
    if args.deck:
        identity, commanders = deck_identity(args.deck)

    # refresh=True unconditionally: a cached price is not a price.
    cards, missing = fetch(args.names, refresh=True, log=lambda *_: None)
    fetched = _now()

    if args.json:
        payload = {"fetched": fetched, "missing": missing, "cards": list(cards.values())}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 2 if missing else 0

    blocks = []
    for asked in args.names:
        card = cards.get(normalize_name(asked))
        if card is None:
            continue
        rulings = None
        if args.rulings and card.get("rulings_uri"):
            rulings = (_get(card["rulings_uri"]) or {}).get("data", [])
            time.sleep(DELAY)
        blocks.append(render(card, asked_as=asked, rulings=rulings, fetched=fetched,
                             identity=identity, commanders=commanders))

    print("\n\n".join(blocks))
    if missing:
        print("\nUNRESOLVED -- do not reason about these, they may not exist:")
        for name in missing:
            print(f"  - {name}")
        return 2
    return 0


def deck_names(deck: str) -> set[str]:
    """Lowercased names the deck already runs, front face included."""
    names = set()
    for _, name in parse_deck(resolve_decks([deck])[0]):
        full = normalize_name(name).lower()
        names.add(full)
        names.add(full.split("//")[0].strip())
    return names


def cmd_search(args: argparse.Namespace) -> int:
    owned = deck_names(args.deck) if args.deck else set()

    url = f"{API}/cards/search?q={urllib.parse.quote(args.query)}&order={args.order}&unique=cards"
    try:
        payload = _get(url)
    except urllib.error.HTTPError as error:
        print(f"Scryfall rejected the query: {error}", file=sys.stderr)
        return 1
    if payload is None:
        print(f"No cards match {args.query!r}", file=sys.stderr)
        return 1

    total = payload.get("total_cards", 0)
    rows = payload.get("data", [])[: args.limit]
    print(f"{total} match{'es' if total != 1 else ''} for `{args.query}`"
          f"{f' -- showing {len(rows)}' if total > len(rows) else ''}")
    print(f"Prices fetched {_now()}.\n")

    for card in rows:
        name = (card.get("name") or "")
        mark = ""
        if owned and (name.lower() in owned or name.lower().split("//")[0].strip() in owned):
            mark = "  [IN DECK]"
        prices = card.get("prices") or {}
        usd = f"${prices['usd']}" if prices.get("usd") else "n/a"
        gc = " [GAME CHANGER]" if card.get("game_changer") else ""
        print(f"- {name}  {card.get('mana_cost') or '--'}  (MV {card.get('cmc')})  {usd}{gc}{mark}")
        print(f"    {card.get('type_line')}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    lookup = sub.add_parser("lookup", help="verify cards against Scryfall, live")
    lookup.add_argument("names", nargs="+")
    lookup.add_argument("--deck", help="check colour identity against this deck's commander")
    lookup.add_argument("--rulings", action="store_true", help="also fetch official rulings")
    lookup.add_argument("--json", action="store_true")

    search = sub.add_parser("search", help="find candidates with Scryfall search syntax")
    search.add_argument("query")
    search.add_argument("--deck", help="mark results this deck already runs")
    search.add_argument("--limit", type=int, default=25)
    search.add_argument("--order", default="edhrec", help="edhrec, cmc, usd, name...")

    args = parser.parse_args(argv)
    if args.command == "search" and args.limit > MAX_SEARCH_ROWS:
        args.limit = MAX_SEARCH_ROWS

    try:
        return cmd_lookup(args) if args.command == "lookup" else cmd_search(args)
    except (LookupFailed, deck_meta.MetaMissing) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
