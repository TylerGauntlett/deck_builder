# markov_chains — Door of Destinies, 2026-08-31

**Verdict: NO.** It is the seventh anthem into a category already six deep, it
serves only the aggro half of a dual-mode deck, and the deck has zero trample to
convert the power it grants.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line.

**Meta as corrected in the 2026-08-30 and 2026-08-31 reviews, which this review
adopts:** games in this pod run **long**; several opponents play **mono-white**,
both token swarms and big-creature builds; **Farewell and Armageddon are commonly
played**; and the deck is **dual-mode** — Edgar resolved turns it into aggro with
large creatures via his attack trigger, Edgar absent turns it into an aristocrats
slow-bleed, bridged by the +1/+1 counter package.

All oracle text, legality, colour identity and prices fetched from Scryfall
2026-09-01 00:53–00:56 UTC. Composition counted from
`decks/markov_chains/cards.json` (built 2026-08-31, current with `base.txt` —
`cards.md` mtime 16:02 vs `base.txt` 10:17). EDHREC from
`commanders/edgar-markov`, n = 50,144, and its Anthems theme, n = 110. Combos via
Commander Spellbook `find-my-combos`.

**I did not pressure-test the speed premise, because this rejection does not rest
on it.** The established long-game meta is the *strongest* version of the case for
Door of Destinies, and the analysis below grants it in full. Nothing here says
"too slow."

---

## The card, verified

```
Door of Destinies  {4}
  Artifact
  As this artifact enters, choose a creature type.
  Whenever you cast a spell of the chosen type, put a charge counter on this artifact.
  Creatures you control of the chosen type get +1/+1 for each charge counter on this artifact.
```

Mana value 4 · colourless · Commander legal · EDHREC rank 1078 ·
**$2.63** (fetched 2026-09-01 00:53 UTC).

Rulings fetched. The relevant one: *"If you cast a creature spell of the chosen
type, Door of Destinies will get a charge counter before the creature enters. The
creature will enter with the additional boost."* — so it is not a turn behind on
its own triggers. Granted.

## Step 0 — the honest best case

**Claim, stated so it could be false:** *Door of Destinies is the only anthem in
the deck whose size is unbounded — with 34 castable Vampire spells in the 99 plus
Edgar himself, in a pod where games run long it plausibly settles at +4/+4 to
+6/+6, more than double the deck's largest static anthem (Lord of Lineage, +2/+2);
and as an artifact it survives the creature wraths the 2026-08-31 structural audit
named as this deck's single biggest weakness.*

That is a real case. Both halves are true as stated. The density is genuinely
there — 35 Vampire-typed cards including the commander:

> Indulgent Aristocrat · Master of Dark Rites · Vampire of the Dire Moon · Viscera
> Seer · Blood Artist · Bloodghast · Bloodthrone Vampire · Charismatic Conqueror ·
> Cordial Vampire · Cruel Celebrant · Legion Lieutenant · Captivating Vampire ·
> Clavileño · Florian · Forerunner of the Legion · Marauding Blight-Priest · Qarsi
> Revenant · Stromkirk Captain · Vito · Welcoming Vampire · Baron Bertram
> Graywater · Bloodletter of Aclazotz · Bloodline Keeper · Edgar Charmed Groom ·
> Elenda · Henrika Domnathi · Sanctum Seeker · Vampire Nocturnus · Anowon ·
> Bloodthirsty Conqueror · High-Society Hunter · Malakir Bloodwitch · Edgar Markov
> · Patron of the Vein · Vein Ripper

Now the attack.

## 1. It serves one of the deck's two modes, and not the one that closes games

The deck's damage overwhelmingly comes from triggers that count **events**, not
power. Grouped by trigger scope, since the scope is the whole point:

**Fire on *any* creature dying (2):**
- Blood Artist — "Whenever **this creature or another creature** dies, target
  player loses 1 life and you gain 1 life."
- Vein Ripper — "Whenever **a creature** dies, target opponent loses 2 life and
  you gain 2 life."

**Fire only on *your* creatures dying (3):**
- Cruel Celebrant — "another creature or planeswalker **you control**"
- Zulaport Cutthroat — "another creature **you control**"
- Bastion of Remembrance — "a creature **you control** dies"

**Other event-counters (5):**
- Sanctum Seeker — "Whenever a Vampire you control **attacks**, each opponent
  loses 1 life." Counts *attackers*, not their power.
- Mirkwood Bats — "Whenever you **create or sacrifice a token**"
- Marauding Blight-Priest — "Whenever you gain life"
- Vito — lifegain → life loss
- Bloodletter of Aclazotz — "If an opponent would lose life **during your turn**,
  they lose twice that much." A doubler on all of the above, on your turn only.

**Ten drain payoffs. Zero of them read power.** Door of Destinies adds nothing to
any of them. In the aristocrats mode — the mode the deck defaults to whenever
Edgar is answered — Door is a blank.

This is failure mode 7 from the rubric run in reverse: the candidate is being
graded generously against one mode. Scored against both, it contributes to one and
literally nothing to the other. Compare the bridge cards, which serve both: Cordial
Vampire (deaths → counters on every Vampire), Indulgent Aristocrat (sac → counters
on every Vampire), Patron of the Vein, Elenda, Blade of the Bloodchief, Edgar's
attack trigger. Door bridges nothing.

## 2. Zero trample in the deck

Checked across all 91 distinct cards in `cards.json`: **`trample` appears zero
times.** Fourteen cards reference flying, but those are individual bodies
(Bloodline Keeper, Bloodletter, Malakir Bloodwitch, Patron of the Vein, Vein
Ripper, Qarsi Revenant, Welcoming Vampire, High-Society Hunter, Nocturnus
conditionally, Mirkwood Bats, Henrika, Clavileño, Bloodthirsty Conqueror, plus
Akroma's Will granting it for a turn).

Against the mono-white **token swarms** this pod is known to run, a wide ground
board at +5/+5 gets chump-blocked by 1/1s all day. Raw power without trample is
the least efficient damage this deck can buy, and it is exactly and only what Door
of Destinies sells. The flyers that *do* get through are already receiving six
anthems.

## 3. The anthem category is the deck's deepest — this is additive, not multiplicative

Static Vampire anthems already in the 99, all text verified this session:

| Card | Cost | Effect |
|---|---|---|
| Legion Lieutenant | `{W}{B}` | Other Vampires you control get +1/+1 |
| Captivating Vampire | `{1}{B}{B}` | Other Vampire creatures you control get +1/+1 |
| Stromkirk Captain | `{1}{B}{R}` | Other Vampire creatures get +1/+1 **and first strike** |
| Edgar, Charmed Groom | `{2}{W}{B}` | Other Vampires you control get +1/+1 |
| Lord of Lineage (Bloodline Keeper flipped) | `{2}{B}{B}` | Other Vampire creatures get **+2/+2** |
| Vampire Nocturnus | `{1}{B}{B}{B}` | +2/+1 **and flying** while top card is black |

Six. On top of that, a permanent-counter package doing the same job durably:
Edgar Markov's attack trigger ("put a +1/+1 counter on **each Vampire you
control**"), Cordial Vampire, Indulgent Aristocrat, Patron of the Vein, Elenda,
Blade of the Bloodchief.

The rubric's closing filter: *prefer the card that multiplies what the deck
already does over the card that adds one more of something.* Door of Destinies
looks multiplicative because it grows, but it grows **inside** the anthem
category, stacking additively with six effects already there. The genuinely
multiplicative cards in this list are Bloodletter of Aclazotz (damage doubler) and
Mirkwood Bats (token count → damage). Door is the seventh copy of the deck's most
redundant effect.

## 4. It doesn't trigger eminence, and it isn't a body

Edgar Markov, verified: *"Eminence — Whenever you cast another **Vampire spell**,
if Edgar is in the command zone or on the battlefield, create a 1/1 black Vampire
creature token."*

Door of Destinies is an **artifact** spell. Casting it produces no token. Every one
of the five creature anthems above produces one. So the real comparison at four
mana is not "anthem vs. anthem" — it is "anthem" versus "anthem + a 3/3 or 4/4
body + a free 1/1 Vampire token + a creature that can block, be sacrificed, and
trigger all five death-drains."

Door also cannot be sacrificed to Viscera Seer, Carrion Feeder, Bloodthrone
Vampire, Indulgent Aristocrat or High-Society Hunter, and triggers none of the
death drains when it dies.

## 5. The counters come from *casting*, and the deck's main Vampire source isn't cast

*"Whenever you **cast a spell** of the chosen type, put a charge counter."*

Edgar's eminence tokens are **created**, not cast. Baron Bertram's tokens, Bloodline
Keeper's tokens, Edgar Markov's Coffin's upkeep tokens, Elenda's death tokens —
none of them add a counter. The deck's largest engine for putting Vampires on the
battlefield contributes zero to Door's growth, while every one of the six existing
anthems buffs those tokens immediately on arrival. Door enters at **+0/+0** and
buys its size on credit.

## 6. The four-slot is the deck's most contested

Twelve nonland cards at MV 4 already, against a curve of 13/15/17/**12**/5/3:

> Akroma's Will · Baron Bertram Graywater · Bloodletter of Aclazotz · Bloodline
> Keeper · Clever Concealment · Edgar Charmed Groom · Elenda · Grave Pact ·
> Henrika Domnathi · Mirkwood Bats · Sanctum Seeker · Vampire Nocturnus

Door would be the thirteenth, and the only one of the thirteen that changes
nothing about the board on the turn it resolves.

## 7. The wrath-resilience case is answered by the specific wrath in this pod

The best structural argument for Door is that it survives a board wipe. But the
user has stated **Farewell is commonly played in this pod**, and Farewell exiles
artifacts. And even when it does survive: Door does not rebuild a board, it
enlarges one. Post-wipe you have an artifact with counters and no creatures, and
the thing that actually saves the deck from a wrath is mass recursion — the hole
the structural audit identified and which is still open.

## Disagreement check

- **EDHREC, Edgar Markov (n = 50,144):** Door of Destinies in **8,830 decks =
  17.6%**.
- The six anthems this deck runs sit at 82.4% (Captivating Vampire), 74.5%
  (Stromkirk Captain), 69.2% (Legion Lieutenant), 68.8% (Bloodline Keeper), 55.6%
  (Edgar Charmed Groom) inclusion.
- On Edgar's **Anthems** theme page (n = 110) — the page whose entire top-10 and
  high-synergy-10 this deck already runs, missing only Drana — Door of Destinies
  **does not appear at all**.

So I am siding with the community's majority here, not against it, and the
independent reason is section 3: this particular Edgar list already runs every
anthem EDHREC rates above Door, plus a six-card permanent-counter package on top.

## Combos

`combos.py markov_chains --add "Door of Destinies" --near`: baseline 2 combos
assembled, **0 newly completed, 0 newly within reach.** No bracket-3 veto concern
in either direction.

## Price

**$2.63** (fetched 2026-09-01 00:53 UTC), against a $40/card cap. Price was not
load-bearing anywhere above. **This rejection survives the card being free** — the
cost that sinks it is the card slot and the four mana, not the dollars.

## Cut discipline — no cut was found, and that is the finding

I never reached step 6, because nothing in the deck is worse. The two cards
closest to cuttable at MV 4, and why each was spared:

- **Baron Bertram Graywater** ($0.35) — *"Whenever one or more tokens you control
  enter, create a 1/1 black Vampire Rogue creature token with lifelink. This
  ability triggers only once each turn. {1}{B}, Sacrifice another creature or
  artifact: Draw a card."* A Vampire spell (triggers eminence), a 3/4 body, a
  repeatable sac outlet, a card-draw engine, and a token multiplier that feeds
  Mirkwood Bats. Spared on four counts.
- **Mirkwood Bats** ($1.09) — *"Whenever you create or sacrifice a token, each
  opponent loses 1 life."* The multiplicative token-count-to-damage converter; the
  rubric's own example of the kind of card that survives scrutiny. Spared.

Per the rubric: *"If the best cut you can find is a card you would defend in any
other context, that is strong evidence the addition isn't worth it."* Both of
these are cards I would defend anywhere.

## No counter-proposal

The rubric asks for one when the role is real but the card is wrong. Here the role
— "make my Vampires bigger" — is the **single most saturated category in the
deck**: six static anthems plus six permanent-counter sources. There is no gap to
counter-propose into.

The genuinely open observation, offered as an observation and not a
recommendation: **the deck has zero trample.** That is the reason a seventh anthem
does not convert, and it is a more interesting question than which anthem to add.
I searched `id<=wbr o:"creatures you control" o:trample f:commander usd<40` (46
matches) and found nothing clean — the results are overwhelmingly red-weighted,
and this deck runs **5 red pips against 63 black and 15 white**. Bleeding Effect
(`{2}{W}{B}`, $0.30) looked like a fit until read closely: it grants trample only
*"if a creature card in your graveyard has trample"* — with zero trample in the
99, it can never grant it. Not a fit either. If the aggro mode's damage conversion
is worth a separate look, that is its own review.

## Verdict

**NO** — the seventh anthem in a deck that already runs six, contributing nothing
to the ten event-counting drain payoffs that actually close its games, with no
trample in the deck to convert the power it does grant.

---

### Figures recorded for later comparison

| Item | Value | Source / timestamp |
|---|---|---|
| Door of Destinies price | $2.63 | Scryfall, 2026-09-01 00:53 UTC |
| Door of Destinies, Edgar inclusion | 8,830 / 50,144 = 17.6% | EDHREC `commanders/edgar-markov` |
| Door of Destinies, Edgar Anthems theme | absent from top-10 and high-synergy-10 | EDHREC Anthems, n = 110 |
| Door of Destinies EDHREC rank | 1078 | Scryfall, 2026-09-01 |
| Combos newly completed | 0 (baseline 2) | Commander Spellbook, 2026-09-01 |
| Vampire-typed cards in deck | 35 incl. commander (34 in the 99) | `cards.json`, built 2026-08-31 |
| Static Vampire anthems in deck | 6 | `cards.json` |
| Event-counting drain payoffs | 10 (2 any-creature, 3 yours-only, 5 other) | `cards.json` |
| Trample references in deck | 0 | `cards.json` |
| Nonland curve | 13 / 15 / 17 / 12 / 5 / 3 at MV 1–6 | `cards.json` |
| Coloured pips | B 63 · W 15 · R 5 | `cards.md` |
