# markov_chains — Authority of the Consuls (2026-10-18)

**Verdict: NO.** It switches off the creature half of Charismatic Conqueror, and
its drain upside rests on 2 cards in the 99.

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
