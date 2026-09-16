# Roil Elemental — lander_commander (Aesi, Tyrant of Gyre Strait)

Bracket 3, 4-player casual, $40/card cap.
All oracle text, legality and prices fetched **2026-09-16 22:15–22:19 UTC** via
`card_facts.py lookup`. EDHREC figures from the Aesi commander page (17,091 decks),
the Landfall theme page (1,214 decks) and the Roil Elemental card page.

## Verdict: NO

Roil Elemental is the 13th nonland at MV 6+ in a list the 2026-09-01 audit already
measured as top-heavy, and it is the only one of the deck's 12 landfall payoffs
whose accumulated output a single removal spell on a 3/2 hands straight back to
the table.

## Premise check

I did **not** re-ask for pod calibration, because it was asked and recorded two
weeks ago in `reviews/2026-08-31-weakness-audit.md`:

- Games run **turns 9–12**.
- Threats: **combo/spell kills**, **go-wide creature combat**, **mill**, **aristocrats**.

That premise is *favourable* to this card, and I want to be explicit that none of
the rejection below rests on "too slow." In a turn 9–12 game a six-drop is
castable four or five turns before the game ends. If the rejection depended on
speed I would be re-asking instead of writing it.

One thing did change: **base.txt does not contain the seven swaps from the
2026-09-01 audit.** Herd Heirloom, Goldvein Hydra, Negate, Zendikar's Roil,
Ghalta, Call Damage Control and Jin-Gitaxias are all still in the 99. The
Vorinclex → Beast Within swap *was* applied. Everything below grades against the
list as it actually stands.

## The card, verified

> **Roil Elemental** {3}{U}{U}{U} — Creature — Elemental — 3/2
> Flying
> Landfall — Whenever a land you control enters, you may gain control of target
> creature **for as long as you control this creature.**

- Mana value 6.0. Colour identity **U** — legal in Simic.
- Commander legality: legal. **Not** a Game Changer (contrast: the same script
  prints `Game Changer: yes` for Cyclonic Rift). Game Changers stay 2/3.
- `combos.py --add`: **0 new combos**, 0 newly within reach. Bracket-3 neutral.
- Price **$13.77** (2026-09-16 22:15 UTC), foil $21.59. Under the $40 cap.
- Ruling [2009-10-01]: *"If Roil Elemental leaves the battlefield, you no longer
  control it, so all of its control-change effects end."*
- Ruling [2024-11-08]: landfall triggers on a land entering **by any means**, so
  Ancient Greenwarden doubles it and the fetches/bouncelands feed it.

Trigger scope, on the four axes:

| Axis | Roil Elemental |
|---|---|
| Whose permanents | "a land **you control** enters" — your land drops only |
| Whose turn | unrestricted — fires on any turn a land of yours enters |
| Targeted | **yes** — blanked by hexproof, ward and protection |
| Who chooses | you choose the target; the "may" is yours |

## Step 0 — the honest best case

**"Roil Elemental is the only landfall payoff in Simic that answers an opponent's
board, and in a list whose unconditional creature answers number four — Pongify,
Beast Within, Imprisoned in the Moon, Cyclonic Rift — against a pod that names
go-wide creature combat as one of four threats, a permanent that converts 2–3 land
drops per turn into repeatable Mind Controls both subtracts from the threat and
adds bodies to the Craterhoof / Overwhelming Stampede alpha strike."**

That case is real, and two parts of it survived checking:

- **It is not redundant with anything.** `card_facts.py search 'id<=gu o:landfall
  (o:"each opponent" or o:"target creature an opponent" or o:"gain control")'`
  returns 6 cards, and the only other opponent-facing landfall payoffs worth
  naming are Guardian of Tazeem (EDHREC rank 13691) and Grappling Kraken. Roil
  Elemental is the unique card in its role. This is not a marginal copy.
- **It serves both of the deck's modes.** The grind mode (draw/ramp into big
  creatures) and the go-wide mode (11 landfall payoffs, 7 of them token makers,
  into Craterhoof or Overwhelming Stampede) both want stolen creatures. A stolen
  blocker is subtracted from the wall *and* added to the Hoof count. I checked
  against both modes rather than one.

So this is not rejected as "a good card that isn't good enough." It is rejected on
four specific things.

## What kills it

### 1. It is the only landfall payoff whose output reverses

The 11 landfall payoffs currently in the 99, grouped by what they bank:

| Payoff | What it leaves behind |
|---|---|
| Aesi, Tyrant of Gyre Strait | a card in hand — permanent |
| Tatyova, Benthic Druid | a card + 1 life — permanent |
| Avenger of Zendikar | +1/+1 counters on Plants — permanent |
| Rampaging Baloths | a 4/4 Beast — permanent |
| Zendikar's Roil | a 2/2 Elemental — permanent |
| Greensleeves, Maro-Sorcerer | a 3/3 Badger — permanent |
| Scute Swarm | a 1/1 Insect, or a Scute Swarm copy — permanent |
| Springheart Nantuko | a 1/1 Insect or a creature copy — permanent |
| Tireless Provisioner | a Food or Treasure — permanent |
| Lotus Cobra | mana this turn — spent, but never taken back |
| Mossborn Hydra | doubled counters on itself — permanent |

Every one of them banks value that survives the payoff dying. Roil Elemental is
the sole exception: *"for as long as you control this creature."* Kill the
Elemental and three opponents get their creatures back simultaneously. That makes
removal aimed at it a 2-for-1 **in the opponent's favour** — they answer your
six-drop and undo every steal with one card.

This is not the engine-versus-answer error. I am not saying Pongify does Roil
Elemental's job. I am saying this engine, uniquely among the deck's engines, has
an undo button that any opponent can press.

### 2. It is a 3/2 in a top end built out of 5-and-6-toughness bodies

Creatures at MV 5+ in the 99, with toughness:

```
5  Acidic Slime 2/2          6  Aesi 5/5                7  Cultivator Colossus */*
5  Greensleeves */*          6  Ancient Greenwarden 5/7 7  Jin-Gitaxias 5/5
5  Tatyova 3/3               6  Kodama of the East Tree 6/6   7  Koma 6/6
                             6  Rampaging Baloths 6/6   7  Nezahal 7/7
                             7  Avenger of Zendikar 5/5 8  Craterhoof 5/5
                                                        8  Terastodon 9/9
                                                       12  Ghalta 12/12
```

At MV 6+, the *lowest* toughness in the deck is 5. Roil Elemental would be a 3.
Acidic Slime is the only comparably fragile expensive creature, and it has already
banked its value on ETB before anything can respond. Roil Elemental banks nothing
on ETB — it needs to survive a full turn rotation to do anything at all, while
wearing a target it painted on itself.

In a 4-player pod, stealing a creature per land drop means three opponents each
have both the means and the maximum possible incentive to kill it.

### 3. It fills none of the zero-count categories, and deepens the over-served one

From the 2026-09-01 audit, re-verified against the current `cards.json`:

| Category | Count | Roil Elemental |
|---|---|---|
| Mass answers / sweepers | **0** | no change |
| Graveyard interaction | **0** | no change |
| Instant-speed artifact/enchantment removal | **0** | no change |
| Exile-based creature removal | **0** | no change (control-change, fully reversible) |
| Landfall payoffs | **11** | → 12 |
| Nonlands at MV 6+ | **12** | → **13** |

The audit's aggregate target for the seven swaps was MV6+ **12 → 10**, on the
explicit grounds that turn 9–12 games reward a deck that can deploy more than one
thing per turn. This moves that number the wrong way.

Against the pod's four named threats, Roil Elemental does nothing at all to
**combo/spell kills** or **mill** — the first of which the audit ranked as the top
threat.

### 4. Six mana is the deck's most contested slot

At MV 6 the deck is already casting Aesi ({4}{G}{U}, the engine itself, and it
gets recast) and Ancient Greenwarden ({4}{G}{G}, which doubles all 11 landfall
payoffs and blocks fliers on a 5/7). The turn you spend on Roil Elemental is a
turn you did not spend deploying or redeploying the thing the deck is actually
built around.

## What did *not* kill it

Stated so the record is honest, and so a later review does not re-litigate these:

- **The triple blue is fine.** I expected this to be the killer and it is not.
  21 of the 44 lands produce blue. Hypergeometric on lands in play:
  P(≥3 blue sources) = **62.2%** at 6 lands, **84.9%** at 8, **91.2%** at 9,
  **95.1%** at 10. A deck with 44 lands, Aesi, Azusa, Exploration, Burgeoning,
  Dryad of the Ilysian Grove and Oracle of Mul Daya is at 8–10 lands when it casts
  a six-drop. It would be the deck's third triple-pip card (Craterhoof {G}{G}{G},
  Cultivator Colossus {G}{G}{G}) and its only triple-blue one; current maximum
  blue demand is {U}{U} across Counterspell, Jin-Gitaxias, Koma and Nezahal. Real
  but mild — not load-bearing in this verdict.
- **Worst-case draw is not terrible.** Opening hand on the draw against a fast
  deck it is a brick, like Craterhoof and Terastodon already are. Drawn on turn
  twelve into an empty board it is genuinely live — it steals the best thing on
  the table. A card that is good at the late end is exactly what a turn 9–12 pod
  wants.
- **Redundancy: none.** See step 0. There is no second Roil Elemental effect in
  these colours.
- **Bracket: clean.** Not a Game Changer, 0 new combos, no mass land denial.
- **Anti-synergy: minor only.** Pongify and Beast Within *destroy*, so you would
  not want to point them at a creature you have stolen. That is a sequencing note,
  not a nonbo.

## Price

**$13.77** (2026-09-16 22:15 UTC). Well inside the $40 cap, so the budget veto
never fires. **The verdict is unchanged if the card were free** — nothing above
is an argument about money. Owning it already does not reopen this.

## EDHREC — the disagreement check

- Roil Elemental is in **29.1% of Aesi decks (4,978 / 17,091)**, its top-2
  commander by raw count. Overall EDHREC rank 3,952.
- It appears in **neither** the Landfall theme's top-10 (cutoff 48.5%, Meloku) nor
  its high-synergy-10 (cutoff 56.3%, Retreat to Coralhelm) across 1,214 decks.

So I am with the ~71% of Aesi pilots who leave it out, and with a theme page that
does not surface it at all. This is not a case where I am overruling the
community. The 29.1% figure is honest and it is not nothing — it reflects exactly
the ceiling the steel-man describes.

Note the standing correction from `2026-08-31-vorinclex-bracket-3.md`: Aesi's
commander page is diluted by the "Reap the Tides" precon (verified via EDHREC's
`precon` field). That dilution pushes *staple* percentages down, so a 29.1% on the
commander page is, if anything, slightly generous to this card — and the
non-diluted Landfall page omits it entirely.

## Cut discipline — why there is no slot

Seven cards the 2026-09-01 audit named as cuttable are still in the 99: Herd
Heirloom, Goldvein Hydra, Negate, Zendikar's Roil, Ghalta, Call Damage Control,
Jin-Gitaxias. So unlike that review, I cannot claim "there is no cut." There are
seven.

The problem is that Roil Elemental loses the head-to-head for every one of them:

| Open slot | Audit's pick | Why it still beats Roil Elemental |
|---|---|---|
| Jin-Gitaxias (MV7 {5}{U}{U}) | Splendid Reclamation {3}{G} | Fills the MV4 hole and turns the pod's mill into landfall triggers. Roil Elemental replaces a top-heavy card with another top-heavy card. |
| Ghalta (MV12) | Aetherize {3}{U} | The only mass answer in the list; category currently at **0**. |
| Goldvein Hydra | Reality Shift {1}{U} — **$0.29** (22:19 UTC) | The only *exile* removal; against the pod's aristocrats deck, Pongify and Beast Within feed the drain. Category currently at **0**. |
| Herd Heirloom | Krosan Grip {2}{G} | First instant-speed artifact/enchantment answer, split second against the pod's combo deck. Category at **0**. |
| Call Damage Control (rank 13,129, re-verified today) | Eternal Witness {1}{G}{G} | Body means Finale of Devastation can fetch it. |
| Negate | An Offer You Can't Refuse {U} | Same scope, one mana cheaper. |
| Zendikar's Roil | Scavenging Ooze {1}{G} | Only graveyard interaction. Category at **0**. |

Every one of those is a cheaper card filling a category measured at zero. Roil
Elemental is a more expensive card deepening a category measured at eleven. That
is the whole comparison.

And if you *do* apply the seven swaps, the audit's finding still holds: the best
remaining cut is Greensleeves, Maro-Sorcerer or Ghost Quarter, and I would defend
both. **The cut has to actually be worse than the add, and here it is not.**

## What would have to be different

Not an ADD IF — I am not inventing a condition to soften the no. But so you know
which part of the argument is the load-bearing one:

The entire rejection rests on reason 1 and reason 2 together — a fragile body
carrying reversible output. The deck currently has **two** protection effects
(Heroic Intervention, Swiftfoot Boots). Swiftfoot Boots on Roil Elemental is a
genuinely strong line: hexproof turns a 2-for-1 liability into a real engine. If
this list were rebuilt with a protection package of four or five pieces —
Lightning Greaves, Tyvar's Stand, Snakeskin Veil, Blossoming Defense alongside
what is there — the card changes class and I would re-run this. Two pieces in 99
is not a plan you can build a six-drop 3/2 on.

That is the specific thing that would move me. More enthusiasm for the ceiling
will not, because I already granted the ceiling in step 0.

## Counter-proposal

The role you have identified is real: this deck answers opponents' creatures with
four cards and the pod plays go-wide creature combat. But the right fix is not a
six-mana engine that can be undone — it is the interaction package already sitting
unapplied in the last review. **Reality Shift ({1}{U}, MV 2, $0.29 as of 2026-09-16
22:19 UTC, EDHREC rank 283)** is the single highest-value one: it is the deck's
only exile-based answer, and against the aristocrats deck in your pod it is the
only creature removal you own that does not feed the drain.

I looked for a better opponent-facing landfall payoff and there isn't one.
Guardian of Tazeem ({3}{U}{U}, 4/5, taps a creature per landfall, $0.36) is the
only near-miss and sits at EDHREC rank 13,691 — I am not recommending it.

## Figures for the next review to compare against

| Item | Value | Fetched |
|---|---|---|
| Roil Elemental price | $13.77 / foil $21.59 | 2026-09-16 22:15 UTC |
| Roil Elemental EDHREC rank | 3,952 | 2026-09-16 |
| Roil Elemental in Aesi decks | 29.1% (4,978 / 17,091) | 2026-09-16 |
| Landfall theme denominator | 1,214 decks | 2026-09-16 |
| Roil Elemental on Landfall theme | absent from top-10 and high-synergy-10 | 2026-09-16 |
| `combos.py --add` | 0 new, 0 near | 2026-09-16 |
| Deck: landfall payoffs | 11 | `cards.json` |
| Deck: nonlands MV 6+ | 12 | `cards.json` |
| Deck: blue-producing lands / total lands | 21 / 44 | `cards.json` |
| Deck: coloured pips | G 59 / U 21 | `cards.json` |
| Reality Shift price | $0.29 | 2026-09-16 22:19 UTC |
| Guardian of Tazeem price / rank | $0.36 / 13,691 | 2026-09-16 22:19 UTC |

`base.txt` not modified.
