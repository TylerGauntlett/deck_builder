# Loot, Exuberant Explorer — lander_commander

Deck: Aesi, Tyrant of Gyre Strait. Bracket 3, 4-player casual, $40/card cap.
Pod premise reused from the 2026-09-01 weakness audit (asked, not assumed then):
games run **turns 9–12**; threats are combo/spell kills, go-wide combat, mill, aristocrats.

## Verified text (card_facts.py, fetched 2026-10-18 16:18 UTC)

> **Loot, Exuberant Explorer** {2}{G} — Legendary Creature, 1/4
> You may play an additional land on each of your turns.
> {4}{G}{G}, {T}: Look at the top six cards of your library. You may reveal a creature
> card with mana value less than or equal to the number of lands you control from among
> them and put it onto the battlefield. Put the rest on the bottom in a random order.

Legal in GU. Not a Game Changer. Price **$2.94** (foil $3.73).
`combos.py --add`: baseline 6 combos, **0 new**, 0 near. Bracket-neutral.

## Steel-man

Loot is two cards. The first line is a sixth extra-land-drop source at MV 3. The second
is something the deck has **zero** of: a *repeatable* way to put a creature onto the
battlefield from the library. (Finale of Devastation is the only other library-to-
battlefield creature effect, and it is a one-shot.) With 28 creatures among the 99,
P(at least one creature in the top six) = **87%**; past 8 lands every creature except
Ghalta is eligible. Effect × frequency × duration: one free creature, every turn, for
as long as Loot lives — an engine, not a ramp spell.

## Attack

**Line 1 is redundant.** Permanent extra-land-drop sources already in the 99:
Aesi, Azusa (two), Dryad of the Ilysian Grove, Exploration, Oracle of Mul Daya — 5 cards,
6 extra drops, plus Burgeoning and Urban Evolution's one-shot. The 2026-08-31 review
rejected Wayward Swordtooth for exactly this: the binding constraint is lands *in hand*,
not permission. Loot supplies no lands. (Contrast Icetill Explorer, which self-fuels.)

**Line 2 is real but lands in the deck's deepest lane.** It costs 6 mana per activation
and Loot must survive a turn cycle first. In a 9–12 turn game, cast on 3, that is
roughly 3–5 activations — real card and board advantage. But the deck's late game is
already Aesi drawing a card per land and 11 landfall payoffs; the audit measured
landfall/ramp as *over*-served. Loot's engine converts mana into board in a deck that
already wins the long game when it isn't killed first.

**Marginal impact on losses: near zero.** The pod kills via combo, go-wide, mill and
aristocrats. Loot answers none of them. A 1/4 blocks one go-wide token per turn. Its
only interaction is incidental — an activation can flip Reclamation Sage, Acidic Slime
or Terastodon, but that is a random dig, not an answer you can hold up.

**Worst case:** turn-3 Loot on a full curve is fine (land drop + blocker). Turn-12 Loot
on an empty board is a 1/4 that needs another turn before it does anything. Not dead,
not strong.

**Disagreement check.** EDHREC: **33.5% of Aesi decks** (5751/17167), 31.3% Tatyova
(2947/9425), 32.6% Azusa (2391/7341) — higher than Icetill Explorer (21.4%) or Wayward
Swordtooth (23.8%) in the earlier review. Why this deck differs: (a) Aesi's page is
diluted by the *Reap the Tides* precon (verified in the 08-31 review) and Loot is a
cheap Foundations reprint; (b) this list already runs five permanent extra-drop
sources and its measured holes are interaction, not engine.

## Cut check

`base.txt` (synced 2026-09-03) still contains all seven cuts the 09-01 audit proposed —
Herd Heirloom, Goldvein Hydra, Negate, Zendikar's Roil, Ghalta, Call Damage Control,
Jin-Gitaxias — so those swaps have not been made. Those slots are the weakest cards in
the list, but each was earmarked for an interaction add that targets this pod's actual
kill vectors. Loot does not beat any of those adds (Krosan Grip, Reality Shift, An Offer
You Can't Refuse, Scavenging Ooze, Aetherize, Eternal Witness, Splendid Reclamation)
for its slot. Beyond those seven, the audit found **no eighth cut** (Greensleeves and
Ghost Quarter defended) and Loot does not change that.

## Verdict: NO

Sixth extra-land-drop source in a deck limited by lands in hand, and its real upside —
a repeatable creature cheat — deepens the lane the deck already wins in rather than the
games it loses. Rejection does not rest on price; it holds if the card is free.

**Ranking within the lane** (if you ever give a slot to an extra-land-drop creature):
Icetill Explorer > Loot > Wayward Swordtooth. Loot beats Swordtooth outright (blocking
body plus an activation vs. a body that can't attack or block early); Icetill wins
because it fixes the lands-in-hand constraint instead of adding permission.

**What would change this:** if your games are actually being lost to *stalling* —
plenty of lands and cards but no threats on board by turn 8 — the creature-cheat
line moves from win-more to a fix, and Loot becomes an ADD over Goldvein Hydra.
Nothing in the 09-01 audit suggested that pattern; tell me if it's happening.

Prices (2026-10-18 16:18 UTC): Loot $2.94, Icetill Explorer $20.53, Wayward Swordtooth
$4.96, Azusa $12.68, Dryad of the Ilysian Grove $10.01.

---

## Addendum — re-evaluated as early ramp (user's stated role)

User: the card's job is to **lower the curve and ramp before Aesi (MV 6) comes down**.
The first pass never measured Loot as early ramp, so I measured it now.

**Method.** Goldfish Monte Carlo, 200k games: a 99-card library with 44 lands, the
candidate forced into the opening 7, on the play, one card isolated (the deck's other
ramp is ignored, so this measures the *marginal* effect of one card). Each candidate
is cast as soon as possible. A land-fetch adds a land from the library; an extra-drop
card only helps if a spare land is in hand.

| Candidate (MV) | Avg lands T4 | Avg lands T5 | P(6 lands by T4) | P(6 lands by T5) |
|---|---|---|---|---|
| nothing | 3.47 | 4.13 | 0% | 0% |
| Explore (2) | 4.11 | 4.71 | 0% | 36% |
| **Loot (3)** | 4.00 | 4.49 | **15%** | **25%** |
| Azusa (3) — already in deck | 4.04 | 4.49 | 15% | 25% |
| Wood Elves (3) | 4.33 | 5.04 | 0% | 49% |
| Nature's Lore (2) | 4.44 | 5.11 | 0% | 49% |

**Findings.**
- Loot occasionally gets you a turn-4 Aesi (15%), but by turn 5 it reaches six
  lands **half as often** as a card that fetches a land (25% vs 49%). The deck needs
  six mana reliably, and a spare land in hand is what Loot is missing.
- Loot's numbers match **Azusa's exactly**, even though Azusa grants two extra drops.
  That confirms a spare land in hand is what limits the extra-drop cards, not
  permission. Loot would be the third 3-mana creature in this role, after Azusa and Dryad.
- Caveat: the real deck's Cultivate, Kodama's Reach, Yavimaya Elder and Coiling Oracle
  put extra lands in hand and lift every extra-drop card somewhat. But a land-fetch
  card still doesn't need any of them.

**Verdict on Loot: still NO.** Re-run on the user's axis, the verdict holds. The role
the user identified, ramp at MV 2–3 that lowers the curve, is real.

## Counter-proposal: ADD Nature's Lore, cut Ghalta, Primal Hunger

> Nature's Lore {1}{G} — Sorcery
> Search your library for a Forest card, put that card onto the battlefield, then shuffle.

Price $2.25 (2026-10-18 18:19 UTC). Legal; `combos.py --add`: 0 new combos.
- Best measured result for this role (tied with Wood Elves), at **MV 2**, so it lowers
  the curve more than a 3-drop. The Forest enters **untapped**, so turn-2 Lore means
  four mana on turn 3. Rampant Growth also costs 2 but its land enters tapped.
- The land entering also triggers landfall: Lotus Cobra, Tatyova, Aesi.
- Ghalta, Primal Hunger: MV 12, the deck's most expensive card. The 09-01 audit
  called it the third redundant finisher behind Craterhoof and Overwhelming
  Stampede. Swapping it for Lore drops the average nonland MV and the MV 6+ count.
- **Conflict to flag:** the audit earmarked Ghalta's slot for Aetherize. If you take
  that swap too, Lore needs a different cut. The runner-up is Jin-Gitaxias, Progress
  Tyrant (MV 7), which is also earmarked (for Splendid Reclamation). You can't take
  both audit swaps and this one without a new cut.
- **Runner-up add: Wood Elves** ($0.26) has the same measured result. It's a creature,
  so Finale of Devastation can fetch it, but it costs MV 3. Pick it if you want a body.

Prices (2026-10-18 18:19–18:21 UTC): Nature's Lore $2.25, Wood Elves $0.26, Explore $0.24,
Three Visits $5.14, Farseek $0.87, Sakura-Tribe Elder $0.44, Ghalta $1.17.
