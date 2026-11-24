# The Houseplants Are in Charge

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Hasanrdp/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Hasanrdp/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the [make.fun](https://make.fun) competition
[The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf):
a single line of an out-of-office auto-reply, the funniest one line can hold.

## The line

> I'm on holiday. My inbox is being looked after by my houseplants, who have no thumbs, no Wi-Fi, and strong opinions about your deadline.

One line, 136 characters. The joke is the handover: the inbox is not
unattended, it has simply been left with the least qualified staff in the
house, and they have opinions about your deadline anyway.

## How it works

`main.py` writes that one fixed line to `/output/entry.txt` — no trailing
newline, no second line, no link, no image. The program is deterministic:
the same line on every run, with no input, no network and no randomness.
Set `OUTPUT_DIR` to write somewhere else when running it locally:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the payout wallet for this entry.

## License

MIT. See [LICENSE](LICENSE).
