# markov_chains — structural audit, 2026-08-31

> ⚠️ **Finding 1's recommendation is WITHDRAWN (same day).** See
> `2026-08-31-teferis-protection.md`, Addendum 1. The user subsequently stated
> that **Farewell** and **Armageddon** are commonly played in this pod and that
> several opponents run **single-type tribal** decks. Farewell *exiles* creatures
> (and can exile all graveyards), so **Patriarch's Bidding has nothing to return**;
> and against a mono-type tribal opponent its symmetry is fully live — they name
> their one type and rebuild their entire creature graveyard. **Patriarch's
> Bidding is now a flat NO.** The replacement recommendation is **Teferi's
> Protection** (the only card that answers Armageddon), cutting Orzhov Basilica.
> Findings 2 and 3 are unaffected and still stand.

Question asked: *"what are ways this deck could be improved?"* — an open diagnosis,
not a candidate evaluation. No card was proposed by the user, so this works the
other direction: model the deck, find the roles it is thin in, and only then look
for cards.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line.

**Meta as corrected in the 2026-08-30 review (Addendums 2 and 6), which this audit
adopts:** games in this pod run **long**; several opponents play **mono-white**,
both token swarms and big-creature builds; and the deck is **dual-mode** — Edgar
resolved turns it into aggro with large creatures via his attack trigger, Edgar
absent turns it into an aristocrats slow-bleed, with the +1/+1 counter package
(Cordial Vampire, Patron of the Vein, Indulgent Aristocrat) as the hinge.

All oracle text, legality, colour identity and prices fetched from Scryfall
2026-08-31 04:40–04:43 UTC. Composition counted from `decks/markov_chains/cards.json`
(built 2026-08-30 23:56, current with `base.txt`). EDHREC from
`commanders/edgar-markov`, n = 50,082, and its Aristocrats theme, n = 1,457.
Combos via Commander Spellbook `find-my-combos`.

---

## Headline

**The deck is not missing staples.** Against EDHREC's Edgar page it runs
**10 of 10** high-synergy cards and **8 of 10** top cards; against the Aristocrats
theme, **10 of 10** high-synergy and **9 of 10** top cards. The only two top cards
it does not run are Charismatic Conqueror (57.2% / 69.1%) and Drana, Liberator of
Malakir (54.3%). There is no shopping list here — improvement has to come from
structure, not from cards the deck forgot.

Three findings, ranked by how much they change games:

1. **The deck cannot rebuild after a board wipe. At all.** — one real fix
2. **Red and white are massively over-supported in the mana base; black, which has
   four `BBB` costs, is not** — free to fix, costs nothing but basics
3. **Orzhov Basilica is the worst card in the deck** — the natural cut for any add

Everything else I checked is already fine, and that list is at the bottom so you
don't spend money on it.

---

## Finding 1 — zero board recovery

This is the one that matters.

### The count

Grepped every oracle face in `cards.json` for `graveyard`. **Two hits, total:**

| Card | Text |
|---|---|
| **Bloodghast** | "Landfall — Whenever a land you control enters, you may return **this card** from your graveyard to the battlefield." |
| **Bojuka Bog** | "When this land enters, exile target player's graveyard." |

Bloodghast returns **only itself**. Bojuka Bog is graveyard *hate*, pointed
outward. So: **the deck has exactly zero cards that return another creature from
the graveyard.**

The prior review counted Edgar, Charmed Groom as a second recursion source. That
is wrong and I am correcting it here — verified text: "When Edgar dies, return
**it** to the battlefield transformed." It returns itself, from the battlefield,
as an artifact. It is self-recursion, not deck recursion.

Protection against a wipe is thin but not absent:

- **Akroma's Will** `{3}{W}` — mode two is "lifelink, indestructible, and
  protection from each color," available whether or not you control a commander
  (the commander clause only lets you take **both** modes). This is a real answer
  to a wrath, at instant speed.
- **Malakir Rebirth** `{B}` — saves exactly one creature.

So the full picture is **one mass-protection instant, one single-creature save,
and no way to recover if neither is in hand.**

### Why this is the deck's real hole and not a generic complaint

Three things stack here:

- **37 creatures**, and the deck's whole plan is board presence. There is no
  non-creature backup win.
- **The pod runs long and is mono-white heavy.** White is *the* wrath colour.
  A meta that reversed three verdicts last review for being grindier than
  `meta.json` claims is also a meta with more wipes in it.
- **The engine pieces are not fungible.** The standard Edgar rebuttal — "eminence
  means you recast two Vampires and get four bodies" — is true for bodies and
  false for effects. Blood Artist, Sanctum Seeker, Bloodletter of Aclazotz,
  Cordial Vampire and Bloodthirsty Conqueror are singleton effects. Eminence
  tokens replace the width; nothing replaces those.

### The candidates, all verified this session

| Card | Cost | Price | One-sided? | Note |
|---|---|---|---|---|
| **Patriarch's Bidding** | `{3}{B}{B}` | $3.92 | no | "Each player chooses a creature type. Each player returns all creature cards of a type chosen this way from their graveyard to the battlefield." |
| Living Death | `{3}{B}{B}` | $3.59 | no | Sacrifices all creatures first, then returns all exiled. A wrath *and* a rebuild. |
| Immortal Servitude | `{X}{W/B}{W/B}{W/B}` | $0.42 | **yes** | "Return each creature card with mana value X." Hybrid pips — castable off pure black. |
| Return to the Ranks | `{X}{W}{W}` | $0.82 | **yes** | Convoke, MV ≤ 2 only. |
| Twilight's Call | `{4}{B}{B}` | $0.69 | no | Strictly worse Bidding here. |

**Recommended: Patriarch's Bidding.** The case, and the honest counter-case:

*For.* 34 of the deck's 37 creatures are Vampires (the three exceptions are
Carrion Feeder — Zombie, Mirkwood Bats — Bat, Zulaport Cutthroat — Human Rogue
Ally). Bidding returns the entire Vampire graveyard for five mana regardless of
mana value, which no other option on that list does. Against the **mono-white
token** half of the pod the symmetry is close to free: tokens cease to exist and
never become graveyard *cards*, so a token swarm gets very little back. And the
returned board arrives with Cordial Vampire, Blood Artist and Sanctum Seeker
attached to it, which is the difference between a board and an engine.

*Against.* It is a five-mana sorcery that does nothing before your graveyard fills,
it is a dead card in an opening hand, and against the **big-creature** mono-white
decks the symmetry is genuinely bad — they get their fatties back too. The deck
has only 5 cards at MV 5 and 2 at MV 6; this makes it 6.

Immortal Servitude is the one-sided alternative and the creature curve suits it
unusually well — 6 creatures at MV 1, 7 at MV 2, 8 at MV 3, so X=3 returns up to
eight bodies. It costs 6 mana to do that and returns strictly less than Bidding.
It is the pick if the symmetry worries you more than the rate does.

**Verdict: ADD IF wipes are actually happening.** This is a real condition, not a
hedge — the entire case rests on one number I do not have. If your board gets
wiped in most games, Bidding is the best card not in this deck by a distance. If
it happens once in ten games, it is a dead five-drop and the answer is no. See the
question at the end.

Combo check: `combos.py --add` — Patriarch's Bidding, Living Death, Immortal
Servitude, Drana and Boromir each complete **zero** new combos. Baseline stays at
2 (Vito + Bloodthirsty Conqueror; Marauding Blight-Priest + Bloodthirsty
Conqueror). The no-early-infinites veto is not engaged by anything here.

### One candidate I checked and am ruling out on a misread most people make

**Flawless Maneuver** `{2}{W}`, $20.69 — "If you control a commander, you may cast
this spell without paying its mana cost." **Edgar's eminence works from the command
zone, which is where he spends most games.** You do not control a commander, so
this is a full-price 3-mana instant most of the time. If you want a second
protection instant, **Unbreakable Formation** ($1.54) does the same job with no
such clause. But Akroma's Will already fills the protection role — the gap is
recovery, not prevention, and a second prevention card does not fix it.

---

## Finding 2 — the mana base is supporting the wrong colours

Free to fix. Counted from `produced_mana` in `cards.json`.

**Supply** (37 land slots, counting Malakir Mire; plus nonland sources):

| Colour | Land sources | + nonland | Total |
|---|---|---|---|
| B | 25 | Arcane Signet, Talisman of Hierarchy, Talisman of Indulgence, Dark Ritual, Master of Dark Rites | **30** |
| W | 18 | Arcane Signet, Talisman of Conviction, Talisman of Hierarchy | **21** |
| R | 18 | Arcane Signet, Talisman of Conviction, Talisman of Indulgence | **21** |

**Demand** (63 B pips · 13 W · 6 R):

- **Black — 16 cards at `BB` or worse, four of them at `BBB`:** Bloodletter of
  Aclazotz `{1}{B}{B}{B}`, Grave Pact `{1}{B}{B}{B}`, Vampire Nocturnus
  `{1}{B}{B}{B}`, Vein Ripper `{3}{B}{B}{B}`.
- **White — 14 cards, and not one of them needs two white pips.** Max demand is a
  single `{W}`.
- **Red — 5 cards, and not one needs two red pips:** Crackling Doom, Florian,
  Impact Tremors, Lightning Bolt, Stromkirk Captain. (Edgar himself is `{3}{R}{W}{B}`,
  but he is usually not cast.)

So red has **21 sources to satisfy 5 single-pip cards**, and black has 30 to
satisfy sixteen double-and-triple-pip cards. That is backwards.

**Fix: 2 Mountain → 2 Swamp.** Red land sources 18 → 16 (18 total, still ample for
five single-`{R}` cards); black 25 → 27 (32 total). Cutting all three Mountains is
also defensible and leaves red at 15 lands / 18 sources.

I checked this does not break anything downstream: **Clifftop Retreat** wants
"a Mountain **or a Plains**" and the 3 Plains cover it; **Dragonskull Summit** wants
"a Swamp or a Mountain" and gets *more* reliable; **Smoldering Marsh** just wants
two basics. **Vampire Nocturnus** is unaffected — it cares about the top card being
black, and lands are colourless cards whatever their type.

This costs nothing and makes your four `BBB` spells meaningfully more castable.
It is the highest ratio of gain to cost available to this deck.

---

## Finding 3 — Orzhov Basilica is the worst card in the list

`{T}: Add {W}{B}`, but: "This land enters tapped. When this land enters, return a
land you control to its owner's hand."

In a deck with **13 one-drops and 14 two-drops** — the lowest, widest curve in the
list — that is a full turn of tempo plus a land off your board, to fix colours
that Finding 2 shows are already over-fixed. Six lands enter unconditionally
tapped (Bojuka Bog, Canyon Slough, Malakir Mire, Nomad Outpost, Orzhov Basilica,
Path of Ancestry); of those, Basilica is the only one whose upside is mana it
doesn't need.

At 36 lands with average nonland MV **2.83** and 7 nonland mana sources, the deck
can afford to be at 35. **Orzhov Basilica is the cut for any add in this review** —
including Patriarch's Bidding, which lands the deck at 35 lands / 64 nonland
cards without touching a single spell.

That matters because it means **the Finding 1 add does not force you to cut a
spell you like.** Runner-up cuts if you would rather stay at 36 lands: Vicious
Conquistador (a 1/1 that drips 1 damage per attack — the prior review spared it
only as a turn-one Vampire body) or Unexplained Absence (`{3}{W}`, exiles one
nonland permanent per player but hands each of them a cloaked 2/2 — giving 2/2s to
the token decks you are trying to beat; EDHREC rank 6670, the most obscure card in
the deck).

---

## Reopened: Charismatic Conqueror

Flagging this for consistency rather than recommending it outright.

Charismatic Conqueror was rejected in the 2026-08-30 review — the one file that is
no longer on disk, so **its reasoning cannot be checked.** What *is* on the record
is that the same review ran on the premise `meta.json` states, and that Addendum 2
of the vampire-seven review reversed **three** verdicts (Malakir Bloodwitch, Elenda,
Grave Pact) on discovering that premise was wrong: long games, mono-white
opponents. **Charismatic Conqueror was never re-run against the corrected premise.**

Verified text, `{1}{W}` 2/2 Vigilance Vampire Soldier: *"Whenever an artifact or
creature an opponent controls enters **untapped**, **they may tap that permanent**.
If they don't, you create a 1/1 white Vampire creature token with lifelink."*

Reading the scope axes properly, because they cut both ways here:

- **Whose permanents:** opponents' — correct, this is a tax on them.
- **Who chooses:** **the opponent does.** A token deck making five tokens can tap
  all five. This is not "you get five Vampires"; it is "you get Vampires *or* their
  board is tapped and cannot block." Against a go-wide deck, both branches are good
  for you, which is why the card is 69.1% in Edgar Aristocrats lists.

Three verified interactions with what is already here: **Baron Bertram Graywater**
("Whenever one or more tokens you control enter, create a 1/1 black Vampire Rogue
token with lifelink" — once each turn), **Welcoming Vampire** (draws when creatures
with power 2 or less enter, once each turn), **Impact Tremors** (1 damage to each
opponent per creature entering, and Bloodletter of Aclazotz doubles that on your
turn). It is also a 2-drop Vampire, so casting it is an eminence trigger.

**Price: $24.43** (fetched 2026-08-31 04:43 UTC). Under the $40 cap. Stating that
separately, as its own factor: the rejection I am reopening was not a price
rejection, and this reopening does not turn on price either.

**Verdict: worth re-running, not an ADD on this pass.** I will not overturn a
verdict whose reasoning I cannot read, on a card I have not modelled against a
named cut, just because the premise behind it shifted. But it is the one rejected
card in this deck's history whose rejection rests on a premise that has since been
proven wrong, and it is aimed squarely at the token decks you are actually facing.
Say the word and I will run it properly.

**Drana, Liberator of Malakir** ($0.84, `{1}{B}{B}`, 54.3% of Edgar decks) is the
other missing top card. I am not recommending it: the deck already has 16 cards at
MV 3 — the fattest rung on the curve — and her payoff (a +1/+1 counter on each
attacking creature on combat damage) duplicates Edgar's own attack trigger and
overlaps Cordial Vampire and Indulgent Aristocrat. The counter package is the one
category this deck is already deep in.

---

## Checked and *not* a problem — don't spend money here

- **Card draw — 12 sources.** Night's Whisper, Painful Truths, Village Rites,
  Skullclamp, Welcoming Vampire, High-Society Hunter, Baron Bertram Graywater,
  Henrika Domnathi (draw mode), Herald's Horn, War Room, Florian (impulse),
  Canyon Slough (cycling). Skullclamp is especially live here — every eminence
  token is a 1/1, so clamping one draws two immediately.
- **Interaction — 9 pieces.** Swords to Plowshares, Lightning Bolt, Anguished
  Unmaking, Feed the Swarm, Crackling Doom, Soul Shatter, Unexplained Absence,
  Oubliette, plus Olivia's Wrath as a one-sided sweeper. Feed the Swarm and
  Anguished Unmaking cover enchantments and artifacts, which is the usual
  mono-black blind spot.
- **Ramp — 7.** Sol Ring, Arcane Signet, three Talismans, Dark Ritual, Master of
  Dark Rites, plus Herald's Horn as cost reduction. Correct for MV 2.83.
- **Sac outlets — 11**, three of them free and repeatable (Carrion Feeder,
  Bloodthrone Vampire, Viscera Seer). Not thin.
- **Curve.** 1→13 · 2→14 · 3→16 · 4→12 · 5→5 · 6→2, average 2.83. Healthy.
- **Bracket compliance.** Zero Game Changers; bracket 3 permits three. Two combos
  assembled, both the late-game Bloodthirsty Conqueror lifegain loops, neither
  tutored. Both `meta.json` vetoes clear, with headroom.
- **Colour identity.** No violations.

---

## Summary

| # | Finding | Fix | Cost | Verdict |
|---|---|---|---|---|
| 1 | Zero graveyard recursion; 37-creature deck with one mass-protection instant | **Patriarch's Bidding**, cut **Orzhov Basilica** | $3.92 | **ADD IF** wipes are frequent |
| 2 | 21 red sources for 5 single-pip red cards; 4 `BBB` costs on 30 black sources | **2 Mountain → 2 Swamp** | free | **DO IT** |
| 3 | Orzhov Basilica: tapped + bounce a land, in a 13-one-drop deck | cut it (36 → 35 lands) | free | **DO IT** |
| — | Charismatic Conqueror rejected under a premise since disproven | re-run on request | $24.43 | reopened, not decided |

Finding 2 is unconditional and free. Finding 3 is unconditional and free. Finding 1
is the only one that needs an answer from you.

## The open question

**How often does your board actually get wiped in these games?** Everything in
Finding 1 turns on it, and nothing else does. Roughly: does a wrath resolve in most
games, or is it a once-in-a-while thing? If it is common, Patriarch's Bidding in
for Orzhov Basilica is the single biggest upgrade available to this list. If it
isn't, it is a dead five-drop and the answer is a flat no.

A second thing that would sharpen the Charismatic Conqueror question: of the
mono-white decks, how many are the **token swarm** builds versus the big-creature
builds? Conqueror is excellent against the former and mediocre against the latter.

## Sources

- Scryfall via `card_facts.py lookup`, fetched 2026-08-31 04:40–04:43 UTC:
  Patriarch's Bidding $3.92 · Living Death $3.59 · Immortal Servitude $0.42 ·
  Return to the Ranks $0.82 · Twilight's Call $0.69 · Unbreakable Formation $1.54 ·
  Clever Concealment $4.72 · Kindred Dominance $4.74 · Boromir, Warden of the Tower
  $6.18 · Drana, Liberator of Malakir $0.84 · Flawless Maneuver $20.69 ·
  Charismatic Conqueror $24.43 · Shared Animosity $4.46 · Teferi's Protection
  $48.47 (**over the $40 cap**, and a Game Changer).
- `Bloodline Recollector` appeared on EDHREC's new-cards list and is
  **not legal in commander** — Scryfall `commander_legality: not_legal`. Disregard it.
- EDHREC `commanders/edgar-markov` (n = 50,082; brackets 1→91, 2→3,540, 3→5,308,
  4→3,954, 5→169) and its Aristocrats theme (n = 1,457).
- Commander Spellbook `find-my-combos`: baseline 2 assembled, 91 one piece short.
- Composition, curve, pips, colour sources and oracle scopes counted from
  `decks/markov_chains/cards.json`.
- EDHREC's per-card page for Patriarch's Bidding **could not be fetched** (the
  script's URL normalisation fails on the apostrophe). Its inclusion rate in Edgar
  decks is therefore unknown to this review and no figure is quoted for it.

`base.txt` was not modified.
