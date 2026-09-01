"""Scryfall lookups for the cards in a deck list.

Same shape as the Auto MTG fetchers: stdlib only, a descriptive User-Agent,
a pause between requests, and a fetch-once cache on disk so a re-run costs
nothing.  The difference is the endpoint -- ``/cards/collection`` takes 75
identifiers per POST, so a 100-card deck is two requests rather than a hundred.

Cards land in ``data/cache/scryfall/<slug>.json``, one file per card, holding
the raw Scryfall payload.  Nothing here writes into ``decks/``.
"""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "data" / "cache" / "scryfall"

API = "https://api.scryfall.com"
HEADERS = {
    "User-Agent": "deck-builder/0.1 (card detail sheets)",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

#: Scryfall asks for 50-100ms between requests, and caps a collection POST at 75.
DELAY = 0.1
CHUNK = 75


class LookupFailed(Exception):
    """Scryfall was reachable but had nothing for this name."""


# ----------------------------------------------------------------------
# names
# ----------------------------------------------------------------------


def normalize_name(name: str) -> str:
    """The name Scryfall answers to.

    Deck exports write a double-faced card as ``Front / Back``; Scryfall spells
    it ``Front // Back``.  A single slash is never part of a real card name, so
    the rewrite is safe.
    """
    name = name.strip()
    if "//" not in name:
        name = re.sub(r"\s*/\s*", " // ", name)
    return re.sub(r"\s+", " ", name).strip()


def front_face(name: str) -> str:
    """Just the front half, for the fallback lookup."""
    return name.split("//")[0].strip()


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# ----------------------------------------------------------------------
# transport
# ----------------------------------------------------------------------


def _request(path: str, payload: dict | None = None) -> dict | None:
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(f"{API}{path}", data=body, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise
    except (urllib.error.URLError, TimeoutError) as error:
        raise LookupFailed(f"Scryfall unreachable: {error}") from error


def _named(name: str) -> dict | None:
    """One card by exact name, then by Scryfall's fuzzy match."""
    quoted = urllib.parse.quote(name)
    card = _request(f"/cards/named?exact={quoted}")
    time.sleep(DELAY)
    if card is not None:
        return card
    card = _request(f"/cards/named?fuzzy={quoted}")
    time.sleep(DELAY)
    return card


# ----------------------------------------------------------------------
# cache
# ----------------------------------------------------------------------


def cache_path(name: str) -> Path:
    return CACHE_DIR / f"{slugify(name)}.json"


def cached(name: str) -> dict | None:
    path = cache_path(name)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def store(name: str, card: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path(name).write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding="utf-8")


# ----------------------------------------------------------------------
# the one entry point
# ----------------------------------------------------------------------


def fetch(names: list[str], *, refresh: bool = False, log=print) -> tuple[dict[str, dict], list[str]]:
    """Resolve every name to its Scryfall payload.

    Returns ``(cards, missing)`` keyed by the name as it was asked for, so the
    caller can still print the deck in its own order and its own spelling.
    """
    wanted = [normalize_name(n) for n in names]
    cards: dict[str, dict] = {}
    todo: list[str] = []

    for name in wanted:
        hit = None if refresh else cached(name)
        if hit is not None:
            cards[name] = hit
        elif name not in todo:
            todo.append(name)

    if cards:
        log(f"  cached  {len(cards)}")

    unresolved: list[str] = []
    for index in range(0, len(todo), CHUNK):
        batch = todo[index : index + CHUNK]
        log(f"  fetch   {len(batch)}")
        payload = _request("/cards/collection", {"identifiers": [{"name": n} for n in batch]})
        time.sleep(DELAY)
        for card in (payload or {}).get("data", []):
            # Scryfall answers with its own spelling; match it back to the ask.
            returned = card.get("name", "")
            key = next(
                (n for n in batch if n.lower() in (returned.lower(), front_face(returned).lower())),
                None,
            )
            if key is None:
                key = next((n for n in batch if front_face(n).lower() == front_face(returned).lower()), returned)
            cards[key] = card
            store(key, card)
        unresolved.extend(n for n in batch if n not in cards)

    # The collection endpoint matches on the whole name, so a deck list that
    # spells a double-faced card with only its front half lands here.
    missing: list[str] = []
    for name in unresolved:
        log(f"  retry   {name}")
        card = _named(name) or _named(front_face(name))
        if card is None:
            missing.append(name)
            continue
        cards[name] = card
        store(name, card)

    return cards, missing
