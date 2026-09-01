# markov_chains — card review, 2026-08-30

Candidates: **Sanguine Bond** · **Exquisite Blood**

Deck context: Edgar Markov, bracket 3, $40/card cap, 4-player casual pods.
Stated goal: "win with a string of individually useful cards rather than by
assembling a named combo," vampire aggro into aristocrats.

All oracle text, legality, colour identity, rulings and prices fetched from
Scryfall 2026-08-31 03:53–03:57 UTC. EDHREC from `commanders/edgar-markov`,
n = 50,082 (bracket spread 1→91 · 2→3,540 · 3→5,308 · 4→3,954 · 5→169).
Combo checks via Commander Spellbook `find-my-combos`.

**Verdict: NO on both.**

---

## Data-integrity note

`base.txt` was edited *while this review was running* — six cards changed. The
first read of the list was the pre-update version. Every count below was
recomputed after `build_card_details.py` was re-run against the current
91-line `base.txt`, and the pre-update numbers were discarded.

Cards now in the list that were not in the pre-update read: Anowon, the Ruin
Sage · Bloodletter of Aclazotz · Crackling Doom · Elenda, the Dusk Rose ·
Grave Pact · Malakir Bloodwitch. Cards no longer present: Champion of Dusk ·
Cliffhaven Vampire · Deadly Dispute · Dusk Legion Zealot · Falkenrath Pit
Fighter · Gallifrey Falls // No More.

**This moved a real number**: the combo baseline dropped from 3 assembled to
**2**, because Cliffhaven Vampire left the deck. The 2026-08-30 vampire-seven
review's "baseline 3" is stale as of this edit.

---

## Deck facts established this session

Counted from `cards.json` after rebuild, not from memory.

- **62 nonland non-commander cards.** Curve: 1→13 · 2→14 · 3→16 · 4→12 · 5→5 ·
  6→2. Average MV **2.81**. Only **7 cards at MV 5+**: Patron of the Vein,
  Vein Ripper (6); Anowon, Bloodthirsty Conqueror, High-Society Hunter,
  Malakir Bloodwitch, Olivia's Wrath (5).
- **"Whenever you gain life" payoffs — exactly 2**, grouped by scope:
  - *target opponent, that much*: Vito, Thorn of the Dusk Rose (MV 3)
  - *each opponent, 1*: Marauding Blight-Priest (MV 3)
- **"Whenever an opponent loses life → you gain that much" — exactly 1**:
  Bloodthirsty Conqueror (MV 5).
- **Lifegain fuel — 17 sources** (Akroma's Will, Baron Bertram, Bastion of
  Remembrance, Blood Artist, Bloodthirsty Conqueror, Cruel Celebrant, Edgar
  Charmed Groom, Elenda, Henrika, Indulgent Aristocrat, Sanctum Seeker, Sorin,
  Vampire of the Dire Moon, Vault of the Archangel, Vein Ripper, Vito,
  Zulaport Cutthroat).
- **Enchantments — 4**: Bastion of Remembrance, Grave Pact, Impact Tremors,
  Oubliette.
- **Tutors — 1**: Forerunner of the Legion, which searches for **a Vampire
  card** only. It cannot find either candidate.
- **Combo baseline — 2**, both the same loop: Vito + Bloodthirsty Conqueror,
  and Marauding Blight-Priest + Bloodthirsty Conqueror.
- EDHREC: the deck runs **10/10** high-synergy cards and **8/10** top cards.
  Missing only Charismatic Conqueror (57.2%) and Drana, Liberator of Malakir
  (54.3%). Game Changers run: **0**.

---

## The house-rule veto does not fire — this is a quality rejection

Worth stating plainly, because it would be easy to reject these by pointing at
the rulebook and skipping the actual argument.

`meta.json` vetoes *early* infinite combos and *tutor-dependent* win lines.
Neither applies:

- **Not early.** Sanguine Bond (5) + Exquisite Blood (5) = **10 mana**. The
  deck's two existing loops both cost **8** (Vito 3 + Conqueror 5;
  Blight-Priest 3 + Conqueror 5). The proposed pair is *slower* than the
  infinite lines the deck already runs and already accepts.
- **Not tutor-dependent.** The only search effect in the deck is Forerunner of
  the Legion, and its oracle text restricts it to a Vampire card. Neither
  enchantment is findable.

So both cards clear the hard constraints. They fail on card quality.

---

## Sanguine Bond — **NO**

`{3}{B}{B}` · MV 5 · Enchantment · colour identity B · legal

> Whenever you gain life, target opponent loses that much life.

**Steel-man.** The deck has 17 lifegain sources and a dense aristocrats shell.
Every Blood Artist / Zulaport / Cruel Celebrant / Bastion / Sanctum Seeker /
Vein Ripper trigger gains life, and Sanguine Bond converts each one into extra
damage. Unlike the other candidate it is a genuine incremental damage
amplifier, not only a combo piece. 45.3% of Edgar decks run it.

**Why it still fails.**

1. **It is word-for-word Vito's first ability, and Vito is already in the
   deck.** Vito's line reads "Whenever you gain life, target opponent loses
   that much life" — identical text, same single-target scope. Sanguine Bond
   costs **two more mana** and delivers only that half; Vito also brings a
   Vampire body and `{3}{B}{B}: Creatures you control gain lifelink`. This is
   not redundancy on a thin category, it is a strictly worse second copy.
2. **A non-Vampire, non-creature permanent misses this deck's whole
   infrastructure.** Verified against the cards that care:
   - Edgar Markov's eminence triggers on casting *another Vampire spell* — no
     token.
   - Herald's Horn discounts *creature spells of the chosen type* — no discount.
   - Path of Ancestry scries on *a creature spell sharing a type* — no scry.
   - Captivating Vampire, Legion Lieutenant, Stromkirk Captain and Vampire
     Nocturnus all pump *Vampires* — no pump.
   - It is not a body for Carrion Feeder, Bloodthrone Vampire, Viscera Seer or
     Indulgent Aristocrat, and it never dies to trigger Blood Artist, Zulaport
     Cutthroat, Cruel Celebrant, Bastion of Remembrance or Grave Pact.
3. **Curve.** A fourth 5-drop in a deck averaging MV 2.81 with only 7 cards at
   MV 5+, and the one you cast at 5 does nothing to the board the turn it
   lands.

Combo delta: **+1 line** (Sanguine Bond + Bloodthirsty Conqueror) — the same
infinite lifegain/lifeloss loop the deck already assembles two ways.

Price: **$6.57** (2026-08-31 03:53 UTC). Under the cap. **This rejection
survives the card being free** — the problem is that Vito already does it for
less on a better card type.

---

## Exquisite Blood — **NO**

`{4}{B}` · MV 5 · Enchantment · colour identity B · legal

> Whenever an opponent loses life, you gain that much life.

**Steel-man.** It is the single most-played nonland card in Edgar Markov decks
at 51.2%, it triples the deck's redundancy on its existing win loop, and the
new lines it makes cost the same 8 mana as the ones already there (Vito 3 +
Blood 5; Blight-Priest 3 + Blood 5). In a pod where the aggro plan gets
stalled, more copies of the inevitability engine is a real want.

**Why it still fails.**

1. **It adds zero damage outside the loop.** This is the decisive point and it
   is worth being precise about. Blood Artist drains 1 and gains you 1;
   Exquisite Blood sees that 1 life lost and gains you 1 *more life*. No
   additional life is lost by anyone. The card's entire damage output is
   routed through Vito or Marauding Blight-Priest — which is the infinite
   loop. So it has exactly two modes: **a dead 5-mana lifegain enchantment, or
   it wins the game.** Nothing in between.
2. **That is a direct conflict with the deck's stated goal**, which is to win
   with individually useful cards rather than by assembling a named combo. Of
   all the cards that could be proposed for this deck, Sanguine Bond +
   Exquisite Blood *is* the named combo.
3. **The effect is already in the deck at the same mana value, on a much
   better card.** Bloodthirsty Conqueror is `{3}{B}{B}`, MV 5, same trigger
   text — on a **5/5 flying deathtouch Vampire** that attacks, blocks, takes
   Edgar's +1/+1 counters, gets the eminence token when cast, gets the
   Herald's Horn discount, and dies to your own aristocrats triggers.
4. Same non-Vampire infrastructure miss as Sanguine Bond, item 2 above.

Combo delta: **+2 lines** (with Vito, with Marauding Blight-Priest) — again the
identical infinite lifegain/lifeloss loop. Adding both candidates gives +4
lines, all of them the same loop.

Price: **$39.45** (2026-08-31 03:53 UTC) — inside the $40 cap by 55 cents.
Stated as its own factor: **price is not carrying this rejection.** The verdict
is unchanged at $0, and it would also be unchanged if you already own the card.

---

## No cut list

Neither card survived evaluation, so there is nothing to cut. For the record,
if you *had* forced both in, the two adds would push MV 5+ from 7 to 9 in a
62-card nonland shell averaging 2.81, and the cheapest defensible cuts would
have had to come out of a deck that already runs 10/10 EDHREC high-synergy
cards — there are no two genuinely cuttable cards here.

## No counter-proposal

The usual counter-proposal move is "the role is real, the card is wrong." Here
the role is **not** real. The deck has 2 lifegain payoffs, 1 opponent-life-loss
converter, 17 lifegain sources and a full aristocrats package; drain is the
category it is deepest in, not thinnest. Adding a fourth and fifth way to do
the same thing does not fix anything.

EDHREC's two missing top cards — Charismatic Conqueror (57.2%) and Drana,
Liberator of Malakir (54.3%) — serve a different role (pressure and evasive
token pressure) and were not evaluated here. Ask if you want them run.

---

## What would change my mind

- **Vito or Bloodthirsty Conqueror leaving the deck.** Both rejections lean on
  those two specific cards being present. Cut Vito and Sanguine Bond becomes a
  real, if expensive, replacement; cut Conqueror and Exquisite Blood becomes
  the only copy of its effect rather than the second.
- **A change to the stated goal.** If you decide you *do* want the deck to win
  by assembling the named combo — moving toward bracket 4 — Exquisite Blood is
  the correct card for that plan and the analysis above flips. That is a
  `meta.json` change, not a card evaluation, and it is yours to make.

What I am not certain about: how long your pod's games actually run. Neither
verdict depends on it — every argument above (duplicated effect, wrong card
type, zero damage outside the loop) holds at any game length. But if games
routinely go long enough that the aggro plan stops mattering and you are
winning through the loop most nights, the deck is already a combo deck in
practice and `meta.json`'s archetype line is the thing to fix first.

---

## Sources

- Scryfall, fetched 2026-08-31 03:53–03:57 UTC — oracle text, legality, colour
  identity, prices, and the Sanguine Bond rulings of 2021-03-19 (which
  describe the Exquisite Blood loop explicitly).
- EDHREC `commanders/edgar-markov`, n = 50,082; per-card pages for Sanguine
  Bond (rank 504, 45.3% of Edgar decks) and Exquisite Blood (rank 512, 51.2%).
- Commander Spellbook `find-my-combos` — baseline **2**; Sanguine Bond +1,
  Exquisite Blood +2, both together +4.
- Deck composition counted from `decks/markov_chains/cards.json`, rebuilt this
  session from the post-edit `base.txt`.

---

## Addendum — did cutting Cliffhaven Vampire remove a win condition?

Asked after the verdict above. Short answer: **no, and nothing needs to be cut.**

- **The deck is at exactly 100 cards** (36 lands, 91 distinct). The 6-for-6 swap
  left it legal and complete. No compensating cut is required.
- **Every infinite line in this deck routes through Bloodthirsty Conqueror** —
  before and after the swap. Verified: re-adding Cliffhaven Vampire completes
  exactly one combo, `[4789-6191] Cliffhaven Vampire + Bloodthirsty Conqueror`.
  Cliffhaven was never an independent win condition.
- **What actually left** was the third copy of the *"whenever you gain life"*
  half. Two remain, and they differ in scope: Vito (*target opponent, that
  much*) and Marauding Blight-Priest (*each opponent, 1*).
- **The real single point of failure is Bloodthirsty Conqueror**, holding the
  *"whenever an opponent loses life → you gain that much"* half alone. That
  asymmetry — 2 copies of one half, 1 of the other — predates the swap and is
  untouched by it. Removing Conqueror leaves zero loops regardless of Cliffhaven.
- **The primary aggro/drain plan never involved Cliffhaven** and looks stronger
  after the swap: Malakir Bloodwitch's ETB drains each opponent for your Vampire
  count *and* gains you that much (a large kickstart for Vito/Blight-Priest), and
  Bloodletter of Aclazotz doubles opponents' life loss — but note the scope:
  **"during your turn" only**.
- Card advantage survived the swap intact — **12 draw sources** remain
  (Skullclamp, Welcoming Vampire, High-Society Hunter, Baron Bertram, Night's
  Whisper, Painful Truths, Village Rites, War Room, Henrika, Clavileño, Canyon
  Slough, Voldaren Estate), despite Deadly Dispute and Dusk Legion Zealot
  leaving.

**Restoring Cliffhaven Vampire: still no.** A 4-mana 2/4 flier that is blank
unless Conqueror is already down, replaced by cards that do more.

**Consistency note on Exquisite Blood.** This analysis does sharpen one point in
its favour: it is the only realistic second copy of the *Conqueror* half, which
is the half with no redundancy. Enduring Tenacity and Starscape Cleric, the other
near-misses, are further copies of the half that already has two. The verdict is
unchanged, because the rejection rested on Exquisite Blood adding **zero damage
outside the loop**, and that is independent of how many copies of each half
exist. The condition stated above still stands: if Bloodthirsty Conqueror ever
leaves the deck, re-open Exquisite Blood.
