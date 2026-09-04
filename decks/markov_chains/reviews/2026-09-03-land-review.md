# markov_chains — land review, 2026-09-03

Question asked: *"are there any lands that would best improve this deck?"* — open
diagnosis, no candidate named. So this works the same direction as the
2026-08-31 structural audit: model the mana base, find the roles it is thin in,
then look for lands that fill them.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line.

**Meta carried forward from prior reviews (user-stated, not assumed):** games in
this pod run **long**; **Armageddon and Farewell are both commonly played**;
several opponents are **mono-white**; the deck is dual-mode (Edgar-on-board
aggro / Edgar-absent aristocrats drain).

All oracle text, legality, colour identity and prices fetched live from Scryfall
**2026-09-03 22:10–22:15 UTC**. Nothing below is from memory.

---

## Verdict summary

| Land | Price (2026-09-03) | Verdict |
|---|---|---|
| **Takenuma, Abandoned Mire** | $11.17 | **ADD** — cut **Mountain** |
| **Phyrexian Tower** | $28.15 | **ADD** — cut **Sundown Pass** |
| **Urborg, Tomb of Yawgmoth** | $55.92 | **ADD IF** the $40 cap flexes |
| Cavern of Souls | $50.06 | NO |
| Command Beacon | $9.68 | NO |
| Castle Locthwain | $4.43 | NO |
| Secluded Courtyard / Unclaimed Territory | $0.26 / $0.29 | NO |
| Bloodstained Mire / Marsh Flats / Prismatic Vista | $17.59 / $32.66 / $32.85 | NO |
| Cabal Coffers | $32.89 | NO |
| Mutavault | $3.98 | NO |
| Ancient Tomb | $133.66 | NO |
| Rogue's Passage · Westvale Abbey · High Market · Savai Triome · Restless Fortress · Accursed Duneyard · Shizo · Volrath's Stronghold · Agadeem's Awakening · Hagra Mauling · Brightclimb Pathway | — | NO |

---

## Where the mana base actually stands

Counted from `produced_mana` in `cards.json`. **35 lands** (plus Malakir Rebirth,
whose land side is incidental — it is played as the instant).

| Colour | Land sources | + nonland | Total | Demand |
|---|---|---|---|---|
| B | 25 | Arcane Signet, Talisman of Hierarchy, Talisman of Indulgence, Dark Ritual, Master of Dark Rites | **30** | 63 pips · **15 cards at `BB` or worse, 4 at `BBB`** |
| W | 18 | Arcane Signet, Talisman of Conviction, Talisman of Hierarchy | **21** | 15 pips · 15 cards · **only Clever Concealment needs `WW`, and it has convoke** |
| R | 16 | Arcane Signet, Talisman of Conviction, Talisman of Indulgence | **19** | 5 pips · **5 cards, every one a single `{R}`** |

The four `BBB` costs, verified: Bloodletter of Aclazotz `{1}{B}{B}{B}`, Grave Pact
`{1}{B}{B}{B}`, Vampire Nocturnus `{1}{B}{B}{B}`, Vein Ripper `{3}{B}{B}{B}`.
Eleven more at `BB`.

The five red cards, verified: Lightning Bolt `{R}`, Impact Tremors `{1}{R}`,
Florian `{1}{B}{R}`, Stromkirk Captain `{1}{B}{R}`, Edgar Markov `{3}{R}{W}{B}` —
and Edgar's **eminence works from the command zone** ("if Edgar is in the command
zone or on the battlefield"), so he is frequently never cast at all.

**The audit's Finding 2 was acted on and it worked** — Mountain went 3 → 1, Swamp
6 → 7, red land sources 18 → 16. But the ratio is still lopsided: **16 red sources
for five single-pip red cards, 25 black for fifteen double-and-triple-pip black
cards.** There are still two red sources' worth of slack to spend, and this review
spends it.

### Quality caveats on the black 25

Three of the 25 are not unconditional:

- **Fetid Heath** is a filter — `{W/B}, {T}: Add {W}{W}, {W}{B}, or {B}{B}`. It
  needs another coloured source to function.
- **Exotic Orchard** — "any color that a land **an opponent controls** could
  produce." Opponent-dependent.
- **Voldaren Estate** — coloured mana only "to cast a **Vampire** spell," and it
  costs 1 life.

So the honest unconditional-black count is **22**, not 25.

### The tapped-land tax

Enters unconditionally tapped: Bojuka Bog, Canyon Slough, Malakir Mire, Nomad
Outpost, Path of Ancestry (5), plus three shocklands that can be paid for. In a
deck with 13 one-drops and 14 two-drops that is already the ceiling of what it can
carry — a point the audit made against Orzhov Basilica, which is now gone. **No
recommendation below adds a tapped land.**

---

## The standing structural gap, and the land that fills it

The 2026-08-31 audit's **Finding 1 — "the deck cannot rebuild after a board wipe.
At all."** — is still open. Its proposed fix (Patriarch's Bidding) was withdrawn
the same day, and nothing replaced it. Re-verified today, the graveyard-facing
cards are still exactly two:

| Card | Verified text | What it actually is |
|---|---|---|
| **Bloodghast** | "Landfall — Whenever a land **you control** enters, you may return **this card** from your graveyard to the battlefield." | self-recursion only |
| **Bojuka Bog** | "When this land enters, exile **target player's** graveyard." | outward hate |

Zero cards return another creature from the graveyard.

### ADD — Takenuma, Abandoned Mire · $11.17 · cut **Mountain**

Verified text:

> Legendary Land
> `{T}`: Add `{B}`.
> **Channel** — `{3}{B}`, Discard this card: Mill three cards, then return a
> creature or planeswalker card from your graveyard to your hand. This ability
> costs `{1}` less to activate for each **legendary creature you control**.

**Why this one and not Patriarch's Bidding.** Bidding was rejected for two
reasons: Farewell *exiles*, leaving it with nothing to return, and against the
pod's mono-type tribal decks its symmetry is fully live. Takenuma has neither
problem, and the reason is structural — **it costs a land slot, not a spell slot.**
Its floor is "a Swamp." A card whose floor is a Swamp cannot be blanked; when the
graveyard is empty you tap it for `{B}` and nothing was lost. Bidding at five mana
in hand against a Farewell deck is a dead card; Takenuma in hand against the same
deck is a land drop.

It is also asymmetric — it returns *your* creature to *your* hand — so the tribal
objection that killed Bidding does not apply.

**Cost reduction is real here.** Nine legendary creatures in the 99: Anowon,
Baron Bertram Graywater, Clavileño, Edgar Markov, Edgar Charmed Groom, Elenda,
Florian, Henrika Domnathi, Vito. With one on board the channel is `{2}{B}`; with
two, `{1}{B}`. This is a deck that reliably has legends out.

**What it recurs.** The targets that matter are the bombs the deck cannot
otherwise replace: Vein Ripper, Bloodthirsty Conqueror, Vampire Nocturnus,
Bloodletter of Aclazotz, Elenda. In a pod where games run long, drawing the second
copy of your best creature out of the graveyard for three mana is exactly the
grind-mode fuel `meta.json` describes.

**What it does not do:** it dodges Grafdigger's Cage (graveyard → *hand*, not
battlefield) but not Bojuka Bog, and it does not answer Farewell's exile clause
any better than anything else does. It is recursion, not protection.

**The cut: Mountain.** Checked downstream, all three conditions still hold without
it:

- **Clifftop Retreat** — "unless you control a Mountain **or a Plains**": 4 Plains,
  plus Sacred Foundry (Mountain Plains) and Blood Crypt / Canyon Slough /
  Smoldering Marsh, all typed Mountain. ✓
- **Dragonskull Summit** — "a Swamp or a Mountain": 7 Swamps. ✓
- **Smoldering Marsh** — "two or more **basic** lands": 11 basics remain. ✓
- **Vampire Nocturnus** — cares only that the top card is *black*; every land is a
  colourless card whatever its type. Unaffected. ✓

Net: red land sources 16 → 15, black 25 → 26. Red is still three times its demand.

**EDHREC:** 8.2% of Edgar Markov decks (4,107 / 50,203). Low — but EDHREC reports
popularity, and this deck has a specific hole that 92% of Edgar decks presumably
fill with an actual reanimation spell.

**No combo risk:** `combos.py --add "Takenuma, Abandoned Mire" --near` returns 0
new and 0 near. Veto clear.

---

### ADD — Phyrexian Tower · $28.15 · cut **Sundown Pass**

Verified text:

> Legendary Land
> `{T}`: Add `{C}`.
> `{T}`, **Sacrifice a creature**: Add `{B}{B}`.

**The role: a sacrifice outlet that is a land.** Verified free repeatable outlets
currently in the deck — exactly three, all small creatures:

| Outlet | Cost |
|---|---|
| Carrion Feeder | free — "Sacrifice a creature: Put a +1/+1 counter on this creature." |
| Viscera Seer | free — "Sacrifice a creature: Scry 1." |
| Bloodthrone Vampire | free — "Sacrifice a creature: This creature gets +2/+2." |
| Indulgent Aristocrat | `{2}` per activation |

All three free outlets are 1- and 2-mana creatures that die to every wipe and every
piece of spot removal. **Tower is the outlet that survives**, and that matters
specifically because the deck's identified worst-case is the post-wipe turn.

**Concretely, it is also the answer to targeted exile.** Vein Ripper and
Bloodthirsty Conqueror are the deck's two bombs and the pod's obvious Swords to
Plowshares targets. With Tower untapped you sacrifice in response and convert the
removal into two black mana plus every death trigger below, instead of losing the
card for nothing.

**Verified payoffs it feeds** (four named, scopes checked):

- **Blood Artist** — "Whenever **this creature or another creature** dies, target
  player loses 1 life and you gain 1 life." *Any* creature, not just yours.
- **Bastion of Remembrance** — "Whenever a creature **you control** dies, **each
  opponent** loses 1 life and you gain 1 life." Yours only, but hits all three.
- **Cordial Vampire** — "Whenever this creature **or another creature** dies, put a
  +1/+1 counter on each Vampire you control." Any creature.
- **Mirkwood Bats** — "Whenever you **create or sacrifice a token**, each opponent
  loses 1 life." Note the scope: this is tokens, not deaths, and Tower sacrificing
  an Edgar eminence token triggers it.

And **Bloodghast**, which Tower turns into a recurring engine: sacrifice it for
`{B}{B}`, return it on the next land drop, repeat. Once per land drop, so no loop
— confirmed below.

**On the objection that it is a colourless land.** This is the real cost and it
should be stated plainly: the deck already has three lands that do not make
coloured mana normally (War Room, Vault of the Archangel, Voldaren Estate for
non-Vampire spells), and it has four `BBB` costs. A fourth would be a genuine
problem in most decks.

It is not one here, because **this deck manufactures spare bodies as a matter of
course.** Edgar's eminence — "Whenever you cast **another Vampire spell**, if Edgar
is in the command zone or on the battlefield, create a 1/1 black Vampire token" —
fires from the command zone, off 35 Vampire cards. Bloodline Keeper taps for a 2/2
every turn. Edgar Markov's Coffin makes one each upkeep. In practice Tower is a
black source that costs a token you were already looking for a way to sacrifice,
and paying that cost is upside, not downside.

**The cut: Sundown Pass** ($2.48). It is the most replaceable of the four R/W
duals (Battlefield Forge, Clifftop Retreat, Sacred Foundry, Sundown Pass), it
enters tapped until you have two other lands, and it is the only one of the four
that is neither a painland with a colourless mode nor a shockland with basic types
that other lands check for. Its mana serves red — the colour with 16 sources and 5
single pips.

**Runner-up cut: Nomad Outpost.** It enters unconditionally tapped, and its
three-colour fixing duplicates Command Tower, Exotic Orchard, Path of Ancestry and
Voldaren Estate. Cutting it is the better *tempo* choice; cutting Sundown Pass is
the better *colour* choice, because Nomad Outpost is a black source and black is
the scarce colour. Take Nomad Outpost instead only if tapped lands are what
actually loses you games.

**EDHREC:** **27.7% of Edgar Markov decks** (13,910 / 50,203), and Edgar is the
#2 commander for the card overall. Strong community calibration.

**No combo risk:** `combos.py --add "Phyrexian Tower" --near` returns 0 new and 0
near. Baseline stays at 2 assembled combos. Veto clear.

---

### After both swaps

Still 35 lands. No new tapped land.

| Colour | Before (land) | After (land) | Demand |
|---|---|---|---|
| B | 25 | **26** | 15 cards at `BB`+, 4 at `BBB` |
| W | 18 | **17** | 15 single-`{W}` cards + Clever Concealment `{W}{W}` w/ convoke |
| R | 16 | **14** | 5 single-`{R}` cards |

White at 17 is the number to sanity-check, and it holds: fourteen of the fifteen
white cards need exactly one `{W}`, and the fifteenth has convoke. Red at 14 is
still nearly three times demand.

Gained: the deck's first real recursion, and a wipe-proof sacrifice outlet.
Combined cost **$39.32**, both under the $40 per-card cap.

---

## ADD IF — Urborg, Tomb of Yawgmoth · $55.92 · **$15.92 over the cap**

> Legendary Land
> Each land is a Swamp in addition to its other land types.

This is the single largest improvement available to this mana base and the only
card that solves the `BBB` problem outright: **black land sources go 25 → 35**,
because every land in the deck taps for `{B}`. It also upgrades Fetid Heath from a
filter that needs help into a land that makes `{B}{B}` on its own, and makes
Dragonskull Summit and Smoldering Marsh unconditional.

The reason this is ADD IF and not ADD is the **$40 cap, and nothing else.** The
card is correct for the deck on every other axis. Precedent exists — Teferi's
Protection was added at $49.02, $9.02 over — so this is your call, not a
structural objection. If the cap flexes, Urborg goes in over Phyrexian Tower, and
the cut is **Sundown Pass** just the same.

Caveat worth knowing: it is symmetric. Opponents' lands become Swamps too, which
in this pod is mostly irrelevant (mono-white opponents gain nothing from it) but
does turn on their own Bojuka Bogs against you.

---

## The rejections, with reasons

**Cavern of Souls — $50.06 — NO.** Over the cap, and unlike Urborg the effect is
partly redundant here: Path of Ancestry and Voldaren Estate already fix for
Vampire spells, and the uncounterable clause is worth much less in a 4-player
casual pod than at a cEDH table. It would be a fine card; it is not $50 of
improvement over the land it replaces.

**Command Beacon — $9.68 — NO.** The premise is that recasting Edgar matters.
Verified, it does not: eminence reads "**if Edgar is in the command zone** or on
the battlefield," so the token engine runs without ever casting him. Beacon would
be a colourless land that saves commander tax on a card the deck is content to
leave in the zone.

**Castle Locthwain — $4.43 — NO.** A close call, and the closest of the
rejections. It is a genuine black source with a repeatable draw, and it would go
in over a Swamp. But the deck's draw is not the thin category — Night's Whisper,
Painful Truths, War Room, Skullclamp, Welcoming Vampire, Florian, Canyon Slough's
cycling and Clavileño's death trigger is eight sources — and `{1}{B}{B}` plus a tap
per card is a slow rate. Takenuma occupies the same "Swamp with a late-game mode"
slot and fills a category the deck has **zero** of. One such land, not two.

**Secluded Courtyard $0.26 / Unclaimed Territory $0.29 — NO.** Verified: coloured
mana "**only to cast a creature spell of the chosen type**." That is 38 of the 64
nonland cards and none of Grave Pact, Teferi's Protection, Akroma's Will, Swords
to Plowshares or Anguished Unmaking. It would replace a land that casts everything
with one that casts most things, to fix a colour axis that is not where the strain
is. Voldaren Estate already covers this role.

**Bloodstained Mire $17.59 / Marsh Flats $32.66 / Prismatic Vista $32.85 — NO.**
The Bloodghast angle is real — a fetch is two landfall triggers, and the second is
at instant speed on a turn of your choosing, which is a genuine rebuy after
sacrificing it. But a fetch does not *add* a black source, it finds one, and it
costs a life on top of six painlands and shocklands and War Room. In a deck whose
problem is source *count*, spending a land slot on a card that keeps the count flat
is the wrong trade at these prices.

**Cabal Coffers — $32.89 — NO.** Eleven Swamp-typed lands. `{2}`, `{T}` for
roughly four black is fine, not the format-warping engine it is in mono-black, and
it does nothing on an empty board. (Note this one flips if Urborg is added —
Coffers + Urborg is the classic pairing and would then tap for 35. Revisit only in
that world.)

**Mutavault — $3.98 — NO.** "Becomes a 2/2 with **all creature types**" does make
it a Vampire for Legion Lieutenant, Captivating Vampire, Stromkirk Captain and Lord
of Lineage, and it dodges wipes. But it is another colourless land in a `BBB` deck,
and a 2/2 for `{1}` that has to be re-activated every turn is not what a deck with
38 creatures is short of.

**Ancient Tomb — $133.66 — NO.** Over the cap by more than triple, and it is a
Game Changer (would be 2 of 3 for bracket 3). Colourless mana in a `BBB` deck.

**Rogue's Passage, Westvale Abbey, High Market, Savai Triome, Restless Fortress,
Accursed Duneyard, Shizo, Volrath's Stronghold, Agadeem's Awakening, Hagra Mauling,
Brightclimb Pathway — NO.** Each fails on the same axis: a colourless or tapped
land bought for an ability the deck either does not need (Rogue's Passage
unblockable, in a deck that wins by draining rather than connecting; Accursed
Duneyard regeneration for `{2}`) or already has covered (High Market is a strictly
worse Phyrexian Tower here; Volrath's Stronghold is Takenuma at a worse rate and on
the Reserved List with no price listed; Westvale Abbey's five-creature sacrifice
competes with the drain payoffs for the same bodies). Savai Triome and Brightclimb
Pathway are fixing for colours that are already over-fixed.

---

## What I am unsure about, and what would settle it

1. **Whether Bojuka Bog is still worth its slot.** It is a black source, but it
   enters unconditionally tapped and its ability is graveyard hate pointed at a pod
   the reviews describe as mono-white. If none of your three regular opponents
   recurs from the graveyard, Bojuka Bog is a tapped Swamp and it becomes a better
   cut than Sundown Pass for Phyrexian Tower — which would also keep white at 18.
   **What would settle it: do any of your regular opponents play a graveyard deck?**

2. **Whether the $40 cap is a real constraint or a default.** Teferi's Protection
   went in at $49.02. If the cap is soft, Urborg is a bigger upgrade than either
   card recommended here, and the ranking changes to Urborg first.

---

## Prices and figures used (all fetched 2026-09-03 22:10–22:15 UTC)

Takenuma, Abandoned Mire $11.17 · Phyrexian Tower $28.15 · Urborg, Tomb of
Yawgmoth $55.92 · Cavern of Souls $50.06 · Prismatic Vista $32.85 · Cabal Coffers
$32.89 · Marsh Flats $32.66 · Shizo, Death's Storehouse $32.95 · Bloodstained Mire
$17.59 · Savai Triome $18.05 · Command Beacon $9.68 · Castle Locthwain $4.43 ·
Brightclimb Pathway $4.64 · Mutavault $3.98 · Westvale Abbey $3.82 · Sundown Pass
$2.48 · Hagra Mauling $1.72 · Bojuka Bog $1.20 · Vault of the Archangel $0.83 ·
High Market $0.47 · Restless Fortress $0.65 · Accursed Duneyard $0.43 · Rogue's
Passage $0.36 · Nomad Outpost $0.32 · Unclaimed Territory $0.29 · Secluded
Courtyard $0.26 · Ancient Tomb $133.66 · Agadeem's Awakening $27.07 · Volrath's
Stronghold no price listed (Reserved List).

EDHREC (Edgar Markov page, 50,203 decks): Phyrexian Tower 27.7% (13,910) ·
Takenuma 8.2% (4,107). Commander Spellbook via `combos.py`: baseline 2 combos
assembled; Phyrexian Tower and Takenuma each complete 0 new and 0 near.

`base.txt` was not modified.
