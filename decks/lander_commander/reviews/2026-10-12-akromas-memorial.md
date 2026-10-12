# Akroma's Memorial — lander_commander

Deck: Aesi, Tyrant of Gyre Strait. Bracket 3, 4-player casual, $40/card cap.
Pod calibration reused from `2026-08-31-weakness-audit.md` (asked of the user then,
not assumed): games run **turns 9–12**; threats are combo/spell kills, go-wide
creature combat, mill, aristocrats.

## Verified facts

> **Akroma's Memorial** {7} — Legendary Artifact
> Creatures you control have flying, first strike, vigilance, trample, haste, and
> protection from black and from red.

- Colourless, Commander-legal, no official rulings, **not** a Game Changer.
- `combos.py --add`: **0 new combos** (baseline 6 assembled).
- Price: **$34.30** (foil $54.74), fetched **2026-10-12 18:42 UTC**. Under the cap.

## EDHREC

Akroma's Memorial is on **no** cardlist of the Aesi page (17,253 decks), the
Aesi/Landfall page (1,127 decks) or the Tatyova page (9,468 decks). The finishers the deck
already runs are on all three: Craterhoof Behemoth (synergy +0.10 / +0.07 / +0.05),
Overwhelming Stampede (−0.00 / +0.03 / −0.06). (`edhrec.py card` returned HTTP
403 this session; figures above were read from the commander JSON pages directly.)

## Honest best case

This would be the deck's only **repeatable** source of team evasion and haste. Today:
- **Flying:** 0 cards grant it (the only oracle hit is Ancient Greenwarden's reach
  reminder text).
- **Haste:** Swiftfoot Boots (one creature), Craterhoof (itself only), Finale of
  Devastation (only at X ≥ 10). Goldvein Hydra (itself).
- **Team trample:** Craterhoof and Overwhelming Stampede, both until end of turn.

It also has a real multiplier: 5 landfall payoffs make creature tokens on *your* turn —
Rampaging Baloths (4/4), Scute Swarm, Zendikar's Roil (2/2), Greensleeves (3/3),
Springheart Nantuko. With Memorial those tokens attack the turn they're made, in the
air. Koma's upkeep Coils and Avenger's Plants come along too. Written as
effect × frequency × duration, it is **not** redundant with Craterhoof or Stampede:
those are one-shot, end-of-turn; Memorial is every turn, permanently. Vigilance and
first strike also mean the same board defends against the pod's go-wide deck.

## Attack

**Marginal impact: which lost games does it change?** Against the pod as measured:
- *Combo/spell kills:* nothing. It doesn't interact.
- *Mill:* nothing.
- *Aristocrats:* protection from black stops targeted black removal on your
  creatures; it does not stop drain (life loss isn't damage to creatures and isn't
  targeted at them).
- *Go-wide combat:* the one real case. Vigilant first-strike flyers attack and still block.

The deck only gets value from it if it already has a board and that board is stuck on
the ground. The deck already has three cards that turn a board into lethal (Craterhoof,
Overwhelming Stampede, Finale X ≥ 10), and Hoof does it from an empty hand by
itself. Memorial is a fourth finisher that does nothing alone.

**Cost of entry.** MV 7, adding to a top end already at **12 nonlands at MV 6+** (Aesi,
Ancient Greenwarden, Avenger, Craterhoof, Cultivator Colossus, Ghalta, Jin-Gitaxias,
Kodama, Koma, Nezahal, Rampaging Baloths, Terastodon). The weakness audit named the
top-heavy curve as a measured weakness; this goes the wrong way.

**Worst-case draw.** Turn 12 after a wipe, empty board: a 7-mana artifact that does
nothing. Opening hand: dead until turn 5–6 at best. Both ends are bad.

**Disagreement check.** Absent from every relevant EDHREC page; I agree. Independent
reason: the deck's measured gaps (instant-speed answers, sweepers, graveyard hate,
curve) are elsewhere, and its "turn the board into a kill" slot is already 3 deep
with stronger single cards.

**Price.** $34.30, own line. The rejection survives the card being free.

## Verdict: NO

A permanent evasion/haste engine for a deck that already has three ways to cash in its
board, and whose losses come from combo, mill and a curve that's already top-heavy.

**What would change it:** if you are losing games *with* a big ground board that gets
walled by a go-wide opponent, and Hoof/Stampede are already gone or not drawn, Memorial's
repeatable evasion is the right fix. Then cut **Ghalta, Primal Hunger**, the same role
and the audit's already-named redundant finisher. Do not cut a land or ramp piece for it.

## Counter-proposal (only if that stall problem is real)

Same evasion for far less mana: **Levitation** {2}{U}{U}, MV 4, $0.34 (2026-10-12 18:43
UTC). "Creatures you control have flying." Fills the MV 4 hole instead of the MV 7
pile, but gives no haste or trample, and it's EDHREC rank 8624. Wonder ({3}{U}, $3.88)
was also checked and rejected: it only works from the graveyard, and the deck's only
discard outlet is Nezahal. Neither is recommended unprompted.
