# markov_chains — Vampire Gourmand (2026-10-30)

**Verdict: ADD, replacing Forerunner of the Legion.**

Deck state: `cards.md` regenerated 2026-10-28, same commit as `base.txt` (Gas Guzzler
in, Clever Concealment out). 100 cards, 34 lands, avg non-land MV 2.82, pips B 64 /
W 17 / R 4. Bracket 3, $40/card cap, Game Changers 2/3 (Necropotence, Teferi's
Protection).

## The card (Scryfall, fetched 2026-10-30 03:17 UTC)

> **Vampire Gourmand** `{1}{B}` — Creature — Vampire, 2/2
> Whenever this creature attacks, you may sacrifice another creature. If you do,
> draw a card and this creature can't be blocked this turn.

Colour identity B · Commander legal · not a Game Changer · no official rulings.

## Steel-man

A 2-mana Vampire, so it triggers eminence and arrives with a token, and that token
is next turn's sacrifice. Every attack after that turns a spare 1/1 into a card
**for no mana**. It also makes Gourmand unblockable, so it connects with every
anthem and counter on it. The sacrifice happens on your turn, so each one fires:

- **Grave Pact**: "Whenever a creature you control dies, each other player
  sacrifices a creature". A free edict every combat.
- **Blood Artist**: "this creature or another creature dies … target player loses
  1 life". This fires on *any* creature dying.
- **Cruel Celebrant**: "another creature … you control dies, each opponent loses 1
  life". This fires only on *your* creatures.
- **Bloodletter of Aclazotz**: "If an opponent would lose life **during your
  turn**" it's doubled. Gourmand's sacrifice always happens on your turn, so both
  drains above are doubled. Grave Pact deaths on opponents' turns aren't.
- **Carmen, Cruel Skymarcher**: "Whenever a player sacrifices a permanent".
- **Edgar, Ancient Bloodlord**: "you gain 1 life", which feeds Vito and Blight-Priest.
- **Bloodline Recollector**: "if three or more creatures died this turn". Gourmand's
  sacrifice plus the Grave Pact deaths it causes gets there.

It works in **both modes**. In the aggro plan it's an evasive attacker. In the
aristocrats plan it's a free, once-a-turn sacrifice that also draws.

## The tests

**Redundancy (effect × frequency × duration).** The deck already has three
repeatable death-to-card engines:

| Card | Cost per card | Frequency | Gate |
|---|---|---|---|
| Baron Bertram Graywater | `{1}{B}` | unlimited, instant | none (4-drop) |
| Gas Guzzler | `{B}` | unlimited, instant | max speed (~3 of your turns) |
| Skullclamp | equip `{1}` | per equip | none; 2 cards |
| **Vampire Gourmand** | **free** | **once per turn, on attack** | must attack |

Gourmand is the only one that costs no mana per card. So it doesn't do the same
job at a worse rate. It's a free card every turn on the turns you're spending your
mana on Vampires anyway. It's still a fourth card in the category, which counts
against it. It isn't a veto, because the 2026-10-02 shape review set card advantage
as the pillar to grow.

**Consistency with the Gas Guzzler review.** On 10-28 I set Gourmand aside as
"weaker, only draws on attack". That compared the two for *one* slot. Guzzler
then took Clever Concealment's slot instead, so Forerunner's slot is still open.
The one-line dismissal was also too quick. Guzzler has the higher ceiling
(unlimited, instant speed). Gourmand has the higher floor (no speed gate, no mana).
The two don't compete with each other.

**Density.** It needs one other creature when it attacks. Eminence makes one with
every Vampire cast, including Gourmand itself, so this is almost never short.

**Worst-case draw.** On turn 2, on the draw: two bodies, then a card on turn 3.
Top-decked on turn 12 with an empty board: two bodies, and a card the following
turn. That's better than either Guzzler or Forerunner at both ends.

**Anti-synergy.** It removes one attacker each combat, and it taps to work. It's
minor, because the body it eats is usually a 1/1 token.

**Speed premise.** The verdict doesn't depend on it. The card works on turn 3 and
on turn 15.

**Bracket and combos.** Not a Game Changer. `combos.py --add`: 0 new, 0 near
(baseline 2). House rules untouched.

**Disagreement check.** EDHREC: 19.7% of Edgar Markov decks (10,305 / 52,331).
That's fringe-to-moderate, and I'm saying yes. My independent reason is that
Forerunner is the weakest card in the 99, not that Gourmand is a staple.

## The cut

1. **Forerunner of the Legion** `{2}{W}` 2/2. "Put that card on top" is
   card-neutral, and "target creature gets +1/+1 until end of turn" is the weakest
   pump in the deck. It has been named the top cut in five reviews (09-06 ×3,
   10-02, 10-28), and the 10-28 follow-up left it as "the next cut in line".
   Vampire for Vampire, so the eminence count doesn't change. It's the deck's only
   tutor, but no line depends on it (house rule).
2. Runner-up: **Bloodthrone Vampire**. **Not offered.** The 09-04 and 10-28
   reasoning still holds: free, instant-speed outlets carry Grave Pact. Gourmand
   only sacrifices once, on attack, at sorcery-ish timing, so it can't take that job.

## Aggregate delta (−Forerunner, +Gourmand)

MV −1 (3→2). Pips W 17→16, B 64→65. Vampire creatures unchanged. Tutors 1→0.
Repeatable death-to-card engines 3→4. 3-drops 19→18.

## Price

$0.26 (foil $0.31), fetched 2026-10-30 03:17 UTC. Under the cap. Price plays no
part in the verdict, which holds if the card were free.

## Sources
- `card_facts.py lookup "Vampire Gourmand" "Forerunner of the Legion" "Bloodthrone
  Vampire" "Gas Guzzler" "Baron Bertram Graywater" "Skullclamp" --deck markov_chains
  --rulings`, 2026-10-30 03:17 UTC.
- Grave Pact, Blood Artist, Cruel Celebrant, Carmen, Edgar Ancient Bloodlord,
  Bloodline Recollector, Bloodletter text from `cards.md` (Scryfall, 2026-10-28).
- `edhrec.py card "Vampire Gourmand" --deck markov_chains`.
- `combos.py markov_chains --add "Vampire Gourmand" --near`: 0 new, 0 near.

`base.txt` was not modified by this review.
