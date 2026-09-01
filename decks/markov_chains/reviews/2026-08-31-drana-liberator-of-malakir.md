# markov_chains — Drana, Liberator of Malakir, 2026-08-31

Single-candidate evaluation, requested after yesterday's structural audit rejected
Drana in a one-paragraph aside. That aside was not a real evaluation and its stated
reason was weak. This is the proper run. **The verdict is unchanged — NO — but the
reason is different, and the old reason should be discarded.**

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line.

Meta premise carried forward from the 2026-08-30 review (Addendums 2 and 6) and the
2026-08-31 audit: games run **long**, several opponents play **mono-white** (both
token swarms and big-creature builds), and the deck is **dual-mode** — Edgar-resolved
aggro, or aristocrats slow-bleed, bridged by the +1/+1 counter package.

All oracle text, rulings, legality, colour identity and prices fetched from Scryfall
2026-08-31 13:31–13:35 UTC. Composition counted from `decks/markov_chains/cards.json`
(built 2026-08-30 23:56, current with `base.txt` of 2026-08-30 23:55). EDHREC from
`commanders/edgar-markov`, n = 50,082, and `cards/drana-liberator-of-malakir`.

---

## The card

```
Drana, Liberator of Malakir  {1}{B}{B}
  Legendary Creature — Vampire Ally
  Flying, first strike
  Whenever Drana deals combat damage to a player, put a +1/+1 counter on
  each attacking creature you control.
  [2/3]
```

Colour identity B ⊆ Mardu — legal. Commander legality: legal. Not a Game Changer.
`combos.py --add`: **zero** new combos completed; baseline stays at 2. Neither
`meta.json` veto is engaged.

**Price: $0.86** (fetched 2026-08-31 13:31 UTC), against a $40 cap. On its own line,
as its own factor: price is not doing any work in this verdict. **The rejection below
survives the card being free** — it is entirely about the eleventh copy of an effect.

---

## Step 0 — the honest best case

Stated as a claim that could be false:

> *Drana is a three-mana, evasive, repeatable, permanently-escalating team anthem in
> a deck whose only other attack-triggered team pump costs six mana and lives on a
> commander that this deck's own reasoning says usually stays in the command zone —
> and per official ruling her first strike makes the counters land **before** the
> regular combat damage step, so the rest of the attacking team hits harder the same
> turn she connects.*

That is a real case and two parts of it are worth taking seriously.

**The Edgar part is correct and it is the part yesterday got wrong.** Yesterday's
aside said Drana "duplicates Edgar's own attack trigger." Verified text —
Edgar: *"Whenever **Edgar attacks**, put a +1/+1 counter on each Vampire you
control"* — requires Edgar on the battlefield, at six mana, whereas his eminence
works from the command zone. The same audit used exactly that fact to reject Flawless
Maneuver. So "duplicates Edgar" leans on an effect that is offline in most games.
Discard that reason.

**The first-strike timing is real and verified**, ruling of 2015-08-25: *"the +1/+1
counters that are put on attacking creatures without first strike will affect the
damage those creatures deal during the regular combat damage step."*

Both survive. The card still fails, on the tests below.

---

## What killed it — test 1: redundancy, on rate and duration

Grepped every oracle face in `cards.json`. The category Drana is joining — *make my
attacking board bigger* — is **ten cards deep**, grouped by scope:

**Static team-wide anthems (6)**

| Card | Effect |
|---|---|
| Bloodline Keeper // Lord of Lineage | "Other Vampire creatures you control get **+2/+2**" (flip side) |
| Vampire Nocturnus | "...this creature and other Vampire creatures you control get **+2/+1** and have flying" (top card black) |
| Captivating Vampire | "Other Vampire creatures you control get **+1/+1**" |
| Stromkirk Captain | "Other Vampire creatures you control get **+1/+1 and have first strike**" |
| Legion Lieutenant | "Other Vampires you control get **+1/+1**" |
| Edgar, Charmed Groom | "Other Vampires you control get **+1/+1**" |

**Team-wide +1/+1 counter sources (4)**

| Card | Trigger scope | Cost |
|---|---|---|
| Cordial Vampire | "Whenever this creature or **another creature** dies" — *any* creature, *any* player | `{B}{B}` |
| Indulgent Aristocrat | `{2}`, Sacrifice a creature — on demand, instant speed | `{B}` |
| Edgar Markov | "Whenever **Edgar attacks**" — needs Edgar on board | `{3}{R}{W}{B}` |
| Patron of the Vein | "Whenever a creature **an opponent controls** dies" | `{4}{B}{B}` |

(Forerunner of the Legion is an eleventh, half-counted: *single target*, *until end
of turn*.)

The rubric says compare **effect × frequency × duration**, not effect alone. Doing
that against the one card that actually occupies Drana's role — the escalating,
permanent, board-wide pump that breaks a stalled board of 1/1 eminence tokens:

| | **Cordial Vampire** `{B}{B}` | **Drana** `{1}{B}{B}` |
|---|---|---|
| **Effect** | +1/+1 counter on each Vampire you control — includes untapped bodies and blockers; 34 of 37 creatures are Vampires | +1/+1 counter on each **attacking** creature — includes non-Vampires, excludes anything held back |
| **Frequency** | **Any** creature dies, **any** player, in a 4-player pod, with **9 sacrifice outlets** in the deck (Bloodthrone Vampire, Carrion Feeder, Viscera Seer, Indulgent Aristocrat, Baron Bertram Graywater, Master of Dark Rites, High-Society Hunter, Village Rites, Vein Ripper's ward) | Must attack **and connect with a player**. Blocked = no trigger. Once per combat |
| **Duration** | Permanent counters | Permanent counters |

All three terms match or favour Cordial Vampire, at one less mana and with no combat
requirement. That is the rubric's definition of genuine redundancy, and it is not a
close call: in an aristocrats deck with nine sac outlets in a four-player pod, deaths
happen several times per turn cycle. Cordial Vampire out-triggers Drana without ever
needing to get through a blocker.

**The long-game premise, which is Drana's best argument, is Cordial Vampire's best
argument too.** Escalation over many turns is precisely why the deck already runs the
cheaper, more reliable escalator.

## What killed it — test 2: Stromkirk Captain turns off the signature trick

This one is specific and I did not see it yesterday.

The first-strike timing case rests on Drana's counters landing *before* the regular
damage step so the rest of the team hits harder. The same ruling states the other
half: *"The +1/+1 counter won't change how much damage Drana or any other attacking
creature **with first strike or double strike** deals during that combat damage
step."*

**Stromkirk Captain gives every other Vampire you control first strike.** With the
Captain on board — and the Captain is 74.5% of Edgar lists and already here — every
attacking Vampire deals its damage in the *same* step Drana does, so her counters
arrive too late to boost any of it. The counters still stick for later turns, but the
same-combat anthem argument is switched off in exactly the wide-attack board state
where it was supposed to matter most.

Not a nonbo that costs you anything — just the best argument for the card
evaporating against a card already in the 99.

## Test 3: it serves one of the deck's two modes

Failure mode 7 says score against every mode. Drana pumps power. The aristocrats mode
does not care about power — verified: **Sanctum Seeker** ("Whenever a Vampire you
control **attacks**, each opponent loses 1 life"), **Blood Artist** and **Zulaport
Cutthroat** and **Cruel Celebrant** and **Bastion of Remembrance** (per *death*),
**Vito** and **Marauding Blight-Priest** (per *lifegain*), **Mirkwood Bats** (per
token). Every drain source in the deck counts bodies, deaths, attacks or lifegain.
**None counts power.**

The bridge cards convert deaths into board growth. Drana converts *connecting* into
board growth, which is aggro-mode output feeding aggro-mode input. She is the one
member of the counter package that is not a bridge.

## Test 4: marginal impact and cost of entry

- **MV 3 is the deck's fattest rung — 16 nonland cards** already sit there, including
  Captivating Vampire, Stromkirk Captain and Forerunner of the Legion from the very
  category Drana joins.
- The deck's identified hole is **zero graveyard recursion** across 37 creatures with
  one mass-protection instant (audit Finding 1). Drana is a 2/3 that dies to every
  wipe and leaves nothing behind. She does not touch the thing that is actually
  losing games.
- **Worst-case draws.** Turn 12 after a wipe with an empty board: a 2/3 flier with a
  dead trigger. Opening hand against the fast deck: a fine 3-mana blocker (flying,
  first strike) — genuinely her best floor, and not a reason to run her.

## Test 5: the disagreement check — and this is the cleanest evidence

I say no, EDHREC says 54.3%. Normally that demands a named reason this deck is
different. Here it doesn't, because **EDHREC's own numbers rank Drana last in her own
package**, and the deck runs everything above her:

| Card | Inclusion in Edgar decks (n = 50,082) | In deck? |
|---|---|---|
| Captivating Vampire | 82.4% (41,258) | yes |
| Cordial Vampire | 81.8% (40,981) | yes |
| Stromkirk Captain | 74.5% (37,326) | yes |
| Indulgent Aristocrat | 72.8% (36,441) | yes |
| Legion Lieutenant | 69.2% (34,672) | yes |
| Bloodline Keeper | 68.8% (34,452) | yes |
| **Drana, Liberator of Malakir** | **54.3% (27,213)** | **no** |

The community's six higher-conviction picks for this exact role are all already in
the 99, and **22,869 Edgar decks leave Drana out**. Agreeing with the top of that list
and stopping short of the bottom of it is not disagreeing with EDHREC — it is reading
it. Drana is 69.4% of *Clavileño* decks and Clavileño is here, but that is Clavileño's
commander page, not this deck's.

## Anti-synergy and bracket

No legend conflict. She is a Vampire, so casting her triggers eminence and she gains
every lord buff. No bracket pressure: not a Game Changer, zero new combos, no
tutoring. Nothing here is a problem — she is simply the eleventh card doing a job ten
cards do.

---

## Verdict

**NO** — the "pump the attacking board" role is ten cards deep, and Cordial Vampire
does Drana's exact job (permanent, board-wide, escalating counters) for one less mana
and at a much higher trigger rate, with no requirement to connect.

Correcting yesterday's stated reason: *"duplicates Edgar's own attack trigger"* was
weak, because Edgar is usually in the command zone. The real reason is Cordial
Vampire plus Indulgent Aristocrat plus six static lords, and Stromkirk Captain
switching off the first-strike timing that was Drana's one unique angle.

### No cut named, deliberately

She never got to the cut stage. For the record, what she would have had to beat: the
audit's runner-up cuts were **Vicious Conquistador** and **Unexplained Absence**, and
Drana is a stronger card than Vicious Conquistador in isolation. That is not enough —
swapping a 1-drop for a 3-drop in the fattest rung of the curve, to add the eleventh
card in a saturated category, while the deck still has zero graveyard recursion, is
motion rather than improvement.

### No counter-proposal for this role

The role Drana was aimed at is not a gap. The gap is still audit Finding 1, and it is
still waiting on the same question: **how often does a wrath actually resolve in these
games?** If it is most games, Patriarch's Bidding ($3.92, fetched 2026-08-31 04:40
UTC) in for Orzhov Basilica is a far bigger upgrade than anything in the pump
category. Findings 2 (2 Mountain → 2 Swamp) and 3 (cut Orzhov Basilica) are still
free and still unapplied — `base.txt` is unchanged since 2026-08-30 23:55.

### What would change my mind

One thing, and it is narrow: if the mono-white decks in your pod genuinely cannot
block a flier, Drana connects every turn and the escalation compounds unopposed. Even
then I think Cordial Vampire out-produces her in a deck with nine sac outlets — but
that is the axis I would re-run, and "none of the white decks play fliers" is the fact
that would make me run it.

## Sources

- Scryfall via `card_facts.py lookup`, fetched 2026-08-31 13:31–13:35 UTC:
  Drana, Liberator of Malakir $0.86 · Edgar Markov $42.28 · Cordial Vampire $1.92 ·
  Indulgent Aristocrat $0.30 · Patron of the Vein $0.40 · Blade of the Bloodchief
  $7.61 · Elenda, the Dusk Rose $5.75 · Sanctum Seeker $0.35 · Clavileño $0.75 ·
  Vicious Conquistador $0.33 · Orzhov Basilica $0.29 · Anowon, the Ruin Sage $2.66 ·
  Forerunner of the Legion $1.34 · Captivating Vampire $3.32 · Stromkirk Captain $1.65.
- Drana rulings (both dated 2015-08-25) via `card_facts.py lookup --rulings`.
- EDHREC `commanders/edgar-markov` (n = 50,082) and `cards/drana-liberator-of-malakir`
  (overall rank 1520; 54.3% of Edgar decks, 69.4% of Clavileño decks).
- Commander Spellbook via `combos.py --add`: baseline 2 assembled, 0 newly completed.
- Composition, curve, anthem/counter/sac-outlet/death-trigger counts and trigger
  scopes from `decks/markov_chains/cards.json`.

`base.txt` was not modified.
