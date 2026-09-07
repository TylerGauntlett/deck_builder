# markov_chains — Drana and Linvala · Nighthawk Scavenger · Vampire Nighthawk, 2026-09-06

Question asked: *"Drana and Linvala"*, then mid-review *"nighthawk scavenger, vampire
nighthawk"*. Three candidates, evaluated as one batch (3 adds = 3 cuts).

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 · $40/card
cap · 4-player casual pods. Vetoes: no early infinite combos, no tutor-dependent win
line. Preference: on-theme Vampires, tiebreaker only.

Pod facts carried forward from the 2026-08-30 → 09-04 reviews, not re-litigated:
games run **long**; the three opponents are **mono-white — 2 fat-creature builds + 1
token swarm**; **Farewell and Armageddon are commonly played**; the deck is dual-mode
(Edgar-on-board aggro / Edgar-absent aristocrats drain, bridged by the +1/+1 counter
package).

All oracle text, legality, colour identity and prices fetched from Scryfall
**2026-09-06 15:29–15:31 UTC**. Deck composition from `decks/markov_chains/cards.json`
(built 2026-09-04, current with `base.txt`). EDHREC from the three cards' own pages
and `commanders/edgar-markov`, n = 50,363. Combos via `combos.py --add`.

`cards.md` was current (built 2026-09-04, `base.txt` last changed 2026-09-03); no
rebuild needed.

---

## Verdict summary

| Card | Price (15:29–15:31 UTC) | Edgar decks (EDHREC) | Verdict |
|---|---|---|---|
| **Drana and Linvala** `{1}{W}{W}{B}` | $8.59 | 23.1% (11,617 / 50,363) | **ADD IF** an opponent's deck actually uses creature activated abilities — cut **Forerunner of the Legion**. Under the pod as recorded: **NO**. |
| **Nighthawk Scavenger** `{1}{B}{B}` | $0.36 | 19.3% (9,709 / 50,363) | **NO** — seventh deathtouch/lifelink deterrent; a Qarsi Revenant swap is a sidegrade, not an upgrade |
| **Vampire Nighthawk** `{1}{B}{B}` | $0.20 | 33.1% (16,656 / 50,363) | **NO** — dominated by two cards, one already in the deck |

None of the three completes or approaches any combo (`combos.py --add`: 0 new, 0
newly within reach, baseline stays at 2). None is a Game Changer. All three are
legal in the deck's identity. Price is stated as its own factor throughout and
**every rejection below survives the card being free.**

---

## The deck, recounted this session

From `cards.json`: 100 cards · 35 lands · 38 creatures · average nonland MV **2.88**.

Curve: 1 → **12** · 2 → **15** · 3 → **18** · 4 → **12** · 5 → 5 · 6 → 3.
MV 3 remains the fattest rung, as every review since 08-31 has noted.

Pips: **B 64 · W 15 · R 4**. Land sources: **B 20 · W 14** of 35 (plus Arcane Signet,
Talisman of Hierarchy, Talisman of Conviction for white; Signet, Hierarchy,
Indulgence, Dark Ritual, Master of Dark Rites for black). The only `{W}{W}` card in
the deck today is Clever Concealment, which convokes.

Vampire creatures: **35 of 38** (non-Vampires: Carrion Feeder, Mirkwood Bats,
Zulaport Cutthroat). All three candidates are Vampires, so "it's an eminence
trigger" is true of all three and separates none of them from the 35 already here.

### The category the two Nighthawks join — deathtouch / lifelink deterrents

Verified text, grouped by what the card actually grants:

| Source | Text (relevant clause) | Cost |
|---|---|---|
| **Vault of the Archangel** (land) | `{2}{W}{B}, {T}`: Creatures you control gain deathtouch and lifelink until end of turn | no spell slot |
| **Vampire of the Dire Moon** | Deathtouch, lifelink, 1/1 | `{B}` |
| **Qarsi Revenant** | Flying, deathtouch, lifelink, 3/3; Renew — `{2}{B}`, exile from graveyard: put flying, deathtouch and lifelink counters on target creature | `{1}{B}{B}` |
| **Bloodthirsty Conqueror** | Flying, deathtouch, 5/5 | `{3}{B}{B}` |
| **Henrika, Infernal Seer** (back face) | Flying, deathtouch, lifelink, 3/4 | transform |
| **Sorin, Imperious Bloodlord** | +1: target creature you control gains deathtouch and lifelink until end of turn | `{2}{B}` |

**Six sources.** The 2026-08-30 review rejected Qarsi Revenant on exactly this
count when it was four ("deathtouch deterrence is the deck's most redundant
defensive feature ... deterrence does not scale with body size"). Qarsi went in
anyway and was later spared on "deathtouch + lifelink blocks mono-white fat". That
spare reason is granted; it does not license a seventh and eighth copy.

### The lifelink → drain bridge (why lifelink bodies are not worthless here)

- **Vito, Thorn of the Dusk Rose** — "Whenever you gain life, target opponent loses
  that much life."
- **Marauding Blight-Priest** — "Whenever you gain life, each opponent loses 1 life."
- **Bloodthirsty Conqueror** — "Whenever an opponent loses life, you gain that much
  life." (the two assembled loops are Vito + Conqueror and Blight-Priest + Conqueror)
- **Bloodletter of Aclazotz** — "If an opponent would lose life during your turn,
  they lose twice that much life instead."

A lifelink hit for N is N drain through Vito, doubled by Bloodletter on your turn.
This is real and it is why the Scavenger question is closer than the Nighthawk one.

---

## 1. Drana and Linvala

`{1}{W}{W}{B}` — Legendary Creature — Vampire Angel, 3/4, flying, vigilance.
*"Activated abilities of creatures your opponents control can't be activated. Drana
and Linvala has all activated abilities of all creatures your opponents control. You
may spend mana as though it were mana of any color to activate those abilities."*

Rulings (2023-04-14): activated abilities only — no triggered or static abilities;
a stolen ability that names its source is read as naming Drana and Linvala.

### Step 0 — the honest best case

She is the best raw 4-mana Vampire body available to the deck — 3/4 flying
vigilance attacks under Sanctum Seeker ("Whenever a Vampire you control attacks,
each opponent loses 1 life and you gain 1 life") and still blocks — and her text
is a one-sided lock on every opponent creature's activated ability, plus a copy of
each of those abilities for you. In a pod where an opponent runs mana creatures,
sacrifice outlets, "tap: gain protection" creatures, or a commander with an
activated ability, she turns those off and gives them to you.

That is a claim that could be false, and whether it is false is the entire verdict.

### Test — marginal impact, and the premise it rests on

The recorded pod is three mono-white decks: two fat-creature builds and one token
swarm. Nothing on record says which, if any, of those decks' creatures have
activated abilities. **I cannot verify the opponents' lists**, so I am not going to
assert that her text is live or dead.

What I can say is the shape of the answer:

- If the opponents' creatures are mostly bodies with triggered and static abilities
  (which is what "fat-creature" and "token swarm" usually means), her first ability
  is blank and her second gives her nothing. She is then a 3/4 flying vigilance
  Vampire for four with a `{W}{W}` cost, in a deck whose bodies come free from
  eminence.
- If even one opponent's deck leans on creature activated abilities, she is a
  one-sided stax piece on a relevant body, and no other card in the deck does that
  job at all. She also blanks the standard responses to the deck's own edicts and
  removal (sacrificing in response to Swords to Plowshares, Feed the Swarm, Soul
  Shatter, Grave Pact and Anowon for value).

This is the rubric's "verdict depends on the premise" case, so it goes to the user
rather than being guessed at.

### Test — cost of entry (the concrete cost either way)

She is the deck's second `{W}{W}` card and the only one that must be hard-cast. From
the actual land counts (14 W lands, 20 B lands, 35 lands in 99):

| Cards seen | WW from W lands | WW counting the 3 white rocks | BB from B lands |
|---|---|---|---|
| 10 (turn 4, play) | **43%** | 54% | 64% |
| 11 (turn 4, draw / turn 5, play) | 48% | 60% | 70% |
| 12 (turn 5, draw) | 53% | 65% | 75% |

So she is a turn-5-or-6 card about half the time, in a deck that was built so that
no white card needs two white pips. That is not a veto, but it means her body is
arriving a turn later than the `{2}{B}{B}` 4-drops it competes with.

### Test — redundancy and the dual-mode check

The 4-slot holds 12 cards, 8 of them Vampire creatures: Baron Bertram Graywater,
Bloodletter of Aclazotz, Bloodline Keeper, Edgar Charmed Groom, Elenda, Henrika
Domnathi, Sanctum Seeker, Vampire Nocturnus. Every one of those carries an
on-plan engine (tokens, doubling, lords, drain, counters, edict). Drana and Linvala's
text serves the **aggro** mode only (a good attacker) and the aristocrats mode not
at all — she does not die well, sacrifice, or drain. Her hate text is off-plan
entirely: it is a meta call, which is exactly what a 23.1% inclusion rate on the
Edgar page says the community treats her as.

### Anti-synergy, bracket, legend rule

None found. Her lock reads "creatures your **opponents** control" — Captivating
Vampire's "Tap five untapped Vampires you control" and Bloodline Keeper's abilities
are yours and unaffected. No other Drana or Linvala in the list. Not a Game
Changer; no combo touched.

### Disagreement check

23.1% of Edgar decks (11,617 / 50,363), EDHREC rank 1,907. That is a meta-call
figure, not a staple figure, and it agrees with the analysis: she is good where
her text is live and a body where it is not.

### Price

$8.59 (15:29 UTC). Under the cap. Not load-bearing in either direction: the NO under
the recorded pod survives at $0, and the ADD IF does not depend on the price.

### Verdict — ADD IF, and the cut

**ADD IF** at least one opponent's deck genuinely uses creature activated abilities
(mana creatures, sacrifice outlets, protection or tap abilities, a commander with an
activated ability). If the three mono-white decks are what the record says —
bodies, anthems and tokens — the answer is **NO**: a `{W}{W}` 4-drop body with blank
text does not beat the cut below.

**The cut, if she goes in: Forerunner of the Legion** `{2}{W}` 2/2 — *"When this
creature enters, you may search your library for a Vampire card, reveal it, then
shuffle and put that card on top. Whenever another Vampire you control enters,
target creature gets +1/+1 until end of turn."* EDHREC rank 6,051, $1.40. Same role
(Vampire creature body), same colour. The tutor puts a card on **top**, not in
hand — card selection, not card advantage, unless Herald's Horn is already out —
and the 08-31 Drana review already half-counted the pump as *"single target, until
end of turn."* It is the weakest creature in the list by rate and it has never
been spared with a specific reason. Curve effect: MV 3 count 18 → 17, MV 4 count
12 → 13, average 2.88 → 2.89. Pips: W 15 → 16.

Runner-up cut: **Henrika Domnathi** (same MV, rank 7,611) — spared because her
first mode, *"Each player sacrifices a creature of their choice,"* is a Grave Pact
trigger and a death trigger for you at the cost of a 1/1 token, and her back face
is a seventh deathtouch/lifelink body, which is the category the rest of this
review argues is already full. If Forerunner is a card you like, Henrika is the
next honest cut, not anything below her.

---

## 2. Nighthawk Scavenger

`{1}{B}{B}` — Creature — Vampire Rogue, (1+*)/3, flying, deathtouch, lifelink.
*"Nighthawk Scavenger's power is equal to 1 plus the number of card types among
cards in your opponents' graveyards."*

### Step 0 — the honest best case

For the same three mana as Qarsi Revenant, this is a flying deathtouch lifelink
Vampire whose power in a long four-player game is usually 4–6 (creature, land,
instant, sorcery, artifact, enchantment across three graveyards). Every point of
lifelink damage is a point of drain through Vito, doubled by Bloodletter on your
turn, and Bloodthirsty Conqueror converts the drain back into lifegain. Deathtouch
plus a lord's first strike (Stromkirk Captain: "Other Vampire creatures you control
get +1/+1 and have first strike") kills any blocker before it deals damage. It is a
deathtouch blocker against the two fat-creature mono-white decks.

### What killed it — redundancy, on rate and duration

It is the **seventh** source of deathtouch deterrence and the **third** flying
deathtouch lifelink body (Qarsi Revenant, Henrika's back face). The 08-30 review
rejected Qarsi Revenant when the count was four, on reasoning that still holds
word-for-word: *"deterrence does not scale with body size: a 1/1 deathtouch blocker
discourages an attack exactly as well as a 3/3."* Adding Scavenger as a seventh is a
marginal copy in the deck's most redundant defensive category, landing on MV 3 —
already the fattest rung at 18.

### Would a Qarsi Revenant → Scavenger swap be an upgrade?

The rubric says being the best of the redundant options argues for a swap, so the
honest comparison, effect × frequency × duration:

- **Attack rate.** Scavenger is bigger once graveyards fill: 5/3 vs 3/3 is +2
  lifelink per hit, so +2 drain through Vito, +4 with Bloodletter. Real.
- **On curve.** Turn 3 on the play, opponents' graveyards often hold 0–2 card
  types. Scavenger is a 1/3 to 3/3 then; Qarsi is a 3/3 always.
- **The pod's sweeper.** Farewell is confirmed common here and one of its modes is
  *"exile all graveyards."* That resets Scavenger to a 1/3. Your own Bojuka Bog
  shrinks it too.
- **After a wipe.** Qarsi's renew (`{2}{B}`, exile from graveyard: flying, deathtouch
  and lifelink counters on target creature) turns a post-wrath eminence token into
  an evasive lifelink threat. The deck's recorded structural gap (08-31 audit
  Finding 1) is board recovery. Scavenger has no graveyard text.

Net: a **sidegrade**. Bigger in the mid-game, smaller at both ends, and it gives up
the one graveyard-facing ability in a 38-creature deck that has two. I would not
spend the slot churn on it.

### Disagreement check

19.3% of Edgar decks (9,709 / 50,363), rank 1,881. Moderate. This deck differs from
the average Edgar list by already running Qarsi Revenant, Henrika, Sorin and Vault
of the Archangel — the category is full here in a way it is not on the average
page.

### Price

$0.36 (15:31 UTC). The rejection survives at $0.

**Verdict: NO** — seventh deathtouch/lifelink deterrent on the fattest rung of the
curve; the swap for Qarsi Revenant trades renew for mid-game size and is not an
upgrade.

---

## 3. Vampire Nighthawk

`{1}{B}{B}` — Creature — Vampire Shaman, 2/3, flying, deathtouch, lifelink.

### Step 0 — the honest best case

The original three-mana flying deathtouch lifelink Vampire. Everything said for
Scavenger's keywords applies.

### What killed it — dominated twice

Same cost, same keywords, and:

- **Qarsi Revenant** (already in the deck) is a 3/3 with renew.
- **Nighthawk Scavenger** (rejected above) is 1 + card types, which exceeds 2 as
  soon as opponents' graveyards hold two card types.

A card that is strictly outclassed by a card the deck runs *and* by the other card
in the same request cannot beat the worst surviving card. It would be the eighth
deathtouch deterrent.

### Disagreement check

**33.1%** of Edgar decks (16,656 / 50,363) — the highest figure of the three, and
the rubric requires naming why this deck is different. Two reasons: this deck already
runs the newer card that does the same job with a bigger body and renew (Qarsi
Revenant), and it runs six deterrent sources including a land. The EDHREC figure is
accumulated inclusion across years of lists; it does not compare Nighthawk against
Qarsi Revenant, which most of those lists predate. (That last sentence is an
inference from the two cards' relative ages, not a fetched figure.)

### Price

$0.20 (15:31 UTC). The rejection survives at $0.

**Verdict: NO** — outclassed at the same cost by Qarsi Revenant, which is already in
the deck, and by Nighthawk Scavenger, which was also rejected.

---

## The batch, modelled together

Three adds would need three cuts. The aggregate:

- **Two of the three candidates are the same card.** Adding both Nighthawks gives
  the deck four flying deathtouch lifelink bodies at MV ≤ 4 and eight deterrent
  sources, in the category the 08-30 review already called its most redundant.
- **Curve.** +10 MV in (4 + 3 + 3) against the best three cuts (Forerunner 3,
  Henrika 4, and then a card I would defend). MV 3 goes 18 → 20 if both Nighthawks
  come in.
- **Cut list exhaustion.** After Forerunner of the Legion and Henrika Domnathi, the
  next cut is Vampire of the Dire Moon, Anowon, Qarsi Revenant or Mirkwood Bats —
  each spared with a specific reason in a prior review (turn-one body and lifelink;
  repeating edict engine; deathtouch/lifelink blocker; token-count-to-damage
  converter). Per the rubric, when the third cut is a card you would defend
  elsewhere, the third add is not worth it. That is the finding, and it is the
  reason the Nighthawks are NO independently of whether Drana and Linvala goes in.

No pod-speed premise was used for any verdict here. The one pod premise in play is
*what the opponents' creatures do*, and that is the open question below.

---

## The open question

**Do any of the three opponents' decks use creature activated abilities?** Mana
creatures, sacrifice outlets, tap-to-protect or tap-to-tap creatures, a commander
with an activated ability. Yes to any of those and Drana and Linvala goes in for
Forerunner of the Legion. No, and she is a `{W}{W}` body with blank text and the
answer is no. The Nighthawk verdicts do not move on this question.

---

## Sources

- Scryfall via `card_facts.py lookup`, 2026-09-06 15:29–15:31 UTC: Drana and Linvala
  $8.59 · Nighthawk Scavenger $0.36 · Vampire Nighthawk $0.20 · Forerunner of the
  Legion $1.40 · Henrika Domnathi $1.28 · Qarsi Revenant $3.04 · Vampire of the Dire
  Moon $1.22 · Mirkwood Bats $1.63 · Anowon $2.72 · Clever Concealment $5.46 ·
  Charismatic Conqueror $23.20 · Vein Ripper $6.95 · Bloodline Keeper $8.17 ·
  Vampire Nocturnus $5.95.
- EDHREC card pages (15:29–15:31 UTC): Drana and Linvala 11,617 / 50,363 Edgar decks
  (23.1%), rank 1,907 · Nighthawk Scavenger 9,709 / 50,363 (19.3%), rank 1,881 ·
  Vampire Nighthawk 16,656 / 50,363 (33.1%), rank 1,742. The Edgar commander page
  (n = 50,363) lists none of the three in its high-synergy or top-cards sections, so
  no synergy score is available for them.
- Commander Spellbook via `combos.py --add`: 0 new combos, 0 newly within reach for
  each candidate; baseline 2 assembled.
- Deck composition, curve, pips, land sources and oracle scopes from
  `decks/markov_chains/cards.json` (built 2026-09-04). WW/BB odds are hypergeometric
  on 99 cards with the land counts above.
- Prior reviews cited: 2026-08-30 vampire-seven (Qarsi Revenant rejection and the
  deterrent count), 2026-08-31 structural audit (recovery gap, white pip design),
  2026-08-31 Drana Liberator (Forerunner half-count), 2026-09-03 fifty-dollar
  upgrades (pod composition, spare reasons for Anowon / Qarsi / Bats).

`base.txt` was not modified.
