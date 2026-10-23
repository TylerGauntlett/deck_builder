# markov_chains — full upgrade review (2026-10-23)

Requested as "full throttle", with no candidates named. This is a whole-deck pass:
every card the EDHREC Edgar page and its Vampires / Aristocrats / Tokens themes say
the deck is missing, plus the unapplied proposals from the 2026-10-02 shape review and
the 2026-10-09 Recollector review. Each was checked against the current 99 and against
every earlier verdict in `reviews/`.

**Deck state.** I tried a Moxfield sync and got 403 from Cloudflare. So this reviews
`base.txt` as of 2026-10-09: 100 cards, 34 lands plus the Malakir Rebirth MDFC, and
65 non-land cards besides Edgar. Average non-land MV 2.94. Curve
1:12 · 2:13 · 3:20 · 4:12 · 5:6 · 6:2 (Edgar excluded). Pips B 64 / W 18 / R 5. Land
colour sources: B 25, W 17, R 13. There are 35 Vampires besides Edgar. Game Changers
are 2/3 (Necropotence, Teferi's Protection), and Commander Spellbook shows 2 combos
assembled, both late-game Conqueror loops. **None of the 2026-10-09 swap has been
applied:** Florian is still in and Bloodline Recollector is not. If Moxfield has moved
on since then, this review can't see it.

## Verdicts

| # | Card | Verdict | Cut | Price (2026-10-23 10:53–10:58 UTC) |
|---|---|---|---|---|
| 1 | **Ruthless Lawbringer** | **ADD** | Vampire of the Dire Moon | $0.25 |
| 2 | **Bartolomé del Presidio** | **ADD** | Bloodthrone Vampire | $0.29 |
| 3 | **Bloodline Recollector** | **ADD** (re-affirmed from 10-09) | Florian, Voldaren Scion | $3.76 |
| — | Emeritus of Woe | NO: it makes both infinites tutorable (house-rule spirit) | — | $12.19 |
| — | Twilight Prophet | NO: draw is 13 deep, and the one cuttable draw slot goes to Recollector | — | $3.52 |
| — | Sorin, Vengeful Bloodlord | NO: Vito and Vault already give the team lifelink | — | $2.77 |
| — | Cathars' Crusade | NO: combat-only, in the deepest tier, and no cut exists | — | $9.01 |
| — | Bloodline Bidding | NO for now: the recovery question is still open (see Questions) | — | $2.66 |
| — | Champion of Dusk, Markov Baron, Vanquisher's Banner, Kindred Dominance, Butcher of Malakir, Drana Liberator, Unclaimed Territory | NO, consistent with earlier reviews | — | see Sources |
| — | Everything else on the EDHREC gap list | NO, one line each below | — | see Sources |

Aggregate if all three ADDs are taken: curve 1:12→11 · 2:13→14 · 3:20→20 (avg
2.94→2.95). B pips unchanged at 64, W 18→20, R 5→4. Vampire count unchanged (three
Vampires out, three in). Creatures unchanged at 37. Answers to a noncreature permanent
go from **1 to 2**. Free unlimited sac outlets stay at 3. Card-flow count unchanged
(same-role swap). Game Changers 2/3 unchanged. **0 new combos** across all three
(`combos.py --add`, run separately for each).

---

## The structural finding: interaction has eroded, and noncreature answers are down to one

Counted from verified oracle text in `cards.md`:

| Role | Cards | Count |
|---|---|---|
| Answers **any nonland permanent** | Anguished Unmaking | **1** |
| Answers a creature, targeted | Swords to Plowshares, Oubliette, New Blood | 3 (+ Patron of the Vein ETB, Sorin IB +1, Captivating Vampire activation) |
| Edict | Soul Shatter (instant, "greatest mana value"), Henrika mode 1 (once) | 2 |
| One-sided sweeper | Olivia's Wrath | 1 |
| Engines | Grave Pact, Anowon | 2 |

The 2026-08-31 structural audit counted **9** interaction pieces, using the list
StP · Bolt · Anguished Unmaking · Feed the Swarm · Crackling Doom · Soul Shatter ·
Unexplained Absence · Oubliette · Olivia's Wrath. On that same definition the deck now
has **6**: StP · Anguished Unmaking · Soul Shatter · Oubliette · New Blood ·
Olivia's Wrath. Each removal was a defensible swap on its own. Together they have cost a
third of the suite.

The sharper problem is artifacts and enchantments. **Anguished Unmaking is the only
card in the 99 that can remove one.** The 2026-09-06 review warned that swapping Feed
the Swarm for New Blood would leave it as the only one, and you made that trade
knowingly. I'm not re-arguing that trade. But the premise around it has changed: on
2026-09-07, `meta.json` moved to *"3 opponents rotate between 10+ different decks …
judged on general usefulness across unknown decks."* In a deck that cannot know what it
faces, one answer to an opposing Grave Pact, Ghostly Prison, Smothering Tithe or
equipment package is thin. That makes it the last of a role, and the gap to fill.

## 1. Ruthless Lawbringer — ADD, cut Vampire of the Dire Moon

> **Ruthless Lawbringer** `{1}{W}{B}` — Creature — Vampire Assassin 3/2
> When this creature enters, you may sacrifice another creature. When you do, destroy
> target nonland permanent.

Ruling (2024-04-12): the target is chosen for a second, reflexive trigger, after the
sacrifice. You can't choose the target first, and opponents can respond to the
destroy.

**Honest best case.** It is the deck's second answer to any nonland permanent, and the
only one that adds a body. It pays for itself in this deck specifically. Casting it
triggers Edgar's eminence (*"Whenever you cast another Vampire spell … create a 1/1
black Vampire creature token"*), and that trigger resolves *while Lawbringer is still on
the stack*. So the sacrifice fodder exists before the ETB, and nothing already on the
board has to be spent. That sacrifice is itself a death and a sacrifice event, which
pays the payoffs the deck already runs:

- Any creature dies: Blood Artist, Cordial Vampire, Vein Ripper, Elenda, Blade of the
  Bloodchief.
- A creature you control dies: Cruel Celebrant, Bastion of Remembrance, Edgar Ancient
  Bloodlord, Grave Pact (*"each other player sacrifices a creature"*).
- A player sacrifices a permanent: Carmen (*"Whenever **a player** sacrifices a
  permanent"*).
- A token is sacrificed: Mirkwood Bats.

Three named partners is the synergy floor. This clears it on three different trigger
scopes.

**Effect × frequency × duration against Anguished Unmaking.** Both are one-shot, both
are permanent. Unmaking exiles and works at instant speed, for 3 life. Lawbringer
destroys and works at sorcery speed, costs no life, leaves a 3/2 Vampire and fires the
death package. They complement each other; they are not redundant.

**Two modes.** In the combat mode it is a 3-power Vampire buffed by five lords. In the
aristocrats mode it is a sac event plus a Grave Pact trigger. It serves both.

**Cost of entry.** MV 3 adds to the crowded 3-slot (20 cards). This is the real cost,
and the batch below offsets it: Florian (MV 3) leaves. `{W}{B}` uses the same pips as
Legion Lieutenant and Cruel Celebrant, against 17 white lands plus Command Tower, Arcane
Signet, Exotic Orchard, Path of Ancestry and two W-producing Talismans.

**Worst case.** Opening hand on the draw: a turn-3 3/2 that can kill a turn-2 mana rock
or an early engine. Turn 12, empty board: if Edgar is in the command zone, the eminence
token is still your fodder, so it is a 3/2 plus removal. A topdeck that does something
every time.

**Bracket and combos.** Not a Game Changer. `combos.py --add` finds 0 new and 0 near
combos.

**Disagreement check.** EDHREC has it in **24.2%** of Edgar decks (12,613 / 52,130),
and it is Edgar's largest home by raw count. The community and I agree. My independent
reason is the one-answer count above, which a popularity figure can't see.

**The cut: Vampire of the Dire Moon** (`{B}`, 1/1 deathtouch lifelink, $0.79). The
2026-09-06 review already named it first among "next cut is Vampire of the Dire Moon,
Anowon, Qarsi Revenant or Mirkwood Bats". It is the cheapest member of a category
counted at **six** deterrent sources that day (Vault, Dire Moon, Qarsi, Conqueror,
Henrika's back face, Sorin IB). It loses the least: one of 12 one-drops and one of five
lifelink bodies. No review records a reason to keep it.

Runners-up, and why each is spared:
- **Anowon:** recurring deaths fuel Blade of the Bloodchief (spared 2026-08-30) and
  Recollector.
- **Qarsi Revenant:** spared for deathtouch-plus-lifelink blocks. It is also the better
  card than Dire Moon at the same job.
- **Mirkwood Bats:** fires on every eminence token *created* as well as sacrificed. That
  is one of the deck's few payoffs that scales with the commander directly.
- **New Blood:** the alternative same-role cut (interaction for interaction), but it
  only reshuffles the suite without growing it. Since the finding is that interaction is
  down from 9 to 6, cutting interaction to add interaction would leave the count where
  it is.

**Alternative considered: Vona, Butcher of Magan** `{3}{W}{B}` 4/4 vigilance lifelink
Vampire: *"{T}, Pay 7 life: Destroy target nonland permanent. Activate only during your
turn."* ($0.33). It is a repeatable engine rather than a one-shot answer, so the two
aren't redundant. But it is MV 5 into a 5-slot of six, it is summoning-sick, and 7 life
per activation competes with Necropotence for the same currency. Pick it over
Lawbringer only if your games run long enough that a repeatable answer matters more than
an immediate one. **Mortify** ($0.20) answers creature-or-enchantment at instant speed
but misses artifacts, adds no body and gets no eminence token. It is a clear second.

## 2. Bartolomé del Presidio — ADD, cut Bloodthrone Vampire

> **Bartolomé del Presidio** `{W}{B}` — Legendary Creature — Vampire Knight 2/1
> Sacrifice another creature or artifact: Put a +1/+1 counter on Bartolomé del Presidio.

> **Bloodthrone Vampire** `{1}{B}` — Creature — Vampire 1/1
> Sacrifice a creature: This creature gets +2/+2 until end of turn.

**Honest best case.** This is a same-role, same-MV upgrade to one of the deck's three
free, unlimited sac outlets (Viscera Seer, Carrion Feeder, Bloodthrone). It keeps every
reason Bloodthrone was spared, and its rate is better on every axis but one:

| | Bloodthrone Vampire | Bartolomé |
|---|---|---|
| Cost to sacrifice | free, unlimited | free, unlimited |
| What it can sacrifice | creatures | creatures **or artifacts** (Treasure from Black Market Connections, Blood from Voldaren Estate, spent rocks) |
| Reward | +2/+2 **until end of turn** | +1/+1 counter, **permanent** |
| Pip | `{B}` | `{W}{B}` |

The permanent counters make it a threat that grows over a game rather than a
combat-only trick. Sacrificing a Treasure or Blood token also triggers Carmen
(*"a player sacrifices a permanent"*) and Mirkwood Bats (*"sacrifice a token"*), which
Bloodthrone can never do.

**Sparing reasons honoured.** On 2026-10-09 Bloodthrone was spared as *"one of the
three free, unlimited sac outlets that prepare Recollector."* Bartolomé is also one, so
the reason transfers intact and the outlet count stays at 3. The 2026-10-02 shape review
proposed cutting Bloodthrone outright, and this is the version of that cut that doesn't
cost an outlet.

**The one cost.** `{W}{B}` instead of `{1}{B}`. A turn-2 outlet now needs white. That is
the same pip as Legion Lieutenant and Cruel Celebrant, and the deck already casts both
on curve. It is legendary, but there is no other Bartolomé, so there is no legend-rule
conflict.

**Worst case.** Opening hand: a turn-2 2/1 outlet. Turn 12, empty board: a 2/1, which
is no worse than Bloodthrone's 1/1. Turn 12 with a board: it eats the board into Grave
Pact triggers and keeps the size.

**Combos.** `combos.py --add` finds 0 new. It puts **1** near: Thornbite Staff +
Bloodline Keeper + Bartolomé, missing Thornbite Staff, which the deck doesn't run.
Nothing changes against the house rules.

**Disagreement check.** EDHREC: **23.4%** of Edgar decks (12,207 / 52,130). Bloodthrone
doesn't appear on the Edgar page's lists at all. The community already prefers this
swap.

## 3. Bloodline Recollector — ADD, cut Florian (re-affirmed)

The 2026-10-09 verdict and its Revision 1 stand, and nothing since has moved them:
- The card is unchanged. Price is now $3.76 (it was $5.24 on 10-09).
- EDHREC is **5.9%** (976 / 16,494), up from 4.4%.
- Still 0 new and 0 near combos.

Bartolomé keeps Recollector's three free outlets intact, so the batch doesn't weaken it.
Lawbringer *adds* a death the turn it lands, which strengthens it.

One correction to carry forward: that review's batch note said **"if Twilight Prophet
also comes in, two draw adds is the ceiling."** Prophet doesn't come in (see below), so
the deck stays at one draw add.

## Rejections worth the reasoning

**Emeritus of Woe // Demonic Tutor** (`{3}{B}` Vampire 5/4, $12.19, **24.7%** of Edgar
decks, not a Game Changer). *"This creature enters prepared … At the beginning of your
end step, if two or more creatures died this turn, this creature becomes prepared."*
In this deck that is a Demonic Tutor on arrival and another nearly every turn after,
because two deaths is trivial with three free outlets. Read literally, the constraint
*"No win line that depends on tutoring to assemble"* isn't breached: adding a tutor
doesn't make an existing line *depend* on one. But the constraint's own note says *"the
test is speed and tutor-dependence,"* and the goal line is *"rather than by assembling
a named combo."* Emeritus on turn 5 into a tutored Bloodthirsty Conqueror next to Vito
on turn 6 turns both late-game loops into tutor-assembled ones, early. That is the line
your house rules were written to keep out. **NO.** It is the strongest card on this
list by raw power, and if you decide your rule allows it, I'd reopen it. That decision
is yours, not mine.

**Twilight Prophet** (`{2}{B}{B}`, $3.52, 45.9%). It's a real card: once you have the
city's blessing, a card and a drain every upkeep. But card flow is 13 sources, 11 of
them repeatable (2026-09-07 count, Necropotence included), and the one cuttable
draw-role card, Florian, is already going to Recollector. Past that, every draw card
has a recorded sparing reason: Village Rites, Skullclamp, Welcoming Vampire, BMC,
High-Society Hunter, Baron and Clavileño are each load-bearing. **NO**: an additive card
in the deck's second-deepest category, with no cut. *A rejection that survives the card
being free.*

**Sorin, Vengeful Bloodlord** (`{2}{W}{B}`, $2.77, 9.5%). *"During your turn, creatures
and planeswalkers you control have lifelink."* With Vito out, that turns an alpha strike
into an equal drain on one opponent. Effect × frequency × duration: the deck already
grants team lifelink twice. Vito's `{3}{B}{B}` activation and Vault of the Archangel's
`{2}{W}{B}, {T}` are both repeatable every turn, and Akroma's Will is a third, one-shot.
Sorin makes it passive. That saves mana, but the effect matters only once Vito or
Blight-Priest is out, and both of those already carry it. The −X recursion is one
creature at MV ≤ 4. Not a Vampire, so no eminence. The cut the shape review proposed
for it (Bloodthrone) goes to Bartolomé. **NO.**

**Cathars' Crusade** (`{3}{W}{W}`, $9.01, 20.3%). Multiplicative with eminence: two
bodies per Vampire cast means two rounds of counters. But it serves the combat mode
only, and that lane already has five lords, Cordial Vampire, Indulgent Aristocrat,
Edgar's attack trigger and Shared Animosity. The cut the shape review named, Malakir
Bloodwitch, was spared on 2026-10-09 as a Vito finisher (one lifegain event worth 3×
the Vampire count). Note for the record: `combos.py` puts Cathars' Crusade next to
Viscera Seer and Carrion Feeder in **6 near-combo variants**. Those need further pieces,
but they would be the deck's first counters-and-sacrifice loop. **NO**: no cut, and
single-mode.

**Bloodline Bidding** (`{6}{B}{B}` convoke, $2.66, 7.9% of Edgar decks). *"Return all
creature cards of the chosen type from your graveyard to the battlefield."* It is
one-sided, unlike Patriarch's Bidding. Both reasons Patriarch's was withdrawn on
2026-08-31 (a symmetric return against a tribal pod, and Farewell's exile) were facts
about the old pod, and that premise was retired on 2026-09-07. The audit's condition,
*"ADD IF wipes are actually happening,"* is still unanswered. At MV 8, with convoke
weak right after a wipe, it is the best recovery card I found, and still a slow one.
**NO for now. Reopen if the answer below is "most games."**

**Three Tree City** ($28.15, 29.8%). *"{2}, {T}: … Add an amount of mana of that colour
equal to the number of creatures you control of the chosen type."* Turns 1–2 and right
after a wipe, it is a colourless land in a deck asking for `{B}{B}{B}` (Grave Pact,
Bloodletter, Necropotence, Vein Ripper). Its upside arrives when you already have a
board. **NO**: the cost hits exactly the draws you're already losing.

**Patchwork Banner** ($2.71, 22.1%). This would be a same-role swap for Talisman of
Conviction: painless any-colour mana plus a Vampire anthem. But it is MV 3 against
MV 2, and turn-2 ramp into the twelve 4-drops is worth more than a sixth anthem.
It would also be the 21st 3-drop. **NO.**

**One line each:**
- **Champion of Dusk:** a past cut. Recollector was chosen over it on 10-09.
- **Markov Baron, Coat of Arms, Etchings of the Chosen:** anthems 6–7. Door of
  Destinies (08-31) and Vanquisher's Banner (09-03) were rejected on the same count.
- **Vengeful Bloodwitch, Falkenrath Noble, Exsanguinate, The Meathook Massacre ($26.27):**
  the payoff tier is already 12, and the shape review said reduce it.
- **Mavren Fein, Elenda's Hierophant, Sorin Lord of Innistrad, Legion's Landing:** the
  generators are right-sized.
- **Vampire Socialite, Rakish Heir, Stensia Masquerade, Olivia Voldaren, Vampires'
  Vengeance:** red cards for the combat lane, in a deck trimming red.
- **Crossway Troublemakers, Butcher of Malakir, Kindred Dominance, Kindred Judgment:**
  MV 6–7. Butcher and Dominance were already rejected 09-03/09-04.
- **Preacher of the Schism, Scheming Silvertongue, Vampire Gourmand, Pact of the
  Serpent:** draw is 13 deep.
- **Yahenni, Knight of the Ebon Legion, Oathsworn Vampire:** they grow themselves and
  serve neither engine.
- **Phyrexian Altar ($54.37):** over the $40 cap.
- **Drana, Liberator of Malakir; Unclaimed Territory:** NO, unchanged from 08-31 and
  09-03.

## Questions that would move verdicts

1. **How often do you get wiped, and is it destroy or exile?** "Most games, destroy"
   reopens Bloodline Bidding. It would also raise Vona over Lawbringer, since a
   repeatable answer matters more in grindier games.
2. **How long do games run now?** The last recorded answer is 2026-08-30 ("long"), from
   a pod description that has since been retired. Nothing above is rejected as "too
   slow" or "win-more," so the three ADDs don't depend on it. Cathars' Crusade and Three
   Tree City lean on it slightly.
3. **Is Emeritus of Woe within your tutor rule?** That's your call. If yes, it's the
   first card to reopen.

## Goldfish checks
- Lawbringer: how often is the eminence token your fodder, versus spending a real
  creature?
- Bartolomé: does it survive to grow, or does it eat removal as the first legendary
  threat?
- After the three swaps, track how many games you lose to a noncreature permanent you
  couldn't answer.

## Sources
- `card_facts.py lookup --deck markov_chains`, live Scryfall, 2026-10-23 10:53–10:58
  UTC. Prices: Bloodline Recollector $3.76 · Twilight Prophet $3.52 · Sorin, Vengeful
  Bloodlord $2.77 · Cathars' Crusade $9.01 · Champion of Dusk $0.27 · Markov Baron
  $0.36 · Mavren Fein $0.33 · Vampire Socialite $0.32 · Yahenni $0.30 · Vengeful
  Bloodwitch $0.32 · Knight of the Ebon Legion $1.95 · Crossway Troublemakers $0.39 ·
  Butcher of Malakir $0.36 · Olivia Voldaren $4.29 · Ruthless Lawbringer $0.25 ·
  Bartolomé del Presidio $0.29 · Preacher of the Schism $0.87 · Elenda's Hierophant
  $6.25 · Falkenrath Noble $0.29 · Rakish Heir $0.34 · Oathsworn Vampire $0.23 ·
  Scheming Silvertongue $1.31 · Emeritus of Woe $12.19 · Vampire Gourmand $0.29 ·
  Vanquisher's Banner $4.54 · Phyrexian Altar $54.37 · Stensia Masquerade $0.31 ·
  Legion's Landing $3.26 · The Meathook Massacre $26.27 · Sorin, Lord of Innistrad
  $0.60 · Kindred Dominance $4.60 · Exsanguinate $0.48 · Pact of the Serpent $1.16 ·
  Three Tree City $28.15 · Patchwork Banner $2.71 · Kindred Judgment $1.50 · Bloodline
  Bidding $2.66 · Coat of Arms $17.84 · Etchings of the Chosen $0.37 · Vampires'
  Vengeance $0.36 · Infernal Grasp $0.37 · Go for the Throat $0.65 · Mortify $0.20 ·
  Path to Exile $1.11 · Drana, Liberator of Malakir $1.12 · Unclaimed Territory $0.34 ·
  Vona, Butcher of Magan $0.33. Cuts: Florian $0.45 · Vampire of the Dire Moon $0.79 ·
  Bloodthrone Vampire $0.15.
- `edhrec.py commander markov_chains --diff --all` (n = 52,130), plus the Vampires,
  Aristocrats and Tokens theme diffs. The deck runs 10/10 top cards on the commander
  page and in all three themes. `edhrec.py card`: Ruthless Lawbringer 24.2%
  (12,613/52,130) · Bartolomé 23.4% (12,207/52,130) · Emeritus of Woe 24.7%
  (4,489/18,167) · Bloodline Recollector 5.9% (976/16,494) · Bloodline Bidding 7.9%
  (1,973/24,943).
- `combos.py --add … --near`: baseline 2 assembled. Lawbringer 0/0 · Bartolomé 0/1
  (Thornbite Staff) · Recollector 0/0 · Sorin VB 0/1 (Volcano Hellion) · Bloodline
  Bidding 0/0 · Emeritus 0/0 · Twilight Prophet 0/0 · Cathars' Crusade 0/6 ·
  Exsanguinate 0/1 · Meathook 0/0.
- Deck counts from `decks/markov_chains/cards.json` (built 2026-10-09; `base.txt`
  unchanged since).

`base.txt` was not modified.

---

# Sync, 2026-10-23: list supplied by the user

`base.txt` was replaced with the list you pasted. 100 cards, 34 lands, all legal, no
colour-identity flags. `cards.md` / `cards.json` rebuilt.

| | Card |
|---|---|
| **in** | Bloodline Recollector (this review's ADD #3 / 2026-10-09) |
| **in** | Authority of the Consuls |
| **in** | Swamp (7 → 8) |
| **out** | Florian, Voldaren Scion (the cut named for Recollector) |
| **out** | Malakir Bloodwitch (moved to the Moxfield sideboard; not tracked in `base.txt`, whose parser ignores section headers and would count it as a 101st card) |
| **out** | Sundown Pass |

After the sync: average non-land MV 2.86. Pips B 63 / W 19 / R 4. Creatures 37,
enchantments 9. Game Changers 2/3 unchanged. **Not applied:** Ruthless Lawbringer and
Bartolomé del Presidio. Vampire of the Dire Moon and Bloodthrone Vampire are still in,
so ADDs #1 and #2 stand as written.

**Flagged from verified text, not re-reviewed:**
- **Authority of the Consuls vs Charismatic Conqueror.** Authority: *"Creatures your
  opponents control enter tapped."* Conqueror triggers on *"an artifact or creature an
  opponent controls **enters untapped**."* With both out, Conqueror stops seeing
  opposing creatures and only works on artifacts.
- **Malakir Bloodwitch.** This review spared it on 2026-10-09 as the Vito finisher. Its
  cut was your call, and the 5-slot drops from 6 to 5.
