# markov_chains — card review, 2026-09-04

Question asked: *"what are ways I can protect something like Grave Pact from being
destroyed?"* — an open role question, no card proposed. So this works the
counter-propose direction: define the threat, enumerate the in-identity answers,
and only then decide whether any of them beats a card already in the 99.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 ·
$40/card cap · 4-player casual pods. Vetoes: no early infinite combos, no
tutor-dependent win line. Preference: on-theme Vampires, tiebreaker only.

Pod facts carried forward from the 2026-08-30 / 08-31 reviews and not re-litigated
here: games run **long**; several opponents play **mono-white** (token swarm and
big-creature builds); **Farewell and Armageddon are commonly played**.

All oracle text, colour identity, legality and prices fetched from Scryfall
2026-09-04 02:03–02:08 UTC. EDHREC from `commanders/edgar-markov`, n = 50,203.
Combo checks via `combos.py --add`.

**Verdict: NO to the dedicated enchantment-protection package. One ADD IF
(Alseid of Life's Bounty). The two best answers are already in the deck.**

---

## 1. Split the threat before shopping for answers

"Destroyed" is three different problems and they take different cards. Grave Pact
({1}{B}{B}{B}, Enchantment, "Whenever a creature you control dies, each other
player sacrifices a creature of their choice") can leave the battlefield by:

| Threat | Example in this pod | Beaten by |
|---|---|---|
| **Targeted removal** | Disenchant, Generous Gift, Anguished Unmaking, Vindicate | shroud / hexproof / protection / counter it / phase out |
| **Mass exile** | **Farewell** — confirmed common here | **phasing only** |
| **Mass destroy** | Merciless Eviction (destroy mode), Austere Command | indestructible, phasing |

Farewell, verified this session: `{4}{W}{W}` Sorcery — *"Choose one or more —
exile all artifacts; exile all creatures; **exile all enchantments**; exile all
graveyards."* It does not target and it exiles. That single line eliminates most
of the category: **shroud, hexproof, protection-from-a-colour, indestructible and
Karmic Justice all do literally nothing against the sweeper this pod actually
casts.**

## 2. The deck already runs both cards that beat Farewell

`card_facts.py search 'id<=rwb (o:"phase out" or o:"gains protection from")
-t:creature -t:land f:commander'` returns 21 cards in the deck's colours. Exactly
two of them phase out a noncreature permanent you control, and the deck runs both:

- **Teferi's Protection** `{2}{W}` — *"All permanents you control phase out."* Not
  targeted, so it also dodges Armageddon (your lands phase out too). Game Changer,
  1 of 3 used. Now **$48.33**, i.e. above the $40 cap — a note for replacement
  cost, not a reason to cut it.
- **Clever Concealment** `{2}{W}{W}` — *"Convoke. Any number of **target** nonland
  permanents you control phase out."* $5.01. In a deck with Edgar's token engine,
  convoke routinely makes this a one- or two-mana spell.

That is the correct answer to the question, and it is already in the list. The
remaining candidates are all answers to the *lesser* threat.

## 3. The shroud package is a trap here — three reasons, in order

**Greater Auramancy** `{1}{W}`, **$39.69** — *"Other enchantments you control have
**shroud**. Enchanted creatures you control have shroud."* **NO.**

1. **It does nothing against Farewell.** See §1.
2. **It only has four legal beneficiaries.** From `cards.json`, the deck's entire
   enchantment count is **5**: Bastion of Remembrance, Black Market Connections,
   Grave Pact, Impact Tremors, Oubliette. "*Other* enchantments" excludes
   Auramancy itself, which is then the removal magnet.
3. **It actively turns off Clever Concealment.** Shroud is not hexproof — it stops
   *you* targeting too, and Clever Concealment reads *"any number of **target**
   nonland permanents you control."* Greater Auramancy would make Grave Pact,
   Bastion, BMC and Impact Tremors **illegal targets for your own best protection
   spell**. It is anti-synergy with the card that answers the threat it can't.

Price is a separate line and does not carry the verdict: at $39.69 it also eats
essentially the whole per-card cap. The rejection survives the card being free.

**Fountain Watch** `{3}{W}{W}` 2/4, $2.32 — *"Artifacts and enchantments you
control have **shroud**."* **NO.** Same reason 1 and same reason 3, on a five-mana
2/4 body with EDHREC rank 15,394.

## 4. The rest of the category, each with the one line that kills it

| Card | Price (02:04–02:07 UTC) | Verdict |
|---|---|---|
| **Karmic Justice** `{2}{W}` | $1.77 | **NO** — it is revenge, not protection: Grave Pact still dies. And its trigger reads *"a spell or ability an opponent controls **destroys** a noncreature permanent you control"* — **exile is not destruction**, so it does not even fire on Farewell, Merciless Eviction's exile mode, or Anguished Unmaking. |
| **Rebuff the Wicked** `{W}` | $7.45 | **NO** — *"Counter target **spell** that targets a permanent you control."* Misses activated and triggered abilities entirely, misses every sweeper, and asks a deck with 14 white sources in 35 lands to hold {W} up on other players' turns. A dead card in most games. |
| **Grand Abolisher** `{W}{W}` | $17.75 | **NO** — *"**During your turn**, your opponents can't cast spells or activate abilities…"* Removal arrives on their turn. Wrong window for this job. |
| **Hall of Heliod's Generosity** | $11.73 | **NO** — rebuy, not protection, and Farewell **exiles**, so there is nothing in the graveyard to rebuy. It is also a colourless-producing land in a deck with BBB and WW costs, at 35 lands. |
| **Sun Titan** `{4}{W}{W}` | $0.33 | **NO** — returns permanents of **mana value 3 or less**. Grave Pact is MV 4. Out of range. |
| **Boromir, Warden of the Tower** `{2}{W}` | $6.83 | **NO** — its counter clause only hits spells cast for no mana, and its sac ability gives **creatures** indestructible. Grave Pact is not covered by either half. |
| **Avacyn, Angel of Hope** `{5}{W}{W}{W}` | $29.08 | **NO** — eight mana in a 2.88-MV deck, and indestructible loses to exile anyway. |
| **Avacyn's Memorial** `{5}{W}{W}{W}` | $7.67 | **NO** — *"Other **legendary** permanents you control have indestructible."* Grave Pact is not legendary. |
| **Deflecting Swat** `{2}{R}` | **$71.36** | **NO** — over the $40 cap. Also wants a commander on the battlefield, and Edgar spends most of the game in the command zone using eminence. |
| **Apostle's Blessing** `{1}{W/P}` | $0.33 | **NO** — *"Target **artifact or creature** you control."* Cannot target an enchantment. |
| **Sterling Grove** / **Privileged Position** | — | **ILLEGAL** — both GW; G is outside Edgar's BRW identity. `card_facts.py --deck` flags them outright. |

## 5. The one candidate that survives — ADD IF

**Alseid of Life's Bounty** `{W}` — Enchantment Creature — Nymph, 1/1, lifelink.
*"{1}, Sacrifice this creature: Target creature **or enchantment** you control
gains protection from the colour of your choice until end of turn."*
**$0.46** (fetched 02:04 UTC). EDHREC rank 2,733.

Steel-man, then the attack.

**For it.** It is the only card in the deck's identity, under budget, that
answers targeted removal aimed specifically at an *enchantment* — and the cost of
using it is close to negative, because sacrificing it is itself a payoff. From
`cards.json`, grouped by trigger scope so the count means something:

- Fires on *"a creature dies"* — **any** player's, so Alseid qualifies: Blood
  Artist, Cordial Vampire, Vein Ripper, Blade of the Bloodchief. (4)
- Fires on *"a creature **you control** dies"*: Bastion of Remembrance, Cruel
  Celebrant, Zulaport Cutthroat, **Grave Pact itself**. (4)
- Fires on *"**another** creature dies"*: Elenda, the Dusk Rose. (1)

Nine payoffs fire when you crack it. Its lifelink also feeds Vito, Marauding
Blight-Priest and Bloodthirsty Conqueror. It protects a creature too — Edgar, or
Bloodthirsty Conqueror — so it is not a narrow enchantment-only card.

**Against it.** Protection from a colour does nothing against Farewell (untargeted
*and* exile — protection never stops exile). It is a one-shot. It is a 1/1 that a
mono-white token deck's blockers ignore and any sweeper eats. It is a **Nymph, not
a Vampire**, so it misses Edgar's eminence trigger, Captivating Vampire, Legion
Lieutenant, Stromkirk Captain and Cordial Vampire's anthem — that is a real cost
in this deck, not just a preference miss. And 14 white sources in 35 lands makes a
{W} one-drop an unreliable turn-one play.

**Condition:** ADD IF targeted enchantment removal is actually resolving on Grave
Pact / Black Market Connections / Bastion in these games. If what actually kills
your enchantments is Farewell, Alseid is a blank and this whole review is "you
already own the answer."

## 6. The cut, and why it is the hard part

The 2026-09-03 `fifty-dollar-upgrades` review established that **exactly one
defensible spell cut existed**, and it was spent (Lightning Bolt → Black Market
Connections). Anowon, Qarsi Revenant and Impact Tremors were each spared for a
named reason I am not reversing here.

The least-bad remaining cut is **Bloodthrone Vampire** ({1}{B} 1/1, *"Sacrifice a
creature: This creature gets +2/+2 until end of turn"*, EDHREC rank **8,643** —
second-worst in the deck; $0.14). It is the weakest of the deck's three *free* sac
outlets: Carrion Feeder ({B}, rank 614) puts a permanent +1/+1 counter on itself
and Viscera Seer ({B}) scrys, while Bloodthrone's pump evaporates at end of turn
and is card-negative. It was never spared on its own merits — the 2026-09-01
review only counted it among the six existing outlets while rejecting a seventh.

I am **not confident** this cut is right, and I would rather you keep Bloodthrone
than force the Alseid in. Free sac outlets are load-bearing for Grave Pact: they
are how you convert a board into edicts at instant speed. Three is not many.

## 7. Redundancy is the better-priced version of "protection"

Worth naming even though it is not what was asked. The most reliable way to keep
the Grave Pact *effect* on the table is a second copy, and the deck runs none.

**Dictate of Erebos** `{3}{B}{B}`, **flash**, *"Whenever a creature you control
dies, each opponent sacrifices a creature of their choice"* — $18.68, EDHREC rank
1,014, played in **5.7%** of Edgar Markov decks (2,840/50,203). Flash is the
relevant word: it dodges sorcery-speed interaction, deploys end-of-turn, and can
be cast *after* a wrath resolves. **Butcher of Malakir** ({5}{B}{B}, 7 MV, $0.34)
is the on-theme Vampire version but is two mana worse for the same text.

This is **not an ADD** — same cut problem, and MV 5 in a 2.88-MV deck — but if you
find yourself with a spare slot, Dictate is a better use of it than any card in
§3 or §4.

`combos.py --add` on Alseid, Dictate and Greater Auramancy: **0 new combos** for
each. No constraint pressure.

## 8. What I am unsure about, and what would settle it

1. **Which threat is actually taking your enchantments?** If it is Farewell, buy
   nothing — you own both answers. If it is Disenchant-effects from the mono-white
   decks, Alseid is live. One question: *in the last few games, did Grave Pact die
   to a sweeper or to a spell pointed at it?*
2. **Does Grave Pact even need protecting?** It is at its best *during* a creature
   wrath — your board dying is nine-plus edicts at the table. The permanents that
   actually want the protection may be Black Market Connections and Bastion of
   Remembrance instead. Worth asking before spending a slot.

## Prices and figures used (fetched 2026-09-04 02:03–02:08 UTC)

Grave Pact $32.51 · Teferi's Protection $48.33 · Clever Concealment $5.01 ·
Greater Auramancy $39.69 · Fountain Watch $2.32 · Karmic Justice $1.77 ·
Rebuff the Wicked $7.45 · Grand Abolisher $17.75 · Hall of Heliod's Generosity
$11.73 · Sun Titan $0.33 · Boromir $6.83 · Avacyn, Angel of Hope $29.08 ·
Avacyn's Memorial $7.67 · Deflecting Swat $71.36 · Apostle's Blessing $0.33 ·
Alseid of Life's Bounty $0.46 · Dictate of Erebos $18.68 · Butcher of Malakir
$0.34 · Bloodthrone Vampire $0.14 · Carrion Feeder $4.62 · Farewell $6.07.

EDHREC `commanders/edgar-markov` n = 50,203 (brackets: 1→91 · 2→3,525 · 3→5,343 ·
4→3,983 · 5→170). Deck runs 10/10 high-synergy cards and 9/10 top cards.

`base.txt` was not modified.
