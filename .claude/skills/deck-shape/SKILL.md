---
name: deck-shape
description: Analyzes and reshapes a Commander deck under decks/ by its structural "shape" — the deck's clear objective, the role every card plays (generator, amplifier, payoff, advantage gainer), and the three support pillars (card advantage, mana advantage, board-state advantage). Use when asked why a deck underperforms, to raise a deck's bracket or consistency without spending much, for a structural or "shape" review, or to plan a batch of cuts and adds around a deck's plan rather than judging single cards.
---

# Deck shape

A deck rarely underperforms because its cards are weak. Far more often, the cards
sit in the **wrong proportions**: too many cards doing the base thing, too few
making that thing matter, no clear way to turn it into a win, and support pillars
filled with generic goodstuff instead of cards that feed off the deck's own plan.
Fixing the proportions — the *shape* — usually raises power more, and costs less,
than buying stronger cards.

This skill diagnoses a deck's shape and proposes a reshape. It works on the
**whole list at once**. For a verdict on one specific card, hand off to the
`mtg-deck-advisor` skill, whose rules (verify every card via Scryfall, default-NO,
name the cut, never edit `base.txt`) apply here too.

> There are no hard rules in deck building. Everything below is a lens, not a law.
> Odd commanders, blurry roles and multi-layered plans are normal. The final word
> is always play-testing.

## Ground rules

- **Classify cards from verified text, not memory.** Read `decks/<deck>/cards.md`
  (regenerate with `python scripts/build_card_details.py <deck>` if `base.txt` is
  newer). For any card not in the deck, run `python scripts/card_facts.py lookup
  "<name>" --deck <deck>` before citing it.
- **Load the deck's context first:** `python scripts/deck_meta.py show <deck>`.
  Bracket, budget, constraints and the pod description all change the right shape.
- **Every count gets card names behind it.** "14 generators" is worthless without
  the list; a reader must be able to dispute any single classification.
- **Never modify `base.txt`.** Propose; the user decides.

## Procedure

### 1. State the keystone (the clear objective)

What separates a muddled deck from a focused one is a **clear way to win**. Write
the objective as three linked parts:

1. **Primary action** — the thing the deck does most turns (make tokens, place
   +1/+1 counters, mill itself, cast spells, set up a loop...).
2. **Capitalization** — how the deck cashes that action in for something bigger
   (e.g. tokens → a "put a permanent from your library onto the battlefield for
   each permanent you control" spell; self-mill → a mass reanimation spell).
3. **Conversion to a win** — what actually ends the game or creates an
   insurmountable lead *off the back of* the capitalization. A capitalization card
   that doesn't itself win needs specific follow-through cards that do.

Then check the follow-through cards **against the exact mechanics of the
capitalization**. This is where nonbos hide: a card that only works if the
commander stays on the battlefield, an enchantment payoff that enters *after* the
creatures it was meant to see, a trigger that needs to already be in play when the
tokens arrive. Quote the clause that makes it work or fail.

If you cannot write the three parts from the list, that *is* the top finding —
the deck has no keystone and every later step will be guesswork. Propose one built
from what the deck already does best, and confirm it with the user before
reshaping around it.

### 2. Classify every non-land card by role

| Role | Definition | Quick test |
|---|---|---|
| **Generator** | Does the deck's primary action | Remove all of them and the deck does nothing at all |
| **Amplifier** | Makes generators do more (doublers, extra copies, extra triggers, enablers) | Does nothing on its own; multiplies something else |
| **Payoff** | Wins the game given a sufficient board | "If I resolve this with my board set up, do I win?" |
| **Advantage gainer** | Card advantage, mana advantage, or board-state advantage (removal, protection) | Supports *any* plan; belongs to a pillar below |

Notes for classifying:

- **Context decides the role, not the card in isolation.** A card that looks like
  a generator can act as an amplifier when it only rides on what the commander
  already does (e.g. an attack-trigger curse in a deck that only ever attacks with
  its commander). Equipment that only improves the commander's attacks is an
  amplifier.
- **Payoffs can have layers.** A deck may have capitalization payoffs and
  win-condition payoffs beneath them. Note whether the win-condition layer also
  wins *without* the capitalization — that's resilience.
- **Cards can hold two roles.** Record the primary one and flag the secondary; do
  not double-count in totals.
- **Classify the commander(s) too.** It decides the shape (step 3). A commander
  that fills no role is a figurehead; the shape is then set by the plan alone.

### 3. Determine the target shape

The baseline structure is a stack — **generators** at the base, **amplifiers**
improving them, **payoffs** on top (naturally the fewest) — held up by three
**pillars**: card advantage, mana advantage, interaction/protection.

Two things bend that baseline:

**The commander.** You always have access to it, so **shrink whichever category it
fills** and spend those slots elsewhere:

| Commander is a... | Shrink | Resulting shape |
|---|---|---|
| Generator | Other generators | **Diamond** — few generators, many amplifiers, few payoffs |
| Amplifier | Other amplifiers | **Inverted triangle / T** — broad generator base |
| Payoff | Other payoffs (often to near zero) | **Rectangle with a point** — generators and amplifiers, one payoff on top |
| Advantage gainer | The pillar it supports | Baseline stack with that pillar thinned |
| Several roles | Each role it fills, proportionally | Judge case by case |

**The plan.** Then adjust each section for what the keystone needs:

- Generators + amplifiers already win on their own → cut payoffs.
- Plan is mana-hungry → thicken mana advantage. Plan needs to dig for specific
  pieces → thicken card advantage.
- Deck is slow to come online → thicken interaction/protection.

Write the target as a direction per section (↑ / ↓ / hold) with a reason. Exact
numbers come from the current list and the deck's goals, not from a template.

### 4. Map current vs target

Lay out the current counts per role and per pillar, with names, next to the
target direction. The gaps are the reshape. Typical finding in a struggling deck:
far too many generators (often doubling up on what the commander already does),
a handful of amplifiers, and payoffs that don't connect to the capitalization.

### 5. Cut, guided by shape then synergy

Cut in this order:

1. **The overstuffed category first** — usually generators when the commander is
   a generator.
2. **Within it, cut what has the least synergy with the keystone.** Concretely
   check: Does it come down when the plan wants it (early for engines)? Does it
   compete for the same mana-value slot as the capitalization cards? Does it do
   anything when the capitalization resolves (e.g. an ETB when permanents are
   spilled onto the battlefield)?
3. **Expensive cards get no exemption.** A high-power, high-price card that
   doesn't serve the keystone is often the *first* cut — and the budget it frees is
   a bonus.
4. **Known trap cards** — effects that read powerfully but cost a whole turn of
   tempo and under-deliver in practice.
5. Duplicates and illegal or accidental inclusions (check quantities in
   `base.txt`).

Note when a cut removes a card from an under-filled category; it must be
replaced in kind.

### 6. Add toward the target shape

Prioritise the categories the target says to grow (amplifiers, in a diamond).
Take a strong card from a shrinking category only if it clearly beats one already
there, and swap one-for-one. Use `python scripts/card_facts.py search '<query>'
--deck <deck>` to find candidates, and `python scripts/edhrec.py` as a sanity
check, not a source of truth.

### 7. Rebuild the three pillars through synergy

This is the cheapest, highest-impact upgrade. Generic staples in each pillar are
expensive because every deck in those colours wants them. The alternative is
cards that **convert the deck's own primary action into advantage** — they are
usually cheaper *and* stronger here than the generic version.

**Card advantage.** A deck aiming for bracket 3–4 must be able to dig for its
answers and its win. Replace low-synergy draw and tutors with **high-synergy dig**:
cards that turn the deck's primary action into cards (e.g. in a treasure/token
deck: sacrifice a treasure to impulse-draw; draw when you've made a token this
turn; loot or filter whenever an artifact enters). Cut expensive draw that the
synergy version outperforms.

**Mana advantage** — three distinct kinds; check the deck has the right mix:

- *Basic ramp* — gets you ahead of curve (a two-drop mana rock).
- *Explosive ramp* — a burst of mana in a single turn.
- *High-synergy mana* — leverages the plan for large mana every turn (e.g.
  improvise in an artifact-token deck, making food or other tokens tap for mana,
  doubling what tokens produce).

If the primary action already makes mana that the plan wants to spend elsewhere,
dedicated ramp still matters.

**Board-state advantage.** Its job is to ensure your board ends up more valuable
than everyone else's — by suppressing opponents and protecting yourself. Decide:

- **How much?** Fast or explosive decks that win suddenly need less; grindy
  out-value decks need more. Then judge **resilience** — how hard the deck is to
  stop and how well it keeps you alive. Ward or hexproof on the commander,
  key pieces being non-creature permanents, and fast rebuilding (e.g. from
  treasure) all reduce the need. Fragile decks need more.
- **Which ratio?** A loud, scary deck that is constantly attacking needs more
  **protection** (including a way to save the whole board). A deck that sits under
  the radar accumulating value needs more **suppression** to remove threats before
  they win.
- **Flexible vs efficient.** If the deck has surplus mana, prefer catch-all
  answers over cheap narrow ones.
- **Redundant protection.** Cut protection the commander already provides itself
  (e.g. haste/hexproof equipment on a commander that already has ward).
- **The overwhelming-interaction effect** — the most often missed and the most
  game-winning. Look for interaction that, in *this* deck, is effectively a win: a
  one-sided-in-practice wipe, removal that scales with surplus mana into lethal, a
  wipe that also leaves you resources. It doesn't have to be the expensive famous
  version; synergy does the work. Flag any that edge into mass land destruction
  and check them against `meta.json` constraints and bracket rules, offering a
  softer alternative.

Also scan for **glaring weaknesses** the shape exposes (e.g. no lifegain at all in
a deck that takes a lot of damage) and spend one slot on it if it's cheap.

### 8. Count and validate

- Confirm 100 cards including commanders, and that the land count still fits the
  curve after the reshape.
- Recompute role and pillar counts and show before → after.
- Re-check the result against `meta.json`: bracket, Game Changer cap, budget,
  house rules. A reshape can make a deck *too* fast for its bracket.
- **Recommend goldfishing** with these checks, since only play reveals the true
  shape: Does it feel consistent? Is it drawing enough? Are pieces landing on
  time? On which turn does it present a win? Then adjust for real-table friction
  the goldfish can't see (e.g. a commander trigger that requires attacking a
  specific opponent will slow real games by a turn or two).

### 9. Report

Give the summary in the terminal, then save the full analysis to
`decks/<deck>/reviews/YYYY-MM-DD-shape.md` using this layout:

```markdown
# <deck> — shape review (YYYY-MM-DD)

## Keystone
- Primary action:
- Capitalization:
- Conversion to a win:
- Nonbos found:

## Commander role → target shape
<role(s)>, so <shape>. Plan adjustments: ...

## Current vs target
| Section | Now | Target | Cards |
|---|---|---|---|
| Generators | n | ↓ | ... |
| Amplifiers | n | ↑ | ... |
| Payoffs | n | hold | ... |
| Card advantage | n | ... | ... |
| Mana advantage (basic / explosive / synergy) | n | ... | ... |
| Interaction (suppress / protect / overwhelming) | n | ... | ... |

## Proposed cuts
| Card | Section | Why (shape or synergy) |

## Proposed adds
| Card | Section | Replaces | Why | Price (fetched <timestamp>) |

## After
Counts before → after, lands, curve, bracket check.

## Goldfish checklist
```

Every proposed add is a candidate, not a verdict: if the user wants a card-level
ruling on any of them, run it through `mtg-deck-advisor`.
