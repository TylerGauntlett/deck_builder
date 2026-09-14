# Pillowfort / deterrence — markov_chains

**Date:** 2026-09-14
**Deck:** markov_chains — Edgar Markov, Commander, bracket 3, $40/card cap
**Supersedes the deterrence portion of** `2026-09-14-no-mercy.md`

**Verdicts:**
- **No Mercy — NO** (re-run on the deterrence axis; reason corrected)
- **Ghostly Prison — ADD**, cutting Anowon, the Ruin Sage
- **Revenge of Ravens — ADD IF** you want the deterrent to also close games

---

## What changed

The user re-framed No Mercy as *"a black alternative to something like Propaganda —
in a pod it makes it so I can't be the target, as I am often targeted due to having
a villain deck."*

That is a **new axis** plus the **pod fact** the first review explicitly asked for.
Both are re-run triggers, so this is a fresh analysis, not a restatement.

### Concession — the first review made a reasoning error

I wrote that No Mercy fails because "the rational play is simply to attack someone
else — at which point No Mercy is a blank." On a deterrence axis that is backwards.
A pillowfort card whose opponents all attack elsewhere is not failing; **that is the
card doing its job.** I scored it as a removal engine and as a combat trick, and
never scored it as a tax. That was my error and the pushback was correct.

Re-running it on the right axis, though, does not save the card — for a reason the
first review never reached.

## The factual correction that decides it

`card_facts.py lookup "Propaganda" "Ghostly Prison" "No Mercy" --deck markov_chains`
(prices fetched 2026-09-14 17:18 UTC):

| Card | Cost | Oracle text |
|---|---|---|
| Propaganda | `{2}{U}` | "Creatures **can't attack you unless** their controller pays {2} for each creature they control that's attacking you." |
| Ghostly Prison | `{2}{W}` | "Creatures **can't attack you unless** their controller pays {2} for each creature they control that's attacking you." |
| No Mercy | `{2}{B}{B}` | "Whenever a creature **deals damage to you**, destroy it." |

**No Mercy is not a Propaganda effect.** Propaganda operates at declare-attackers
and prevents the attack; you take zero damage. No Mercy lets the attack happen,
lets the damage resolve in full, and *then* destroys the creature. It does not
prevent a single point of damage, ever.

For the stated goal — "I can't be the target" — that gap is the whole question.
No Mercy does not stop you being the target; it charges a toll after you have
already paid in life. Specifically it fails at:

- **Expendable attackers.** Tokens, recursive creatures (Bloodghast-likes), anything
  whose ETB value is already banked. They swing, you take it, they shrug.
- **The alpha strike.** Three players swinging lethal: No Mercy destroys all of it,
  after you are dead.
- **Being "targeted" in the sense you probably mean.** Removal aimed at Edgar, board
  wipes, counterspells, being ganged up on politically — No Mercy answers none of it.

`{2}{B}{B}` is also a full mana more than Propaganda, and $26.54 against $2.85.

**And you don't need a black alternative at all.** Propaganda is blue —
`card_facts.py` flags it outright: *"ILLEGAL IN THIS DECK: U is outside BRW."* But
Edgar Markov is **Mardu**, and white is the best pillowfort colour in Magic.
**Ghostly Prison is a word-for-word functional reprint of Propaganda in white.**
The premise of the question — that a black substitute is required — is the thing to
drop.

For completeness, the literal black Propaganda does exist and is worse:
**Koskun Falls** `{2}{B}{B}`, World Enchantment, "At the beginning of your upkeep,
sacrifice this enchantment unless you tap an untapped creature you control," plus
the Propaganda text. Reserved List, $18.27, EDHREC rank 10654. It taxes your board
every upkeep and dies to another World Enchantment. Ghostly Prison beats it on every
axis.

## The options, verified

`card_facts.py search 'id<=rwb o:"attack you unless" -t:land f:commander'` → 5 hits;
plus attack-count caps and attack-punishers. The live candidates:

| Card | Cost | Effect | Price |
|---|---|---|---|
| **Ghostly Prison** | `{2}{W}` | Propaganda, verbatim | $6.25 |
| **Windborn Muse** | `{3}{W}` | Ghostly Prison on a 2/3 flier | $0.78 |
| **Norn's Annex** | `{3}{W/P}{W/P}` | Tax is {W} **or 2 life** — harder to pay through | $5.35 |
| **Crawlspace** | `{3}` | "No more than two creatures can attack you each combat" — a hard cap, unpayable | $9.91 |
| **Dáin, Lord of the Iron Hills** | `{1}{W}` | {1} tax per creature, only while you have an enduring story | $0.23 |
| **Revenge of Ravens** | `{3}{B}` | Attackers' controller loses 1, **you gain 1**, per creature | $0.58 |
| **Marchesa's Decree** | `{3}{B}` | Monarch + attackers lose 1 (no lifegain) | $4.01 |
| **Koskun Falls** | `{2}{B}{B}` | Propaganda + upkeep creature tap, World | $18.27 |

## Recommendation: Ghostly Prison

It is the card you were reaching for. It is 3 mana instead of 4, $6.25 instead of
$26.54, it is in your colours, and — unlike No Mercy — it actually prevents the
damage. It is also **one-sided in exactly the way an archenemy aggro deck wants**:
they can't profitably attack you, you keep attacking them. Nothing about it slows
your own clock.

Ranked runners-up: **Crawlspace** if your pod's threat is go-wide swarms or
mana-rich decks that shrug off a {2} tax (a hard cap can't be paid through);
**Norn's Annex** if they have mana to burn but not life to spare.

### The cut: Anowon, the Ruin Sage

`{3}{B}{B}`, 4/3, "At the beginning of your upkeep, each player sacrifices a
non-Vampire creature **of their choice**." EDHREC rank 5169.

Three reasons, all verified:

1. **"Of their choice" hands the decision to the opponent** — the exact flaw I'm
   rejecting No Mercy for, so cutting it keeps this review consistent with itself.
   Against any deck making tokens, they sacrifice a 1/1 every upkeep and it does
   nothing.
2. **It eats your own cards.** The deck's non-Vampire creatures are
   **Carrion Feeder** (a free sac outlet), **Zulaport Cutthroat** (a core drain
   payoff) and **Mirkwood Bats**. Anowon is a repeating tax on three of your better
   pieces.
3. **It is a 5-drop on a 2.92 average curve**, and Ghostly Prison at 3 improves the
   curve while replacing it.

Runners-up I chose not to cut: Vampire Nocturnus (rank 8921) and Bloodthrone Vampire
(rank 8643) are rarer in registered lists, but Nocturnus is a genuine anthem on 66
black pips and Bloodthrone is a free sac outlet — low play rate is not low value.
High-Society Hunter and Baron Bertram both draw cards. Anowon is the only card in
that tier whose effect an opponent gets to blank.

## Revenge of Ravens — ADD IF

`{3}{B}`, $0.58: *"Whenever a creature attacks you or a planeswalker you control,
that creature's controller loses 1 life and you gain 1 life."*

Weaker deterrence than Ghostly Prison — it doesn't stop the damage either — but it
is the only card here that is **on-plan**, because the lifegain is a bridge into the
deck's drain half. Three verified payoffs:

- **Vito, Thorn of the Dusk Rose** — "Whenever you gain life, target opponent loses
  that much life."
- **Marauding Blight-Priest** — "Whenever you gain life, **each opponent** loses 1
  life."
- **Sanctum Seeker** / the lifelink suite already turn incidental gain into reach.

One creature attacking you with Vito and Blight-Priest out: they lose 1 (Revenge),
you gain 1 → Vito drains 1 more, Blight-Priest drains 1 from *each* of three
opponents. That is 5 life of swing off one attacker, and a four-creature swing is
catastrophic for the attacker. It converts "I get attacked" from a problem into a
win condition.

**Condition:** add it if what you want is for attacking you to be *bad for them*
rather than *impossible*. If you want the damage stopped, Ghostly Prison is the card.
If you end up running both, the second cut is High-Society Hunter (5 MV, rank 4426).

## Price

All fetched 2026-09-14 17:18 UTC: No Mercy $26.54 · Ghostly Prison $6.25 ·
Revenge of Ravens $0.58 · Crawlspace $9.91 · Norn's Annex $5.35 · Koskun Falls
$18.27 · Windborn Muse $0.78. All inside the $40 cap; price decides none of this.
**The No Mercy rejection survives the card being free** — it would still not prevent
damage, which is the job.

## Still open

"Targeted" is doing a lot of work in the original framing. If the pod points
*removal and wipes* at you rather than creatures, none of these cards help, and the
answer is protection (you already run Teferi's Protection, Clever Concealment,
Akroma's Will) or a faster clock. Worth knowing which it is before the Ghostly
Prison slot gets spent.

---

*Facts: Scryfall via `card_facts.py` (prices fetched 2026-09-14 17:18 UTC), deck
contents counted from `cards.json`. `base.txt` not modified.*
