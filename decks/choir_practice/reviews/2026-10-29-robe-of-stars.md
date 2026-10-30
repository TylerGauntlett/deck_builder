# Robe of Stars (2026-10-29): NO

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `base.txt` (100 cards). Card texts for the deck's own cards come from `cards.md` (Scryfall, generated 2026-10-28).
Prices: Scryfall, fetched 2026-10-29 23:26 UTC. EDHREC: Robe of Stars card page and Giada commander page (38,846 decks). Spellbook: `combos.py --add`.

## Facts (verified this session)

**Robe of Stars** {1}{W}, Artifact — Equipment. "Equipped creature gets +0/+3. Astral Projection — {1}{W}: Equipped creature phases out. … Equip {1}." Legal, colour identity W, not a Game Changer.
Rulings (2021-07-23):
- A phased-out creature keeps its counters.
- It can't block, and it is removed from combat.
- Phasing doesn't trigger leaves- or enters-the-battlefield abilities.
- It phases back in during your untap step.

## Steel-man

A repeatable, instant-speed answer for one creature to **every** removal type: destroy, exile, -X/-X, bounce, targeted or mass. The deck's existing protection is mostly *indestructible*, which does nothing against exile wipes such as Farewell. Robe would let Giada, or an Archangel of Thune covered in counters, survive a wipe and lead the rebuild.

## The tests

**Redundancy: effect × frequency × duration.** The protection suite in the list:

| Card | Covers | Frequency | Scope |
|---|---|---|---|
| Swiftfoot Boots | targeted (opponents') | permanent, passive | one creature |
| Lightning Greaves | all targeting | permanent, passive | one creature |
| Giver of Runes | targeted/coloured, one colour | repeatable, needs to untap | one other creature |
| Flawless Maneuver | destroy | one-shot, free with a commander | whole board |
| Clever Concealment | **everything** (phasing) | one-shot | any number of your nonland permanents |
| Akroma's Will | destroy + coloured (both modes with commander) | one-shot | whole board |
| Valorous Stance | destroy | one-shot | one creature |
| Avacyn, Angel of Hope | destroy | permanent | all other permanents |
| Sephara, Sky's Blade | destroy | permanent | other fliers |

That's nine cards. Robe's unique slice is *repeatable* protection from exile and -X/-X wipes, for one creature. Every other cell it covers is already filled, often by a passive card that costs no mana each turn.

**Cost of the unique slice.** You need {1}{W} to cast it and {1} to equip (sorcery speed, before the threat arrives). Then you hold {1}{W} open on every opponent's turn. That's 5 mana before it protects anything once. Against targeted removal, Boots and Greaves already do the job with no mana held up.

**What it saves.** On Giada, a 2/2 with no counters of her own, the alternative is recasting her for 4 (commander tax). Robe's 5-mana investment barely beats that. On a large Angel it saves more, but you have to have guessed in advance which one to equip.

**Anti-synergy.**
- **Lightning Greaves** gives shroud ("can't be the target of spells or abilities"), so Robe's equip can't target a creature wearing Greaves. They can't both be on Giada. Swiftfoot Boots (hexproof, opponents only) can share.
- Phasing Giada out leaves you without a commander on the battlefield until your untap step. Flawless Maneuver ("If you control a commander…") loses its free cast, and Akroma's Will ("If you control a commander as you cast this spell…") becomes single-mode. That window is exactly when a wipe is on the stack. You have to sequence those cards before phasing.
- A phased-out creature can't block. The pod mostly wins with ground attacks, so this matters on the turn you use it.

**Synergy (three named cards?).**
- The +0/+3 does nothing for the deck. Righteous Valkyrie gains life equal to a creature's toughness when it *enters*, before any equip.
- Herald of Eternal Dawn already covers the "survive the turn" role.
- There are no equipment payoffs in the list.

No three-card synergy.

**Marginal impact.** It only matters in the narrow case where an exile or -X/-X wipe resolves *and* Clever Concealment isn't available. Teferi's Protection is already on the books as the open ADD IF for that exact risk. It covers the whole board and you, not one creature.

**Worst case.**
- Early: a 2-drop that does nothing until there's something worth equipping.
- Late with an empty board: dead.

**Bracket.** Not a Game Changer. 0 combos, 0 near (`combos.py --add`).

**Disagreement check.** It doesn't appear on the Giada commander page. Giada isn't among Robe's top 24 commanders on its card page either. Low community inclusion agrees with the verdict.

**Speed premise.** The verdict doesn't rest on it.

## Price (separate factor)

**$13.95**, fetched 2026-10-29 23:26 UTC. Under the cap. **The NO holds if it's free.**

## Counter-proposal

None. If exile or -X/-X wipes start costing games, the answer is the existing ADD IF: **Teferi's Protection** (Game Changer #3, cut Valorous Stance; see the 2026-10-02 remaining-budget review). Its price hasn't been refetched this session.

## Verdict

**NO.** It would be the tenth protection card, and it covers one creature at 5 mana up front plus 2 per use. It conflicts with Lightning Greaves and briefly switches off the commander-keyed cards.
