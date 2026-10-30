# Authority of the Consuls (2026-10-30): ADD, cut Wojek Investigator

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap, ~$300 total. Evaluated against `base.txt` as of commit 4df3f86 (Land Tax and Battle Angels of Tyr in; Mind Stone and Tome of Legends out). 37 lands, 26 Angels.
Prices: Scryfall, fetched 2026-10-30 04:42–04:44 UTC. EDHREC: Authority card page (Giada 14,768 / 38,846 decks = 38.0%). Spellbook: `combos.py --add` → 0 new combos, 0 near.

## Facts (verified this session)

**Authority of the Consuls** {W}, Enchantment. "Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life." Legal, colour identity W, not a Game Changer. No official rulings.

Scope: both clauses are **opponents' creatures only**, include tokens, and fire on **any player's turn**. Not targeted, no choices.

## Steel-man

It is the deck's only source of lifegain *events* that fires on opponents' turns without combat. Every one of the deck's per-event payoffs works on every turn, so Authority roughly extends them from one turn in four to all four.

**Per-event payoffs ("Whenever you gain life"):**
- **Archangel of Thune**: "put a +1/+1 counter on each creature you control". One per opposing creature, token or not.
- **Lyra, Archangel of Dawn**: "put a +1/+1 counter on each Angel you control".
- **Exemplar of Light**: a counter, then "draw a card … only once each turn". With Authority, that's up to one extra card on each opponent's turn.
- **Dawn of Hope**: "you may pay {2}. If you do, draw a card", a mana sink at instant speed on opponents' turns.

**End-step payoff:**
- **Ob Nixilis, the Ascended**: "At the beginning of **each** end step, if you gained life this turn, create a 4/4 … Angel". Each opponent who casts a creature now gives you an Angel at their end step.

**The tapped clause:** creatures an opponent casts on their turn stay tapped until that opponent's next untap step.
- They can't block on your turn, which matters for the air plan against reach and fliers, and for Elesh Norn and myriad tokens.
- Haste creatures can't attack the turn they arrive. The pod's recorded tendency is ground wins, and the recorded loss mode is ground alpha strikes.
- **Ob Nixilis**' enter trigger, "destroy all tapped creatures your opponents control", now catches every creature cast since its controller's last untap, not only the ones that attacked.
- **The Wandering Emperor**'s −2, "Exile target tapped creature", gets the same extended target pool.

Synergy test (three named cards): Archangel of Thune, Lyra AoD, Exemplar of Light, Dawn of Hope, Ob Nixilis, The Wandering Emperor. That's six. Passes.

## The tests

**Redundancy: effect × frequency × duration.** Every other lifegain source in the list keys off **your** creatures entering (Bishop of Wings, Righteous Valkyrie, Dazzling Angel, Seraph Sanctuary) or **your** creatures dealing damage (the lifelinkers, Battle Angels, Angel of Destiny). On opponents' turns, the only gains today come from a lifelinker blocking. Nothing else gives non-combat events on other players' turns. This is a **multiplier** on the existing engine, not a 12th feeder.

**Density (opponent-dependence).** Archivist of Oghma and Linvala were rejected because their value depended on what the rotating pod plays. Authority depends on opponents casting creatures, which nearly every Commander deck does, and `meta.json` records that the pod mostly wins through ground attacks. The premise it needs is the one already on file. Against a creature-light control deck it's weak, but that's one opponent in three, not the whole table.

**Marginal impact.**
- Without a payoff on board, it's 1 life per creature, plus haste denial and a round of blocker denial. That's real, but small.
- With Thune or Lyra AoD out, a token-making opponent is now growing your board.

**Worst case.** As a turn-1 play it's a fine opening at the cheapest slot in the deck. As a late topdeck it's 1 mana for a card that does nothing alone. Being cheap is the only thing protecting its floor.

**Anti-synergy.** None found. It's asymmetric, so your creatures and Myriad tokens aren't affected. It doesn't interact with Magus of the Moat or Ghostly Prison.

**Bracket.** Not a Game Changer. 0 combos, 0 near.

**Disagreement check.** 38.0% of Giada decks run it. The community agrees, and the deck-specific reason (six payoffs that become opponent-turn engines) is independent of popularity.

**Speed premise.** The verdict doesn't rest on it.

## The cut: Wojek Investigator

The 2026-10-30 Battle Angels review named it the first runner-up, "take this cut instead if Tome has been drawing well." Tome is now gone, so it's the next card in line. Its role, card draw, is still the deck's deepest support category without it:
- Folk Hero, Dawn of Hope, Vanquisher's Banner, Exemplar of Light, Inspiring Overseer, Court of Grace (monarch) and Battle Angels of Tyr
- Minas Tirith, War Room and Bonders' Enclave
- Authority itself adds draws through Exemplar and Dawn on opponents' turns

What you lose:
- A 3-mana 2/4 flying, vigilant Angel. Angels go 26 → 25, which feeds Giada counters, Bishop, Righteous Valkyrie, Folk Hero and Vanquisher's Banner one fewer time.
- A blocker that can hold the ground.

The curve trades a 3-drop for a 1-drop, so average nonland MV drops by about 0.03.

Runners-up, spared:
1. **Seraph of the Sword.** It's the same role (defence), but it does what Authority can't: it blocks a non-haste ground attacker every turn. The user picked it on 2026-10-28, so it's not reopened.
2. **Radiant Fountain.** A land. 36 lands plus Land Tax is defensible, but the rubric says cut a spell for a spell. Take this instead if Wojek's Clues have been a real card engine in your games.
3. **Patchwork Banner.** Spared in the Land Tax review. Rocks are down to Sol Ring, Arcane Signet, Pearl Medallion and Banner, plus three reducers.
4. **Thraben Watcher.** It gives Battle Angels vigilance.
5. **Dazzling Angel.** It's the only gain source on non-Angels entering.
6. **Valorous Stance, Fateful Absence.** Still reserved as the cuts for Teferi's Protection and Darksteel Mutation.

## Unsure about

How often Wojek actually makes Clues. This deck empties its hand, so it may fire for 2–3 opponents per upkeep. If that's been happening, use runner-up 2.

## Price (separate factor)

**$5.54** (foil $6.32), fetched 2026-10-30 04:42 UTC. Under the cap. The running total was already likely over ~$300 after Battle Angels. **The verdict would be the same if the card were free.**
