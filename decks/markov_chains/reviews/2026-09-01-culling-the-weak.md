# markov_chains — Culling the Weak, 2026-09-01

Candidate: **Culling the Weak**. Verdict: **NO**.

Deck context (`deck_meta.py show markov_chains`): Edgar Markov · commander ·
bracket 3 · $40/card cap · 4-player casual pods. Vetoes: no early infinite combos;
no win line that depends on tutoring to assemble. Stated goal: *"Win with a string
of individually useful cards rather than by assembling a named combo."*

All candidate text and price fetched from Scryfall **2026-09-01 16:51–16:52 UTC**.
Deck composition counted from `decks/markov_chains/cards.json` (built 2026-08-31
16:02, newer than `base.txt` at 10:17 — no rebuild needed). EDHREC from
`cards/culling-the-weak`. Combos via `combos.py --add`.

---

## Verified text

**Culling the Weak** `{B}` — Instant
> As an additional cost to cast this spell, sacrifice a creature.
> Add {B}{B}{B}{B}.

MV 1 · colour identity B · **legal** · in Edgar's identity · EDHREC rank 533.
**Price $6.93** (fetched 2026-09-01 16:51 UTC) — under the $40 cap.

No hard veto fires. It is legal, in identity, in budget, and completes **zero**
new combos (`combos.py --add` — baseline stays at 2: Vito + Bloodthirsty
Conqueror, Marauding Blight-Priest + Bloodthirsty Conqueror). The
no-early-infinites veto is not engaged. This is rejected on the tests, not vetoed.

---

## Step 0 — the honest best case

Stated so it could be false:

> *In this deck the additional cost is not a cost. Edgar's eminence — "Whenever
> you cast another Vampire spell, if Edgar is in the command zone or on the
> battlefield, create a 1/1 black Vampire creature token" — produces bodies as a
> by-product of casting the deck's 35 Vampires, and feeding one to Culling the
> Weak triggers a wall of payoffs. It is a one-mana instant that nets **+3 mana**,
> beating Dark Ritual's +2, and it is castable in response to targeted removal so
> the creature is converted rather than lost.*

That case is real and I want to give it its full weight before attacking it.

**The payoffs, grouped by trigger scope** (this matters — see failure mode 3):

*Fires on any creature dying, yours or theirs:*
- **Blood Artist** — "Whenever this creature **or another creature** dies, target player loses 1 life and you gain 1 life."
- **Cordial Vampire** — "Whenever this creature **or another creature** dies, put a +1/+1 counter on **each Vampire you control**."
- **Vein Ripper** — "Whenever **a creature** dies, target opponent loses 2 life and you gain 2 life."
- **Blade of the Bloodchief** — "Whenever **a creature** dies, put a +1/+1 counter on equipped creature. If equipped creature is a Vampire, put **two**."
- **Elenda, the Dusk Rose** — "Whenever **another creature** dies, put a +1/+1 counter on Elenda."

*Fires only on your own creatures dying:*
- **Bastion of Remembrance**, **Cruel Celebrant**, **Zulaport Cutthroat** — each opponent loses 1, you gain 1.
- **Grave Pact** — "Whenever a creature **you control** dies, each other player sacrifices a creature **of their choice**." (Their choice — this is a grind, not a blowout.)

*Fires only if the sacrificed body is a token:*
- **Mirkwood Bats** — "Whenever you create **or sacrifice a token**, each opponent loses 1 life." An eminence token fed to Culling does trigger this; a real Vampire does not.

So: sacrificing one eminence token with a developed board can be a drain, a
counter on every Vampire, an edict on all three opponents, and a Bats ping. That
is a genuinely good sacrifice. **And the strongest concrete line exists:** turn 1
one-drop creature (the deck has five — Carrion Feeder, Indulgent Aristocrat,
Master of Dark Rites, Vampire of the Dire Moon, Viscera Seer), turn 2 land + `{B}`
for Culling, sacrifice it, `{B}{B}{B}{B}` exactly casts **Grave Pact**
`{1}{B}{B}{B}`, **Bloodletter of Aclazotz** `{1}{B}{B}{B}` or **Vampire
Nocturnus** `{1}{B}{B}{B}` on turn two.

That is the card at its best. Now the attack.

---

## What kills it

### 1. The role is filled, and filled at a better rate

The job "convert a spare body into black mana" is already in this deck, as a
repeatable permanent rather than a one-shot spell:

**Master of Dark Rites** `{B}` — "{T}, Sacrifice another creature: Add
{B}{B}{B}. Spend this mana only to cast **Vampire, Cleric, and/or Demon** spells."

Per the rubric's *effect × frequency × duration* rule, these are **not** strictly
redundant and I am not going to pretend they are — Culling is instant-speed,
unrestricted, and needs no untapped creature. But run the comparison honestly and
Culling loses on every term that matters here:

| | Culling the Weak | Master of Dark Rites |
|---|---|---|
| Frequency | once, ever | **every turn** |
| Card cost | spends a card | already on board |
| Mana | +3 net | +2 net |
| Restriction | none | Vampire/Cleric/Demon — **35 of the deck's 38 creatures are Vampires**, so near-free |

The restriction that is supposed to be Master of Dark Rites' weakness is close to
nonexistent in a deck this tribal. And the deck **also** runs **Dark Ritual**
`{B}` → `{B}{B}{B}`, the one-shot unrestricted burst that costs no creature at all.
Culling is the third card competing for a job two cards already do.

### 2. The mana it makes has nowhere good to go

Nonland curve, counted from `cards.json` — **13 at MV1, 15 at MV2, 17 at MV3, 12 at
MV4, 5 at MV5, 3 at MV6**. Average nonland mana value **2.85**. Forty-five of the
65 nonland cards cost three or less.

A ritual is worth what its ceiling is worth, and this deck's ceiling is eight cards
at MV 5+. Two specific problems:

- **It cannot cast your commander.** Edgar is `{3}{R}{W}{B}`. `{B}{B}{B}{B}` pays
  `{3}{B}` and leaves `{R}{W}` outstanding, so the classic "ritual out the
  commander" line needs a red source *and* a white source on top.
- **Its only clean targets are the four `BBB` cards** — Bloodletter of Aclazotz,
  Grave Pact, Vampire Nocturnus, Vein Ripper (`{3}{B}{B}{B}`, needs two more mana).
  Outside those, four black mana on turn 2–3 buys two two-drops you were going to
  cast anyway a turn later.

Mana supply is not a gap either: 35 lands plus Sol Ring, Arcane Signet, three
Talismans, Dark Ritual and Master of Dark Rites, against an average MV of 2.85.
This deck is not short of mana. It is short of **board recovery** — see below.

### 3. It spends the deck's only currency, in the deck with no way to get it back

The 2026-08-31 structural audit's Finding 1 stands unrefuted: the deck has **zero
cards that return another creature from the graveyard** (Bloodghast returns only
itself; Bojuka Bog is outward-facing hate), 38 creatures, and **no non-creature win
condition**. Its one currency is bodies on the battlefield.

And the bodies are not spare. Every Vampire on board is being multiplied by:

- **Sanctum Seeker** — "Whenever **a Vampire you control attacks**, each opponent loses 1 life and you gain 1 life." Per body, per attack, per opponent.
- **Edgar's own attack trigger** — "Whenever Edgar attacks, put a +1/+1 counter on **each Vampire you control**." Scales with count.
- Four lords: **Captivating Vampire**, **Legion Lieutenant**, **Stromkirk Captain** (+1/+1 each), **Vampire Nocturnus** (+2/+1 and flying while the top card is black).

A 1/1 eminence token under two lords with Sanctum Seeker out is a 3/3 that drains
three per swing. Culling the Weak trades that, permanently, for four mana once —
in a deck that cannot rebuild it, in a pod you have told me runs **long** and is
**mono-white heavy** (the wrath colour). This is the anti-synergy test, and it
fails it hard.

### 4. The deck already runs the strictly better version of the same effect

**Village Rites** `{B}` — Instant — "As an additional cost to cast this spell,
sacrifice a creature. **Draw two cards.**"

Identical cost, identical additional cost, identical instant speed, identical
access to all eleven death triggers above, identical "sac in response to removal"
play pattern. The only difference is what you get back: two cards, or four mana.
Village Rites replaces itself **and** the body. Culling the Weak leaves you down a
card and down a creature, holding mana.

If the appeal is "instant-speed sacrifice with a wall of triggers," you already own
it and it doesn't cost you the card.

### 5. Worst-case draw — dead at both ends

- **Opening hand, on the draw:** literally uncastable on turn 1 — the additional
  cost requires a creature on the battlefield and you have none. It is the one
  ritual that cannot power out a turn-one play.
- **Turn 12, board wiped, top-decking:** uncastable again, for the same reason,
  and this is exactly the game state the audit identified as this deck's losing
  one.

A card that is excellent only in the narrow middle — developed board, a `BBB`
four-drop in hand, and a reason to want it a turn early — is worse than its
average suggests. That is the rubric's flag verbatim.

### 6. The community agrees, and the company it keeps is the tell

**8.7% of Edgar Markov decks run it — 4,374 of 50,184** (EDHREC, fetched
2026-09-01). I am saying no and the community is saying no, so the disagreement
check does not fire against me. But the co-occurrence data is more informative
than the percentage:

| Commander | Inclusion |
|---|---|
| Rograkh // Silas Renn | **92.3%** (8,123/8,805) |
| Kraum // Tymna the Weaver | 60.6% (7,174/11,848) |
| Yawgmoth, Thran Physician | 46.3% (3,282/7,088) |
| K'rrik, Son of Yawgmoth | 38.4% (7,799/20,295) |
| **Edgar Markov** | **8.7%** |

And its top co-played cards: Dark Ritual, Mystic Remora, Force of Will,
Flusterstorm, Pact of Negation, Brain Freeze, Deflecting Swat, Mental Misstep.
That is a **cEDH storm profile**. Culling the Weak is a card for decks that convert
a burst of black mana directly into a win on the spot — which is precisely the
thing `meta.json` says this deck is built *not* to do: *"Win with a string of
individually useful cards rather than by assembling a named combo."* Here it
completes zero combos, so it isn't even doing that job; it is just a ritual in a
deck with no storm turn to pay for.

---

## The premise check (failure mode 1)

My rejection leans partly on games running long, so I checked what that rests on.
It is **not** `meta.json` — it is your own correction, recorded in the 2026-08-30
review's Addendum 2 and adopted by the 2026-08-31 audit: this pod plays **long
games**, several opponents are **mono-white**, and **Farewell and Armageddon are
commonly played**. A ritual is worth most in short games and decays to nothing in
long ones, so the corrected premise points the same way my verdict does.

**And the verdict survives the premise flipping.** If your games were actually
fast, Culling the Weak still cannot cast Edgar, still has only four clean `BBB`
targets, still costs a body in an aggro plan whose currency is bodies, and is still
uncastable on turn one. The speed premise makes the rejection more comfortable; it
is not carrying it.

## The dual-mode check (failure mode 7)

Scored against both plans and the bridge between them, not one at a time:

- **Aggro plan** (Edgar resolved, wide board, lords, Sanctum Seeker): Culling
  *spends* the resource this plan wins with, for mana the plan doesn't need — its
  curve tops out at four.
- **Aristocrats plan** (Edgar absent, grind and drain): the sacrifice triggers are
  real, but *causing deaths is not this deck's bottleneck.* It runs three free
  repeatable outlets — **Carrion Feeder** ("Sacrifice a creature: Put a +1/+1
  counter on this creature"), **Viscera Seer** ("Sacrifice a creature: Scry 1"),
  **Bloodthrone Vampire** ("Sacrifice a creature: This creature gets +2/+2") — plus
  **Indulgent Aristocrat** `{2}`, **Baron Bertram Graywater** `{1}{B}`, and
  **High-Society Hunter** on attack. Six outlets. A seventh, one-shot, card-negative
  outlet is not what this plan wants.
- **The bridge** (the +1/+1 counter package — Cordial Vampire, Patron of the Vein,
  Indulgent Aristocrat): Culling feeds Cordial Vampire **once**. Carrion Feeder
  feeds it every turn, for free, and is already in the deck.

It loses to both modes and to the bridge. This is not a card that got rejected by
each plan in turn for opposite reasons — it fails the same way in all three.

---

## The cut that doesn't exist

Every cut candidate the record has named for this deck is already gone from
`base.txt`: **Orzhov Basilica** (the audit's Finding 3), and the two runners-up,
**Vicious Conquistador** and **Unexplained Absence**. The list is now 100 cards
with 35 lands and 65 nonland spells, and I could not find a card in it I would
defend less than the ones above.

Per the rubric: *"If the best cut you can find is a card you would defend in any
other context, that is strong evidence the addition isn't worth it."* That is the
situation here, and it applies to any add from this point on, not just this one.

## Price

**$6.93**, fetched 2026-09-01 16:51 UTC. Comfortably under the $40 cap. Price is
its own line and it is **not** load-bearing: **this rejection survives the card
being free.** If you already own it, nothing above changes.

---

## Verdict

**NO** — it is a third "body into black mana" effect behind Master of Dark Rites
(repeatable) and Dark Ritual (no body), making mana for a curve that tops out at
four, by spending the one resource the deck has no way to rebuild.

**Not an ADD IF.** I looked for an honest condition and there isn't one. "If you
added more top end" would be a different deck; "if games got faster" doesn't fix
the four clean targets or the turn-one uncastability.

## What I'd point at instead

**The role Culling aims at is not a real gap** — 35 lands + 7 nonland mana sources
against a 2.85 average MV is already generous. So there is no counter-proposal for
*this* role; suggesting one would be inventing a problem.

The gap the audit found is still open and still unanswered: **board recovery after
a wipe**. That verdict was **ADD IF wipes are actually happening**, and it hinges
on one number I still don't have. If your board gets wiped in most games,
**Patriarch's Bidding** ($3.92 as of 2026-08-31) or the one-sided **Immortal
Servitude** ($0.42) is the best card not in this deck — but note the audit's own
withdrawal: Farewell *exiles*, so Bidding has nothing to return against it, and
against mono-type tribal opponents its symmetry is fully live. If wipes are rare,
that stays a no too, and the deck is genuinely close to done.

**The one open question:** roughly how often does your board actually get wiped?
That answers a live ADD IF. Nothing about Culling the Weak turns on it.
