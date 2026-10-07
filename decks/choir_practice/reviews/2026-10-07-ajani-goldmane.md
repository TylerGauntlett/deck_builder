# Angels — "swap planeswalker for Ajani Goldmane" (2026-10-07)

Deck state reviewed: `complete.txt` (100 cards; the list after the Lightning Greaves swap). `base.txt` untouched.
Prices: Scryfall cheapest printing, fetched 2026-10-07 03:34–03:37 UTC. EDHREC: Giada commander page, 36,555 decks; Giada lifegain theme page, 3,006 decks.
Constraints (meta.json): bracket 3, ≤3 Game Changers (deck has 2: Farewell, Drannith Magistrate), no early or tutor-dependent infinites, $40/card, ~$300 total.

## What "the planeswalker" is

The deck runs **two** planeswalkers, not one. Ob Nixilis, the Ascended is a 7-mana Angel *creature* (verified), not a planeswalker.

| In deck | Cost | Loyalty | Verified text (abridged) | Giada EDHREC |
|---|---|---|---|---|
| **The Wandering Emperor** | {2}{W}{W} | 3 | Flash; loyalty abilities at instant speed the turn she enters. +1: counter + first strike on up to one creature. −1: 2/2 vigilance Samurai. −2: exile target **tapped** creature, gain 2 life. | not in the top 4 planeswalkers (below 5.2%) |
| **Serra the Benevolent** | {2}{W}{W} | 4 | +2: fliers you control +1/+1 until EOT. −3: 4/4 white **Angel** token, flying, vigilance. −6: emblem, damage can't take you below 1 while you control a creature. | **30.3%** (11,073 / 36,555) |

Candidate, verified:

**Ajani Goldmane** — {2}{W}{W}, loyalty 4. +1: gain 2 life. −1: +1/+1 counter on **each creature you control**, they gain vigilance until EOT. −6: white Avatar token with P/T equal to your life total. Mono-W, Commander-legal, not a Game Changer. **$4.83** (M11; fetched 2026-10-07 03:34 UTC). Giada EDHREC: **0.3%** (126 / 36,555). `combos.py --add`: completes 0 combos, 0 within reach.

## Verdict: NO — for either planeswalker

### Honest best case
Ajani is a board-independent lifegain trigger every turn (+1) and a Cathars' Crusade trigger that needs no creature to enter (−1); in a deck that sits at 50–70 life, his −6 is a body the size of your life total.

### What killed it

**1. The +1 is the deck's ~17th lifegain source, and it only matters when the deck is already gaining life.**
Grouped by how they fire (all verified this session):
- *An Angel/creature enters* (your turn almost always, plus Court of Grace upkeep tokens and Ob Nixilis end-step tokens): Bishop of Wings ("Whenever an Angel you control enters, you gain 4 life"), Righteous Valkyrie ("another Angel or Cleric … gain life equal to that creature's toughness"), Seraph Sanctuary (1), Dazzling Angel ("another creature … gain 1 life").
- *Lifelink combat*: Archangel of Thune, Lyra Dawnbringer (and she grants lifelink to every other Angel), Gisela, Angel of Invention, Valkyrie Harbinger, Sephara, Dawn of Hope's Soldier tokens, Resplendent Angel's activation, Akroma's Will mode 2.
- *One-shots*: Inspiring Overseer (1), Radiant Fountain (2), The Wandering Emperor −2 (2), Ob Nixilis ETB, Angel of Destiny's combat trigger.
- *Modifier*: Angel of Vitality (+1 per event).

The payoffs Ajani's 2 life would feed (Thune: counter on each creature; Lyra, Archangel of Dawn: counter on each Angel; Exemplar of Light: counter + draw; Dawn of Hope: pay 2, draw; Ob Nixilis: 4/4 Angel at end step) are all **creatures or need a board**. When they are out, the deck is casting Angels and swinging with lifelinkers and already gains life on its own turn (the mass-token review established Ob Nixilis fires on nearly every own turn). When the board is empty after a wipe, Ajani's +1 gains 2 life into nothing. The card does its job exactly when the job is already done.

The 2 life (3 with Vitality) also **misses every threshold** in the deck on its own: Resplendent Angel wants 5 in a turn, Valkyrie Harbinger 4, Righteous Valkyrie's anthem +7 over starting, Angel of Destiny +15. Serra's −3 Angel, by contrast, is one event worth 4 (Bishop) + 4-plus (Valkyrie, toughness including Giada's counters) + 1 + 1, which clears both token thresholds in one go.

**2. The −1 is the sixth board-wide counter engine, and the weakest-rate one.** Cathars' Crusade (each creature, every creature entry), Archangel of Thune (each creature, every lifegain event), Lyra AoD (each Angel, every lifegain event), Metastatic Evangel (proliferate on nontoken entry), Norn's Choirmaster (proliferate on Giada entering/attacking). Those fire several times a turn once the deck is running. Ajani's −1 is once a turn, sorcery speed, and loyalty-capped at **four uses ever** without proliferate. The vigilance rider is already covered by Angelic Field Marshal ("creatures you control have vigilance" with Giada out), Thraben Watcher ("other nontoken creatures … have vigilance"), and the vigilance already printed on Giada, Angel of Invention, Wojek Investigator, Avacyn, Elesh Norn and the Serra/Court Angel tokens.

**3. The −6 fights the deck.** From 4 loyalty it needs two +1 turns, so the Avatar arrives no earlier than Ajani's third turn (turn 7+ on curve), when the shape review expects the deck to be presenting lethal in the air anyway. The Avatar has **no flying**, so Magus of the Moat ("Creatures without flying can't attack") stops it attacking; it is not an Angel, so it gets no Giada counters, no Lyra Dawnbringer lifelink, no Sephara indestructible, no Incubator/Horn/Aspirant discount, no Bishop or Valkyrie trigger; and a 60/60 with no evasion against a table that has seen it coming for two turns is a Swords target. The deck's existing finishers (Akroma's Will, Elesh Norn, Sephara, Avacyn, Angel of Destiny) all work with the air force it actually builds.

**4. Role versus shape.** The shape review (2026-10-02) set targets: generators hold, amplifiers **↓1** (13 was over-full), suppression hold at 15. Ajani is an amplifier. Cutting Serra (a generator, and an Angel source) for him moves a card from the base of the inverted T to the layer that was asked to shrink. Cutting the Emperor (suppression) for him trades an answer for an amplifier in the layer with the least room.

**5. Disagreement check.** 0.3% of Giada decks run Ajani Goldmane; Serra runs in 30.3%. I agree with the community and have an independent reason (points 1–3). What would I see that 36,000 lists don't? Nothing.

**Price** is not load-bearing: $4.83 is cheap, and the rejection survives the card being free.

### If you still want one of the two walkers out
The more cuttable of the two is **The Wandering Emperor**, not Serra. Her −2 is the 8th instant-speed single-target answer (Swords, Path, Fateful Absence, Get Lost, Generous Gift, Valorous Stance, Eiganjo channel), it only hits *tapped* creatures, and Magus of the Moat and Ghostly Prison reduce how often creatures attack you at all. Serra's −3 is an Angel entering, which is the deck's primary action. But Goldmane loses to the Emperor too, for the reasons above; a planeswalker-for-planeswalker swap only makes sense with a better planeswalker.

## Counter-proposal: Ajani, Strength of the Pride — ADD IF, cut The Wandering Emperor

Verified: {2}{W}{W}, loyalty 5. "+1: You gain life equal to the number of creatures you control plus the number of planeswalkers you control. −2: Create a 2/2 white Cat Soldier creature token named Ajani's Pridemate with 'Whenever you gain life, put a +1/+1 counter on this token.' 0: If you have at least 15 life more than your starting life total, exile Ajani and each artifact and creature your opponents control." Mono-W, legal, **not** a Game Changer. **$8.68** (fetched 2026-10-07 03:37 UTC). Giada EDHREC 3.6% (1,298 / 36,555). Ruling 2019-07-12: the 15-life check is made as the 0 ability resolves. `combos.py --add`: 0 combos.

Why this Ajani is a different card from Goldmane in this deck:
- **The +1 scales with the board.** With Giada plus five Angels and Ajani out, that is 7 life (8 with Vitality) in one event every turn, which clears Resplendent Angel's 5 and Valkyrie Harbinger's 4 on its own, so each of those is a 4/4 Angel at end step, each of which triggers Giada's counters, Bishop (4), Valkyrie, Crusade, Dazzling and Youthful Valkyrie again. It also guarantees Ob Nixilis's end-step Angel and a Thune/Lyra AoD/Exemplar round. Goldmane's flat 2 reaches none of this.
- **The 0 is the missing conversion the shape review named.** It said the lifegain half of the engine had no finisher that used *life*; Angel of Destiny was added for that. Strength of the Pride is a second one, and it is **overwhelming interaction** (one-sided exile of every opposing creature and artifact), which the remaining-budget review identified as the gap against the go-wide ground decks this pod wins with. The 15-over-starting threshold is the same one Destiny already asks the deck to hit.
- **Worst case is fine.** On an empty board the +1 still gains 1 (Ajani counts himself) and the −2 makes a body that grows with every lifegain event; the Emperor on an empty board makes a 2/2 or exiles one attacker.
- **Anti-synergy check:** none found. Avacyn's indestructible is irrelevant to exile. The 0 exiles only *opponents'* creatures and artifacts (clause verified), so Pridemate, Servos, Clues and your rocks stay. It does exile Ajani himself, so it is a once-per-game effect.

**The condition.** Both the 0 ability and the case for the +1 rest on the deck actually sitting at 55+ life by turns 6–8, which is goldfish item 2 from the shape review and has not been reported back. If games in this pod end before that, or the deck's life total is usually 40-something, Strength of the Pride is a 4-mana lifegain engine in a deck that has 17 of them, and the answer is NO like Goldmane. **Confirm two things before buying: how long games in this pod actually run, and what your end-of-turn-7 life total typically is.**

**The cut.** The Wandering Emperor, for the reasons above (suppression 15 → 14, still within the shape target's "hold" range given 7 other instant-speed single-target answers; her −2 "exile target tapped creature" overlaps Swords and Path). Runners-up, spared:
- *Serra the Benevolent*: a 4/4 Angel on arrival is the deck's primary action; 30.3% inclusion; stays.
- *Valorous Stance*: named as the Teferi's Protection cut in the remaining-budget review and still the weakest non-planeswalker slot, but the user asked for a planeswalker-for-planeswalker swap, so it is not the cut here.

**Budget.** About $277.50 spent as of the shape review, plus $4.02 for Lightning Greaves; Strength of the Pride at $8.68 brings the total to roughly $290 of ~$300. Price is its own line; the ADD IF stands or falls on the life-total premise, not on the $8.68.

## Numbers used
| | |
|---|---|
| Ajani Goldmane | $4.83 (M11), Giada 0.3% (126/36,555), EDHREC rank 10,338 |
| Ajani, Strength of the Pride | $8.68, Giada 3.6% (1,298/36,555), rank 3,102 |
| Serra the Benevolent | $7.69 (MH1), Giada 30.3% (11,073/36,555), rank 5,749 |
| The Wandering Emperor | $3.93 (NEO), rank 5,561; not in Giada's top-4 planeswalker list |
| Other walkers on Giada's page | Elspeth Resplendent 12.0%, Elspeth, Storm Slayer 6.9% ($43.30, over cap), Archangel Elspeth 5.2% |

Prices fetched 2026-10-07 03:34–03:37 UTC. All combo checks via Commander Spellbook: 0 before and after each candidate.
