# Weakness audit — lander_commander (Aesi, Tyrant of Gyre Strait)

Bracket 3, 4-player casual, $40/card budget cap.
All oracle text, prices and legality fetched **2026-09-01 01:47–02:21 UTC** via
`card_facts.py lookup`. EDHREC figures from the Aesi commander page (16,889 decks),
Landfall theme (1,255) and Lands Matter theme (1,751).

## Pod calibration (asked, not assumed)

- Games run **turns 9–12**.
- Threats: **combo/spell-based kills**, **go-wide creature combat**, plus **mill**
  and **aristocrats**.

This is the premise everything below is graded against. It moves interaction ahead
of engine-tuning, and it makes the graveyard a live axis the deck ignores entirely.

## Bracket check (unchanged, re-verified)

`combos.py` still reports 10 assembled combos, including two-card Springheart
Nantuko + Lotus Cobra / Tireless Provisioner lines. Re-grepped all 76 distinct cards
for land-animation and repeatable land-untap text: the only hit is **Fabled Passage**
("untap that land"), a one-shot on its own fetch, not a repeatable untapper. The
two-card lines are **not** assembled. Bracket 3 holds. Game Changers 2/3.

## Measured weaknesses (script output, not recall)

| # | Category | Count in the 99 | Cards |
|---|---|---|---|
| 1 | Instant-speed answers | **6** | Counterspell, Negate, Arcane Denial, Beast Within, Pongify, Cyclonic Rift |
| 2 | Instant-speed artifact/enchantment removal | **0** | (only Acidic Slime MV5, Reclamation Sage MV3, Terastodon MV8 — all sorcery-speed creature ETBs) |
| 3 | Mass answers / sweepers | **0** | none. Propaganda taxes, it does not reset |
| 4 | Graveyard interaction | **0** | none |
| 5 | Exile-based creature removal | **0** | Pongify and Beast Within both *destroy* — death triggers fire |
| 6 | Nonland recursion | **1** | Call Damage Control (EDHREC rank 13882) |
| 7 | Nonland tutors | **1** | Finale of Devastation |
| 8 | Commander protection | **2** | Heroic Intervention, Swiftfoot Boots |
| 9 | Cards that put lands **in hand** | **4** | Coiling Oracle, Cultivate, Kodama's Reach, Yavimaya Elder — against 6 extra-land-drop effects |
| 10 | Curve | MV4 = **2**, MV6+ = **12** | MV4 is only Arixmethes + Oracle of Mul Daya |

Mana base is **not** a weakness: 21 blue-producing lands, 23 green, plus 7 fetches
and Dryad of the Ilysian Grove, against G59/U21 pips. Leave it alone.

Landfall/ramp is **over**-served, not under-served: 11 landfall payoffs, 7 of which
make tokens. EDHREC confirms — the deck runs 9/10 high-synergy cards on the commander
page and 10/10 on Lands Matter. There is nothing left to gain in the deck's strong lane.

## The seven swaps

Every add: legal in GU, `combos.py --add` returns **0 new combos**, not a Game Changer.

| Add | Price | Cut | Reason |
|---|---|---|---|
| Krosan Grip {2}{G} | $1.69 | Herd Heirloom | First instant-speed artifact/enchantment answer. Split second beats a combo player holding protection — the specific failure mode of this pod. |
| Reality Shift {1}{U} | $0.30 | Goldvein Hydra | **Exiles.** Against aristocrats, Pongify and Beast Within *feed* the drain; this doesn't. Hydra has no landfall, no ETB, no land text. |
| An Offer You Can't Refuse {U} | $3.38 | Negate | Identical scope one mana cheaper — you can hold it up *and* cast Aesi. Cost: two Treasures to a combo player. |
| Scavenging Ooze {1}{G} | $0.27 | Zendikar's Roil | Deck's only graveyard interaction. Targeted, so it never eats your own lands (Ramunap Excavator, Ancient Greenwarden, Finale all stay live). Roil is the 7th token-landfall payoff and makes the smallest bodies. |
| Aetherize {3}{U} | $0.57 | Ghalta, Primal Hunger | Only mass answer in the list. **Not Evacuation** — that bounces your own Avenger plants, Baloths beasts, Scute copies, Roil elementals, Greensleeves badgers and Springheart insects; Aetherize hits attackers only, so it is one-sided while you defend. Ghalta is the third redundant finisher behind Craterhoof and Overwhelming Stampede. |
| Eternal Witness {1}{G}{G} | $2.55 | Call Damage Control | 44.3% of Aesi decks (7475/16889). Body means Finale of Devastation can *fetch* it; CDC is uncastable value at rank 13882. Rebuy matters more against mill and attrition. |
| Splendid Reclamation {3}{G} | $0.40 | Jin-Gitaxias, Progress Tyrant | Turns the pod's mill into your engine: opponents fill your yard with lands, you return **all** of them at once for a pile of landfall triggers, doubled by Ancient Greenwarden. 10 of your own lands already self-sacrifice into the yard. Fills the MV4 hole; Jin-Gitaxias is MV7 {5}{U}{U} with zero land synergy. |

Total: **$9.16**, all under the $40 cap.

### Aggregate delta
- Instant-speed answers **6 → 9**, and 3 of the new ones cover categories that were at zero.
- Nonland recursion 1 → 1 (upgraded), tutors 1 → 1.
- MV4 **2 → 4**; MV6+ **12 → 10** — correct direction for turn 9–12 games.
- Pips G 59 → 57, U 21 → 21. Creatures 29 → 28. **No mana base change needed.**
- Game Changers 2 → 2.

## There is no eighth cut

Explore ($0.20, 60.9% of Landfall decks, synergy +0.41) is the best remaining add —
it feeds the six extra-land-drop effects that card 9 above shows are under-fuelled.
I am not recommending it, because the best cut left is **Greensleeves, Maro-Sorcerer**
or **Ghost Quarter**, and I would defend both in any other list. Greensleeves is a
lands-sized body plus a 3/3-per-landfall engine; Ghost Quarter is one of two answers
to a problem land. That is the finding: the list is tight enough that seven swaps is
the honest ceiling.

## Rejected, with reasons

- **Fierce Guardianship** — $57.52, over the $40/card cap. Constraint veto, not a
  judgment call. It would otherwise be the correct use of the open 3rd Game Changer
  slot: free interaction while tapped out is exactly this deck's tension.
- **Evacuation** ($0.32) — symmetric; kills your own tokens from 6 producers.
- **Whelming Wave** ($2.32) — spares Serpents/Krakens (Aesi, Koma, Arixmethes) but
  still bounces your token board out of existence.
- **Grafdigger's Cage** ($2.13) — shuts off Finale of Devastation's graveyard mode.
- **Icetill Explorer** ($20.09) — recommended in the 2026-08-31 review and passed
  over. Still good, still MV4, still self-fuelling. Ranked behind all seven above
  because it improves the lane the deck is already deepest in.
- **Nature's Claim** ($1.52) — lost to Krosan Grip on split second, given combo
  opponents. Take it instead if you want the 1-mana rate.
- **Swan Song** ($11.15) — misses artifacts and creatures; Offer is broader and cheaper.
- **Veil of Summer** ($4.25), **Mystic Confluence** ($1.07), **Rapid Hybridization**
  ($1.03), **Kenrith's Transformation** ($1.06), **Lightning Greaves** ($4.86),
  **Tyvar's Stand** ($1.14), **River's Rebuke** ($0.29), **Ezuri's Predation** ($2.64),
  **Harrow** ($0.28), **Nature's Lore** ($2.69), **Life from the Loam** ($5.23) — all
  legal, none beat a named card above for a named slot.

## Flagged, not an add

**You can deck yourself.** Aesi draws on every land, with 44 lands, 6 extra-land-drop
effects, and a mill deck in the pod. Reliquary Tower, Thought Vessel and Nezahal
handle *hand* size; nothing in the 99 handles *library* size. If you actually lose a
game this way, the one-card fix is **Gaea's Blessing** ({1}{G}, $0.29 — shuffles your
graveyard back in when it is milled). EDHREC rank 5457, so this is a pod-specific
call, not a general one. Don't pre-emptively slot it.
