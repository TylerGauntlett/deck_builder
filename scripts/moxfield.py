"""The current list for a deck, from its public Moxfield page.

Moxfield is where the decklist is edited, so it is the only list that is ever
right.  ``meta.json`` holds the deck's URL under ``source``.

The API answers 403 to urllib's default User-Agent, so the header here is not
optional.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

API = "https://api2.moxfield.com/v3/decks/all"
HEADERS = {
    "User-Agent": "mtg-deck-builder/0.1 (card detail sheets)",
    "Accept": "application/json",
}

#: The boards that are actually the deck; maybeboard and sideboard are not.
BOARDS = ("commanders", "companions", "mainboard")


class MoxfieldUnavailable(Exception):
    """The list could not be pulled, so nothing is known about the live deck."""


def deck_id(source: str) -> str:
    match = re.search(r"moxfield\.com/decks/([\w-]+)", source)
    if match is None:
        raise MoxfieldUnavailable(f"not a Moxfield deck URL: {source!r}")
    return match.group(1)


def pull(source: str) -> tuple[list[tuple[int, str]], str]:
    """``([(qty, name)], last_updated)`` for the deck at this URL."""
    request = urllib.request.Request(f"{API}/{deck_id(source)}", headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            deck = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        raise MoxfieldUnavailable(f"Moxfield unreachable: {error}") from error

    entries = [
        (entry["quantity"], entry["card"]["name"])
        for board in BOARDS
        for entry in deck["boards"].get(board, {}).get("cards", {}).values()
    ]
    if not entries:
        raise MoxfieldUnavailable(f"Moxfield returned no cards for {source}")
    return entries, deck.get("lastUpdatedAtUtc", "unknown")
