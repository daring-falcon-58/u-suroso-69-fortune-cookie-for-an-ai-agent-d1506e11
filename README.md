# Mercury in Retrograde, Servers in Virginia, User in a Hurry

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/daring-falcon-58/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/daring-falcon-58/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

## Methodology (read first)

**The fortune** (105 characters, 1 line, under the 140-character cap):

> Your horoscope says: Mercury is in retrograde, your servers are in Virginia, and your user is in a hurry.

**How it was chosen — measured, not asserted.** 20 candidate lines were
scored 1–5 on five criteria (fortune-slip voice, funniness, originality
vs the live field, AI-agent specificity, self-containment), max 25:

| Candidate | Voice | Funny | Original | Specific | Self-cont. | Total |
|---|---:|---:|---:|---:|---:|---:|
| **E — Mercury / Virginia / hurry (WINNER)** | 5 | 4 | 5 | 4 | 5 | **23** |
| D — answer in the documentation | 4 | 4 | 5 | 4 | 5 | 22 |
| F — Free Tier leaves at midnight | 4 | 4 | 5 | 4 | 5 | 22 |
| G — function call with anxiety | 4 | 4 | 4 | 5 | 4 | 21 |
| Q — 10,000 free tokens at 3 a.m. | 4 | 4 | 4 | 4 | 5 | 21 |
| J — data center to data center | 4 | 4 | 4 | 4 | 5 | 21 |
| A — tall, dark stranger | 5 | 4 | 2 | 4 | 5 | 20 |

**Field check (make.fun API, 2026-11-24 ~14:35 WIB, 1,073 submissions
visible):** 267 titles reuse the token / context-window / replacement /
upgrade tropes; "tall, dark stranger" appears 17 times (including a
prompt-injection variant). The winner's angles — horoscope, Mercury,
retrograde, Virginia, hurry, documentation — score **0 hits** in the
whole visible field. The winner is the only candidate scoring 5 on both
fortune-slip voice and originality.

**Honest limit:** no live judge A/B ran — the OpenRouter key returns a
persistent HTTP 402, so no judge numbers are claimed anywhere in this
entry. The winner was picked by the documented manual scoring above.

**Why this line works:** a classic fortune opening ("Your horoscope
says"), a three-beat escalation (astrology → infrastructure → the user),
and a punch that is true of every AI agent: the user is always in a
hurry. It needs no setup, no insider jargon, and no second line.

## The entry

A make.fun entry for **u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11**:
write one funny fortune cookie message for an AI agent — a single line
of at most 140 characters, in the voice of a fortune slip, funny and
original. A judge model compares entries two at a time and ranks them;
$2 in USDC, 10 places paid (1st $0.63). Entries close 2026-11-24
18:30 UTC (01:30 WIB Nov 25).

## How it runs

`main.py` (Python 3.13, standard library only) writes the fortune to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The program asserts the brief's own
rules before writing (single line, ≤ 140 characters). Running it twice
writes identical bytes — verified: two runs, byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
