# Angels — raising the ceiling inside bracket 3

Date: 2026-10-02 · Deck state reviewed: `complete.txt` (24 changes from base) · Prices: Scryfall, fetched 2026-10-02 15:12 UTC
Constraints: bracket 3 (≤3 Game Changers, no early infinites, no tutor-dependent win), $40/card, ~$300 total (~$96 left).

## Where the remaining power is

The list has **0 of 3 Game Changers** used and about $96 of budget unspent. Its weakest slots are now utility, not threats: Commander's Sphere, Angel of Finality, Cleansing Nova and basic Plains. Each recommendation below is a same-role upgrade or a replacement for one of those.

`card_facts.py search 'is:gamechanger id<=w f:commander'` → 19 cards. Most are over the $40 cap at every printing: Ancient Tomb, The One Ring ($111.48 cheapest), Mana Vault, Chrome Mox, Smothering Tithe ($54.48 cheapest), Serra's Sanctum, and others. Humility would blank this deck's own creatures. That leaves four that fit: **Farewell, Drannith Magistrate, Enlightened Tutor, Teferi's Protection**.

## ADD

| Add | Cut | Price | Case |
|---|---|---|---|
| **Farewell** (GC 1) | Cleansing Nova | $6.21 | Same role, strictly more flexible. It **exiles** instead of destroying, and you pick any subset of artifacts, creatures, enchantments and graveyards. You can sweep artifacts and enchantments and keep your board, or add graveyards, which makes it this deck's second graveyard hate. With **Clever Concealment** you can phase out your own board first and make the wipe one-sided. Giada EDHREC 34.8% (12,549 decks). |
| **Drannith Magistrate** (GC 2) | Angel of Finality | $9.58 (TLE #2; $12.60 default) | "Your opponents can't cast spells from anywhere other than their hands." It **shuts off casting opposing commanders from the command zone entirely** while it is out, and also flashback, escape, foretell, adventure-from-exile and cascade. It makes the deck's 9 targeted removal spells permanent against commanders. That is useful against every deck in a rotating pod, not just some. Angel of Finality was spared earlier only as the last graveyard hate. Farewell can be cast in graveyards-only mode, so it now covers that role and the last-of-role protection no longer applies. *(Corrected 2026-10-02: an earlier version said Magistrate also covered graveyard hate. It doesn't stop reanimation, per the ruling "Effects may put cards from other zones onto the battlefield under an opponent's control." Farewell is now the deck's only graveyard answer.)* Giada EDHREC: under 5% (not listed). The difference is that most Giada lists skip soft stax; this pod's general-usefulness rule favours it. |
| **Archivist of Oghma** | Commander's Sphere | $6.30 | Flash. "Whenever an opponent searches their library, you gain 1 life and draw a card." Opponents search for fetchlands, ramp spells and tutors, so this is a card-draw engine in almost any pod. Each draw comes with lifegain, which triggers **Archangel of Thune** (counters on every creature), **Lyra, Archangel of Dawn** (counters on Angels) and pushes toward **Resplendent Angel** and **Valkyrie Harbinger**'s end-step thresholds. As a Cleric it also triggers **Righteous Valkyrie**. Sphere is the least important of 12 ramp pieces. Giada EDHREC 9.5% (3,407). |
| **Castle Ardenvale** | Plains | $0.29 | Enters untapped with a Plains. Late game, {2}{W}{W},{T} makes a token every turn. Each token triggers Cathars' Crusade and Dazzling Angel, and Dazzling Angel's life triggers Thune and Lyra AoD. A land slot that turns into an engine for free. |
| **Eiganjo, Seat of the Empire** | Plains | $5.79 | Untapped W. Channel deals 4 to an attacker or blocker, {1} cheaper per legend (Giada, both Lyras, Gisela, Avacyn and Sephara). Uncounterable removal from a land slot, and it answers ground attackers in this pod. |

Total: $28.17 → overall build ≈ **$232**. Plains 29 → 27. Emeria still needs only 7 Plains, and Endless Atlas still needs 3 same-named lands. Neither is at risk.

## ADD IF

- **Teferi's Protection** (GC 3, $36.26 MAR #51): add it if you want insurance against **you** being killed (combo, life loss, alpha strike). Clever Concealment protects the board, not you. Cut: Invoke the Divine. Farewell and Generous Gift cover artifacts and enchantments.

## NO

| Card | Reason |
|---|---|
| Enlightened Tutor (GC) | A tutor that costs a card. The deck wins through redundancy, not one piece. Under the house rule against tutor-dependent wins it adds consistency but no new line. |
| Skullclamp | Anti-synergy. Giada and Cathars' Crusade put counters on everything, so few creatures die to −1 toughness. Only Servos and Spirit tokens qualify. |
| Esper Sentinel ($60.38), Mox Amber ($87.04) | Over the $40 cap at their cheapest printings. |
| Windbrisk Heights | Enters tapped. Castle Ardenvale and Eiganjo are better land upgrades. |

## What stays off the table at bracket 3

A 4th Game Changer, *early* two-card infinites, mass land denial and extra-turn chains. Late-game infinites are allowed by the house rules (see below). Past these adds, the next real gains come from bracket 4 cards, not better bracket 3 choices.

Combo check: `combos.py --add` on Archivist, Drannith, Farewell and Castle Ardenvale: none completes a combo. (combos.py reads `base.txt`. Thune and Crusade were each checked separately in the build-out review.)

## Correction: the near-combos are allowed, and still not recommended

An earlier line here said to keep Walking Ballista, Triskelion and Storm Herd out. That was wrong. `meta.json` allows late-game infinites and bans only early or tutor-dependent ones. Details from Commander Spellbook, fetched 2026-10-02:

| Line | Pieces actually needed | Earliest realistic | Allowed? |
|---|---|---|---|
| Thune + Walking Ballista (2919-3693) | Thune (5), Ballista with ≥2 counters (X=2 → 4), **and lifelink on Ballista**. Lyra Dawnbringer only gives Angels lifelink, so the deck's only source is Akroma's Will (4, instant, one turn). Three specific cards, about 13 mana in total. | Late game | Yes |
| Thune + Triskelion (1495-2919) | Same, with Triskelion (6) | Late game | Yes |
| Storm Herd + Cathars' Crusade (2067-2744) | {8}{W}{W}. Finite: X tokens and X² counters, where X is your life. Not a loop. | Late game | Yes |

**Verdicts on merit:**
- **Walking Ballista** ($10.72): **NO, close.** On its own it is a flexible X-drop that grows off Cathars' Crusade, Thune and Norn's Choirmaster's proliferate, and pings X/1s. But the combo needs three specific cards, and the deck has no tutors, so it will rarely come together. Without the combo, Ballista doesn't beat the remaining weakest slots by enough. If you want the line anyway, cut Metallic Mimic.
- **Triskelion** ($0.69): **NO.** A 6-mana version of the same line that doesn't scale.
- **Storm Herd** ($1.06): **NO.** A 10-mana sorcery that only Pearl Medallion reduces, and it creates the army at sorcery speed into a wipe. The deck already has enough finishers: Akroma's Will, Avacyn, Sephara and the counter engines.

## Clarification: what Drannith Magistrate is for (2026-10-02)

The user asked what problem it solves. It is a **disruption piece, not a synergy piece**. It doesn't advance the Angel plan; it doesn't get Giada's counters or Angel cost reductions.

- **Stops:** casting opponents' commanders from the command zone, including the first cast if Magistrate lands earlier. Also flashback, escape, foretell, adventure-from-exile and cascade.
- **Makes removal permanent:** Swords, Path, Generous Gift and Get Lost on a commander normally buy one or two turns before it is recast. With Magistrate out, the commander stays gone.
- **Doesn't stop:** reanimation and other put-onto-battlefield effects (official ruling), commanders already on the battlefield, or decks that don't rely on their commander.
- **Costs:** a 1/3 that dies to anything, and it draws attention at the table.

**Open question for the user:** how commander-dependent are the pod's decks? If not much, swap the Game Changer slot to Teferi's Protection, cutting Drannith Magistrate.
