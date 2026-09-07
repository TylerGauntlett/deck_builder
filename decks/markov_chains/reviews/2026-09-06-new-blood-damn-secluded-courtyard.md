# markov_chains — New Blood · Damn · Secluded Courtyard, 2026-09-06

Question asked: *"new blood, damn, Secluded Courtyard"*. Three candidates, modelled as
one batch.

Deck context (`deck_meta.py show`): Edgar Markov · commander · bracket 3 (up to 3 Game
Changers, no early infinites) · $40/card cap · 4-player casual pods. Vetoes: no early
infinite combos, no tutor-dependent win line. Preference: on-theme Vampires, tiebreaker
only.

Pod facts carried forward from the 2026-08-30 → 09-06 reviews (user-stated, not
`meta.json`), not re-litigated here: games run **long**; the three opponents are
**mono-white — 2 fat-creature builds + 1 token swarm**; **Farewell and Armageddon are
commonly played**; the deck is dual-mode (Edgar-on-board aggro / Edgar-absent
aristocrats drain, bridged by the +1/+1 counter package).

All prices fetched **2026-09-07 03:41–03:45 UTC**.

## Verdicts

| Card | Price | Verdict |
|---|---|---|
| New Blood | $0.34 | **ADD** — cut Forerunner of the Legion |
| Damn | $2.22 | **NO** |
| Secluded Courtyard | $0.33 | **NO** (re-affirms 2026-09-03 land review) |

Legality: all three legal in Commander and inside Edgar's B/R/W identity (New Blood B,
Damn BW, Secluded Courtyard colourless). None is a Game Changer. The deck runs exactly
**one** Game Changer (Teferi's Protection), so the bracket-3 allowance of three is not a
constraint on this batch.

## Deck model (counts from `cards.json`, verified)

- 100 cards: **35 lands**, **38 creatures**, 27 other nonland.
- Of the 38 creatures, **35 are Vampires**. The three that are not: Carrion Feeder
  (Zombie), Mirkwood Bats (Bat), Zulaport Cutthroat (Human Rogue Ally).
- Coloured land sources (unrestricted): **B 26, W 16, R 13**. Voldaren Estate's coloured
  mana is Vampire-spell-only and is excluded from those counts; Path of Ancestry's is
  unrestricted and is included.
- Targeted removal, 6: Swords to Plowshares, Anguished Unmaking, Feed the Swarm,
  Soul Shatter, Oubliette, Patron of the Vein (ETB destroy).
- Mass removal, 2, **both asymmetric by scope**: Olivia's Wrath — *"Each **non-Vampire**
  creature gets -X/-X until end of turn, where X is the number of Vampires you
  control"*; Anowon, the Ruin Sage — *"each player sacrifices a **non-Vampire** creature
  of their choice."* With 35 Vampires, neither meaningfully hits this deck's own board.

That last line is the load-bearing fact for two of the three verdicts, so it is quoted
rather than counted.

---

## New Blood — ADD

`{2}{B}{B}` Sorcery. *"As an additional cost to cast this spell, tap an untapped Vampire
you control. Gain control of target creature. Change the text of that creature by
replacing all instances of one creature type with Vampire."* EDHREC rank 4,418 overall;
**35.2% of Edgar Markov decks (17,713/50,363)** — Edgar is its #1 commander. $0.34.

### The case

**1. It is the deck's only unconditional permanent theft.** The deck has exactly one
other theft effect and it is heavily gated: Captivating Vampire's *"Tap five untapped
Vampires you control: Gain control of target creature."* Five untapped Vampires is a
board state, not a card. New Blood is the same effect for four mana and one tap.

**2. Against the verified pod it is a 2-for-1, not removal parity.** Two of three
opponents are fat-creature mono-white builds. Destroying a 6/6 is a one-for-one; taking
it is a twelve-point board swing and leaves you a body that attacks. The deck's existing
answers to a genuinely large creature are thinner than the raw count of six suggests —
Feed the Swarm costs you life equal to its mana value, Olivia's Wrath only gives -X/-X
for X = your Vampire count and often cannot kill a big one, and Soul Shatter lets each
opponent choose.

**3. The text change is mechanical, not flavour.** Verified interactions with named
cards, six of them:

- *Legion Lieutenant* — "Other Vampires you control get +1/+1."
- *Captivating Vampire* — "Other Vampire creatures you control get +1/+1" (and the
  stolen creature then counts toward its own five-Vampire activation).
- *Stromkirk Captain* — "Other Vampire creatures you control get +1/+1 and have first
  strike."
- *Vampire Nocturnus* — "this creature and other Vampire creatures you control get +2/+1
  and have flying" while the top card is black.
- *Sanctum Seeker* — "Whenever a **Vampire you control** attacks, each opponent loses 1
  life and you gain 1 life." Scope checked: yours only, and the stolen creature now
  qualifies.
- *Bloodletter of Aclazotz* — doubles that drain on your turn.

**4. The non-obvious half: it protects the theft from your own deck.** Both of this
deck's sweepers are keyed to *non-Vampire*. Without the text change, a stolen creature is
precisely what Anowon's *"each player sacrifices a non-Vampire creature of their choice"*
would make **you** sacrifice on your own upkeep, and what Olivia's Wrath would shrink.
Turning it into a Vampire is what lets you keep it. This is the argument I would have
missed by reading the card as "Threaten, but permanent."

**5. Summoning sickness does not apply to the additional cost.** Ruling [2017-08-25]:
*"you may tap any untapped Vampire you control, including one you haven't controlled
continuously since the beginning of your most recent turn. (Note that tapping the
creature doesn't use {T}.)"* A Vampire token Edgar's eminence made this turn pays the
cost. The cost is close to free on any developed board.

### The case against, honestly stated

- **It targets.** It answers indestructible (theft is not destruction) but not hexproof,
  ward, or protection from black. Mono-white does play protection effects.
- **Weak against the token-swarm opponent** — one of three. Stealing a 1/1 is not a card.
- **It is not a Vampire spell**, so Edgar's eminence does **not** trigger on casting it.
  This is a genuine cost of the swap and is priced in below.
- Rank 4,418 overall says it is a bad card in the abstract. It is: it is a good card
  *here*, in this pod, which is the only question being asked.

`combos.py --add "New Blood"` — 0 new combos completed, 0 newly within reach. It does not
touch the no-early-infinites veto.

### The cut — Forerunner of the Legion

`{2}{W}` Vampire Knight 2/2. *"When this creature enters, you may search your library for
a Vampire card, reveal it, then shuffle and put that card on top. Whenever another
Vampire you control enters, target creature gets +1/+1 until end of turn."* EDHREC rank
6,037 — the worst-ranked nonland card in the deck, and the 2026-09-06 Drana review already
recorded that it *"has never been spared with a specific reason."* That still holds: the
ETB is selection rather than advantage, and the pump is a single **target**, **until end
of turn**, in a deck whose whole counter package (Edgar's attack trigger, Cordial Vampire,
Patron of the Vein) puts down permanent +1/+1 counters instead.

**Aggregate delta of the swap:** creatures 38 → 37; MV 3 count −1, MV 4 count +1; pips
−W, +BB (26 black sources supports this comfortably). One fewer Vampire spell means one
fewer eminence token over a game — the honest price of the trade. Against the pod on
record, taking an opponent's best creature is worth more than a 2/2 plus a 1/1.

**Cut collision — read this before actioning.** Two other pending reviews draw on the
same shallow pool. The 2026-09-06 Drana/Linvala review names Forerunner as *its* cut
(under an ADD IF that review suggests probably fails), and the 2026-09-06 Necropotence
review cuts Painful Truths. `base.txt` has not changed since 2026-09-03, so neither has
been actioned. If you take Drana and spend Forerunner there, New Blood's cut becomes
**Painful Truths** — and then Necropotence has no cut left.

Past those three the deck has no comfortable cut. Everything below them that looks
cuttable on rank is doing a named job: Bloodthrone Vampire and Master of Dark Rites are
free sacrifice outlets, High-Society Hunter and Baron Bertram Graywater are sac-outlet
plus draw engines that bridge the two modes, and Henrika Domnathi was explicitly spared
in the 09-06 review as a Grave Pact trigger. **That is the finding: the deck can absorb
about three more adds total across all pending reviews, not three per review.**

---

## Damn - NO

`{B}{B}` Sorcery. *"Destroy target creature. A creature destroyed this way can't be
regenerated. Overload {2}{W}{W}."* EDHREC rank 345; 28.9% of Edgar decks. $2.22.

**The steel-man, which is real:** Edgar's eminence works from the command zone, so this
deck rebuilds from a board wipe better than two fat-creature decks do - a symmetric wrath
is asymmetric in your favour. And Damn kills a creature of *any* size, which is the exact
axis where Olivia's Wrath fails. Overloading it behind Clever Concealment (*"Any number
of target nonland permanents you control phase out"*, with convoke) or Teferi's
Protection is a genuinely one-sided sweep.

**Why it still fails:**

1. **The wrath mode wants a board you do not have, and the protection combo wants one you
   would not wrath.** Clever Concealment's convoke is only cheap when you are wide - and
   when you are wide, this deck is winning and does not want a sweeper. The two-card
   one-sided version costs roughly 8 mana in a turn. That is a story, not a plan.
2. **The sweeper slot is filled, and filled better.** Olivia's Wrath is asymmetric on the
   card, with no second card and no protection spell required, and it scales off exactly
   the board this deck builds. Anowon does it again on a loop.
3. **The `{B}{B}` mode is a seventh targeted removal spell** in a category already at six.
   That is improving a category the deck is deep in.
4. **The one thing Damn adds over Olivia's Wrath - killing an arbitrarily large creature -
   is the same gap New Blood fills**, and New Blood fills it while gaining you the
   creature instead of trading one-for-one. Within this batch the two cards compete for
   one job, and Damn loses.

`combos.py --add "Damn"` - 0 new combos. Not a bracket concern; the rejection is purely
that a symmetric wrath is the effect a 38-creature go-wide drain deck least wants, and
its flexible half is redundant.

Price was not part of this reasoning. At $2.22 it is trivially affordable and the answer
would be the same if it were free.

---

## Secluded Courtyard - NO

`{T}: Add {C}.` / *"{T}: Add one mana of any color. Spend this mana only to cast a
creature spell of the chosen type or activate an ability of a creature source of the
chosen type."* EDHREC rank 219; **41.4% of Edgar decks (20,863/50,363)** - the most
popular card in this batch by a wide margin. $0.33.

This was already rejected in the **2026-09-03 land review** and `base.txt` is unchanged
since, so the facts are identical. I re-ran the count anyway, and it moved in two
directions:

**Correction to the prior review, in the card's favour.** That review said the coloured
mana covers *"38 of the 64 nonland cards."* The real figure is **35** - naming Vampire
excludes Carrion Feeder, Mirkwood Bats and Zulaport Cutthroat, which are creatures but
not Vampires. Separately, the prior review's framing understated the card: three of the
deck's four `BBB` cards - Vampire Nocturnus, Bloodletter of Aclazotz, Vein Ripper - **are**
Vampire creature spells, so Courtyard does help cast them, and it helps cast Edgar's
`{3}{R}{W}{B}` from the command zone.

**Why the verdict does not move.** It still cannot help cast **Grave Pact** `{1}{B}{B}{B}`,
**Clever Concealment** `{2}{W}{W}`, Teferi's Protection, Akroma's Will, Swords to
Plowshares, Anguished Unmaking, Soul Shatter, Feed the Swarm, Night's Whisper, Painful
Truths, Village Rites, Dark Ritual or Impact Tremors - 26 of 64 nonland cards get nothing
but `{C}`. The deck already runs **two** restricted/utility lands in this exact space
(Voldaren Estate, whose coloured mana is Vampire-spell-only, and Path of Ancestry, which
enters tapped), and Voldaren Estate is close to a functional duplicate with a late-game
Blood token mode attached. A third makes "hand of lands that cannot cast Grave Pact or
Clever Concealment" materially more likely.

And the cut has to come from the 35 lands. Cutting a basic reduces unrestricted sources;
cutting a dual reduces them more. With B 26 / W 16 / R 13 the base is healthy, and the
strain that exists is on `BBB`-plus-`WW` *noncreature* spells - the half Courtyard does
not touch.

41% inclusion is popularity, not fit: most Edgar lists run more Vampires and fewer
white-pip instants than this one. **NO**, unchanged.

Price was not part of this reasoning; at $0.33 the answer is the same if you already own
it.

---

## Summary

**ADD New Blood over Forerunner of the Legion.** **NO** to Damn and Secluded Courtyard.

Open question worth settling before you action several pending reviews at once: the
cut pool is roughly three cards deep (Forerunner, Painful Truths, and then it gets
painful), while the pending reviews collectively recommend more adds than that. If you
want more than three total, the next conversation should be about which *good* card
leaves, not which weak one.


---

# Revision, 2026-09-06 (same day)

Two changes after user pushback and a deck update. Both verdicts on Damn and
Secluded Courtyard stand unchanged; only New Blood's **cut** moved.

## 1. Forerunner of the Legion is spared - I was wrong

User's argument: *"Forerunner of the Legion offers great flexibility and is the only
effective tutor. this shouldn't be dropped."* Both halves verified, both hold.

**"Only effective tutor" - confirmed.** Scanning the oracle text of all 91 entries for
`search your library` returns exactly one hit: Forerunner of the Legion. Nothing else in
the deck searches. The near misses are all selection, not search: Sorin's `-3` puts a
Vampire **from your hand** onto the battlefield, Herald's Horn and Vampire Nocturnus look
at the top card, Path of Ancestry scries, Viscera Seer scries on sacrifice.

**"Great flexibility" - confirmed, and pod-specific.** With 35 Vampires to choose from,
the ETB finds the answer the board actually calls for. The line that matters most here:
**Malakir Bloodwitch** has *"Flying, protection from white"* and *"each opponent loses
life equal to the number of Vampires you control."* All three opponents are mono-white.
Forerunner can go get a creature that, against this specific table, cannot be blocked or
targeted by anything they play.

**Where my reasoning failed.** I evaluated the pump trigger (*"target creature gets +1/+1
until end of turn"*), correctly found it weak, and dismissed the ETB as "selection rather
than advantage" without asking what it selects *for* in this pod. The pump was never the
point. I also inherited the 09-06 Drana review's line that Forerunner *"has never been
spared with a specific reason"* and treated absence of a recorded reason as absence of a
reason. The reason existed; nobody had written it down. It is written down now.

## 2. Deck updated

Per user: **Necropotence was added, Drana was not.** Applied to `base.txt`:

- `-1 Painful Truths`, `+1 Necropotence` (the cut the 2026-09-06 Necropotence review
  named). Forerunner stays, since Drana was not taken.
- Verified after rebuild: 100 cards, 91 distinct. Game Changers 1 -> **2**
  (Necropotence, Teferi's Protection) - still inside bracket 3's allowance of three.
- `build_card_details.py` re-run; `cards.md` and `cards.json` regenerated.

## 3. New Blood's cut is now Oubliette

The two cards this review's cut pool was resting on are both gone: Forerunner is spared
above, and Painful Truths was spent on Necropotence. This is exactly the squeeze the
original review predicted, arriving one day early.

**Cut: Oubliette** `{1}{B}{B}` - *"When this enchantment enters, target creature phases
out until this enchantment leaves the battlefield."*

1. **Same-role swap, so nothing else moves.** New Blood and Oubliette are both
   "answer one large creature." Answers-to-a-creature stays at 6. Creature count stays
   38. **Black pips stay flat** (both cards are two black pips). Only MV moves: MV 3
   count -1, MV 4 count +1. Enchantments 6 -> 5.
2. **It is the only removal in the deck that can be undone.** Oubliette does not destroy
   or exile - the creature is phased out *"until this enchantment leaves the
   battlefield."* Kill the enchantment and the creature comes back. The pod is verified
   to play **Farewell** commonly, and mono-white is the colour with the most enchantment
   removal in the format. Every other answer in the suite is permanent once it resolves.
3. **New Blood covers the same job in a form this pod cannot undo**, and gains the body
   rather than trading one-for-one.
4. **It does not touch enchantment coverage.** Verified: the deck has exactly **two**
   cards that can answer an enchantment - Anguished Unmaking and Feed the Swarm. Cutting
   Oubliette leaves both.

**Runner-up: Feed the Swarm** `{1}{B}` - and the case for flipping these two is real, so
here it is. *"You lose life equal to that permanent's mana value"* got materially worse
the moment Necropotence entered the deck: life is now the deck's card-draw currency, and
Feed the Swarm's cost peaks exactly against the fat-creature opponents it is aimed at -
killing a seven-drop costs seven cards' worth of Necropotence activations. Oubliette
costs no life at all, which makes it the piece that got *relatively better* from the
Necropotence add.

I still cut Oubliette first, because cutting Feed the Swarm drops enchantment answers
from two to one and leaves Anguished Unmaking as the only one - which also costs 3 life.
But if your table's mono-white decks lean on creatures rather than enchantments, flipping
these is defensible and I would not argue hard against it.

## Net position after this revision

- **New Blood IN, Oubliette OUT.**
- Forerunner of the Legion: **stays**, now with a recorded sparing reason - the deck's
  only tutor, and the line to Malakir Bloodwitch's protection from white in an all
  mono-white pod.
- Damn: **NO**, unchanged. Secluded Courtyard: **NO**, unchanged.
- Cut pool remaining: thin. Feed the Swarm is the only card below the swap line with a
  named, non-hypothetical reason to go, and that reason is a trade-off rather than a
  weakness.


---

# Revision 2, 2026-09-07

User raised a rules point on Oubliette and proposed two further candidates, Blood
Tribute and Shared Animosity. Oubliette is spared; both new candidates are NO.

## 1. Oubliette is spared — the user is right, and it is the deck's only permanent commander answer

User's claim: *"Oubliette when used on commanders prevent them from going back to the
command zone, effectively taking them out of the game forever as long as Oubliette
remains OTB."* **Verified and correct.**

Oubliette phases the creature out; phasing is **not a zone change**. The permanent stays
on the battlefield, treated as though it does not exist. The commander replacement effect
only applies if a commander *would be put into a graveyard, hand, library, or exile* —
none of which happens. So it never reaches the command zone and can never be recast. The
official ruling closes the loop: *"A creature phased out by Oubliette doesn't phase in
during its controller's untap step as normal. Rather, it phases in immediately after
Oubliette leaves the battlefield."*

**Checked against the rest of the suite, and the role is unique.** Every other answer in
the deck hands a commander back to its owner:

| Card | What happens to a commander |
|---|---|
| Swords to Plowshares | exiled → command zone, recastable |
| Anguished Unmaking | exiled → command zone, recastable |
| Soul Shatter | sacrificed → graveyard → command zone |
| Feed the Swarm | destroyed → graveyard → command zone |
| Patron of the Vein | destroyed, then exiled → command zone |
| Olivia's Wrath | dies → command zone |
| **Oubliette** | **never changes zones — gone while Oubliette stays** |

Oubliette is the only card in the 99 that permanently answers a commander. That is the
same standard by which Forerunner was spared one revision ago (only tutor), and applying
it to one card but not the other inside a single session would be exactly the
self-inconsistency this process is supposed to prevent.

**What this does to my earlier argument.** I cut Oubliette for being the only removal
that can be *undone* — kill the enchantment, get the creature back. That risk is real and
I do not withdraw it. But it is the same property viewed from one side only: Oubliette is
simultaneously the most fragile answer and the most permanent one, and I priced only the
fragility. Against a commander the permanence is worth more, because the alternative is
not "clean answer" but "they recast it next turn."

Honest limits that stand: it **targets**, so hexproof, ward and protection from black
beat it; and mono-white is the format's best enchantment-removal colour.

## 2. New Blood's cut is now Feed the Swarm

Third cut candidate, third revision. **Cut: Feed the Swarm** `{1}{B}` — *"Destroy target
creature or enchantment an opponent controls. You lose life equal to that permanent's
mana value."*

1. **Necropotence changed its price.** Life is now the deck's card-draw currency, and
   Feed the Swarm's cost peaks exactly where it is aimed — killing a seven-drop in a
   fat-creature pod costs seven Necropotence activations. This is a real change since the
   card was last assessed, not a re-argument.
2. **It is the removal piece New Blood most directly replaces**: both answer a large
   creature, both are sorcery-speed, and New Blood costs no life and keeps the creature.
3. **Same-role swap.** Answers-to-a-creature stays at 6. Creatures stay 38. MV 2 → MV 4
   is the only curve move; black pips 1 → 2.

**The cost, stated plainly:** enchantment answers drop from **2 to 1**. Verified by oracle
scan — only Anguished Unmaking and Feed the Swarm can answer an enchantment, and against
mono-white that matters. This is a genuine trade, not a free upgrade. If your opponents'
enchantments are load-bearing, the right call is that **the deck is full and New Blood
does not get in** — that is a defensible outcome and I will not dress it up as a win.

Everything else below the swap line has a recorded sparing reason tied to a card still in
the deck: Blade of the Bloodchief (Anowon's recurring deaths, +6/+6 per cycle — taken off
the cut list 2026-08-30), War Room (a land, survives Farewell), Village Rites (only
instant-speed draw that doubles as a sac outlet), Impact Tremors (kept over Deadly
Dispute, Addendum 7), Forerunner (only tutor), Oubliette (above).

## 3. Blood Tribute — NO

`{4}{B}{B}` Sorcery, MV 6. *"Kicker—Tap an untapped Vampire you control. Target opponent
loses half their life, rounded up. If this spell was kicked, you gain life equal to the
life lost this way."* EDHREC rank **6,088** — the worst-ranked card considered this
session; 17.3% of Edgar decks. $4.68 (fetched 2026-09-07 13:22 UTC).

`combos.py --add` confirms it completes two lines already live in the deck: **Vito +
Blood Tribute** and **Bloodletter of Aclazotz + Blood Tribute**, both "target opponent
loses the game." Those are real — Bloodletter's *"they lose twice that much life
instead"* turns half a life total into all of it.

**It fails on the deck's own stated goal.** `meta.json`: *"Win with a string of
individually useful cards rather than by assembling a named combo."* Blood Tribute is not
individually useful. Alone, six mana takes one opponent from 40 to 20, affects no
permanent, and does nothing to the other two players. Its value is entirely in pairing
with a 4- or 5-drop enabler — and when Bloodletter or Vito is already on board with a wide
Vampire team, you were winning anyway. That is the definition of win-more.

**It is also off the deck's axis.** This deck drains *all three opponents at once* —
Sanctum Seeker, Blood Artist, Cruel Celebrant, Zulaport Cutthroat, Bastion of
Remembrance, Mirkwood Bats, Marauding Blight-Priest. Blood Tribute is single-target at
six mana.

Not a bracket violation — the lines are late and untutored, and the deck already runs two
Bloodthirsty Conqueror loops. It is simply a worse card than what it would cut.

## 4. Shared Animosity — NO as built, ADD IF the deck learns to connect

`{2}{R}` Enchantment. *"Whenever a creature you control attacks, it gets +1/+0 until end
of turn for each other attacking creature that shares a creature type with it."* EDHREC
rank 679; **35.7% of Edgar decks (17,965/50,363)**. $4.11 (fetched 2026-09-07 13:23 UTC).
Completes no combos.

**Steel-man, and it is stronger than "another lord."** The scaling is quadratic, not
additive. With 8 attacking Vampires each gets +7/+0 — **+56 total power**, where a lord
adds +8. It compounds with Bloodletter rather than duplicating it. This is a genuinely
powerful card in this shell and I am not rejecting it as a weak card.

**Why it still does not get a slot:**

1. **The gap it was counter-proposed for has been filled, on this deck's own record.**
   The 2026-08-30 review counter-proposed Shared Animosity as the finisher and wrote:
   *"It aims at the same gap Bloodletter fills. If you take Bloodletter, re-evaluate
   whether you still want it — the gap will be much smaller."* **Bloodletter is now in
   the deck.** That re-evaluation condition has been met, and this is it.
2. **It boosts the half of the attack this pod is built to stop.** The deck's actual kill
   is attack-*triggered*, not damage-based: Sanctum Seeker — *"Whenever a Vampire you
   control attacks, **each opponent** loses 1 life and you gain 1 life"* — fires on
   declaration, hits all three opponents, and **blockers cannot stop it**, then Bloodletter
   doubles it. Eight attackers with Sanctum Seeker and Bloodletter is 16 to each opponent
   before a single combat-damage step. Shared Animosity adds nothing to that line. What it
   boosts is combat damage that must connect — against two fat-creature decks and a token
   swarm whose chump blockers are its whole defensive plan, and with no trample anywhere
   in the deck.
3. **Fourth red card, and an enchantment in a Farewell pod.** Minor next to the above,
   but not free.

**ADD IF** you shift the deck toward connecting in combat — trample or mass evasion beyond
Vampire Nocturnus's conditional flying, or a pod where blockers are scarcer. In the pod on
record, the attack trigger is the kill and Shared Animosity does not touch it.

## Net position after Revision 2

| Card | Verdict |
|---|---|
| New Blood | **ADD** — cut Feed the Swarm (see the trade-off above) |
| Damn | NO |
| Secluded Courtyard | NO |
| Blood Tribute | NO — conflicts with the deck's stated no-named-combo goal |
| Shared Animosity | **ADD IF** the deck gains trample/evasion; NO as built |

Spared this session with newly recorded reasons: **Forerunner of the Legion** (only
tutor; finds Malakir Bloodwitch's protection from white into an all-mono-white pod) and
**Oubliette** (only permanent commander answer). Both were my cuts; both were wrong.


---

# Revision 3, 2026-09-07 — correction to the Blood Tribute reasoning

**Process error, conceded.** Revision 2 rejected Blood Tribute primarily on this line from
`meta.json`: *"Win with a string of individually useful cards rather than by assembling a
named combo."* That line sits under **Goals**. `meta.json` separately lists **Hard
constraints (vetoes)** — no early infinite combos, no tutor-dependent win line — and
**Preferences (tiebreakers only)**. Blood Tribute violates neither veto, and Revision 2
said so itself before rejecting it on the goal anyway.

Goals are direction, not vetoes. A card can be individually strong and earn a slot
without serving the headline plan. Treating a goal as a hard constraint let me skip the
work of evaluating the card on its own merits. That reasoning is withdrawn.

## Re-evaluated on the merits — still NO

1. **The effect anti-scales and cannot close.** *"Target opponent loses half their life,
   rounded up"* is 20 from 40, 10 from 20, 5 from 10. It never kills. Its absolute value
   shrinks exactly as the deck's own incremental drain works — Sanctum Seeker, Blood
   Artist, Cruel Celebrant, Zulaport Cutthroat, Bastion of Remembrance, Mirkwood Bats. In
   a pod where games run long, the card is weakest at the point it is castable.
2. **Six mana is scarce in this list.** Verified curve: the deck runs exactly **three**
   MV6 cards — Edgar Markov, Patron of the Vein (ETB destroy + 4/4 flier + counters on
   every Vampire when an opponent's creature dies) and Vein Ripper (6/5 flier, ward—
   sacrifice, drains on every creature death). Blood Tribute would be the fourth, and the
   only one leaving no permanent behind. Nonland curve: 1→12, 2→15, 3→18, 4→12, 5→5, 6→3.
3. **Single-target in a four-player pod**, with no board impact.

## The strongest argument for it, which neither side had made

Kicked, Blood Tribute gains roughly 20 life. **Necropotence entered the deck on
2026-09-06**, which converts life into cards at 1:1 — so the kicked mode is worth
something like 20 cards, entirely independent of the Vito and Bloodletter kill lines.
That is a genuine standalone use and a better case than the combo framing Revision 2
attacked.

It remains gated: Necropotence must already be resolved (9 mana across the two cards),
and Necropotence cards discarded at cleanup are exiled, so 20 life is fuel spread across
turns rather than a burst.

## What actually decides it

The slot. With Forerunner and Oubliette both spared on verified unique roles, **Feed the
Swarm is the only remaining cut**, and Blood Tribute must beat New Blood for it. It does
not: 6 mana, one opponent, no permanent left behind, versus 4 mana that answers the pod's
central problem (two fat-creature mono-white builds) and keeps the creature.

## ADD IF — a real condition, stated with the fact that settles it

The halving scales with the **opponent's** life total, and mono-white is the colour most
likely to inflate it. Against a deck sitting at 60–80 life, Blood Tribute removes 30–40
in one card and hands the same amount to Necropotence. **If any of the three opponents
routinely climbs above ~50 life, this should be re-run as a metagame card rather than a
generic one.** Unknown to this review; the user's answer settles it.

## Verdicts unchanged

New Blood **ADD** (cut Feed the Swarm) · Damn **NO** · Secluded Courtyard **NO** ·
Blood Tribute **NO**, on the merits above rather than on the goal ·
Shared Animosity **ADD IF** the deck gains trample or mass evasion.


---

# Revision 4, 2026-09-07 — the pod premise was wrong, and every verdict was re-run

## 1. The premise correction

User: *"There are 10+ decks used by 3 people that rotate from game to game. Building
against specific decks isn't my goal. Just trying to have generally useful cards that can
be reasonably applied sometimes."*

Every review since 2026-08-30 carried forward *"three opponents, mono-white — 2
fat-creature builds + 1 token swarm,"* and this review inherited it without
pressure-testing it. That is the exact failure the skill's step 1 warns about: a stale
meta premise does not produce one wrong verdict, it produces a wrong verdict for every
card whose case touches it. It produced three here.

**This premise should not be load-bearing in future reviews of this deck.** The standard
is general usefulness across 10+ rotating decks, not fit against named opponents.

## 2. Verdicts re-run on the general-usefulness standard

| Card | Verdict | Moved |
|---|---|---|
| Shared Animosity | **ADD** | ↑ from ADD IF |
| New Blood | **ADD** | unchanged |
| Damn | NO | unchanged |
| Secluded Courtyard | NO | unchanged |
| Blood Tribute | NO | ↓ reverted |

**Shared Animosity — up.** The ADD IF condition ("unless the deck gains trample or mass
evasion") was reasoning about specific opponents' blockers and does not survive. The
meta-independent facts carry it: 35 Vampires, a commander whose eminence makes a Vampire
token on every Vampire spell, and an Edgar trigger that rewards attacking. Five attackers
is +20 total power; eight is +56, against a lord's +8.

**New Blood — unchanged, and worth noting its case never depended on the pod.** Theft is
a 2-for-1 against any creature deck; it is the only unconditional steal in the 99; the
Vampire text-change synergies are internal to the deck list. The fat-creature framing was
supporting evidence, not the argument.

**Damn and Secluded Courtyard — unchanged, reasoning never touched the pod.** A symmetric
wrath is structurally wrong for a 38-creature go-wide deck regardless of opponents, and
Courtyard still cannot cast Grave Pact or Clever Concealment.

**Blood Tribute — reverted to NO.** Revision 3 moved it toward ADD on the strength of a
"two healing decks, totals above 40" read. That premise is gone and the move goes with
it. Generally: six mana, one opponent, no permanent left behind, and the halving shrinks
as totals fall.

**Tainted Remedy and Erebos, God of the Dead — counter-proposals withdrawn.** Both were
explicitly metagame cards aimed at a pod that does not exist as described.

**Both spared cards survive on meta-independent grounds.** Oubliette is the only permanent
commander answer and every deck has a commander. Forerunner's case *strengthens* under
rotation — a toolbox tutor is worth more when you do not know what you will face.

## 3. The cut changed again — Night's Whisper, not Blade of the Bloodchief

User: *"Nights whisper feels lower impact than bloodchief."* Checked, and it holds.

**Night's Whisper** `{1}{B}` — *"You draw two cards and lose 2 life."* EDHREC rank 182,
$5.45 (fetched 2026-09-07 14:36 UTC).

1. **Card flow is 13 sources and 11 are repeatable permanents** — Necropotence,
   Skullclamp, Welcoming Vampire, Black Market Connections, Clavileño, Baron Bertram
   Graywater, High-Society Hunter, Henrika Domnathi, War Room, Voldaren Estate, Canyon
   Slough. The only one-shots are Night's Whisper and Village Rites, and Village Rites was
   spared as the only instant-speed draw that doubles as a sac outlet.
2. **Necropotence made it redundant at an exact rate.** Necropotence: *"Pay 1 life"* for
   one card — 1:1, no mana, repeatable. Night's Whisper: 2 life for 2 cards — the same
   1:1, plus two mana, plus the card itself. With Necropotence on the battlefield,
   casting Night's Whisper is strictly worse than paying the life directly.

**Blade of the Bloodchief keeps its slot, and its trigger is broader than earlier
revisions treated it.** *"Whenever **a creature** dies"* — not "a creature you control."
It collects from every death at a four-player table, the counters are permanent rather
than until-end-of-turn, and on Edgar (first strike, haste) it is a genuine commander-damage
clock.

**The honest counter, recorded:** Night's Whisper is rank 182 against Blade's 2,450, and
it is never a dead card where Blade does nothing on an empty board. The gap is real. What
overrides it is that the specific weakness here — eleven repeatable engines plus
Necropotence's identical life-per-card rate — is invisible to a global ranking.

## 4. Recommended swaps

**Primary: Night's Whisper → Shared Animosity.** This also resolves the enchantment
question raised earlier — Feed the Swarm stays, so enchantment answers remain at 2
(Anguished Unmaking, Feed the Swarm).

Aggregate: MV 2 → MV 3 (curve 15/18 → 14/19); pips −B +R (red cards 3 → 4 against 13 red
sources); card flow 13 → 12, still 11 repeatable; enchantments 6 → 7, which is the one
real cost — more exposure to Farewell.

**Second, if both cards are wanted: Feed the Swarm → New Blood**, accepting enchantment
answers dropping to Anguished Unmaking alone.

`base.txt` not modified by this revision; the only change applied this session remains
Painful Truths → Necropotence.
