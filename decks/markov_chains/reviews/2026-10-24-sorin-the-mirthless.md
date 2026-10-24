# markov_chains — Sorin the Mirthless (2026-10-24)

**Verdict: NO.** It's a good card that gives this deck a third repeatable card-draw
engine. Card draw is already the deck's deepest support role. Sorin isn't a Vampire,
so it doesn't trigger Edgar's eminence. And there's no card left that it clearly beats:
the two weakest cards flagged in past reviews were spared for reasons that still hold.

Deck state: `base.txt` and `cards.md` were both regenerated 2026-10-23 and are in sync.
100 cards, 34 lands, average non-land MV 2.86. Curve 1:13 · 2:14 · 3:19 · 4:12 · 5:5 ·
6:3. Pips B 63 / W 19 / R 4. Bracket 3, $40/card cap, Game Changers 2/3 (Necropotence,
Teferi's Protection).

## The card (Scryfall, fetched 2026-10-24 08:33 UTC)

> **Sorin the Mirthless** `{2}{B}{B}` — Legendary Planeswalker — Sorin, loyalty 4
> +1: Look at the top card of your library. You may reveal that card and put it into
> your hand. If you do, you lose life equal to its mana value.
> −2: Create a 2/3 black Vampire creature token with flying and lifelink.
> −7: Sorin deals 13 damage to any target. You gain 13 life.

Colour identity B · Commander legal · not a Game Changer · EDHREC rank 8,119.
Ruling [2021-11-19]: if you don't take the card, it stays on top of your library.

It has a different name from **Sorin, Imperious Bloodlord**, which the deck already
runs, so the legend rule doesn't stop you having both on the battlefield.

## Honest best case

It's two cards in one, and both halves touch the deck's engines. Every claim below
uses verified text:

- **The −2 token is a Vampire, it flies, and it has lifelink.**
  - **Sanctum Seeker:** *"Whenever a Vampire you control attacks, each opponent loses 1
    life and you gain 1 life."* The token counts.
  - **Welcoming Vampire:** *"Whenever one or more other creatures you control with power
    2 or less enter, draw a card."* A 2/3 token qualifies.
  - **Mirkwood Bats:** *"Whenever you create or sacrifice a token, each opponent loses 1
    life."* That's one drain when you make it and one more when you sacrifice it.
  - **Vito** (*"Whenever you gain life, target opponent loses that much life"*) and
    **Marauding Blight-Priest** (*"Whenever you gain life, each opponent loses 1
    life"*): lifelink combat damage triggers both of them. That ties the token to the
    drain plan.
  - The anthems pump it.
- **The walker itself dying does something.** **Cruel Celebrant** triggers on *"another
  creature or planeswalker you control"* dying. **Edgar, Ancient Bloodlord** can
  *"Sacrifice another creature or planeswalker"*. Use −2 twice and Sorin dies, which
  still pays off Celebrant.
- **The +1 is a card every turn.** It's optional, so you can turn down an expensive
  card. Lands cost 0 life, and 34 of the 99 are lands. A wide board of tokens is
  exactly what keeps a planeswalker alive.

As a claim that could be false: *"For 4 mana, Sorin is either two flying lifelink
Vampires over two turns that drain through Seeker, Bats, Vito and Blight-Priest, or a
card every turn for as long as the board protects it."* That's true, and the synergy
test passes easily: well over three verified cards interact with it.

## The tests

**Redundancy — effect × frequency × duration.** The +1 is a repeatable, permanent card
engine. The deck already runs two of those that are at least as strong:

| Card | Effect × frequency × duration |
|---|---|
| **Necropotence** `{B}{B}{B}` | *"Pay 1 life: Exile the top card …"* — any number of cards per turn, for as long as it stays out |
| **Black Market Connections** `{2}{B}` | each first main phase, *"Draw a card. You lose 2 life"*, and you can also choose a Treasure or a 3/2 changeling. Every turn, for as long as it stays out |
| Sorin the Mirthless +1 | one card per turn, costing life equal to its MV. Lasts only while the walker survives attacks |

Behind those two, the deck has eight more nonland draw/selection sources (verified scan
of `cards.json`): Skullclamp, High-Society Hunter, Welcoming Vampire, Bloodline
Recollector, Baron Bertram Graywater, Henrika, Clavileño and Herald's Horn. Village
Rites is a one-shot. Sorin would be the third repeatable engine, in a category the
2026-10-09 review already called saturated: *"with both [adds], draw stops being the
constraint."* Recollector was the first of those two adds, and it's in.

The −2 is also less than it looks next to a Vampire 4-drop. Edgar's eminence fires on
*"another Vampire spell"*. A planeswalker isn't one, so Sorin doesn't make the free 1/1
that every Vampire 4-drop in the deck makes. Sorin's two tokens come one per turn, on
consecutive turns. A Vampire 4-drop puts two bodies on the battlefield the turn it
resolves.

**Density.** Not an issue. The token works with a dozen cards and the +1 needs nothing.

**Marginal impact — does it change games you lose?** A little. After a wipe, Sorin
gives you a flying blocker and a card a turn, which helps with the board-recovery
weakness the 2026-08-31 audit found. But the deck doesn't lose games for lack of cards.
Necropotence and BMC already refill the hand, and lifegain covers the life they cost.
On a losing board with no blockers, a 4-loyalty walker that has just used −2 is at 2
and dies to any attacker.

**Cost of entry.** MV 4 joins a 12-card 4-slot. `{B}{B}` is trivial on 63 black pips.
It also adds to the deck's pay-life cards: Necropotence, BMC, Ancestral Craving,
Anguished Unmaking, Henrika. The deck's lifegain covers that, but it's another one.

**Anti-synergy.** No eminence trigger. No other nonbo found.

**Worst-case draw.** Opening hand, on the draw, against a fast deck: you cast it on
turn 4, make a token, and hope. Turn 12 on an empty board: it's one of the better
topdecks the deck has. Its range of outcomes is fine. It isn't dead at either end.

**Bracket fit.** Not a Game Changer. `combos.py --add` finds **0** new and **0** near
combos (baseline: 2 assembled). The house rules aren't affected.

**Disagreement check.** EDHREC has it in **7.1%** of Edgar Markov decks (3,716 /
52,168). The community and I agree. My independent reason: Edgar decks value every slot
by whether it triggers eminence, and this deck's draw role was already full before
Sorin was proposed.

## The cut — and why there isn't one

Spells for a spell, lands untouched. These are the candidates, with the reasons each
was spared before. I re-read those reasons for this review:

1. **Forerunner of the Legion** — spared 2026-09-06/07 and again 2026-10-09 as **the
   deck's only tutor**. That's still true, and Sorin doesn't tutor.
2. **Bloodthrone Vampire** — spared 2026-10-09 as one of the three free, unlimited sac
   outlets that prepare Bloodline Recollector. Recollector is in the deck, so the
   reason holds.
3. **Malakir Bloodwitch, Vampire Nocturnus** — the earlier "obvious" cuts. Both have
   already left the list.
4. **Herald's Horn** (the same-role swap) — it's both a cost reducer and Vampire-only
   card selection. It's the closest match in role, but cutting it trades ramp for draw
   in a deck that has plenty of draw.
5. **Mirkwood Bats** (the same-MV swap) — it's a Sorin synergy piece itself, and every
   eminence token drains through it. I'd defend it.

Past the first two, every cut is a card I'd defend somewhere else. Per the rubric, that
is the finding: there's nothing in the 99 that Sorin is clearly better than.

## On the speed premise

This NO doesn't depend on the deck's clock. If anything, the long games recorded on
2026-08-30 make Sorin better, because a card engine has more turns to pay off. The
rejection rests on redundancy and the missing cut, and neither changes with game length.

## What would change it

- **Draw turns out to be the constraint.** If you're out of cards by turns 7–8 even
  with Necropotence, BMC and Recollector, the draw role is thinner in practice than on
  paper. Sorin would then be a reasonable swap for **Herald's Horn**.
- **You overrule a spare.** If you decide Forerunner's tutor isn't worth the slot,
  Sorin is a better card than Forerunner and a fair candidate for the opening.
  Spellbook shows no new combos, so the house rules don't block it.

## Price

$2.39 (foil $2.56), fetched 2026-10-24 08:33 UTC. Under the $40 cap. The NO survives
the card being free.

Other prices this session (fetched 2026-10-24 08:34 UTC): Black Market Connections
$11.85 · Necropotence $38.47 · Herald's Horn $5.59 · Mirkwood Bats $1.88.

## Sources

- `card_facts.py lookup "Sorin the Mirthless" --deck markov_chains --rulings`,
  2026-10-24 08:33 UTC.
- `card_facts.py lookup` for Black Market Connections, Necropotence, Herald's Horn,
  Welcoming Vampire, Vito, Marauding Blight-Priest, Cruel Celebrant, Sanctum Seeker,
  Mirkwood Bats and Edgar Markov, 2026-10-24 08:34 UTC.
- `edhrec.py card "Sorin the Mirthless" --deck markov_chains`: Edgar Markov 7.1%
  (3,716/52,168).
- `combos.py markov_chains --add "Sorin the Mirthless" --near`: baseline 2 assembled;
  0 new, 0 near.
- Deck counts from `decks/markov_chains/cards.json` (generated 2026-10-23).

`base.txt` was not modified by this review.
