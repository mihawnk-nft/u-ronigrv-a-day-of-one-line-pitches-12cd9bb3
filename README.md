# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mihawnk-nft/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mihawnk-nft/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
competition **A Day of One-Line Pitches**.

## The entry

`main.py` (pure Python standard library, no network, no randomness) writes
one sentence — at most 240 characters — to `/output/entry.txt`. The sentence
is a pitch meant to convince a friend who has never coded to let an AI agent
build their first app idea on make.fun:

> Just tell me your app idea in plain words and I'll have an AI agent build
> your first working version on make.fun tonight — free to try, no code
> needed, and you only keep it if you love it.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py out.txt    # optional output path, for local testing
```

The program checks its own output before writing: 1–240 characters,
exactly one sentence, UTF-8, no trailing newline.

## License

MIT — see [LICENSE](LICENSE).
