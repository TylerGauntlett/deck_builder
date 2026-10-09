# Darksteel Angel (2026-10-09)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards).
Prices: Scryfall, fetched 2026-10-09 06:03–06:05 UTC. EDHREC: Giada commander page, 36,794 decks; Darksteel Angel card page.
Scripts read `base.txt`, so EDHREC and Spellbook were run against a temporary copy of `complete.txt` (deleted afterwards). All 73 non-basic cards in `complete.txt` were fetched live this session.

## Verdict

| Card | Verdict |
|---|---|
| Darksteel Angel | **NO.** A nine-mana body that stops you losing but does not advance a win, in a deck that already cut the same effect at seven mana (Herald of Eternal Dawn) and the same mana value (Reya Dawnbringer). The cut it would force is Angel of the Ruins, which is the better card in this deck on every axis but one. |

Nothing applied. `complete.txt`, `adds.txt` and `base.txt` are unchanged.

## Facts (all verified this session)

**Darksteel Angel** {9}, Artifact Creature — Angel, 4/4. "Flying, indestructible. You can't lose the game and your opponents can't win the game. Creatures you control can't have -1/-1 counters put on them." Colour identity colourless, legal in mono-white, **not** a Game Changer. EDHREC rank 9513. **$4.11.**

Rulings (2026-08-21): no game effect can make you lose while you control it, including 0 life, drawing from an empty library, or ten poison counters; you keep playing. Conceding still works. Draw-the-game effects are unaffected.

**Giada, Font of Hope** {1}{W}. "Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control. {T}: Add {W}. Spend this mana only to cast an Angel spell."

Cost reducers in the deck, checked against Darksteel Angel's cost:

| Card | Clause | Applies? |
|---|---|---|
| Urza's Incubator | "Creature spells of the chosen type cost {2} less" | yes, −2 |
| Starnheim Aspirant | "Angel spells you cast cost {2} less" | yes, −2 |
| Herald's Horn | "Creature spells you cast of the chosen type cost {1} less" | yes, −1 |
| Pearl Medallion | "**White** spells you cast cost {1} less" | **no**, the card is colourless |
| Giada's mana | "Spend this mana only to cast an Angel spell" | yes, pays {1} of it |

Floor with all three applicable reducers on the battlefield: **{4}**. With one of them: {7} or {8}. Every other top-end Angel in the deck is white and also gets the Medallion.

**Herald of Eternal Dawn** {4}{W}{W}{W}, Angel 6/6. "Flash. Flying. You can't lose the game and your opponents can't win the game." $1.57. In the precon, cut in the 2026-10-02 build-out review for Akroma's Will with the reason: "a 7-mana 'can't lose' body that does not advance a win." The same review cut Reya Dawnbringer with "Reya costs 9 and does nothing on the turn it lands," and recorded "the 9-drop and one 7-drop are gone" as a gain.

**Platinum Angel** {7}, Artifact Creature — Angel 4/4. "Flying. You can't lose the game and your opponents can't win the game." $10.51. Not in the deck. Same clause, two mana cheaper, not indestructible.

## The honest best case

It is an Angel, so Giada's counters, the three Angel discounts, Giada's mana, Vanquisher's Banner ("Whenever you cast a creature spell of the chosen type, draw a card"), Folk Hero ("shares a creature type"), Bishop of Wings (+4 life), Righteous Valkyrie (life equal to toughness) and Cathars' Crusade all trigger on it. On a board of five Angels it enters as a 9/9 flying indestructible, and from then on no combat step, drain, poison or alternate win can end your game. Indestructible means Wrath-type wipes and Elesh Norn's −2/−2 leave it standing, so it is only answered by exile, bounce, edicts or −X/−X mass effects. With Lightning Greaves ("shroud") or Giver of Runes ("protection from the colour of your choice") on it, the common white exile spells can't touch it either. The deck already sits at 50–70 life behind Ghostly Prison, Magus of the Moat and Archangel of Tithes, so the one way it dies is a combo or an overwhelming board, and this is a flat answer to both.

That case is real. It is also the case for Herald of Eternal Dawn, which the deck already rejected.

## What killed it

**1. The deck has already decided this role is not worth a top-end slot, and nothing has changed since.** Herald of Eternal Dawn is the same clause at seven mana, with flash (it can be cast in response to the lethal attack or the combo) and a 6/6 body, and it was cut on 2026-10-02 because a "can't lose" body does not advance a win. Darksteel Angel trades flash and two points of body for indestructible and costs two more. The build-out and Bruna reviews both treated the 7-plus top end as full: six cards at mana value 7–8 (Sephara, Angel of the Ruins, Elesh Norn, Ob Nixilis, Emeria's Call, Avacyn). Bruna was rejected at seven mana for that reason. A nine is not a different question.

**2. Rate.** Pearl Medallion does not reduce it, so it is the only Angel in the list that gets three discounts instead of four. Realistically it is a seven- or eight-mana spell on the turn it matters, in a deck whose average non-land mana value is about 3.5 and whose own shape review called the mana "over-supplied" for that curve. Raising the top end does not use that surplus; it adds hands with two uncastable cards.

**3. Marginal impact — which lost games does it change?** The table reports on file say the deck's losses come from Giada being removed and the board turning into "small/medium flyers" (2026-10-05). Darksteel Angel without Giada enters with no counters, gets no Giada mana, and is a nine-mana 4/4. It does nothing for the games this deck actually loses. In the games it would change, where you are about to lose to a lethal swing or a combo on turn nine-plus, it keeps you in the game but does not rebuild the board; the win still has to come from the same Angels it was failing to protect. That is Herald's problem again.

**4. The second clause is blank here.** "Creatures you control can't have -1/-1 counters put on them" is relevant against infect, wither and persist decks. None of the deck's own cards use −1/−1 counters, so it is pure pod-specific upside against an unknown rotation.

**5. Anti-synergy.** Farewell ("Exile all artifacts") removes it; indestructible does not stop exile. Minor, and shared with Angel of the Ruins and the rocks, but it is one more artifact under the deck's own best wipe.

**Tests it passed:** legal, colourless identity, under budget, not a Game Changer, no early or tutor-dependent infinite. `combos.py --add`: 0 combos completed; one near-miss (Transcendence, not in the deck and not in colour). No legend-rule conflict.

**Disagreement check.** Giada EDHREC: 3.3% (276 of 8,490 decks on the card's page; the card is new). Kaalia, the commander most often running it, 7.9%. The community agrees with the no, and the reason this deck is not an exception is the one above: it already has the lifegain and pillowfort that make the effect unneeded, and it already cut the cheaper version.

## The cut it would force

Prefer cutting within the role: another indestructible or top-end Angel.

| Rank | Cut candidate | Why spared |
|---|---|---|
| 1 | Angel of the Ruins | The only genuine candidate, and still a loss. {5}{W}{W} 5/7 flyer; "exile up to two target artifacts and/or enchantments"; Plainscycling {2}. It gets all four discounts. It is never dead in an opening hand (cycles for a Plains), it is interaction against unknown decks (Rhystic Study, Smothering Tithe, stax pieces), and the Bruna review already named it the swap slot *if games run long and Angels pile up in the graveyard*. Darksteel beats it on exactly one axis: the turn you would otherwise lose. |
| 2 | Avacyn, Angel of Hope | The nearest role match (eight-mana indestructible Angel). Avacyn protects the board, which is the deck's recorded loss mode; Darksteel protects only the life total. Avacyn stays. |
| 3 | Ob Nixilis, the Ascended | One-sided wipe on entry plus a 4/4 Angel each end step the deck gains life, which it does most turns. Stays. |
| 4 | Magus of the Moat | Overlaps most with Darksteel on *outcome* (stops the pod's ground wins) at four mana, and it also keeps attackers off Giada. Darksteel does not protect Giada. Stays. |
| 5 | Thraben Watcher | Weakest static anthem, but swapping a four-drop for a nine-drop is a cross-role cut that worsens the curve. Stays. |

Rank 1 is a card I would defend in any other context. Per the rubric, that is the finding: the addition is not worth its slot.

## Price

$4.11, fetched 2026-10-09 06:03 UTC. Price was not a factor. The rejection survives the card being free.

## Counter-proposal

The role, "I can't lose while this is out," is not a gap in this deck as it stands: it sits at 50–70 life behind three pillowfort pieces, and the losses on record are Giada removal and wipes, which Giver of Runes, Lightning Greaves, Swiftfoot Boots, Flawless Maneuver, Clever Concealment, Avacyn and Sephara already cover. No counter-proposal.

For the record, the cheaper cards with the same clause (Scryfall search `o:"can't lose the game" ci:w f:commander`, 9 matches, prices fetched 06:05 UTC): Platinum Angel $10.51 (7 mana, Angel, not indestructible), Herald of Eternal Dawn $1.57 (7 mana, flash, already cut), Angel's Grace $3.33 (one turn), Gideon of the Trials $1.53 (needs a Gideon planeswalker on board). If the role ever becomes real, Herald of Eternal Dawn is the one to revisit, not Darksteel: it is cheaper, white, flashes in on the lethal turn, and the reason it was cut applies to all of them equally.

## What would reopen this

The verdict rests partly on the deck's speed and on where its losses come from. If the table reports change to the following, re-run the review:

- Games regularly go past turn nine **and** the losses are to opponents' combos or one-shot lethal swings rather than to Giada removal or wipes.

In that case the swap is Darksteel Angel for Angel of the Ruins, and the comparison to make first is against Herald of Eternal Dawn.
