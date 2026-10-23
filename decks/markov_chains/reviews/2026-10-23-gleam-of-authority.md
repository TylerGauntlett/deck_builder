# markov_chains — Gleam of Authority (2026-10-23)

**Verdict: NO.** It turns the deck's spread-out +1/+1 counters into one big creature
with no evasion and no drain. The deck spreads counters so that its board can't be
answered one creature at a time, and an Aura stacks everything back onto one removal
target. It's also a non-Vampire, so it makes no eminence token.

Deck state: `base.txt` as synced 2026-10-23 (see `2026-10-23-full-throttle.md`). Bracket 3,
$40/card cap.

## The card (Scryfall, fetched 2026-10-23 15:11 UTC)

> **Gleam of Authority** `{1}{W}` — Enchantment — Aura
> Enchant creature
> Enchanted creature gets +1/+1 for each +1/+1 counter on other creatures you control.
> Enchanted creature has vigilance and "{W}, {T}: Bolster 1."

Colour identity W · Commander legal · not a Game Changer · EDHREC rank 17,423.
Ruling: bolster doesn't target. It picks your creature with the least toughness on resolution.

## What feeds it (verified scan of `cards.json`)

It counts **counters on other creatures you control**, so I've grouped the deck's
counter sources by how many creatures each one hits:

**Mass, "each Vampire you control" (4).** This is where Gleam scales.
- Cordial Vampire: *"Whenever this creature or another creature dies"* (any creature)
- Edgar Markov: *"Whenever Edgar attacks"*. Only works with Edgar on the battlefield, not in the command zone.
- Indulgent Aristocrat: *"{2}, Sacrifice a creature"*
- Patron of the Vein: *"Whenever a creature an opponent controls dies"*

**Single creature (7).** Each one adds +1 to Gleam per counter, and only when Gleam is on a different creature.
- Blade of the Bloodchief (equipped creature), Carmen, Carrion Feeder,
  Edgar Ancient Bloodlord, Elenda, High-Society Hunter (all self-only)
- Sorin, Imperious Bloodlord +1 (one target Vampire)

## Honest best case

The deck turns deaths into +1/+1 counters, and Gleam turns those counters into a single
threat. With Cordial Vampire out and eight Vampires on board, every death adds
about +7/+7 to the enchanted creature. The best home is **Elenda, the Dusk Rose**. She
has lifelink, so the Gleam bonus becomes life gain. Her death trigger uses
*"Elenda's power as it last existed on the battlefield"* (official ruling), so Gleam's
bonus also becomes extra lifelink Vampire tokens when she dies. Bolster is a mana sink
on a vigilant attacker. Three verified interactions: Cordial Vampire, Indulgent
Aristocrat, Elenda. The synergy is real.

## The tests

**It reverses the deck's design.** Every mass counter source above puts counters on
*each* Vampire. That spreading is the point: a wide, pumped board survives spot
removal. Gleam stacks the whole board's value onto one creature. One Swords to
Plowshares, a bounce spell or a chump block then answers it, and you lose the Aura
as well (a 2-for-1).

**Anti-synergy with sacrifice.** This deck sacrifices its own creatures constantly
(Viscera Seer, Carrion Feeder, Phyrexian Tower, Indulgent Aristocrat, Bloodthrone
Vampire, Village Rites, High-Society Hunter's attack trigger). The Aura limits which
creature you're willing to sacrifice. If you need to sacrifice the enchanted creature
in response to removal, the Aura goes with it.

**No evasion, no drain.** The bonus is just power and toughness on one creature. It
doesn't reach Sanctum Seeker, Blood Artist, Impact Tremors or Vein Ripper, which are
how the deck actually closes. On Elenda it's lifegain, not damage to opponents.

**Density.** Only 4 cards in the 99 spread counters, and one of them (Edgar's attack
trigger) needs the 6-mana commander on the battlefield. That's well under a third of
the deck. Without one of the four, Gleam is +1 to +3 from the single-creature sources,
which is a 2-mana Aura doing roughly what Stromkirk Captain or a lord already does
across the whole team.

**Marginal impact / worst case.** In an opening hand it's a 2-mana Aura that needs a
creature and counters before it does anything. On turn 12 with an empty board it's
blank. After a wipe it's gone with the creature. It's strongest on a board that's
already winning, and long games (the last recorded speed answer, 2026-08-30) mean more
removal and wipes, which makes an Aura worse. **The NO doesn't depend on the speed
premise.**

**Eminence.** It isn't a Vampire, so casting it makes no Edgar token. That's the
deck's preference tiebreaker only, not the reason for the NO.

**Bracket / combos.** Not a Game Changer. `combos.py --add`: baseline 2 assembled,
0 new, 0 near. House rules untouched.

**Disagreement check.** EDHREC has no Edgar Markov entry for the card. Its homes are
+1/+1-counter commanders that put counters on everything: Mikaeus, the Lunarch 16.1%
(91/565), Anafenza, Kin-Tree Spirit 16.3% (72/442), Dromoka, the Eternal 8.2%
(46/559), Optimus Prime 4.1%. Low inclusion even there. The community and I agree. My
independent reason is the concentration-versus-spread problem above.

## Counter-proposal

None. The role it would fill, turning counters into a finisher, isn't a gap. The deck
already closes through Akroma's Will, Shared Animosity, Sanctum Seeker and the drain
loops.

## What would change it

A deck that ran several lasting hexproof or protection pieces to keep one creature on
the battlefield, or a move toward a Voltron plan around a single creature. Today the
deck's only protection is one-shot: Akroma's Will (until end of turn) and Teferi's
Protection (until your next turn). Neither matches the stated plan.

## Price

$0.37 (foil $0.57), fetched 2026-10-23 15:11 UTC. Under the $40 cap. The NO survives
the card being free.

## Sources
- `card_facts.py lookup "Gleam of Authority" --deck markov_chains --rulings`, 2026-10-23 15:11 UTC.
- `card_facts.py lookup "Elenda, the Dusk Rose" --rulings` (last-known-power ruling).
- `edhrec.py card "Gleam of Authority" --deck markov_chains` (figures above).
- `combos.py markov_chains --add "Gleam of Authority" --near`: 0 new, 0 near.
- Counter-source grouping from `decks/markov_chains/cards.json`.

`base.txt` was not modified by this review.
