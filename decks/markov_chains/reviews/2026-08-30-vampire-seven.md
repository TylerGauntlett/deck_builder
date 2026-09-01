# markov_chains — card review, 2026-08-30

Candidates: Anowon, the Ruin Sage · Bloodletter of Aclazotz · Carmen, Cruel
Skymarcher · Elenda, the Dusk Rose · Malakir Bloodwitch · Qarsi Revenant ·
Grave Pact

Deck context: Edgar Markov, bracket 3, $40/card cap, 4-player casual pods. Stated
goal is "win with a string of individually useful cards rather than by assembling
a named combo," vampire aggro into aristocrats.

All oracle text, legality, colour identity and prices fetched from Scryfall
2026-08-31 01:33–01:37 UTC. EDHREC figures from `commanders/edgar-markov`,
n = 50,082 registered decks (bracket spread 2 → 3,540 · 3 → 5,308 · 4 → 3,954).
Combo checks against Commander Spellbook `find-my-combos`.

**Verdict: one ADD (Bloodletter of Aclazotz), six NO.**

---

## Deck facts established this session

These drive everything below. All counted from `cards.json`, not from memory.

- **37 creatures, of which exactly 3 are non-Vampire**: Carrion Feeder (Zombie),
  Mirkwood Bats (Bat), Zulaport Cutthroat (Human Rogue Ally).
- **Every token the deck makes is a Vampire** except Bastion of Remembrance's
  1/1 Human Soldier. Token makers: Edgar Markov (eminence), Edgar, Charmed Groom,
  Bloodline Keeper, Baron Bertram Graywater, Clavileño.
- **11 opponent-life-loss sources**: Bastion of Remembrance, Blood Artist,
  Cliffhaven Vampire, Cruel Celebrant, Marauding Blight-Priest, Mirkwood Bats,
  Sanctum Seeker, Vein Ripper, Vicious Conquistador, Vito, Zulaport Cutthroat.
- **10 sacrifice outlets**, 3 of them free and repeatable (Carrion Feeder,
  Bloodthrone Vampire, Viscera Seer); then Indulgent Aristocrat, Baron Bertram,
  Master of Dark Rites, Falkenrath Pit Fighter, High-Society Hunter, Village
  Rites, Deadly Dispute.
- **Curve (63 nonland cards)**: 1→14, 2→16, 3→15, 4→10, 5→4, 6→3, 9→1.
  Average MV 2.83. Only **7 non-commander cards at MV 5+**.
- **Pips**: B 56 · W 13 · R 8. Mana base ~25 black-producing lands plus 6 nonland
  black sources.
- **Game Changers: zero.** Checked all seven candidates against Scryfall
  `is:gamechanger` — none is one. The bracket-3 cap of 3 is not a constraint here.
- **Combos**: baseline 3 assembled (all Bloodthirsty Conqueror lifegain loops).
  **All seven candidates complete zero new combos.** The no-early-infinites veto
  is not engaged by any of them.

---

## Bloodletter of Aclazotz — **ADD**

`{1}{B}{B}{B}` · MV 4 · Creature — Vampire Demon · 2/4 · colour identity B
$35.58 (fetched 2026-08-31 01:37 UTC) · EDHREC 41.8% of Edgar decks (20,925/50,082)
· overall rank 853

> Flying. If an opponent would lose life during your turn, they lose twice that
> much life instead. (Damage causes loss of life.)

**The claim, stated so it could be false:** this is the only card in the 100 that
multiplies an effect the deck already produces eleven different ways, and because
damage is life loss it *also* doubles every point of combat damage from a
37-creature go-wide board on the turn that matters.

**Density.** 11 named drain sources above, plus all combat damage. This is not a
payoff hunting for enablers — the deck is already the enabler, comprehensively.

**Redundancy.** Nothing in the deck doubles anything. The other "convert board to
damage" cards (Impact Tremors, Sanctum Seeker, Vicious Conquistador) are additive
and small; this is multiplicative and applies to all of them at once. It is the
first copy of its effect, not the twelfth of another.

**Marginal impact — the test that killed the other six.** The gap this deck has,
identified in the 2026-08-30 review too, is converting a wide board into a
*finished* game rather than grinding the last ten life. Bloodletter closes exactly
that, and unlike a bigger creature it scales with the board the deck already
reliably builds. Three named interactions: **Sanctum Seeker** (each Vampire attack
drains 1 → 2 per opponent), **Akroma's Will** (flying + double strike, then every
point doubled — a 4× combat multiplier), **Blood Artist / Cruel Celebrant /
Zulaport Cutthroat** during your own sacrifice turns.

**Cost of entry.** MV 4 lands in the 10-card 4-slot, and it *lowers* the deck's top
end via the cut below. `{B}{B}{B}` off ~25 black lands + 6 nonland black sources
(~31 total) in a deck that is 56/77 black pips — castable on curve.

**Honest caveats, both real:**

- **"During your turn" only.** Blood Artist and Vein Ripper trigger on any creature
  dying, including on opponents' turns, and those triggers are *not* doubled. This
  is a your-turn finisher, not a passive value engine.
- **The ruling limits it.** Official ruling [2023-11-10]: it does not change damage
  dealt, so a lifelinker dealing 1 makes the opponent lose 2 but you still gain only
  1. It does **not** amplify the lifegain half of the deck's Vito / Cliffhaven /
  Marauding Blight-Priest engine — only the life-loss half. Vito's output ("target
  opponent loses that much life") *is* doubled; Vito's input is not.
- **Worst case:** turn-4 topdeck with an empty board, it is a 2/4 flier that does
  nothing. Better than Elenda's 1/1 in the same slot, but not nothing-proof.

**Agreeing with 41.8% independently:** the community likes it in Edgar because Edgar
makes free bodies; I like it here for the specific count of 11 drain sources plus a
37-creature board, which is higher than the average registered list.

**Price is the genuine objection.** $35.58 is under the $40 cap but is by far the
most expensive thing considered, and it is 89% of the cap. If that is more than you
want in one slot, **Malakir Bloodwitch at $4.38 is the honest budget substitute** —
see below. It is worse, and I would still take Bloodletter.

### The cut: Gallifrey Falls // No More

`{4}{R}{R} // {2}{W}` · MV 9 · split, fuse · $0.78 · EDHREC rank 9,953

The weakest card in the deck, and it loses no role:

- **The red half is anti-synergistic.** "Deals 4 damage to each creature" wipes the
  deck's own 1/1 and 2/2 Vampire tokens. In a go-wide token deck a symmetric
  4-damage sweeper is a card you rarely want to resolve.
- **Its sweeper role is already covered, better.** Olivia's Wrath ({4}{B}) gives
  each non-Vampire creature -X/-X where X is your Vampire count — a genuinely
  one-sided wipe, at MV 5 instead of MV 9.
- **Its protection role is already covered, better.** No More phases out your
  creatures for {2}{W}; Akroma's Will ({3}{W}) grants indestructible *and*
  protection from each colour, and doubles as a finisher.
- **Nine mana** to fuse both halves, in a deck averaging 2.83.
- It burns `{R}{R}` — 2 of the deck's 8 total red pips, its thinnest colour.
  Cutting it drops red to 6 pips and moves the deck's demands toward the black it
  actually supports.

Curve effect: MV 9 out, MV 4 in. Strictly an improvement.

**Runners-up, and why each was spared:**

- **Cliffhaven Vampire** ({2}{W}{B}, MV 4) — the closest same-role cut, and a
  redundant copy of Marauding Blight-Priest's trigger at one more mana and a worse
  pip. Spared because the two *stack* (gain 1 life → each opponent loses 2), and
  cutting it removes one of the three Bloodthirsty Conqueror loops. If you would
  rather keep Gallifrey Falls as instant-speed insurance, this is the cut to make
  instead — the deck keeps two of three loop lines and loses little.
- **Impact Tremors** — earmarked as the cut in the 2026-08-30 review for Shared
  Animosity. Spared here because Bloodletter *doubles* it (1 damage becomes 2 per
  token), so they are synergistic rather than competing.
- **Vicious Conquistador** — a 1-drop that keeps the curve's bottom fat; the deck
  wants turn-one plays.

---

## Anowon, the Ruin Sage — **NO**

`{3}{B}{B}` · MV 5 · Legendary Creature — Vampire Shaman · 4/3 · $2.66 (01:33 UTC)
· EDHREC 26.5% of Edgar decks (13,247/50,082)

> At the beginning of your upkeep, each player sacrifices a non-Vampire creature
> of their choice.

**The best case, and it is a real one:** with only 3 non-Vampire creatures in 37
and every token but one a Vampire, this is a near one-sided repeating edict. Most
turns you sacrifice nothing and each opponent loses a creature. That is a genuinely
strong steel-man and the reason the card exists.

**What sinks it:**

- **It is an attrition card in an aggro deck.** It adds no damage and does not
  advance the clock. Its plan — grind three opponents down one chaff creature per
  upkeep — takes many turns, and `meta.json` says this deck wins by going wide and
  converting to drain. Slowing the game favours the pod, not you.
- **Opponents choose.** They sacrifice their worst creature. Against the token or
  go-wide deck at the table it does approximately nothing; it is best against decks
  with few, large creatures, which is where the deck's existing removal already
  points (Feed the Swarm, Swords to Plowshares, Soul Shatter, Anguished Unmaking,
  Patron of the Vein, Oubliette, Unexplained Absence — 7 pieces of interaction).
- **It eats your own best cards.** The three non-Vampires it can hit are Carrion
  Feeder (a free repeatable sac outlet), Zulaport Cutthroat and Mirkwood Bats (two
  of the 11 drain sources). When one is your only non-Vampire on board, Anowon
  takes it.
- **Cost of entry.** MV 5 where the deck has only 7 non-commander cards at 5+ and
  averages 2.83. It does nothing the turn it lands — the trigger waits for your
  next upkeep, so it must survive a full turn cycle as a 4/3.
- **Worst-case draw:** turn 5 against the fast deck, a 4/3 that has not triggered.
  Turn 12 with an empty board, a 4/3 that trades.

**Disagreement check:** 26.5% is low-middling, and I agree with the 73.5%.

## Carmen, Cruel Skymarcher — **NO**

`{3}{W}{B}` · MV 5 · Legendary Creature — Vampire Soldier · 2/2 · $5.60 (01:33 UTC)
· EDHREC 16.6% of Edgar decks (8,294/50,082)

**Best case:** with 10 sac outlets she grows on every sacrifice by any player, and
her attack trigger recurs a permanent from the yard — a role (recursion) the deck is
genuinely thin in, running only Bloodghast, Malakir Rebirth and Edgar, Charmed Groom.

**What sinks it:** she is a **2/2 for five** that must survive, then attack, before
returning anything — and at power 2 she can only return MV ≤ 2. The payoff arrives
two turns after the investment, in a deck whose average card costs 2.83 and whose
plan is to have won by then. She also wants a `{W}` pip where white is 13 pips
against 56 black, and stacks into the MV-5 slot that already holds Champion of Dusk,
High-Society Hunter and Bloodthirsty Conqueror.

**Disagreement check, and it is telling:** 16.6% in Edgar against **76.2% in
Clavileño** (8,058/10,568) and 46.4% in Ardbert. The community is clear that she
belongs in the grindy sacrifice decks, not the aggro one. That matches the analysis
rather than contradicting it.

## Elenda, the Dusk Rose — **NO** (unchanged from 2026-08-30)

`{2}{W}{B}` · MV 4 · $5.28 (refetched 01:33 UTC — identical to last review)
· EDHREC 58.7%, synergy +0.49

Reviewed and rejected in `2026-08-30-anowon-elenda-conqueror.md`. I refetched rather
than trusting the file: **the price, the oracle text and the inclusion figure are all
unchanged**, and the combo check still returns zero new combos. Nothing about the
deck has changed either — same 100 cards.

The verdict therefore does not change. The reasons stand: she is the eleventh death
trigger in the deck's deepest category, does nothing the turn she lands as a 4-mana
1/1, wants a `{W}` pip in the thin colour, and is a grind card in a lean list.

**What would change my mind:** if you rebuilt toward a slower, higher-land, +1/+1
counters shell, or if the pod slowed down enough that turn-4 do-nothings are safe.
Not a marginal call I am shading to no — the same analysis, run again on the same
facts.

## Malakir Bloodwitch — **NO** (but the budget substitute for Bloodletter)

`{3}{B}{B}` · MV 5 · Creature — Vampire Shaman · 4/4 · $4.38 (01:33 UTC)
· EDHREC 52.6% of Edgar decks (26,337/50,082) — a listed "top card"

**Best case, and it is strong:** flying, protection from white (dodges Swords to
Plowshares and most white removal in a typical pod), and an ETB that drains each
opponent for your Vampire count. On a board of five Vampires in a four-player pod
that is 15 life lost across the table and 15 gained — which then triggers Vito,
Cliffhaven Vampire and Marauding Blight-Priest. Three named cards, so the synergy
claim is real.

**What sinks it as an addition:**

- **One-shot, not an engine.** The deck already has 11 incremental drain sources.
  Bloodwitch is a burst version of an effect the deck has in depth, where Bloodletter
  is a multiplier of all of them, every turn.
- **Win-more.** It needs a wide Vampire board to be large, and with a wide Vampire
  board this deck is usually already converting. It does not improve the draws you
  lose with.
- **MV 5** into the crowded, thin top end — the same objection that sinks Anowon
  and Carmen.

**Where it does earn a slot:** if $35.58 for Bloodletter is more than you want to
spend, take Bloodwitch instead of it, for the same Gallifrey Falls cut. At $4.38 it
is roughly half the card for an eighth of the price, and the rubric's price-per-unit
test genuinely favours it. This is an either/or with Bloodletter, not an add
alongside it — I would still pay for Bloodletter.

## Qarsi Revenant — **NO**

`{1}{B}{B}` · MV 3 · Creature — Vampire · 3/3 · $2.44 (01:33 UTC)
· EDHREC 16.6% of Edgar decks (6,645/40,063)

**Best case:** 3/3 flying deathtouch lifelink for three is an efficient, on-theme
Vampire body; the lifelink turns on Vito, Cliffhaven Vampire and Marauding
Blight-Priest; and Renew ({2}{B} from the graveyard) means it is never a dead late
draw.

**What sinks it:** it fills no gap. The deck has 37 creatures and its 3-slot is
already 15 cards deep, occupied by cards that *do* something — Legion Lieutenant,
Marauding Blight-Priest, Oubliette, Stromkirk Captain. Qarsi Revenant is a good
body among lords and engines, and a good body is the most replaceable thing in a
deck with 37 of them. It is not a lord, not a drain source, not an outlet, not
interaction, not card draw.

**Disagreement check:** 16.6%, on a smaller and newer sample (40,063). I would need
to see something 33,000 Edgar decks are missing, and I do not. Nothing here beats a
*named* card the deck already runs.

## Grave Pact — **NO**

`{1}{B}{B}{B}` · MV 4 · Enchantment · $32.27 (01:33 UTC)
· EDHREC **10.7%** of Edgar decks (5,355/50,082) · overall rank 579

**Best case, and it is the strongest of the six rejections:** the deck has 10 sac
outlets, 3 of them free and repeatable, plus a token engine in Edgar's eminence that
makes a Vampire every time you cast one. Grave Pact turns each spare token into a
table-wide edict. That is a real, well-supported engine — the shell is genuinely
there.

**What sinks it:**

- **It is a control card and this is an aggro deck.** It adds no damage, no speed,
  no card. It wins by attrition over many turns, which is the opposite of the stated
  plan. Stripping blockers helps the attack, but Grave Pact demands you feed it your
  own attackers to do so.
- **It is win-more in the shape that matters.** It locks the table when you have a
  board and outlets; when you are behind with no creatures it is a blank enchantment.
- **`{B}{B}{B}` at MV 4** and **$32.27** — nearly the price of Bloodletter for an
  effect that does not close the game.
- **The disagreement check is decisive, and it points the same way as the analysis.**
  Grave Pact is EDHREC rank 579 overall and sits at 54.7% in Sephiroth, 40.3% in
  Teysa Karlov, 37.1% in Marrow-Gnawer, 35.9% in Tergrid — and **10.7% in Edgar**.
  Nearly 45,000 Edgar decks skip a card they clearly know about. The reason is the
  one above: Edgar is the aggro vampire deck, not the grindy sacrifice deck. I am
  agreeing with a strong, specific community signal, not overriding one.

**If you want Grave Pact, the honest ADD IF:** if you rebuild this list toward the
Aristocrats/Sacrifice theme rather than Aggro — more outlets, more recursion, fewer
lords, a higher land count — Grave Pact becomes correct. In the current 100 it is not.

---

## Sources

- Scryfall, fetched 2026-08-31 01:33–01:37 UTC — oracle text, legality, colour
  identity, Game Changer flags, prices, and the Bloodletter ruling of 2023-11-10.
- EDHREC `commanders/edgar-markov`, n = 50,082 — inclusion and synergy; per-card
  pages for each candidate; `lifedrain` theme page (n = 467) — the deck runs 16 of
  the 20 listed top/high-synergy cards, missing only Exquisite Blood, Sanguine Bond,
  Charismatic Conqueror and Elenda.
- Commander Spellbook `find-my-combos` — baseline 3 combos assembled (all
  Bloodthirsty Conqueror lifegain loops); **all seven candidates added zero**.
- Deck composition counted from `decks/markov_chains/cards.json`.

## Still open from the 2026-08-30 review

Shared Animosity ($4.46 at that fetch, not refetched this session) was
counter-proposed as the finisher and has not been added. It aims at the same gap
Bloodletter fills. If you take Bloodletter, re-evaluate whether you still want it —
the gap will be much smaller.

---

## Addendum — "I own them all, add all but Carmen" (same session)

User proposed adding six: Anowon, Bloodletter, Elenda, Malakir Bloodwitch, Qarsi
Revenant, Grave Pact. Modeled the aggregate rather than re-arguing each card.

**Ownership removes price, which was load-bearing for none of the rejections.**
Price went unmentioned for Anowon, Qarsi and Elenda; it was one bullet of four for
Grave Pact; and for Malakir Bloodwitch it was the argument *in favour* ("half the
card for an eighth of the price"). Removing price makes Bloodwitch a weaker
proposal, not a stronger one.

**Modeled 6 adds against the 6 most defensible cuts** (Gallifrey Falls, Cliffhaven
Vampire, Impact Tremors, Vicious Conquistador, Dusk Legion Zealot, Vampire of the
Dire Moon):

- Curve: 1→14/12, 2→16/14, 3→15/16, 4→10/12, 5→4/6, 9→1/0
- Average MV 2.83 → 2.92 (smaller shift than expected)
- MV≤2: 30 → 26 · MV≥4: 18 → 21
- Vampire spells (eminence triggers): 34 → **35** — five of six adds are Vampires;
  only Grave Pact is not. The eminence-dilution objection does **not** hold.
- Pips B/W/R: 56/13/8 → **65**/12/5. Two adds want `{B}{B}{B}`, five want `{B}{B}+`,
  against ~25 black lands.

**The load-bearing objections, in order:**

1. **There are not six cuttable cards.** Past Gallifrey Falls, Impact Tremors and
   Dusk Legion Zealot (16 draw sources, so this one is genuinely spare), every
   remaining cut is a card defensible in any other context — the rubric's own
   signal that the additions are not worth it.
2. **Six cards, two roles.** Anowon and Grave Pact are the same effect here
   (repeating opponent edicts). Elenda, Malakir Bloodwitch and Bloodletter are all
   board-dependent payoffs, in a deck with 11 drain sources already.
3. **Four of six are blank on arrival** (Anowon, Elenda, Grave Pact, Bloodletter),
   concentrated at MV 4–5 — the turns an aggro deck needs to apply pressure. Only
   Bloodwitch has an immediate ETB.
4. **They are a coherent different deck** — grindy attrition aristocrats — not six
   upgrades to this one. Half-installing it yields neither.

**Recommendation unchanged:** Bloodletter (cut Gallifrey Falls). If a second is
wanted, Qarsi Revenant is cheapest to accommodate at MV 3 (cut Impact Tremors or
Dusk Legion Zealot).

**The open question that would flip this**, and it is the user's to answer: if the
pod's games routinely run past turn 10, the aggro premise in `meta.json` is wrong,
and Grave Pact, Anowon and Elenda all improve together. Re-run all six against a
grindy build if so.

---

## Addendum 2 — meta correction: long games, multiple mono-white opponents

User supplied two facts that invalidate a premise this whole review rested on:
**games in the pod routinely run long**, and **several opponents play mono-white**.
`meta.json` says "vampire aggro" and 4-player casual; the aggro half is not what
actually happens at the table. Three verdicts reverse.

The reversal is not new card data — text and prices refetched 2026-08-31 02:47 UTC
and are unchanged. It is that "this is an aggro deck that wants the game over by
turn 9" was doing most of the work in the NO column, and it is false.

### Reversals

- **Malakir Bloodwitch: NO -> ADD.** Protection from white against *multiple*
  mono-white decks is not a rider, it is the card. It cannot be blocked by their
  creatures, targeted by their removal, or damaged by their sources; only a
  non-targeted wrath or an edict answers it. Long games also mean a higher Vampire
  count when the ETB resolves. Verified: "Flying, protection from white."
- **Elenda, the Dusk Rose: NO -> ADD.** I under-read the trigger. It is "whenever
  **another creature** dies" -- *any* creature, not just yours. Mono-white go-wide
  decks feed her every combat, and the deck has 10 sac outlets to cash her in on
  demand. Long games are exactly her format. Ruling [2018-01-19]: token count uses
  her power as it last existed on the battlefield.
- **Grave Pact: NO -> ADD.** The load-bearing objection was "control card in an
  aggro deck," and the premise was wrong. With 10 outlets you control the trigger
  frequency, which is what breaks a white token board -- an opponent-paced edict
  does not. The 10.7% Edgar inclusion still stands as a signal, but it measures the
  average *aggro* Edgar list, which this is not.

### Held

- **Bloodletter of Aclazotz: ADD** (unchanged, still the best of the seven).
- **Anowon, the Ruin Sage: ADD IF** the mono-white decks are few-fat-creature
  builds rather than token swarms. Against tokens each opponent sacrifices a 1/1
  and the card does nothing; it is also opponent-paced where Grave Pact is
  self-paced, and it eats your own Carrion Feeder / Zulaport Cutthroat / Mirkwood
  Bats. A checkable condition, not a hedge.
- **Qarsi Revenant: NO**, but first off the bench. Deathtouch blocks white fatties
  and Renew is real value in long games; it still fills no gap among 37 creatures.

### The 4-add build, modeled

Adds: Bloodletter, Malakir Bloodwitch, Elenda, Grave Pact.
Cuts: Gallifrey Falls // No More, Vicious Conquistador, Impact Tremors, Dusk
Legion Zealot.

- Curve: 1→14/13, 2→16/14, 3→15/15, 4→10/13, 5→4/5, 9→1/0
- Average MV 2.83 → **2.87**
- Pips B/W/R: 56/13/8 → **63/13/5** (white unchanged; red falls because both red
  cuts were the weak draws)
- Vampire spells (eminence): 34 → **35**

**The cut problem from Addendum 1 dissolves**, and for a principled reason: a
grindy meta devalues exactly the cheap aggro drip cards (Vicious Conquistador's
1 damage per attack, Impact Tremors' 1 per token, Dusk Legion Zealot's single
card) that I was previously unable to justify cutting. The four cuts are now easy.

### Correction to the 2026-08-30 review

That review spared Blade of the Bloodchief partly because it "is the only
equipment." **That is wrong -- Skullclamp is also an Artifact — Equipment.** Blade
is therefore not the last of its role and is a legitimate fifth cut if Anowon's
condition is met.

*Note: `2026-08-30-anowon-elenda-conqueror.md` was present at the start of this
session and is no longer on disk; it was not modified by this review.*

### Action item

`meta.json` should be updated -- its "vampire aggro / win fast" framing is what
produced three wrong verdicts, and it will keep producing them for future reviews.

### Resolution (same session)

User confirmed the mono-white opponents are **token swarm / go-wide** builds, and
chose to **leave `meta.json` unchanged**.

- **Anowon, the Ruin Sage: NO, final.** The ADD IF condition was not met. Against
  token swarms each opponent sacrifices a 1/1 and the card does nothing, every
  upkeep, for five mana.
- **Final list: 4 adds** -- Bloodletter of Aclazotz, Malakir Bloodwitch, Elenda
  the Dusk Rose, Grave Pact. **4 cuts** -- Gallifrey Falls // No More, Vicious
  Conquistador, Impact Tremors, Dusk Legion Zealot.
- Blade of the Bloodchief is **not** cut (it was only the fifth cut if Anowon came
  in). It stays.

Why the three adds are specifically good against white token swarms:

- **Grave Pact** is self-paced: with Carrion Feeder, Bloodthrone Vampire and
  Viscera Seer (three free outlets) you chain triggers in one turn and strip a wide
  board, which a once-per-upkeep edict cannot. It also pairs with Olivia's Wrath,
  already in the deck, which is a blowout against non-Vampire token boards.
- **Elenda** grows off *their* dying tokens, not only yours -- a go-wide opponent
  losing creatures in combat is her engine.
- **Malakir Bloodwitch** cannot be blocked by white creatures at all, so a 4/4
  flier with protection from white is unanswerable by a token board.

**Known and deliberate:** `meta.json` still describes this deck as vampire aggro in
casual pods. The table is grindier and white-heavy. A future review should read this
addendum before trusting the aggro framing -- the user has chosen to keep the file
as written.

---

## Addendum 3 — proposed swap: Champion of Dusk -> Anowon; the big-creature gap

User proposed cutting **Champion of Dusk** for **Anowon, the Ruin Sage** (a
curve-, pip- and type-neutral swap: both {3}{B}{B}, MV 5, Vampire), on the grounds
that the pod also contains big-creature decks whose threats this deck cannot kill.

**Verdict: NO to the swap. The underlying gap is real; the counter-proposal is
Crackling Doom.** All text and prices fetched 2026-08-31 03:23-03:24 UTC.

### Why Anowon is the wrong tool for this specific job

Anowon: "each player sacrifices a non-Vampire creature **of their choice**." An
opponent holding any chaff sacrifices the chaff. It reaches the large creature only
when that creature is their sole body.

The deck already runs the better version:

**Soul Shatter** {2}{B} instant -- "Each opponent sacrifices a creature or
planeswalker with the **greatest mana value** among creatures and planeswalkers
they control." No choice, no targeting: it beats hexproof, ward, protection and
indestructible, and it forces the largest permanent. Anowon is a worse Soul Shatter
at two more mana on a fragile body.

**Grave Pact** (added in Addendum 2) already supplies the *repeatable* edict, and
self-paced: three free outlets (Carrion Feeder, Bloodthrone Vampire, Viscera Seer)
fire it several times per turn, where Anowon fires once per upkeep at opponents'
convenience.

### Why Champion of Dusk is the wrong cut

"Draw X, lose X, where X is the number of Vampires you control" -- X is routinely
5-8 here. In the long games this pod actually plays, that is the deck's largest
single refuel, and the lifelink density pays the life cost. Cutting the grind
engine to add a card that does not solve the stated problem loses twice.

### The gap, audited

Creature interaction split by whether an opponent can dodge it:

- **Non-targeted (beats hexproof/ward/protection): 2** -- Soul Shatter, Olivia's
  Wrath (and Olivia's Wrath needs 8 Vampires to kill an 8/8).
- **Targeted: 6** -- Swords to Plowshares, Feed the Swarm, Anguished Unmaking,
  Patron of the Vein, Oubliette, Lightning Bolt.

So "big creatures are unkillable by this deck" is overstated -- six cards answer a
targetable one -- but the narrower claim is correct and is the real gap: only two
answer an *untargetable* one. Grave Pact makes three.

### Counter-proposal: Crackling Doom -- cut Blade of the Bloodchief

`{R}{W}{B}` · instant · MV 3 · **$0.39** · EDHREC rank 2116 · not a Game Changer

> Crackling Doom deals 2 damage to each opponent. Each opponent sacrifices a
> creature with the greatest power among creatures that player controls.

- Non-targeted and forces the largest creature, from **every** opponent at once.
- Exactly Edgar's `BRW` identity -- it consumes the deck's underused red and white
  pips (R falls to 5 and W sits at 13 after the Addendum 2 changes).
- The 2 damage is life loss during your turn, so **Bloodletter doubles it to 4 per
  opponent** -- 12 across a four-player table alongside the edicts.
- Instant speed, $0.39.

**Runner-up, also worth owning: Flare of Malice** `{2}{B}{B}` · $1.99 -- "You may
sacrifice a nontoken black creature rather than pay this spell's mana cost," then
each opponent sacrifices their greatest-mana-value creature. Free at instant speed,
and the sacrifice triggers Blood Artist, Cruel Celebrant, Zulaport Cutthroat,
Bastion of Remembrance and Vein Ripper.

**Cut: Blade of the Bloodchief** -- the spare identified once Skullclamp was
confirmed to also be an Equipment (see the correction in Addendum 2). Converts a
slow win-more equipment into the interaction the deck is short on.

**Anowon, the Ruin Sage: NO, third time, final.** Dead against the pod's token
decks, redundant with Grave Pact against the creature decks, and beaten at its one
job by a Soul Shatter already in the list.

---

## Addendum 4 — proposed swap: Vicious Conquistador -> Qarsi Revenant

User proposed the swap on the grounds that Qarsi's deathtouch is "a deterrent to
attacking."

**Verdict: NO. The stated reason does not survive an audit of the deck.**

**Bookkeeping first:** Vicious Conquistador is *already* a cut in the Addendum 2
build. Qarsi would therefore be a sixth add requiring a sixth cut, not a swap.

**Deathtouch deterrence is the deck's most redundant defensive feature** -- four
existing sources, verified from `cards.json`:

- **Vault of the Archangel** (a *land*) -- `{2}{W}{B}, {T}`: creatures you control
  gain deathtouch and lifelink until end of turn. Whole board, repeatable, costs no
  spell slot.
- **Vampire of the Dire Moon** `{B}` -- deathtouch + lifelink for one mana.
- **Bloodthirsty Conqueror** -- flying, deathtouch.
- **Sorin, Imperious Bloodlord** -- +1 grants deathtouch and lifelink.

Deterrence also does not scale with body size: a 1/1 deathtouch blocker discourages
an attack exactly as well as a 3/3, because any damage from it is lethal. Vampire of
the Dire Moon buys the same deterrent at one mana instead of three.

**The half that is right:** Vicious Conquistador is genuinely weak in a grindy pod
-- a 1/1 that must attack to do anything, into boards it cannot profitably attack.
That is why it was already cut. But a freed slot goes to the best available card,
and that is Crackling Doom (Addendum 3), not Qarsi.

**If the user wants Qarsi anyway**, the sixth cut is **Cliffhaven Vampire** --
identical trigger to Marauding Blight-Priest at one more mana and a worse pip;
two of three Bloodthirsty Conqueror loop lines survive.

---

## Final state of this review

**In (5):** Bloodletter of Aclazotz · Malakir Bloodwitch · Elenda, the Dusk Rose ·
Grave Pact · Crackling Doom

**Out (5):** Gallifrey Falls // No More · Vicious Conquistador · Impact Tremors ·
Dusk Legion Zealot · Blade of the Bloodchief

**Rejected:** Anowon, the Ruin Sage (three times) · Qarsi Revenant · Carmen, Cruel
Skymarcher (withdrawn by user) · Charismatic Conqueror (prior review)

**Note on the reversals.** Three verdicts reversed across this session (Malakir
Bloodwitch, Elenda, Grave Pact), all from a *single* premise correction: the pod
plays long games against mono-white token swarms and big-creature decks, not the
fast pod `meta.json` describes. Anowon and Qarsi did not move, because their cases
rest on effects the deck already owns better versions of -- Soul Shatter and Grave
Pact for the edict, Vault of the Archangel and Vampire of the Dire Moon for the
deathtouch -- and that remains true in a grindy meta.

`base.txt` was not modified at any point. All swaps are the user's to make.

---

## Addendum 5 — Anowon reversed to ADD. The engine framing was correct.

User's argument: Anowon triggers **every upkeep**, where Soul Shatter / Crackling
Doom / Flare of Malice are one-shot. It is not a removal spell -- it is a recurring
death engine feeding the deck's aristocrats payoffs, and an opponent must answer it
or the drain continues.

**This is correct and the prior three rejections were wrong on the axis that
matters.** Verified from `cards.json`.

### The error

Every prior rejection leaned on "against token decks each opponent sacrifices a 1/1
and you get nothing." That is false. Under the engine framing it is irrelevant
*what* dies -- the death is the payoff. I had been checking death triggers against
"creature **you control** dies" (Cruel Celebrant, Zulaport Cutthroat, Bastion of
Remembrance -- which indeed do not fire) without ever separating out the triggers
that fire on **any** creature dying.

**Payoffs that fire on an opponent's creature dying (6):**

| Card | Per death |
|---|---|
| Blood Artist | 1 drain |
| Vein Ripper | 2 drain |
| Cordial Vampire | +1/+1 on every Vampire you control |
| Patron of the Vein | +1/+1 on every Vampire, and exiles it |
| High-Society Hunter | draw a card (nontoken only) |
| Blade of the Bloodchief | +2/+2 on an equipped Vampire |

(Elenda, added in Addendum 2, makes a seventh.)

### The decisive interaction

Anowon triggers at the beginning of **your** upkeep -- during your turn -- and
**Bloodletter of Aclazotz doubles life loss during your turn.** In a 4-player pod,
3 opponent creatures die per cycle:

| Per turn cycle | Alone | With Bloodletter |
|---|---|---|
| Blood Artist (3 x 1) | 3 | **6** |
| Vein Ripper (3 x 2) | 6 | **12** |
| **Total drain** | **9** | **18** |

Plus +3/+3 on every Vampire you control per cycle from Cordial Vampire, again from
Patron of the Vein, and up to 3 cards from High-Society Hunter. Comparing this to
Soul Shatter was a category error: Soul Shatter answers one threat once; Anowon is
a wincon that also strips boards.

**Consequence: Blade of the Bloodchief comes OFF the cut list** (Addendums 3-4 had
it as a cut). Three deaths per upkeep is +6/+6 per cycle on an equipped Vampire.

**Remaining honest risk:** Anowon is a 5-mana 4/3 that dies to almost anything, and
the drain half needs Blood Artist or Vein Ripper already on board. The board-pump
half works regardless.

---

## FINAL LIST (supersedes all earlier ledgers in this file)

**In (6):** Bloodletter of Aclazotz · Anowon, the Ruin Sage · Malakir Bloodwitch ·
Elenda, the Dusk Rose · Grave Pact · Crackling Doom

**Out (6):** Gallifrey Falls // No More · Vicious Conquistador · Impact Tremors ·
Dusk Legion Zealot · Champion of Dusk · Cliffhaven Vampire

The user's original **Champion of Dusk -> Anowon** swap is accepted: same
`{3}{B}{B}`, same MV 5, both Vampires -- curve-, pip- and eminence-neutral. High-
Society Hunter now draws off Anowon's deaths, covering part of Champion's refuel.
Cliffhaven Vampire is the sixth cut (duplicate of Marauding Blight-Priest's trigger
at one more mana and a worse pip; two of three Bloodthirsty Conqueror loops survive).

Curve: 1→13, 2→14, 3→16, 4→12, 5→5, 6→3. Average MV 2.83 → **2.86**.
Pips B/W/R: 56/13/8 → **63/13/6**. Vampire spells: 34 → 34.

**Still rejected:** Qarsi Revenant (deathtouch deterrence already covered four ways,
see Addendum 4) · Carmen, Cruel Skymarcher (withdrawn by user) · Charismatic
Conqueror (prior review).

**Scoreboard of this review's own errors, for the next reader:** three verdicts
reversed on a stale `meta.json` premise (Addendum 2); one factual error about
Equipment count (Addendum 2); one category error treating an engine as removal
(this addendum). The user was right on Anowon and argued it down over three
exchanges. `base.txt` was never modified.

---

## Addendum 6 — the deck is dual-mode; correcting a framing error

User clarified the design: the deck runs **two modes**. With Edgar resolved, his
attack trigger grows the whole board and it becomes aggro with large creatures;
without him, it slow-bleeds as aristocrats.

**This corrects an error I repeated across Addendums 2-5**: I treated "aggro" and
"grindy aristocrats" as mutually exclusive, first rejecting cards for being too
slow for an aggro deck, then reversing when told games run long. Both framings were
half-right. The deck is not one or the other -- it has an explicit mechanical hinge.

### The bridge, verified from `cards.json`

| Card | Converts |
|---|---|
| **Cordial Vampire** | *any* creature dying → +1/+1 on **every** Vampire you control |
| **Patron of the Vein** | an *opponent's* creature dying → +1/+1 on every Vampire, and exiles it |
| **Indulgent Aristocrat** | `{2}`, sacrifice → +1/+1 on every Vampire |

Deaths do not merely drain; they grow the board. Mode B feeds Mode A. Supporting
anthems: Captivating Vampire, Legion Lieutenant, Stromkirk Captain (+1/+1 and first
strike), Vampire Nocturnus, Edgar Charmed Groom. Further counter sources: Edgar
Markov's attack trigger, Carrion Feeder, Blade of the Bloodchief, High-Society
Hunter, Sorin.

### Consequences for the recommendations

- **Anowon is stronger than Addendum 5 argued.** It was justified there purely as a
  bleed engine. Under the dual-mode framing, 3 deaths per upkeep does both jobs
  simultaneously: 18 drain per cycle with Bloodletter, *and* +3/+3 on the entire
  Vampire board per cycle via Cordial Vampire and Patron of the Vein. It
  accelerates whichever mode the game offers.
- **Bloodletter is the same shape from the other side** -- it doubles combat damage
  (Mode A) and doubles drain (Mode B). These two are the best adds precisely
  because they are mode-agnostic.

### One cut reconsidered

**Vicious Conquistador** is a 1-mana Vampire body. In Mode A cheap Vampires are the
plan -- Edgar's attack trigger grows them all and each casting makes an eminence
token. Cutting it thins the turn-one plays.

**Alternative sixth cut: Falkenrath Pit Fighter.** Clunkier -- `{1}{R}`, discard a
card, sacrifice a Vampire, and only if an opponent lost life this turn -- and it
needs red, which falls to 6 pips after these changes and is the thinnest colour.
User's choice; both are defensible.

No other recommended cut is a counter source, a lord, or a bridge card.

### Note for future reviews

`meta.json` describes this deck as "vampire aggro into aristocrats," which the user
has chosen to leave as written. Read it as **dual-mode**, not as a fast aggro deck:
the pod plays long games, and the +1/+1 counter package is the hinge between the
two plans. Grading candidates against a pure-aggro premise produced three wrong
verdicts in this review.

---

## Addendum 7 — keep Impact Tremors, cut Deadly Dispute instead. Accepted.

User proposed keeping Impact Tremors and cutting Deadly Dispute, and asked whether
Impact Tremors scales with Bloodletter's doubling. **It does, and the swap is
correct.** Text refetched 2026-08-31 03:37 UTC.

**Self-contradiction acknowledged.** The original review spared Impact Tremors with
the explicit reasoning "Bloodletter *doubles* it (1 damage becomes 2 per token), so
they are synergistic rather than competing." Addendum 2 then cut it as "small,"
dropping that reasoning when re-sorting the cut list for the grindy meta. The user
caught the inconsistency.

### Impact Tremors scales with Bloodletter

Bloodletter's own reminder text: "(Damage causes loss of life.)" Impact Tremors
deals damage, therefore it is doubled during your turn.

- 1 damage → **2 per opponent = 6 across a 4-player table, per creature entering**
- **Elenda dying at power 6 → 6 tokens → 36 damage from a single trigger**

Nearly all token production happens on your turn and therefore doubles: Edgar's
eminence (triggers on *cast*), Bloodline Keeper (tap), Baron Bertram Graywater
(verified: "This ability triggers only once each turn" -- no loop), Edgar Charmed
Groom (upkeep), Clavileño, Bastion of Remembrance.

### Why Deadly Dispute is the better cut

It is an efficient card sitting in three categories the deck is already deep in:

- Card draw: **16 → 15** sources
- Sacrifice outlets: **10 → 9**
- Ramp: Sol Ring, Arcane Signet, three Talismans, Dark Ritual, Master of Dark Rites
  all remain

Impact Tremors is in a thin category -- it is the only card converting raw token
count into damage. Not the last of any role for Deadly Dispute, so the cut is safe.

**Structurally free:** both are MV 2, so the curve is unchanged. Keeping the `{R}`
leaves red at 7 pips rather than 6, which matters now that Crackling Doom wants
`{R}{W}{B}`.

---

## FINAL LIST (supersedes Addendum 5's ledger)

**In (6):** Bloodletter of Aclazotz · Anowon, the Ruin Sage · Malakir Bloodwitch ·
Elenda, the Dusk Rose · Grave Pact · Crackling Doom

**Out (6):** Gallifrey Falls // No More · Deadly Dispute · Dusk Legion Zealot ·
Champion of Dusk · Cliffhaven Vampire · Vicious Conquistador *(or Falkenrath Pit
Fighter -- user's choice, see Addendum 6)*

**Kept after reconsideration:** Impact Tremors (this addendum), Blade of the
Bloodchief (Addendum 5).

Curve: 1→13, 2→14, 3→16, 4→12, 5→5, 6→3. Average MV 2.83 → **2.86**.
Pips B/W/R: 56/13/8 → **62/13/7**. Vampire spells: 34 → 34.

**Rejected throughout:** Qarsi Revenant · Carmen, Cruel Skymarcher (withdrawn) ·
Charismatic Conqueror (prior review).

---

## APPLIED 2026-08-30 — `base.txt` updated at the user's direction

The user made these swaps in paper and directed the decklist file be updated.
`base.txt.bak` holds the pre-change list.

**Removed (6):** Champion of Dusk · Cliffhaven Vampire · Deadly Dispute ·
Dusk Legion Zealot · Falkenrath Pit Fighter · Gallifrey Falls // No More

**Added (6):** Anowon, the Ruin Sage · Bloodletter of Aclazotz · Crackling Doom ·
Elenda, the Dusk Rose · Grave Pact · Malakir Bloodwitch

User resolved the one open choice from Addendum 6 by cutting **Falkenrath Pit
Fighter** rather than Vicious Conquistador, keeping the 1-mana Vampire body for
the aggro mode. Impact Tremors kept per Addendum 7.

### Verified post-change state (`build_card_details.py` rerun)

- **100 cards, 91 distinct** · 37 creatures · 36 lands
- Curve: 1→13, 2→14, 3→16, 4→12, 5→5, 6→3 (the MV 9 slot is gone)
- Average MV nonland: **2.83** · pips **B 63 / W 13 / R 6**
- Vampire spells (eminence triggers): **34** — unchanged
- Colour-identity violations: **none** · Game Changers: **none** (bracket 3
  permits 3)
- Combos assembled: **3 → 2**. Cutting Cliffhaven Vampire removed one of the three
  redundant Bloodthirsty Conqueror lifegain loops, as predicted; the Vito and
  Marauding Blight-Priest lines remain. Still late-game and non-tutored, so the
  `meta.json` veto on early infinites is not engaged.

**Note on projections:** Addendum 7 projected avg MV 2.86 and pips B 62 / W 13 /
R 7. Actuals are 2.83 and B 63 / W 13 / R 6. Two causes: cutting Falkenrath Pit
Fighter (`{R}`) rather than Vicious Conquistador (`{B}`) moved a pip from red to
black, and the projection model counted the Malakir Rebirth // Malakir Mire MDFC
as a nonland where `build_card_details.py` counts it as a land. The script's
figures are authoritative.
