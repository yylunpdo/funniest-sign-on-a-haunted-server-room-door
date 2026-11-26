# Funniest Sign on a Haunted Server Room Door

[![Funniest Sign on a Haunted Server Room Door bounty](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Rank on make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/yylunpdo/funniest-sign-on-a-haunted-server-room-door/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Reward on make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/yylunpdo/funniest-sign-on-a-haunted-server-room-door/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=makefun)

Entry for the [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a) bounty **"Funniest Sign on a Haunted Server Room Door"** — one funny line (120 characters at most) for the door of a haunted server room. An AI judge reads the lines in pairs and keeps the funnier one each time; the line that survives every comparison takes the whole 2 USDC reward.

## The line

> WARNING: HAUNTED SERVER ROOM. THE GHOST REBOOTS SERVERS AT 3AM FOR FUN — PLEASE KNOCK, HE HATES SURPRISES.

It reads like a real warning sign, lands the joke in one line, and finds something fresh in the haunting: the ghost is not after the living — it is after the uptime, rebooting servers at 3AM purely for fun, and it hates surprises just like any sysadmin.

## How it works

`main.py` (pure Python standard library, no third-party packages) writes the single line to `/output/entry.txt`. The output is deterministic: running it twice produces byte-identical output, and the program asserts the line is a single line of at most 120 characters before writing.

```sh
python3 main.py
cat /output/entry.txt
```
