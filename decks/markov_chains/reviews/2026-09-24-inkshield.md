# markov_chains — Inkshield, 2026-09-24

Candidate proposed: **Inkshield**. One card, one slot.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods, **rotating opponents (10+ decks)**, judged
on general usefulness. Vetoes: no early infinite combos, no tutor-dependent win
line. `meta.json` (updated 2026-09-07) explicitly says not to carry forward any
fixed description of what the pod plays, so the Farewell / Armageddon / tribal
premise from the 2026-08-31 reviews is **not** used here.

All oracle text, legality, colour identity and prices fetched from Scryfall via
`card_facts.py` on **2026-09-24 16:49–16:51 UTC**. Composition counted from
`decks/markov_chains/cards.json` (built 2026-09-07, current with `base.txt` — same
commit). EDHREC from `commanders/edgar-markov` (n = 51,097) and its Tokens theme.
Combos via `combos.py`.

---

## Verdict: **NO**

A five-mana reactive spell that only does anything on the turn an opponent
chooses to swing lethal-ish combat damage at your face while you are holding
five mana open, in a deck whose entire plan is to tap out for a Vampire every
turn. The one loss it addresses is already covered, more completely and for two
mana less, by Teferi's Protection. Its tokens miss every Vampire payoff in the
list.

**Price: $5.80** (fetched 2026-09-24 16:49 UTC), under the $40 cap. Stated as
its own factor. **The rejection survives the card being free** — nothing below is
a price argument.

---

## 1. The card, verified

    Inkshield  {3}{W}{B}  Instant
      Prevent all combat damage that would be dealt to you this turn. For each
      1 damage prevented this way, create a 2/1 white and black Inkling creature
      token with flying.

- Mana value 5 · colour identity **BW** → **legal** in Edgar's WBR identity.
- Commander: legal. **Not** a Game Changer (deck is at 2 of 3: Necropotence,
  Teferi's Protection).
- `combos.py --add "Inkshield"` → **0** new combos, 0 newly within reach.
  Baseline stays at the two late-game Bloodthirsty Conqueror lifegain loops.
- Ruling (2021-04-16): with multiple prevention effects you choose the order.
  Nothing else on record.

Scope, read on the four axes:

| Axis | Inkshield |
|---|---|
| Whose damage | **to you** only — not to your creatures, not to Sorin |
| What kind | **combat** only — burn, drain, combo and "each opponent loses" all go through |
| Whose turn | any, but in practice **an opponent's** — see §3b |
| Who chooses | the **opponent** chooses whether to attack you at all |

No veto. Decided on merit.

## 2. Steel-man — the strongest honest case

Written as a claim that could be false:

> *Inkshield is the only card that turns an opponent's alpha strike into a
> board, and this deck has four token-enter payoffs (Mirkwood Bats, Impact
> Tremors, Baron Bertram Graywater, Welcoming Vampire), ten sac outlets and
> nine death triggers waiting for exactly that board. Twelve damage prevented
> with Mirkwood Bats out is twelve life from each opponent on the spot, and the
> survivors are twelve 2/1 fliers that share a creature type for Shared
> Animosity next turn.*

That is a real case, and I want to be precise about how real:

- **Mirkwood Bats** — "Whenever you **create** or sacrifice a token, each
  opponent loses 1 life." Fires once per Inkling created. Twelve Inklings is
  twelve drain to each opponent, then twelve more when they are sacrificed.
- **Impact Tremors** — "Whenever a creature you control enters, this enchantment
  deals 1 damage to each opponent." Same per-token rate.
- **Baron Bertram Graywater** — "Whenever one or more tokens you control enter,
  create a 1/1 … Vampire Rogue … This ability triggers **only once each turn**."
  One extra body, not twelve.
- **Welcoming Vampire** — 2/1 Inklings are power ≤ 2, so: one card, once.
- **Shared Animosity** — Inklings are Inklings; N attacking Inklings each get
  +(N−1)/+0. Twelve of them attacking is lethal on its own.
- Death triggers that count Inklings: **any-creature** group (Blood Artist,
  Cordial Vampire, Elenda, Vein Ripper, Blade of the Bloodchief) and
  **you-control** group (Bastion of Remembrance, Cruel Celebrant, Grave Pact,
  Zulaport Cutthroat). Nine cards. All fire on an Inkling dying.

It is also, honestly, the deck's **second** answer to "I take lethal combat
damage this turn." The first is Teferi's Protection. Clever Concealment phases
out *permanents*, not you; Akroma's Will's protection mode is on *creatures you
control*, not you. So the role currently has exactly one card.

Now the attack.

## 3. Why it fails anyway

### 3a. Five mana held open is the wrong shape for this deck

Curve from `cards.json`: **1→12 · 2→13 · 3→19 · 4→13 · 5→5 · 6→3**, average
nonland MV **2.92**, 35 lands, 7 nonland mana sources. Cards at MV ≥ 5 in the
99: Anowon, Bloodthirsty Conqueror, High-Society Hunter, Malakir Bloodwitch,
Olivia's Wrath, Patron of the Vein, Vein Ripper — **seven, every one of them a
proactive spell you cast on your own turn.** Inkshield would be the eighth and
the **only reactive card in the deck above MV 3** (the instants are Swords {W},
Dark Ritual {B}, Village Rites {B}, Malakir Rebirth {B}, Soul Shatter {2}{B},
Anguished Unmaking {1}{W}{B}, Teferi's Protection {2}{W}, Akroma's Will {3}{W},
Clever Concealment {2}{W}{W} with convoke).

The Teferi's Protection review made the "held-open mana" objection at three
mana and it was judged real but survivable because the window that mattered
started around turn 5–6. At **five** mana the objection is not survivable: a
deck whose engine is *cast a Vampire, get a token* has to skip its Vampire on
the turn it holds Inkshield up, and it has to keep doing that every turn until
someone attacks it. Every turn you hold five open and nobody swings, you have
spent a turn of eminence for nothing.

Pips are fine — `{W}{B}` is already asked for by seven cards, 17 W land sources
/ 26 B / 10 duals that make both, plus Signet and Talisman of Hierarchy. The
cost is the five, not the colours.

### 3b. The opponent decides whether it ever does anything

"Prevent all combat damage that would be dealt **to you**." Two things follow.

First, it is blank against everything that is not a creature attacking you:
burn, drain, "each opponent loses life," combo kills, wipes, and damage to
Sorin. Teferi's Protection covers all of those; Inkshield covers one.

Second, the card's whole value scales with **how much an opponent chooses to
point at you.** A 4-player pod with rotating decks (per `meta.json`) does not
let me assert that number. What I *can* say from the list: this deck attacks
with everything every turn (Edgar's trigger, Sanctum Seeker, Shared Animosity
all reward it) and has **one** vigilance creature (Charismatic Conqueror), so it
is often the most crack-back-able board at the table — which is the best
argument for the card — but the same list has **38 creatures**, and a player who
sees five open mana and a wide board in front of an Orzhov player often simply
attacks someone else. The card is at its best exactly when you look weakest,
and this deck rarely looks weak.

### 3c. The board it makes is not this deck's board

Inklings are **not Vampires**. Verified, the following do nothing for them:

| Card | Clause | Inklings get |
|---|---|---|
| Legion Lieutenant | "Other **Vampires** you control get +1/+1" | nothing |
| Captivating Vampire | "Other **Vampire** creatures you control get +1/+1" | nothing |
| Stromkirk Captain | "Other **Vampire** creatures … +1/+1 and first strike" | nothing |
| Edgar, Charmed Groom | "Other **Vampires** you control get +1/+1" | nothing |
| Lord of Lineage | "Other **Vampire** creatures you control get +2/+2" | nothing |
| Vampire Nocturnus | "other **Vampire** creatures … +2/+1 and flying" | nothing |
| Edgar Markov | "put a +1/+1 counter on each **Vampire** you control" | nothing |
| Cordial Vampire | "put a +1/+1 counter on each **Vampire** you control" | nothing |
| Indulgent Aristocrat | "+1/+1 counter on each **Vampire** you control" | nothing |
| Sanctum Seeker | "Whenever a **Vampire** you control attacks" | nothing |
| Master of Dark Rites | mana "only to cast Vampire, Cleric, and/or Demon spells" | nothing (they can still be the sacrifice) |

Eleven cards. The deck's bridge between its two modes — deaths becoming +1/+1
counters on Vampires — does not touch an Inkling. What *does* touch them is the
per-token drain (Mirkwood Bats, Impact Tremors: **two** cards in 99), one
extra body (Baron), one card (Welcoming Vampire), Shared Animosity, and the
sac/death package. The explosive line in §2 needs **Mirkwood Bats specifically**
on the battlefield; without it, twelve Inklings are twelve 2/1 fliers with no
lord, no counters and no attack trigger, which is a fine chump-block wall and
not a win.

Two small nonbos, recorded not weighed: **Olivia's Wrath** ("Each **non-Vampire**
creature gets -X/-X") kills your own Inklings, and **Anowon** makes you sacrifice
one each upkeep (a non-Vampire "of their choice" — yours, so it costs you the
worst one; negligible). And because Inkshield is cast on an opponent's turn,
**Bloodletter of Aclazotz** ("during **your** turn") does not double the Bats /
Tremors drain, and **Florian** never sees it.

### 3d. Which loss does it fix?

Applying the marginal-impact test honestly:

| Loss | Inkshield | Already covered by |
|---|---|---|
| Board wiped | no | Clever Concealment, Teferi's Protection, Akroma's Will (partial) |
| Killed by combat damage to your face | **yes** | Teferi's Protection |
| Killed by noncombat / combo / drain | no | Teferi's Protection |
| Slow start, bad draw | no — it is the worst card in a slow hand | — |

It improves one row, and that row already has the better card in it. The
rubric's question — *does it change games you lose?* — gets "only the games
you lose to a combat alpha while holding five mana, and TP was not in hand."

### 3e. Worst-case draw

Opening hand on the draw against the fastest deck: dead until turn five, and
turns five through seven are when this deck wants to cast Bloodthirsty
Conqueror, Malakir Bloodwitch and Vein Ripper. Turn twelve with an empty board:
genuinely good — a fog that makes a board out of the swing that would have
killed you. Dead early, strong late, and the deck is built to be strong early.

### 3f. Not a Vampire

Tiebreaker only per `meta.json`, but every three-mana Vampire spell in this list
also makes a 1/1 off eminence. This makes nothing on cast.

## 4. Redundancy, done as effect × frequency × duration

- **Teferi's Protection**: all damage and all life change, one shot, until
  your next turn, 3 mana, phases out your board too.
- **Inkshield**: combat damage to you, one shot, this turn, 5 mana, makes
  tokens.

Not redundant — different effect and different rider. But the role ("do not
die this turn") has one card today and Inkshield would be the second, and the
first is the one you would rather draw in every scenario except "an opponent
swung 12 at me and I have Mirkwood Bats out."

## 5. Community check

- **Edgar commander page**: Inkshield is **not in the top 31 instants** (floor
  5.3%, 2,694 of 51,097 decks — Deflecting Swat). Not in the Tokens theme's 29
  instants either.
- **Its own page**: EDHREC rank 786; top commanders are Killian (75.5%),
  Shadrix Silverquill (73.2%), Breena (65.7%), Queen Marchesa (56.1%) — pillow-
  fort and politics decks that *want* to be attacked and hold mana up by design.
  Edgar is not on the list.
- I am agreeing with a low inclusion, so the independent reason: §3a. Those
  decks hold mana; this one spends it.

## 6. The cut I would have had to make

Only recorded because the rubric says the quality of the best available cut is
itself evidence. Same-role cuts do not exist (the protection instants are all
better here). Same-MV cuts: of the five 5-drops, the weakest is **High-Society
Hunter** — a 5/3 flier whose draw trigger reads "**nontoken** creature dies,"
narrow in a deck whose deaths are mostly tokens. And I would still defend it
over Inkshield: it is a Vampire spell (eminence token on cast, four lords, Edgar
counters) that attacks every turn with a built-in sac outlet. When the best cut
is a card you would defend, the add is not worth it. That is the finding.

## 7. Counter-proposal — if the role is real

The role — *a second card that stops you dying to a combat swing* — is thin at
one card. Whether it is worth a slot depends on one thing I cannot read from
the list: **are you actually losing games to combat damage aimed at you,
rather than to wipes, combos or drain?** If yes, the card to run through this
rubric is not Inkshield. Verified this session, all under the cap:

| Card | Cost | Text (abridged, verified) | Price |
|---|---|---|---|
| **Comeuppance** | `{3}{W}` | Prevent all damage (not just combat) to you and your planeswalkers from sources you don't control; deals it back to each creature source, or to the controller of a noncreature source. | $5.54 |
| Dawn Charm | `{1}{W}` | Fog **all** combat damage, or counter a spell that targets you. | $2.97 |
| Batwing Brume | `{1}{W/B}` | Fog all combat damage; each player loses 1 per attacking creature they control. | $7.53 |
| Settle the Wreckage | `{2}{W}{W}` | Exile all attacking creatures target player controls. | $0.42 |

Comeuppance is the one I would evaluate first: one mana cheaper, covers burn and
combo damage that Inkshield does not, and answers the alpha by killing the
attackers rather than by making 2/1s that the deck cannot pump. **This is not
an ADD** — I have not run it through the cut discipline and the §3a objection
applies at four mana too, just less hard. It is the right card to test if you
confirm the loss.

## 8. Summary

| Card | Price (2026-09-24 16:49–16:51 UTC) | Verdict |
|---|---|---|
| **Inkshield** | $5.80 | **NO** — a 5-mana reactive spell in a tap-out eminence deck; only prevents combat damage to you, which Teferi's Protection already does more completely at 3; its tokens miss all eleven Vampire payoffs. Rejection stands at $0. |
| Comeuppance | $5.54 | not evaluated — the card to test **if** combat damage to your face is a recurring loss |

## 9. What I am unsure about, and what would settle it

- **Which loss the deck takes.** If you keep dying to alpha strikes, the role
  is real and §7 applies. If you keep dying to wipes or drain, this whole
  category is the wrong place to spend a slot.
- **How often you actually get attacked.** §3b is a reading of the list, not of
  your games. If opponents routinely swing 10+ at you because you are the drain
  deck, Inkshield's ceiling is higher than I have credited — but §3a and §3c
  do not move, and the verdict would not either without a cut I could defend.

## Sources

- Scryfall via `card_facts.py lookup`, fetched **2026-09-24 16:49–16:51 UTC**:
  Inkshield $5.80 (rank 786, BW, legal, not a Game Changer, 1 ruling) ·
  Teferi's Protection $49.83 (Game Changer) · Clever Concealment $3.54 ·
  Akroma's Will $15.58 · Mirkwood Bats $1.31 · Baron Bertram Graywater $0.42 ·
  Welcoming Vampire $3.37 · Impact Tremors (foil $2.24, no nonfoil price) ·
  Shared Animosity $5.18 · Bloodletter of Aclazotz $39.09 · Olivia's Wrath
  $0.47 · Anowon $2.56 · Sorin, Imperious Bloodlord $6.22 · Comeuppance $5.54 ·
  Batwing Brume $7.53 · Dawn Charm $2.97 · Settle the Wreckage $0.42 ·
  Deflecting Palm $3.15 · Darkness $24.03.
- `card_facts.py search 't:instant id<=wbr (o:"prevent all combat damage" or
  o:"prevent all damage that would be dealt to you")'` — 28 matches, fetched
  2026-09-24 16:51 UTC.
- EDHREC `commanders/edgar-markov`, n = 51,097 (brackets 1→95, 2→3,511,
  3→5,508, 4→4,104, 5→178); instants list (31 cards, floor 5.3%) via
  `--tags instants`; Tokens theme instants (29 cards). Inkshield absent from
  both. Inkshield's own page: rank 786, top commanders as quoted in §5.
- Commander Spellbook via `combos.py markov_chains --add "Inkshield" --near`:
  baseline 2, **0** newly completed, 0 newly within reach.
- Composition, curve, MV ≥ 5 list, instants, token makers, enter payoffs, sac
  outlets, death-trigger scope groups, vigilance count and colour sources
  computed from `decks/markov_chains/cards.json`.

`base.txt` was not modified.
