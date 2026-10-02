# Angels — proliferate options

Date: 2026-10-02 · Deck state: `complete.txt` · Prices: Scryfall, fetched 2026-10-02 15:18 UTC
Search: `card_facts.py search 'id<=w o:proliferate f:commander'` → 20 results (Norn's Choirmaster already in).

## Framing: proliferate's rate against what the deck already has

Proliferate gives +1 counter to each permanent that already has one. Here that is almost every creature, through Giada, Cathars' Crusade, Archangel of Thune and Lyra, Archangel of Dawn. It also adds loyalty to Serra the Benevolent and page counters to Tome of Legends, and triggers Exemplar of Light's draw once a turn.

The deck already has three engines that put a counter on each creature **every time** they trigger (Crusade per creature entering, Thune per lifegain, Lyra AoD per lifegain, Angels only). One proliferate is therefore worth about **one extra trigger** of an engine the deck already has. **One-shot proliferate is additive and loses.** Only cheap, repeating proliferate is worth a slot.

## ADD — Metastatic Evangel, cut Metallic Mimic ($0.37)

`{1}{W}` 3/1 Phyrexian Human **Cleric**: "Whenever another nontoken creature you control enters, proliferate."

- Repeating and cheap: a 2-mana second Cathars' Crusade that triggers on the deck's **31 nontoken creatures** (25 of them Angels), including reanimations from Emeria, the Sky Ruin. Tokens don't trigger it.
- Scope check: "nontoken creature **you control**". It triggers on your casts and reanimations, not on tokens, and grows every creature that already has a counter (nearly all of them).
- As a Cleric it triggers Righteous Valkyrie's lifegain (toughness 1), which feeds Thune and Lyra AoD.
- **Same-role cut.** Metallic Mimic also costs 2 and gives **one** extra counter to **the creature entering**. Evangel gives one extra counter to **every** creature with counters on the same event.
- Weakness: a 3/1 body that dies to anything. It can't attack under Magus of the Moat, but its job isn't attacking.
- EDHREC: not on Giada's lists (under ~5%). The difference is that this build stacks Crusade, Thune and Lyra AoD, which most Giada lists don't.

## ADD IF — Patrolling Peacemaker, cut Serra Avenger ($0.78)

`{2}{W}` Robot Soldier, enters with two +1/+1 counters: "Whenever an opponent commits a crime, proliferate."

Scope check (ruling 2025-07-25): a crime is any spell or ability **targeting an opponent of that player**, or their permanents, spells or graveyard. In a 4-player game that includes opponents targeting **each other**, not just you. The trigger happens on cast, before the spell resolves. It does not depend on your own draws, so it keeps proliferating when your hand is empty.

**Condition:** add it if your pod casts a lot of targeted removal, burn and targeted abilities. This pod's wins come mostly from ground attacks, and attacking is not a crime, so the trigger rate is uncertain. Serra Avenger is the cut: a 2-mana 3/3 flying Angel with no text that matters past turn 4.

## NO

| Card | Reason |
|---|---|
| Karn's Bastion ($2.27) | Colourless land. The deck already has 6 colourless lands against WW/WWW costs (Avacyn, Archangel of Tithes, Sephara, Magus). {4},{T} proliferate is a mana sink for turns when nothing else is worth casting. |
| Sword of Truth and Justice ($33.45) | Once per combat, and costs half the remaining budget. Protection from **white** on your own creature means your targeted white spells (Clever Concealment, Valorous Stance) can't save it. Akroma's Will and Flawless Maneuver don't target and still work. Evangel does more for $0.37. |
| Contagion Engine ($14.26) | 6 mana. The ETB −1/−1 on one opponent's board is real, but proliferate twice for {4} a turn is a late mana sink. |
| Grateful Apparition | 1/1 flier that needs to connect, once per turn. |
| Proud Pack-Rhino, Unbounded Potential, Glistening Sphere, Wanderer's Strike | One-shot proliferate. Additive, per the framing above. |
| Throne of Geth, Filigree Vector, Surge Conductor | Need artifacts entering or to sacrifice. The deck has few non-mana artifacts to spare. |
| Staff of Compleation | Pay 3 life per proliferate, once a turn unless you pay {5}. Life is a resource this deck converts into board (Resplendent and Harbinger thresholds). |
| Core Prowler | Infect, a death trigger, no synergy. |

Combo check: `combos.py --add` Evangel, Peacemaker and Karn's Bastion: none completes a combo.

Applied to `complete.txt` / `adds.txt`: Metastatic Evangel for Metallic Mimic. Peacemaker is listed as optional.
