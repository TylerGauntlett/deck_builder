# Banishing Light for commander control: review (2026-10-03)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards).

## The question

Banishing Light is proposed as a way to deal with problem commanders, which the user says are common in the pod. The user compares it to Imprisoned in the Moon and Oubliette in their other decks. The user already owns a copy.

## Verdicts

| Card | Verdict |
|---|---|
| Banishing Light | **NO.** It does not do what Imprisoned in the Moon and Oubliette do, and Grasp of Fate already does its job better. |
| Darksteel Mutation (counter-proposal) | **ADD, cut Fateful Absence.** This is the white version of the effect the user actually wants. |

## Why Banishing Light isn't like Imprisoned in the Moon or Oubliette

All three verified this session:

- **Imprisoned in the Moon** (U): "Enchanted permanent is a colorless land ... and loses all other card types and abilities." The commander **stays on the battlefield**.
- **Oubliette** (B): "target creature **phases out** until this enchantment leaves the battlefield." A phased-out permanent never leaves the battlefield.
- **Banishing Light** (W): "**exile** target nonland permanent an opponent controls until this enchantment leaves the battlefield."

The commander rules (CR 903.9a) let a commander's owner move it to the command zone whenever it would be exiled. So Banishing Light does the same thing to a commander as Swords to Plowshares: the opponent recasts it next turn and pays 2 more. The two cards the user cited are good against commanders because the commander never changes zones, so the owner never gets that choice. Banishing Light doesn't share that property.

Both reference cards are also off-colour for this deck (U and B, flagged illegal by `--deck`).

## Banishing Light on its own merits

**Best case:** a 3-mana answer to any nonland permanent that the user already owns.

**Redundancy.** It loses to Grasp of Fate, which is already in the deck. Grasp of Fate ({1}{W}{W}) exiles "for each opponent ... up to one target nonland permanent that player controls" until it leaves. It costs the same, has the same weakness to enchantment removal, and handles up to three permanents instead of one. Banishing Light is the weaker copy of a card the deck already runs.

The deck has 9 targeted answers, all verified this session:

- Swords to Plowshares, Path to Exile: exile, creature
- Get Lost: destroy, creature, enchantment or planeswalker
- Fateful Absence: destroy, creature or planeswalker
- Valorous Stance: destroy, toughness 4 or greater
- Generous Gift: destroy, any permanent
- Grasp of Fate: exile until it leaves, one per opponent
- The Wandering Emperor −2: exile a tapped creature
- Angel of the Ruins: exile up to two artifacts or enchantments

None of the nine keeps a commander away. Each one lets the owner send it to the command zone. Banishing Light would be the tenth answer of that kind.

The deck has one card that makes this removal stick: **Drannith Magistrate**, "Your opponents can't cast spells from anywhere other than their hands." While it's in play, any of the nine keeps a commander out of the game. Banishing Light gains nothing from Magistrate that Grasp of Fate doesn't also gain.

**Price:** $0.51 (fetched 2026-10-04 00:07 UTC). The user owns a copy. Price played no part in this verdict, and the NO stands even though the card is free.

**EDHREC:** 4.9% of Giada decks (1,761 of 36,133). Low inclusion agrees with the NO.

## Counter-proposal: Darksteel Mutation

The gap the user identified is real. The deck has **0** answers that leave a commander on the battlefield with no abilities. Every commander answer it has costs the opponent only a turn and 2 mana. In a pod where commanders are often the problem, that matters in every game, so it holds up across unknown decks and doesn't count as tuning against one opponent.

Search: `id<=w t:aura o:"loses all" f:commander` returned 5 results.

| Card | Text (verified) | Commander lock? |
|---|---|---|
| **Darksteel Mutation** {1}{W} | Enchanted creature is an Insect artifact creature, base 0/1, **has indestructible**, and loses all other abilities, card types and creature types | **Yes.** Indestructible keeps it locked through destroy-based wipes, including our Austere Command. |
| Reprobation {1}{W} | loses all abilities, base 0/1 Coward | Partly. Any wipe kills the creature and sends the commander to the command zone, which frees it. |
| Minimus Containment {2}{W} | becomes a Treasure that loses all other abilities | **No.** The opponent can sacrifice the Treasure whenever they want and get the commander back. |
| Heliod's Punishment {1}{W} | can't attack or block, loses abilities, removes itself after 4 taps | No. It's temporary. |
| Swift Reconfiguration {W} | becomes a Vehicle with crew 5 | No. It doesn't remove abilities. |

**Official rulings for Darksteel Mutation (2013-10-17):**

- "if it's enchanting a commander, that creature will continue to be a commander."
- It does not override +1/+1 counters or anthem-style P/T changes.
- Abilities gained after it attaches work normally.

**Weaknesses:**

- It's sorcery speed.
- It only hits creatures. Imprisoned in the Moon could also hit planeswalkers.
- Enchantment removal or bounce frees the commander.
- If the opponent has a sacrifice outlet, they can sacrifice the creature and send the commander to the command zone.
- A commander with counters on it keeps its size.

**Price:** $0.97 (fetched 2026-10-04 00:08 UTC), well under the cap. EDHREC rank 585 overall.

### The cut: Fateful Absence

Swap within the role so removal stays at 9.

1. **Fateful Absence (cut).** It covers mostly the same targets as Mutation (creatures; planeswalkers are the only extra). Against a commander, it gives the opponent a Clue and a recast. Its advantages are instant speed and hitting planeswalkers.
2. **Valorous Stance (spared).** It also protects one of our creatures. The 2026-10-02 remaining-budget review already reserved it as the cut for Teferi's Protection, so don't spend it twice.
3. **Get Lost (spared).** It's one of 4 targeted enchantment answers. The Bruna review counted that category as thin.
4. **Swords / Path (spared).** At 1 mana they are the cheapest answers in the deck.

Caveat: Fateful Absence isn't a bad card. If the creatures causing trouble are mostly non-commander creatures, keep it and cut nothing. The swap is only worth making if the user's report holds up, meaning commanders really are the recurring problem.
