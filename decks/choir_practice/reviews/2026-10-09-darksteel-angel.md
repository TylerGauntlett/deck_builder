# Darksteel Angel (2026-10-09)

Deck: choir_practice (Giada, Font of Hope), bracket 3, $40/card cap. Evaluated against `complete.txt` (100 cards, the current build after the 2026-10-05 Lightning Greaves swap). `base.txt` is the original precon and was not used for counts.
Prices: Scryfall, fetched 2026-10-09 06:02–06:04 UTC. EDHREC: Giada commander page, 36,794 decks; Darksteel Angel card page.

## Verdict

| Card | Verdict |
|---|---|
| Darksteel Angel | **NO.** It is the deck's already-cut "can't lose" Angel at +2 mana without flash; the pod's main win route is already blanked by a 4-mana Magus of the Moat. |

## Facts (all verified this session)

**Darksteel Angel** {9}, Artifact Creature — Angel, 4/4. "Flying, indestructible. You can't lose the game and your opponents can't win the game. Creatures you control can't have -1/-1 counters put on them." Colorless, legal, not a Game Changer. $4.11 (06:02 UTC).

Rulings (2026-08-21): concession still loses; effects that make the game a draw still work; nothing else can make you lose or an opponent win while you control it.

**Herald of Eternal Dawn** {4}{W}{W}{W}, Creature — Angel, 6/6. "Flash. Flying. You can't lose the game and your opponents can't win the game." $1.57. In the precon (`base.txt`), cut for Akroma's Will in the 2026-10-02 build-out with the reason: *"a 7-mana 'can't lose' body that does not advance a win."*

## Step 0: the honest best case

The pod's wins mostly come through ground attacks (meta.json, 2026-10-02). Darksteel Angel makes every one of those attacks, and every other win route, unable to finish you. Unlike every other "don't lose" piece in the list it is **indestructible**, so it survives Day-of-Judgment-style wipes, destroy-based spot removal, combat, and your own Austere Command. It is an Angel, so it is not a dead body: it enters with Giada's counters (with Giada + 4 Angels out, an 8/8 indestructible flier), and triggers Bishop of Wings ("Whenever an Angel you control enters, you gain 4 life"), Righteous Valkyrie ("gain life equal to that creature's toughness"), Cathars' Crusade, Folk Hero and Vanquisher's Banner. Its generic cost is payable by Giada's Angel-only mana, Three Tree City and colourless lands, and reduced by Starnheim Aspirant ({2}), Urza's Incubator ({2}) and Herald's Horn ({1}).

That is a real case. It loses on the tests below.

## The tests

**Redundancy — Herald of Eternal Dawn is the same card, cheaper, and the deck already cut it.**
Effect × frequency × duration is identical: a static "you can't lose / opponents can't win" on a flying Angel body, lasting while it survives. The differences:

| | Darksteel Angel | Herald of Eternal Dawn |
|---|---|---|
| Cost | {9} | {4}{W}{W}{W} (7) |
| Reducers in this deck | Aspirant, Incubator, Horn, Giada mana | same **plus Pearl Medallion** ("White spells you cast cost {1} less"). Darksteel is colorless, so Medallion does nothing for it. |
| Speed | sorcery | **flash** — cast it in combat after attackers are declared, or at end of turn with Giada's mana, so it dodges a full turn cycle of sorcery-speed answers |
| Body | 4/4 indestructible | 6/6 |
| Survives | destroy, damage | neither, but Sephara ("Other creatures you control with flying have indestructible") and Avacyn ("Other permanents you control have indestructible") cover that for both |
| Dies to | exile (Swords to Plowshares, Path to Exile), bounce, edicts, Farewell | same |

Indestructible is Darksteel's only edge, and the removal that actually answers a "can't lose" card in casual pods is exile and bounce, which ignore it. Flash is the more useful property for this effect: the job is to be on the battlefield when lethal damage would land, and flash lets you hold it until then. So if the deck wants this role at all, Herald is the card, and the deck has already decided against Herald. Recommending Darksteel would contradict the build-out reasoning without a new fact to justify it. None has been offered.

**Marginal impact — the games it changes are already covered, cheaper.**
The pod's stated win route is ground combat. The deck already answers that, verified:

- **Magus of the Moat** (4): "Creatures without flying can't attack." Blanks the pod's main win route for the whole table.
- **Ghostly Prison** (3): "Creatures can't attack you unless their controller pays {2} for each creature."
- **Archangel of Tithes** (4): attack tax of {1} per creature while untapped.
- **Elesh Norn** (7): "Creatures your opponents control get -2/-2."
- **Ob Nixilis** (7): "destroy all tapped creatures your opponents control."
- Plus the life buffer: Bishop of Wings alone is 4 life per Angel, and the shape review notes the deck routinely sits at 55+.

Darksteel does more than these in one respect: it also stops non-combat wins (drain, alt-wins, poison). There is no table report that the deck is losing to those. And it arrives three to five turns after Magus.

**Cost of entry.** The current nonland curve (from `complete.txt`): 1:4, 2:16, 3:16, 4:11, 5:7, 6:3, 7:5, 8:1. The build-out deliberately removed the deck's only 9 (Reya Dawnbringer, *"costs 9 and does nothing on the turn it lands"*) and left Avacyn as the lone 8. Darksteel would be the highest-cost card in the deck. Without a reducer out it needs nine mana; Pearl Medallion, the cheapest reducer, does not apply.

**Worst-case draw.** Opening hand: dead until turn 7 at best, and the deck's early game has no use for it. Turn 12 on an empty board: genuinely good — a 4/4 indestructible flier that stops you dying. That is the card's best scenario, and it is also exactly where Herald (flash it in at end of turn, untap with a 6/6) is at least as good.

**Anti-synergy.** None real. Angel of Destiny's alt-win makes opponents *lose*; Darksteel only stops opponents *winning*, so the two do not conflict. Farewell's creature mode exiles it, but Farewell is a choice you make. The -1/-1 counter clause is defensive only; Elesh Norn's -2/-2 is not counters.

**Density.** Self-contained; needs only mana.

**Bracket.** Not a Game Changer. `combos.py --add "Darksteel Angel" --near` (run against `complete.txt`): baseline 0 combos, completes 0. The one near-combo is Transcendence + Darksteel Angel (draw the game); Transcendence is not in the deck.

**Disagreement check.** Community agrees: Darksteel Angel is in 276 Giada decks (~0.75% of 36,794); Herald of Eternal Dawn is in 10,251 Giada decks (28.1% of 36,521). Independent reasons, from above: the deck already chose against Herald, and Magus of the Moat answers the pod's specific win route.

**Price.** $4.11, fetched 2026-10-09 06:02 UTC. Not part of the verdict. The rejection holds if the card is free.

## The cut it would need

Prior reviews ranked the next cuts: Heraldic Banner (named the next cut on 2026-10-05), Radiant Fountain (only if flooding shows up), Valorous Stance (reserved for Teferi's Protection). The honest cut for Darksteel would be **Heraldic Banner** ({3} rock, "Creatures you control of the chosen color get +1/+0"). Trading a mana rock for a 9-drop makes the 9-drop harder to cast. That is not a swap I would make for a card that loses to Herald on every axis but one.

## Counter-proposal

The role, "don't lose to a board you can't beat", is real only if the table is actually beating you that way. If it is, **Herald of Eternal Dawn** is the card, and you already own it (it is in the precon). I am **not** recommending it today either: the build-out cut it for Akroma's Will, and nothing new says that was wrong.

What would reopen it — two questions for the user:

1. **How long do games actually run?** If they routinely go past turn 10, a 7-mana flash lock is castable on time and the build-out's "does not advance a win" reasoning should be rechecked against how late the wins actually come.
2. **How does this deck actually lose?** If it loses through Magus of the Moat and the attack taxes (fliers, trample over a stalled board, drain, alt-wins), the "can't lose" role is unfilled, and Herald for Heraldic Banner becomes a real question.

## Housekeeping

`scripts/combos.py` and `edhrec.py --diff` read `base.txt`, which is the original precon, not the current build. For this review they were run against a temporary copy of `complete.txt`, deleted afterwards. If `complete.txt` is the list you play, consider making it `base.txt` (keeping the precon as e.g. `precon.txt`) so the tooling and the reviews agree by default. That is your call; `base.txt` was not modified.
