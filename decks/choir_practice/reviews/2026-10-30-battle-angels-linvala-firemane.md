# Battle Angels of Tyr, Linvala Keeper of Silence, Firemane Commando (2026-10-30)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap, ~$300 total.
Evaluated against the user's current list. It is `base.txt` with **Land Tax in and Mind Stone out**, as recommended 2026-10-29; `base.txt` itself has not been updated. The list has 37 lands (27 Plains), 63 nonland cards at average MV 3.60, and 25 Angels.
Curve (nonland): 1:5, 2:15, 3:14, **4:12**, 5:8, 6:2, 7:6, 8:1.
Prices: Scryfall, fetched 2026-10-30 03:04 UTC. EDHREC: Giada commander page, 38,846 decks. Spellbook: `combos.py` with all three candidates plus Land Tax → 0 new combos, 0 near.

## Verdicts

| Card | Verdict |
|---|---|
| Battle Angels of Tyr | **ADD, cut Tome of Legends** |
| Linvala, Keeper of Silence | **NO** |
| Firemane Commando | **NO as an addition.** ADD IF it replaces Seraph of the Sword *and* Seraph isn't stopping the attacks aimed at you |

## Facts (verified this session)

- **Battle Angels of Tyr** {2}{W}{W} 4/4 Angel Knight. Flying, myriad. "Whenever this creature deals combat damage to a player, draw a card if that player has more cards in hand than each other player. Then you create a Treasure token if that player controls more lands than each other player. Then you gain 3 life if that player has more life than each other player." $31.26.
  Rulings: conditions are checked on resolution. Myriad tokens enter attacking and are **not declared attackers**. Tokens copy the printed card only (no counters). "Enters with" effects apply to them.
- **Linvala, Keeper of Silence** {2}{W}{W} 3/4 legendary Angel. Flying. "Activated abilities of creatures your opponents control can't be activated." This includes mana abilities. Triggered abilities and abilities that work from other zones are unaffected. $20.71.
- **Firemane Commando** {3}{W} 4/3 Angel Soldier. Flying. "Whenever you attack with two or more creatures, draw a card. Whenever another player attacks with two or more creatures, they draw a card if none of those creatures attacked you." $0.93.

None is a Game Changer. All are legal in mono-W.

## Battle Angels of Tyr: ADD

**Why this reverses the 2026-10-02 NO.** The build-out review rejected it as "not better than any remaining 4-drop by enough to justify $29". That rested on price and predated **Herald of the Host** (added 2026-10-28). That review showed myriad is an Angel-*entering* engine in this deck, not just evasion. Battle Angels is a second copy of that engine, one mana cheaper.

**Best case.** Each attack in a 4-player pod makes two token copies, each an Angel entering under your control. Verified from the list:
- **Giada** gives each token "an additional +1/+1 counter … for each Angel you already control".
- **Cathars' Crusade** triggers twice (a counter on every creature each time).
- **Bishop of Wings** triggers twice (8 life).
- **Righteous Valkyrie** gains life equal to each token's toughness.
- **Seraph Sanctuary** and **Dazzling Angel** each trigger twice.
- **Youthful Valkyrie** gets two counters.

Each of those gains is a separate event for **Archangel of Thune**, **Lyra, Archangel of Dawn**, **Exemplar of Light** and **Dawn of Hope**. It serves both modes: the tokens are extra evasive attackers (go-wide mode), and their entering grows the board (counter mode). On top of that, every copy that connects checks its own draw / Treasure / life clauses. **Akroma's Will**'s double strike makes each copy check them twice.

**Scope of the combat trigger.** "More cards in hand than **each other player**" includes you. The three copies split across the three opponents, so you typically collect the card from whichever opponent holds the most, and the Treasure from whoever has the most lands. The life clause rarely fires, because this deck is usually the highest life total. Count on roughly one card and one Treasure per connecting combat, not three of each.

**Redundancy.** Only Herald of the Host does this. That's one comparable card, so it passes. Two myriad bodies make it more likely the engine is online, and both together put four Angels onto the battlefield per combat.

**Cost of entry.** 4 MV, {W}{W}, and it's an Angel, so Giada's mana, Starnheim Aspirant (−2), Urza's Incubator (−2), Herald's Horn and Pearl Medallion all apply. It has no vigilance of its own. Angelic Field Marshal (with Giada) and Thraben Watcher ("other nontoken creatures … have vigilance") cover that.

**Worst case.** On turn 4 it is a 4/4 flier that must survive a turn cycle before it attacks. As a late topdeck it is still a 4/4 flier, worth two Angels entering per attack. It is never dead, and its floor is the vanilla 4/4 flier the deck plays anyway.

**Disagreement check.** 48.3% of Giada decks (18,746 / 38,846) run it, so the community agrees. Independent reason: this list already runs the myriad engine plus Cathars' Crusade, Bishop of Wings, Archangel of Thune and Lyra AoD, which every token feeds.

**Anti-synergy.** Myriad tokens aren't declared attackers. They don't trigger Firemane Commando, Minas Tirith's "attacked with two or more creatures", Tome of Legends or Norn's Choirmaster. They are exiled at end of combat, which isn't dying, so Bishop of Wings makes no Spirits.

### The cut: Tome of Legends

It is the weakest card on the draw side, and it's off-tribe. "Whenever your commander enters or attacks, put a page counter … {1}, {T}, Remove a page counter: Draw a card." It needs Giada, a 2/2, to attack each turn to keep drawing. It is a non-Angel artifact, so it gets none of the Angel synergies. Card draw stays deep without it:
- Folk Hero, Dawn of Hope, Vanquisher's Banner, Exemplar of Light, Inspiring Overseer, Wojek Investigator and Court of Grace (monarch)
- Minas Tirith, War Room and Bonders' Enclave
- now Battle Angels' own combat draws

The swap adds an Angel (25 → 26), and the curve trades a 2-drop for a 4-drop (4-drops 12 → 13).

Runners-up, spared:
1. **Wojek Investigator.** Its Clues only come when an opponent has more cards in hand than you, but it's an Angel: Giada counters, Bishop, Righteous Valkyrie, Folk Hero and Vanquisher's all key off it. It's also a 2/4 vigilant flying blocker for a player who gets targeted. Take this cut instead if Tome has been drawing well in practice.
2. **Seraph of the Sword.** It was your pick on 2026-10-28 for blocking the attacks aimed at you, and that reason still holds. It's the swap target for Firemane below, so don't spend it twice.
3. **Thraben Watcher.** Gives Battle Angels the vigilance it lacks.
4. **Dazzling Angel.** Still the only gain source that triggers on non-Angel creatures entering (2026-10-28 addendum), and it triggers on myriad tokens too.
5. **Valorous Stance, Fateful Absence.** Still held back as the cuts for Teferi's Protection and Darksteel Mutation.

## Linvala, Keeper of Silence: NO

**Best case.** A 4-mana 3/4 flying Angel with all the tribal synergies that also switches off every opponent's creature activations: mana dorks, creature sac outlets, Walking Ballista-style combos, and commanders with tap abilities. It doesn't affect your own creatures (Giada's mana, Giver of Runes, Resplendent Angel).

**What kills it.**
- **Its value depends on what opponents play.** The meta is "judged on general usefulness across unknown decks", the same test that cut Archivist of Oghma. In a pod with no dork or creature-combo decks, it's a 3/4 flier.
- **As a body, it adds nothing distinctive.** It would be the 26th or 27th Angel, at a 4-drop slot that's already the deck's widest (12 cards). The deck already has one hate piece, Drannith Magistrate, covering a different axis (spells cast from outside the hand).
- **It doesn't address your stated problem.** You're targeted by attacks, and Linvala doesn't stop attacks.
- **It forces a cut you'd defend.** After Tome of Legends, the next cut is Wojek, Seraph, Thraben Watcher or Dazzling Angel, and each was spared above for a specific reason.

**Disagreement check.** 43.7% of Giada decks run it (16,994). The difference here: the list is already 25 Angels deep with a full 4-drop slot, so it has to win on its static ability alone, and that ability depends on the pod.

**Would change my mind:** if the pod regularly fields creature-based combo decks, mana dork ramp, or commanders that win through activated abilities.

## Firemane Commando: NO as an addition; ADD IF it replaces Seraph of the Sword

**Consistency with 2026-10-28.** That review moved Firemane to ADD IF the targeting is mainly combat damage. The plan was then replaced by Seraph of the Sword in the same role. The reasons from both still hold:
- **For it:** its second clause pays opponents who attack someone else. Combined with Ghostly Prison, Archangel of Tithes and Magus of the Moat (all still in the list), attacking you is taxed and attacking elsewhere is rewarded.
- **Against it:** Magus of the Moat stops ground attacks for everyone, so the reward rarely fires while Magus is out. It gives the table cards. Its own-attack draw overlaps Minas Tirith. Myriad tokens don't count toward "attack with two or more creatures", because they aren't declared attackers.

**As an addition**, it is a third anti-targeting card on top of Seraph and the three attack taxes, in a card-draw category that's already deep. It would take the cut that Linvala couldn't find either. NO.

**As a swap for Seraph**, it depends on what's happening at the table:
- If Seraph is holding off the attacks (blocking one big non-trampler each turn), keep it.
- If opponents are getting around it with trample or several attackers, Firemane's incentive works on the whole attack rather than one creature. It also draws you a card on your own 2-creature attacks. In that case, Firemane for Seraph.

## Aggregate delta (recommended change only)

- +Battle Angels of Tyr, −Tome of Legends.
- Angels 25 → 26. Curve: one 2 out, one 4 in, average nonland MV 3.60 → ~3.63.
- Lifegain events per combat: up to +2 Angels entering per attack (+4 with Herald of the Host).
- Card draw: −1 source (Tome), +1 combat-conditional source.
- Combos: 0. Game Changers: still 2.

All three in at once would mean three cuts. After Tome, every remaining candidate was spared for a stated reason. That's the main finding for the batch: there is room for **one** of these three, and Battle Angels is the one.

## Prices (separate factor)

Fetched 2026-10-30 03:04 UTC: Battle Angels of Tyr **$31.26** (foil $31.93), Linvala **$20.71**, Firemane Commando **$0.93**. All are under the $40 per-card cap.
The ~$300 total was last tallied on 2026-10-02 (~$277.50). Since then: Lightning Greaves, Herald of Eternal Dawn, Kindred Judgment, Herald of the Host, Seraph of the Sword and Land Tax ($16.74 on 2026-10-29). Battle Angels very likely takes the deck **over** the ~$300 guideline. That's your call. The verdict is on merit and would be the same if the card were free.
