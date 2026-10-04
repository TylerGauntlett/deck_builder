# Angels — mass Angel token makers

Date: 2026-10-02 · Deck state: `complete.txt` · Prices: Scryfall, fetched 2026-10-02 15:30 UTC
Search: `card_facts.py search 'id<=w o:"angel creature token" f:commander'` → 29 results. The deck already runs Court of Grace, Resplendent Angel, Valkyrie Harbinger and Serra the Benevolent.

## Why mass Angels multiply in this deck

Each Angel token entering separately triggers:
- **Giada**: counters equal to the Angels you already control. Ruling 2024-11-08: "each Angel you control other than the Angel entering". Tokens entering together don't count each other.
- **Bishop of Wings**: 4 life per Angel. Each gain triggers **Archangel of Thune** (counter on every creature), **Lyra, Archangel of Dawn** (counter on every Angel) and **Dawn of Hope** (pay {2}: draw).
- **Righteous Valkyrie**: life equal to the token's toughness.
- **Cathars' Crusade**: a counter on every creature, per token.
- **Dazzling Angel**: 1 life per creature.

**Not triggered:** Metastatic Evangel (nontoken only) and Folk Hero (spells cast, not tokens).

So X Angels at once means about X Crusade triggers plus 2X–3X lifegain triggers. The payoff is real; the question is cost and whether the card works from an empty board.

## ADD — Ob Nixilis, the Ascended, cut Sunblast Angel ($2.48)

`{5}{W}{W}` Legendary **Angel**, 4/4 flier:
- "When Ob Nixilis enters, destroy all tapped creatures **your opponents control**. You gain 1 life for each creature destroyed this way."
- "At the beginning of **each** end step, if you gained life this turn, create a 4/4 white Angel creature token with flying."

**Same-role upgrade.** Sunblast Angel's ETB is "destroy all tapped creatures", which hits your own creatures too (ruling: "including creatures you control"). Ob Nixilis has the one-sided version, and the life it gains triggers Thune and Lyra AoD.

**Engine.** "Each end step" means all four players' turns. The deck gains life on opponents' turns through Archivist of Oghma, Seraph Sanctuary, the Wandering Emperor's −2 and lifelink blockers. On its own turn it gains life almost every time. That is an Angel every turn, sometimes several per round, and each one runs the cascade above. Ruling 2026-08-21: it triggers even if you also lost life that turn.

It is an Angel, so Incubator, Horn, Aspirant and Giada mana all reduce its cost; Sunblast also got those. Giada EDHREC: 22.7% (675 of 2,977 decks, from the new-cards list). Combos: none.

## ADD IF — Entreat the Angels ($0.41)

`{X}{X}{W}{W}{W}`: X 4/4 Angels. Miracle `{X}{W}{W}`. It is the best **rebuild-from-nothing** finisher here: it works on an empty board after a wipe. The miracle can fire on opponents' turns when Archivist of Oghma or Dawn of Hope gives you your first draw of that turn. Hard-cast it is expensive: X=3 costs 9. Giada EDHREC 27.4% (9,867 decks).

**Condition:** add it if games often go to a wipe and you lose the rebuild race. Cut Serra Avenger. Otherwise the deck has enough finishers (Akroma's Will, Avacyn, Elesh Norn, Sephara, and the counter engines).

## NO

| Card | Reason |
|---|---|
| Devout Invocation ($2.17) | 7 mana for an Angel per creature you tap. Explosive after attacking with vigilant creatures, but it needs a board to do anything, so it is win-more. Dead after a wipe, which is when you'd want mass tokens. |
| Divine Visitation ($0.49) | Turns tokens into 4/4 Angels. Only about 6 token sources would upgrade (Court of Grace Spirits, Bishop Spirits, Castle Ardenvale, Angel of Invention Servos, Emperor Samurai, Dawn of Hope Soldiers). A 5-mana non-Angel enchantment that does nothing alone. |
| Decree of Justice ($0.24) | Hard-cast X=2 costs 8 for two Angels. The instant-speed cycling mode makes 1/1 Soldiers, not Angels. |
| Finale of Glory ($2.25) | Angels only at X≥10, which costs 12 mana. |
| Elspeth Resplendent | −7 for five Angels takes 3+ turns of protecting her. |
| Parhelion II | 8 mana plus crew 4. |
| Battle at the Helvault ($5.57) | 6-mana saga. The Avacyn token arrives two turns later. |
| Sigil of the Empty Throne, Historian's Boon | Need enchantment or Saga density the deck doesn't have. |
| Empyrial Storm | Copies per commander recast. Giada is cheap and rarely recast many times. |
| Luminarch Ascension, Angelic Accord, Book of Exalted Deeds | Rejected in the build-out review. Same reasons. |

## Totals

Buy list: 30 cards, ~$255.10. `complete.txt` 100 cards. Game Changers 2. Combos 0.
