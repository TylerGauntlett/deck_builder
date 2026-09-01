# The rubric

Work each candidate through this. Steel-man first, then attack. Write down the
answers — a test you skipped is a test the card passed for free.

## Step 0: the honest best case

Before attacking anything, make the strongest argument for the card you can,
using verified text. If you can't construct a real case, stop here and say so;
the analysis is already over.

State the case as a claim that could be false: *"This is the deck's fourth
unconditional sac outlet and the only one that costs zero mana, which matters
because eleven of its payoffs trigger on death."* Not *"it's a strong card."*

## Hard vetoes

Any one of these ends it. No balancing, no "but it's really strong."

**Colour identity.** Outside the commander's identity, it is not legal. Report and
stop. `card_facts.py lookup --deck` flags this for you.

**Format legality.** `Commander legality: legal` or it's out. Check banned lists by
fetching, never by recall.

**`meta.json` constraints.** These are the user's house rules and they are vetoes,
not preferences. Read them literally and apply them literally — a constraint
against *early* infinite combos is not a constraint against combos, and a deck
that already runs late-game infinites has told you where its line is.

**Budget.** Over `budget.per_card_max_usd`, from the live price. If the card is
genuinely worth breaking the cap, say so explicitly and let the user decide — do
not quietly ignore the number.

## The tests

Each of these can sink a card on its own. Answer them with card names and counts,
not adjectives.

**Redundancy — what already does this?**
List the cards in the deck doing this job. If two or more do it comparably well,
reject: the marginal copy of an effect the deck already has is worth far less than
the first. Being the *best* of the redundant options is an argument for a swap,
not for an addition.

**Redundancy compares rate and duration, not just effect.** Before calling
anything redundant, write both cards as *effect × frequency × duration*. "Each
opponent sacrifices a creature" is a different card at once-per-game than at
once-per-upkeep-forever, and a one-shot answer is never redundant with a
repeatable engine in either direction. Two cards are redundant when all three
terms match, not when their effect lines rhyme.

The specific error to avoid: comparing a permanent that *generates* a resource
every turn against a spell that *answers* one threat once, concluding they do the
same job, and rejecting the engine because the answer is cheaper. Ask which one
the opponent must respond to, and what happens on the turns after it resolves.

**Density — how many cards turn this on?**
Count them and name them. A payoff needs enablers; an enabler needs payoffs. Below
roughly a third of the deck for a card that needs support, the card is a
do-nothing in too many draws. If the honest count is four, say four.

**Marginal impact — does it change games you lose?**
The real question. A card that makes winning positions more winning is close to
worthless. Does this improve the deck's bad draws, its slow starts, its losses to
the fast deck in the pod, its resilience to a wipe? If the honest answer is "it's
great when I'm already ahead", that's a no.

Before applying this test, check what it is resting on. "Win-more" and "too slow"
are verdicts about the *deck's speed premise*, and that premise comes from
`meta.json`, which records intent rather than the table. If several rejections in
a batch lean on it, stop and confirm the premise with the user instead of
producing the same wrong verdict repeatedly. A card is only win-more relative to a
clock you have actually established.

**Cost of entry.**
Mana value against the existing curve — the deck's curve, from `cards.md`, not a
theoretical one. Coloured pips against the actual mana base: a `{B}{B}{B}` card in
a three-colour deck is a different card than its text suggests. Count the sources.

**Anti-synergy.**
Nonbos, legend-rule conflicts, symmetric effects that help the table, sacrifice
versus recursion tension, cards that turn off your own triggers, lifegain that
fights an aristocrats plan. Look for these actively; they don't announce
themselves.

**Worst-case draw.**
It's in your opening hand, on the draw, against the fastest deck at the table.
What happens? Then: you draw it on turn twelve with an empty board. Still fine? A
card that's excellent in the middle and dead at both ends is worse than its
average suggests.

**Bracket fit.**
Would it push the deck past `meta.json`'s bracket? Check the `Game Changer` flag
from Scryfall, and watch for fast mana, unconditional tutors, and two-card
infinites. At brackets 1–3 these are costs, not upside.

**The disagreement check.**
Compare your verdict to EDHREC's inclusion %.
- You say no, the community says yes (high inclusion): why is this deck different?
  Name the actual difference. If you can't, your reasoning is probably wrong.
- You say yes, the community says no (low inclusion): what do you see that
  thousands of decks don't? Usually the answer is nothing.
- You agree with a high inclusion: make sure you have an independent reason.
  Agreeing with EDHREC because it's EDHREC is deferring, not analysing.

**Price per unit of improvement.**
From the live figure. A $2 card that is 80% as good as a $40 card is the better
recommendation in almost every deck. Say the dollar figure and the date you
fetched it.

## Cut discipline

A card is not recommended until you name what leaves. Cuts have their own rules:

- **Never cut below the land and ramp count the curve supports.** If the deck runs
  36 lands at an average MV of 2.8, cutting a land to fit a spell is a downgrade
  dressed as an upgrade. Cut a *spell* for a spell.
- **Never cut the last of a role.** If it's the only board wipe, the only
  graveyard hate, the only way to remove an artifact, it stays — even if it's the
  weakest card by raw power.
- **Rank the cut candidates and show the runners-up**, with why each was spared.
  The user knows their deck better than you do and may overrule your pick; give
  them the list to overrule.
- **Prefer cutting within the same role** as the card coming in. That keeps the
  deck's category counts stable, which is what the curve and the mana base were
  built around.
- **The cut has to actually be worse.** If the best cut you can find is a card you
  would defend in any other context, that is strong evidence the addition isn't
  worth it. Say that.

## Preferences

`meta.json.preferences` are **tiebreakers only**, never vetoes. When two cards are
close, the preferred one wins and you say that's why. Never reject a clearly
stronger card for violating a preference — report the trade-off and let the user
choose.

## Writing the verdict

For each candidate:

1. The honest best case, in one sentence.
2. What killed it, or what it survived — with the counts and names.
3. **ADD** (naming the cut), **ADD IF** (naming the condition), or **NO** (one line).
4. If NO but the role it was aimed at is real: the counter-proposal, found with
   `card_facts.py search`, verified the same way.

Prices carry the fetch timestamp. EDHREC figures carry the inclusion count they
came from. Both go in the saved report so the next review can compare.

---

# Failure modes seen in practice

These are real errors from a real review, kept because each one felt like rigour
at the time. Worked example: `decks/markov_chains/reviews/2026-08-30-vampire-seven.md`
(an Edgar Markov review whose verdicts reversed repeatedly under user pushback).

**1. A stale `meta.json` premise producing a batch of identical wrong verdicts.**
The file said "vampire aggro"; the pod actually played long games. Three cards were
rejected as "grind cards in a lean aggressive list." All three were correct adds.
One stale line, three wrong answers, and none of the card-level verification caught
it because none of the *facts* were wrong.
→ When a rejection rests on the deck's speed, confirm the speed.

**2. Comparing an engine to an answer.** A permanent generating a forced sacrifice
every upkeep was compared against one-shot removal spells, judged redundant, and
rejected three separate times. The rejection kept citing that a cheaper spell "does
the same job better." It did not do the same job at all.
→ Compare *effect × frequency × duration*.

**3. Counting a category on the wrong clause.** Death triggers were tallied against
"a creature **you control** dies" while the argument actually depended on the
"**any** creature dies" group — a different set of six cards. The count was
confidently reported and confidently wrong for three exchanges.
→ Group by trigger scope; report the groups separately.

**4. A remembered claim about the deck's own contents.** "Blade of the Bloodchief
is the only Equipment" was asserted from memory. Skullclamp is also an Equipment.
The false claim protected a card from being cut for two rounds.
→ Rule 1 covers the 99, not just the candidates.

**5. Self-contradiction across a long session.** Impact Tremors was spared with the
explicit reasoning "the new card doubles it, so they are synergistic" — then cut
two rounds later as "small," when the cut list was re-sorted under a new premise.
The user caught it.
→ Re-read your own spare reasons before re-ranking.

**6. Entangling price with the verdict.** A card was framed as "the budget
substitute" for a more expensive one. When the user said they owned everything,
that framing implied the verdict should move — but price had never been
load-bearing, and for that card it had been an argument *in favour*.
→ Price is its own line. Say whether a rejection survives the card being free.

**7. Forcing a binary on a dual-mode deck.** The deck ran both an aggro plan and an
aristocrats plan, bridged by a +1/+1 counter package that turned deaths into board
growth. Cards were evaluated against one mode at a time and rejected by each in
turn — too slow for the first, redundant with the second.
→ Find the bridge, then score against every mode.

## The pattern underneath all seven

Every one of these was a reasoning error sitting on top of *correctly fetched
facts*. The Scryfall lookups, colour-identity checks, combo queries and Game
Changer checks were all accurate throughout. Verification discipline does not
protect you from framing errors — it only guarantees the inputs. The rubric's job
is the framing, and the tests above are where it goes wrong.

A useful closing filter from that review: the changes that survived scrutiny were
**multiplicative** — a damage doubler, a repeating death engine, a token-count-to-
damage converter. The ones correctly rejected were **additive** cards landing in
categories already ten to sixteen cards deep. When a deck is deep everywhere,
prefer the card that multiplies what it already does over the card that adds one
more of something.
