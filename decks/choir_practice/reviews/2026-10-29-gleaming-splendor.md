# Gleaming Splendor (2026-10-29) — NO

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap, ~$300 total. Evaluated against `base.txt` (100 cards; `cards.md` regenerated 2026-10-28, same commit).
Prices: Scryfall, fetched 2026-10-29 23:08–23:09 UTC. EDHREC: Gleaming Splendor card page. Spellbook: `combos.py --add`.

## Facts (verified this session)

**Gleaming Splendor** {1}{W}, Enchantment. "Whenever an opponent draws their second card each turn, you create a Treasure token. {2}{W}: Two target players each draw a card." Legal, colour identity W, **not** a Game Changer.
Rulings (2026-06-29): the trigger works even if Splendor arrived after the first card was drawn; it "can trigger only once each turn for each opponent"; the activation needs **two different** target players.

## Steel-man

A 2-mana repeatable draw engine in mono-white, a colour short on draw. Activate it at an opponent's end step targeting yourself and that opponent. They already drew for the turn, so their card is the second one and you get a Treasure. That makes it **2 net mana per card**, once per opponent turn, at instant speed. It also ramps for free against draw-heavy opponents.

## The tests

**Scope (whose draw, who chooses).** The trigger only fires on **opponents'** draws. The activation **must** target two different players. If you want a card, an opponent gets one too, every time. The Treasure refund comes **once per opponent per turn**. Each later activation that turn costs the full {2}{W} and still gives a card away.

**Redundancy: rate × frequency × duration.** The deck's repeatable mana-sink draw:

| Card | Rate | Frequency | Gives opponent a card? |
|---|---|---|---|
| Dawn of Hope | {2} per card | every lifegain event, uncapped | no |
| Wojek Investigator | {2} per Clue | upkeep, per opponent with a bigger hand | no |
| War Room / Bonders' Enclave | {3} per card | once a turn each, land slot | no |
| Minas Tirith | {1}{W} per card | once a turn, after attacking with 2+ | no |
| **Gleaming Splendor** | {2} net (first use per opponent turn), {2}{W} after | once a turn per target | **yes** |

At best Splendor matches Dawn of Hope's rate, and its card is shared with the table. Dawn of Hope runs on this deck's main engine (lifegain from Bishop of Wings, Righteous Valkyrie, Dazzling Angel, the lifelinkers and Seraph Sanctuary). Splendor runs on nothing the deck does. It is an additive copy of an effect the deck already has, at a worse rate. The other draw sources (Folk Hero, Tome of Legends, Vanquisher's Banner, Exemplar of Light, Inspiring Overseer, Court of Grace's monarch, Mind Stone) are separate from this.

**Synergy: three named cards?** No. Treasure feeds nothing specific. Wojek Investigator looks like a fit ("opponents with more cards in hand than you") but isn't: each activation gives you a card and the opponent a card, so the gap between your hand and theirs doesn't change. It isn't an Angel, so Giada's mana, Starnheim Aspirant, Urza's Incubator and Herald's Horn don't help cast it. Pearl Medallion does. The Folk Hero, Bishop and Vanquisher's triggers don't fire either.

**Density (the passive Treasure).** It depends entirely on what opponents' decks do. The meta here is a rotating pod with 10+ unknown decks. It is the same flaw that got Archivist of Oghma cut on 2026-10-05: "entirely opponent-dependent… the user reports it rarely fires." When it does fire, it ramps a category the 2026-10-02 shape review already called **over-supplied** (9 rocks or reducers plus Giada).

**Marginal impact.** The deck's recorded loss modes are Giada being removed and ground alpha strikes. Splendor does nothing about either. Giving cards to the decks that beat you on the ground actively hurts.

**Anti-synergy.** It's symmetric card advantage in a deck whose plan is to out-board the table, not out-politic it.

**Worst case.** Turn 2 on the draw: a 2-mana enchantment that doesn't affect the board. Turn 12 topdeck with an empty board: {2}{W} to draw a card and give a card away. It's weak at both ends.

**Bracket.** Not a Game Changer. `combos.py --add`: completes 0 combos, 0 near-combos.

**Disagreement check.** 8.0% of Giada decks (858 / 10,736) run it. Its top homes are group-hug and draw-matters commanders: Thorin, King of Durin's Folk 52.6%, Bard, King of Dale 60.3%, Kynaios and Tiro 21.1%. Those decks want opponents drawing. This one doesn't. Low inclusion agrees with the verdict.

**Speed premise.** The verdict doesn't depend on it. The rejection rests on rate, scope and redundancy, not on "too slow".

## Price (separate factor)

**$33.79** (foil $36.34), fetched 2026-10-29 23:08 UTC. That's under the $40 per-card cap. The last recorded running total was ~$277.50 of ~$300 (shape review, 2026-10-02). Later swaps (Lightning Greaves, Herald of Eternal Dawn, Kindred Judgment, the 10-28 reviews) were never added to that tally, so the card may not fit the total budget at all. **The NO holds even if the card is free.**

## Counter-proposal

None needed. No card-draw gap has been reported from the table, and the deck already has a lifegain-to-cards engine. The cards that do Splendor's job properly in white are both over the cap: Smothering Tithe ($58.63, and a Game Changer) and Esper Sentinel ($54.82), fetched 2026-10-29 23:09 UTC. If goldfishing shows the deck running out of cards by turn 6–7, reopen the draw question as its own review.

## Verdict

**NO.** It's symmetric draw at no better rate than Dawn of Hope, and its Treasure depends on opponents in a pod you can't predict.
