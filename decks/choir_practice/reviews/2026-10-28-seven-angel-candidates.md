# Seven candidates: Starnheim Unleashed, Herald of the Host, Yoshimaru, Sanctuary Warden, Angelic Sleuth, Patron of the Valiant, Moonsilver Spear (2026-10-28)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards), the current working list, not the precon `base.txt`.
Prices: Scryfall, fetched 2026-10-28 21:56 UTC. EDHREC: each candidate's card page and the Giada commander page (fetched 2026-10-28). Spellbook: `combos.py --add` with all seven (reads `base.txt`).

## Verdict

| Card | Verdict |
|---|---|
| Herald of the Host | **ADD, cut Gisela, the Broken Blade.** |
| Starnheim Unleashed | NO. A seventh Angel-token source, and as a sorcery it gets none of the deck's Angel discounts. |
| Sanctuary Warden | NO. An eleventh card at MV 6+, buying card draw the deck already has. |
| Moonsilver Spear | NO. Eight mana before the first Angel. Herald does the same job for 5. |
| Patron of the Valiant | NO. A one-time +1 counter in a deck with 8 anthem effects and 2 proliferators. |
| Yoshimaru, Beloved Companion | NO. A 3-mana non-Angel 2/2 that only multiplies engines the deck already has. |
| Angelic Sleuth | NO. Cut on 2026-10-02 as the weakest card. Herald makes it better, but not enough. |

Seven adds would need seven cuts. Only one card survived, so the batch question doesn't come up.

## Facts (all verified this session)

All seven are legal and mono-white or colourless. None is a Game Changer. `combos.py --add` with all seven: **0 new combos**.

| Card | Cost | Text the argument rests on |
|---|---|---|
| Herald of the Host | {3}{W}{W} Angel 4/4 | Flying, vigilance. "Myriad (Whenever this creature attacks, for each opponent other than defending player, you may create a token copy that's tapped and attacking that player... Exile the tokens at end of combat.)" |
| Starnheim Unleashed | {2}{W}{W} Sorcery | "Create a 4/4 white Angel Warrior... If this spell was foretold, create X of those tokens instead." Foretell {X}{X}{W} |
| Sanctuary Warden | {4}{W}{W} Angel Soldier 5/5 | Enters with two shield counters. "Whenever this creature enters or attacks, you may remove a counter from a creature or planeswalker you control. If you do, draw a card and create a 1/1... Citizen" |
| Moonsilver Spear | {4} Equipment | "Whenever equipped creature attacks, create a 4/4 white Angel creature token with flying." Equip {4} |
| Patron of the Valiant | {3}{W}{W} Angel 4/4 | ETB: "put a +1/+1 counter on each creature you control with a +1/+1 counter on it." |
| Yoshimaru, Beloved Companion | {2}{W} legendary **Dog** 2/2 | "If one or more +1/+1 counters would be put on a creature you control, that many plus one... instead." |
| Angelic Sleuth | {2}{W} Angel Advisor 2/3 | "Whenever another permanent you control leaves the battlefield, if it had counters on it, investigate." |

Herald of the Host rulings (2015-11-04) that matter here:
- "Any enters-the-battlefield abilities of the copied creature will trigger when the token enters... 'enters with' abilities... will also work."
- The tokens "were never declared as attackers. Abilities that trigger whenever a creature attacks won't trigger."
- "The token creatures all enter the battlefield at the same time."

Giada: "Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control." Ruling 2024-11-08: "each Angel you control other than the Angel entering, including Giada."

## The deck as it stands (script counts from `complete.txt`)

- 63 spells (Emeria's Call counted as a spell), 37 lands + the Emeria's Call MDFC. Curve: 1:4, 2:16, 3:15, 4:11, 5:7, 6:2, 7:7, 8:1. **MV 6+: 10** (Herald of Eternal Dawn, Emeria's Call, Sephara, Avacyn, Elesh Norn, Ob Nixilis, Farewell, Kindred Judgment, Valkyrie Harbinger, Angel of the Ruins).
- Creatures: **25 Angels, 7 non-Angels** (Bishop of Wings, Drannith Magistrate, Elesh Norn, Giver of Runes, Metastatic Evangel, Starnheim Aspirant, Magus of the Moat).
- **Discounts that only apply to Angel or creature spells:** Giada's mana, Starnheim Aspirant, Urza's Incubator, Herald's Horn (4). Cast triggers on Angel spells: Folk Hero, Vanquisher's Banner. Pearl Medallion is the only discount that applies to every white spell.
- **Angel-token sources (6):** Court of Grace (while you're the monarch), Emeria's Call, Valkyrie Harbinger, Resplendent Angel, Ob Nixilis, Serra the Benevolent −3.
- **Cards that trigger when an Angel or creature *you control* enters:** Giada (Angels, counters), Bishop of Wings (Angel, 4 life), Righteous Valkyrie (Angel or Cleric, life equal to its toughness), Dazzling Angel (any creature, 1 life), Seraph Sanctuary (Angel, 1 life), Cathars' Crusade (any creature, +1/+1 counter on each creature), Youthful Valkyrie (Angel, +1/+1 counter on itself). **Seven.** Metastatic Evangel is left out because it only triggers on nontoken creatures.
- **Payoffs when you gain life:** Archangel of Thune, Lyra, Archangel of Dawn, Exemplar of Light, Dawn of Hope; at end step, Valkyrie Harbinger (4+ life), Resplendent Angel (5+), Ob Nixilis (any).
- **Anthem-style buffs:** Lyra Dawnbringer, Angel of Invention, Thraben Watcher, Elesh Norn, Righteous Valkyrie (at +7 life), Vanquisher's Banner, Patchwork Banner, Angelic Field Marshal (vigilance only, plus its own +2/+2). **Proliferate:** Metastatic Evangel, Norn's Choirmaster.
- **Repeatable +1/+1 counter sources:** Giada, Cathars' Crusade, Archangel of Thune, Lyra Archangel of Dawn, Youthful Valkyrie, Exemplar of Light, Angel of Invention (fabricate), The Wandering Emperor +1, plus the 2 proliferators.
- **Card draw:** Tome of Legends, Mind Stone, Dawn of Hope, Folk Hero, Exemplar of Light, Inspiring Overseer, Wojek Investigator, Vanquisher's Banner, Herald's Horn (card selection), Bonders' Enclave, War Room, Minas Tirith, Secluded Steppe cycling.

**Two modes and the bridge.** One plan is to go wide with fliers and swing. The other is to gain life so the end-step token makers fire. The bridge is the seven Angel-entering triggers listed above: each Angel that enters turns into life, which turns into more Angels at end step and more counters from Thune and Lyra AoD. A card that makes Angels enter **every turn** feeds both plans at once.

## Herald of the Host: ADD

**Best case.** Each attack puts two extra Angels onto the battlefield, attacking the other two opponents. Each copy enters under Giada with one +1/+1 counter for every Angel you control, Herald included. The ruling confirms that "enters with" effects apply. Each copy also fires all seven of the deck's Angel-entering triggers. With Giada and two other Angels out, each copy enters as a 4/4 with 4 counters, an 8/8 flier, and swings at a different player. Bishop of Wings alone turns that into 8 life, enough for both Harbinger's and Resplendent's end-step thresholds.

**Is it real?** Verified synergy, by card: Giada, Bishop of Wings, Righteous Valkyrie (life equal to each copy's toughness, counters included), Dazzling Angel, Seraph Sanctuary, Cathars' Crusade (two triggers per attack), Youthful Valkyrie. Lyra Dawnbringer gives the copies lifelink. Downstream: Thune, Lyra AoD, Exemplar, Harbinger, Resplendent, Ob Nixilis. That is well past three named cards.

**Attacks.**
- *Vetoes:* passes, as above.
- *Multiplicative or additive?* Multiplicative. The copies' size scales with your Angel count, and their triggers scale with your board. This is the kind of card the rubric's closing filter favours.
- *Cost of entry:* 5 MV and an Angel, so all four discounts and Giada's mana apply. With Aspirant out it costs 3.
- *Pod fit:* most games are won with ground attacks (`meta.json`). Herald attacks in the air and has vigilance, so it still blocks. The verdict doesn't depend on a speed premise.
- *Weaknesses:* no haste, so it needs a turn cycle to survive. Swiftfoot Boots and Lightning Greaves cover that. The copies are exiled, not killed, so Bishop of Wings' death trigger doesn't fire. Hitting all three opponents every turn draws attention. Against a single opponent, myriad does nothing (ruling), which matters late in the game.
- *Disagreement check:* EDHREC has it in **13.8% of Giada decks (5,335 / 38,783), synergy +0.12**. That is low for an ADD. The deck-specific reason is countable: this list has seven Angel-entering triggers and 25 Angels, so each copy does more here than in an average Giada list.

### The cut: Gisela, the Broken Blade

Same role. The shape review counts both as Angel "generators" with the note "hold (swap weakest)".

Gisela is a 4-mana 4/3 with flying, first strike and lifelink, and nothing else in this deck. The meld needs Bruna, which isn't in the list. The 2026-10-02 shape review kept Gisela "as a 4-mana lifelink first-striker that feeds Thune and Lyra AoD each combat." **That reason still partly holds, so here is the trade-off.** Gisela gains life on her own. Herald only causes lifegain when Bishop of Wings, Righteous Valkyrie, Dazzling Angel, Seraph Sanctuary or Lyra Dawnbringer is out. When one is, Herald gains more life per combat than Gisela, because two Angels enter and there is more lifelinked damage. When none is, Gisela is the better lifegain card. Herald wins on damage and board in every case.

Side effects: 4-drops 11 → 10, 5-drops 7 → 8; average MV up by about 0.02. Legendary creatures go down by one, which affects Eiganjo's discount and Minas Tirith entering untapped. Angels stay at 25.

Runners-up, spared:
1. **Angel of Vitality.** A 3-mana 2/2. Its "+1 life" replacement adds 1 to each copy's Bishop, Righteous Valkyrie, Dazzling and Seraph Sanctuary trigger, so Herald makes it better. Cut this one instead if you'd rather keep the 4-drop.
2. **Valorous Stance.** Still set aside as the Teferi's Protection cut (remaining-budget review). Not spent twice.
3. **Patchwork Banner.** The ramp was already trimmed once (Heraldic Banner, 2026-10-14). Don't cut it below the count the curve needs.

## The rejections

**Starnheim Unleashed (NO).** *Best case:* flexible. At 4 mana it makes one 4/4 Angel, and if foretold early it makes three at 7 mana or four at 9, each with Giada counters. *What kills it:* the deck already has 6 Angel-token sources, and Emeria's Call fills the same 7-mana slot. Starnheim is a sorcery, so Giada's mana, Aspirant, Incubator and Horn don't reduce it and Folk Hero and Vanquisher's Banner don't draw off it. Only Pearl Medallion helps. The tokens enter at the same moment, so they don't count each other for Giada. It is additive in a category that is already six deep. 14.2% of Giada decks (5,491 / 38,783). Would still be NO if it were free.

**Sanctuary Warden (NO).** *Best case:* a resilient 6-drop. Two shield counters plus Giada counters, and a card and a 1/1 on entering and on each attack, paid for by removing a counter (its own shield counter works). It is the most popular candidate: **17.2% (6,677 / 38,783)**. *What kills it:* the deck already has **10 cards at MV 6+**. Card draw has 13 sources listed above. Exemplar and Wojek already draw every turn. The only other 6-MV creature is Valkyrie Harbinger, which is an engine, so there is no clean like-for-like cut. The realistic swap is Angel of the Ruins at 7. *Closest of the six.* If games show the deck running out of cards rather than mana, reconsider it for Angel of the Ruins.

**Moonsilver Spear (NO).** *Best case:* a permanent 4/4 Angel on every attack, with Giada counters, kept after combat, unlike Herald's copies. *What kills it:* 4 + equip 4 = 8 mana before the first token. It is an artifact, so no Angel discount applies, and the equipped creature has no protection. Herald does "attack, get Angels" for 5 in one card. With Herald in, the Spear is redundant. 12.4% (4,791 / 38,783).

**Patron of the Valiant (NO).** *Best case:* under Giada nearly every Angel has a counter, so this is +1/+1 to the team on a 4/4 flier. *What kills it:* it happens once and is additive. The deck has 8 anthem effects and 2 proliferators, and Norn's Choirmaster does this every time Giada attacks. 7.8% (3,039 / 38,783).

**Yoshimaru, Beloved Companion (NO).** *Best case:* the only multiplier in the batch apart from Herald. Every Angel enters with one more Giada counter, Thune and Cathars' Crusade put 2 counters each instead of 1, and there are 10 counter sources listed above. *What kills it:* it is a **Dog**. Giada's mana, Aspirant, Incubator, Horn, Folk Hero and Vanquisher's Banner don't apply. It dies to the deck's own Kindred Judgment, which brings the non-Angels to 8. Alone it is a 3-mana 2/2 that doesn't fly. The extra counter is roughly a third Banner for Angels you cast after it, and the anthem category is already 8 deep. EDHREC doesn't list Giada among its top commanders at all. It would be NO if it were free.

**Angelic Sleuth (NO).** Cut on 2026-10-02 as "the weakest remaining card." The only new fact is Herald of the Host: its copies leave the battlefield with Giada counters on them, so Sleuth would investigate twice per Herald attack. That is a real two-card synergy, but it depends on one specific card, and the deck's card draw isn't thin. 16.7% (6,496 / 38,783). Still NO.

## Prices (fetched 2026-10-28 21:56 UTC)

Herald of the Host $0.39 · Starnheim Unleashed $1.73 · Sanctuary Warden $1.52 · Moonsilver Spear $0.67 · Patron of the Valiant $0.21 · Yoshimaru $0.31 · Angelic Sleuth $0.47. All are under the cap, and price decided none of the verdicts.

## What would change this

- **Herald copies often run into a single remaining opponent** (late game, eliminations). Myriad does nothing then. Watch for it.
- **None of the five lifegain-on-entry cards tends to be out when Herald attacks.** Then Gisela's built-in lifelink matters more, so swap the cut to Angel of Vitality and keep Gisela.
- **Hands run out of cards before mana:** reconsider Sanctuary Warden for Angel of the Ruins.
