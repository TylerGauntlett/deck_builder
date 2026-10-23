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

---

## Revision 1: Gleam on Edgar Markov (your pushback, same day)

**Verdict moves: NO → ADD IF Edgar is regularly cast and attacking in your games.**
I haven't named a cut, which is still open (below).

You measured Gleam on an axis I didn't evaluate: **commander damage with Edgar as the
host**. That holds, and it knocks out my main objection.

**One correction to the claim.** Edgar's text (Scryfall, 2026-10-23 15:13 UTC) is
*"Whenever Edgar attacks, put a +1/+1 counter on each **Vampire** you control"*. Those
are permanent counters on Vampires, not 1/1s on every creature. Nearly everything the
deck makes is a Vampire (every eminence token is), so the count is close to what you
meant.

**The maths.** Edgar is a 4/4 with first strike and haste. Gleam counts counters on
*other* creatures, and the attack trigger resolves before blocks. With N other
Vampires on the board:
- Swing 1: Edgar is 4 + 1 (his own counter) + N. With N = 5 that's **10**.
- Swing 2: the counters from swing 1 are still there, so he's 4 + 2 + 2N = **16**.
  Two connected swings at one player add up to 26, past the 21 commander damage needed.
- Every death with Cordial Vampire out, and every Indulgent Aristocrat or Patron of
  the Vein activation, adds another +N to Edgar on top.
- With **Akroma's Will** (*"flying, vigilance, and double strike"*), N = 6 gives an
  11-power double striker: 22 commander damage to one player in a single swing.

**What I got wrong.** I wrote that Gleam "stacks the whole board's value onto one
creature." It doesn't. The counters stay spread across the board, and Gleam adds a
*copy* of that total onto one body. If the host dies, you lose a 2-mana Aura and
nothing else. The 2-for-1 objection was overstated.

**What still holds:**
- **It depends on Edgar being on the battlefield.** He's a 6-drop, plus 2 more each
  time he's recast. My Full Throttle review said Edgar mostly sits in the command
  zone, but that was my assumption, not anything from your games. It's the one
  question that decides this card.
- **Chump blocks.** Edgar has no evasion of his own. One 1/1 blocks a 16-power
  first striker. The deck has two ways to give him evasion: Akroma's Will (one turn)
  and **Qarsi Revenant**'s Renew (*"a flying counter, a deathtouch counter, and a
  lifelink counter on target creature"*, permanent, from the graveyard). Edgar,
  Ancient Bloodlord's menace applies only to himself.
- **When Edgar isn't out**, it's the earlier analysis: decent on Elenda, otherwise
  mediocre.

**No reason I gave earlier is reversed.** The Elenda interaction still stands. The
eminence point (no token, because Gleam isn't a Vampire) is still a tiebreaker only.

## The cut: still open

The amplifier-tier cuts from earlier reviews have already been used or were spared
for reasons that still hold:
- **Bloodthrone Vampire**: spared on 2026-10-09 as one of three free, unlimited sac
  outlets that switch on Bloodline Recollector.
- **Forerunner of the Legion**: spared as the deck's only tutor.
- **Malakir Bloodwitch**: spared on 2026-10-09 against Vito.

I'm not going to drop those reasons to make room. If Gleam goes in, the cut needs a fresh
look at the 2-drop and amplifier slots.

## Price

$0.37 (foil $0.57), fetched 2026-10-23 15:11 UTC. Not a factor.
