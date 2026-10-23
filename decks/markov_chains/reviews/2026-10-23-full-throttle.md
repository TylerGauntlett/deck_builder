# markov_chains — Full Throttle (2026-10-23)

**Verdict: NO.** It is a second alpha-strike finisher, alongside Akroma's Will, in a
deck that already closes once it has a board. It only works while you're ahead, and it
costs `{4}{R}{R}` in a deck with 4 red-pip cards.

Deck state: `base.txt` synced on 2026-10-23 from the list you supplied. Bloodline
Recollector, Authority of the Consuls and an 8th Swamp in; Florian, Malakir Bloodwitch
(to sideboard) and Sundown Pass out. 100 cards, 34 lands, average non-land MV 2.86,
pips B 63 / W 19 / R 4. Bracket 3, $40/card cap, Game Changers 2/3.

## The card (Scryfall, fetched 2026-10-23 11:26 UTC)

> **Full Throttle** `{4}{R}{R}` — Sorcery
> After this main phase, there are two additional combat phases.
> At the beginning of each combat this turn, untap all creatures that attacked this turn.

Colour identity R · Commander legal · not a Game Changer · EDHREC rank 1,320.

Rulings that matter:
- There is no main phase between the extra combats. Cast it in main phase 1 and you
  get three combats. Cast it in main phase 2 and you get two, then go straight to the
  end step.
- It only untaps creatures **that attacked this turn**. Anything that didn't attack in
  the first combat (summoning-sick tokens, for example) gains nothing.

## Honest best case

Three combats multiply every attack trigger in the deck by three, and the deck runs
seven cards whose text says "attack" (verified scan of `cards.json`):

| Card | Clause | ×3 combats |
|---|---|---|
| Sanctum Seeker | *"Whenever a Vampire you control attacks, each opponent loses 1 life"* | 3 drain per attacking Vampire. Doubled by Bloodletter of Aclazotz (*"during your turn"*) |
| Edgar Markov | *"Whenever Edgar attacks, put a +1/+1 counter on each Vampire you control"* | +3 to the team, **only if Edgar is on the battlefield** |
| Clavileño | *"Whenever you attack"* → a Demon that draws and leaves a 4/3 on death | 3 triggers |
| Carmen | *"Whenever Carmen attacks, return up to one target permanent card …"* | 3 recursions |
| High-Society Hunter | attack: sacrifice another creature for a counter | 3 sacrifices |
| Shared Animosity | +1/+0 per other attacker sharing a type | applies each combat |
| Ghostly Prison | (defensive; not an attack trigger) | — |

Lifelink granted by Vito's `{3}{B}{B}` activation or Vault of the Archangel lasts
*"until end of turn"*, so it covers all three combats. Every combat-damage step then
feeds Vito and Marauding Blight-Priest. That is a real bridge to the drain plan.

So the case is: *"With Sanctum Seeker and five attacking Vampires, Full Throttle is 15
drain to each opponent before combat damage, 30 with Bloodletter."* That is true, and it
is the best the card does.

## The tests

**Redundancy — effect × frequency × duration.** The deck already has a one-turn
alpha-strike finisher: **Akroma's Will** `{3}{W}`, an instant. *"Creatures you control
gain flying, vigilance, and double strike"*, and with a commander out, also *"lifelink,
indestructible, and protection from each color."* Both are once per game, for one
turn. Akroma's Will is two mana cheaper, works at instant speed, and gives the
**evasion** that Full Throttle lacks. Full Throttle untaps your attackers, but blocking
doesn't tap the opponents' creatures, so the same blockers are waiting in every combat.
Full Throttle wins on attack triggers (×3 against Akroma's ×1). Akroma's Will wins on
damage getting through. Behind those two, the deck closes through the drain loops
(Vito/Blight-Priest + Bloodthirsty Conqueror), Vein Ripper, Impact Tremors and Mirkwood
Bats. The finisher role is not thin.

**Density.** The big multiplier, Edgar's +1/+1 per attack, needs the 6-mana commander
on the battlefield. For most of a game Edgar sits in the command zone, using eminence.
Without Edgar, the triggers that scale are Sanctum Seeker alone and the one-per-combat
cards (Clavileño, Carmen, Hunter). Seeker is one card, and Full Throttle is a Seeker
amplifier more than a deck amplifier.

**Marginal impact — does it change games you lose?** No. It needs a board that has
already survived to your turn, plus 6 spare mana. On a turn where you have both, the
deck is already winning: Akroma's Will, Sanctum Seeker or the drain loops would close
it. When you're behind, after a wipe or against a board of blockers, it's a 6-mana
sorcery that does nothing. Worst-case draw: in your opening hand it's dead until turn 6
or later, and on an empty board on turn 12 it's blank.

**Cost of entry.** MV 6 joins Vein Ripper and Patron of the Vein as the deck's most
expensive non-land cards (Edgar aside). `{R}{R}` against 11 red-producing lands plus
Arcane Signet and two Talismans. Voldaren Estate doesn't count because its coloured mana
is Vampire-only, and Exotic Orchard depends on what your opponents play. The deck has
been cutting red: red pips dropped from 5 to 4 with Florian's exit today. This would be
the deck's first double-red card.

**Anti-synergy.** It's not a Vampire, so no eminence token. Charismatic Conqueror has
vigilance anyway. No nonbo found beyond the missing evasion.

**Bracket fit.** Not a Game Changer. `combos.py --add` finds 0 new and 0 near combos.
House rules untouched.

**Disagreement check.** EDHREC lists no Edgar Markov figure on the card's page. Its top
homes are extra-combat commanders: Lightning, Army of One 41.8%; Rootha 59.0%; Kaalia
5.2%. It doesn't appear on the Edgar commander page's sorcery list either, where the
lowest listed is 6.8%. The community and I agree. My independent reason is the
redundancy with Akroma's Will and the Edgar-on-battlefield dependency.

## On the speed premise

"Only works when you're ahead" is a verdict about the deck's clock. The last recorded
answer (2026-08-30) is that games run long. If they do, the case against Full Throttle
gets **stronger**, not weaker: long games mean more wipes and more defended boards.
That is exactly where a 6-mana sorcery with no evasion fails. The NO doesn't depend on
the premise.

## What would change it

The deck repeatedly reaching a wide, surviving board with Edgar on the battlefield and
Sanctum Seeker out, and still failing to close. That would be evidence the closing role
is thin. Even then, the first comparison would be against Akroma's Will, not an add.

## Price

$5.35 (foil $6.11), fetched 2026-10-23 11:26 UTC. Under the $40 cap. The NO survives
the card being free.

## Sources
- `card_facts.py lookup "Full Throttle" --deck markov_chains --rulings`, 2026-10-23 11:26 UTC.
- `edhrec.py card "Full Throttle"` (top commanders as above).
- `combos.py markov_chains --add "Full Throttle" --near`: baseline 2 assembled; 0 new, 0 near.
- Deck counts from `decks/markov_chains/cards.json` rebuilt 2026-10-23 after the sync.

`base.txt` was not modified by this review.
