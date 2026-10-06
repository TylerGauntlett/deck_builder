# markov_chains — Carmen, Cruel Skymarcher (2026-10-06)

Candidate: **Carmen, Cruel Skymarcher** (owned). User's framing: the deck now
carries several more sacrifice outlets than it did when Carmen was first
considered on 2026-08-30.

Deck context (`meta.json`, updated 2026-09-07): Edgar Markov, bracket 3, $40/card,
4-player casual pods, rotating opponents (no fixed pod description), dual-mode —
Vampire aggro into aristocrats. List: 100 cards, 34 lands, 65 nonland, avg MV
2.88, Game Changers 2/3. `base.txt` matches the 2026-10-02 shape review (none of
that review's four proposed swaps has been made).

All oracle text, legality and prices fetched from Scryfall **2026-10-06 02:24
UTC**. EDHREC figures from `cards/carmen-cruel-skymarcher` and
`commanders/edgar-markov` (n = 51,456). Combos from Commander Spellbook.

**Verdict: ADD — cut Vampire Nocturnus.** Alternate cut: Malakir Bloodwitch.

---

## 1. Why the 2026-08-30 NO does not carry forward

That rejection rested on three legs: (a) "a 2/2 for five that must survive, then
attack ... in a deck whose plan is to have won by then"; (b) stacks into a crowded
MV-5 slot; (c) 16.6% EDHREC inclusion in Edgar versus 76% in Clavileño, read as
"she belongs in grindy sacrifice decks, not the aggro one."

Leg (a) was the fast-aggro premise that the same review later retracted
(Addendums 2 and 6: games run long; the deck is explicitly dual-mode). Leg (c)
is the same premise restated through EDHREC. Only leg (b) survives, and it is
re-tested below. The user withdrew Carmen before the premise was corrected, so
she was never evaluated under the corrected one. This is a re-evaluation on a
**new axis** (the forced-sacrifice engines added since), not a re-argument.

## 2. Verified text

```
Carmen, Cruel Skymarcher  {3}{W}{B}  — Legendary Creature — Vampire Soldier  2/2
Flying
Whenever a player sacrifices a permanent, put a +1/+1 counter on Carmen and you gain 1 life.
Whenever Carmen attacks, return up to one target permanent card with mana value
less than or equal to Carmen's power from your graveyard to the battlefield.
```

Legal, identity WB (inside Mardu), not a Game Changer. Rulings (2023-11-10): if
Carmen's power drops below the target's MV before the attack trigger resolves,
the return fails; sacrificing Carmen herself still fires her own trigger.

Scope of the first trigger, read on the four axes:

| Axis | Reading |
|---|---|
| Whose permanents | **any player's**, and any **permanent** — not "creature", not "you control" |
| Whose turn | any turn |
| Targeted | no — counter and life are untargeted |
| Who chooses | n/a |

This is a different card from Edgar, Ancient Bloodlord's "another creature or
planeswalker **you control** dies": Carmen fires on opponents' sacrifices and on
non-creature sacrifices (Treasure, Blood, fetchlands), and does **not** fire on
deaths that are not sacrifices (combat, removal, wraths).

## 3. What turns her on — counted from `cards.json`

**Sacrifice outlets you control (11):**

| Group | Cards |
|---|---|
| Free, repeatable (3) | Viscera Seer, Carrion Feeder, Bloodthrone Vampire |
| Mana or tap, repeatable (5) | Indulgent Aristocrat ({2}), Edgar, Ancient Bloodlord ({2}), Baron Bertram Graywater ({1}{B}), Master of Dark Rites ({T}), Phyrexian Tower ({T}) |
| Attack-triggered (1) | High-Society Hunter |
| One-shot (2) | Village Rites, Sorin, Imperious Bloodlord (+1) |

**Effects that make opponents sacrifice (5):** Grave Pact ("each other player
sacrifices a creature"), Anowon, the Ruin Sage ("each player sacrifices a
non-Vampire creature" every upkeep), Henrika Domnathi (mode 1, "each player
sacrifices a creature"), Soul Shatter (each opponent), Vein Ripper (ward —
sacrifice a creature).

**Permanents that make sacrificeable tokens (2):** Black Market Connections
(Treasure), Voldaren Estate (Blood).

That is 18 of 99 cards. Against the 2026-08-30 list, the user's premise is
correct on the axis that matters: the count of *your own* outlets is roughly flat
(10 → 11; Falkenrath Pit Fighter and Deadly Dispute out, Edgar AB, Phyrexian Tower
and Sorin in), but the **forced-opponent-sacrifice group went from 0 to 5**.
Grave Pact, Anowon and Henrika were all added after Carmen was withdrawn. Because
her trigger reads "a player", those cards multiply her:

- You sacrifice one token to Viscera Seer with Grave Pact out: Carmen's trigger
  fires once for your sacrifice and once per opponent who sacrifices to Pact —
  **four counters and 4 life per token**, at instant speed.
- Anowon's upkeep: up to four triggers a turn with nothing spent.
- An opponent paying Vein Ripper's ward: a trigger.

**Where the life goes.** The deck's lifegain payoffs are Vito, Thorn of the Dusk
Rose ("whenever you gain life, target opponent loses that much life"), Marauding
Blight-Priest ("whenever you gain life, each opponent loses 1 life") and
Bloodthirsty Conqueror (via the existing loops). Each Carmen trigger is a
separate 1-life event, so with Vito out the Grave Pact line above is **4 drain
per token on top of** Blood Artist / Cruel Celebrant / Bastion. Carmen is a
drain source in this deck, not just a lifegain source.

## 4. The second ability — the role the deck is thin in

Repeatable graveyard-to-battlefield recursion in the list: **none**. What exists:

| Card | Scope |
|---|---|
| Bloodghast | returns itself only |
| Edgar, Charmed Groom | returns itself only (as Coffin) |
| Malakir Rebirth | one creature, one-shot, 2 life |
| Takenuma, Abandoned Mire | to **hand**, one-shot, costs the land |

The 2026-08-31 structural audit and the 2026-10-02 shape review both named board
recovery as the deck's one standing structural hole; the shape review proposed
Sorin, Vengeful Bloodlord partly for its −X reanimation. Carmen does that job every
attack for no mana, and returns any **permanent** (Grave Pact and Skullclamp are
targets, not only creatures).

Target pool by her power (permanents, nonland, from `cards.json`):

| Power | Eligible permanents | Notable |
|---|---|---|
| 2 (base) | 21 | Blood Artist, Cruel Celebrant, Cordial Vampire, Viscera Seer, Bloodghast, Edgar AB, Skullclamp, Blade of the Bloodchief |
| 3 | 38 | + Vito, Marauding Blight-Priest, Captivating Vampire, Stromkirk Captain, Clavileño, Sorin |
| 4 | 48 | + Grave Pact, Bloodline Keeper, Elenda, Sanctum Seeker, Mirkwood Bats |

One sacrifice puts her at 3; one Edgar Markov attack trigger adds another. In
practice she attacks as a 4-power flier the turn after she lands.

**Honest limit:** she does not fix the *wrath* case — she dies to the wrath with
everything else and must be recast (5 mana) before she can rebuy anything. What
she fixes is the **attrition** case: spot removal and chump-trades that pick off
Blood Artist, Vito or Seer one at a time. Against a wrath the recovery still
comes from Bloodghast, the Coffin and eminence.

## 5. Rubric tests

**Best case, as a falsifiable claim:** "Eighteen cards in the list trigger her
first ability, five of them on opponents' permanents; she is the deck's only
repeatable recursion; and each trigger is a Vito/Blight-Priest drain event — so
she serves the combat mode (a growing evasive body that Edgar's attack trigger
also grows) and the aristocrats mode (drain and rebuy) at once." Every count
above is script output.

**Redundancy (effect × frequency × duration).**
- Recursion: nothing repeatable exists. Not redundant.
- Lifegain-per-event: Edgar AB (your creatures dying, free), Blood Artist /
  Cruel Celebrant / Bastion (die-drain). Carmen is an additional incremental
  source, on a different trigger (sacrifice, any player). Partially redundant —
  this is her weakest axis.
- Grow-on-death body: Elenda ("another creature dies", incl. wraths and combat;
  lifelink; tokens on death), Carrion Feeder, High-Society Hunter. Elenda is the
  closest comparable. Different trigger (death vs sacrifice), different payoff
  (tokens vs recursion + life). Not redundant by the rubric's three-term test,
  but they are the same *kind* of card and the deck would carry two.

**Density.** 18/99 for trigger 1 (plus every opponent fetchland, Treasure and
aristocrats outlet at the table). Trigger 2 needs only a graveyard and an attack.
Under the rubric's rough one-third line for trigger 1 alone; above it once
opponents' sacrifices and trigger 2 are counted. Reported as 18.

**Marginal impact.** Changes attrition losses (rebuys the engine piece that got
answered) and speeds the drain clock when Grave Pact or Anowon is out. Does not
change wrath losses or fast-combo losses. Not win-more: she is at her best when
you are trading, which is when the deck is *not* ahead.

**Cost of entry.** MV 5: the slot goes 5 → 6 (8 cards at MV 5+ of 65). Avg MV
2.88 → 2.90 replacing Nocturnus (unchanged replacing Bloodwitch). The one {W}
pip: 14 of 34 lands produce W, 20 sources with rocks; W pips 17 → 18 against B 71.
Fine on turn 5+. Master of Dark Rites ({B}{B}{B} for Vampire spells) casts her a
turn early.

**Anti-synergy.** Teferi's Protection stops her lifegain for a cycle (same as
every other gain source; counters still accrue). Anowon's "each player" edict
includes you — Carrion Feeder, Mirkwood Bats or Bastion's Soldier token are the
non-Vampire sacrifices, and each one is a Carmen trigger, so that is a synergy
not a nonbo. Legend rule: no conflict. She is a Vampire: eminence token on cast.

**Worst-case draw.** Opening hand vs. the fast deck: a 5-drop you hold; the deck
has 25 one- and two-drops to play first. Turn-12 topdeck on an empty board: a
2/2 flier that attacks next turn into a full graveyard and returns Blood Artist
or Cordial Vampire — one of the better topdecks in the list at that point.

**Bracket.** Not a Game Changer. Commander Spellbook: **0 new combos**. One
near-combo, Carmen + **Breath of Fury** (infinite combats). Breath of Fury is red,
in identity, and *not* in the deck — do not add it; that would be a two-card
infinite at bracket 3.

**Disagreement check — the hard one.** EDHREC: **16.4%** of Edgar decks
(8,461/51,456) against 76.1% in Clavileño (8,187/10,763) and 43.9% in Elenda
(3,062/6,982). She is absent from every Edgar theme list the script prints,
including *aristocrats*, *sacrifice* and *reanimator*. So what does this deck have
that 43,000 Edgar lists do not? The answer is specific: Grave Pact is in 10.7% of
Edgar decks, and this list runs Grave Pact, Anowon, Henrika and Phyrexian Tower
with three free outlets. The median Edgar list is an anthem-tribal deck where
Carmen is a 2/2 for five; this one is structurally closer to the Clavileño and
Elenda shells where she is a majority include. That is a named difference, not a
hand-wave, and it is the same difference that already reversed Grave Pact,
Elenda and Anowon in this deck.

**Price.** $6.49 (fetched 2026-10-06 02:24 UTC). Owned. Price was not
load-bearing in the 2026-08-30 rejection and is not load-bearing here.

## 6. The cut

Carmen enters as an amplifier (counters on herself) and payoff (drain via
lifegain) with a recursion rider. Same-role cuts first. **Sacrifice outlets are
explicitly spared** — they are her fuel, which overrides the 2026-10-02 proposal
to cut Bloodthrone Vampire as "the third free outlet."

| Rank | Cut | Why |
|---|---|---|
| **1** | **Vampire Nocturnus** (MV 4) | "As long as the top card of your library is black": 47 of 99 cards are black, so the anthem is off more than half the time and reveals your top card all game. Viscera Seer's scry 1 only re-rolls it. It is the worst-rate amplifier in the deck's deepest category (5 other anthems: Legion Lieutenant, Captivating Vampire, Stromkirk Captain, Charmed Groom, Lord of Lineage, plus Shared Animosity). Already named as cut #1 on 2026-10-02 — consistent. Combat-mode only; Carmen serves both modes. |
| 2 | Malakir Bloodwitch (MV 5) | Same MV, same colour-pip count — the curve-neutral swap. It was reversed to ADD on 2026-08-31 for "protection from white against multiple mono-white decks," a spare reason `meta.json` has since expired ("do not carry forward any fixed description of what the pod plays"). What still defends it: the ETB gain is one event, so with Vito out and six Vampires it is an 18-point drain at one opponent. That is why it is #2, not #1. |
| 3 | Forerunner of the Legion (MV 3) | Tutor-to-top is card-neutral; named weakest on 2026-09-06 and 2026-10-02. Spared here because cutting a 3 for a 5 moves the curve the wrong way, and the 3-slot is not the problem. |
| — | Elenda, the Dusk Rose | The closest same-kind card, but she triggers on *any* death including wraths — the case Carmen does not cover. Spared. |
| — | Patron of the Vein | The only ETB removal creature; its counter trigger is the Grave Pact / Anowon payoff. Spared. |

**After (Carmen in, Nocturnus out):** curve 1:12 · 2:13 · 3:20 · 4:12 · 5:6 · 6:2;
avg MV 2.90; pips B 68 / W 18 / R 4; Vampire spells 35 → 35; lands 34; Game
Changers 2/3; combos assembled 2 → 2.

**Interaction with the 2026-10-02 proposals.** Carmen covers the recursion role
that Sorin, Vengeful Bloodlord was proposed for. If Carmen goes in, Sorin VB's
case narrows to its lifelink-on-your-turn line alone — still real, but weaker. The
Nocturnus slot was also Twilight Prophet's proposed slot; if both are wanted, the
next cut is Bloodwitch.

## 7. What would change this verdict

- If the pod's games turn out to be decided by turn 6 more often than not: she is
  a 5-drop with a one-turn delay, and the 2026-08-30 "no" was right for that pod.
- If graveyard hate is common at the table (Bojuka Bog is in *this* deck, so the
  pod knows the card): her attack trigger blanks.
- If the user removes Grave Pact or Anowon: her trigger count drops from 18 to 16
  sources and she loses the four-per-token multiplier. Still an add, less clearly.

`base.txt` was not modified. The swap is the user's to make.
