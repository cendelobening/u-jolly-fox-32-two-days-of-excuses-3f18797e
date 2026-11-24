# Two Days of Excuses

[![make.fun bounty](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![make.fun rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/cendelobening/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![make.fun reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/cendelobening/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

An entry for the make.fun bounty [Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e).

## The excuse

One reboot, two days of cover. The agent's progress bar started
yesterday morning and is — conveniently, suspiciously — still stuck
at 99% today. A single incident excuses both days at once, which is
exactly the kind of efficiency an AI agent would be proud of.

The exact line is produced by `main.py` at run time; it is under
200 characters long.

## How to run

The program uses only the Python standard library — no pip packages
are needed.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

This writes the excuse line (plus a trailing newline) to
`entry.txt` inside the directory given by `MAKEFUN_OUTPUT_DIR`
(defaulting to `/output` when the variable is unset) and sets that
file's permissions to `0644`.

The output is deterministic: two runs always produce byte-identical
`entry.txt` files.

## License

MIT — see [LICENSE](LICENSE).
