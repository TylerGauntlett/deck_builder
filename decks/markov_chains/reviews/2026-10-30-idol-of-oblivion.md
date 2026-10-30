# markov_chains — Idol of Oblivion (2026-10-30)

**Verdict: NO.** The engine works the way you describe. But the deck already has
the same engine in Welcoming Vampire. Card advantage is the category the
2026-10-09 review said to stop growing, and every cut is one I've already spared
for a stated reason.

Deck state: `cards.md` regenerated 2026-10-30, same timestamp as `base.txt`
(Vampire Gourmand in, Gas Guzzler out). 100 cards, 34 lands. Bracket 3,
$40/card cap, Game Changers 2/3.

## The card (Scryfall, fetched 2026-10-30 13:57 UTC)

> **Idol of Oblivion** `{2}` — Artifact
> {T}: Draw a card. Activate only if you created a token this turn.
> {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.

Colourless · Commander legal · not a Game Changer. Ruling (2019-08-23): the
token can have been made before Idol entered, or have already left the
battlefield.

## Your premise, checked

> "A vampire token is created for every vampire. This could lead to a card draw
> every turn."

- **Mostly right.** Edgar's eminence says *"Whenever you cast another Vampire
  spell … create a 1/1 black Vampire creature token."* The deck has 38 Vampire
  cards, counted by type line in `cards.md`. Any **token** counts for Idol, not
  just creatures. That includes Treasure from Black Market Connections (*"At the
  beginning of your first main phase … Create a Treasure token"*), Blood from
  Voldaren Estate, and the upkeep token from Edgar, Charmed Groom. So once one of
  those is on the battlefield, you draw every one of your turns even without
  casting a Vampire.
- **"Every turn" means every *one of your* turns.** On an opponent's turn you
  need a token made at instant speed. Only two cards here do that: Bloodline
  Keeper ({T}, so at instant speed) and Charismatic Conqueror (only if the
  opponent declines to tap). So it's one card per turn cycle, not one per turn.
- **Agreed: the Eldrazi half doesn't matter.**

## Steel-man

It costs 2 colourless, so you can cast it off any land. That matters in a deck
whose white and red sources are the tight ones. It's an artifact, so it survives
creature wipes, including the deck's own Olivia's Wrath. It needs no attack and no
sacrifice. EDHREC lists it in 15.0% of Edgar Markov decks (7,825 / 52,331).

## Why it fails

**1. Welcoming Vampire already does this job.**

> **Welcoming Vampire** `{2}{W}`: "Whenever one or more other creatures you
> control with power 2 or less enter, draw a card. This ability triggers only
> once each turn."

| | Welcoming Vampire | Idol of Oblivion |
|---|---|---|
| Trigger | ≤2-power creature enters (eminence tokens qualify) | any token created |
| Rate | 1 per turn | 1 per turn |
| Cost per card | free, automatic | free, but costs a tap |
| Opponents' turns | yes, if a creature enters (Keeper, Conqueror) | yes, same sources |
| Vampire (eminence token on cast) | **yes** | no |
| Survives a creature wipe | no | **yes** |

Idol's real edges are three: it survives wipes, it also counts non-creature
tokens, and it costs less coloured mana. Those are real but narrow. On most turns
the two cards are the same draw, triggered by the same eminence token. The second
copy of an engine is worth much less than the first.

**2. The category is already full.** Repeatable or recurring draw in the 99
(from oracle text in `cards.md`): Necropotence, Black Market Connections,
Skullclamp, Welcoming Vampire, High-Society Hunter, Baron Bertram Graywater,
Vampire Gourmand, Bloodline Recollector, Clavileño. One-shots: Village Rites,
Henrika. Lands: War Room, Voldaren Estate. On 2026-10-09 I wrote *"two
card-advantage adds into a category already 13 deep … Don't go past two."* Two
have gone in since then: Bloodline Recollector, and Vampire Gourmand (which took
Gas Guzzler's slot). Idol would be the third.

**3. No honest cut.** These are the cuts at the bottom of the list, each with the
reason it was spared in an earlier review:

1. **Forerunner of the Legion.** It's the deck's only tutor. You chose to keep
   it on 2026-10-30.
2. **Henrika Domnathi.** Spared on 2026-10-30 because she does *"three different
   jobs, none of them a copy of something already in the deck"*. That reason
   still holds. Cutting a card that copies nothing to make room for one that
   copies Welcoming Vampire would invert it.
3. **Bloodthrone Vampire.** A free, instant-speed sacrifice outlet, which is what
   makes Grave Pact work (2026-09-04, and again 10-09, 10-28 and 10-30).

**Bracket and combos.** No issue at bracket 3: not a Game Changer, and
`combos.py --add` found 0 new and 0 near combos (baseline 2).

**Speed premise.** The verdict doesn't depend on it. In short games and long
ones, Idol is still the second copy of a draw engine the deck already runs.

## What would change it

- **You let Forerunner go.** Idol beats Forerunner as a card. Forerunner has been
  named the weakest card in five reviews, and only your attachment to the tutor
  keeps it. If that changes, Idol is a reasonable replacement. Gourmand,
  Recollector and Baron are all in now, so it's no longer the strongest draw
  option.
- **Your games show you running out of cards** with this draw suite in. That
  would be a new fact, and the category cap would move.
- **Welcoming Vampire keeps dying to wipes** and you want a draw engine that
  survives them. That's a real reason to swap Welcoming Vampire for Idol, rather
  than add Idol alongside it. You'd lose a Vampire (one eminence token) and a 2/3
  flier, and gain a draw that survives wipes and can be cast with any colour.
  That's roughly even.

## Price

$3.17, fetched 2026-10-30 13:57 UTC. Under the cap. The NO doesn't depend on
price; it holds if the card were free.

## Sources
- `card_facts.py lookup "Idol of Oblivion" --deck markov_chains --rulings`, and
  `lookup "Edgar Markov" "Welcoming Vampire" "Black Market Connections"
  "Forerunner of the Legion"`, 2026-10-30 13:57 UTC.
- Token and draw sources grepped from `decks/markov_chains/cards.json`
  (Scryfall, 2026-10-30).
- `edhrec.py card "Idol of Oblivion" --deck markov_chains`: Edgar Markov 15.0%.
- `combos.py markov_chains --add "Idol of Oblivion" --near`: 0 new, 0 near.

`base.txt` was not modified by this review.
