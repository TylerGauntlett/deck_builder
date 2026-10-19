# Herald of Eternal Dawn back in, for Heraldic Banner (2026-10-14)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards), the current working list, not the precon `base.txt`.
Prices: Scryfall, fetched 2026-10-14 09:18–09:21 UTC. EDHREC: Giada commander page, 37,383 decks; Herald card page, 37,200 Giada decks.

## The question

Herald of Eternal Dawn came in the Calling All Angels precon and was cut on 2026-10-02 (build-out review, row 7) as the one-for-one slot for Akroma's Will, with the reason "a 7-mana 'can't lose' body that does not advance a win." The user asks whether it belongs in the current list. That is a different question from the one answered then: Akroma's Will is still better than Herald and stays. The question now is whether Herald beats the worst card that survives in `complete.txt`.

## Verdict

| Card | Verdict |
|---|---|
| Herald of Eternal Dawn | **ADD, cut Heraldic Banner.** |

Applied to `complete.txt` and `removal.txt`. `base.txt` is unchanged (Herald is a precon card, so `adds.txt` is unchanged too). `moxfield.txt` is the user's export and is untouched.

## Facts (all verified this session)

**Herald of Eternal Dawn** {4}{W}{W}{W}, Creature — Angel, 6/6. "Flash. Flying. You can't lose the game and your opponents can't win the game." Legal, mono-white, **not a Game Changer**. $1.74 (FDN). EDHREC rank 4014. Rulings 2024-11-08: no game effect can make you lose or an opponent win while you control it, including 0 or less life, drawing from an empty library, ten poison, Maze's End. You still can't pay more life than you have.

**Heraldic Banner** {3}, Artifact. "As this artifact enters, choose a color. Creatures you control of the chosen color get +1/+0. {T}: Add one mana of the chosen color." $0.34.

Cards cited below, with the clause the argument rests on:

| Card | Clause |
|---|---|
| Giada, Font of Hope | "Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control. {T}: Add {W}. Spend this mana only to cast an Angel spell." |
| Starnheim Aspirant | "Angel spells you cast cost {2} less to cast." |
| Urza's Incubator | "Creature spells of the chosen type cost {2} less to cast." |
| Herald's Horn | "Creature spells you cast of the chosen type cost {1} less to cast." |
| Pearl Medallion | "White spells you cast cost {1} less to cast." |
| Bishop of Wings | "Whenever an Angel **you control** enters, you gain 4 life." |
| Righteous Valkyrie | "Whenever another Angel or Cleric **you control** enters, you gain life equal to that creature's toughness." |
| Resplendent Angel | "At the beginning of **each** end step, if you gained 5 or more life this turn, create a 4/4 white Angel creature token with flying and vigilance." |
| Valkyrie Harbinger | "At the beginning of **each** end step, if you gained 4 or more life this turn, create a 4/4 … Angel …" |
| Ob Nixilis, the Ascended | "At the beginning of **each** end step, if you gained life this turn, create a 4/4 white Angel creature token with flying." |
| Folk Hero | commander gains "Whenever you cast a spell that shares a creature type with this creature, draw a card. This ability triggers only once each turn." |
| Lyra Dawnbringer | "Other Angels you control get +1/+1 and have lifelink." |
| Sephara, Sky's Blade | "You may pay {W} and tap four untapped creatures you control with flying rather than pay this spell's mana cost. … Other creatures you control with flying have indestructible." |
| Magus of the Moat | "Creatures without flying can't attack." |
| Serra the Benevolent −6 | emblem: "If you control a creature, damage that would reduce your life total to less than 1 reduces it to 1 instead." |
| The Wandering Emperor | "Flash" (the list's only other flash card; it is a planeswalker) |

## The deck as it stands (counts from `cards.json` built from `complete.txt`)

- 62 nonland, 38 lands (27 Plains, 4 lands that don't make W: Radiant Fountain, Bonders' Enclave, Seraph Sanctuary, War Room; Three Tree City makes {C} natively). Average nonland MV **3.50**.
- Curve: 1: 4 · 2: 16 · 3: 16 · 4: 11 · 5: 7 · 6: 3 · 7: 4 · 8: 1.
- MV 6+ (8): Farewell, Austere Command, Valkyrie Harbinger, Sephara, Elesh Norn, Ob Nixilis, Angel of the Ruins, Avacyn.
- Triple-W costs (3): Sephara, Avacyn, Archangel of Tithes.
- Angels: **24** including Giada. Angel cost reducers: 4 (Aspirant, Incubator, Horn, Medallion) plus Giada's mana.
- Mana rocks and reducers: **9** (Sol Ring, Arcane Signet, Mind Stone, Heraldic Banner, Patchwork Banner, Pearl Medallion, Urza's Incubator, Herald's Horn, Starnheim Aspirant) plus Giada and Three Tree City. The 2026-10-02 shape review called this "over-supplied".
- Cards with lifegain or lifelink text: **21**.
- Flash creatures: **0**. Flash anything: 1 (The Wandering Emperor).
- Cards that stop *you* losing: **0**. Nearest: Serra's −6 emblem (two turns to reach, damage only), Magus of the Moat (stops ground attacks only, 0/3 body).
- Loss modes on record: Giada removed → "a bunch of small/medium flyers" (2026-10-05); wipes (2026-10-02); and from `meta.json`, "the majority of wins [in the pod] come through ground (non-flying) attacks" (user report 2026-10-02). Opponents rotate 10+ decks, so combo and alt-win losses are possible and unmodelled.

## Herald through the rubric

**Best case, as a falsifiable claim.** Herald is the list's only "you can't lose" effect and its only flash creature, in a deck whose main reported loss mode is a ground alpha strike and whose 21 lifegain cards can turn a bought turn cycle into a positive life total again. It is also an Angel, so it costs {W}{W}{W} with Aspirant and Incubator out, enters with Giada's counters, and triggers Bishop, Righteous Valkyrie, Folk Hero and the three "each end step" token makers.

**Redundancy (effect × frequency × duration).** Zero cards in the list do this job. The comparisons people reach for are different cards:
- Teferi's Protection (not in the deck; the open Game Changer #3 question since the ceiling review): one turn, instant, exiled after, also phases out your board. $45.36 today at the default print, and a Game Changer.
- Angel's Grace ($3.52) and Everybody Lives! ($16.85): one turn each. One-shot answers, not a permanent.
- Magus of the Moat: permanently stops one attack mode. It does nothing against fliers, drain, combo or alt-wins. Complementary, not redundant.
- Serra's emblem: needs Serra to survive two turns, and only caps damage.

Passes.

**Density.** Needs nothing to function. The Angel package it plugs into is 24 Angels, 4 reducers, Giada's mana, Bishop, Righteous Valkyrie, Folk Hero, Cathars' Crusade, Metastatic Evangel, Youthful Valkyrie, Vanquisher's Banner. Well over a third of the deck interacts with "an Angel spell is cast and enters".

**Marginal impact: does it change games you lose?** Yes, two of the four loss modes:
- *Ground alpha strike.* Flash makes it an ambush 6/6-plus blocker on one attacker and a guarantee that the rest don't kill you. That is the pod's majority win mode by the user's own report.
- *Combo / drain / alt-win from an unknown deck.* The ruling list is explicit: poison, empty library, 0 life, Maze's End. "Your opponents can't win" also blanks Approach, Thassa's Oracle and the like.
It does not help the other two: Giada being removed, or a wipe (though flash lets you deploy it *after* a sorcery-speed wipe resolves, on the end step, rather than into it).

The reason this isn't just Platinum Angel's usual "they kill it and you die" is the lifegain density. One Angel entering with Bishop and Righteous Valkyrie out is 4 life plus toughness; an attack with Lyra Dawnbringer out is lifelink across the Angel board. Going from below 0 back to double digits in one turn cycle is realistic here in a way it isn't in most decks. **Play it to stay positive, not as a licence to go negative:** at 0 or less life every removal spell is lethal.

**The 2026-10-02 objection, "does not advance a win," revisited.** As a one-for-one against Akroma's Will it was right and still is. On its own it understates the body: a 6/6 flier that enters with one counter per Angel you already control (three Angels out → 9/9), gets +1/+1 and lifelink from Lyra Dawnbringer, counts toward Sephara's four fliers and gets indestructible from her. That is a finisher-sized attacker, not a wall.

**The flash line that is specific to this deck.** Resplendent Angel, Valkyrie Harbinger and Ob Nixilis all trigger on *each* end step. Flash Herald in on an opponent's turn with Bishop out: 4 life (plus Righteous Valkyrie's 6+, Dazzling Angel, Seraph Sanctuary, Angel of Vitality's +1 if present) → a 4/4 Angel token on *their* end step, Thune and Lyra AoD counters on everything, Exemplar and Dawn of Hope draws, and Folk Hero's once-per-turn draw on a turn you otherwise wouldn't use it. Then you untap. Three verified cards each side of that line.

**Cost of entry.** 7-drops go 4 → 5, MV 6+ goes 8 → 9 of 62, average MV 3.50 → about 3.56 if the cut is a 3-drop. Triple-W costs go 3 → 4; with 34 W-producing lands and three W-producing rocks that is fine in mono-white. In practice Herald is the cheapest of the top end to cast: all four reducers and Giada's mana apply to it; Elesh Norn, Ob Nixilis and Emeria's Call only get Pearl Medallion. The Bruna review's objection ("the top end is already six cards at 7–8") is addressed below under the cut.

**Anti-synergy.** None found. Magus of the Moat: Herald flies. Emeria, Shattered Skyclave's 3-life payment: trivial. Drannith, Ghostly Prison, Tithes: unaffected. Angel of Destiny's alt-win makes opponents lose, which Herald doesn't touch.

**Worst-case draw.** Opening hand against the fastest deck: dead until about turn 5 with one reducer, same as Sephara, Avacyn, Elesh Norn and Ob Nixilis, and unlike Angel of the Ruins, which can plainscycle. Turn-twelve topdeck on an empty board: a flash 6/6 that says you don't lose this turn, which is one of the best topdecks the deck has in that spot. Fine at the late end, weak at the early end, and the deck already carries five cards with that profile.

**Bracket.** Not a Game Changer. `combos.py --add "Herald of Eternal Dawn" --near` on the current 100: completes 0 combos; the only near-combo is Transcendence (draw the game), which is not in the deck and not wanted.

**Disagreement check.** 28.5% of Giada decks (10,606 of 37,200). Part of that is the precon printing. The independent reasons it's right *here*: the pod's reported ground-attack loss mode, the 21-card lifegain base that converts bought turns into life, and the "protect you" gap the ceiling review left open for a Game Changer slot. Herald fills that gap on a permanent, for no Game Changer.

**Price.** $1.74, fetched 2026-10-14 09:18 UTC, and the user already owns the precon copy. Price played no part. The verdict stands if the card cost $20.

## The cut: Heraldic Banner

The deck's own reviews have named it the weakest surviving card twice: the shape review called mana "over-supplied" at 9 rocks/reducers plus Giada at average MV 3.5, and the Lightning Greaves review called Banner "the weakest of them" and "the cut if Archivist starts triggering again." Archivist has since left, and no card has claimed Banner's slot.

What it does here: a 3-mana rock in a mono-white deck that has no fixing problem, plus +1/+0 for white creatures, in the static-anthem layer the shape review wanted to thin (Patchwork Banner, Vanquisher's Banner, Thraben Watcher, Lyra Dawnbringer, Angel of Invention, Angelic Field Marshal and Elesh Norn all give +1/+1 or better). It is additive in a category the deck is deep in; Herald adds a category the deck has zero of.

After the cut the mana base is 38 lands, 8 rocks/reducers, Giada and Three Tree City for a 62-spell deck at about MV 3.56. That still supports the curve, and it is the direction the shape review pointed. The rubric's "never cut the ramp the curve needs" is not triggered; the shape review's "↓ one" was.

Runners-up, spared:

1. **Angel of the Ruins.** The like-for-like 7-drop swap, and the route the Bruna review preferred for top-end adds. Spared because its plainscycling covers exactly the bad early draw Herald adds, and it is one of six artifact/enchantment answers (Generous Gift, Get Lost, Grasp of Fate, Farewell, Austere Command, Ruins). If you would rather hold the top end at six cards than thin the mana, this is the cut instead, and it is close.
2. **Radiant Fountain.** The shape review's flood cut, "only if goldfishing shows flooding," and the rubric says cut a spell for a spell.
3. **Valorous Stance.** Reserved since the remaining-budget review as the cut for Teferi's Protection. Not spent twice.
4. **Fateful Absence.** Reserved by the Banishing Light review as the cut for Darksteel Mutation, if that swap is ever made.

## Alternatives in the same role, checked and not chosen

- **Angel of the Dire Hour** ($2.48): {5}{W}{W} Angel 5/4, flash, flying, "When this creature enters, if you cast it from your hand, exile all attacking creatures." The strongest *one-shot* answer to the pod's ground alpha strikes, and a political card (flash it during someone else's combat). It does nothing against combo, drain, fliers you didn't block, or alt-wins, and the trigger doesn't fire off Emeria recursion. 13.9% of Giada decks (5,213 of 37,383). If the user wants a second card for the alpha-strike problem specifically, this is the next one to look at, with Angel of the Ruins as its cut.
- **Platinum Angel** ($10.92): same clause on a colorless 4/4 with no flash. Herald is better on every axis here (bigger, flash, white for Pearl Medallion).
- **Angel's Grace** ($3.52), **Everybody Lives!** ($16.85): one-turn instants. Answers, not a permanent, and the rubric says not to compare the two as if they were the same job.
- **Gideon of the Trials** ($1.54): the emblem needs Gideon to stay on the battlefield, a 3-loyalty walker in a pod that attacks on the ground.
- **Teferi's Protection**: still the ADD IF from the ceiling review if you want *board* protection against exile wipes; Herald takes the "you can't be killed" half of that case off it, so the Game Changer #3 question is now only about wipes.

## After the swap

| | Before | After |
|---|---|---|
| "You can't lose" effects | 0 | **1** |
| Flash creatures | 0 | **1** |
| Angels (incl. Giada) | 24 | **25** (Herald's Horn hit rate ≈ 25%) |
| Rocks / reducers | 9 + Giada | **8** + Giada |
| Static anthems | 7 | **6** |
| 7-drops / MV 6+ | 4 / 8 | **5 / 9** |
| Average nonland MV | 3.50 | ≈3.56 |
| Game Changers | 2 | 2 |
| Combos | 0 | 0 |

Play notes: cast it at an opponent's end step when you can, for Giada's counters and the end-step token triggers, then untap and attack. Hold it against an alpha strike or a combo turn when you can't. Keep it off the table as your *only* reason you're alive: at 0 or less life, every removal spell in the pod is lethal, so use the turn it buys to get back above zero with Bishop, Righteous Valkyrie and lifelink.

Condition to reverse: if goldfishing shows the top end clogging hands (two or more 7-drops stuck by turn 6 in a noticeable share of games), swap the cut to Angel of the Ruins and put Heraldic Banner back, or cut Herald for Angel of the Dire Hour and keep the Banner cut.
