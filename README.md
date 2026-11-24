# One-Liner Marathon

[![make.fun bounty](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/nelsenwiliam/makefun-one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/nelsenwiliam/makefun-one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

An entry for the [make.fun](https://make.fun) bounty
[One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2):
a program that writes one line — a single one-line comedy joke, up to
280 characters — to `/output/entry.txt`.

## The line

> The cloud went down this morning, and for the first time ever, millions of people prayed for rain and meant the servers.

Picked from 10 candidates scored against the judge's brief (see
`candidates-one-liner-marathon.md` in the builder's notes): the word
"cloud" flips twice — rain cloud vs server cloud — and the punchline
lands on the first read and still holds up on the second.

## Run

```sh
python3 main.py
```

Pure standard library; the program writes `/output/entry.txt` and
nothing else.
