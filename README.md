# deck_builder

Turns a plain Commander deck list into a full card reference an agent can reason
over — every card's mana cost, type line, oracle text, power/toughness, keywords,
colour identity, EDHREC rank and price.

## Layout

```
decks/<deck>/base.txt     the deck list you maintain  (`<qty> <name>` per line)
decks/<deck>/meta.json    what the deck is FOR -- commander, bracket, budget, house rules
decks/<deck>/cards.md     generated -- the reference sheet an agent reads
decks/<deck>/cards.json   generated -- the same data, machine-readable
decks/<deck>/reviews/     saved card reviews, one per date
data/cache/scryfall/      one raw Scryfall payload per card; a re-run is free
scripts/build_card_details.py
scripts/scryfall.py
scripts/deck_meta.py      read/write meta.json
scripts/card_facts.py     live Scryfall lookup and search
scripts/edhrec.py         inclusion % and synergy from EDHREC
scripts/combos.py         combos the deck assembles, via Commander Spellbook
.claude/skills/mtg-deck-advisor/
```

`decks/<deck>.txt` (a loose file, no folder) also works — the generated files go
into `decks/<deck>/`.

## Building

```
python scripts/build_card_details.py                  # every deck
python scripts/build_card_details.py markov_chains    # one deck
python scripts/build_card_details.py --refresh        # ignore the cache, re-pull
```

Stdlib only, no venv needed. The first run makes two requests to Scryfall's
`/cards/collection` endpoint per 150 cards, plus one lookup per double-faced card
the deck list spells with a single slash (`Front / Back`). Every card is cached
under `data/cache/scryfall/`, so later runs hit the network only for cards you
added. Exit code is `2` if any name failed to resolve; the unresolved names are
listed at the top of `cards.md` as well.

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
Commander Spellbook, and every price is fetched live in that session. It never
edits `base.txt` — it writes a dated review to `decks/<deck>/reviews/` and leaves
the decklist to you.

It needs `decks/<deck>/meta.json`, because "is this card good" has no answer
without a power target and a pod:

```json
{
  "commander": ["Edgar Markov"],
  "format": "commander",
  "bracket": 3,
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
