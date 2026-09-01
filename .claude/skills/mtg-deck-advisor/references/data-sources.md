# The sources, and what each one can't tell you

All three were tested and are reachable from this machine. The scripts wrap them;
this file is for when you need to go past what the scripts expose.

## Scryfall — what a card says

The only authority here. Everything else is opinion.

```
GET https://api.scryfall.com/cards/named?exact=<name>
GET https://api.scryfall.com/cards/search?q=<query>
POST https://api.scryfall.com/cards/collection      # 75 identifiers per request
```

**WebFetch cannot reach Scryfall — it returns 403.** The API requires a real
`User-Agent`. Use `scripts/card_facts.py`, or `curl` with a `User-Agent` header.
`scripts/scryfall.py` already sets one and paces requests at 100 ms.

Fields that matter: `oracle_text` (per `card_faces` on a DFC), `type_line`,
`mana_cost`, `cmc`, `color_identity`, `legalities.commander`, `game_changer`,
`edhrec_rank`, `prices`, `rulings_uri`, `all_parts`.

**Cannot tell you:** whether a card is good, or good *here*. It also can't tell you
today's price from yesterday's fetch — see below.

### Prices

`prices.usd` is a recent market snapshot from one marketplace, in USD, for the
printing Scryfall returned — not the cheapest printing, not your local shop, not
what you'd actually pay. It moves daily.

**The local cache never expires.** `data/cache/scryfall/` is fetch-once by design;
a price in `cards.md` may be a year old. `card_facts.py lookup` always passes
`refresh=True`, so use it for every dollar figure, quote the timestamp it prints,
and never round from memory — not even for a ballpark.

## EDHREC — what people play

```
GET https://json.edhrec.com/pages/commanders/<slug>.json
GET https://json.edhrec.com/pages/commanders/<slug>/<theme>.json
GET https://json.edhrec.com/pages/cards/<slug>.json
```

Reachable via plain GET, no key. The commander page is ~100 KB — `scripts/edhrec.py`
reduces it; don't fetch it raw into context.

Shape: `container.json_dict.cardlists[]` → `{header, tag, cardviews[]}`. Tags seen
in practice: `highsynergycards`, `topcards`, `gamechangers`, `newcards`,
`creatures`, `instants`, `sorceries`, `enchantments`, `utilityartifacts`,
`manaartifacts`, `utilitylands`, `lands`; card pages add `topcommanders` and
`highliftcards`.

Each cardview: `name`, `sanitized`, `slug`, `url`, `synergy`, `num_decks`,
`potential_decks`, `trend_zscore`. **Inclusion % = `num_decks / potential_decks`.**
Also top-level `bracket_counts`, `budget_counts`, `similar`, and
`panels.taglinks` (the archetype themes, ordered by popularity).

Slugs fold accents and drop punctuation: `Clavileño, First of the Blessed` →
`clavileno-first-of-the-blessed`. This is **not** the same rule as
`scryfall.slugify`, which leaves the accent as a separator.

**Cannot tell you** whether a card is good. Inclusion % measures popularity, which
tracks price, precon printings, brand recognition and age at least as much as
power. A card in 80% of decks may be there because it came in the precon. A card
in 4% may be a genuine gem or may be bad. Treat a large gap between your reasoning
and the inclusion % as a prompt to find out which of the two is wrong — not as a
verdict.

It also can't tell you about *this* deck. The numbers average over every registered
list at every power level, most of them worse than a tuned one.

## Commander Spellbook — what combos exist

```
POST https://backend.commanderspellbook.com/find-my-combos/
     {"commanders": [{"card": "..."}], "main": [{"card": "..."}]}
GET  https://backend.commanderspellbook.com/variants/?q=card%3A%22<name>%22
```

Response: `results.included` (combos the deck assembles), `results.almostIncluded`
(missing one or more pieces), `results.identity`. Each variant has `id`, `uses[]`
(`.card.name`), `produces[]` (`.feature.name`).

`scripts/combos.py --add` runs the deck twice and diffs, so a claim that a card
enables a combo is checkable rather than remembered.

**Cannot tell you** whether the deck *wants* the combo. It lists what's
mechanically possible. A deck whose `meta.json` bars early infinites wants this
output as a warning, not a selling point. It also doesn't weigh how hard the pieces
are to assemble, or whether the loop actually wins on the spot — read `produces`
and check that the deck can convert it.

## Rate limits and manners

Scryfall asks for 50–100 ms between requests; `scryfall.py` uses `DELAY = 0.1` and
a descriptive `User-Agent`, and all four scripts reuse both. EDHREC and Spellbook
publish no limits — the same pacing applies. Batch through
`/cards/collection` (75 per POST) rather than looping over `/cards/named`.
