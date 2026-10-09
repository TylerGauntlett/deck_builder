# markov_chains — Bloodline Recollector (2026-10-09)

**Verdict: ADD — cut Vampire Nocturnus.**

Deck state: `base.txt` and `cards.md` both last changed 2026-10-02 (in sync). 100
cards, 34 lands + Malakir Rebirth MDFC. Bracket 3, $40/card cap. None of the
2026-10-02 shape review's swaps have been applied yet — Vampire Nocturnus, Forerunner
of the Legion, Bloodthrone Vampire and Malakir Bloodwitch are all still in the list.

## The card (Scryfall, fetched 2026-10-09 16:04 UTC)

**Bloodline Recollector** `{1}{B}` — Creature — Vampire Warlock 2/2
> At the beginning of each end step, if three or more creatures died this turn, this
> creature becomes prepared. (While it's prepared, you may cast a copy of its spell.
> Doing so unprepares it.)

**Ancestral Craving** `{B}` — Instant
> Target player draws three cards and loses 3 life.

Colour identity B · Commander legal · not a Game Changer · EDHREC rank 14,534.
(The 2026-08-31 structural audit recorded it as *not legal*; it was pre-release then.
It is legal now.)

Scope read on the four axes:

| Axis | Reading |
|---|---|
| Whose permanents | "three or more **creatures** died" — any creatures, any controller, tokens included |
| Whose turn | "**each** end step" — your turn and every opponent's |
| Targeted | Ancestral Craving targets a *player*; normally yourself |
| Who chooses | you choose whether to cast the copy |

Rulings that matter:
- Preparation cards are cast from hand only as the creature; Ancestral Craving is
  reachable only through the prepared copy.
- The copy exists only "for as long as that permanent is on the battlefield and is
  prepared." If Recollector dies or is sacrificed while prepared, the draw is lost —
  cast it in response to removal, and never sacrifice it to its own trigger's fuel.
- Can't be prepared twice at once; one copy per end step at most.

## Honest best case

A 2-mana Vampire (so it is also an Edgar eminence token) that turns the deck's
already-planned sacrifice turns — and opponents' Grave Pact / Anowon / combat deaths —
into three cards for `{B}`, repeatably, at instant speed. That is a claim that could be
false, so the counts:

**What switches it on (from verified text):**

| Group | Cards | Notes |
|---|---|---|
| Free, unlimited sac outlets | Viscera Seer, Carrion Feeder, Bloodthrone Vampire | 3 tokens → 3 deaths, no mana, any turn (instant speed) |
| Free, once per turn | Phyrexian Tower, Master of Dark Rites | tap-limited |
| Mana sac outlets | Edgar, Ancient Bloodlord `{2}`, Indulgent Aristocrat `{2}`, Baron Bertram Graywater `{1}{B}` | 3 deaths ≈ 6 mana — only incidental |
| One card → 3+ deaths | Grave Pact (each own death → "each other player sacrifices a creature"), Anowon (your upkeep: "each player sacrifices a non-Vampire creature"), Henrika mode 1 (once), Soul Shatter ("each opponent sacrifices"), Olivia's Wrath | Grave Pact + one sac = up to 4 deaths |
| Death-for-value enablers | Skullclamp (+1/−1 kills a 1/1 token), Village Rites, Sorin +1, High-Society Hunter attack | each adds one death |

Plus four-player combat, which happens on turns that aren't yours and still counts.

**What each death already pays for** (so the 3 deaths are rarely a pure cost):
Blood Artist, Cruel Celebrant, Bastion of Remembrance, Vein Ripper, Elenda, Cordial
Vampire, Blade of the Bloodchief; Mirkwood Bats on token sacrifice; Skullclamp if
equipped. Three verified interaction partners is the synergy floor — this clears it
on the switch-on side (Viscera Seer, Grave Pact, Anowon) and the payoff side (Blood
Artist, Cruel Celebrant, Vein Ripper) independently.

## The tests

**Redundancy — effect × frequency × duration.** The deck's death→card converters:

| Card | Effect | Frequency | Counts tokens? | Counts opponents' creatures? |
|---|---|---|---|---|
| Skullclamp | 2 cards per equipped death | unlimited, `{1}` each | yes (equipped only) | no |
| High-Society Hunter | 1 card per death | unlimited | **no** — "another **nontoken** creature" | yes |
| Baron Bertram | 1 card | `{1}{B}` + sac each | yes | no |
| Village Rites | 2 cards | once | yes | no |
| **Bloodline Recollector** | 3 cards for `{B}` | ≤1 per end step | **yes** | **yes** |

Not redundant: it is the only converter that reads token deaths *and* opponents'
deaths without a per-death mana cost. Skullclamp is the better rate per token, and
the two stack (three clamp deaths = 6 cards *and* prepares Recollector).

The general card-flow category is deep (13 sources, 11 repeatable, per the
2026-09-07 count, including Necropotence). That is the strongest argument against —
this is an additive card in a deep category. What carries it past that is the cut:
it isn't competing with a draw card, it is replacing the weakest amplifier.

**Density.** 3 free unlimited outlets + 5 one-card mass-death effects + 2 tap-limited
outlets = 10 cards that, alone with Edgar tokens, reach three deaths in a turn. Plus
combat. Below a third of the deck, but this isn't a card that's dead without them —
see worst case.

**Two modes.** This deck runs go-wide combat *and* aristocrats. Recollector serves
both: in the combat mode it is a turn-2 Vampire + eminence token buffed by five lords,
and attacks into blockers produce deaths on both sides that prepare it; in the grind
mode it is a card engine. It is a bridge card, not a single-mode card.

**Marginal impact.** Long games in this pod (recorded 2026-08-30, not contradicted
since) are where the deck runs out of gas after trading its board; Recollector turns
the trade itself into a refill. It does **not** fix the deck's standing structural
hole — post-wrath recovery — because it dies in the wrath. Only if already prepared
can you cast Ancestral Craving in response.

**Cost of entry.** MV 2, one `{B}` pip. Curve now 1:12 · 2:13 · 3:20 · 4:13 · 5:5 ·
6:3. Swapping Nocturnus (MV 4, `{B}{B}{B}`) for Recollector moves one card 4→2 and
drops two black pips (66 → 64).

**Anti-synergy.** 3 life per cast shares a budget with Necropotence, painlands,
Talismans, War Room, Voldaren Estate and Anguished Unmaking — real, but the same
sacrifices that prepare it usually gain life (Blood Artist, Cruel Celebrant, Bastion,
Vein Ripper, Edgar Ancient Bloodlord). No nonbo found with Vito / Blight-Priest /
Conqueror (losing life triggers none of them). Teferi's Protection makes the life loss
not happen — harmless.

**Worst case.** Opening hand, on the draw: a 2-mana 2/2 Vampire plus eminence token
on turn 2 — never dead. Turn 12 on an empty board: a 2/2 and a token, and the
trigger needs three deaths it may not get. Weak topdeck, not a blank.

**Bracket fit.** Not a Game Changer, no tutor, no fast mana. Commander Spellbook:
`combos.py --add` completes **0** new combos and puts **0** in reach. Constraints
untouched.

**Disagreement check.** EDHREC: **4.4%** of Edgar Markov decks (684 / 15,484 in its
new-card window), synergy +0.04. I'm saying yes and the community is mostly saying
not yet. Two honest reasons this deck differs: (1) the card's rulings are dated
2026-08-21, so it has weeks of data, not years; (2) this list runs Grave Pact, Anowon,
Soul Shatter and three free outlets — far more death density than the typical
go-wide Edgar build, which is exactly what the trigger reads. If (2) is wrong in
practice — if you rarely see three deaths before end step — the community is right
and the card should come back out.

## The cut

Spells for a spell; lands untouched.

1. **Vampire Nocturnus — cut.** `{1}{B}{B}{B}`: *"As long as the top card of your
   library is black…"* Only 43 of 99 library cards are black (the 2026-10-02 shape
   review's count; lands are colourless cards), so it is off more often than on, and
   it reveals your top card all game. Amplifiers are the deck's deepest tier (17). No
   review has recorded a reason to keep it. It was the shape review's first cut too.
2. **Malakir Bloodwitch — runner-up.** One-shot 5-drop drain in a 12-card payoff
   tier. Its earlier case (protection from white against an all-white pod) retired
   with the pod premise on 2026-09-07. Take this cut instead if Nocturnus is already
   spent on Twilight Prophet.
3. **Forerunner of the Legion — spared.** The 2026-10-02 shape review proposed
   cutting it for this exact card, but it was spared on 2026-09-06/07 as **the deck's
   only tutor**, with the note that the case *strengthens* under a rotating pod. The
   shape review didn't engage that reason, and nothing has changed since. It stays
   unless you overrule.
4. **Bloodthrone Vampire — spared.** It is one of the three free, unlimited sac
   outlets that prepare Recollector. Cutting it to fit Recollector removes a third of
   what switches it on.

**Aggregate if taken:** curve 4:13→12, 2:13→14; black pips 66→64; amplifiers 17→16;
card flow +1; Vampire count unchanged (Vampire for Vampire); Game Changers 2/3
unchanged.

**Batch note:** if you also take the shape review's Twilight Prophet, that is two
card-advantage adds into a category already 13 deep. Each is defensible alone; with
both, draw stops being the constraint and the third-best cut (Forerunner) is a card
I'd defend. Don't go past two.

## Price

$5.24 (foil $6.57), fetched 2026-10-09 16:04 UTC — under the $40 cap. (The shape
review quoted $7.03 on 2026-10-02.) The verdict doesn't depend on price: it survives
the card being free and doesn't strengthen if it were.

Other prices this session (fetched 2026-10-09 16:06 UTC): Vampire Nocturnus $5.95 ·
Forerunner of the Legion $1.26 · Bloodthrone Vampire $0.14 · Champion of Dusk $0.24.

## Alternative considered

**Champion of Dusk** `{3}{B}{B}` — *"you draw X cards and you lose X life, where X is
the number of Vampires you control."* 43.2% of Edgar decks (22,296 / 51,609), a
past cut (2026-08-30, for Anowon). A one-shot burst at MV 5 into the five-slot,
against Recollector's repeating engine at MV 2. Not redundant in either direction;
Recollector fits the curve and the death count. Champion remains the pick if you'd
rather have a guaranteed burst than a conditional engine.

## Goldfish checks

- How many end steps per game does it actually get prepared without Grave Pact or
  Anowon out?
- Do you end up holding it unprepared because you won't spend three tokens? If so,
  the trigger is reading the wrong deck.
- Life total after a Necropotence turn plus an Ancestral Craving.

## Sources used

- `card_facts.py lookup --rulings --deck markov_chains`, 2026-10-09 16:04–16:06 UTC.
- `edhrec.py card "Bloodline Recollector"`: Edgar Markov 4.4% (684/15,484), synergy
  +0.04. `edhrec.py commander --diff`: Champion of Dusk 43.2% (22,296/51,609),
  Forerunner 34.6% (17,881/51,609), Nocturnus 17.2% (8,858/51,609).
- `combos.py --add "Bloodline Recollector" --near`: baseline 2 assembled; 0 new, 0
  near.
- Deck counts from `decks/markov_chains/cards.json` (oracle-text scan).
