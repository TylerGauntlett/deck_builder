"""Pull a deck's current list from Moxfield and expand it into a card reference.

    python scripts/build_card_details.py                  # every deck
    python scripts/build_card_details.py markov_chains    # one deck
    python scripts/build_card_details.py --refresh        # re-pull from Scryfall

A deck is a directory under ``decks/`` whose ``meta.json`` names its Moxfield URL
under ``source``.  Two files are written beside it:

``cards.json``
    The last synced list, with every card's full Scryfall detail -- mana cost,
    type line, oracle text, power/toughness, keywords, colour identity, the lot.
    Committed, and the only copy of the list the other scripts read.
``cards.md``
    The same set rendered for reading.  This is the file to hand an agent asking
    about swaps and synergies.  Gitignored, since it is derived from cards.json.

If Moxfield can't be reached, ``cards.md`` is rendered from the last ``cards.json``
with a staleness warning, and the exit code is 3.

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from moxfield import MoxfieldUnavailable, pull  # noqa: E402
from scryfall import LookupFailed, fetch, normalize_name  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DECKS = ROOT / "decks"

#: Exit code when the list on disk could not be checked against Moxfield.
STALE = 3


# ----------------------------------------------------------------------
# reading the list
# ----------------------------------------------------------------------


def deck_names() -> list[str]:
    """Every deck under ``decks/``."""
    return sorted(path.parent.name for path in DECKS.glob("*/meta.json"))


def deck_source(deck: str) -> str:
    """The Moxfield URL in the deck's ``meta.json``."""
    path = DECKS / deck / "meta.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if not data.get("source"):
        raise SystemExit(f"{path} has no Moxfield `source` -- ask the user for the deck's URL")
    return data["source"]


def read_list(deck: str) -> list[tuple[int, str]]:
    """``[(qty, name)]`` from the deck's last sync."""
    path = DECKS / deck / "cards.json"
    if not path.exists():
        raise SystemExit(f"no {path} -- run: python scripts/build_card_details.py {deck}")
    data = json.loads(path.read_text(encoding="utf-8"))
    return [(d["qty"], d["name"]) for d in data["cards"]]


# ----------------------------------------------------------------------
# flattening a Scryfall payload
# ----------------------------------------------------------------------


def faces(card: dict) -> list[dict]:
    """One entry per printed face.  Single-faced cards are a list of one."""
    sub = card.get("card_faces") or []
    return sub if len(sub) > 1 else [card]


def face_detail(face: dict, card: dict) -> dict:
    """The rules-relevant half of a face, with the card-level fallback."""
    return {
        "name": face.get("name"),
        "mana_cost": face.get("mana_cost") or card.get("mana_cost") or "",
        "type_line": face.get("type_line") or card.get("type_line") or "",
        "oracle_text": face.get("oracle_text") or card.get("oracle_text") or "",
        "power": face.get("power"),
        "toughness": face.get("toughness"),
        "loyalty": face.get("loyalty"),
        "defense": face.get("defense"),
        "colors": face.get("colors") or card.get("colors") or [],
    }


def detail(card: dict, qty: int) -> dict:
    """Everything about one card worth reasoning over."""
    return {
        "name": card.get("name"),
        "qty": qty,
        "mana_cost": card.get("mana_cost", ""),
        "cmc": card.get("cmc"),
        "type_line": card.get("type_line", ""),
        "layout": card.get("layout"),
        "colors": card.get("colors") or [],
        "color_identity": card.get("color_identity") or [],
        "produced_mana": card.get("produced_mana") or [],
        "keywords": card.get("keywords") or [],
        "power": card.get("power"),
        "toughness": card.get("toughness"),
        "loyalty": card.get("loyalty"),
        "faces": [face_detail(f, card) for f in faces(card)],
        "rarity": card.get("rarity"),
        "set": card.get("set"),
        "set_name": card.get("set_name"),
        "released_at": card.get("released_at"),
        "reserved": card.get("reserved", False),
        # Scryfall's Commander-bracket flag: the cards that push a deck up a tier.
        "game_changer": card.get("game_changer", False),
        "commander_legal": (card.get("legalities") or {}).get("commander"),
        "edhrec_rank": card.get("edhrec_rank"),
        "price_usd": (card.get("prices") or {}).get("usd"),
        "all_parts": [
            {"name": p.get("name"), "component": p.get("component"), "type_line": p.get("type_line")}
            for p in card.get("all_parts") or []
            if p.get("name") != card.get("name")
        ],
        "scryfall_uri": card.get("scryfall_uri"),
        "oracle_id": card.get("oracle_id"),
    }


# ----------------------------------------------------------------------
# the sheet
# ----------------------------------------------------------------------


def is_land(detail_row: dict) -> bool:
    """Front face only.  A modal card like Malakir Rebirth // Malakir Mire is a
    spell you sometimes play as a land, and counting it in the mana base would
    overstate the land count in every summary below."""
    return "Land" in (detail_row["type_line"] or "").split("//")[0]


def stats(details: list[dict]) -> dict:
    """The counts a reviewer would otherwise tally by hand."""
    lands = [d for d in details if is_land(d)]
    spells = [d for d in details if not is_land(d)]
    spell_copies = sum(d["qty"] for d in spells)
    costs = [d["cmc"] * d["qty"] for d in spells if isinstance(d.get("cmc"), (int, float))]

    types: dict[str, int] = {}
    for d in details:
        primary = (d["type_line"] or "").split("//")[0]
        for kind in ("Land", "Creature", "Artifact", "Enchantment", "Planeswalker", "Battle", "Instant", "Sorcery"):
            if kind in primary:
                types[kind] = types.get(kind, 0) + d["qty"]
                break

    pips: dict[str, int] = {}
    for d in details:
        for symbol in re.findall(r"\{([WUBRG])\}", d["mana_cost"] or ""):
            pips[symbol] = pips.get(symbol, 0) + d["qty"]

    return {
        "cards": sum(d["qty"] for d in details),
        "distinct": len(details),
        "lands": sum(d["qty"] for d in lands),
        "avg_mana_value_nonland": round(sum(costs) / spell_copies, 2) if spell_copies else 0,
        "type_counts": dict(sorted(types.items(), key=lambda kv: -kv[1])),
        "color_pips": dict(sorted(pips.items(), key=lambda kv: -kv[1])),
        "game_changers": sorted(d["name"] for d in details if d["game_changer"]),
    }


def render_card(d: dict) -> str:
    """One card, as a heading plus the fields that carry rules meaning."""
    head = f"### {d['name']}"
    if d["qty"] > 1:
        head += f" (x{d['qty']})"
    lines = [head, ""]

    for face in d["faces"]:
        if len(d["faces"]) > 1:
            lines.append(f"**{face['name']}**")
            lines.append("")
        lines.append(f"- Cost: {face['mana_cost'] or '-'}  |  Mana value: {d['cmc']}")
        lines.append(f"- Type: {face['type_line'] or '-'}")
        body = (face["oracle_text"] or "").strip()
        lines.append("- Text: " + (body.replace("\n", "\n  ") if body else "-"))
        if face["power"] is not None:
            lines.append(f"- P/T: {face['power']}/{face['toughness']}")
        if face["loyalty"] is not None:
            lines.append(f"- Loyalty: {face['loyalty']}")
        if face["defense"] is not None:
            lines.append(f"- Defense: {face['defense']}")
        lines.append("")

    tags = [f"Color identity: {''.join(d['color_identity']) or 'C'}"]
    if d["keywords"]:
        tags.append("Keywords: " + ", ".join(d["keywords"]))
    if d["produced_mana"]:
        tags.append("Produces: " + "".join(sorted(d["produced_mana"])))
    if d["edhrec_rank"]:
        tags.append(f"EDHREC rank: {d['edhrec_rank']}")
    if d["price_usd"]:
        tags.append(f"~${d['price_usd']}")
    if d["game_changer"]:
        tags.append("**Game Changer**")
    if d["commander_legal"] and d["commander_legal"] != "legal":
        tags.append(f"Commander: {d['commander_legal']}")
    if d["all_parts"]:
        tags.append("Related: " + ", ".join(p["name"] for p in d["all_parts"]))
    lines.append("- " + " | ".join(tags))
    lines.append("")
    return "\n".join(lines)


def render(deck: str, details: list[dict], missing: list[str], updated: str, *, stale: str = "") -> str:
    summary = stats(details)
    out = [
        f"# {deck} - card details",
        "",
    ]
    if stale:
        out += [f"**STALE LIST: {stale}. This is the last synced list and may not match the deck.**", ""]
    out += [
        f"List from Moxfield, last updated {updated}. Generated "
        f"{datetime.now(UTC).strftime('%Y-%m-%d')} by `scripts/build_card_details.py`. "
        "Regenerate rather than editing by hand.",
        "",
        "## Deck at a glance",
        "",
        f"- {summary['cards']} cards ({summary['distinct']} distinct), {summary['lands']} lands",
        f"- Average mana value of non-lands: {summary['avg_mana_value_nonland']}",
        "- Types: " + ", ".join(f"{k} {v}" for k, v in summary["type_counts"].items()),
        "- Colored pips: " + (", ".join(f"{k} {v}" for k, v in summary["color_pips"].items()) or "none"),
    ]
    if summary["game_changers"]:
        out.append("- Game Changers: " + ", ".join(summary["game_changers"]))
    if missing:
        out.append("- **Unresolved names:** " + ", ".join(missing))
    out.append("")

    # Lands last: a reviewer reads the spells, and the mana base is its own pass.
    spells = [d for d in details if not is_land(d)]
    lands = [d for d in details if is_land(d)]
    for group, title in ((spells, "Spells and permanents"), (lands, "Lands")):
        if not group:
            continue
        out.append(f"## {title}")
        out.append("")
        out += [render_card(d) for d in sorted(group, key=lambda d: d["name"] or "")]
    return "\n".join(out).rstrip() + "\n"


# ----------------------------------------------------------------------


def render_stale(deck: str, reason: str) -> int:
    """Moxfield is out of reach: show the last sync, and say that it is the last sync."""
    target = DECKS / deck
    if not (target / "cards.json").exists():
        print(f"{deck}: {reason}, and there is no earlier sync to fall back on")
        return 1
    data = json.loads((target / "cards.json").read_text(encoding="utf-8"))
    updated = data.get("moxfield_updated", "unknown")
    sheet = render(deck, data["cards"], data.get("unresolved", []), updated, stale=reason)
    (target / "cards.md").write_text(sheet, encoding="utf-8")
    print(f"{deck}: STALE -- {reason}. Using the last sync (Moxfield updated {updated}).")
    return STALE


def build(deck: str, *, refresh: bool) -> int:
    source = deck_source(deck)
    try:
        entries, updated = pull(source)
    except MoxfieldUnavailable as error:
        return render_stale(deck, str(error))

    print(f"{deck}: {sum(q for q, _ in entries)} cards, {len(entries)} distinct (Moxfield updated {updated})")
    cards, missing = fetch([name for _, name in entries], refresh=refresh)

    details = []
    for qty, name in entries:
        card = cards.get(normalize_name(name))
        if card is not None:
            details.append(detail(card, qty))

    target = DECKS / deck
    (target / "cards.md").write_text(render(deck, details, missing, updated), encoding="utf-8")
    (target / "cards.json").write_text(
        json.dumps(
            {
                "deck": deck,
                "source": source,
                "moxfield_updated": updated,
                "stats": stats(details),
                "unresolved": missing,
                "cards": details,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"  wrote   {target / 'cards.md'}")
    if missing:
        print(f"  MISSING {', '.join(missing)}")
        return 2
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("decks", nargs="*", help="deck names; default is every deck under decks/")
    parser.add_argument("--refresh", action="store_true", help="ignore the cache and re-pull from Scryfall")
    args = parser.parse_args()

    decks = args.decks or deck_names()
    if not decks:
        print(f"no decks under {DECKS}")
        return 1

    status = 0
    for deck in decks:
        try:
            status = max(status, build(deck, refresh=args.refresh))
        except LookupFailed as error:
            print(f"  {error}")
            status = 1
    return status


if __name__ == "__main__":
    raise SystemExit(main())
