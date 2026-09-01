# markov_chains — Teferi's Protection, 2026-08-31

Candidate proposed: **Teferi's Protection**. One card, one slot.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line.

**Meta premise carried forward** from the 2026-08-30 review (Addendums 2 and 6)
and the 2026-08-31 structural audit: games in this pod run **long**, several
opponents play **mono-white**, and the deck is **dual-mode** (Edgar resolved →
aggro; Edgar absent → aristocrats slow-bleed). Nothing in this review depends on
the *speed* line of `meta.json`, so it is not re-litigated here. The one premise
this review does lean on — **how often a wipe actually resolves** — is still the
open question from the structural audit and is still unanswered. It is flagged
where it bites.

All oracle text, rulings, legality, colour identity and prices fetched from
Scryfall via `card_facts.py` on **2026-08-31 13:34–13:37 UTC**. Composition,
curve and colour sources counted from `decks/markov_chains/cards.json`
(built 2026-08-30 23:56; `cards.md` is newer than `base.txt`, so no rebuild).

---

## Verdict: **NO** — ⚠️ SUPERSEDED, see Addendum 1

> **This verdict was reversed later the same day.** The user supplied three pod
> facts — Farewell is common, opponents play single-type tribal, and **Armageddon
> is common** — and the third inverts §3b below: phasing out your own lands is not
> a cost against Armageddon, it is the whole card. **Revised verdict: ADD.**
> Patriarch's Bidding is withdrawn.
>
> **Addendum 2** then syncs the deck from Moxfield, which had moved on: the cut
> named in Addendum 1 (Orzhov Basilica) is **already gone**, so the current cut is
> **Vicious Conquistador**.
>
> Read §1–§6 for the verified card facts, then Addendum 1 for the reversal and
> **Addendum 2 for the current recommendation against the current 100**.

It is a great card. It is not a card this deck's 100 has room for, and the
version of it that this deck actually wants costs $4.70 and is called
**Clever Concealment**.

Price is stated separately below and is **not** the reason. The rejection
survives the card being free — see "Would I run it at $0?".

---

## 1. The card, verified

    Teferi's Protection  {2}{W}  Instant
      Until your next turn, your life total can't change and you gain protection
      from everything. All permanents you control phase out.
      Exile Teferi's Protection.

- Mana value 3 · Colour identity **W** → **legal** in Edgar Markov's WBR identity.
  No colour-identity veto.
- **Game Changer: yes.** The deck currently runs **0** Game Changers
  (counted over `game_changer` in `cards.json`); bracket 3 permits 3. So there
  is no bracket veto either — this would be 1 of 3.
- `combos.py --add "Teferi's Protection"` → **0 new combos**. Baseline stays at
  the two late-game Bloodthirsty Conqueror lifegain loops. The
  no-early-infinites veto is not engaged.
- EDHREC: **31.4%** of 50,082 Edgar decks, synergy **+0.13**. It is the single
  most-played Game Changer on the Edgar page — and see §5 for why that number
  means less than it looks.

Nothing here stops the evaluation. It has to be decided on merit.

## 2. Steel-man — the strongest honest case for it

This is the most complete "I do not lose this turn" card in Magic, and three
things about *this* deck make that argument better than it would be elsewhere:

1. **The deck cannot rebuild.** The structural audit's Finding 1 stands: grepping
   every oracle face in `cards.json` for `graveyard` returns exactly two hits —
   **Bloodghast** (returns *itself*) and **Bojuka Bog** (graveyard hate, pointed
   outward). There is **zero** recursion of another creature. With **37
   creatures** and no non-creature win, a resolved wrath is close to a loss.
2. **Akroma's Will covers less than it appears to.** Verified text: *"Choose one.
   If you control a commander as you cast this spell, you may choose both
   instead."* Edgar's eminence works from the command zone, which is where he
   spends most games — so you usually get **one** mode, not both. And the
   protection mode ("lifelink, indestructible, and protection from each color")
   answers destruction and coloured damage but **does not** answer Toxic Deluge
   (-X/-X kills through indestructible), edicts and sacrifice effects, or
   exile-based wipes like Farewell. Teferi's Protection answers all of them.
   The audit's line *"the gap is recovery, not prevention"* was overstated on
   this point and I am tightening it here.
3. **You are frequently the archenemy.** A go-wide drain deck in a long
   four-player game draws the table. Protection from everything plus a life
   total that can't change is the button that survives the turn three people
   decide it is your turn to die — and Akroma's Will does not do that at all,
   because protection from each *color* does not stop a colourless source or a
   life-total-set effect.

That is a real case. Now the attack.

## 3. Why it fails anyway

### 3a. The mana requirement fights the deck's whole shape

Curve from `cards.json`: **1→13 · 2→14 · 3→16 · 4→12 · 5→5 · 6→2**, average
nonland MV **2.83**. This is the widest, lowest curve in the list and its plan is
to deploy a threat every turn and attack. Teferi's Protection is only ever good
with **three mana held open on an opponent's turn**, every turn, from the turn
you draw it.

A deck with 13 one-drops and 14 two-drops does not have those turns spare. The
turns where you *can* comfortably hold three up are the late turns — which are
exactly the turns you are least likely to still be holding it, because you drew
it eight turns ago and had nothing to do with it.

This is the objection Clever Concealment answers and Teferi's Protection cannot
(§6).

### 3b. It phases out your lands, so you are locked out for a full turn cycle

Verified ruling: *"While a permanent is phased out, it's treated as though it
doesn't exist… its triggered abilities can't trigger."* **All** your permanents
phase out, lands included. For the rest of that turn and every opponent's turn
until your untap step, you have:

- **No mana.** Swords to Plowshares, Lightning Bolt, Crackling Doom, Anguished
  Unmaking, Feed the Swarm, Malakir Rebirth — every piece of instant-speed
  interaction in the deck is uncastable. You are protected and completely inert
  while three opponents take free turns.
- **No aristocrats triggers.** Blood Artist, Cruel Celebrant, Zulaport Cutthroat,
  Bastion of Remembrance and Mirkwood Bats do not exist, so opponents' creatures
  dying during that window drains nobody.

### 3c. It turns off the deck's own engine

Three verified triggers, all keyed on life *changing*, all dead while your life
total can't change (ruling: *"Spells and abilities that would normally cause you
to gain or lose life still resolve while your life total can't change, but the
life-gain or life-loss part simply has no effect"*):

| Card | Clause | Effect under Teferi's Protection |
|---|---|---|
| **Vito, Thorn of the Dusk Rose** | "Whenever **you gain life**, target opponent loses that much life." | never triggers — you cannot gain life |
| **Marauding Blight-Priest** | "Whenever **you gain life**, each opponent loses 1 life." | never triggers |
| **Bloodthirsty Conqueror** | "Whenever an opponent loses life, **you gain that much life**." | resolves, gains nothing; and it feeds Vito/Blight-Priest nothing |

**Sanctum Seeker** ("each opponent loses 1 life **and** you gain 1 life") still
drains — the opponent's half is unaffected — but the gain half, and therefore
the Vito/Blight-Priest chain hanging off it, is off.

This is a one-turn-cycle cost, not a permanent one, and I am not pretending it is
the main objection. It is the tiebreaker: the deck's two assembled combos and its
whole slow-bleed mode run on life *changing*, and this card's cost line is "your
life total can't change."

### 3d. It does nothing, ever, to advance the game

Zero board, zero cards, zero damage, and it exiles itself. Compare the card it
would sit beside: **Akroma's Will** is *also a finisher* — "flying, vigilance,
and double strike" on a wide Vampire board with Edgar's +1/+1 attack trigger
ends games outright. That is why Akroma's Will earns a slot in a 63-nonland list
and a pure insurance policy has to clear a much higher bar.

### 3e. Not a Vampire

`meta.json` lists on-theme Vampires as a **tiebreaker only**, so this is not a
veto — but every three-mana Vampire spell in this deck also makes a 1/1 off
eminence. This one makes nothing.

### 3f. It spends a third of the bracket's power headroom on pure defence

0 of 3 Game Changers used today. That headroom is real and it is worth
something; a card that never wins a game is a strange thing to spend it on when
the same page lists Demonic Tutor, Smothering Tithe and Bolas's Citadel. (Not a
recommendation of any of those — I have not evaluated them, and the tutors sit
close to the no-tutor-dependent-win-line veto.)

## 4. Would I run it at $0?

Asked deliberately, because the price is disqualifying on its own and I do not
want that doing the work.

**No — but it is close.** At zero cost it is a defensible 100th card in a deck
that could not otherwise survive a wrath. It still loses the slot to
Clever Concealment, which is better *in this deck specifically* for the reasons
in §6, and it still forces a cut of a card that does something on a normal turn.
Nothing in §3 is a price argument.

## 5. What the EDHREC number actually says

31.4% inclusion looks like an endorsement. The number beside it is the tell:
**synergy +0.13**. Compare the deck's high-synergy core — Captivating Vampire
+0.72, Cordial Vampire +0.71, Blood Artist +0.64. A synergy of +0.13 means
"white decks in this bracket range play this card," not "Edgar decks want this
card." It is the generic-staple signature. Note also that EDHREC's Edgar sample
is 3,954 bracket-4 and 169 bracket-5 decks out of 50,082; the Game Changers
panel is weighted toward exactly the tables this deck is not sitting at.

Its per-card EDHREC page **could not be fetched** — the script's URL handling
403s on the apostrophe, the same failure the audit hit on Patriarch's Bidding.
No Edgar-specific inclusion figure beyond the commander-page number is quoted.

## 6. Counter-proposal — the role is real, the card is wrong

**Clever Concealment** `{2}{W}{W}` Instant, **$4.70** (fetched 2026-08-31 13:36 UTC):

> Convoke. *Any number of target nonland permanents you control phase out.*

Against Teferi's Protection, in **this** deck:

| | Teferi's Protection | Clever Concealment |
|---|---|---|
| Saves the board from a wrath | yes | yes |
| Beats exile wipes / Toxic Deluge / edicts | yes | yes |
| **Leaves your lands up** | **no** — you are inert for a turn cycle | **yes** — you keep mana and can still cast Swords, Bolt, Crackling Doom |
| **Real mana cost with a wide board** | 3, always, held open | 4 nominal; **convoke** taps your tokens, so often just `{W}{W}` |
| Turns off Vito / Blight-Priest / Conqueror | yes | no |
| Protects **you** from lethal damage or a combo kill | **yes** | no |
| Game Changer slot | 1 of 3 | none |
| Price | $49.02 | $4.70 |

§3a is the objection that decides this. Convoke is the answer to "a deck with 13
one-drops cannot hold three mana open" — you cast it *with the board you are
protecting*, and creatures tapped for convoke phase out and phase back in able
to attack (verified ruling: permanents phasing in "will be able to attack and pay
a cost of {T} during that turn"). Counters are preserved on phase-in too, which
matters with Cordial Vampire, Indulgent Aristocrat and Edgar's attack trigger.

**The honest cost of the swap:** Clever Concealment does not protect *you*, only
your permanents. The archenemy scenario in §2.3 — three opponents pointing lethal
at your face — is the one thing Teferi's Protection does that Concealment does
not. If that is the loss you actually keep experiencing, rather than losing the
board to a wipe, then my counter-proposal misses and you should say so.

**Mana caveat, verified:** `{W}{W}` is a real ask here. White has **18 land
sources** (of 37 lands) plus Arcane Signet, Talisman of Conviction and Talisman
of Hierarchy = **21 total** — but the audit's Finding 2 also established that
**no card currently in the deck needs two white pips**, so this would be the
first. Convoke does not fix it: eminence tokens are **black** 1/1 Vampires and
pay only `{1}`, and only 8 creatures in the deck are white-costed (Baron Bertram
Graywater, Clavileño, Cruel Celebrant, Edgar, Elenda, Forerunner of the Legion,
Legion Lieutenant, Welcoming Vampire). So the realistic cast is "tap two tokens,
pay `{W}{W}` from lands."

### Cut, if you take it

The structural audit named **Orzhov Basilica** ($0.29) as the cut for any add:
enters tapped **and** bounces a land, in a deck with 13 one-drops and 14
two-drops, to fix colours that are already over-fixed. That still holds and takes
the deck to 35 lands / 65 nonland cards.

If you also take Patriarch's Bidding, the two adds need two cuts and Basilica
only covers one. Second cut: **Unexplained Absence** `{3}{W}` (EDHREC rank 6671,
the most obscure card in the deck) — it exiles one nonland permanent per player
but hands each of them a cloaked 2/2, i.e. gives 2/2s to the mono-white token
decks you are trying to beat. Runner-up: **Vicious Conquistador** (`{B}` 1/2,
"Whenever this creature attacks, each opponent loses 1 life" — spared in the
2026-08-30 review purely as a turn-one Vampire body, and that reason still
holds, which is why it is third and not second).

### Clever Concealment vs. Patriarch's Bidding

Both answer the audit's Finding 1 from opposite ends, and they are not
redundant with each other:

- **Bidding** ($3.81, `{3}{B}{B}` sorcery) is *recovery*: reliable — it works
  whenever you draw it, no mana held, no timing — but symmetric, dead in an
  opening hand, dead against exile wipes, and it makes the deck's fifth card at
  MV 5.
- **Concealment** is *prevention*: one-sided, far cheaper in practice, and it
  answers exile wipes that Bidding cannot — but it must be in hand at the exact
  moment.

**If you are buying one, I would now take Clever Concealment**, on the strength
of the one-sidedness and the convoke cost. That is a change of ranking from the
audit, and the reason it changed is §2.2: I had credited Akroma's Will with more
prevention coverage than it actually has, which made "the gap is recovery, not
prevention" too strong a statement.

**Both remain ADD IF**, on the audit's still-open condition: **does a wrath
actually resolve in most of your games, or is it a once-in-a-while thing?** If
it is rare, both are dead cards and the answer to all of this is no.

## 7. Summary

| Card | Price (2026-08-31 13:34–13:37 UTC) | Verdict |
|---|---|---|
| **Teferi's Protection** | $49.02 (**over the $40 cap**) · Game Changer | **NO** — a held-open 3 mana with no board impact, in a 2.83-MV deck that spends its mana; phases out your own lands and switches off Vito / Marauding Blight-Priest / Bloodthirsty Conqueror for a turn cycle. Rejection stands at $0. |
| **Clever Concealment** | $4.70 | **ADD IF** wipes are frequent — cut **Orzhov Basilica** |
| Patriarch's Bidding | $3.81 | **ADD IF** wipes are frequent — second cut **Unexplained Absence** |

## 8. What I am unsure about, and what would settle it

- **Wipe frequency.** Unchanged from the audit and still the hinge for the
  counter-proposals. A wrath in most games → Concealment is the best card not in
  this list. Once in ten → flat no to all three.
- **Which loss you are actually taking.** If you are dying to *lethal aimed at
  your face* rather than to *wraths*, Teferi's Protection is the only card here
  that fixes it, and I would want to re-run this with that as the stated premise.
  That is a genuinely different axis and it would move the verdict.

## Sources

- Scryfall via `card_facts.py lookup`, fetched **2026-08-31 13:34–13:37 UTC**:
  Teferi's Protection $49.02 (foil $60.31, Game Changer, EDHREC rank 109, W
  identity, legal) · Clever Concealment $4.70 · Patriarch's Bidding $3.81 ·
  Unbreakable Formation $1.54 · Akroma's Will $14.62 · Vito $11.73 ·
  Bloodthirsty Conqueror $38.09 · Marauding Blight-Priest $0.32 · Sanctum Seeker
  $0.35 · Malakir Bloodwitch $4.72 · Indulgent Aristocrat $0.30 · Edgar Markov
  $42.28 · Vault of the Archangel $0.77 · War Room $5.57 · Orzhov Basilica $0.29 ·
  Unexplained Absence $0.43 · Vicious Conquistador $0.33.
- Teferi's Protection official rulings (2017-08-25) via `--rulings`, quoted
  inline in §3b and §3c.
- EDHREC `commanders/edgar-markov`, n = 50,082 (brackets 1→91, 2→3,540, 3→5,308,
  4→3,954, 5→169). Teferi's Protection 31.4% / synergy +0.13, top of the Game
  Changers panel. The per-card page `edhrec.py card "Teferi's Protection"`
  **failed with HTTP 403** on the apostrophe in the URL — same script bug the
  audit hit on Patriarch's Bidding.
- Commander Spellbook via `combos.py markov_chains --add "Teferi's Protection"`:
  baseline 2 assembled, **0** newly completed.
- Composition, curve, colour sources, Game Changer count and white-creature count
  computed from `decks/markov_chains/cards.json`.
- Minor correction to the 2026-08-31 audit: Vicious Conquistador is a **1/2**,
  not a 1/1. Changes nothing.

`base.txt` was not modified.

---

# Addendum 1 — three pod facts, and a reversal (2026-08-31, same day)

After the verdict above, the user supplied three facts about the pod. All three
bear on this card, one of them **inverts a clause I had scored as a liability**,
and together they **reverse the verdict**.

Stated by the user, in order:

1. **Farewell is common** in their games.
2. **Several opponents play single-type tribal** decks — every creature a Dragon,
   every creature a Human, and so on.
3. **Armageddon is commonly played.**

All card text below fetched from Scryfall via `card_facts.py` on
**2026-08-31 13:45–13:47 UTC**.

## The three threats, verified

| Card | Cost | Text |
|---|---|---|
| **Farewell** | `{4}{W}{W}` Sorcery | "Choose one or more — • Exile all artifacts. • Exile all creatures. • Exile all enchantments. • Exile all graveyards." |
| **Armageddon** | `{3}{W}` Sorcery | "Destroy all lands." |

## What the deck currently has against them: nothing

Re-checked against verified text, not memory:

- **Akroma's Will** — indestructible does not stop **exile**, and protection from
  each *color* does not stop a non-targeting "exile all creatures." Blank against
  Farewell. Blank against Armageddon (it does not affect lands at all).
- **Malakir Rebirth** — verified: *"that creature gains 'When this creature
  **dies**, return it to the battlefield tapped.'"* Exile is not dying. Blank
  against Farewell. Blank against Armageddon.
- Recursion: still the two hits from the audit — Bloodghast (itself) and Bojuka
  Bog (outward-facing hate). And Farewell's fourth mode exiles all graveyards,
  so even that is answerable.

**Against the two wipes the user actually names, this deck has zero outs today.**

## The clause I read backwards

My §3b was: *"It phases out your lands, so you are locked out for a full turn
cycle"* — filed as a cost.

Against **Armageddon**, that clause is the entire card. Phased-out permanents are
*"treated as though they don't exist"* (verified ruling), so a phased-out land is
not there to be destroyed. You respond to Armageddon by tapping the lands you are
about to phase out, and you untap with your **whole mana base and your whole
board** while three opponents have zero lands. In a 37-creature go-wide deck that
is not survival, it is the game.

That also collapses §3d ("it does nothing, ever, to advance the game"). Against
Armageddon it is the most game-advancing card this deck could be holding.

I scored a scope clause as a downside without checking what it answers. The user
named the format that inverts it. Verdict moves.

## Coverage, re-run across all four threats

| | Teferi's Protection | Clever Concealment |
|---|---|---|
| Farewell (exile creatures / artifacts / enchantments) | **yes** | **yes** |
| **Armageddon (destroy all lands)** | **yes** | **no** — "any number of target **nonland** permanents you control" |
| Conventional destroy-all-creatures wrath | yes | yes |
| Lethal damage aimed at you / a combo kill | **yes** | no |

Clever Concealment answers two of four. Teferi's Protection answers four of four.
The `nonland` word in Concealment's oracle text is what separates them, and
Armageddon is precisely the card that word was written to exclude.

## The objections that survive, honestly

- **§3a (holding mana)** — still real, but smaller than I made it. Armageddon
  costs 4 and Farewell costs 6, so the window that matters starts around turn 5–6,
  when this deck has six-plus lands and can deploy a two-drop *and* hold three up.
  My framing ("hold three open from the turn you draw it") overstated it.
- **§3c (engine off for a turn cycle)** — unchanged and verified: Vito, Marauding
  Blight-Priest and Bloodthirsty Conqueror all key on life changing and all go
  quiet. Still a genuine cost. Against a resolved Armageddon it is irrelevant.
- **§3e (not a Vampire, no eminence trigger)** — unchanged, tiebreaker only.
- **§3f (a Game Changer slot)** — unchanged. It would be 1 of 3, and 0 are used.

None of these outweigh "answers the two wipes you say you keep facing, and nothing
else in the 99 does."

## Revised verdict: **ADD** — cut **Orzhov Basilica**

On gameplay merit, at any price. §4 of the original review asked "would I run it
at $0?" and answered "no, but close"; on the corrected reading the answer is
plainly yes.

**Price, stated separately as its own factor and not as part of the case:
$49.02** (fetched 2026-08-31 13:34 UTC) against a **$40/card cap** in
`meta.json` — over by $9.02. That cap is the user's rule and waiving it is the
user's call. It is the only thing between this card and an unconditional add;
nothing in the gameplay analysis turns on it.

**The cut is Orzhov Basilica** ($0.29), unchanged from the structural audit's
Finding 3: enters tapped **and** bounces a land, in a deck with 13 one-drops and
14 two-drops, fixing colours Finding 2 showed are already over-fixed. Deck goes
to 35 lands / 65 nonland cards. No spell is cut.

A note on that cut under an Armageddon meta: the instinct is "keep lands." It is
wrong here. Post-Armageddon everyone rebuilds from zero, and what matters is curve
— this deck has average nonland MV **2.83** with 13 one-drops and eminence working
from the command zone with no board at all, so it rebuilds faster than almost
anything. A land that enters tapped and *returns another land to your hand* is the
worst possible card in that rebuild.

## Reversal: **Patriarch's Bidding is withdrawn** — now a flat NO

The structural audit's headline recommendation. Facts 1 and 2 kill it
independently:

- **Farewell exiles.** Verified: "Exile all creatures," and a fourth mode "Exile
  all graveyards." Bidding returns creature *cards from graveyards*. Against the
  wipe the user actually faces, there is nothing to return — and the caster can
  exile the graveyards too, on the same card, for free.
- **The pod is single-type tribal.** Verified Bidding text: *"**Each player**
  chooses a creature type. **Each player** returns all creature cards of a type
  chosen this way from their graveyard to the battlefield."* The audit argued the
  symmetry was near-free because mono-white *token* decks get little back — tokens
  never become graveyard cards. That argument does not survive fact 2. An
  all-Dragons or all-Humans opponent names their one type and returns their
  **entire** creature graveyard, exactly as completely as you return yours, and
  their creatures are individually bigger than your 1/1s.

Two independent reasons, both from user-supplied facts. Bidding is off the list.

## Clever Concealment: still a good card, now the second pick

**$4.70**, `{2}{W}{W}` instant with convoke. It remains the better card against
Farewell specifically — it keeps your lands *and* your mana up so you can still
interact, it preserves +1/+1 counters and tokens on phase-in (verified rulings:
counters are kept, and "if a token is phased out, it will phase in"), and it
covers the **9 artifacts and 4 enchantments** in the list that Farewell's other
modes exile. Blink-style alternatives do not: Eerie Interlude ($7.17), Ghostway
($5.57) and Semester's End ($1.27) all *exile and return*, which makes new
objects — **your tokens are gone permanently and every +1/+1 counter is wiped**.
In an eminence deck whose board is mostly countered-up 1/1 tokens, that rules all
three out.

But it reads `nonland`, so it does nothing about Armageddon.

**Verdict: ADD IF you want a second wipe answer** — one card in 99 is thin
insurance against two commonly-played wipes, and this is the right second card.
Second cut: **Unexplained Absence** (`{3}{W}`, EDHREC rank 6671, hands each
opponent a cloaked 2/2). Take Teferi's Protection first; this is redundancy, not
a substitute.

**Convoke caveat, verified:** the deck has **zero creatures with vigilance**
(checked `keywords` across all 37 creatures in `cards.json`), so anything that
attacked is tapped through all three opponents' turns. Convoke fuel is the
eminence tokens made on your own turn and any creatures you held back — real, but
not guaranteed. And eminence tokens are **black**, so they pay only `{1}`; the
`{W}{W}` comes from lands (18 white land sources of 37).

## One free upside from fact 2

**Anowon, the Ruin Sage**, already in the deck — verified: *"At the beginning of
your upkeep, each player sacrifices a non-Vampire creature **of their choice**."*
Against all-Dragon and all-Human opponents, **every** creature they control is a
legal sacrifice and none of yours are (34 of 37 creatures are Vampires, and
eminence tokens are Vampires). Reading the "who chooses" axis honestly: they pick
their worst one, so it is a grind, not a blowout — and it does clip you whenever
your only non-Vampires are on board (**Carrion Feeder** — Zombie, **Mirkwood
Bats** — Bat, **Zulaport Cutthroat** — Human Rogue Ally). Still, this card is
meaningfully better in this pod than the audit credited. No action needed; do not
cut it.

## Revised summary

| Card | Price (2026-08-31 13:34–13:47 UTC) | Verdict |
|---|---|---|
| **Teferi's Protection** | $49.02 · **$9.02 over the $40 cap** · Game Changer 1 of 3 | **ADD** — cut **Orzhov Basilica**. Only answer in the deck to Armageddon; also answers Farewell. |
| **Clever Concealment** | $4.70 | **ADD IF** you want a second wipe answer — cut **Unexplained Absence** |
| ~~Patriarch's Bidding~~ | $3.81 | **NO** — withdrawn. Dead to Farewell's exile; symmetry is live against tribal opponents. |
| Eerie Interlude / Ghostway / Semester's End | $7.17 / $5.57 / $1.27 | **NO** — exile-and-return destroys your tokens and wipes every +1/+1 counter |

## Open items

- The audit's wipe-frequency question is **answered** for Farewell and Armageddon.
  It is still unanswered for conventional destroy-all-creatures wraths, but that
  no longer changes any verdict here — both recommended cards cover those anyway.
- If you take both adds, the deck is at 35 lands / 65 nonland with two cuts
  (Orzhov Basilica, Unexplained Absence). I have not modelled a third add and
  would push back on one: past those two, the next cut is a card I would defend.

## Addendum sources

- Scryfall via `card_facts.py lookup`, fetched **2026-08-31 13:45–13:47 UTC**:
  Farewell $6.00 (`{4}{W}{W}`, Game Changer) · Armageddon $14.23 (`{3}{W}`) ·
  Eerie Interlude $7.17 · Ghostway $5.57 · Semester's End $1.27 ·
  Anowon, the Ruin Sage $2.66 · Malakir Rebirth $14.27.
- Teferi's Protection rulings (2017-08-25) on phasing, counters and tokens, as
  quoted in the main review.
- Vigilance count, artifact count (9), enchantment count (4) and creature-type
  breakdown computed from `decks/markov_chains/cards.json`.

`base.txt` was not modified.

---

# Addendum 2 — deck synced from Moxfield (2026-08-31, same day)

The user pointed at `https://moxfield.com/decks/Sr3op2p6G0m0Msv1n_jLZw` and asked
for the local deck to be brought up to date. Fetched from
`api2.moxfield.com/v3/decks/all/Sr3op2p6G0m0Msv1n_jLZw`, **2026-08-31 14:00 UTC**;
Moxfield reports the deck ("Markov Chains", commander, public) last updated
**2026-08-31 04:56:54 UTC** — i.e. after the structural audit was written.

**`base.txt` was modified**, which this skill normally never does. It was done on
an explicit instruction and nothing was invented: every line comes from the
Moxfield payload. The previous list is backed up in the session scratchpad as
`base.txt.bak`. `build_card_details.py markov_chains` re-ran clean — 100 cards,
91 distinct, all resolved, no unresolved names. Only DFC spelling was normalised
(` // ` → ` / `) to match the existing file's convention.

## The diff

| | Card | Note |
|---|---|---|
| **out** | Orzhov Basilica | the audit's Finding 3 |
| **out** | Crackling Doom | not recommended by any review — the user's own call |
| **in** | Charismatic Conqueror | the card the audit reopened and did not decide |
| **in** | Qarsi Revenant | new, not previously reviewed |
| **±** | Mountain 3 → 1, Swamp 6 → 8 | the audit's Finding 2, and then some — it recommended 2 Mountain → 2 Swamp |

So two of the audit's three findings are now applied, and the reopened
Charismatic Conqueror question has been answered by the user in the affirmative.

## New composition, recounted from the rebuilt `cards.json`

| | before | now |
|---|---|---|
| Lands | 37 | **36** |
| Nonland | 63 | **64** |
| Creatures | 37 | **39** |
| Avg nonland MV | 2.83 | **2.84** |
| Curve 1/2/3/4/5/6 | 13/14/16/12/5/2 | **13/15/16/12/5/3** |
| Game Changers | 0 | **0** (bracket 3 permits 3) |
| Pips W / B / R | 13 / 63 / 6 | **13 / 64 / 5** |
| Land sources W / B / R | 18 / 25 / 18 | **17 / 26 / 16** |
| Creatures with vigilance | 0 | **1** (Charismatic Conqueror) |

`combos.py` on the updated list: still **2** assembled (Vito + Bloodthirsty
Conqueror; Marauding Blight-Priest + Bloodthirsty Conqueror), both the late-game
lifegain loops. Adding Teferi's Protection still completes **0** new combos. Both
`meta.json` vetoes remain clear.

## The two new cards, verified (2026-08-31 14:03 UTC)

- **Qarsi Revenant** `{1}{B}{B}` 3/3 Vampire, $2.44 — "Flying, deathtouch,
  lifelink. **Renew** — `{2}{B}`, Exile this card from your graveyard: Put a
  flying counter, a deathtouch counter, and a lifelink counter on target creature.
  Activate only as a sorcery."
- **Charismatic Conqueror** `{1}{W}` 2/2 Vigilance Vampire Soldier, $23.84 —
  scope as read in the audit: the trigger is on **opponents'** permanents entering
  **untapped**, and **the opponent chooses** whether to tap or give you a token.

Note for Finding 1's bookkeeping: `graveyard` now returns **three** hits across
the list rather than two — Bloodghast (returns itself), Bojuka Bog (outward hate)
and Qarsi Revenant's Renew. Renew **exiles itself** to put counters on a creature;
it is not recursion. **The deck still has zero ways to return another creature
from the graveyard.** Finding 1 is unchanged.

## What this changes about the recommendation

**The cut I named for Teferi's Protection no longer exists.** Orzhov Basilica was
the cut in both the main review and Addendum 1, and the user has already cut it.
At 36 lands with average nonland MV 2.84 there is no second land I would cut — the
five remaining tapped lands (Bojuka Bog, Canyon Slough, Malakir Mire, Nomad
Outpost, Path of Ancestry) each buy something real for the tempo. **So the add now
costs a spell.**

### Revised cut: **Vicious Conquistador** (`{B}` 1/2, $0.33)

Verified text, whole card: *"Whenever this creature attacks, each opponent loses
1 life."*

I spared this card twice — in the 2026-08-30 review and again in the audit — both
times for the same stated reason: *a turn-one Vampire body*. Per the consistency
rule I am not allowed to quietly drop that. So, explicitly: **the reason no longer
holds, and what changed is the pod, not my opinion of the card.** Its entire value
is early board presence in a deck that already has 13 one-drops, and the user has
since established that **Farewell and Armageddon are both common**. Early board
presence is precisely the currency those two cards burn. A 1/2 that deals 1 damage
per attack is the cheapest thing to lose in a list that is now at **39 creatures**
— its deepest category by a distance — and it is the deck's lowest-impact card by
EDHREC rank at **9,024**.

**Runner-up: Unexplained Absence** (`{3}{W}`, rank 6,671) — still the card I would
cut second, and it is the cut for Clever Concealment if that add is also taken.
I have moved it to second rather than first for one reason that is new since the
audit: **Crackling Doom left the deck**, taking interaction from 9 pieces to 8.

### A side effect of the user's own edit, flagged not contested

Crackling Doom was one of only **two** non-targeted removal effects in the list —
*"Each opponent sacrifices a creature with the greatest power among creatures that
player controls"* — the kind that answers hexproof, ward and protection, which
targeted removal cannot. **Soul Shatter** (`{2}{B}`, verified: *"Each opponent
sacrifices a creature or planeswalker with the greatest mana value among creatures
and planeswalkers they control"*) is now the only one left, plus Olivia's Wrath as
a sweeper. In a pod of single-type tribal decks running commander-level threats,
that is a thinner answer suite than it was. This is not a request to revert
anything — the cut was the user's call and Crackling Doom's `{R}{W}{B}` cost was
genuinely awkward on 16 red sources. It is recorded so a later review does not
mistake it for an oversight.

## Verdicts, restated against the current 100

| Card | Price (2026-08-31 13:34–14:04 UTC) | Verdict |
|---|---|---|
| **Teferi's Protection** | $49.02 · **$9.02 over the $40 cap** · Game Changer 1 of 3 | **ADD** — cut **Vicious Conquistador** (was Orzhov Basilica, now already gone) |
| **Clever Concealment** | $4.70 | **ADD IF** you want a second wipe answer — cut **Unexplained Absence** |
| ~~Patriarch's Bidding~~ | $3.81 | **NO** — withdrawn in Addendum 1 |
| Eerie Interlude / Ghostway / Semester's End | $7.17 / $5.57 / $1.27 | **NO** — exile-and-return destroys tokens and wipes counters |

Everything in Addendum 1's gameplay reasoning survives the sync unchanged: the
deck still has **zero** answers to Armageddon and **zero** answers to Farewell,
and Teferi's Protection is still the only card that covers both. Adding it takes
the deck to 39 creatures → 38 and leaves lands at 36.

## Addendum 2 sources

- Moxfield public API `api2.moxfield.com/v3/decks/all/Sr3op2p6G0m0Msv1n_jLZw`,
  fetched 2026-08-31 14:00 UTC; deck `lastUpdatedAtUtc` 2026-08-31T04:56:54Z;
  mainboard 99 + commanders 1 = 100. Maybeboard (**not** imported, and not
  evaluated here): Carmen, Cruel Skymarcher · Sheoldred, the Apocalypse ·
  Cover of Darkness.
- Scryfall via `card_facts.py lookup`, fetched **2026-08-31 14:03–14:04 UTC**:
  Qarsi Revenant $2.44 · Charismatic Conqueror $23.84 · Crackling Doom $0.39 ·
  Soul Shatter $3.39 · Vicious Conquistador $0.33.
- Composition, curve, pips, colour sources, vigilance and Game Changer counts
  recomputed from the rebuilt `decks/markov_chains/cards.json`.
- `combos.py markov_chains` and `--add "Teferi's Protection"` re-run on the
  updated list.

**`base.txt` was modified this time** — synced from Moxfield at the user's
explicit request, backup at `scratchpad/base.txt.bak`. No card was added or
removed by me.
