# markov_chains — Susur Secundi, Void Altar, 2026-09-05

Question asked: *"markov_chains — Susur Secundi, Void Altar"*, phrased as two
candidates. **It is one card**, not two: Scryfall returns the same object for
"Susur Secundi" and for "Void Altar". So this is a single-candidate review.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line. Preference: on-theme Vampires as a tiebreaker only.

**Meta carried forward from prior reviews (user-stated, not assumed):** games in
this pod run **long**; **Armageddon and Farewell are both commonly played**;
several opponents are **mono-white**; the deck is dual-mode (Edgar-on-board
aggro / Edgar-absent aristocrats drain).

**On whether to re-confirm the speed premise.** The rubric says to stop and ask
when a rejection leans on "too slow." I am not asking here, deliberately: the
premise was already corrected by the user in the 2026-08-30 review and the
correction is *favourable* to this card. Everything below grades Susur against
the long-game version of the pod, and it is still a no. The reasons that kill it
— rate when fully online, and the mana base — do not improve with more turns.

All oracle text, legality, colour identity and prices fetched live from Scryfall
**2026-09-05 13:55–13:59 UTC**. Nothing below is from memory.

---

## Verdict

| Card | Price (2026-09-05) | Verdict |
|---|---|---|
| **Susur Secundi, Void Altar** | $4.87 | **NO** |

One line: *the deck already runs a wipe-proof sacrifice outlet on a land
(Phyrexian Tower) and a `{1}{B}` sacrifice-to-draw outlet (Baron Bertram
Graywater), and Susur is worse than both at their own jobs after a 12-power
setup cost paid in creature taps.*

---

## The card, verified

> **Susur Secundi, Void Altar** — Land — Planet
> This land enters tapped.
> `{T}`: Add `{B}`.
> **Station** (Tap another creature you control: Put charge counters equal to its
> power on this Planet. Station only as a sorcery.)
> **12+** | `{1}{B}`, `{T}`, Pay 2 life, Sacrifice a creature: Draw cards equal to
> the sacrificed creature's power. **Activate only as a sorcery.**

Mana value 0 · Colour identity **B** · **Commander legality: legal** · not a Game
Changer · EDHREC rank 1884 · **$4.87** (foil $5.95), fetched 2026-09-05 13:55 UTC.

Colour identity B is inside Edgar's BRW. `card_facts.py lookup --deck
markov_chains` raised no legality or identity flag. **No hard veto fires** —
legal, in identity, under the $40 cap, not a Game Changer, and `combos.py --add
"Susur Secundi, Void Altar" --near` returns **0 new combos and 0 near** against a
baseline of 2 already assembled, so the "no early infinites" constraint is clear
too. This card is rejected on the tests, not on a veto.

**Scryfall returns no official rulings** for Susur, and none for any of the other
four Planets (`Evendo, Waking Haven`, `Uthros, Titanic Godcore`, `Adagia,
Windswept Bastion`, `Kavaron, Memorial World`). So one point below is
**unverified**: whether a summoning-sick creature can be tapped to Station. By
analogy to crew, tapping *another* permanent as a cost should be legal with
summoning sickness. **I have granted the card this reading throughout** — it is
the favourable one, and it still does not save it. Flagging it because I could
not confirm it from a ruling.

---

## Step 0 — the honest best case

Stated as a claim that could be false:

> *Susur costs a land slot rather than a spell slot, so its floor is a tapped
> Swamp; the deck's most recent structural finding is that it cannot rebuild after
> a board wipe in a pod that plays Farewell; charge counters are not creatures, so
> a stationed Susur survives every wipe; and sacrificing a creature is upside
> rather than cost here, because **twelve** verified cards pay off on a creature
> dying.*

Those twelve, grouped by trigger scope (the count that matters is the second
group — nine of them do not care whose creature dies):

**"a creature you control dies" (3):** Bastion of Remembrance · Grave Pact ·
Zulaport Cutthroat.

**"a/another creature dies," any controller (9):** Blood Artist · Vein Ripper
("Whenever a creature dies, target opponent loses 2 life and you gain 2 life") ·
Cordial Vampire · Blade of the Bloodchief · Elenda, the Dusk Rose · High-Society
Hunter (nontoken only) · Skullclamp (equipped creature only) · Clavileño (the
granted trigger) · Malakir Rebirth (the granted trigger).

Plus Cruel Celebrant ("creature **or planeswalker** you control") and Mirkwood
Bats, which is scoped to **tokens created or sacrificed**, not to deaths — a
different clause that Susur does trigger when the sacrifice is an Edgar token.

That is a real best case. It is the one I attacked.

---

## What killed it

### 1. The wipe-proof-outlet role is already filled, by a land added two days ago

`Phyrexian Tower` — verified 2026-09-05 13:59 UTC:

> Legendary Land · `{T}`: Add `{C}` · **`{T}`, Sacrifice a creature: Add `{B}{B}`**

The 2026-09-03 land review added Tower for *exactly* the role Susur's best case
claims — "a sacrifice outlet that is a land… **Tower is the outlet that
survives**, and that matters specifically because the deck's identified worst-case
is the post-wipe turn." Against Tower, Susur is:

| | Phyrexian Tower | Susur Secundi |
|---|---|---|
| Setup | none | **12 charge counters** |
| Enters | untapped | **tapped** |
| Activation cost | `{T}`, sac | `{1}{B}`, `{T}`, **2 life**, sac |
| Timing | **instant speed** | **sorcery only** |
| Mana | **adds `{B}{B}`** | costs 2 and taps the land |
| Per turn | unlimited (one `{T}`) | one |

Tower converts a Swords to Plowshares aimed at Vein Ripper into two black mana
and every trigger above. Susur cannot do that at all — sorcery-speed activation
means it never responds to anything.

### 2. Fully online, it is worse than a creature already in the deck

`Baron Bertram Graywater`, verified in the 99:

> `{1}{B}`, **Sacrifice another creature or artifact: Draw a card.**

Same mana cost. **No `{T}` symbol**, so it is repeatable as many times per turn as
you have mana. Instant speed. No life payment. No station requirement.

Write both as *effect × frequency × duration*, as the rubric demands:

- **Baron:** draw 1 × unlimited per turn × instant × from the turn it resolves.
- **Susur:** draw N × **once** per turn × **sorcery** × **after 12 power of taps**.

Susur beats Baron only when the sacrificed creature's power is 3 or more, and
only on the one activation per turn. Which brings the density problem.

### 3. Density — the creatures you can spare are the ones worth the fewest cards

Power distribution across the 38 creature cards: **power 0 — 1 · power 1 — 11 ·
power 2 — 10 · power 3 — 6 · power 4 — 4 · power 5 — 2 · power 6 — 1** (3 with no
printed power). The bodies the deck actually has spare are tokens, and the token
makers are: Edgar's eminence (1/1 black Vampire, off **35 Vampire cards**), Edgar
Charmed Groom (1/1 lifelink each upkeep), Bloodline Keeper (2/2 flier), Baron
Bertram (1/1 lifelink), Bastion of Remembrance (1/1), Elenda on death, Charismatic
Conqueror (1/1), Voldaren Estate (Blood).

So the realistic activation is **sacrifice a 1/1 for `{1}{B}` + 2 life at sorcery
speed to draw one card** — which is Baron Bertram's rate, worse in every other
term. Drawing 3+ means sacrificing Vein Ripper (6/5), Patron of the Vein, Malakir
Bloodwitch or a counter-loaded Elenda: your best creatures, the ones the deck is
built to keep on the battlefield.

The counter-argument I checked, and it is the strongest one available: Edgar's
attack trigger ("Whenever Edgar attacks, put a `+1/+1` counter on each Vampire you
control") does make tokens into 3/3s over a few combats, and Cordial Vampire adds
counters on every death. That is the deck's **bridge** between its two modes, and
it genuinely inflates Susur's draws. It also creates the next problem.

### 4. Anti-synergy: Station competes with the attack step that makes the payoff big

Station taps creatures at sorcery speed. The counters that make Susur draw 3
instead of 1 come from **Edgar attacking**. Every creature you tap to Station is a
creature not attacking, which is a `+1/+1` counter not placed on every Vampire you
control, which is the next Station tap being smaller. The card's own payoff
scaling fights its own setup cost.

Granting the favourable summoning-sickness reading (§ the card, verified), you can
mitigate this by stationing post-combat with freshly-cast eminence tokens. That
gets you roughly **1 counter per Vampire spell cast**, so 12 counters is on the
order of a dozen tokens or several turns of holding creatures back. During all of
it the card is a tapped Swamp.

### 5. It does not survive the wipe it claims to survive

The charge counters do persist through Farewell — that part of the best case is
true. But the ability requires **sacrificing a creature**, and after a wipe you
have none. A stationed Susur on an empty board draws zero cards. It rebuilds
nothing; Takenuma, Abandoned Mire (added 2026-09-03) is the card that does that
job. Under Armageddon it is worse still: a tapped land whose activation needs
`{1}{B}` from two *other* lands.

### 6. Cost of entry — it is the 6th unconditionally-tapped land, in the colour that is already fine

Recounted from `produced_mana` in `cards.json` today, on the current 100:

| Colour | Land sources | Pip demand (nonland) |
|---|---|---|
| B | **27** | 64 pips · 4 at `BBB`, 11 at `BB` |
| W | **17** | 15 pips · 14 cards at a single `{W}`, Clever Concealment `{W}{W}` w/ convoke |
| R | **14** | 4 pips · 4 cards, every one a single `{R}` |

Susur adds a **28th black source** — the colour that went 25 → 27 in the last
review and is the best-served axis relative to what changed. And it enters
unconditionally tapped, joining Bojuka Bog, Canyon Slough, Malakir Mire, Nomad
Outpost and Path of Ancestry. The 2026-09-03 land review's finding stands and I am
not going to contradict it two days later: *"In a deck with 13 one-drops and 14
two-drops that is already the ceiling of what it can carry… **No recommendation
below adds a tapped land.**"* Nothing about Susur argues for reopening that.

### 7. Draw is not the thin category, and this deck already rejected a better version of this card

Verified draw sources in the 99: Black Market Connections · Night's Whisper ·
Painful Truths · Skullclamp · Village Rites · War Room · Welcoming Vampire · Baron
Bertram Graywater · High-Society Hunter · Clavileño · Henrika Domnathi · Canyon
Slough (cycling). **Twelve.**

`Castle Locthwain` was rejected on 2026-09-03 for this exact shape — a land with a
late-game draw mode — with the reasoning *"the deck's draw is not the thin
category… and `{1}{B}{B}` plus a tap per card is a slow rate."* Susur is the same
argument with a 12-counter tax bolted on. Rejecting Castle Locthwain and accepting
Susur would be incoherent.

Per the rubric's closing filter: the changes that survive here are
**multiplicative**. Susur is **additive**, landing in a category twelve cards deep.

### 8. The disagreement check

I say no; the community effectively says no *for this commander*. Susur's own
EDHREC page lists **24 top commanders** — Xu-Ifit, Osteoharmonist (64.6%, 3,032 /
4,691), Infinite Guideline Station (22.4%), Betor, Sephiroth, Teysa Karlov (6.7%,
955 / 14,349), Meren, Henzie — Planet/Station decks and big-creature sacrifice
decks. **Edgar Markov is not among them.** On the Edgar Markov commander page
(50,337 decks) and its Sacrifice theme page (222 decks), Susur appears in no list.
No disagreement to resolve.

---

## Cut discipline: there is no cut that makes this work

The rubric says cut within the same role — land for land, and never below the land
count the curve supports. The deck is at **35 lands** with an average nonland MV
of 2.88, so this must be a land-for-land swap.

The only cut candidate worth naming is **Bojuka Bog** — tapped, mono-black, and
flagged in the 2026-09-03 review's own open questions as possibly dead against a
mono-white pod. Even taking it, the swap is *sideways at best*: you trade a tapped
black source with a **free, immediate** ETB for a tapped black source that does
nothing for a dozen creature-taps, and Bojuka Bog is the deck's **only graveyard
hate** — "never cut the last of a role."

**Runners-up, and why each is spared:**

- **Vault of the Archangel** — colourless, but `{2}{W}{B}`, `{T}`: deathtouch and
  lifelink for the whole team is a combat blowout and a Vito/Sanctum Seeker
  amplifier in a 38-creature deck. Spared on impact.
- **War Room** — colourless, but it is repeatable card draw that survives wipes
  and needs no board at all, which is precisely what Susur fails to be.
- **Nomad Outpost** — tapped, but a **three-colour** source including the scarce
  white; cutting it to add a mono-black tapped land makes the mana strictly worse.
- **Path of Ancestry** — tapped, but five colours plus scry on 35 Vampire spells.
- **Voldaren Estate / Takenuma / Phyrexian Tower** — all added or defended in the
  last two reviews for roles Susur does not fill.

Per the rubric: *"if the best cut you can find is a card you would defend in any
other context, that is strong evidence the addition isn't worth it."* That is
where this lands.

---

## Price

**$4.87** (foil $5.95), fetched 2026-09-05 13:55 UTC — comfortably inside the $40
cap. **Price is not load-bearing in this verdict.** The rejection survives the
card being free: the objections are the station cost, the sorcery-speed once-per-
turn rate against Baron Bertram and Phyrexian Tower, and a sixth tapped mono-black
land. If you already own it, the answer is still no.

---

## No counter-proposal, and why

The usual move here is "the role is real, the card is wrong." I do not think the
role is real in this deck. Susur is aimed at *late-game card draw from a land
slot*, and that role was diagnosed and closed on 2026-09-03: twelve draw sources
already, and Takenuma was chosen over Castle Locthwain specifically as the **one**
"Swamp with a late-game mode" the deck should carry. Manufacturing a second
candidate for a slot the deck does not have would be inventing work.

The gap that *is* still open, from the 2026-08-31 audit, is **rebuilding after a
board wipe** — partly addressed by Takenuma (graveyard → hand) and not at all by
Susur. If you want the next land-slot upgrade, the standing answer is still
**Urborg, Tomb of Yawgmoth** as an ADD IF on the $40 cap flexing, unchanged from
2026-09-03.

---

## What would change my mind

Not game length — the pod already plays long games and I graded against that.
Specifically:

1. **A rebuild toward power.** If the creature base moved to reliably 4+ power
   bodies you are happy to sacrifice, Susur's draw stops being "1 card for two
   mana and 2 life."
2. **Planet/Station density.** One Station card with no other Planets is a
   mechanic with no support. Several would change the arithmetic on the setup.
3. **A ruling that Station can be paid at instant speed** — it cannot; the reminder
   text says "Station only as a sorcery," and the ability itself says "Activate
   only as a sorcery."

I am also unsure about one thing and would like to be corrected if I have it
wrong: **can a summoning-sick creature be tapped to Station?** Scryfall lists no
rulings for any of the five Planets. I assumed **yes** throughout, which is the
reading most favourable to the card. If the answer is no, Susur is worse than
described here, not better.

---

## Figures used

Prices fetched **2026-09-05 13:55–13:59 UTC**: Susur Secundi, Void Altar $4.87
(foil $5.95) · Phyrexian Tower $27.92 · Vein Ripper $6.81 · Skullclamp $5.74 ·
Elenda, the Dusk Rose $5.89 · Blade of the Bloodchief $7.75 · Edgar Markov $40.68 ·
Bojuka Bog $1.26 · Vault of the Archangel $0.83 · Mirkwood Bats $1.43. Other
Planets: Evendo $19.75 · Uthros $13.98 · Adagia $5.54 · Kavaron $1.39.

EDHREC: Susur overall rank **1884**; its top-commanders list (24 entries) does not
include Edgar Markov — leaders are Xu-Ifit, Osteoharmonist 64.6% (3,032/4,691),
Edea 29.0% (1,244/4,285), Infinite Guideline Station 22.4% (2,280/10,166), Teysa
Karlov 6.7% (955/14,349). Edgar Markov commander page: **50,337 decks**; Sacrifice
theme page: **222 decks**; Susur in neither. Deck already runs 10/10 high-synergy
and 9/10 top cards on the commander page, 10/10 and 10/10 on the Sacrifice theme.

Commander Spellbook via `combos.py`: baseline **2 combos assembled**; Susur
completes **0 new** and **0 near**.

`base.txt` was not modified.
