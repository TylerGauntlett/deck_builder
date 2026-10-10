# Oboro, Palace in the Clouds — lander_commander (Aesi, Tyrant of Gyre Strait)

Bracket 3, 4-player casual, $40/card cap. Pod premise carried from the
2026-08-31 weakness audit (games run turns 9–12; combo, go-wide, mill and
aristocrats opponents). This verdict does not rest on the speed premise — the
card replaces a land at no tempo cost — so it was not re-asked.

All oracle text and prices fetched **2026-10-10 20:34–20:36 UTC** via
`card_facts.py lookup`.

## Verdict: **ADD — cut one Island**

## The card (verified)

> Oboro, Palace in the Clouds — Legendary Land
> {T}: Add {U}.
> {1}: Return Oboro to its owner's hand.

Colour identity U, Commander-legal, not a Game Changer, no official rulings.
Price: **$22.04** (fetched 2026-10-10 20:34 UTC) — under the $40 cap.

## Honest best case

Oboro is a land drop that never runs out. It enters untapped, taps for {U}, and
that {U} pays its own {1} bounce, so each replay is mana-neutral. Every spare land
drop the deck has becomes a landfall trigger even with no lands in hand.

That fixes the gap the 2026-08-31 audit measured and left open: only **4** cards
put lands into hand (Coiling Oracle, Cultivate, Kodama's Reach, Yavimaya Elder),
against the extra-land-drop effects Aesi, Azusa (two more), Exploration, Dryad of
the Ilysian Grove and Oracle of Mul Daya, plus Urban Evolution once. The audit's
fix was Explore, and it found no spell worth cutting for it. Oboro is a *land*, so
it doesn't need a spell slot.

## Tests

**Synergy (named, verified).** Every "land you control enters" payoff fires on each
replay: Aesi (draw), Tatyova (draw + life), Lotus Cobra (+1 mana, so each loop
nets mana), Tireless Provisioner (Treasure), Scute Swarm, Rampaging Baloths,
Greensleeves, Zendikar's Roil, Mossborn Hydra (doubling), Avenger of Zendikar and
Springheart Nantuko. That's 11 payoffs, all scoped to *your* lands, all hit.
**Burgeoning:** the bounce works at instant speed, so in response to an opponent's
land drop you return Oboro and put it back in with Burgeoning. That gives you
landfall on their turns, which nothing else in the list does.

**Redundancy (effect × frequency × duration).** The closest card is Simic Growth
Chamber, which returns a land once, enters tapped and costs a land drop. The
Karoos (Coral Atoll, Jungle Basin) also return one land once each. Oboro does it
repeatedly, every turn, untapped. Not redundant.

**Worst-case draw.** Opening hand: an untapped Island. Turn-12 topdeck with an
empty hand: with Aesi out it's a repeatable card draw every turn. Neither end is dead.

**Anti-synergy.** It's not an Island, so it can't feed Coral Atoll's "return an
untapped Island" unless Dryad of the Ilysian Grove is out. It's not basic, so the
basic-land searches can't find it. Both are minor. It's legendary, but there's only
one. Upside: opponents' Ghost Quarter / Field of Ruin can be dodged by bouncing it
for {1} in response.

**Cost of entry.** Zero mana value. It makes {U}, exactly what the cut Island
makes, so blue source count and the G59/U21 pip balance don't change.

## Bracket flag — read this before sleeving it

`combos.py --add` reports **6 new combos**. All six are Kodama of the East Tree +
Oboro + one of Scute Swarm, Rampaging Baloths, Springheart Nantuko, Greensleeves,
Zendikar's Roil or Tireless Provisioner, giving infinite tokens and landfall.

The deck **already runs the same six combos** with Simic Growth Chamber in
Oboro's seat (baseline: 6 assembled, all `Kodama + Simic Growth Chamber + X`). So
Oboro doesn't cross a new line; it gives the existing Kodama loop a second land
piece. Kodama is MV6, and Finale of Devastation needs X=6 (8 mana) to fetch it, so
this isn't an early-game two-card infinite and doesn't break the meta.json
constraint as written. In practice it makes Kodama a more reliable win: with Oboro
anywhere on your side, Kodama resolving plus any of six common creatures/enchantments
ends the game. If you play Kodama as a value card and don't want that, take this
as **NO**. The rest of the case doesn't save it from that objection.

## Cut

Land for land, keeping 44 lands. Ranked:

1. **Island (one of 12)** — same colour, same untapped entry. You lose only the
   basic type, and 11 Islands is plenty for Coral Atoll and the searches.
2. Reliquary Tower — colourless, so swapping in Oboro gains a blue source. Spared
   because Thought Vessel and Nezahal (the other no-max-hand-size cards) both die to
   removal, and Aesi fills a hand.
3. Field of Ruin — spared to stay consistent with the 2026-08-31 audit, which
   kept Ghost Quarter and Field of Ruin as the deck's two land answers.

## Community check

EDHREC: **19.5% of Aesi decks (3,354/17,236)**, 14.8% of Tatyova decks,
29.6% of Kodama of the East Tree decks. So I'm saying yes where most Aesi lists
don't run it. My independent reason is the audit's measured lands-in-hand gap,
not its popularity.
