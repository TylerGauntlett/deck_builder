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
