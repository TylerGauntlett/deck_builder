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

---

## Follow-up: "Forerunner is the only tutor and fixes my hand" (2026-10-30)

**Checked:** it is the only tutor. `search your library` appears once in `cards.md`,
on Forerunner. I had recorded that as "Tutors 1→0" without weighing it.

**This is a new axis, not a new fact.** "Card-neutral" measured Forerunner on card
*count*. Your point is about card *quality*: which card you draw next. That's a real
job and I under-rated it. What it can and can't do, from its text ("search your
library for a Vampire card … put that card on top"):

- **It can find:** any Vampire. That covers the payoffs and engines: Vito, Bloodthirsty
  Conqueror, Bloodletter, Blood Artist, Cruel Celebrant, Welcoming Vampire, Baron.
- **It can't find:** removal, protection, Grave Pact, Skullclamp, Necropotence, or
  lands. So it fixes "I need a threat or an engine" and not "I need an answer".
- **It's slow:** the card arrives on your next draw, not now.

**Does it change the verdict?** Gourmand still goes in. A free card every turn still
beats a one-time, Vampires-only, next-turn selection. What changes is **which card
leaves**. If you value the selection, the 09-06 review already named the next honest
cut: *"If Forerunner is a card you like, Henrika is the next honest cut."*

**Henrika Domnathi** `{2}{B}{B}` (fetched 2026-10-30 03:25 UTC). At the beginning of
combat on your turn, choose one that hasn't been chosen: each player sacrifices a
creature; you draw a card and lose 1 life; or transform her into a 3/4 flier with
deathtouch and lifelink.
- **The case for keeping her:** she's an edict that also triggers Grave Pact, plus a
  card and a body, spread over three turns. That's a stronger card than Forerunner.
- **The case for cutting her:** she's a one-shot package at 4 mana. Gourmand gives a
  card every turn for 2 mana. Edicts aren't the last of their role here: Grave Pact,
  Anowon, Olivia's Wrath, Swords to Plowshares and others remain. Her back face is
  one more deathtouch/lifelink body in a category the 09-06 review called full.

This is closer than the Forerunner swap, and I'd say so plainly.

**Revised verdict:** **ADD Vampire Gourmand.**
- **Cut Forerunner** if the tutor is a "nice to have".
- **Cut Henrika Domnathi** if Forerunner really does change games for you.

Both are Vampire-for-Vampire swaps, so the eminence count doesn't change.
- With the Henrika cut: MV 4→2, B pips 64→63 (`{B}{B}` out, `{B}` in), W pips unchanged at 17, and 4-drops −1.
- Bloodthrone Vampire is still spared, for the same Grave Pact reason as before.

---

## Follow-up: cut Gas Guzzler instead? (2026-10-30)

**One correction first.** Gourmand's draw costs no mana. Only Guzzler's costs `{B}`.

**Why this isn't contradicting 10-28.** On 10-28 I said Guzzler beats Forerunner.
That judgement was made in a deck **without** Gourmand. Redundancy depends on what
else is in the deck, and Gourmand changes that. Here are the four death-to-card
engines with Gourmand in (verified text above):

| Card | Cost per card | Frequency | Timing | Online |
|---|---|---|---|---|
| Baron Bertram Graywater | `{1}{B}` | unlimited | instant | when cast (4 MV) |
| Skullclamp | equip `{1}` | per equip | sorcery (equip) | when cast; 2 cards |
| Gas Guzzler | `{B}` | unlimited | instant | max speed: 3+ of your turns |
| Vampire Gourmand | free | once per turn | on attack | next turn |

**What only Guzzler does.** It can turn the whole board into cards at instant speed,
for example in response to a wipe. **Baron** already does that, at one more mana per
card and with no wait. So Guzzler is a cheaper Baron that shows up three turns late.

**Its worst draw.** Guzzler is the deck's only "start your engines" card (grep of
`cards.md`), so your speed only starts counting once it's on the battlefield. Drawn
late on an empty board, it's a 2/1 that enters tapped and does nothing for three
turns. Gourmand drawn the same way gives you a card the next turn.

**Against the other two cuts:**
- **Henrika:** an edict plus a card plus a body. That's three different jobs, none
  of them a copy of something already in the deck.
- **Forerunner:** the deck's only tutor, and you value it.
- **Guzzler:** the most redundant card once Gourmand is in. It's the card that
  overlaps most with the one coming in, so this is a same-role cut, which the rubric
  prefers.

**Final verdict: ADD Vampire Gourmand, cut Gas Guzzler.** Keep Forerunner and Henrika.

Aggregate (−Guzzler, +Gourmand): MV 1→2, B pips unchanged at 64 (one `{B}` each),
Vampire count unchanged, death-to-card engines stay at 3, and there are no more
speed/max-speed cards. Bloodthrone Vampire is still spared for the Grave Pact reason.
