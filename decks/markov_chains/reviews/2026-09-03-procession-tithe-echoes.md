# markov_chains — Anointed Procession, Smothering Tithe, Mana Echoes — 2026-09-03

Deck context: Edgar Markov, bracket 3, $40/card cap, 4-player casual pods.
Pod facts carried forward from the 2026-08-30 addendum (user-supplied, not
`meta.json`): **games routinely run long**, **several opponents play mono-white**,
**Farewell is commonly played**. `meta.json` still says "vampire aggro"; that line
is stale and I am not evaluating against it.

## The cards, verified

All three fetched live 2026-09-03 21:53 UTC. All three are MV 4. All three are
legal and inside Edgar's `BRW` identity.

| Card | Cost | EDHREC rank | Edgar inclusion | Synergy | Price |
|---|---|---|---|---|---|
| Anointed Procession | `{3}{W}` | 366 | 13,489 / 50,203 = **26.9%** | — | $59.52 |
| Smothering Tithe | `{3}{W}` | 65 | 11,713 / 50,203 = **23.3%** | **−0.01** | $61.52 |
| Mana Echoes | `{2}{R}{R}` | 4017 | 543 / 50,203 = **1.1%** | — | $55.75 |

> **Anointed Procession** — *If an effect would create one or more tokens under
> your control, it creates twice that many of those tokens instead.*
>
> **Smothering Tithe** — *Whenever an opponent draws a card, that player may pay
> {2}. If the player doesn't, you create a Treasure token.* **Game Changer: yes.**
>
> **Mana Echoes** — *Whenever a creature enters, you may add an amount of {C}
> equal to the number of creatures you control that share a creature type with it.*

Combos newly completed, checked against Commander Spellbook (baseline 2):
**Procession 0, Mana Echoes 0.** The no-early-infinites veto is not engaged by any
of the three.

Bracket: the deck runs **1** Game Changer (Teferi's Protection). Grave Pact and
Vein Ripper are *not* Game Changers — I checked rather than assumed. Tithe would
make 2 of the 3 allowed at bracket 3, so bracket is not a veto for it.

**Budget applies to all three.** $59.52 / $61.52 / $55.75 against a $40 cap. Per
the rubric that is a flagged veto the user may override, not a silent one. It is
recorded here on its own line and is not used as an argument anywhere below.

---

## Mana Echoes — NO

**Step 0, honest best case.** This is a Vampire tribal deck with 34 Vampire spells
in the 99 and an eminence trigger that makes a Vampire token every time one is
cast. Casting a Vampire into a board of six Vampires triggers Mana Echoes twice —
once for the eminence token, once for the creature — for something like 13
colorless mana off one card. No other card in the deck approaches that rate.

**What killed it — three independent failures, any one sufficient.**

**1. There is nothing to spend the mana on.** I searched the whole list for sinks:

- `{X}` costs anywhere in the 99: **zero**.
- Repeatable generic-cost activated abilities: **Indulgent Aristocrat** (`{2}`,
  *sacrifice a creature* — consumes board, not a sink), **War Room** (`{3}`, `{T}`
  — once per turn), **Voldaren Estate** (`{5}`, `{T}` — once per turn).

There is no untapped, repeatable outlet. A burst of 13 colorless arrives and
drains away.

**2. The mana it makes is the wrong colour.** Colored pips are **B 63 · W 15 · R 5**.
Mana Echoes adds `{C}`. Against `{1}{B}{B}{B}` Bloodletter of Aclazotz, `{1}{B}{B}{B}`
Grave Pact, `{1}{B}{B}{B}` Vampire Nocturnus and `{3}{B}{B}{B}` Vein Ripper, it pays
the generic digit and nothing else. The deck's constraint is coloured sources, and
this card does not produce colour.

**3. It is barely castable itself.** `{2}{R}{R}` — a double-red pip in a deck with
**5 red pips total** and **19 red sources** (16 lands including the
opponent-dependent Exotic Orchard, plus Arcane Signet and two Talismans). That is
around the floor for a *single* red pip and well under it for a double. It would
raise the deck's red demand by 40% for one card.

**Disagreement check.** I say no; the community says no far harder than I do —
**1.1%** of Edgar decks, 543 of 50,203. Mana Echoes' actual homes are Krenko
(17.0%) and Sliver Overlord (32.9%), decks with mana sinks and mono/near-mono mana.
Nothing here is a case where I see something 50,000 decks missed.

**The rejection survives the card being free.** Price is not doing any work.

**NO** — it makes colourless mana in a deck with 63 black pips and zero `{X}` sinks,
and `{R}{R}` is barely castable off 19 red sources.

---

## Smothering Tithe — NO

**Step 0, honest best case.** In a four-player pod with long games, three opponents
each draw at minimum one card per round. Untaxed, that is three Treasures per
turn cycle, compounding. Treasures also fix colour, and the structural audit
already flagged the deck's four `BBB` costs as its mana-base pressure point. It is
a Game Changer and the deck has room for two more.

**What killed it.**

**1. Its EDHREC synergy in Edgar is −0.01.** This is the cleanest number in the
review. 23.3% of Edgar decks run it — and that is *exactly* the rate any white deck
runs it. Edgar contributes nothing to Smothering Tithe and Smothering Tithe
contributes nothing to Edgar. It is on the list because it is a good Magic card,
which is precisely the argument the rubric says does not clear the bar.

**2. It touches no part of the deck's plan.** It is not a Vampire, so it does not
trigger eminence. It is not a body. It creates Treasure tokens — artifacts, not
creatures — so it feeds **Impact Tremors** (*"whenever a creature you control
enters"*) not at all, and of the ten event-counting drain payoffs it feeds only
**Mirkwood Bats** (*"whenever you create or sacrifice a token"* — Treasures are
tokens). One payoff, incidentally.

**3. Ramp is not a thin category.** Sol Ring, Arcane Signet, three Talismans, Dark
Ritual, Master of Dark Rites, plus Herald's Horn as a cost reducer, against 35
lands and an average nonland MV of 2.85. The deck is not mana-starved. The rubric's
redundancy test asks what already does this job; eight things do.

**4. The pod fact cuts against it specifically.** Several opponents play
mono-white. Smothering Tithe's rate is a direct function of how much the table
draws, and mono-white is historically the lowest-draw archetype. This is the one
point I am genuinely unsure of — modern mono-white commanders do draw — and it is
listed under open questions below.

**Marginal impact.** It does not improve a bad draw, does not rebuild after a wipe,
and does not close a game. It makes a developed board develop faster.

**The rejection survives the card being free.** If you already own it, it is still
a zero-synergy mana engine in a deck that is not short of mana. Price changes
nothing here.

**Counter-proposal: none, because the role is not real.** The rubric asks for one
when the role is genuine and the card is wrong. Ramp is not a gap in this deck. The
gap the structural audit found — **zero board recovery** — is still open, and
Smothering Tithe is not aimed at it.

**NO** — zero Edgar synergy (−0.01), feeds one of ten drain payoffs, and ramp is
already eight cards deep.

---

## Anointed Procession — ADD

**Step 0, honest best case, as a claim that could be false.** *Edgar's eminence
triggers from the command zone, so every one of the deck's 34 Vampire spells is
already a token-maker in every game with no setup; Anointed Procession doubles
that source plus seven others, and the deck's ten event-counting drain payoffs
convert extra bodies into damage without needing combat — which matters because
the deck has zero trample and combat conversion is its known bottleneck.*

**The nine token sources, verified from `cards.json`:**

| Source | Trigger | Doubled? |
|---|---|---|
| Edgar Markov | eminence — *whenever you cast another Vampire spell*, from the command zone | yes, 34 times over |
| Edgar, Charmed Groom | each upkeep | yes |
| Bloodline Keeper | `{T}`, repeatable | yes |
| Elenda, the Dusk Rose | dies — X tokens where X is her power | yes |
| Clavileño, First of the Blessed | granted death trigger, 4/3 flier | yes |
| Charismatic Conqueror | opponent's untapped permanent enters | yes |
| Bastion of Remembrance | ETB, one-shot | yes |
| Voldaren Estate | `{T}`, Blood token | yes |
| Baron Bertram Graywater | *"one or more tokens... **This ability triggers only once each turn**"* | **no** — batched, not doubled |

That last row is the honest limit and I am reporting it rather than letting the
count read as nine clean multipliers. It is eight.

**Why the output converts.** Extra 1/1 Vampire tokens are not just bodies here:

- **Impact Tremors** — *"Whenever a creature you control enters, this enchantment
  deals 1 damage to each opponent."* Ruling [2024-11-08] confirms it triggers once
  per creature, so doubled tokens are doubled damage.
- **Mirkwood Bats** — *"Whenever you create or sacrifice a token, each opponent
  loses 1 life."* Note the wording is *"a token"*, not the batching *"one or more
  tokens"* that Baron Bertram uses; on the standard reading it triggers per token,
  so it doubles too. Flagging this as a textual reading — Scryfall lists **no
  official rulings** on this card, and it is the one interaction below that I
  cannot point to a ruling for.
- **Edgar's attack trigger** — *"put a +1/+1 counter on each Vampire you control"* —
  twice as many recipients.
- **Skullclamp** on 1/1 tokens: more bodies, more draw, and each death feeds the
  drain payoffs.

That is four named payoffs, past the three-card bar.

**Why this is not Door of Destinies.** I rejected Door on 2026-08-31, and the
distinction matters or this review contradicts itself. Door was the *seventh anthem*
into a six-deep category, and it failed specifically because *"the counters come
from casting, and the deck's main Vampire source isn't cast."* Anointed Procession
attacks that exact clause from the other side: it is the card that scales with the
tokens Door could not see. Door was additive into the deck's deepest category;
Procession is multiplicative on its engine. The rubric's own closing filter — *"prefer
the card that multiplies what it already does over the card that adds one more of
something"* — points opposite ways for the two cards.

**Density.** Not a concern, and this is the strongest structural point. Edgar sits
in the **command zone**, so the primary enabler is available in 100% of games from
turn zero, with 34 Vampire spells to trigger it. Procession is a blank only in a
draw where you cast no Vampires, which is a draw you were losing anyway.

**What it does not do — the honest weaknesses.**

1. **It changes nothing the turn it resolves.** Four mana, no board.
2. **It is a blank after a wipe**, and Farewell — common in this pod — exiles
   enchantments, so it does not even survive to rebuild. The deck's identified hole
   is board recovery and Procession does not address it.
3. It is the **13th card at MV 4**, the deck's most contested slot (curve
   12/15/17/**12**/5/3).

I weighed these and they do not sink it, because the long-game pod premise — which
is user-supplied, not `meta.json`'s — is exactly the condition under which a
compounding enchantment gets to compound. Under the stale "aggro, game over by turn
nine" premise I would have rejected it, and that would have been failure mode #1
repeating.

**Disagreement check.** I say yes, the community says yes: **26.9%** of Edgar decks,
and **Edgar Markov is Anointed Procession's single largest home by raw deck count**
(13,489 decks — more than Rin and Seri, Baylen, or any dedicated token commander).
My independent reason is the eight verified sources and four verified payoffs above,
not the percentage.

**ADD** — cut **Anowon, the Ruin Sage**.

---

## The cut

**Anowon, the Ruin Sage** `{3}{B}{B}`, MV 5, $2.67 —
*"At the beginning of your upkeep, each player sacrifices a non-Vampire creature of
their choice."*

Three reasons, all checked this session:

1. **It eats exactly your own best pieces.** I counted the non-Vampire creatures in
   the 99. There are **three**: **Carrion Feeder** (free sac outlet), **Mirkwood
   Bats** (the token-count-to-damage converter the Door review explicitly spared as
   *"the multiplicative token-count-to-damage converter"*), **Zulaport Cutthroat**
   (drain payoff). Plus Bastion of Remembrance's Human Soldier token. Anowon's edict
   is aimed at a pool of three cards, and all three are core aristocrat pieces.
2. **It was an ADD IF whose condition was never confirmed.** The 2026-08-30 addendum
   made it conditional on *"the mono-white decks being few-fat-creature builds rather
   than token swarms."* Against a token swarm each opponent sacrifices a 1/1 and the
   card does nothing. That condition is still unverified — see the open question.
3. **It is opponent-paced.** Grave Pact already fills the edict role and is
   self-paced off ten sac outlets, which the addendum itself identified as the
   distinction that mattered.

**Deltas after Procession in, Anowon out:**

- Curve: 12/15/17/12/**5**/3 → 12/15/17/**13**/**4**/3
- Pips: B 63 · W 15 · R 5 → **B 61 · W 16 · R 5** (slightly eases the four `BBB` costs)
- Vampire spells for eminence: 34 → **33** (a real cost; Procession is not a Vampire)
- Creature count: 38 → 37

### Runners-up, and why each was spared

- **Impact Tremors** — the 2026-08-30 addendum listed it as a cut, and I am
  deliberately not taking it. Procession doubles its triggers, and cutting the card
  the new card multiplies is failure mode #5 from the rubric, by name. Spared, and
  the earlier recommendation is superseded rather than ignored.
- **Lightning Bolt** — weak in a long four-player game as reach, but it is one of
  only six pieces of targeted interaction and the cheapest. Spared on the
  never-cut-below-a-role rule.
- **Qarsi Revenant** — the 2026-08-30 review called it *"NO, but first off the
  bench,"* which makes it a live candidate. Spared over Anowon because deathtouch
  plus lifelink blocks mono-white fatties and Renew is real value in long games,
  where Anowon's edict is conditional on a pod shape we have not confirmed.

If the mono-white decks turn out to be fat-creature builds, **swap the cut to Qarsi
Revenant** and keep Anowon.

---

## Open questions — both resolved 2026-09-03

1. **Are the mono-white decks token swarms or few-fat-creature builds?**
   → **Token swarms.** This closes the ADD IF that was left hanging on
   2026-08-30 and settles it against Anowon: against a token swarm each opponent
   sacrifices a 1/1 every upkeep while you feed it Carrion Feeder, Mirkwood Bats or
   Zulaport Cutthroat. **The cut is Anowon, the Ruin Sage, confirmed.** Qarsi
   Revenant is spared and stays first off the bench.

   This also strengthens Procession independently, which I am noting rather than
   quietly banking: against three go-wide white boards, the deck wins by having the
   wider board *and* by converting it through the drain payoffs, and Grave Pact —
   self-paced off ten sac outlets — is the card that punishes their width. Extra
   token bodies feed both halves of that.

2. **How much do your opponents actually draw?**
   → **About one per turn.** Smothering Tithe is left at its floor: three
   opponents, one draw each per turn cycle, and each may simply pay `{2}`. The
   **NO stands**, now on rate as well as on the −0.01 synergy. Both axes checked;
   neither moves it.

---

## Addendum — pod correction: only one mono-white deck plays tokens

User correction, 2026-09-03: **only 1 of the mono-white decks uses token
creatures**; the others build bigger creatures. My AskUserQuestion offered a
binary — "token swarms" vs "few fat creatures" — and I applied the answer to the
whole pod. That was my error, not a changed answer. Under the corrected
composition the pod is roughly **2 fat-creature decks + 1 token deck**, which is
the "few fat creatures" branch where I had already committed to keeping Anowon.

### Anowon, the Ruin Sage — cut reversed, it stays

The load-bearing objection was *"against a token swarm each opponent sacrifices a
1/1 and the card does nothing."* That now applies to **one** opponent out of three.
Against two decks with few, expensive creatures, an edict **every upkeep** is real
attrition — the rubric's own *effect × frequency × duration* test, which I applied
to Grave Pact and did not apply here.

The self-inflicted cost is also smaller than I framed it. Ruling [2010-03-01]:
*"If a player controls no creatures, or if all creatures a player controls are
Vampires, that player simply doesn't sacrifice anything."* With only three
non-Vampires in the 99 (Carrion Feeder, Mirkwood Bats, Zulaport Cutthroat), you
dodge your own trigger entirely on any turn none of them is out, and you choose
which when one is.

### But the mechanism is not what it was proposed as

The stated reason was *"prevents the others from building any bigger creatures."*
The card does not do that. Verified text: *"each player sacrifices a non-Vampire
creature **of their choice**."* Ruling [2010-03-01] confirms each player picks
their own. A fat-creature deck sacrifices its **worst** creature; the big one is
the last thing to go, not the first. Anowon strips chaff and grinds — it is an
attrition engine, not an answer to a fatty.

The card that does what was wanted is already in the deck: **Soul Shatter**
`{2}{B}` — *"Each opponent sacrifices a creature or planeswalker with the
**greatest mana value** among creatures and planeswalkers they control."*
Non-targeted, so it goes through hexproof and ward, and it takes the biggest thing
rather than the smallest. Keep Anowon for the grind; Soul Shatter is the answer.

### The cut moves to Lightning Bolt

The corrected premise re-ranks all three candidates, and it moves them in
different directions — which is what makes this a re-rank rather than a
contradiction:

- **Anowon** — the correction makes it *better* (2 of 3 opponents now feel the
  edict). Spared.
- **Qarsi Revenant** — I spared it on *"deathtouch plus lifelink blocks mono-white
  fatties."* More fat creatures makes that reason **stronger**, not weaker. A 3/3
  flying deathtouch lifelink blocker trades up with anything they cast. Spared,
  and cutting it now would contradict my own spare reason.
- **Lightning Bolt** — the correction makes it *worse*. Three damage does not
  answer a fat white creature, and as reach in a long four-player game it is
  negligible against 120 combined starting life. It is the one card the new fact
  devalues.

It is not the last of its role: interaction after the cut is **Swords to
Plowshares** (exile any creature), **Anguished Unmaking** (exile any nonland
permanent), **Feed the Swarm** (creature or enchantment), **Soul Shatter**
(greatest MV), **Olivia's Wrath** (*each non-Vampire creature gets -X/-X where X is
your Vampire count* — a one-sided sweeper that gets better as Procession widens the
board), plus Grave Pact as a repeating edict. Five pieces plus an engine remain.

**Revised swap: +1 Anointed Procession, −1 Lightning Bolt.**

- Curve: 12/15/17/12/5/3 → **11**/15/17/**13**/5/3
- Pips: B 63 · W 15 · R 5 → **B 63 · W 16 · R 4** — cutting a red pip in a deck
  with 19 red sources is what Finding 2 of the structural audit asked for
- Vampire spells for eminence: **34, unchanged** (Lightning Bolt is not a Vampire;
  the previous Anowon cut would have dropped it to 33)

This version of the swap is strictly better than the one I proposed first: it keeps
the eminence count intact, improves the colour balance instead of leaving it flat,
and removes a card the pod correction devalued rather than one it upgraded.

## Figures recorded for later comparison

| Item | Value | Source / timestamp |
|---|---|---|
| Anointed Procession price | $59.52 | Scryfall, 2026-09-03 21:53 UTC |
| Smothering Tithe price | $61.52 | Scryfall, 2026-09-03 21:53 UTC |
| Mana Echoes price | $55.75 | Scryfall, 2026-09-03 21:53 UTC |
| Anowon, the Ruin Sage price | $2.67 | Scryfall, 2026-09-03 21:57 UTC |
| Procession, Edgar inclusion | 13,489 / 50,203 = 26.9% | EDHREC `commanders/edgar-markov` |
| Tithe, Edgar inclusion / synergy | 11,713 / 50,203 = 23.3%, synergy −0.01 | EDHREC |
| Mana Echoes, Edgar inclusion | 543 / 50,203 = 1.1% | EDHREC |
| Combos newly completed | 0 for all three (baseline 2) | Commander Spellbook, 2026-09-03 |
| Game Changers in deck | 1 (Teferi's Protection) | Scryfall flag, per-card |
| Token sources in deck | 9 (8 doubled by Procession; Baron Bertram batches) | `cards.json` |
| Non-Vampire creatures in 99 | 3 (Carrion Feeder, Mirkwood Bats, Zulaport Cutthroat) | `cards.json` |
| `{X}` mana sinks in deck | 0 | `cards.json` |
| Red sources | 19 (16 lands incl. Exotic Orchard, 3 rocks) | `cards.json` |
| Nonland curve | 12 / 15 / 17 / 12 / 5 / 3 at MV 1–6 | `cards.json` |
| Coloured pips | B 63 · W 15 · R 5 | `cards.json` |
