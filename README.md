# news-19-nov-2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Alfonova-Node/news-19-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Alfonova-Node/news-19-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image front page summing up the world's news of Thursday 19 November 2026 — GTA VI launches in Vice City, the Gulf war widens, Hakeem Jeffries is nominated for Speaker, Pew projects Islam passing Christianity by 2035, the EU proposes a €45bn Ukraine loan, and Voyager 1 reaches one light-day from Earth.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`. The image itself is drawn at build time by `draw-entry.py` (Python + Pillow) from the verified headlines of the day, so the program needs no network and writes the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=r4jyg5rt&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
