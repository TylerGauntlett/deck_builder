# markov_chains — Gas Guzzler (2026-10-28)

**Verdict: ADD, replacing Forerunner of the Legion.** The case is modest. Guzzler
isn't a strong card. It wins because Forerunner is still the weakest card in the
deck, it has been named the top cut in four earlier reviews, and Guzzler turns
eminence tokens into cards, which Forerunner never does. If you're keeping
Forerunner on purpose, the answer is **NO**. The next cut is Bloodthrone Vampire,
and I won't cut that for this (see "The cut").

Deck state: `base.txt` unchanged since the 2026-10-23 sync. 100 cards, 34 lands,
average non-land MV 2.86, pips B 63 / W 19 / R 4. Bracket 3, $40/card cap, Game
Changers 2/3 (Necropotence, Teferi's Protection).

## The card (Scryfall, fetched 2026-10-28 14:56 UTC)

> **Gas Guzzler** `{B}` — Creature — Vampire Rogue, 2/1
> Start your engines! *(If you have no speed, it starts at 1. It increases once on
> each of your turns when an opponent loses life. Max speed is 4.)*
> This creature enters tapped.
> Max speed — `{B}`, Sacrifice another creature or Vehicle: Draw a card.

Colour identity B · Commander legal · not a Game Changer · EDHREC rank 10,717.

Rulings that matter:
- Speed is per player and **never goes down**. Losing Guzzler doesn't reset it.
- Speed rises **once per turn, and only on your turn**. Drains on opponents' turns
  (Grave Pact or Blood Artist firing during their removal) don't count.
- So the activation needs **three of your turns with an opponent losing life**
  after Guzzler arrives. Cast on turn 2, it's online on turn 5 at the earliest.
  Top-decked on turn 10 with no speed, it's online on turn 13.

## Steel-man

- It's a 1-mana Vampire, so it triggers eminence for one mana: two bodies on turn 1.
- Getting to max speed costs nothing extra here. Eminence tokens attacking, Sanctum
  Seeker, and Blood Artist (*"target player loses 1 life"*) or Cruel Celebrant
  (*"each opponent loses 1 life"*) on a sacrifice during your turn all count.
- Once it's online, every spare token becomes a card for `{B}`, at instant speed,
  in response to removal or a wrath. Each activation is also a death, which triggers:
  - **Grave Pact**: *"Whenever a creature you control dies, each other player
    sacrifices a creature"*. So it's an edict plus a card.
  - **Blood Artist**: *"this creature or another creature dies"* (any creature).
  - **Cruel Celebrant**: *"another creature … you control dies"*.
  - **Carmen, Cruel Skymarcher**: *"Whenever a player sacrifices a permanent"*.
    Carmen gets a +1/+1 counter and you gain 1 life.
  - **Edgar, Ancient Bloodlord**: *"another creature … you control dies, you gain
    1 life"*. That life gain feeds Vito and Blight-Priest.
- The 2026-10-02 shape review asked for card draw that **converts deaths and the
  Vampire count into cards**. This card does exactly that.

## The tests

**Redundancy.** The deck already runs this exact activation, ungated:
**Baron Bertram Graywater**, *"{1}{B}, Sacrifice another creature or artifact: Draw a
card."* **Skullclamp** gets two cards per death at a better rate. Guzzler is a third
death-to-card engine. It's cheaper to deploy than Baron (1 vs 4 mana) and cheaper
to activate (`{B}` vs `{1}{B}`), but its gate means it's live in fewer turns than
Baron. That counts against it. It isn't a hard veto, because card advantage is the
pillar the shape review wanted bigger.

**Sacrifice outlets aren't the gap.** The deck already has these outlets (verified
text): Viscera Seer, Carrion Feeder, Bloodthrone Vampire and Phyrexian Tower (free),
plus Indulgent Aristocrat `{2}`, Edgar, Ancient Bloodlord `{2}`, Baron `{1}{B}`,
Master of Dark Rites (tap), High-Society Hunter (on attack) and Village Rites
(one-shot). Guzzler's only new contribution is the card it draws, so judge it as a
draw card.

**Worst-case draw.** It's top-decked late on an empty board. It's a 2/1 that can't
block the turn it lands, and its ability is three turns away. That's a real dead
draw, but it's the same dead draw as Forerunner, a 3-mana 2/2.

**Speed premise.** The verdict doesn't depend on how fast the pod is. The last
recorded answer (2026-08-30) is that games run long. Long games help Guzzler,
because more turns at max speed means more cards. If games ran short, Guzzler would
be worse, but it would still beat Forerunner.

**Bracket and combos.** Not a Game Changer. `combos.py --add` finds 0 new combos
and 0 near combos (baseline 2). House rules untouched.

**Disagreement check.** EDHREC: 5.2% of Edgar Markov decks (2,573 / 49,275). Its
real homes are speed commanders: The Speed Demon 62.1%, Far Fortune 55.1%, Zahur
52.7%. The community treats it as a fringe card in Edgar. My reason for adding it
anyway isn't that it's good in general. It's that Forerunner is weaker.

## The cut

1. **Forerunner of the Legion** `{2}{W}` 2/2. *"search your library for a Vampire
   card … put that card on top"* is card-neutral. *"Whenever another Vampire you
   control enters, target creature gets +1/+1 until end of turn"* is the deck's
   weakest pump. It was named the top cut on 09-06 (Drana/Linvala), 09-06 (New
   Blood), 09-06 (Necropotence) and 10-02 (shape). The cut also moves a card from
   the crowded 3-drop slot to a 1-drop, and swaps a W pip for a B pip. Forerunner
   is the deck's only tutor. Losing it doesn't break any house rule, because the
   deck has no tutor-dependent lines.
2. Runner-up: **Bloodthrone Vampire**. **Not offered.** The 2026-09-04 review spared
   it because *"free sac outlets are load-bearing for Grave Pact"*. They let you
   turn a board into edicts at instant speed with no mana. That still holds.
   Guzzler isn't free (`{B}` each) and is gated by speed, so it can't take
   Bloodthrone's job.

If Forerunner stays for reasons outside this review, the verdict is **NO**.
Nothing else in the 99 is weaker than Gas Guzzler for its role.

## Aggregate delta (−Forerunner, +Guzzler)

MV −2. Pips B 63→64, W 19→18. Vampire count unchanged. Tutors 1→0. Repeatable
death-to-card engines 2→3 (Baron, Skullclamp, +Guzzler).

## Price

$0.31 (foil $0.34), fetched 2026-10-28 14:56 UTC. Under the $40 cap. Price plays no
part in the verdict.

## Sources
- `card_facts.py lookup "Gas Guzzler" --deck markov_chains --rulings`, 2026-10-28 14:56 UTC.
- `card_facts.py lookup` for Bloodthrone Vampire, Forerunner of the Legion, Viscera
  Seer, Carrion Feeder, Edgar Ancient Bloodlord, Skullclamp, Village Rites, Welcoming
  Vampire, Bloodline Recollector, High-Society Hunter, Phyrexian Tower (same fetch).
- Blood Artist, Cruel Celebrant, Grave Pact, Carmen, Baron Bertram, Indulgent
  Aristocrat, Master of Dark Rites text from `cards.md` (built from Scryfall).
- `edhrec.py card "Gas Guzzler" --deck markov_chains`.
- `combos.py markov_chains --add "Gas Guzzler" --near`: 0 new, 0 near.
- `card_facts.py search` for sac-for-card creatures at MV ≤ 3 (2026-10-28 14:57 UTC).
  Vampire Gourmand and Sanguine Spy were checked as alternatives. Both are weaker:
  Gourmand only draws on attack, and Spy only surveils.

`base.txt` was not modified by this review.
