# Kindred Judgment, for Austere Command (2026-10-24)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards), the current working list, not the precon `base.txt`.
Prices: Scryfall, fetched 2026-10-24 06:34 UTC. EDHREC: Kindred Judgment card page and Giada commander page (fetched 2026-10-24). Spellbook: `combos.py --add` (reads `base.txt`).

## Verdict

| Card | Verdict |
|---|---|
| Kindred Judgment | **ADD, cut Austere Command.** |

Applied 2026-10-24 after the user made the swap in Moxfield: `complete.txt`, `adds.txt` and `removal.txt` updated. `base.txt` is unchanged; `moxfield.txt` is the user's export and is untouched.

## Prior history

The 2026-10-02 build-out review rejected Kindred Judgment in one row with Angelic Accord and Book of Exalted Deeds. The reason given ("Accord and Book duplicate Resplendent Angel and Harbinger") is about those two cards only. Kindred Judgment was never evaluated on its own. This is its first real review.

## Facts (all verified this session)

**Kindred Judgment** {5}{W}{W}, Sorcery. "Choose a creature type. Destroy all creatures that aren't of the chosen type." Legal, mono-white, **not a Game Changer**. No official rulings. $1.50 (FRA). EDHREC rank 11284.

Trigger-scope read:

| Axis | Kindred Judgment |
|---|---|
| Whose permanents | **All** creatures, yours included, that aren't the chosen type |
| Whose turn | Sorcery, your main phase |
| Targeted | No. Gets past hexproof, ward and protection. Does not get past indestructible (destroy). |
| Who chooses | **You** choose the type |

Cards cited below, with the clause the argument rests on:

| Card | Clause |
|---|---|
| Austere Command | {4}{W}{W} "Choose two — Destroy all artifacts. / Destroy all enchantments. / Destroy all creatures with mana value 3 or less. / Destroy all creatures with mana value 4 or greater." |
| Farewell | {4}{W}{W} "Choose one or more — Exile all artifacts. / creatures. / enchantments. / graveyards." Game Changer. |
| Elesh Norn, Grand Cenobite | {5}{W}{W} Phyrexian Praetor. "Creatures your opponents control get -2/-2." |
| Ob Nixilis, the Ascended | {5}{W}{W} Angel. "When Ob Nixilis enters, destroy all tapped creatures your opponents control." |
| Flawless Maneuver | "Creatures you control gain indestructible until end of turn." Free with a commander out. |
| Akroma's Will | mode 2: "Creatures you control gain lifelink, indestructible, and protection from each color until end of turn." |
| Clever Concealment | "Any number of target nonland permanents you control phase out." |
| Avacyn, Angel of Hope | "Other permanents you control have indestructible." |
| Sephara, Sky's Blade | "Other creatures you control with flying have indestructible." |
| Court of Grace | upkeep: 4/4 white **Angel** token if monarch, else 1/1 white **Spirit** token |
| Emeria's Call | two 4/4 **Angel Warrior** tokens |
| Valkyrie Harbinger, Resplendent Angel, Ob Nixilis | each end step: 4/4 white **Angel** token on their lifegain condition |
| Pearl Medallion | "White spells you cast cost {1} less to cast." |
| Starnheim Aspirant | "**Angel** spells you cast cost {2} less to cast." |
| Giada | "{T}: Add {W}. Spend this mana only to cast an **Angel** spell." |

## The deck as it stands

From `card_facts.py lookup` on every nonland card in `complete.txt`:

- **Creatures: 32.** Angels **25** (Giada included). Non-Angels **7**: Bishop of Wings, Drannith Magistrate, Elesh Norn, Giver of Runes, Metastatic Evangel, Starnheim Aspirant, Magus of the Moat.
- **Token makers by type.** Angel tokens: Court of Grace (as monarch), Emeria's Call, Valkyrie Harbinger, Resplendent Angel, Ob Nixilis, Serra the Benevolent −3. Non-Angel tokens: Court of Grace (not monarch, Spirit), Bishop of Wings (Spirit), Angel of Invention (Servo), The Wandering Emperor (Samurai).
- **Mass creature removal, by scope:**
  - Symmetric (hits your board too): Farewell, Austere Command.
  - One-sided: Elesh Norn (−2/−2, continuous while she lives), Ob Nixilis (opponents' **tapped** creatures only, once).
- **Cards that make a symmetric wipe one-sided:** Flawless Maneuver, Akroma's Will, Clever Concealment, Avacyn (all yours), Sephara (your fliers only). 5. These are also the deck's whole answer to *opponents'* wipes.
- **Mass artifact/enchantment removal:** Farewell, Austere Command (2). Spot artifact/enchantment removal: Generous Gift, Get Lost, Grasp of Fate, Angel of the Ruins (4).
- **Loss modes on record:** ground alpha strikes ("the majority of wins come through ground (non-flying) attacks", `meta.json`, user report 2026-10-02), Giada removed (2026-10-05), wipes (2026-10-02).

## Kindred Judgment through the rubric

**Best case, as a falsifiable claim.** Naming Angel, Kindred Judgment is a single-card wipe that kills every opposing creature except Angels and Changelings, while 25 of this deck's 32 creatures and all six of its Angel-token sources survive. The deck's only other one-sided mass removal is conditional (Ob Nixilis: tapped creatures only) or a 7-mana creature that has to stay alive (Elesh Norn). Its symmetric wipes need a second card from the protection suite to stay one-sided, and that suite is the deck's defence against opposing wipes. The pod's main way to win is a wide ground board, and this card answers that board without costing you yours.

**Hard vetoes.** Colour identity: W, legal. Format: legal. Not a Game Changer, so the count stays at 2 of 3 (Farewell, Drannith Magistrate). `combos.py --add`: completes 0 combos. Price $1.50, well under the $40 cap. **Passes.**

**Redundancy (effect × frequency × duration).**

| Card | Effect | Frequency | Duration | Your board |
|---|---|---|---|---|
| Kindred Judgment | destroy all non-Angels | once | permanent | loses 7 non-Angel creatures and non-Angel tokens |
| Austere Command | destroy one or both MV bands, plus art/ench | once | permanent | loses everything in the band unless a protection card is spent |
| Farewell | exile any subset | once | permanent | same as Austere, but exile also beats indestructible |
| Ob Nixilis | destroy opponents' tapped creatures | once (ETB) | permanent | none, plus a 4/4 body and an Angel engine |
| Elesh Norn | −2/−2 to opponents | continuous | while she lives | none, but she is the effect and dies to removal |

The cards whose effect line rhymes with Kindred Judgment (Austere, Farewell) are not redundant with it on the term that matters, which is what happens to *your* board. The ones that match on one-sidedness (Ob Nixilis, Elesh Norn) differ on scope (tapped only) or duration (as long as a creature lives). Austere Command is the closest. Kindred Judgment beats it at the one job this deck casts it for.

**Austere + protection already makes a one-sided wipe. Does that kill the case?** That was the strongest objection, and it doesn't hold. That line needs two cards. It also spends Flawless Maneuver, Akroma's Will or Clever Concealment on your own wipe, and those 5 cards are the deck's only cover against an opponent's wipe. Kindred Judgment does it with one card and keeps the protection in hand.

**Density.** The card needs your board to be Angels. 25/32 creatures are Angels (78%), and 6 token sources make Angels. Well above the threshold.

**Marginal impact on games you lose.** It works directly against the recorded main loss mode, a wide ground board. Magus of the Moat, Ghostly Prison and Archangel of Tithes slow that board down. Kindred Judgment removes it, and your fliers stay in play to swing into the empty board next turn. Against the "Giada removed" loss it does nothing, and Austere did nothing there either. This is not win-more: it is a card you cast when you are behind on board. The verdict does not rest on any speed premise, so `meta.json`'s speed and archetype lines were not pressure-tested.

**Cost of entry.** 7 MV and {W}{W}, against Austere's 6 and {W}{W}: +1 to the swap's total MV, and the 6+ count doesn't change because it replaces a 6-drop. It is a **sorcery, not an Angel**, so Giada's mana, Starnheim Aspirant, Urza's Incubator and Herald's Horn don't reduce it. Only Pearl Medallion does. This is the card's real cost: it is one of the few 7s in the list that the Angel ramp can't pay for.

**Anti-synergy.**
- It kills your 7 non-Angels. The painful ones are Starnheim Aspirant (a cost reducer), Magus of the Moat and Drannith Magistrate (a Game Changer). Elesh Norn dies too, but if she is in play you don't need this card. Austere Command with a creature mode chosen kills more of your board in nearly every case, Giada included.
- Spirit, Servo and Samurai tokens die. Court of Grace's tokens are Angels while you hold the monarch.
- Bishop of Wings' "Whenever an Angel you control dies" never triggers, because no Angels die.
- It doesn't kill opposing Angels, Changelings or indestructible creatures. Farewell handles the last two.

**Worst-case draw.** In the opening hand it is a dead 7-drop, one mana worse than the Austere Command it replaces, and neither does anything early. On turn twelve with an empty board it is a one-for-many against whoever is ahead, and it leaves any Angel you play next untouched. It is good at the late end and no worse than Austere at the early end.

**Bracket fit.** Not a Game Changer, not fast mana, not a tutor, no combo. A mostly one-sided wipe is a strong effect, but it costs 7 at sorcery speed and the deck already runs Elesh Norn and Ob Nixilis. Fine for upper bracket 3.

**Disagreement check.** EDHREC: **21.5% of Giada decks (1,472 / 6,853 decks since the card's release), synergy +0.15**. Austere Command: 43.1% (16,558 / 38,376). Low-to-mid inclusion while I say yes means I owe a reason. The reason: the 6,853 denominator shows the card is recent, so it competes with years of built lists that never updated. Its positive synergy says Giada lists play it more than average decks do. Most importantly, the deck-specific reason is countable: this list is 78% Angels and its pod wins on the ground. A Giada list with more Humans and Clerics, or a pod that wins with fliers, would rate it lower.

## The cut

Same role first. Kindred Judgment is a creature wipe, so a creature wipe leaves.

1. **Austere Command — cut.** Kindred Judgment beats it as a creature wipe in this deck in almost every board state, as shown above. The 2026-10-02 build-out review kept Austere for its "more flexible modes", and that reason still holds: the artifact and enchantment modes go out with it. Mass artifact/enchantment removal drops from 2 to 1 (Farewell). Spot artifact/enchantment removal stays at 4 (Generous Gift, Get Lost, Grasp of Fate, Angel of the Ruins), and the 2026-10-14 review's count of six total answers becomes five. The artifact mode also destroyed this deck's own 11 mana rocks and artifacts, so it was rarely the mode you wanted. **Not the last of a role:** Farewell remains as a symmetric mass answer.
2. **Valorous Stance — runner-up.** Cut this instead if you want to keep Austere's artifact/enchantment flexibility and run three wipes. The cost is a cheap instant protection or removal spell, and the deck's wipe count goes up in a creature deck. Spared because it is a 2-mana instant, and the protection suite is the other half of this argument.
3. **Farewell — spared.** It exiles, so it handles indestructible creatures and graveyards, which Kindred Judgment doesn't. Cutting it would free a Game Changer slot, but it is not a worse card.

Not considered: lands (38 is right at 3.5 average MV) and any of the 25 Angels (they are why this card works).

## Price

Kindred Judgment $1.50 (fetched 2026-10-24 06:34 UTC). Austere Command $0.37, same fetch. The verdict doesn't rest on price. It would be the same if the card cost $40.

## What would change this

- **The pod adds Angel, Changeling or indestructible-heavy decks.** Naming Angel stops being one-sided against them. Then Farewell is the better wipe and Austere matters more.
- **You find yourself reaching for Austere's artifact or enchantment modes.** If artifact or enchantment boards beat you often, take the Valorous Stance cut instead.
- **The list moves toward more non-Angel support** (more Humans or Clerics). Each one lowers the density this verdict rests on.
