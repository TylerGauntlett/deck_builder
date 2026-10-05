# Lightning Greaves for Archivist of Oghma (2026-10-05)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards).
Prices: Scryfall, fetched 2026-10-05 12:25–12:27 UTC. EDHREC: Giada commander page, 36,267 decks.

## The question

The user proposes cutting Archivist of Oghma for Lightning Greaves. Two table reports drive it:

1. Archivist "doesn't seem to trigger much" in their pod.
2. Giada is the centrepiece; when she is gone the deck is "a bunch of small/medium flyers".

Both are new facts from the table, not a re-argument of an old verdict. The second one is also what the 2026-10-02 shape review found on paper ("Commander dependence is high and has one guard").

## Verdict

| Card | Verdict |
|---|---|
| Lightning Greaves | **ADD, cut Archivist of Oghma.** |

Applied to `complete.txt` and `adds.txt`. `base.txt` is unchanged. `moxfield.txt` is the user's export and still lists Archivist.

## Facts (all verified this session)

**Lightning Greaves** {2}, Artifact — Equipment. "Equipped creature has haste and shroud. (It can't be the target of spells or abilities.) Equip {0}." Colorless, legal, not a Game Changer. EDHREC rank 13. $3.96.

**Archivist of Oghma** {1}{W}, Halfling Cleric 2/2, Flash. "Whenever an opponent searches their library, you gain 1 life and draw a card." $6.39.

**Swiftfoot Boots** {2}, Equipment. "Equipped creature has hexproof and haste. Equip {1}." Already in the deck. The only other Equipment in `complete.txt` (checked against `cards.json` type lines for the precon cards and by lookup for every added artifact).

**Giada, Font of Hope** {1}{W}, 2/2 flying, vigilance. "Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control. {T}: Add {W}. Spend this mana only to cast an Angel spell."

## How commander-dependent the deck really is

Cards in the list whose text names the commander, verified:

| Card | Clause |
|---|---|
| Flawless Maneuver | "If you control a commander, you may cast this spell without paying its mana cost." |
| Akroma's Will | "If you control a commander as you cast this spell, you may choose both instead." |
| Angelic Field Marshal | "Lieutenant — As long as you control your commander, this creature gets +2/+2 and creatures you control have vigilance." |
| Folk Hero | "Commander creatures you own have 'Whenever you cast a spell that shares a creature type with this creature, draw a card...'" |
| Norn's Choirmaster | "Whenever a commander you control enters or attacks, proliferate." |
| Tome of Legends | "Whenever your commander enters or attacks, put a page counter on this artifact." |

Six cards plus Giada's own counters and Angel mana. That is more commander-keyed text than a typical Giada list carries, and it confirms the user's report: without Giada the Angels are smaller, Flawless Maneuver costs 3, Akroma's Will is single-mode, and three draw/proliferate engines go quiet.

## What protects Giada today

Grouped by how they work, because the rate matters:

- **Permanent, proactive, stops targeting:** Swiftfoot Boots (hexproof, equip {1}). One card.
- **Repeatable, one colour per activation, needs to untap, dies to wipes:** Giver of Runes ("Another target creature you control gains protection from colorless or from the color of your choice until end of turn").
- **Instant-speed, one-shot:** Flawless Maneuver (indestructible; free with a commander), Clever Concealment (phase out any number of your nonland permanents), Akroma's Will (indestructible + protection from each colour), Valorous Stance mode 1 (target creature gains indestructible).

Against targeted removal before turn 6, the deck has exactly one card that is already on the board doing the job. The odds of seeing at least one such card in the opening hand plus three draws: about 10% with Boots alone, about 19% with Boots and Greaves. That is the category Greaves goes into.

## Lightning Greaves through the rubric

**Best case.** The second cheap, permanent anti-targeting piece for a commander that six other cards key off, and the only one with equip {0}, which is what matters on the recast: Giada dies, comes back for 4, gets shroud and haste for free, and taps for Angel mana the same turn. With Boots the recast turn costs 5.

**Redundancy.** Swiftfoot Boots does the same job at a comparable rate. That is one comparable card, not two, so it passes. The pair is the standard answer for commander-centric decks and the community runs both in Giada: Greaves 41.2% (14,930 of 36,267), Boots 34.2% (12,398).

**Density.** Giada is in the command zone every game. 100%.

**Marginal impact.** Yes. The user's stated loss mode is "Giada is gone". Greaves changes the games where she is removed once and the recast gets removed again, which is the commonest way a 2/2 commander loses a game.

**Cost of entry.** 2-drop colorless for a 2-drop {1}{W}. Curve and pips get slightly easier.

**Anti-synergy — the real cost.** Shroud blocks *our own* targeting. The deck's own-side targeting, verified:

| Card | Clause | Effect with Greaves on Giada |
|---|---|---|
| Clever Concealment | "Any number of target nonland permanents you control phase out" | **Cannot phase Giada out.** Against a wipe you still have Flawless Maneuver and Akroma's Will (neither targets), and Concealment still saves the rest of the board. This is the one interaction worth knowing. |
| Giver of Runes | "Another target creature you control" | Cannot target Giada. Giver is then free to guard Archangel of Thune, Angel of Destiny or Lyra, Archangel of Dawn instead, which is a redistribution, not a loss. |
| Valorous Stance | "Target creature gains indestructible" | Cannot target Giada. Minor. |
| The Wandering Emperor +1 | "Put a +1/+1 counter on up to one target creature" | Cannot target Giada. Minor. |
| Swiftfoot Boots equip | targets | Can't stack Boots on top of Greaves. Irrelevant; put Boots on the next-best Angel. |

Not affected: Sephara's alternative cost (tapping four fliers is a cost, not a target), Cathars' Crusade, Archangel of Thune, Lyra AoD, Metastatic Evangel, Giada's own counters (none target).

Equip {0} means Greaves can also move to a freshly cast Avacyn, Lyra Dawnbringer or Sephara for an immediate attack, and a recast Giada with haste can attack for a Tome of Legends counter and a Choirmaster proliferate that turn. Small bonuses.

**Worst-case draw.** Late topdeck with Giada already wearing Boots: it still gives haste to a new Angel, otherwise dead. Same as Boots' worst case.

**Bracket.** Not a Game Changer. `combos.py --add "Lightning Greaves" --near`: completes 0 combos; the only near-combo is Crackdown Construct, which is not in the deck.

**Disagreement check.** Community says yes at 41.2%. Independent reason: six verified commander-keyed cards, above the usual Giada count.

**Price.** $3.96, fetched 2026-10-05 12:25 UTC. Not part of the verdict.

## The cut: Archivist of Oghma

Its only trigger is "Whenever an **opponent** searches their library." It is entirely opponent-dependent. In a rotating casual pod of 10+ decks, the user reports it rarely fires. When it doesn't fire it is a 2-mana 2/2 with flash whose only in-deck interaction is Righteous Valkyrie ("Whenever another Angel or Cleric you control enters, you gain life equal to that creature's toughness"): 2 life. Folk Hero does not draw off it, because Giada's creature type is Angel.

Card-advantage count goes 8 to 7 (Folk Hero, Dawn of Hope, Tome of Legends, Vanquisher's Banner, Exemplar of Light, Inspiring Overseer, Wojek Investigator) plus Minas Tirith, War Room and Bonders' Enclave. A draw engine that doesn't draw was never really the eighth, so the real count is unchanged. Giada EDHREC: 9.4% (3,418). Low inclusion agrees.

Runners-up, spared:

1. **Heraldic Banner.** 3-mana rock with +1/+0 for white creatures. The shape review called mana "over-supplied" at 9 rocks/reducers plus Giada, and this is the weakest of them. It is the cut if Archivist starts triggering again.
2. **Radiant Fountain.** The shape review named it the next flood cut, but only if goldfishing shows flooding. Cut a spell for a spell.
3. **Valorous Stance.** Already reserved by the 2026-10-02 remaining-budget review as the cut for Teferi's Protection. Don't spend it twice.

Condition to reverse: if the pod's decks start searching often (green ramp, fetchlands, tutors), Archivist is a real engine again, and Heraldic Banner becomes the cut for Greaves instead.

## Counter-proposals checked

Verified and rejected for this slot:

- **Champion's Helm** ($3.03): +2/+2 and hexproof while legendary, equip {1}, 3 mana. The alternative if the Clever Concealment interaction bothers you: hexproof keeps Giver, Concealment, Stance and the Emperor able to target Giada. Costs 1 more to cast, 1 more per equip, no haste, and the hexproof disappears if you move it to a non-legendary Angel. Greaves is better for the recast problem the user described.
- **Mother of Runes** ($12.70, 10.9% in Giada): a second Giver. Same rate (one colour, must untap), dies to the wipes the deck is weakest to, and doesn't fix the recast turn.
- **Darksteel Plate** ($7.04): indestructible doesn't stop Swords to Plowshares or Path to Exile, the removal white decks see most.
- **Whispersilk Cloak** ($2.26), **Mask of Avacyn** ($1.38): equip {2} and {3}. Worse rate than either Boots or Greaves.
- **Loran's Escape** ($1.48), **Blacksmith's Skill** ($0.38): 1-mana instants. Reactive and one-shot; the deck already holds four of those.
- **Commander's Plate** ($40.89): over the cap, and in mono-white it gives no protection from white.
- **Teferi's Protection**: different role (protects you, not Giada); still the open Game Changer #3 question from the ceiling review.

## After the swap

| | Before | After |
|---|---|---|
| Protect (permanent anti-targeting) | 1 (Boots) | **2** (Boots, Greaves) |
| Card advantage | 8 + 3 lands | 7 + 3 lands |
| Equipment | 1 | 2 |
| Game Changers | 2 | 2 |
| Combos | 0 | 0 |
| Clerics for Righteous Valkyrie (other than herself) | Giver of Runes, Angel of Destiny, Archivist | Giver of Runes, Angel of Destiny |

Play note: put Greaves on Giada by default. If you are holding Clever Concealment and expect a wipe, Boots on Giada and Greaves on the biggest Angel is the better split, since Concealment can then phase Giada out.
