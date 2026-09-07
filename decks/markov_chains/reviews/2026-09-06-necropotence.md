# markov_chains — Necropotence, 2026-09-06

Question asked: *"Necropotence"*. One candidate, one cut.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 (up to 3
Game Changers, no early infinites) · $40/card cap · 4-player casual pods. Vetoes: no
early infinite combos, no tutor-dependent win line. Preference: on-theme Vampires,
tiebreaker only.

Pod facts carried forward from the 2026-08-30 → 09-06 reviews (user-stated, not
`meta.json`): games run **long**; the three opponents are **mono-white — 2
fat-creature builds + 1 token swarm**; **Farewell and Armageddon are commonly
played**; the deck is dual-mode (Edgar-on-board aggro / Edgar-absent aristocrats
drain, bridged by the +1/+1 counter package).

All oracle text, legality, colour identity and prices fetched live from Scryfall
**2026-09-06 18:06–18:10 UTC**. Deck composition recounted from
`decks/markov_chains/cards.json` (built 2026-09-04; `base.txt` last changed
2026-09-03, so no rebuild was needed). EDHREC from `commanders/edgar-markov`
(n = 50,363), the Aristocrats and Lifegain theme pages, and the card's own page.
Combos via `combos.py --add`.

---

## Verdict

**ADD — cut Painful Truths.**

| | |
|---|---|
| Card | **Necropotence** `{B}{B}{B}` Enchantment |
| Price | **$36.97** (fetched 2026-09-06 18:06 UTC) — under the $40 cap |
| Game Changer | **Yes.** Deck goes from 1 of 3 (Teferi's Protection) to **2 of 3** |
| EDHREC | 10.9% of Edgar decks (5,480 / 50,363) · 18.5% of Edgar *Aristocrats* decks (272 / 1,467) · 11.6% of Edgar *Lifegain* decks (395 / 3,396) · global rank 508 |
| Combos | 0 newly completed; 4 "newly within reach", none with a piece the deck runs or should run |
| Cut | **Painful Truths** `{2}{B}` sorcery, $0.33, EDHREC rank 1,703 |

Price is its own line and does not carry the verdict: the ADD holds at $0. The one
cost that *is* load-bearing is the Game Changer slot, discussed below.

---

## The card, verified

> Necropotence `{B}{B}{B}` — Enchantment
> Skip your draw step.
> Whenever you discard a card, exile that card from your graveyard.
> Pay 1 life: Exile the top card of your library face down. Put that card into your
> hand at the beginning of your next end step.

Rulings that matter here (2017-11-17): the last ability is a **delayed trigger**
that fires at the beginning of your *next* end step, and it still fires if
Necropotence has left the battlefield. Practical consequence: activate it in your
**second main phase**, before the end step begins; activations made *during* the end
step deliver a full turn later. Cards arrive at end step, then the cleanup step
discards you to seven — and those discards are **exiled**, not binned.

Legal, mono-black identity, inside the deck's BRW identity.

---

## Step 0 — the honest best case

*This deck manufactures a surplus resource (life) from 21 verified sources and has
no sink for it that scales; Necropotence converts that surplus into cards at one
life per card, with no mana after the first three, and it is the only draw engine in
the list that survives Armageddon, needs no creatures, and refills to seven in a
single turn after a wrath.*

That is a claim that can be false on four counts: the lifegain count, the "no
scaling sink" claim, the survivability claim, and the "only" claim. Each is checked
below.

---

## The deck, recounted this session

From `cards.json`: 100 cards · 35 lands · 65 nonland · average nonland MV **2.88**.
Curve: 1 → 12 · 2 → 15 · **3 → 18** · 4 → 12 · 5 → 5 · 6 → 3. MV 3 is the fattest
rung, as every review since 08-31 has noted.

Pips: **B 64 · W 15 · R 4**. Game Changers: **1** (Teferi's Protection).
Enchantments: 5 (Bastion of Remembrance, Black Market Connections, Grave Pact,
Impact Tremors, Oubliette).

### Black sources — can the deck cast `{B}{B}{B}`?

Lands producing black: **26 of 35** by Scryfall's `produced_mana`. Honest split:

- **22 unconditional**: Blood Crypt, Bojuka Bog, Canyon Slough, Caves of Koilos,
  Command Tower, Dragonskull Summit, Godless Shrine, Haunted Ridge, Isolated Chapel,
  Nomad Outpost, Path of Ancestry, Shattered Sanctum, Smoldering Marsh, Sulfurous
  Springs, Swamp ×7, Takenuma. (Plus Malakir Mire as an MDFC land.)
- **4 conditional**: Exotic Orchard (opponents' lands — mono-white pod, so this is
  *white*, not black, most games), Fetid Heath (needs a `{W/B}` to filter), Phyrexian
  Tower (`{B}{B}` only with a sacrifice), Voldaren Estate (Vampire spells only —
  **cannot cast Necropotence**).

Nonland black: Arcane Signet, Talisman of Hierarchy, Talisman of Indulgence, Dark
Ritual. **Master of Dark Rites cannot cast it** — verified text: *"Spend this mana
only to cast Vampire, Cleric, and/or Demon spells."*

The deck already carries four `{B}{B}{B}`-pip cards at MV 4–6: Grave Pact, Bloodletter
of Aclazotz, Vampire Nocturnus, Vein Ripper. Necropotence asks for the same three
black pips one land earlier. With 22 clean black lands of 35, a natural turn-3
`BBB` from three lands is roughly a one-in-three proposition; turn 4–5 is the
realistic floor, and **Dark Ritual** (`{B}` → `{B}{B}{B}`, verified) casts it on turn
one or two. Phyrexian Tower plus one Swamp plus a sacrifice is a turn-2 line. This
is friction the mana base was already built to absorb, not a new demand.

### Lifegain — the resource Necropotence spends

21 cards put life on the table, grouped by scope (verified text):

| Scope | Cards |
|---|---|
| Drain-and-gain on **any** creature dying | Blood Artist (target player loses 1, you gain 1) · Vein Ripper (target opponent loses 2, you gain 2) |
| Drain-and-gain on **your** creature dying | Zulaport Cutthroat · Cruel Celebrant · Bastion of Remembrance (each opponent loses 1, you gain 1) |
| Drain-and-gain on attack / ETB | Sanctum Seeker (each Vampire attacks: each opponent loses 1, you gain 1) · Malakir Bloodwitch (ETB: opponents lose life = your Vampire count, you gain that much) |
| **Opponent's loss → your gain** | **Bloodthirsty Conqueror** — *"Whenever an opponent loses life, you gain that much life"* — the multiplier: every drain trigger above, every combat hit, every Bloodletter-doubled loss, becomes life |
| Lifelink bodies | Indulgent Aristocrat · Vampire of the Dire Moon · Qarsi Revenant · Elenda · Henrika (transformed) |
| Lifelink tokens | Baron Bertram Graywater · Charismatic Conqueror · Edgar Markov's Coffin · Elenda's death tokens |
| Lifelink grants | Vito (`{3}{B}{B}` activation) · Vault of the Archangel · Sorin +1 · Akroma's Will |
| Convert *gaining* into drain | Vito, Thorn of the Dusk Rose · Marauding Blight-Priest |

The last row matters for the anti-synergy check: Vito and Blight-Priest key off
**gaining** life, not the life total. Paying life to Necropotence does not turn them
off; the next lifelink hit still triggers both.

### Life already treated as a resource

16 cards in the list pay life or damage you: Anguished Unmaking, Black Market
Connections, Night's Whisper, Painful Truths, Malakir Rebirth, Henrika (draw mode),
War Room, Voldaren Estate, three Talismans, three painlands, two shocklands. The
deck already spends life; it spends it at fixed, small rates. Black Market
Connections' draw mode — *"Draw a card. You lose 2 life"*, once per turn — is the
best existing sink and it is 2 life per card, capped at one card. Necropotence is 1
life per card, capped at hand size. The "no scaling sink" claim holds.

### Card draw — what already does this job

15 cards touch card flow (the 08-31 audit counted 12; I am counting three more
marginal ones for completeness). Grouped by what kills them:

| Group | Cards | Dies to |
|---|---|---|
| **Creature-bound engines** (6) | Baron Bertram (`{1}{B}`, sac: draw) · Clavileño (attacker dies: draw) · Florian (impulse, X = life opponents lost) · Henrika (once) · High-Society Hunter (nontoken death: draw) · Welcoming Vampire (power ≤ 2 enters: draw, once/turn) | any creature wipe |
| **Noncreature repeatable** (4) | Black Market Connections (1 card / 2 life / turn) · Herald's Horn (top-card Vampire creatures only) · Skullclamp (needs a body) · Voldaren Estate (Blood token, `{1}`, discard) | Farewell's artifact / enchantment modes; Skullclamp also needs creatures |
| **Lands** (2) | War Room (`{3}`, `{T}`, 3 life: draw 1) · Canyon Slough (cycle once) | Armageddon |
| **One-shot** (3) | Night's Whisper (2 cards / 2 life) · Painful Truths (X cards / X life, X = colours spent) · Village Rites (sac: 2 cards) | nothing — but they are one card each |

The survivability claim, against the pod's two named wipes (both verified):

- **Farewell** (`{4}{W}{W}`, *"Choose one or more — Exile all artifacts / all
  creatures / all enchantments / all graveyards"*): a full-mode Farewell takes
  Necropotence with everything else. Nothing in the deck survives it except lands.
  No draw card is better here; War Room is the only engine left standing and it is
  3 mana + 3 life per card.
- **Armageddon** (`{3}{W}`, *"Destroy all lands"*): Necropotence survives and is
  the **only** repeatable card-flow source that then costs zero mana per card (Black
  Market Connections also needs no mana but is one card per turn). The six creature
  engines survive too, but every one of them needs the deck to *do* something — cast,
  attack, sacrifice — and with no lands, casting is the bottleneck. Seven cards in
  hand with no mana is still better than one.
- **A plain creature wrath** (the mono-white pod's most likely play): six draw
  engines gone, Necropotence untouched. The turn after, it converts the life banked
  from the pre-wrath drain into a fresh seven. This is the case that matters most
  often, and it is where Necropotence stops being "another draw card."

The "only" claim survives with one qualification: Black Market Connections is the
other post-Armageddon engine, at a seventh of the volume and twice the price per
card.

---

## The tests

### Redundancy — effect × frequency × duration

No existing card matches on all three terms:

| | Effect | Frequency | Duration |
|---|---|---|---|
| **Necropotence** | N cards for N life, N ≤ hand room | every turn, at will, no mana | permanent |
| Black Market Connections (draw mode) | 1 card for 2 life | once per turn | permanent |
| Painful Truths | ≤ 3 cards for ≤ 3 life | once | one-shot |
| Night's Whisper | 2 cards for 2 life | once | one-shot |
| War Room | 1 card for 3 life + 3 mana | once per turn | permanent (land) |
| Skullclamp | 2 cards per equipped death | per death, `{1}` each | needs bodies |

The closest card on *rate* is Painful Truths (1 life per card), and it is a one-shot.
That is why it is the cut, not a reason Necropotence is redundant with it. The
closest on *duration* is Black Market Connections, at half the rate and a seventh
the ceiling. Not redundant.

### Density — how many cards turn it on?

Necropotence needs life, not board. 21 lifegain sources feed it and 35 lands cast
it; every card in the deck "turns it on" in the sense that its cost is a resource
the deck cannot run out of while the drain engine is working. Passes.

### Marginal impact — does it change games the deck loses?

The 09-03 role audit named exactly one open gap: **board rebuild after a wipe** (2
sources). The pod's mono-white opponents are the wrath colour, and Farewell and
Armageddon are both stated as common. Necropotence does not recur anything, but it
is the deck's largest single refuel, and it is the *only* refuel that costs nothing
after a land wipe and needs no creatures after a creature wipe. The 08-30 review
spared Champion of Dusk on exactly this reasoning — *"in the long games this pod
actually plays, that is the deck's largest single refuel, and the lifelink density
pays the life cost"* — and Champion has since been cut. This is a better version of
the same card: no body to wrath, no `{3}{B}{B}` recast, no dependence on Vampire
count.

Is it win-more? It is best when life is high, and life is high when the drain
engine is running — which is the deck being *ahead on board*, not ahead on the game.
The specific game it fixes is: drain for twenty, get wrathed, sit with an empty hand
and 45 life. That is a game this deck currently loses slowly and would win with seven
new cards. It is not a card that wins already-won games; it is a card that spends a
resource the deck banks and then has nowhere to put.

This rests partly on the speed premise (long games). That premise was confirmed by
the user across four reviews and corrected the other direction on 08-30; I am
carrying it forward, not re-litigating it. If the pod has sped up since, the ADD
weakens but does not flip — turn-3 Necropotence into seven cards is not a slow play.

### Cost of entry

MV 3 → MV 3 with the Painful Truths cut: the fattest rung stays at **18**, average
stays **2.88**. Pips: B 64 → **66** (+3, −1), W 15, R 4. Black is already 64 of 83
coloured pips; the mana base is built for this.

### Anti-synergy — looked for, found small

- **Skip your draw step.** One card per turn forgone. Necropotence has to produce at
  least one card per turn to break even; it produces up to seven. Herald's Horn,
  Florian and Vampire Nocturnus all work off the *top of the library*, not the draw
  step, and are unaffected.
- **Discards are exiled.** The deck's discard-adjacent cards are Canyon Slough
  (cycling itself), Takenuma (channel, discards itself), and Voldaren Estate's Blood
  token. The real cost: cleanup discards from over-activating are exiled, so
  **Bloodghast** (landfall recursion from the graveyard) and **Qarsi Revenant**
  (Renew from the graveyard) lose their graveyard modes if you pitch them. Pay for
  what you can hold; this is player discipline, not a nonbo.
- **Teferi's Protection.** *"Your life total can't change"* until your next turn —
  no Necropotence activations during that window. Irrelevant in practice.
- **Vampire Nocturnus.** Exiling the top card face down changes the revealed card.
  Mildly *positive*: 1 life flips a non-black top card until a black one shows.
- **Bloodletter of Aclazotz** doubles *opponents'* life loss on your turn; it does
  not touch yours.
- **Vito / Marauding Blight-Priest** trigger on *gaining* life; paying it away does
  not interfere.
- **Symmetry.** None. One-sided.
- **The real cost:** two fat-creature decks in the pod means combat pressure on
  your life total is genuine. Necropotence is optional per point; the deck's 21 gain
  sources and Bloodthirsty Conqueror's conversion are the counterweight. If the deck
  routinely sits below 15 life mid-game, Necropotence is a much weaker card. I do not
  have that number; see "What would change my mind."

### Worst-case draw

- **Opening hand, on the draw, against the fastest deck at the table.** `{B}{B}{B}`
  by turn 3 is roughly one in three from lands alone; Dark Ritual makes it turn 1–2.
  A turn-4 or turn-5 Necropotence into a full hand is still the strongest thing this
  deck can do that turn. Never dead in an opener.
- **Turn 12, empty board.** At 30+ life: three mana, seven cards, game back on. At 8
  life facing two fat mono-white boards: a three-mana enchantment that draws two.
  That tail is real and it is correlated with already losing. Compare Painful Truths
  in the same spot: three cards once, at the same life rate, then nothing.

### Bracket fit — the one real cost

Necropotence is a **Game Changer**. The deck runs one (Teferi's Protection); bracket
3 allows three. Adding it spends the second slot. It is not fast mana, not a tutor,
and it completes no combo the deck runs (`combos.py --add`: 0 new; the four
"within reach" lines need Approach of the Second Sun, Near-Death Experience, Ashiok,
Wicked Manipulator or Cool but Rude, none of which belong here and one of which —
Near-Death Experience — would violate the no-tutor-dependent-win-line veto in
spirit). Both `meta.json` vetoes clear.

The remaining Game Changer slot is the thing being spent. Given the deck's vetoes
rule out the tutors that make up most of EDHREC's Game Changer list for Edgar
(Demonic Tutor 29.2%, Vampiric Tutor 28.9%), the realistic competitors for the third
slot are Smothering Tithe (23.3%) and Bolas's Citadel (20.1%). Neither has been
proposed; I am naming them so the slot is spent knowingly.

### Disagreement check

I say ADD; the community says **10.9%** (5,480 / 50,363 Edgar decks). What is
different about this deck? Three named things:

1. **Bracket suppression.** EDHREC's bracket counts for Edgar are 3,520 bracket-2 and
   92 bracket-1 decks against 5,379 bracket-3 and 4,013 bracket-4 — a quarter of the
   bracketed lists cannot run a Game Changer by rule. Within the *Aristocrats* theme,
   which is what this deck is, inclusion rises to 18.5% (272 / 1,467).
2. **Speed.** Most Edgar lists are the turn-6 aggro deck; in that deck the game ends
   before life-to-cards matters. This pod's games run long, so the duration term —
   the whole reason to prefer an engine over a one-shot — is fully live.
3. **Lifegain density.** 21 sources including Bloodthirsty Conqueror is high even
   for Edgar, and the deck's recorded gap is post-wipe rebuild.

Phyrexian Arena (28.5%, 14,363 / 50,363; `{1}{B}{B}`, $4.50 at 18:08 UTC) is the
non-Game-Changer comparator the community prefers: one card per upkeep for one
life. Verified text. It is the same rate at a fifteenth of the ceiling, and it does
nothing the turn after a wrath that Black Market Connections does not already do.
If the Game Changer slot is the objection, Arena is the fallback — but it is a
different card, not an 80%-as-good one.

Dark Prophecy (`{B}{B}{B}`, *"Whenever a creature you control dies, you draw a card
and you lose 1 life"*, $6.77, 2.2% of Edgar decks) is the on-theme aristocrats
engine. It is creature-dependent — exactly the failure mode the wipe problem is
about — and loses to Grim Haruspex / Midnight Reaper on cost. Not a counter-proposal.

### Price

$36.97 (2026-09-06 18:06 UTC). Under the $40 cap. Not load-bearing: the ADD holds
at $0, and would hold at $60 if the cap were not a house rule — it is, so above $40
it would be the user's call.

---

## The cut — Painful Truths, and the runners-up

**Painful Truths** `{2}{B}` sorcery — *"Converge — You draw X cards and lose X life,
where X is the number of colors of mana spent to cast this spell."* EDHREC rank
1,703, $0.33.

Why it and not another draw card:

- **Same role, same MV, same life-per-card rate, strictly less of it.** Necropotence
  at three mana and three life gives the same three cards on the turn it resolves,
  then keeps going. There is no axis on which Painful Truths is better.
- **Its full rate is conditional on three colours.** X = 3 needs a red *and* a white
  source in the same turn, in a deck with **4 red pips** and Voldaren Estate's mana
  restricted to Vampires. Turn-3 Painful Truths for three is not a given; for two it
  is Night's Whisper at one more mana.
- **Never spared.** Every prior mention of Painful Truths in the review history is a
  line in a draw-count list. No review has given it a specific reason to stay.

Runners-up, in order, each with why it was spared:

1. **Night's Whisper** `{1}{B}` — cheaper, mono-black, unconditional. Strictly
   better than Painful Truths in this mana base. Keep.
2. **War Room** — the worst *rate* in the deck (3 mana + 3 life per card), but it
   is a land, it survives Farewell, and cut discipline says never cut a land for a
   spell. Keep.
3. **Forerunner of the Legion** — the 09-06 review's top cut, and still the next
   cut if you would rather keep Painful Truths. Not a draw card, so it breaks the
   same-role rule; that is the only reason it is not first.
4. **Henrika Domnathi** — the 09-06 runner-up. Same reasoning.
5. **Village Rites** — spared because it is the deck's only *instant-speed* draw
   that also acts as a sacrifice outlet in response to removal; that is a role
   Necropotence does not fill.

Aggregate delta with the Painful Truths cut: curve unchanged (MV 3 stays 18), B pips
64 → 66, card-flow sources 15 → 15, Game Changers 1 → 2, enchantments 5 → 6.

---

## How to play it here (from the rulings, not opinion)

- Activate in your **second main phase**, not the end step. Activations during the
  end step deliver next turn.
- Cards arrive at the beginning of your end step, so they are in hand for
  opponents' turns — Village Rites, Malakir Rebirth, Anguished Unmaking, Soul
  Shatter, Clever Concealment and Teferi's Protection are all live off Necropotence
  cards the same turn.
- Do not overpay past seven: cleanup discards are exiled, and Bloodghast and Qarsi
  Revenant are the two cards that specifically mind.
- Master of Dark Rites' mana cannot cast it. Dark Ritual's can.

---

## What I am unsure about, and what would settle it

- **Mid-game life totals in this pod.** The whole case assumes the drain engine
  banks life faster than two fat-creature decks take it. If the deck is often under
  15 life by turn 8, Necropotence's ceiling collapses and the ADD becomes an ADD IF.
  Two or three games' worth of "what was my life total when I would have wanted to
  activate this" would settle it.
- **The second Game Changer slot.** If Smothering Tithe or Bolas's Citadel is on the
  wish list, this is a decision about which two of the three the deck wants, not
  about whether Necropotence is good. I have named the competitors; I have not
  evaluated them.
- **Farewell frequency vs. creature-wrath frequency.** If the pod's wipes are mostly
  Farewell with the enchantment mode chosen, Necropotence's survivability edge over
  the creature engines is smaller than argued. It is still the better refuel when it
  lives.

---

## Prices and figures used (fetched 2026-09-06 18:06–18:10 UTC)

| Card | Price (USD) | EDHREC rank | Edgar decks |
|---|---|---|---|
| Necropotence | 36.97 | 508 | 10.9% (5,480 / 50,363); Aristocrats 18.5% (272 / 1,467); Lifegain 11.6% (395 / 3,396) |
| Painful Truths | 0.33 | 1,703 | — |
| Phyrexian Arena | 4.50 | 102 | 28.5% (14,363 / 50,363) |
| Dark Prophecy | 6.77 | 4,329 | 2.2% (1,091 / 50,363) |
| Grim Haruspex | 3.30 | 1,135 | — |
| Midnight Reaper | 0.23 | 1,050 | — |
| Teferi's Protection | 48.11 | 109 | 31.3% (15,758 / 50,363) |
| Black Market Connections | 8.08 | 131 | — |
| Night's Whisper | 5.45 | 182 | — |
| Bloodthirsty Conqueror | 36.23 | 858 | — |
| Farewell | 6.06 | 171 | — |
| Armageddon | 13.72 | 4,053 | — |

Edgar Markov bracket counts on EDHREC: 1 → 92 · 2 → 3,520 · 3 → 5,379 · 4 → 4,013 ·
5 → 174. Game Changers in Edgar decks: Demonic Tutor 29.2%, Vampiric Tutor 28.9%,
Smothering Tithe 23.3%, Bolas's Citadel 20.1%, Enlightened Tutor 11.9%,
Necropotence 10.9%.

`combos.py --add "Necropotence"`: baseline 2 combos assembled; 0 newly completed; 4
newly within reach (Approach of the Second Sun, Near-Death Experience, Ashiok Wicked
Manipulator, Cool but Rude — none in the deck).

`base.txt` was not modified.
