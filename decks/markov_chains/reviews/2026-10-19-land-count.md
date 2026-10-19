# markov_chains — land count, 2026-10-19

Question: *"Should I be running more lands? If so, which ones and what gets swapped?"*

Deck context (`deck_meta.py show`): Edgar Markov · bracket 3 · $40/card cap ·
rotating 4-player pod (no fixed opponent profile). `base.txt` and `cards.json` in
sync (100 cards, nothing missing). All card text and prices fetched live from
Scryfall 2026-10-19 07:26–07:28 UTC.

## Verdicts

| Change | Verdict |
|---|---|
| Raise the count 34 → 35 (land for a spell) | **NO** |
| **Sundown Pass → Swamp** (count stays 34) | **ADD** |
| Fell the Profane (MDFC) for Oubliette | **ADD IF** you're actually missing land drops in real games |

## Where the mana stands

- **34 lands + Malakir Rebirth (MDFC, its land side enters tapped)**. Nonland mana:
  Sol Ring, Arcane Signet, three Talismans, Dark Ritual, Master of Dark Rites.
- Average nonland MV **2.94**. Curve 1:12 · 2:13 · 3:20 · 4:12 · 5:6 · 6:2 (Edgar
  excluded). 45 cards at MV ≤3, only 8 at 5+.
- Edgar's eminence runs from the command zone, so the deck never *needs* to
  reach 6 mana.
- **How the count drifted:** 36 lands at MV 2.83 (08-31 audit) → 35 (Orzhov
  Basilica cut) → 34 (Canyon Slough out for Edgar, Ancient Bloodlord, a Moxfield
  change on 09-29 that no review looked at). Over the same stretch average MV went up
  and Night's Whisper and Painful Truths left. So the question is fair: the count
  went down while the curve went up.

### Simulation (scratch Monte Carlo, 100k games per cell, one mulligan rule, ignores draw spells)

| Lands | 4 mana by T4 (draw) | 4 mana by T4 (play) | ≤2 lands on T4 (draw) | ≥9 lands in first 15 cards |
|---|---|---|---|---|
| 33 | 80.1% | 71.9% | 10.1% | 2.9% |
| **34 (now)** | **81.9%** | **74.0%** | **8.9%** | 3.7% |
| 35 | 83.8% | 75.8% | 7.9% | 4.4% |
| 36 | 85.2% | 77.9% | 6.8% | 5.1% |

One more land buys about **+2 points** of on-curve mana and about **−1 point** of
screw. That's roughly one game in fifty, and it leaves out the deck's draw engines
(Necropotence, Skullclamp, Black Market Connections, Village Rites and others),
which all help more against screw than against flood.

## Raise the count? NO

A 35th land has to beat the weakest spell that would stay. Every spell named as
weak in recent reviews has a recorded reason to stay:

- **Forerunner of the Legion**: the only tutor (09-06/07, 10-09).
- **Bloodthrone Vampire**: one of three free, unlimited sac outlets (10-09).
- **Malakir Bloodwitch**: one gain event that Vito turns into a big hit on one
  player (10-09 revision).
- **Florian**: already earmarked as the cut for Bloodline Recollector (10-09). I'm
  not spending it twice.

At about 2% of games, the 35th land doesn't beat any of these. 34 lands plus an
MDFC plus five rocks is a normal setup for a 2.94 curve whose commander does its job
from the command zone. If the curve keeps rising (MV ≥3.0, or more 5-drops), check
this again.

## ADD: Swamp, cut Sundown Pass

The real weakness is **black** mana, not the land count.

- **Black demand:** 64 black pips. 16 cards cost `{B}{B}` or more. Four cost `{B}{B}{B}`:
  Bloodletter of Aclazotz `{1}{B}{B}{B}`, Grave Pact `{1}{B}{B}{B}`,
  **Necropotence `{B}{B}{B}`**, Vein Ripper `{3}{B}{B}{B}`.
- **Black supply:** 25 lands list `{B}` in `produced_mana`, but 4 of those are
  conditional:
  - Exotic Orchard: "a land **an opponent controls** could produce". It depends
    on the opponent, and the pod now rotates.
  - Fetid Heath: a filter, so it needs another coloured mana to work.
  - Phyrexian Tower: `{B}{B}` only if you sacrifice a creature.
  - Voldaren Estate: coloured mana only for Vampire spells.

  That leaves about **21 unconditional black lands**.
- **Simulation (crude, relative only):** `{B}{B}{B}` by turn 4 comes out ~47% now,
  ~51% with this swap.

**Red is over-supplied.** There are 13 red sources and only 5 red cards, each with
one `{R}`: Edgar Markov (rarely cast), Florian, Impact Tremors, Shared Animosity,
Stromkirk Captain. If Florian leaves for Recollector, that's 4.

Three lands produce neither black nor anything the deck is short on: Battlefield
Forge, Sacred Foundry and Sundown Pass, all `{R}`/`{W}`. Sundown Pass is the one
to go:
- It enters tapped early: "This land enters tapped unless you control two or more
  other lands."
- Sacred Foundry is typed **Mountain Plains**. Isolated Chapel checks for Plains,
  and red/white sources aren't the constraint anyway.
- Battlefield Forge always enters untapped.
- The 09-03 land review already named Sundown Pass "the most replaceable of the R/W
  duals". It survived that review only because Clifftop Retreat went instead.

A **basic Swamp** beats a utility land here:
- Dragonskull Summit wants "a Swamp or a Mountain".
- Isolated Chapel wants "a Plains or a Swamp".
- Smoldering Marsh wants "two or more basic lands".

A basic turns on all three. Castle Locthwain was considered and stays rejected for
the 09-03 reason: draw is the deck's deepest support category.

After the swap: B 25 → 26 (unconditional ~21 → 22), W 17 → 16, R 13 → 12. White is
still fine: 16 of its 17 cards need exactly one `{W}`, and Clever Concealment
`{2}{W}{W}` has convoke. No combo change (a basic land).

Price: Swamp has no listed price. Sundown Pass $2.73 (07:28 UTC). The swap doesn't
depend on price.

## ADD IF you're stalling on lands: Fell the Profane over Oubliette

If games show you missing drops more than the ~9% the simulation predicts, don't
cut a spell for a 35th land. Turn a spell into a land-that's-also-a-spell instead:

- **Fell the Profane // Fell Mire** `{2}{B}{B}` instant: "Destroy target creature or
  planeswalker."
- Land side: "As this land enters, you may pay 3 life. If you don't, it enters
  tapped." `{T}`: Add `{B}`.
- **Cut: Oubliette** `{1}{B}{B}`, an enchantment: "target creature phases out until
  this enchantment leaves the battlefield".
- The swap keeps the role (single-target creature removal), adds planeswalkers and
  instant speed, and the answer can't be undone by removing the enchantment. The cost
  is one more MV (3 → 4).
- In practice it is a 35th black source that's never a dead land draw.

Facts:
- $5.33 (07:26 UTC).
- EDHREC rank 198; it shows in no Edgar top list I pulled.
- `combos.py --add --near`: 0 new, 0 near.

It is conditional because, by the numbers above, the deck isn't short on lands. Take
it if what you see at the table says otherwise.

Considered and not taken: **Hagra Mauling** ($1.10; its land side always enters
tapped). **Agadeem's Awakening** ($27.60; it would be the deck's recursion, but its
`{X}{B}{B}{B}` makes the black problem worse). **Emeria's Call** ($4.42; a 7-mana
`{W}{W}{W}` spell). **Witch Enchanter** ($5.89; artifact/enchantment removal isn't
the hole). **Urborg** ($53.68): still the best black fix there is, and still over
the $40 cap. The 09-03 ADD IF stands unchanged.

## Unsure / would settle it

- How often you're actually stuck on 2–3 lands, versus stuck on colour (holding
  Necropotence or Grave Pact with the wrong lands out). This review thinks it's colour.
  If it's count, take the Fell the Profane swap.

`base.txt` not modified.
