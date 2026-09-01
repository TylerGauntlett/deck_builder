# Sheoldred, Whispering One — markov_chains

**Date:** 2026-09-01
**Status: BLOCKED — no verdict issued.** Scryfall, EDHREC and Commander Spellbook
are all unreachable from this session. The candidate could not be verified, and
this skill's first rule is that a card's text, cost, colour identity, legality and
price are never stated from memory. So there is no ADD, ADD IF or NO here.

---

## 1. What blocked it

All three data sources are denied at the egress proxy — not a script bug, not a
rate limit, not a Scryfall `User-Agent` problem:

| Host | Result |
|---|---|
| `api.scryfall.com` | `Tunnel connection failed: 403 Forbidden` |
| `json.edhrec.com` / `edhrec.com` | `Tunnel connection failed: 403 Forbidden` |
| `backend.commanderspellbook.com` | 403 |

Proxy status endpoint recorded the denial explicitly:

```
"recentRelayFailures": [{ "kind": "connect_rejected",
  "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host": "api.scryfall.com:443" }]
```

`WebFetch` against Scryfall returns `EGRESS_BLOCKED` for the same domain. The
proxy README states that 403/407 denials are organization egress policy and must
be reported rather than retried or routed around, so no workaround was attempted.

**`Sheoldred, Whispering One` is not in the local cache.** `data/cache/scryfall/`
holds 220 cards, all previously-fetched deck members; the candidate is absent, so
there is no offline fallback for it.

Everything below therefore comes from `decks/markov_chains/cards.json`, which is
Scryfall-derived data fetched by `build_card_details.py` in an earlier session.
Oracle text, mana costs and type lines from it are quoted freely — those are
stable. **No price is quoted anywhere in this document**, because the cache never
expires and a stale dollar figure is exactly what the skill forbids.

## 2. Premise check — this is the finding worth keeping

`meta.json` describes the deck as "Vampire aggro into aristocrats: go wide with
tokens and lords, then convert the board into drain," in 4-player casual pods. It
makes no explicit claim about game length.

Asked directly, the user reports:

- **Games usually run turns 10–13.**
- **Opponents are other creature decks.**

This matters more than it looks. A 10–13 turn clock means the deck's second mode —
grind and drain — is doing real work in most games, and that expensive top-end
cards actually get cast rather than rotting in hand. Any future review of this
candidate that rejects it as "too slow for an aggro deck" would be evaluating a
premise the user has now contradicted, not evaluating the card. Recorded here so
that reasoning is not available to a later session by default.

Creature-heavy opponents is the second half: it means effects keyed to creatures
dying — on *any* board, not just yours — have more surface area here than the
`meta.json` archetype line implies.

## 3. Deck model (verified, network-independent)

Composition from `cards.json` `stats`:

- 100 cards, 91 distinct, **35 lands**, avg nonland mana value **2.85**
- Types: Creature 38 · Land 35 · Instant 10 · Artifact 8 · Enchantment 4 ·
  Sorcery 4 · Planeswalker 1
- Coloured pips: **B 63 · W 15 · R 5** — overwhelmingly black
- Game Changers: **1** (`Teferi's Protection`) — bracket 3 allows up to 3

### Curve (nonland)

| MV | Count |
|---|---|
| 1 | 12 |
| 2 | 15 |
| 3 | 17 |
| 4 | 12 |
| 5 | 5 |
| 6 | 3 |
| 7+ | **0** |

**The nonland curve tops out at 6, and only three cards are there:**
`Edgar Markov` (the commander, so only two sit in the 99), `Patron of the Vein`,
`Vein Ripper`. Eight nonland cards total at MV 5+.

This is the single most important number for the candidate. Any 7-drop would
become the most expensive card in the deck and would have to beat one of two
on-theme six-mana Vampires that each serve both of the deck's modes:

> **Patron of the Vein** {4}{B}{B} — "Flying / When this creature enters, destroy
> target creature an opponent controls. / Whenever a creature an opponent controls
> dies, exile it and put a +1/+1 counter on each Vampire you control."

> **Vein Ripper** {3}{B}{B}{B} — "Flying / Ward—Sacrifice a creature. / Whenever a
> creature dies, target opponent loses 2 life and you gain 2 life."

Both are removal-plus-payoff, both scale with the wide board, both are Vampires
for the lord effects. That is a high bar, and it is the bar — not "is this card
good" — that the candidate has to clear.

### Death triggers, grouped by scope

The skill requires these be separated rather than totalled, because "yours" and
"any" are different cards:

**"a creature *you control* dies" — 4**
- `Bastion of Remembrance` — "Whenever a creature you control dies, each opponent loses 1 life and you gain 1 life."
- `Cruel Celebrant` — "Whenever this creature or another creature or planeswalker you control dies, each opponent loses 1 life and you gain 1 life."
- `Grave Pact` — "Whenever a creature you control dies, each other player sacrifices a creature of their choice."
- `Zulaport Cutthroat` — "Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life."

**"*a creature* dies" / any board — 5**
- `Blood Artist` — "Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life."
- `Cordial Vampire` — "Whenever this creature or another creature dies, put a +1/+1 counter on each Vampire you control."
- `Vein Ripper` — "Whenever a creature dies, target opponent loses 2 life and you gain 2 life."
- `Elenda, the Dusk Rose` — "Whenever another creature dies, put a +1/+1 counter on Elenda."
- `High-Society Hunter` — "Whenever another nontoken creature dies, draw a card."
- (`Patron of the Vein` is opponent-only: "Whenever a creature an opponent controls dies…")
- (`Blade of the Bloodchief` is any-board but equipment-gated: "Whenever a creature dies, put a +1/+1 counter on equipped creature.")

Against creature decks, the any-board group is where the deck's real reach lives.

### Role counts

- **Sac outlets: 9** — `Viscera Seer`, `Carrion Feeder`, `Bloodthrone Vampire`,
  `Indulgent Aristocrat`, `Village Rites`, `Master of Dark Rites`,
  `Baron Bertram Graywater`, `High-Society Hunter`, `Vein Ripper` (ward only).
  Deep. A card that only adds a sac outlet is redundant here.
- **Recursion: 4** — `Bloodghast`, `Edgar, Charmed Groom`, `Malakir Rebirth`,
  `Qarsi Revenant`. **Thin**, and all four recur *themselves* — the deck has no
  card that returns an arbitrary creature from the graveyard.
- **Card draw: 12**, **Tutors: 1** (`Forerunner of the Legion`, top-of-library
  only — consistent with the "no tutor-dependent win line" constraint).
- **Ramp:** `Sol Ring`, three Talismans, `Arcane Signet`, `Dark Ritual`,
  `Master of Dark Rites`. Modest; nothing that ramps to seven.

### The bridge between the two modes

Cards that convert go-wide output into drain, or deaths into board growth:

- Deaths → counters on the whole team: `Cordial Vampire`, `Indulgent Aristocrat`,
  `Patron of the Vein`
- Deaths → drain: `Blood Artist`, `Zulaport Cutthroat`, `Cruel Celebrant`,
  `Bastion of Remembrance`, `Vein Ripper`
- Tokens → damage: `Mirkwood Bats` ("Whenever you create or sacrifice a token,
  each opponent loses 1 life"), `Impact Tremors`
- Lifegain → drain: `Vito, Thorn of the Dusk Rose`, `Marauding Blight-Priest`,
  with `Bloodthirsty Conqueror` looping the two together

The deck genuinely has two modes and is well bridged. A candidate should be scored
against **both**, not just the aggro line named first in `meta.json`.

## 4. Gaps worth a counter-proposal later

From the counts above, the thin categories are **recursion** (4, all self-recursive)
and **top end** (2 cards in the 99 above MV 4). The deep ones — sac outlets, drain
triggers, two-mana lords — do not need help.

## 5. What would settle it

One of:

1. Egress policy allowing `api.scryfall.com` (plus `json.edhrec.com` and
   `backend.commanderspellbook.com` for steps 4), then re-run:
   ```
   python scripts/card_facts.py lookup "Sheoldred, Whispering One" --deck markov_chains --rulings
   python scripts/edhrec.py card "Sheoldred, Whispering One" --deck markov_chains
   python scripts/combos.py markov_chains --add "Sheoldred, Whispering One" --near
   ```
2. Or the user pasting the Scryfall page contents for the card.

## 6. Open question for the user

The 2026-08-31 Teferi's Protection review recorded the Moxfield maybeboard as:
*Carmen, Cruel Skymarcher · **Sheoldred, the Apocalypse** · Cover of Darkness*.

That is a **different card** from `Sheoldred, Whispering One`. Both are blocked
equally, but they are not interchangeable and the eventual verdict differs. Worth
confirming which one is actually under consideration before the re-run.

## 7. Sources

- `decks/markov_chains/cards.json` (Scryfall-derived, built in a prior session) —
  composition, curve, pips, oracle text, type lines.
- `decks/markov_chains/meta.json` via `deck_meta.py show`.
- User, this session: pod games run turns 10–13; opponents are creature decks.
- Live Scryfall / EDHREC / Commander Spellbook: **unavailable**, 403 at the egress
  proxy. No prices, inclusion percentages or combo data are quoted in this
  document, because none were fetched.
