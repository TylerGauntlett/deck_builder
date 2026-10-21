# Bristly Bill, Spine Sower / Dancing from Dark to Dawn — lander_commander

Deck: Aesi, Tyrant of Gyre Strait. Bracket 3, $40/card cap, 4-player casual.
Pod premise carried over from the 2026-08-31 weakness audit (asked, not assumed):
games run **turns 9–12**; opponents are combo, go-wide, mill, aristocrats.
All oracle text and prices fetched **2026-10-21 07:37 UTC** via `card_facts.py lookup`.

Note: the second card was asked as "Dancing from dawn to dusk"; Scryfall resolved it
to **Dancing from Dark to Dawn**. If you meant a different card, say so.

## Verified text

> **Bristly Bill, Spine Sower** {1}{G} — Legendary Creature — Plant Druid 2/2
> Landfall — Whenever a land you control enters, put a +1/+1 counter on target creature.
> {3}{G}{G}: Double the number of +1/+1 counters on each creature you control.

Legal, G, not a Game Changer. EDHREC rank 918. **$32.96** (2026-10-21 07:37 UTC).

> **Dancing from Dark to Dawn** {3}{G}{G} — Enchantment
> Whenever you cast a creature spell, put X +1/+1 counters on target creature you
> control, where X is that spell's mana value.
> Landfall — Whenever a land you control enters, create a 2/2 green Bear creature token.

Legal, G, not a Game Changer. EDHREC rank 6377. **$6.12** (2026-10-21 07:37 UTC).

## Deck model (from cards.json, script output)

- Landfall payoffs (non-land): **11** — Aesi, Avenger of Zendikar, Greensleeves,
  Lotus Cobra, Mossborn Hydra, Rampaging Baloths, Scute Swarm, Springheart Nantuko,
  Tatyova, Tireless Provisioner, Zendikar's Roil.
- Of those, **token-makers on landfall: 6** — Avenger (plants on ETB, counters on
  landfall), Greensleeves, Rampaging Baloths, Scute Swarm, Springheart Nantuko,
  Zendikar's Roil.
- Cards that put **+1/+1 counters**: **3** — Avenger of Zendikar (on Plants only),
  Goldvein Hydra (enters with X), Mossborn Hydra (enters with 1, doubles its own).
- Counter doublers / proliferate: **1** — Mossborn Hydra (self only).
- Creatures: 29 (incl. Aesi). Curve of nonlands: MV1 5, MV2 16, MV3 15, MV4 2,
  MV5 6, MV6 4, MV7+ 8.
- Unchanged holes from the audit: interaction, graveyard hate, mass answers. Neither
  candidate touches them.

## Dancing from Dark to Dawn — ADD, replacing Zendikar's Roil

**Best case:** it is Zendikar's Roil with a second ability. Write both as
effect × frequency × duration:

| | Cost | Landfall clause | Extra |
|---|---|---|---|
| Zendikar's Roil | {3}{G}{G} enchantment | "create a 2/2 green Elemental creature token" | — |
| Dancing from Dark to Dawn | {3}{G}{G} enchantment | "create a 2/2 green Bear creature token" | X counters per creature spell cast |

Same cost, same card type, same landfall output, same permanence. The difference is
pure upside: **"Whenever you cast a creature spell"** — your spells only, targeted,
"target creature **you control**". The deck has 28 creatures in the 99, and casting
Aesi from the command zone counts (6 counters). Late-game casts are big: Craterhoof,
Terastodon, Koma, Avenger are all MV 7–8.

**Tests:**
- Redundancy: it *is* the redundant card — but it supersedes Roil rather than
  joining it, so the token-landfall count stays at 6.
- Combos: `combos.py --add` reports one new line, **Kodama of the East Tree + Simic
  Growth Chamber + Dancing**. The baseline already contains the identical template
  with Zendikar's Roil ([1479-1671-4677]) and four other payoffs. Swapping
  Roil out leaves the combo count at 6. Bracket-neutral.
- Anti-synergy: none found. Bears have no tribal relevance here; no downside to the
  counters.
- Worst case: identical to Roil's — a 5-mana enchantment that does nothing until
  the next land. Not worse in any draw.
- EDHREC: low adoption (rank 6377; not in Aesi's top commanders; mostly Bear
  decks). The disagreement is explained: it is a 2026 card, and in a deck already
  running Roil it is a strict upgrade, which inclusion % cannot show.
- Price: $6.12. Not part of the argument — the verdict would be the same if it cost
  nothing or $40.

**Consistency with the 2026-08-31 audit:** that review recommended cutting Roil for
**Scavenging Ooze**, because the token-landfall lane is over-served and the deck
has no graveyard interaction. That reasoning still holds and is **not** overturned by
this card — Dancing does the same job in the same over-served lane. So:
- If Roil is still in the deck (it is, per `base.txt` today): **swap Roil →
  Dancing.** Strict upgrade.
- If you are applying the audit's Roil → Scavenging Ooze swap: keep the Ooze. Dancing
  does not earn a slot of its own, and the audit already found no eighth cut.

## Bristly Bill, Spine Sower — NO

**Best case:** a 2-mana landfall payoff that comes down early, gets a counter on
something every land drop (two with Aesi's extra drop), and then becomes a repeatable
late-game mana sink: {3}{G}{G} to double the counters on every creature you control.
With an Avenger plant board, that is a second Craterhoof — and in 9–12-turn games the
deck has the spare mana to activate it.

**What killed it:**
- **Density.** Bill's second ability, the one that multiplies, needs counters
  already on your creatures. Cards that add them: **3** (Avenger — Plants only;
  Goldvein Hydra; Mossborn Hydra), plus Bill's own one-per-land trickle. That is
  far below the roughly one-third of the deck a support-hungry card needs. The
  deck's tokens — Badgers, Beasts, Insects, Elementals, Scute copies — come in with no
  counters. Bill doubles 0 on most of the board.
- **Marginal impact.** The scenario where Bill is strong (Avenger resolved, lots of
  mana) is already a game-winning board. Avenger plus landfall already pumps every
  Plant, and Craterhoof, Overwhelming Stampede and Finale of Devastation are the
  existing finishers. Bill makes winning boards win harder. It does nothing about the
  combo, mill and aristocrats decks the audit found this deck losing to.
- **Without Avenger,** the landfall clause adds one counter to one creature per land.
  It is additive, in an 11-deep landfall lane the audit already called over-served.
- **Fragility.** A legendary 2/2 for 2 that dies to any sweeper and is the first
  thing aristocrats or go-wide boards trade with.
- **No cut.** The early landfall creatures are Lotus Cobra (MV2), Springheart
  Nantuko (MV2) and Scute Swarm (MV3). Each one does its job without needing support.
- Combos: `combos.py --add` → 0 new. Not a Game Changer. Bracket-neutral.
- EDHREC: 14.3% of Aesi decks (2481/17355). Its strong adoption is in
  counters-first commanders (Tifa 46.4%, Toph Earthbending Master 48.8%, Agatha
  40.9%). That is the difference: those decks are built around counters. This one
  is built around tokens and cards drawn.
- Price: $32.96 (2026-10-21 07:37 UTC), under the cap. **The rejection survives the
  card being free.**

**What would change it:** a real +1/+1 counter package in the deck — Hardened
Scales-style doublers and several counter-entering creatures. That is a re-theme,
not a one-card add.

## Summary

| Card | Verdict | Cut | Price (2026-10-21 07:37 UTC) |
|---|---|---|---|
| Dancing from Dark to Dawn | **ADD** | Zendikar's Roil (strict upgrade) | $6.12 |
| Bristly Bill, Spine Sower | **NO** | — | $32.96 |

Role counts after the swap: token-landfall payoffs 6 → 6, combos 6 → 6, Game
Changers 2 → 2, curve unchanged (MV5 ↔ MV5). `base.txt` not modified.
