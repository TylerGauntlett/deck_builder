# Quantum Misalignment — lander_commander (Aesi, Tyrant of Gyre Strait)

Bracket 3, 4-player casual, $40/card cap. Oracle text, rulings, legality and prices
fetched **2026-10-30 02:01–02:03 UTC** via `card_facts.py lookup`. Decklist graded
as of the 2026-10-23 sync (100 cards, 43 lands; `cards.md` regenerated this session).

> **Quantum Misalignment** {4}{U} — Sorcery
> Create a token that's a copy of target creature you control, except it isn't legendary.
> Rebound

- Legal in GU, not a Game Changer.
- Price: **$4.15** (fetched 2026-10-30 02:01 UTC). Under the cap; plays no part in the verdict.

## Verdict: **ADD IF you've passed on the audit's Aetherize-for-Ghalta swap. Then cut Ghalta, Primal Hunger.** It also takes that slot ahead of Nissa, Worldsoul Speaker.

## Premise used

From the 2026-09-01 audit, where the user was asked: games run **turns 9–12**, and the
pod's threats are **combo/spell kills, go-wide combat, mill, aristocrats**. Nothing
since then has changed it.

## Best case

It's the deck's **only way to copy a legendary creature and keep both**. One cast
gives two non-legendary copies, the second free on your next upkeep, picked from
whatever is best at the time:

| Target (verified text) | What the copy does |
|---|---|
| Aesi — "You may play an additional land… / Landfall — … you may draw a card" | +1 land drop a turn and +1 draw per land, permanently. Extra land-play effects stack (CR 305.2). A rebound cast at upkeep lands before your land drops, so it pays off that same turn. |
| Azusa — "two additional lands" | +2 land drops for 5 mana |
| Tatyova — landfall: gain 1, draw | a second Tatyova |
| Koma — Serpent token "at the beginning of each upkeep" | twice as many Coils, and more Serpents to sacrifice |
| Craterhoof — ETB +X/+X, haste | the token has haste and re-triggers the pump. A rebound cast on upkeep then attack is a real kill turn. |
| Avenger — ETB a Plant per land | a second batch of Plants |
| Terastodon — ETB destroy up to 3 noncreature permanents | 3 more answers (Acidic Slime and Reclamation Sage work the same way) |

**The one existing copy effect is different.** Springheart Nantuko ("create a token
that's a copy of that creature", {1}{G} per landfall while bestowed) repeats, but its
copies **are legendary**, so it can't usefully copy Aesi, Azusa, Tatyova, Koma or
Kodama (the legend rule kills one). QM covers exactly the legendary targets
Springheart can't. They don't overlap.

**Multiplies Jin-Gitaxias:** "Whenever you cast an … sorcery spell, copy that spell"
works on both the hand cast and the rebound cast. That's four tokens from one card.

## The attack

- **Marginal impact.** The main use, a second Aesi, needs Aesi on board plus 5 spare
  mana. That's a game you're already winning. Against the four ways the deck loses,
  it does very little. Its one answer mode (copying Terastodon / Acidic Slime /
  Reclamation Sage) is sorcery speed and needs the creature already in play. This
  is the strongest point against it.
- **Lane depth.** The audit found landfall/draw over-served (11 landfall payoffs, 4
  repeatable draw engines). QM adds nothing to a new category. Its saving grace: it's
  **multiplicative**. It doubles the engine the deck runs on, where most cards in that
  lane add one more piece.
- **Worst case.** With an empty board after a wipe it's dead: it needs a target on
  both casts. In an opening hand it does nothing before turn ~6. Ghalta, the proposed
  cut, has the same problem (costs 12 with no board).
- **Deck-out.** Aesi's draw is "may", so a second Aesi doesn't add forced draws.
  Copying Tatyova does ("draw a card" is mandatory). With a thin library, copy Aesi.
- **Combos.** `combos.py --add` shows 2 new lines: Kodama of the East Tree + {Simic
  Growth Chamber | Oboro, Palace in the Clouds} + QM → infinite landfall triggers.
  The deck **already assembles 12** Kodama + bounce-land 3-card lines, and these need
  11 mana across three cards. That isn't the "early two-card" combo the house rule
  bans. Bracket stays the same.
- **Disagreement check.** QM isn't listed on Aesi's EDHREC page at all, and doesn't
  appear in the Aesi "Clones" theme (26 decks). Its EDHREC homes are clone/token
  commanders (Koma 25.5%, 2016/7897). I can't name a way this deck differs from
  typical Aesi decks. The case rests on the Springheart gap and the multiplier
  argument, not on anything unusual about this list. So this is ADD IF, not ADD.

## The cut

Only one slot is honestly cuttable, and it's already claimed twice:

1. **Ghalta, Primal Hunger** ({10}{G}{G}): third finisher behind Craterhoof and
   Overwhelming Stampede (audit, 2026-09-01). QM beats it in every mode. It's a
   finisher when copying Craterhoof, an engine when copying Aesi or Azusa, and removal
   when copying Terastodon. Both are dead with an empty board.
   - **But** the audit gave this slot to **Aetherize**, the deck's only mass answer,
     because that's how the deck loses. Interaction still beats engine here. That's
     why this is ADD IF.
   - **Against Nissa** (the 2026-10-23 ADD IF for this same slot): QM wins. Nissa
     needs four lands per free spell and pays off only at the top end. QM pays off
     the turn it resolves and again next upkeep.
2. Runners-up, each spared:
   - **Herd Heirloom**: MV2 ramp. Cutting ramp for a 5-drop moves the curve the
     wrong way (the audit's Krosan Grip claim on this slot is also still open).
   - **Jin-Gitaxias**: the one card that multiplies QM (see above). Cutting it would
     contradict that argument.
   - **Goldvein Hydra**: claimed by the audit for Reality Shift (exile vs
     aristocrats).

## Counter-proposal check

`card_facts.py search 'id<=gu o:"isn't legendary" o:copy'`, 22 hits. The closest are:
- **Spark Double** {3}{U}, $10.91: one copy, not two, but it's a creature, so Finale
  of Devastation can fetch it (X=4), and it lands at MV4 where the deck has only 2
  cards. Copy-for-copy, QM gives more.
- **Helm of the Host** {4}, $5.16: repeating, but equip {5} plus 4 to cast is 9 mana
  before the first copy.
- **Double Major** {G}{U}, $2.34: copies only a creature *spell* as it's cast, so it
  can't copy Aesi once she's in play and does nothing for a commander already out.

None beats QM for this role in this deck.

## Aggregate (if added for Ghalta)

| | Before | After |
|---|---|---|
| Lands | 43 | 43 |
| MV5 / MV12 | 6 / 1 | 7 / 0 |
| Pips | G61 U21 | G59 U22 |
| Creatures / Sorceries | 30 / 8 | 29 / 9 |
| Game Changers | 2 | 2 |
| Assembled combos | 12 | 14 (same Kodama shape) |

## Open question for the user

Since the September audit you cut Call Damage Control and added Oboro, Turntimber
Symbiosis and Verdant Kraken, but none of the audit's seven interaction swaps went
in. If you've decided against Aetherize, QM replaces Ghalta. If Aetherize is still
planned, it gets the slot and QM waits.

---

## Update (same day): current list differs from `base.txt`

The user pasted their current list (100 cards). Against `base.txt` it has two swaps,
both from the 2026-10-23 review:

- **Ghalta, Primal Hunger → Nissa, Worldsoul Speaker**
- **Botanical Sanctum → Willowrush Verge**

That answers the open question: Nissa was conditional on passing on Aetherize, so
Aetherize is off. It also removes the cut I named, because Ghalta is already gone.
Re-ranking the cuts (texts re-fetched 2026-10-30 02:37 UTC):

### New verdict: **ADD, cut Goldvein Hydra**, unless you still plan to use that slot for Reality Shift.

1. **Goldvein Hydra** ({X}{G}: vigilance, trample, haste; dies → tapped Treasures
   equal to its power). The only reason I spared it above was that the audit had
   claimed its slot for Reality Shift. That's the same claim pattern as Aetherize on
   Ghalta, and none of the audit's seven swaps have gone in over two months. Taken on
   its own merits it's the cut: no landfall, no ETB, no land text (audit), and
   Craterhoof, Overwhelming Stampede and Avenger already cover winning games. The
   10-23 review already ranked it with Ghalta as cuttable.
2. **Zendikar's Roil** (runner-up): the 7th token-landfall payoff, with the smallest
   bodies (audit). Spared because it fits the deck's landfall tiebreaker, which QM
   doesn't, and because the audit claimed its slot for Scavenging Ooze.
3. **Nissa, Worldsoul Speaker** (spared): above I said QM would take the Ghalta slot
   ahead of her, and that still holds if only one of them can stay. But Goldvein is
   worse than both. Nissa is also the deck's only way to cast spells from landfall,
   and one of only 3 cards at MV4 (Arixmethes, Oracle of Mul Daya, Nissa). Cutting her
   would undo the curve fix you just made.
4. Herd Heirloom and Jin-Gitaxias stay spared for the reasons above. Both still hold.

### Aggregate vs the pasted list

| | Before | After |
|---|---|---|
| Lands | 43 | 43 |
| MV1 / MV5 | 5 / 6 | 4 / 7 |
| Pips | G60 U21 | G59 U22 |
| Creatures / Sorceries | 30 / 8 | 29 / 9 |
| Game Changers | 2 | 2 |

`base.txt` is still the pre-swap list. Sync it before the next review.
