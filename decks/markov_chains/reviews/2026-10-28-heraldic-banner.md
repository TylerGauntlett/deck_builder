# markov_chains — Heraldic Banner (2026-10-28)

**Verdict: NO.** Both halves of the card add to categories the deck already has
plenty of. The anthem half would be the 19th pump effect, and it is the same
case already made against Door of Destinies (2026-08-31): none of the deck's ten
drain payoffs reads power. The mana half is a 6th rock that makes only black,
in a deck whose problem colours are white and red. There's also no cut to pay
for it.

## The card (Scryfall, fetched 2026-10-28 14:59 UTC)

> **Heraldic Banner** `{3}` — Artifact
> As this artifact enters, choose a color.
> Creatures you control of the chosen color get +1/+0.
> {T}: Add one mana of the chosen color.

Colourless · Commander legal · not a Game Changer · EDHREC rank 849.
Ruling: you must choose one colour. "Multicolor" isn't an option.

## Steel-man

Choose black. That covers 34 of the deck's 37 creatures. The only non-black ones
are Charismatic Conqueror, Forerunner of the Legion and Welcoming Vampire.
Edgar's eminence token (*"create a 1/1 black Vampire creature token"*) is black
too. So it's effectively a team-wide +1/+0 that also ramps from 3 mana to 5 on
turn 4. It's one card serving two roles, and it does it for $0.34.

## The tests

**Anthem half: adds to the deck's deepest category.** The 2026-09-03 review counted
18 anthem/pump effects. That review rejected Vanquisher's Banner as the 19th, and
the 2026-08-31 review rejected Door of Destinies as the 7th static anthem. The
reason given there still holds: *"Ten drain payoffs. Zero of them read power."*
When Edgar is answered, the deck falls back to aristocrats. In that mode, +1/+0
does nothing. It also adds no toughness, so it doesn't save tokens from
1-damage sweepers or pings.

**Mana half: the wrong colour.** The deck runs 5 rocks: Sol Ring, Arcane Signet,
Talisman of Conviction, Talisman of Hierarchy and Talisman of Indulgence. The
shape review set the mana pillar at "hold". The deck's pips are B 63 / W 19 /
R 4. Black is the one colour it never struggles to find. Edgar costs
`{3}{R}{W}{B}`, and the Talismans and Signet fix toward red and white. Banner
can't. Swapping a Talisman for Banner would trade fixing for a mono-black rock
in a three-colour deck.

**Curve.** 3-drop is the most crowded slot in the deck.

**Cut.** There isn't a cuttable card. Forerunner of the Legion is already spent
on Gas Guzzler (today's review). Bloodthrone Vampire stays, for the reason the
2026-09-04 review gave: free sac outlets are what make Grave Pact work. Swapping
out a Talisman would hurt the mana, as above.

**Speed premise.** The verdict doesn't depend on how fast games run. In short
games, the anthem would be one of 19. In long games, the drain mode decides more
of them and the anthem matters even less.

**Bracket and combos.** `combos.py --add` finds 0 new combos and 0 near
combos.

**EDHREC.** Its top homes are go-wide token commanders: Krenko 23.2%, Giada
17.2%, Ovika 45.4%. No Edgar Markov figure is listed on the card's page.

## What would change it

Cutting two of the existing static anthems for it. That would be a sidegrade to
weigh then (a weaker anthem in exchange for ramp), not an add.

## Price

$0.34 (foil $0.46), fetched 2026-10-28 14:59 UTC. The NO survives the card being
free.

## Sources
- `card_facts.py lookup "Heraldic Banner" "Edgar Markov" "Talisman of Indulgence" --deck markov_chains --rulings`, 2026-10-28 14:59 UTC.
- `edhrec.py card "Heraldic Banner" --deck markov_chains`.
- `combos.py markov_chains --add "Heraldic Banner" --near`: baseline 2; 0 new, 0 near.
- Creature colours and rocks counted from `decks/markov_chains/cards.json`.

`base.txt` was not modified by this review.
