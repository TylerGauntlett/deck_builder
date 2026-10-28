# Firemane Commando + Herald of War for Angel of Vitality + Dazzling Angel

Date: 2026-10-28. Deck: choir_practice (Giada, bracket 3). The current list is `complete.txt`, which is base minus `removal.txt` plus `adds.txt`.

**Verdict: NO on both.** Keep Angel of Vitality and Dazzling Angel.

This brings back two precon cards that earlier reviews already cut. Firemane Commando was cut for Ghostly Prison on 2026-10-02 (`2026-10-02-bracket-3-buildout.md`). Herald of War was cut for Angel of Invention in the same review, where it was already on the "next out" list.

## Verified text (Scryfall, fetched 2026-10-28 22:31 UTC)

| Card | Cost | Text that matters | Price |
|---|---|---|---|
| Angel of Vitality | {2}{W} 2/2 | "If you would gain life, you gain that much life plus 1 instead." "+2/+2 as long as you have 25 or more life." | foil $0.27 (no non-foil price listed) |
| Dazzling Angel | {2}{W} 2/3 | "Whenever another creature you control enters, you gain 1 life." | $0.33 |
| Firemane Commando | {3}{W} 4/3 | "Whenever you attack with two or more creatures, draw a card." / "Whenever **another player** attacks with two or more creatures, **they** draw a card if none of those creatures attacked you." | $0.93 |
| Herald of War | {3}{W}{W} 3/3 | "Whenever this creature attacks, put a +1/+1 counter on it." "Angel spells and Human spells you cast cost {1} less … for each +1/+1 counter on this creature." | $2.70 |

None of the four completes a Commander Spellbook combo (`combos.py --add`: 0 new combos for Herald of War and for Firemane Commando).

EDHREC inclusion in Giada decks: Herald of War 77.1%, Angel of Vitality 67.4%, Firemane Commando 56.7%, Dazzling Angel 43.7%. All four are popular, so popularity does not settle this.

## The deck's bridge, and where each card sits

Lifegain connects the deck's two modes: going wide with Angels, and growing them with counters. Each lifegain **event** fires every "whenever you gain life" payoff:

- **Per-event payoffs:** Archangel of Thune (a counter on each creature), Lyra, Archangel of Dawn (a counter on each Angel), Exemplar of Light, Dawn of Hope (pay {2}: draw), and Ob Nixilis's end step ("if you gained life this turn").
- **Threshold payoffs (amount matters):** Resplendent Angel (5 or more this turn), Valkyrie Harbinger (4 or more), Righteous Valkyrie (+2/+2 at starting life +7), Angel of Destiny (wins at starting life +15).
- **Repeating per-enter gain sources:** Bishop of Wings (4 per Angel), Seraph Sanctuary (1 per Angel), Righteous Valkyrie (toughness per Angel or Cleric), and **Dazzling Angel (1 per creature of any type)**.

The two cards you want to cut both sit on that bridge:

- **Angel of Vitality is a multiplier, not filler.** It adds no new events, but it raises every amount. For example, Bishop of Wings' 4 becomes 5, so one Angel entering now turns on Resplendent Angel's 4/4 token by itself. It also counts toward Valkyrie Harbinger's 4, Righteous Valkyrie's +7 and Angel of Destiny's +15. On its own it is a 4/4 flier for 3 whenever you are at 25 or more life, which is most of a 40-life game.
- **Dazzling Angel is the only per-enter gain source that counts non-Angels.** Servos from Angel of Invention, Spirits from Bishop and Soldiers from Dawn of Hope all trigger it. With Archangel of Thune out, every creature entering puts a counter on your whole team. It is the weaker of the two, but it is still on the engine.

The two cards you want to add sit off the bridge, in categories the deck is already deep in:

### Firemane Commando: NO

- **Steel-man:** a 4-mana 4/3 flying Angel that draws a card on most of your attacks. It is an Angel, so Giada and the reducers apply to it.
- **Attack:** its second clause pays opponents. The deck runs Ghostly Prison, Archangel of Tithes ("creatures can't attack you … unless their controller pays {1}") and Magus of the Moat. All three exist to push attacks toward other players, and every 2-creature attack that skips you draws that opponent a card. This was the reason it was cut on 2026-10-02, and that reason still holds: all three cards are still in the list.
- **Overlap:** the deck already has an attack-draw that gives opponents nothing. Minas Tirith reads "{1}{W}, {T}: Draw a card. Activate only if you attacked with two or more creatures this turn."
- **Would change my mind:** if Ghostly Prison, Archangel of Tithes and Magus of the Moat all left the deck, Firemane's downside mostly goes away and it should be re-evaluated.

### Herald of War: NO

- **Steel-man:** this is the strongest case in the proposal, so it is worth stating fully. Giada says "Each other Angel you control enters with an additional +1/+1 counter … for each Angel you already control." With Giada and two other Angels out, Herald enters with 3 counters, so Angels cost 3 less right away. Archangel of Thune, Lyra, Archangel of Dawn and Cathars' Crusade keep adding counters, which keeps raising the discount.
- **Attack:** it is a 5-mana reducer in a deck that already has Starnheim Aspirant (−2), Urza's Incubator (−2), Herald's Horn (−1), Pearl Medallion (−1) and Giada's Angel-only mana. It lands on turn 5 or later, when you need the discount least. A cost reducer only lowers generic mana, and it does nothing if it dies before you cast more Angels. It is an additive card in a category that is already deep.
- **Consistency:** the 2026-10-02 review ranked it among the first cards out, and nothing has changed since then.

## Aggregate delta

- **Curve:** two 3-drops leave and a 4-drop and a 5-drop come in, so the curve gets heavier.
- **Lifegain bridge:** you lose one multiplier and one per-enter gain source, and gain no lifegain at all.
- **Card draw and cost reduction:** both categories are already deep. You would gain one card in each, and Firemane's draw comes with a cost to you.
- **Angel count:** unchanged.

Both rejections hold even if the cards are free, because price is not part of the reasoning. These rejections also do not depend on how fast the pod's games run.

## Cut order if you want to move either 3-drop later

Dazzling Angel is the more cuttable of the two. Angel of Vitality should stay. Any replacement for Dazzling should either add lifegain events or be a payoff that multiplies them. Neither Firemane Commando nor Herald of War does either.

## Addendum (same day): the user is frequently targeted

The user explained that the pod targets them a lot, and that they want Firemane Commando's draw clause as an incentive for opponents to attack someone else. This is a new way to judge the card: as politics, not as card advantage. Under that framing the original reason for cutting it reverses.

- I cut Firemane because its second clause rewards opponents who attack players other than you. If the problem is being targeted, that reward is the reason to play the card.
- It works together with the attack taxes the deck already runs. With Ghostly Prison out, attacking you with two creatures costs {4} and draws nothing. Attacking someone else costs nothing and draws a card. Archangel of Tithes adds {1} per creature to attacks on you. A tax alone can be paid by an opponent with spare mana, but this gives them a reason to go elsewhere.
- Its first clause ("you attack with two or more creatures, draw a card") helps you rebuild after you've been focused.
- Limits:
  - It only affects combat. It does nothing against removal or wraths aimed at you.
  - Magus of the Moat stops ground attacks for everyone, so while Magus is out, opponents' two-creature attacks on each other are rare and the reward seldom fires.
  - It is a 4/3, so the first removal spell aimed at your board can take it.
  - It gives the whole table extra cards.

**Revised verdicts:**
- **Firemane Commando: ADD IF the targeting is mainly combat damage.** It replaces Dazzling Angel, which was already the softer of the two cuts. If the targeting is mostly removal and spells, Firemane doesn't address it and the NO stands.
- **Herald of War: still NO.** Being targeted makes a 5-mana, removal-vulnerable cost reducer worse, not better.
- **Angel of Vitality: still stays.** It multiplies every life gain, and the extra life is also a defensive buffer.
