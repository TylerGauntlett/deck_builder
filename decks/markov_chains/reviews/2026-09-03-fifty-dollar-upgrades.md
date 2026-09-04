# markov_chains — best upgrades for $50 — 2026-09-03

Question asked: *"what is the best upgrades to this deck for $50"* (deck named as
`edgar_markov`; the list on disk is `markov_chains`, commander Edgar Markov).

**Budget read as $50 total spend**, not $50 per card. `meta.json` already carries a
separate **$40/card** cap, so "$50" reads as a shopping list, not a cap change. This
matters: it makes the exercise an *allocation* problem, which is a constraint none
of the prior reviews faced. Flagged to the user.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 · $40/card ·
4-player casual pods. Vetoes: no early infinite combos, no tutor-dependent win line.

**Pod facts carried forward** (user-stated across prior reviews, not `meta.json`):
games run **long**; **Armageddon and Farewell are both commonly played**; the
mono-white opponents are **2 fat-creature decks + 1 token deck** (per the 2026-09-03
procession addendum correction); the deck is dual-mode — Edgar-on-board aggro /
Edgar-absent aristocrats drain.

All oracle text, legality, colour identity and prices fetched live from Scryfall
**2026-09-03 22:23–22:29 UTC**. Nothing below is from memory.

---

## Verdict summary — the $50 package

| # | Add | Price | Cut | Slot |
|---|---|---|---|---|
| 1 | **Takenuma, Abandoned Mire** | $11.17 | **Mountain** | land |
| 2 | **Phyrexian Tower** | $28.15 | **Sundown Pass** | land |
| 3 | **Black Market Connections** | $10.33 | **Lightning Bolt** | spell |
| | **Total** | **$49.65** | | |

Also evaluated and rejected: Bolas's Citadel $16.01 · Kindred Dominance $4.58 ·
Vanquisher's Banner $5.30 · Ashnod's Altar $16.28 · Phyrexian Altar $56.76 ·
Reconnaissance $6.20 · Agent of the Iron Throne $0.59 · Anointed Procession $59.52
(over budget).

---

## The finding that shapes everything: the community list is exhausted

`edhrec.py commander --diff` and both relevant theme diffs, run this session:

| List | Deck runs |
|---|---|
| Commander — High Synergy Cards | **10 of 10** |
| Commander — Top Cards | **9 of 10** (missing only Drana, rejected 2026-08-31) |
| Aristocrats theme — High Synergy | **10 of 10** |
| Aristocrats theme — Top Cards | **10 of 10** |
| Vampires theme — High Synergy | **10 of 10** |
| Vampires theme — Top Cards | **9 of 10** (Drana again) |

There is no popular card this deck is missing. Every remaining EDHREC suggestion is
a Game Changer (mostly tutors, which sit against the no-tutor-dependent-win-line
veto) or a new-set card. So the $50 cannot buy "the staple you forgot" — it has to
buy a **structural** fix, and the analysis below works from the deck's own role
counts rather than from a popularity list.

## Role counts, recomputed from `cards.json` this session

| Role | Count | Thin? |
|---|---|---|
| Lands | 36 | no |
| Creatures | 38 | no |
| Vampire spells (eminence fuel) | 35 | no |
| Drain payoffs | ~11 | no — deepest category in the deck |
| Anthem / pump effects | 18 | no — Door of Destinies rejected as the 7th |
| Card draw | 12 | no (audited 2026-08-31) |
| Ramp | 7 | no |
| Sac outlets | 11, three free & repeatable | no |
| Targeted interaction | 5–6 | adequate |
| One-sided sweepers | 1 (Olivia's Wrath) | adequate |
| **Graveyard recursion / board rebuild** | **2** | **YES — the only open gap** |

The two graveyard-facing cards, verified today:

- **Bloodghast** — *"Landfall — Whenever a land **you control** enters, you may return
  **this card** from your graveyard to the battlefield."* Self-recursion only.
- **Qarsi Revenant** — *"Renew — {2}{B}, **Exile this card from your graveyard**: Put
  a flying counter, a deathtouch counter, and a lifelink counter on target
  creature."* Puts counters on something else; returns nothing.

**Zero cards in the 99 return another creature from the graveyard.** The
2026-08-31 audit's Finding 1 is still open.

---

## 1. ADD — Takenuma, Abandoned Mire · $11.17 · cut **Mountain**

Standing recommendation from this morning's land review, re-verified and re-priced
today. Verified text:

> Legendary Land · `{T}`: Add `{B}`.
> **Channel** — `{3}{B}`, Discard this card: Mill three cards, then return a creature
> or planeswalker card from your graveyard to your hand. This ability costs `{1}`
> less to activate for each **legendary creature you control**.

It is the single best card available inside this budget and the reason is structural:
**it fills the only open gap while costing a land slot rather than a spell slot.**
Its floor is a Swamp, so unlike Patriarch's Bidding (withdrawn 2026-08-31 — dead to
Farewell's exile, and symmetric against the pod's tribal decks) it cannot be
blanked. Channelling from hand also dodges Armageddon entirely.

The legendary discount is live here: the deck runs Edgar in the command zone plus
Anowon, Baron Bertram, Clavileño, Elenda, Florian, Henrika, Vein Ripper and Vito.

**No combo risk:** `combos.py --add` returns 0 new and 0 near.

## 2. ADD — Phyrexian Tower · $28.15 · cut **Sundown Pass**

Also standing from the land review. Verified text:

> Legendary Land · `{T}`: Add `{C}`. · `{T}`, **Sacrifice a creature**: Add `{B}{B}`.

**This one deserved re-testing, and I re-tested it,** because $28.15 is 57% of the
budget and the sac-outlet role is one I have twice rated "not thin" (11 outlets).
The opportunity-cost question is new — the land review recommended it with no budget
ceiling in play.

It survives the re-test on two grounds the raw outlet count does not capture:

1. **It is the only outlet that survives a wipe.** All three free repeatable outlets
   (Carrion Feeder, Viscera Seer, Bloodthrone Vampire) are 1- and 2-mana creatures
   that die to every wrath. The deck's identified worst case is the post-wipe turn.
2. **It answers targeted exile at instant speed.** Vein Ripper and Bloodthirsty
   Conqueror are the deck's two bombs and the obvious Swords targets; with Tower
   untapped you sacrifice in response and convert the removal into `{B}{B}` plus every
   death trigger, instead of losing the card for nothing.

That is a different axis from "the 12th sac outlet," and it is why it keeps the slot
over Ashnod's Altar ($16.28), which is cheaper and also free — but is an artifact
that dies to the same Farewell as everything else, and makes colourless.

**No combo risk:** 0 new, 0 near.

## 3. ADD — Black Market Connections · $10.33 · cut **Lightning Bolt**

The new find this session, and the reason the top-10 lists missed it: it is not a
Vampire card and not on any of the six lists above, yet **23.9% of Edgar Markov
decks run it (11,988 of 50,203)** and Edgar is its **third-largest home by raw deck
count** across all of EDHREC.

Verified text:

> `{2}{B}` Enchantment · At the beginning of your first main phase, choose one or more —
> • **Sell Contraband** — Create a Treasure token. You lose 1 life.
> • **Buy Information** — Draw a card. You lose 2 life.
> • **Hire a Mercenary** — Create a 3/2 colorless Shapeshifter creature token with
>   **changeling**. You lose 3 life. *(It is every creature type.)*

**The load-bearing detail is `changeling`.** The token is every creature type, so it
is a **Vampire**. Verified payoffs, with scopes checked rather than assumed:

| Payoff | Verified clause | Token qualifies? |
|---|---|---|
| **Captivating Vampire** | *"Other **Vampire creatures you control** get +1/+1"* | yes — and it counts toward "Tap five untapped Vampires" |
| **Vampire Nocturnus** | *"this creature and other **Vampire creatures you control** get +2/+1 and have flying"* | yes |
| **Legion Lieutenant** | *"Other **Vampires you control** get +1/+1"* | yes |
| **Stromkirk Captain** | *"Other **Vampire creatures you control** get +1/+1 and have first strike"* | yes |
| **Sanctum Seeker** | *"Whenever a **Vampire you control** attacks, **each opponent** loses 1 life and you gain 1"* | yes — a 3/2 attacker drains all three |
| **Cordial Vampire** | *"Whenever this creature **or another creature** dies, put a +1/+1 counter on **each Vampire you control**"* | yes |
| **Indulgent Aristocrat** | *"`{2}`, Sacrifice a creature: Put a +1/+1 counter on **each Vampire you control**"* | yes — token is both fodder and recipient |
| **Mirkwood Bats** | *"Whenever you **create or sacrifice a token**, each opponent loses 1 life"* | yes — **both** the Treasure and the Shapeshifter trigger it |

That is eight verified interactions, well past the three-card synergy floor.

**Why it fits this deck specifically, on four axes:**

1. **It serves both modes.** The Edgar-aggro mode gets a recurring 3/2 lord-buffed
   Vampire body; the aristocrats mode gets recurring sacrifice fodder plus a card
   plus a Treasure. Cards that serve both modes are the strongest adds available and
   the easiest to under-rate.
2. **It is a rebuild engine.** A 3-mana permanent that manufactures a fresh 3/2 body
   *every turn* is the closest thing in budget to answering "the deck cannot rebuild
   after a wipe." It is not graveyard-based, so unlike every recursion spell it is
   not blanked by Farewell exiling graveyards. (Farewell can still exile the
   enchantment itself — stated plainly, not hidden.)
3. **Its cost is a resource this deck has in surplus.** All three modes cost life;
   the deck runs Vito, Sanctum Seeker, Cruel Celebrant, Blood Artist, Bastion of
   Remembrance, Malakir Bloodwitch, Bloodthirsty Conqueror and Vault of the
   Archangel. Paying 6 life a turn for a body, a card and a Treasure is a rate this
   deck can pay and most decks cannot.
4. **Modality means it is never dead.** Ahead, take the body; behind, take the card;
   short on mana, take the Treasure.

**Honest weaknesses.** It does **not** trigger Edgar's eminence — eminence needs you
to *cast another Vampire spell*, and a token is not cast. And it does nothing the
turn it resolves. Both are real; neither sinks a 3-mana permanent in a pod where
games run long.

**No combo risk:** 0 new, 0 near.

### The cut: Lightning Bolt ($0.70)

This is the cut the 2026-09-03 procession addendum already designated, for reasons
independent of what replaces it: *"Three damage does not answer a fat white creature,
and as reach in a long four-player game it is negligible against 120 combined
starting life. It is the one card the new fact devalues."* Since Anointed Procession
is out of budget at $59.52, that cut slot is free, and the reasoning transfers intact.

Role floor respected — interaction after the cut is **Swords to Plowshares** (exile
any creature), **Anguished Unmaking** (any nonland permanent), **Feed the Swarm**
(creature or enchantment), **Soul Shatter** (greatest MV, non-targeted, beats
hexproof), **Oubliette**, plus **Olivia's Wrath** as a one-sided sweeper and **Grave
Pact** as a repeating edict.

---

## The cut discipline is the real constraint, and it caps the package at three cards

Worth stating explicitly, because it is *why* this is the answer and not a longer
list. N adds means N cuts, and this deck has almost no cuttable spells left. Every
obvious candidate has already been examined and **spared for a specific reason I am
not going to quietly reverse**:

- **Anowon, the Ruin Sage** — cut, then *un*-cut on 2026-09-03 when the pod turned
  out to be 2 fat-creature decks + 1 token deck. An upkeep edict is real attrition
  against two of three opponents.
- **Qarsi Revenant** — spared on *"deathtouch plus lifelink blocks mono-white
  fatties,"* a reason the pod correction made **stronger**.
- **Impact Tremors** — spared because it is a payoff, not filler.
- **Lightning Bolt** — the one card the pod correction devalued. This is the cut.

So exactly **one** defensible spell cut exists. Everything beyond it would have to
displace a card I would defend anywhere else — which is precisely why the two
**land** upgrades are so efficient here: Mountain and Sundown Pass are the two
weakest lands in the base, and swapping them costs the 99 nothing.

**This also settles the allocation question.** The tempting alternative — skip the
$28.15 Tower and buy Bolas's Citadel + Kindred Dominance + Black Market Connections
for $30.92 — fails not on the cards' merits but because it needs **three** spell
cuts and only one exists.

## Deltas after all three swaps

- **Lands: 36 → 36.** Two land-for-land swaps.
- **Curve (nonland):** 1→**12**, 2→15, 3→**17**, 4→12, 5→5, 6→3 becomes
  1→**11**, 2→15, 3→**18**, 4→12, 5→5, 6→3.
- **Vampire spells: 35 → 35.** Neither Bolt nor BMC is a Vampire, so eminence fuel is
  untouched. Creature count unchanged at 38.
- **Red:** red-pip cards in the 99 drop 4 → **3** (Florian, Impact Tremors, Stromkirk
  Captain), red land sources 16 → **14**. The 2026-08-31 audit flagged 21 red sources
  for 5 red cards as over-supplied; this moves toward correct, not away.
- **White land sources: 18 → 17.** See open question below.
- **Black land sources: 25 → 27** (Takenuma adds `{B}`; Phyrexian Tower's `{B}{B}` is
  conditional on a sacrifice). This eases the four `BBB` costs.
- **Bracket: unchanged.** None of the three adds is a Game Changer; the deck stays at
  **1 of 3** (Teferi's Protection). Both `meta.json` vetoes clear — all three
  candidates return **0 new combos and 0 near** on `combos.py --add`.

---

## Rejected, with reasons

| Card | Price | Verdict |
|---|---|---|
| **Bolas's Citadel** | $16.01 | **NO** — a genuine engine in a 2.83-MV lifegain deck, and bracket has room (GC 2 of 3). But it is a 6-drop that needs the one available spell cut, and `combos.py --near` shows it opens **12** new near-combo lines (all missing Mortuary) — against a deck whose stated goal is *"win with a string of individually useful cards rather than by assembling a named combo."* Loses the slot to BMC on fit, not on power. |
| **Kindred Dominance** | $4.58 | **NO** — MV **7** in a 2.83-MV deck, and the one-sided-sweeper role is already filled by **Olivia's Wrath** (MV 4, $0.40). Its one edge over Wrath is working from an empty board — but seven mana is exactly what you do not have on the post-wipe turn. |
| **Vanquisher's Banner** | $5.30 | **NO** — MV 5, and its anthem half is the 19th pump effect in a deck that rejected Door of Destinies as the 7th anthem. BMC draws at a better rate for two less mana. |
| **Ashnod's Altar** | $16.28 | **NO** — see Phyrexian Tower above. |
| **Phyrexian Altar** | $56.76 | **NO** — over both the $40/card cap and the total budget. |
| **Reconnaissance** | $6.20 | **NO** — a combat trick in a deck with 18 pump effects and no evasion problem. |
| **Agent of the Iron Throne** | $0.59 | **NO** — a Background; the drain role is ~11 deep already. |
| **Anointed Procession** | $59.52 | **out of budget** — the ADD from earlier today stands on its merits but does not fit $50. |
| **Drana, Liberator of Malakir** | $0.88 | **NO** — unchanged from 2026-08-31. |

---

## What I am unsure about, and what would settle it

1. **Carried forward, unresolved from this morning's land review: does any regular
   opponent play a graveyard deck?** If not, **Bojuka Bog** — a tapped Swamp whose
   only ability is graveyard hate pointed at a pod described as mono-white — is a
   better cut for Phyrexian Tower than Sundown Pass, **and it keeps white at 18
   sources instead of 17.** This is a free improvement to the package and costs
   nothing to take if the answer is no.

2. **The budget reading.** If "$50" meant **$50 per card** rather than $50 total, the
   answer changes: **Anointed Procession** ($59.52) is still out, but **Urborg, Tomb
   of Yawgmoth** ($55.92, the land review's ADD IF) and **Cavern of Souls** ($50.06)
   come back into range, and the ranking would be re-run.

3. **Is the $40/card cap real or a default?** Teferi's Protection went in at $49.02,
   which suggests soft. Unchanged from the land review; it does not affect any card
   in this package, all three of which are under $30.

---

## Prices and figures used (all fetched 2026-09-03 22:23–22:29 UTC)

Takenuma, Abandoned Mire $11.17 · Phyrexian Tower $28.15 · Black Market Connections
$10.33 · Lightning Bolt $0.70 · Bolas's Citadel $16.01 · Kindred Dominance $4.58 ·
Vanquisher's Banner $5.30 · Ashnod's Altar $16.28 · Phyrexian Altar $56.76 ·
Reconnaissance $6.20 · Agent of the Iron Throne $0.59 · Anointed Procession $59.52 ·
Anowon $2.67 · Qarsi Revenant $2.69 · Impact Tremors (no non-foil price; foil $2.10) ·
Olivia's Wrath $0.40 · Skullclamp $6.04 · Herald's Horn $5.86.

EDHREC, Edgar Markov page, **n = 50,203**: Black Market Connections **23.9%
(11,988)**, overall rank 131, Edgar its 3rd-largest home by raw count · Kindred
Dominance 16.6% (8,332), rank 707 · Drana 54.3% (27,268). Aristocrats theme
n = 1,464; Vampires theme n = 6,480.

Commander Spellbook `find-my-combos`: baseline **2** assembled. Takenuma, Phyrexian
Tower, Black Market Connections and Kindred Dominance each complete **0 new / 0
near**; Bolas's Citadel completes **0 new / 12 near** (all missing Mortuary).

---

## Addendum — 2026-09-03: the Phyrexian Tower cut moves to Clifftop Retreat

User asked: *"why not remove Clifftop Retreat or Dragonskull Summit instead of
Sundown Pass?"* Both re-verified live from Scryfall 2026-09-03 23:03 UTC. The user is
right about Clifftop Retreat; Dragonskull Summit is a no.

### Dragonskull Summit — NO

> `enters tapped unless you control a Swamp or a Mountain.` `{T}`: Add `{B}` or `{R}`.

It is a **black source**, and black is the deck's demanding colour — 63 pips and four
`BBB` costs. Phyrexian Tower produces `{C}` normally and `{B}{B}` only by sacrificing
a creature, so this swap would downgrade the primary colour. It is also the **most
reliable checkland in the deck**: counting subtypes after the Takenuma swap, its
condition is met by **12** lands (7 Swamps, Sacred Foundry, Godless Shrine, Blood
Crypt, Canyon Slough, Smoldering Marsh).

### Clifftop Retreat — YES, this replaces Sundown Pass as the cut

The land review's stated reason for cutting Sundown Pass was that it is *"neither a
painland with a colourless mode nor a shockland with basic types that other lands
check for."* That argument correctly separates Sundown Pass from **Battlefield Forge**
and **Sacred Foundry** — but it never compared it to **Clifftop Retreat**, which it
put in the keep pile without a reason. On the one axis that separates those two:

| | Enters untapped when | Enablers after the Takenuma swap |
|---|---|---|
| **Clifftop Retreat** | you control a **Mountain or Plains** subtype | **9** of 35 — 4 Plains, Sacred Foundry, Godless Shrine, Blood Crypt, Canyon Slough, Smoldering Marsh |
| **Sundown Pass** | you control **two or more other lands** | **unconditional from the third land drop onward** |

- **Land drop 1:** both tapped. Tie.
- **Land drop 2:** Clifftop better, but only when the turn-1 land was a Plains/Mountain
  subtype — roughly 26%, and this deck's turn-1 land is usually a Swamp or black dual
  because its early plays are almost all black (Viscera Seer, Indulgent Aristocrat,
  Vampire of the Dire Moon, Carrion Feeder).
- **Land drop 3+:** Sundown Pass is **guaranteed** untapped; Clifftop Retreat is still
  conditional. In a pod where games run long, this window dominates.

Two compounding points: **cutting the Mountain for Takenuma removes one of Clifftop
Retreat's own enablers** (10 → 9), so the package actively degrades it; and both are
R/W, so the colour delta is identical either way — W 18 → 17, red land sources → 14
against only **3** red-pip cards left in the 99 once Lightning Bolt is cut (Florian,
Impact Tremors, Stromkirk Captain). Red is the deck's most over-supplied colour,
making this the cheapest possible cut.

### This also closes open question 1

Cutting **Bojuka Bog** costs a *black* source; cutting Clifftop Retreat costs a *red*
one. Black is the scarce colour here and red is oversupplied, so Clifftop Retreat is
the better cut **regardless** of whether any opponent plays a graveyard deck. The
question no longer needs an answer for this swap.

### Revised package — unchanged at $49.65

| Add | Price | Cut |
|---|---|---|
| Takenuma, Abandoned Mire | $11.17 | Mountain |
| Phyrexian Tower | $28.15 | **Clifftop Retreat** (was Sundown Pass) |
| Black Market Connections | $10.33 | Lightning Bolt |

Prices re-fetched 2026-09-03 23:03 UTC: Sundown Pass $2.48 · Clifftop Retreat $0.23 ·
Dragonskull Summit $0.46 · Battlefield Forge $0.32 · Haunted Ridge $8.38 ·
Smoldering Marsh $0.28 · Sacred Foundry no price listed.
