# Replacing Vorinclex for bracket 3 — lander_commander
(revised after user challenge to the EDHREC signal)

Deck: Aesi, Tyrant of Gyre Strait. meta.json says bracket 4; target is **bracket 3**.
Prices fetched 2026-09-01 01:14–01:26 UTC.

## 1. Cutting Vorinclex is correct

> Vorinclex, Voice of Hunger {6}{G}{G} — 7/6 trample
> Whenever you tap a land for mana, add one mana of any type that land produced.
> **Whenever an opponent taps a land for mana, that land doesn't untap during its controller's next untap step.**

Bracket 3 (fetched from the WotC Commander Brackets announcement): ≤3 Game Changers,
**no mass land denial**, no intentional *early-game* two-card infinites, extra turns
low and unchained. The bolded clause is the violation.

Vorinclex is **not** a Game Changer. The deck runs 2 of 3 allowed (Cyclonic Rift,
Rhystic Study). That was never the issue.

## 2. Cutting it is probably sufficient

`combos.py` reports 10 assembled combos; that number is misleading.
- The **two-card** Springheart Nantuko lines carry a Spellbook template requiring a
  land-animation ("Earthbend") effect. Grepped all 99 oracle texts for
  `becomes a … creature` / `animat` / `Earthbend`: **zero hits**. Not assembled.
- The genuinely assembled lines route through **Kodama of the East Tree (MV 6)** +
  a bounce land + a landfall payoff — three cards behind six mana. Late-game, which
  bracket 3 permits.

## 3. The EDHREC correction (user's point, and it holds)

I initially leaned on Aesi's commander-page inclusion %. The user pointed out Aesi
is a precon face commander, so those numbers are diluted by unmodified lists.

**Verified:** EDHREC's own `container.json_dict.card.precon` field for Aesi returns
**"Reap the Tides"** (Duskmourn: House of Horror Commander). The mechanism is real.
I could not quantify the dilution — the precon JSON's `deck` field returned only 4
entries, malformed — so magnitude is unverified.

Recalibrated against two less-diluted sources:

**Landfall theme page (1,255 decks; brackets {3:135, 2:51, 4:98}):**

| Card | Aesi cmdr page | Landfall theme | Δ |
|---|---|---|---|
| Beast Within | 58.6% (9905/16889) | **62.4%** (783/1255) | +3.8 |
| Explore | 58.8% (9928/16889) | **60.9%** (764/1255) syn +0.41 | +2.1 |
| Retreat to Coralhelm | — | 56.7% (712/1255) syn +0.48 | |
| Meloku the Clouded Mirror | — | 49.2% (618/1255) syn +0.46 | |

**Cross-check, three non-precon lands commanders:**

| Card | Tatyova (9,265) | Kruphix (4,573) | Omnath LoR (8,828) |
|---|---|---|---|
| Beast Within | 44.3% | 46.6% | 52.2% |
| Explore | 48.8% | 17.7% | 37.8% |
| Wayward Swordtooth | 25.3% | — | 19.1% |
| Summer Bloom | 21.6% | — | — |
| Zendikar Resurgent | — | 26.1% | — |
| Nyxbloom Ancient | — | 43.6% | — |

Correcting for the dilution moves Beast Within **up**, not down.

## 4. Reversal on my own earlier pick

I first recommended **Zendikar Resurgent** to preserve Vorinclex's land-mana-doubler
role. Under the corrected signal that looks worse: it appears only in Kruphix
(26.1%) — a dedicated big-mana commander — and is absent from Tatyova's and Omnath's
lists entirely. Same for Nyxbloom Ancient (Kruphix 43.6%, nowhere else).

**Mana doubling is a Kruphix role, not an Aesi role.** Aesi converts *land drops*
into cards; doubled mana does not produce land drops. I was preserving a role the
deck doesn't actually want. Withdrawn.

## 5. Verdict — ADD Beast Within, replacing Vorinclex

> Beast Within {2}{G} — Instant
> Destroy target permanent. Its controller creates a 3/3 green Beast creature token.

- **Fills the deck's largest hole.** Unconditional answers to a resolved permanent
  today: **Pongify** (creatures only), **Cyclonic Rift**, **Acidic Slime**
  (artifact/enchantment/land), **Reclamation Sage** (artifact/enchantment). That is
  **one creature answer in 99 cards**, and no answer at all to a resolved
  planeswalker or a problem land.
- 62.4% of Landfall decks; 44–52% across three non-precon lands commanders.
- MV 3 against a list with **13 nonlands at MV 6+** and only 2 at MV 4 — a real
  curve improvement over the MV 8 it replaces.
- `combos.py --add`: **0 new combos.** Not a Game Changer. Bracket-neutral.
- Anti-synergy: gives an opponent a 3/3. Irrelevant across from Craterhoof, Ghalta,
  Terastodon, Koma.
- Worst-case draw: an instant that answers anything is never dead.
- Price **$0.61** (2026-09-01 01:16 UTC). Verdict unchanged if it cost $60.

## 6. The user's four candidates

Prices fetched 2026-09-01 01:24–01:27 UTC. None of the four is a Game Changer;
`combos.py --add` returns **0 new combos** for all four.

### Icetill Explorer {2}{G}{G}, MV 4, $20.09 — the one that survives

> You may play an additional land on each of your turns.
> You may play lands from your graveyard.
> Landfall — Whenever a land you control enters, mill a card.  [2/4]

This defeats the objection I used to reject Wayward Swordtooth, and I should say so
directly. I argued that a sixth extra-land-drop effect is weak because the binding
constraint is **lands in hand**, not permission. Icetill Explorer *relieves* that
constraint rather than adding to it: the landfall mill puts lands into the yard, and
its own second line plays them from there. It is self-fueling, so the Swordtooth
reasoning does not transfer.

Support verified in the 99:
- Play-lands-from-graveyard becomes the **third** such effect (Ancient Greenwarden,
  Ramunap Excavator) — a real package, not an orphan.
- **Ten** lands already self-sacrifice or fetch into the graveyard: Blighted Woodland,
  Coral Atoll, Evolving Wilds, Fabled Passage, Field of Ruin, Ghost Quarter, Jungle
  Basin, Myriad Landscape, Terramorphic Expanse, Waterlogged Grove.
- It is the deck's **only** self-mill effect.
- **MV 4 fills the deck's biggest curve hole** — currently only Arixmethes and
  Oracle of Mul Daya sit there, against 13 nonlands at MV 6+.

Adoption: 21.4% Aesi (2397/11181), 21.4% Landfall (108/505), 23.3% Tatyova
(1369/5864). Consistent, and the smaller denominators are EDHREC restricting to
decks registered since the card's release — so that is 21% of *eligible* decks.

Costs: milling can bin Craterhoof or Ghalta with only three recursion effects in the
deck and no way to retrieve a nonland card except Ancient Greenwarden's land clause.
A 2/4 body does nothing. $20.09 is the most expensive of the four; budget is uncapped.

**Verdict: ADD — the correct pick if you want the slot to stay in the lands-engine
lane.** Ranked behind Beast Within only because interaction is the larger hole.

### Wayward Swordtooth {2}{G}, MV 3, $3.98 — NO
Sixth extra-land-drop effect behind Aesi, Azusa, Dryad of the Ilysian Grove,
Exploration, Oracle of Mul Daya. Grants one extra drop where Azusa grants two, on a
body that can't attack or block until you control ten permanents, and it supplies no
fuel. 23.8% Aesi / 22.0% Landfall / 25.3% Tatyova.

### Summer Bloom {1}{G}, MV 2, $1.68 — NO
One-shot; EDHREC rank 2897; 21.6% even among Tatyova decks. Dead in hand whenever you
lack two or three spare lands to dump.
→ **Counter-proposal: Explore** ({1}{G}, MV 2, **$0.20**, 60.9% / synergy +0.41 on
the Landfall page). Same effect class, but it draws a card, so it replaces itself and
is never a dead draw.

### Kiora, the Crashing Wave {2}{G}{U}, MV 4, foil $1.27 — NO
**EDHREC rank 7811**, and it appears in none of the Aesi, Landfall, or Tatyova lists.
Starting loyalty 2 means the −1 (draw a card, play an additional land this turn) can
be used twice before it dies — two cards and two land drops for four mana, spread over
two turns. The −5 Kraken emblem requires three turns of +1, which only prevents damage
to and from a single opponent's permanent. Too slow and too small.

## 7. Also considered

**Meloku the Clouded Mirror — REJECTED.** 49.2% / synergy +0.46 on the Landfall page
and only $0.80, but `combos.py --add` confirms it completes a **two-card infinite
with Kodama of the East Tree**. At 11 total mana that is late-game and bracket-3
legal, but it is the wrong direction while deliberately lowering bracket.

**Nissa, Who Shakes the World — REJECTED, actively harmful here.** Its +1 animates a
land, and `combos.py --add` confirms it completes **Springheart Nantuko + Nissa =
infinite landfall triggers** — a genuine two-card infinite at 7 total mana in a deck
that ramps there by turn four. Exactly the bracket-3 restriction being targeted.

**Retreat to Coralhelm** — $0.34, 56.7% on the Landfall page, adds no combos in this
deck (the classic combo needs an untapper like Sakura-Tribe Scout, which is absent).
Reasonable filler, but the tap/scry modes are minor next to Beast Within.

**Nyxbloom Ancient ($28.42) / The Great Henge ($65.80) / Zendikar Resurgent ($2.35)**
— see §4. Doubler role withdrawn.

## 8. Cut discipline

One card leaves (Vorinclex), named by the user. Lands and ramp unchanged.
Role counts: Game Changers 2 → 2; unconditional permanent answers 4 → 5;
nonlands MV 6+ 13 → 12; MV 3 slot 14 → 15.
