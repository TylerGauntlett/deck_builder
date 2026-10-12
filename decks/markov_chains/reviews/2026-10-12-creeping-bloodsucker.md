# markov_chains — Creeping Bloodsucker (2026-10-12)

**Verdict: NO.** It's a low-rate drain that doesn't scale, going into the deck's most
overstuffed tier (payoffs). Every interaction that makes it look strong is already
covered by cards the deck runs, and no cut is actually worse than it.

Deck state: `base.txt` and `cards.md` match the 2026-10-09 sync (Carmen in, Nocturnus
out). 100 cards, 34 lands + Malakir Rebirth MDFC, avg non-land MV 2.94. Bracket 3,
$40/card cap, Game Changers 2/3. None of the swaps from the 10-02 shape review or the
10-09 Recollector review have been applied: Florian, Bloodthrone Vampire, Forerunner
and Malakir Bloodwitch are all still in the list.

## The card (Scryfall, fetched 2026-10-12 18:42 UTC)

**Creeping Bloodsucker** `{1}{B}`: Creature — Vampire 1/2
> At the beginning of your upkeep, this creature deals 1 damage to each opponent. You
> gain life equal to the damage dealt this way.

Colour identity B · Commander legal · not a Game Changer · no official rulings.
Price **$5.03** (2026-10-12 18:42 UTC). Under the cap; price played no part in the verdict.

| Axis | Reading |
|---|---|
| Whose permanents | none, it triggers on its own |
| Whose turn | "**your** upkeep": once per turn cycle |
| Targeted | no, it hits "each opponent" (gets around hexproof/ward) |
| Who chooses | nobody |

## Honest best case

A 2-mana Vampire (so it also gives an Edgar eminence token) that drains every turn
with no combat, no sacrifice and no other piece needed. It's the only unconditional
repeating drain in the list. Its trigger lands on your turn, so it stacks with the
deck's lifegain and doubling payoffs:

- **Vito, Thorn of the Dusk Rose**: "Whenever you gain life, target opponent loses
  that much life." Bloodsucker's gain is one 3-life event, so 3 more on one opponent.
  That's 6 opponent life per upkeep.
- **Marauding Blight-Priest**: "Whenever you gain life, each opponent loses 1 life."
  +3.
- **Bloodletter of Aclazotz**: "If an opponent would lose life **during your turn**,
  they lose twice that much." Upkeep is your turn, so the base trigger becomes 2 each
  (you still gain only 3, since the gain equals *damage dealt*).
- **Bloodthirsty Conqueror**: "Whenever an opponent loses life, you gain that much
  life." That's 3 more gain events per upkeep for Vito and Blight-Priest.

That clears the three-card synergy floor. The case is real. Here's where it breaks.

## The tests

**Redundancy: effect × frequency × duration.** The deck already has **11 cards that
make opponents lose life** (oracle scan of `cards.json`): Blood Artist, Cruel
Celebrant, Bastion of Remembrance, Impact Tremors, Vito, Marauding Blight-Priest,
Sanctum Seeker, Mirkwood Bats, Malakir Bloodwitch, Bloodthirsty Conqueror, Vein Ripper.
It has **~20 lifegain sources** to feed Vito and Blight-Priest. Rate per turn cycle:

| Card | Opponent life lost per cycle | Scales with board? |
|---|---|---|
| **Creeping Bloodsucker** | 3 (1 × 3 opponents), fixed | **no** |
| Impact Tremors | 3 per creature entering; each Vampire cast with eminence = 2 entries = 6 | yes |
| Sanctum Seeker | 3 per attacking Vampire | yes |
| Blood Artist / Cruel Celebrant | 1 or 3 per death | yes |
| Vein Ripper | 2 per death, any creature | yes |

Bloodsucker has the lowest ceiling of any drain in the deck. It's the only one that
works without a board. That's its whole edge, so the question is whether that matters.

**Its best combo is already closed.** Vito + Bloodthirsty Conqueror (and Blight-Priest
+ Conqueror) are the deck's two assembled loops. Once both pieces are out, *any* gain
or loss starts the loop: a combat hit, a death with Blood Artist out, an eminence token
entering with Impact Tremors, Edgar, Ancient Bloodlord's gain. Bloodsucker would start
it at your next upkeep, and the deck already starts it sooner. Commander Spellbook:
`combos.py --add` shows **0 new combos, 0 newly within reach** (baseline 2).

**Density / multiplier test.** The closing filter from the 08-30 review: the adds that
survived were *multiplicative*, and the ones correctly rejected were additive cards in
categories already 10+ deep. Bloodsucker is the textbook additive card. Its output is
the same with 1 Vampire or 15, and the payoffs tier is already **12**. The 10-02 shape
review marked that tier **↓** (diamond shape: few payoffs, many amplifiers).

**Marginal impact: does it change games you lose?** The deck's standing structural
hole is recovering after a wrath (08-31 audit, 10-02 shape). Bloodsucker dies in the
wrath with everything else and does nothing to rebuild. In a slow start it's a fine
turn-2 play, but the deck has 13 two-drops and this one doesn't develop toward either
plan. **This rejection doesn't depend on game speed.** The shape review records that
the pod runs long, and long games are Bloodsucker's best case. Even counting a
generous 10 upkeeps, that's ~10 per opponent spread over the whole game. Impact
Tremors or Sanctum Seeker gets there in one or two turns once the board is wide.

**Worst-case draws.** Opening hand: playable (2-drop, eminence token). Turn 12 off the
top with an empty board: a 1/2 that drains 3 a turn. That's weak, but it's the one
spot where it beats the deck's death/attack payoffs. One good scenario out of the two.

**Anti-synergy.** Teferi's Protection ("your life total can't change") turns off its
lifegain for a cycle. That's minor, and already accepted for Vito (08-31).

**Bracket fit.** No issue.

**Disagreement check.** EDHREC: **16.6% of Edgar Markov decks (8,605 / 51,731)**, but
50.1% of Vito-commander decks (2,481 / 4,951). That difference fits this analysis.
Vito decks are built around lifegain triggers, where a free 3-life event every turn is
core. In Edgar decks it's one payoff among many. I agree with the low Edgar figure for
my own reason: rate against the board.

## Cut check (for completeness)

Even setting the tests aside, nothing in the list is clearly worse in this role:

1. **Bloodthrone Vampire**: the weakest 2-drop by raw stats, and the 10-02 shape review
   proposed cutting it. But it's an *amplifier* (free, unlimited sac outlet). Each
   sacrifice feeds Blood Artist, Cruel Celebrant, Vein Ripper, Carmen (counter + gain
   → Vito), Grave Pact and Bastion. Swapping it for a payoff goes the opposite way from
   the target shape. If it goes, the shape review's planned replacement (Sorin,
   Vengeful Bloodlord) is the better use of the slot. (On 10-09 I spared it as a
   Recollector enabler. Recollector hasn't been added, so that reason is dormant, but
   the outlet argument holds by itself.)
2. **Impact Tremors**: the closest same-MV drain. It scales with eminence (6 per
   Vampire cast); Bloodsucker doesn't. Kept.
3. **Forerunner of the Legion**: the only tutor (09-06/07). Kept.
4. **Malakir Bloodwitch**: spared on 10-09 as a Vito finisher. Kept.

The best cut I can find is a card I'd defend anywhere else. That's the finding.

## Counter-proposal: the role is real, the card is wrong

If the gap you're feeling is "a drain that ticks every upkeep without needing combat or
sacrifices", the deck already has a better candidate on file:

**Twilight Prophet** `{2}{B}{B}`: Creature — Vampire Cleric 2/4, flying (fetched
2026-10-12 18:43 UTC, **$3.76**)
> Ascend … At the beginning of your upkeep, if you have the city's blessing, reveal the
> top card of your library and put it into your hand. Each opponent loses X life and you
> gain X life, where X is that card's mana value.

It does the same thing at the same time (upkeep, your turn, so Bloodletter-doubled and
Vito-fed). It adds **a card every turn**, drains for ~2.94 average per opponent instead
of 1, and carries evasion. Ten permanents is easy with eminence tokens. It was proposed
in the 10-02 shape review (over Vampire Nocturnus, since gone) and hasn't been
evaluated against a current cut. It's the stronger version of what Bloodsucker is
reaching for, but it's a separate review.

## Data used

- Scryfall via `card_facts.py lookup`, 2026-10-12 18:42–18:43 UTC: Creeping Bloodsucker
  $5.03; Twilight Prophet $3.76; Vito $9.52; Bloodthirsty Conqueror $37.79; Bloodletter
  $36.26; Bloodthrone Vampire $0.14.
- EDHREC (`edhrec.py card`): overall rank 1550; Edgar Markov 16.6% (8,605/51,731);
  Vito 50.1% (2,481/4,951).
- Commander Spellbook (`combos.py --add --near`): baseline 2 assembled; 0 new, 0 near.
- Deck counts: oracle-text scan of `decks/markov_chains/cards.json` (generated
  2026-10-09).
