# Angels — Elspeth Resplendent (2026-10-07)

Deck state reviewed: `complete.txt` (100 cards). `base.txt` untouched.
Prices: Scryfall, fetched 2026-10-07 03:45 UTC. EDHREC: Giada commander page, 36,555 decks. Follows the same-day Ajani Goldmane review, which already modelled the deck's lifegain and counter engines; counts below reuse that verified text.
Constraints (meta.json): bracket 3, ≤3 Game Changers (deck has 2), no early or tutor-dependent infinites, $40/card, ~$300 total.

## The card, verified

**Elspeth Resplendent** — {3}{W}{W}, loyalty 5. "+1: Choose up to one target creature. Put a +1/+1 counter and a counter from among flying, first strike, lifelink, or vigilance on it. −3: Look at the top seven cards of your library. You may put a permanent card with mana value 3 or less from among them onto the battlefield with a shield counter on it. Put the rest on the bottom of your library in a random order. −7: Create five 3/3 white Angel creature tokens with flying."
Mono-W, Commander-legal, not a Game Changer. **$4.74** (SNC). Giada EDHREC **12.0%** (4,372 / 36,555), the second most-played planeswalker on the page after Serra the Benevolent (30.3%). `combos.py --add`: 0 combos, 0 within reach.

Earlier verdict on record (remaining-budget review, 2026-10-02): NO against The Wandering Emperor, "at 5 mana it does less on arrival than the Emperor at 4 with flash." That was a one-line comparison for an interaction slot. This is the full evaluation.

## Verdict: NO

### Honest best case
Elspeth is a wipe-proof Angel generator: her −3 digs seven cards for one of the deck's 28 cheap engine permanents and lands it with a shield, and her −7 is the largest single "Angels enter" event the deck can produce, five fliers at once into Giada, Bishop of Wings, Righteous Valkyrie, Cathars' Crusade and the Thune/Lyra chain. In a pod that wins on the ground, Magus of the Moat ("Creatures without flying can't attack") and Archangel of Tithes ("creatures can't attack you or planeswalkers you control unless their controller pays {1}") keep her alive long enough to get there.

### What killed it

**1. Cost of entry: the most expensive 5 in the deck.** Nonland curve from verified mana values:

| MV | Cards |
|---|---|
| 4 | Court of Grace, Serra the Benevolent, The Wandering Emperor, Exemplar of Light, Gisela, Angelic Field Marshal, Archangel of Tithes, Thraben Watcher, Magus of the Moat, Clever Concealment, Akroma's Will (11) |
| 5 | Cathars' Crusade, Archangel of Thune, Lyra Dawnbringer, Angel of Invention, Angel of Destiny, Norn's Choirmaster, Vanquisher's Banner (7) |
| 6+ | Valkyrie Harbinger, Austere Command, Farewell, Ob Nixilis, Elesh Norn, Angel of the Ruins, Sephara, Avacyn, Emeria's Call (9) |

Five of the seven 5-drops are Angels, and every Angel spell is cut by Starnheim Aspirant (−2), Urza's Incubator (−2), Herald's Horn (−1), Pearl Medallion (−1) and paid for with Giada's Angel-only mana. Thune or Lyra Dawnbringer costs 2–3 with two reducers out. Elspeth is a non-Angel, non-creature: only Pearl Medallion touches her. She would be the eighth 5-drop and, in practice, the one that actually costs five.

**2. On arrival she does less than any 5-drop she competes with.** The −3 puts a permanent onto the battlefield: it is not cast, so no Folk Hero draw, no Vanquisher's Banner draw, no cost reducer matters. A creature found this way does still *enter* (Giada's counters, Bishop's 4 life, Valkyrie, Crusade, Evangel's proliferate), and the hit rate is high: 28 nonland permanents at MV ≤3 plus 37 lands qualify, so seven cards almost always show one. But the ceiling of the mode is "a Bishop of Wings with a shield counter," and it leaves Elspeth at 2 loyalty. Serra the Benevolent at 4 mana does the same job better on the same turn: a 4/4 flying vigilance **Angel** that enters alone and takes a Giada counter for every Angel already out.

**3. The −7 is the whole case, and it is two to three turns away.** From 5 she needs two +1 activations, so the earliest natural −7 is her third turn. Metastatic Evangel ("whenever another nontoken creature you control enters, proliferate") and Norn's Choirmaster ("whenever a commander you control enters or attacks, proliferate") can each shave a turn, and those are 2 of 99 cards. The +1 that fills those turns is small here: one creature, one counter, one keyword, at sorcery speed, in a deck where Thune and Lyra AoD put counters on everything several times a turn, and it cannot target a Giada wearing Lightning Greaves (shroud). Flying on Elesh Norn so she can attack under Magus is the one non-trivial use.

When the −7 does fire, what does it do that the deck's state needed? Two cases:
- *Engines out* (Bishop, Valkyrie, Crusade, Thune): five Angels entering is 20 life from Bishop, 15-plus from Valkyrie, five Crusade triggers, ten-plus Thune/Lyra events. This is overwhelming. It is also a board that was already lethal in the air; the shape review has the deck presenting lethal around turn 7–8 with exactly those engines. Win-more.
- *After a wipe*: fifteen power of fliers from a permanent the wipe missed. This is the real argument, and it requires Elspeth to have been on the battlefield before the wipe and to survive two attack steps with no board in front of her. Ghostly Prison does not protect planeswalkers (text: "can't attack **you**"); Tithes does; Magus stops ground attackers only. Court of Grace (an Angel every upkeep while monarch), Emeria, the Sky Ruin and Emeria's Call already fill the rebuild role without the two-turn wait.

Giada and simultaneous tokens: the 2024-11-08 ruling says "each Angel you already control" means the Angels other than the one entering. Five tokens entering together do not count one another under the general rule for simultaneous entry, so each gets counters only for the Angels on the battlefield beforehand. After a wipe that is Giada alone: five 4/4s, not more.

**4. Redundancy by rate.** Angel-token sources already in the deck, as effect × frequency × duration: Court of Grace (one 4/4 per upkeep, indefinitely, while monarch), Serra (one 4/4 now, another every ~3 turns), Resplendent Angel and Valkyrie Harbinger (one 4/4 per end step on a lifegain threshold), Ob Nixilis (one 4/4 per end step on any lifegain), Emeria's Call (two 4/4s once, at 7 mana, or a land). Elspeth is five 3/3s once, three turns after a 5-mana investment. The burst mode is covered by Emeria's Call at a cost the deck's mana already supports; the stream mode is covered three ways.

**5. Disagreement check.** 12.0% of Giada lists run her, so the community is mildly in favour. The difference here is specific: this list runs four Angel cost reducers plus Giada's mana, which makes a non-Angel five-drop relatively more expensive than in a typical Giada deck, and it already carries Emeria's Call and Court of Grace in the roles Elspeth would fill. I would expect her inclusion to be higher in lists without the reducer suite, and it is a fair card there.

**6. Anti-synergy.** None structural. Magus of the Moat does not affect her tokens (fliers). Austere Command and Farewell do not hit her. Elesh Norn makes the tokens 5/5s.

**Price** $4.74 is not load-bearing; the rejection survives the card being free.

### Against each planeswalker specifically
- **For Serra the Benevolent:** NO. Same role, Serra is a turn faster, a mana cheaper, and her Angel is a real Giada target. Serra's weakness is sitting at 1 loyalty; Elspeth's is doing little for two turns. In a ground pod with Magus and Tithes, both survive about equally.
- **For The Wandering Emperor:** NO, and this is the closer call. The Emperor is the deck's 8th instant-speed single-target answer and was named the more cuttable walker in the Ajani review. But she trades for Elspeth across roles (suppression → generator) and the Ajani review already named a stronger occupant for that slot if the lifegain premise holds (Ajani, Strength of the Pride). Elspeth would be the third-best card for the Emperor's slot, behind keeping the Emperor.

### What would flip this
Two premises are doing the work, and both are about the table, not the card:
1. **Wipes.** If goldfish/table item 5 from the shape review ("after a wipe, how fast does the board come back?") is where the deck is actually losing, a planeswalker finisher that survives Farewell-class effects is worth a slot, and Elspeth for The Wandering Emperor is the swap.
2. **Game length.** If games in this pod routinely run past turn 10, the two-turn wait on the −7 stops mattering and her ceiling is the highest of any white planeswalker under $40.
Report either of those and this verdict moves. Until then: NO.

## Numbers used
| | |
|---|---|
| Elspeth Resplendent | $4.74 (SNC, fetched 2026-10-07 03:45 UTC), Giada 12.0% (4,372/36,555), EDHREC rank 5,338 |
| Serra the Benevolent | $7.69, Giada 30.3% (11,073/36,555) |
| The Wandering Emperor | $3.93, below the top-4 planeswalker cut-off (5.2%) on Giada's page |
| Combos | 0 before and after, Commander Spellbook via `combos.py` |
