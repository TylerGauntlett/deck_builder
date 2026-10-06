# Call Damage Control replacements — lander_commander (Aesi, Tyrant of Gyre Strait)

Bracket 3, 4-player casual, $40/card cap. Candidates proposed by the user, all
already owned: Turntimber Symbiosis, Through the Forest Gate, Carnivorous
Cultivator. All oracle text, legality and prices fetched **2026-10-06 02:11–02:14
UTC** via `card_facts.py lookup`. Deck counts below are script output against the
current `base.txt` (unchanged since the 2026-09-04 `cards.md` build; none of the
2026-08-31 audit's seven swaps have been applied).

## Premise carried over from the 2026-08-31 weakness audit

Pod games run **turns 9–12**; threats are combo/spell kills, go-wide combat, mill
and aristocrats. No verdict below is a "too slow" rejection, so this premise is
not load-bearing for any NO. It *is* load-bearing for the one ADD at MV8.

## What Call Damage Control actually does here

`{1}{G}` sorcery, up to two of: artifact, creature, enchantment, land card from
graveyard to hand. In this list the deck's own cards that put lands into the yard:

- **8 self-sacrificing lands**: Blighted Woodland, Evolving Wilds, Fabled Passage,
  Field of Ruin, Ghost Quarter, Myriad Landscape, Terramorphic Expanse, Waterlogged
  Grove (plus Coral Atoll and Jungle Basin, which sacrifice only if you can't bounce).
- **Already play lands from the graveyard**: Ramunap Excavator, Ancient Greenwarden
  (2 engines). CDC's land mode is the one-shot version of what these do forever.
- Nonland recursion in the 99: **1** (CDC itself). Cutting it without a recursion
  card takes the category to 0. The audit's role-for-role replacement was Eternal
  Witness; that stands and is restated at the end.

## Carnivorous Cultivator // Enroot — NO

**Verified text.** `{1}{G}` 2/3 deathtouch, "enters prepared". On combat damage to
a player, return target land card from your graveyard to your hand. Enroot (`{G}`
sorcery): search your library for a land card, put it into your graveyard, shuffle.
Rulings (2026-08-21): entering prepared creates a castable copy of Enroot in exile
for as long as the creature stays on the battlefield and prepared; casting it
un-prepares the creature.

**Honest best case.** Three mana total buys a 2/3 deathtouch body plus a one-shot
"tutor any land into the graveyard", and the deck has two permanents (Ramunap
Excavator, Ancient Greenwarden) that then play that land straight from the yard.

**What killed it.**
- *Density.* The Enroot line needs one of exactly **2** cards to do anything on the
  turn it is cast. Without them the land sits in the yard until a 2/3 connects
  through a go-wide board in a four-player pod.
- *Redundancy, rate × duration.* Ramunap Excavator and Ancient Greenwarden are
  repeatable "lands from graveyard" engines. Cultivator's trigger is one land per
  hit, to **hand** not battlefield, gated on combat damage. It is strictly the slower
  version of a job two cards already do without conditions.
- *What is there to tutor?* The nonbasic suite is duals, fetches, Reliquary Tower,
  Field of Ruin, Ghost Quarter, Blighted Woodland, Myriad Landscape. No land in the
  99 is worth a tutor slot.
- *Disagreement check.* EDHREC rank 19804; not present on the Aesi commander page,
  Lands Matter page or Landfall page. The community is not missing anything.
- Price $0.44 (2026-10-06). Owned. The rejection survives the card being free.

## Turntimber Symbiosis // Turntimber, Serpentine Wood — ADD, replacing a basic Forest (not CDC)

**Verified text.** Front: `{4}{G}{G}{G}` sorcery, look at the top seven, you may put
a creature from among them onto the battlefield (+3 counters if MV ≤ 3), rest on
the bottom. Back: land, pay 3 life or enters tapped, `{T}: Add {G}`.

**Honest best case.** It is a Forest that is never a dead draw: late game it is a
7-mana "put one of the top seven's creatures onto the battlefield" with 28 creatures
in the 99 (12 at MV ≤ 3 and eligible for the counters). From a full library the top
seven contains at least one creature about 91% of the time. Live hits: Craterhoof
Behemoth (haste, ETB pump), Avenger of Zendikar, Terastodon, Mossborn Hydra (enters
with 4 counters and doubles on every landfall).

**Why it is a land swap, not a CDC swap.** The deck runs **44 lands** at average
nonland MV 3.7. Putting an MDFC in a spell slot is a 45th land. Nothing in the
audit or in this list says the deck is short on lands; it says the deck is short on
*lands in hand relative to extra land drops* (4 land-to-hand effects vs 6
extra-drop effects), and a 45th land in 100 moves that by about one percent. The
honest comparison is Turntimber vs **a basic Forest**, and against a Forest it is a
small, free upgrade: same colour, same count, a 7-mana mode bolted on.

**Costs, stated.** Can't be found by the 10 basic-land fetchers (Cultivate,
Kodama's Reach, Rampant Growth, Search for Tomorrow, Evolving Wilds, Terramorphic
Expanse, Fabled Passage, Myriad Landscape, Blighted Woodland, Field of Ruin); 13
Forests + 12 Islands remain, so that is fine. Untapped on curve costs 3 life, in a pod
with go-wide combat and aristocrats. Dryad of the Ilysian Grove makes the basic
land type irrelevant either way.

- EDHREC: rank 2320; 8.5% of Azusa decks (629/7380), 10.2% of Ghalta decks
  (973/9578); not on the Aesi commander page lists. `combos.py --add`: 0 new combos.
- Price $4.10 (2026-10-06). Owned. Not load-bearing.
- **Cut: one basic Forest.** Land count stays 44, green sources unchanged.

## Through the Forest Gate — ADD, cutting Ghalta, Primal Hunger

**Verified text.** `{6}{G}{G}` sorcery. Look at the top twenty cards, put any number
of land cards from among them onto the battlefield tapped, shuffle. Gain 8 life.

**Honest best case.** With 44 lands in 99, the top twenty holds roughly 8–9 lands
in a mid-game library. They all enter at once, so **every landfall payoff on the
battlefield triggers ~9 times**, and the commander is one of them. The audit found
the deck's real bottleneck is land drops limited by lands in hand; this card
bypasses the hand entirely.

**Payoff density, by verified clause ("whenever a land you control enters"):**
Aesi (commander, "you may draw a card"), Tatyova ("gain 1 life and draw a card",
not optional), Avenger of Zendikar (+1/+1 on each Plant), Rampaging Baloths (4/4
Beast), Scute Swarm (1/1 or a Scute copy at 6+ lands), Greensleeves (3/3 Badger),
Zendikar's Roil (2/2 Elemental), Springheart Nantuko (Insect or a copy), Lotus Cobra
(one mana), Tireless Provisioner (Food or Treasure), Mossborn Hydra (double
counters). That is **11 landfall cards in the 99** plus Ancient Greenwarden, whose
"triggers an additional time" clause doubles all of it, and Kodama of the East Tree,
whose "another permanent you control enters" fires once per land and lets you drop
a land from hand each time. With Aesi alone it is "ramp 9, draw up to 9, gain 8"
for eight mana. With Aesi plus Baloths it is nine 4/4s. With Lotus Cobra the nine
lands also pay for the next spell the same turn.

**Attacks, and what survived.**
- *Redundancy.* The only comparable effect is Cultivator Colossus (MV7), which puts
  lands from **hand** one at a time and draws between them, so it is hand-limited
  exactly where this is not. No Splendid Reclamation, no Scapeshift. Not redundant.
- *Marginal impact.* It is not only win-more: after a sweeper you still have the
  lands and a re-castable commander, and this refills the hand and rebuilds the
  board in one cast. It does nothing against a combo player, which is the audit's
  standing weakness and is unchanged by this review.
- *Cost of entry.* MV8 in a 99 that already has **11 cards at MV6+** (12 counting
  Aesi). That is the real price, and it is why the cut has to come from the same
  band, below.
- *Worst case.* Dead in the opening hand for seven turns; so are the other eleven.
  On turn twelve with an empty board it is one of the best topdecks in the deck.
- *Anti-synergy.* Shuffles away Oracle of Mul Daya's revealed top card (minor).
  Tatyova's draw is mandatory, so Tatyova + this is a forced 9 draws, 18 with
  Greenwarden. The audit already flagged decking as a live risk in a pod with a mill
  deck; this card also removes ~9 lands from the library. Not a veto in a 75-card
  mid-game library, but it is the first card in the list that makes Gaea's Blessing
  worth revisiting if a game is actually lost to decking.
- *Bracket.* Not a Game Changer. `combos.py --add`: 0 new combos. Bracket 3 holds.
- *Disagreement check.* Aesi commander page 10.1% (319/3144, synergy +0.06); Lands
  Matter 10.7% (42/391, +0.07); Landfall 14.4% (30/208, +0.11). Listed under "New
  Cards" on all three. Mildly positive, rising with how land-focused the list is.
  What this deck has that the average does not: 11 landfall payoffs plus a doubler,
  which is the multiplier the card needs.
- Price $1.09 (2026-10-06). Owned. Not load-bearing.

**The cut.** Same role (top-end nonland), ranked:

1. **Ghalta, Primal Hunger** — `{10}{G}{G}`, 12/12 trample, no landfall, no ETB, no
   land text. Third finisher behind Craterhoof Behemoth and Overwhelming Stampede,
   and only cheap when the board is already winning. The 2026-08-31 audit already
   named it as a cut (for Aetherize); if you later take that swap too, move to #2.
2. **Jin-Gitaxias, Progress Tyrant** — MV7 `{5}{U}{U}`, zero land synergy. Spared as
   runner-up only because its "whenever an opponent casts an artifact, instant, or
   sorcery spell, counter that spell" clause is the deck's one repeatable piece of
   anti-spell interaction in a combo pod, even at once per turn.
3. **Call Damage Control** — the slot you asked about. It works, but it trades a
   2-drop for an 8-drop (MV6+ in the 99 goes 11 → 12) and takes nonland recursion to
   0. Not wrong, just worse than #1 for the same card coming in.

## Aggregate delta if you take both ADDs (Turntimber for a Forest, Forest Gate for Ghalta)

- Lands 44 → 44. Green sources unchanged.
- MV6+ in the 99: 11 → 11 (Ghalta out, Forest Gate in). Average nonland MV falls
  slightly (12 → 8 in that slot).
- Landfall-burst effects: 1 (Cultivator Colossus, hand-limited) → 2.
- Nonland recursion: 1 → 1. Call Damage Control is **not** cut by this review.
- Game Changers 2 → 2. Combos 6 → 6.

## On the Call Damage Control slot itself

None of the three candidates does CDC's job, so this review does not replace it;
it finds a better home for two of them. If you still want CDC out, the
role-for-role card is unchanged from the audit: **Eternal Witness** (`{1}{G}{G}`
2/1, "you may return target card from your graveyard to your hand"; 43.6% of Aesi
decks, 7523/17246; $2.15 on 2026-10-06). It returns any card type, including
Cyclonic Rift or Finale of Devastation, and it is a creature Finale can fetch.
CDC's edge is rate: two cards for two mana when a sacrificed fetch land and a dead
creature are both in the yard, which with 8 self-sacrificing lands is common. That
is a real argument for keeping CDC; it is not an argument for any of the three
cards above.
