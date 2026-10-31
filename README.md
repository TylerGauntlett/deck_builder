# mtg-deck-builder

Pulls a Commander deck's current list from Moxfield and turns it into a full card
reference an agent can reason over — every card's mana cost, type line, oracle text,
power/toughness, keywords, colour identity, EDHREC rank and price.

## Layout

```
decks/<deck>/meta.json    what the deck is FOR -- commander, bracket, budget, house
                          rules -- and its Moxfield URL (`source`)
decks/<deck>/cards.json   generated -- the last synced list with full card data
decks/<deck>/cards.md     generated, gitignored -- the same data, for reading
decks/<deck>/reviews/     saved card reviews, one per date
data/cache/scryfall/      one raw Scryfall payload per card; a re-run is free
scripts/build_card_details.py
scripts/moxfield.py       the current list from Moxfield
scripts/scryfall.py
scripts/deck_meta.py      read/write meta.json
scripts/card_facts.py     live Scryfall lookup and search
scripts/edhrec.py         inclusion % and synergy from EDHREC
scripts/combos.py         combos the deck assembles, via Commander Spellbook
.claude/skills/mtg-deck-advisor/
```

The decklist lives on Moxfield and is edited there; nothing in this repo is a second
copy to maintain.

## Building

```
python scripts/build_card_details.py                  # every deck
python scripts/build_card_details.py markov_chains    # one deck
python scripts/build_card_details.py --refresh        # ignore the cache, re-pull
```

Stdlib only, no venv needed. Each run makes one request to Moxfield for the list.
The first run also makes two requests to Scryfall's `/cards/collection` endpoint per
150 cards. Every card is cached under `data/cache/scryfall/`, so later runs hit
Scryfall only for cards you added. Exit code is `2` if any name failed to resolve;
the unresolved names are listed at the top of `cards.md` as well. Exit code is `3`
if Moxfield couldn't be reached, in which case `cards.md` is rendered from the last
`cards.json` with a staleness warning at the top.

## Using the sheet

`decks/<deck>/cards.md` is the file to hand an agent asking for swap
recommendations, weak-synergy calls, or a curve/mana-base review. It opens with a
deck-at-a-glance block (card and land counts, average mana value, type spread,
coloured pip counts, Scryfall's Game Changer flags), then lists every card —
spells first, lands last, each face of a double-faced card printed separately.

`cards.json` carries the same fields plus `oracle_id`, `layout`, `produced_mana`,
`all_parts` (tokens and meld halves) and `scryfall_uri` for anything that wants to
filter rather than read.

## Judging new cards

`.claude/skills/mtg-deck-advisor/` is a skill that takes a deck plus some cards
you're considering and tells you whether they're actually worth a slot. It defaults
to **no** and makes the card earn it: every fact is refetched from Scryfall rather
than recalled, community numbers come from EDHREC, combo claims are checked against
Commander Spellbook, and every price is fetched live in that session. It works on
`main`: it syncs the list from Moxfield first, writes a dated review to
`decks/<deck>/reviews/`, and commits and pushes straight to `main` with no branch or
pull request. It never changes the decklist; you apply swaps on Moxfield.

It needs `decks/<deck>/meta.json`, because "is this card good" has no answer
without a power target and a pod:

```json
{
  "commander": ["Edgar Markov"],
  "format": "commander",
  "bracket": 3,
  "source": "https://moxfield.com/decks/<id>",
  "budget": { "per_card_max_usd": 40 },
  "constraints": ["No early infinite combos."],
  "preferences": ["Prefer on-theme Vampire cards."]
}
```

`constraints` are hard vetoes; `preferences` are tiebreakers only. Start one with
`python scripts/deck_meta.py init <deck>`.

The four scripts also stand alone, and all take `--help`:

```
python scripts/deck_meta.py show markov_chains
python scripts/card_facts.py lookup "Vein Ripper" --deck markov_chains --rulings
python scripts/card_facts.py search 'o:"whenever a creature dies" id<=rwb' --deck markov_chains
python scripts/edhrec.py commander markov_chains --diff
python scripts/combos.py markov_chains --add "Sanguine Bond" --near
```

`card_facts.py lookup` always ignores the cache and refetches, because the cache
under `data/cache/scryfall/` never expires and a stale price is worse than none.
