# markov_chains — Authority of the Consuls (2026-10-18)

**Verdict (revised same day): ADD — cut Malakir Bloodwitch.** The original NO
misread how long "enter tapped" lasts; see *Revision* at the end. The original
analysis is kept below for the record.

~~Original verdict: NO. It switches off the creature half of Charismatic
Conqueror, and its drain upside rests on 2 cards in the 99.~~

## Deck context
Edgar Markov · bracket 3 · $40/card cap · rotating 4-player casual pod (games run
long, per 08-30/08-31 reviews; not contradicted since). Vetoes: no early
infinites, no tutor-dependent win line. This verdict does **not** rest on the
deck's speed premise, so it was not re-confirmed.

## Verified text (card_facts.py, 2026-10-18)
- **Authority of the Consuls** {W} Enchantment — "Creatures your opponents control
  enter tapped. Whenever a creature an opponent controls enters, you gain 1 life."
  Commander-legal, colour identity W (in identity). Not a Game Changer. No rulings.
- **Charismatic Conqueror** {1}{W} — "Whenever an artifact or creature an opponent
  controls enters **untapped**, they may tap that permanent. If they don't, you
  create a 1/1 white Vampire creature token with lifelink."
- **Vito, Thorn of the Dusk Rose** — "Whenever you gain life, target opponent loses
  that much life."
- **Marauding Blight-Priest** — "Whenever you gain life, each opponent loses 1 life."
- **Ghostly Prison** {2}{W} — "Creatures can't attack you unless their controller
  pays {2} for each creature they control that's attacking you."

Scope read: Authority's both clauses are **opponents' creatures**, non-targeted,
every turn, no choice given to the opponent.

## Steel-man
A 1-mana permanent that (a) kills haste against you and makes any blocker an
opponent flashes in or creates during your combat enter tapped — real help for the
go-wide attack plan — and (b) turns every opposing creature ETB into 1 life, which
with Vito or Blight-Priest out is a drain per opposing creature, all game.

## Attack
- **Anti-synergy (decisive).** Authority makes opponents' creatures enter tapped, so
  Charismatic Conqueror's "enters untapped" condition never occurs for creatures.
  The Conqueror's tax-or-token choice — the card's whole function — survives only
  for artifacts. Authority does not add a stax effect to the deck; it replaces the
  creature half of one the deck already has, and the version it replaces is the one
  that *pays you* (a lifelink Vampire token, which is also eminence-adjacent board
  presence and sac fodder) rather than 1 life.
- **Density.** "Whenever you gain life" payoffs in the 99: **2** (Vito,
  Marauding Blight-Priest; grep of cards.md). Bloodthirsty Conqueror converts
  drain into lifegain but needs one of those two to loop. Without either on board,
  Authority's second clause is 1 life per opposing creature — irrelevant in this
  deck.
- **Redundancy (rate × duration).** Defensive taxing is already filled by Ghostly
  Prison (every attack, every turn, forever) and Charismatic Conqueror (every
  opponent ETB, forever). Authority's tap is a one-turn delay per creature — a
  weaker rate than Prison on the same axis.
- **Marginal impact.** The games this deck loses are wraths and board recovery
  (08-31 audit, 10-02 shape). Authority does nothing there.
- **Worst-case draw.** Turn-12 topdeck on an empty board: does nothing to rebuild.
  Opening hand: a fine turn-1 play, mild.
- **Combos.** Commander Spellbook: completes 0 new combos, 0 near-misses
  (baseline 2 assembled).

## Community check
EDHREC overall rank 312. Not present on Edgar Markov's commander page. Top homes
are lifegain/pillowfort decks (Karlov 81.2%, Oloro 66.7%, Amalia 66.1%) — decks
with many "gain life" payoffs and no "enters untapped" card. Disagreement explained:
this deck has 2 such payoffs and runs the card Authority turns off.

## Price
USD $5.03 (foil $5.88), fetched 2026-10-18 10:21 UTC. Under cap. Not load-bearing:
the rejection holds at $0.

## Counter-proposal
None. The roles Authority aims at (opponent ETB tax, early defence) are not a gap —
Charismatic Conqueror and Ghostly Prison already fill them.

## What would change this
- If Charismatic Conqueror leaves the deck, re-run: the nonbo goes away and the
  card becomes a marginal NO on density rather than a firm one.
- If the deck adds two or more further "whenever you gain life" payoffs, the drain
  clause becomes real — re-evaluate then.

---

## Revision (2026-10-18, after user pushback)

**Pushback:** it's one card in the 99, not a curve play; shutting down blockers
and drawing removal for 1 mana is what it's for.

**Sorted as a new axis, and it holds.** The original read Authority's tap as "a
one-turn delay per creature" that mostly catches flash blockers. That is wrong. A
creature an opponent casts in their own main phase enters tapped and **stays tapped
until that player's next untap step**, so it cannot block on any other player's
turn, including ours. In practice: every creature an opponent adds to the board is
unavailable to block our next attack. That serves the combat lane (anthems, Shared
Animosity, Akroma's Will alpha) directly, every turn, at 1 mana, on a permanent
that survives creature wraths.

**The Charismatic Conqueror nonbo, re-measured.** Conqueror's trigger gives the
opponent a choice: tap the new creature (the *same* blocker outcome Authority
forces) or give us a 1/1 lifelink Vampire. With both on board, Authority turns
that choice into a guaranteed tap, so we lose only the token branch, which the
opponent was choosing anyway. And the overlap exists only while a 2/2 creature
survives; Authority keeps working after it dies. The original overstated this as
"replaces the version that pays you." It is a small tax that applies only
sometimes.

**Redundancy, re-measured.** Ghostly Prison taxes attacks *on us* (defence).
Authority stops opponents' *new* creatures from blocking (offence), plus stops
haste attacks at us. Different jobs; not redundant.

**Unchanged from the original:** the lifegain clause is a bonus only. It has 2
payoffs (Vito, Marauding Blight-Priest), and the verdict does not rest on it.
**Not credited:** "draws removal." A 1-mana enchantment soaking an answer that
would have hit a payoff is plausible but not something I can measure; it is
not part of the case.

**Limits, stated plainly:** it does nothing to creatures already on the board, so
in a long game it matters more and more for the *new* blockers and less for the
board already in place. It does not help against wraths (the deck's main way to
lose).

### The cut
1. **Malakir Bloodwitch — cut.** `{3}{B}{B}`, one-shot ETB drain in the payoff tier
   (12, flagged top-heavy on 10-02). Runner-up cut in both the 10-02 shape review and the
   10-09 Recollector review; no review has recorded a reason to keep it since its
   protection-from-white case retired with the pod premise on 09-07. Note what
   leaves: its "you gain life equal to the life lost" does trigger Vito /
   Blight-Priest, so the drain lane loses a 5-drop burst, and the 1-mana card
   coming in carries a small lifegain trigger of its own.
2. **Bloodthrone Vampire — spared.** Spared on 10-09 as one of the three free sac
   outlets that switch on Bloodline Recollector; that reason holds while the
   Recollector add is pending.
3. **Forerunner of the Legion — spared.** The deck's only tutor (09-06/07 reviews);
   unchanged.
(Florian is already earmarked as the Recollector cut; not double-counted.)

**Aggregate:** curve 5-drops −1, 1-drops +1; black pips −2, white pips +1; payoffs
12→11; Vampire count −1 (Bloodwitch is a Vampire; Authority is not, so one less
eminence trigger). Game Changers unchanged. Combos: 0 new (Spellbook, as above).

### Price
Authority of the Consuls $5.03 (fetched 2026-10-18 10:21 UTC). Malakir
Bloodwitch $4.03 (fetched 2026-10-18 18:21 UTC). Not load-bearing either way.
