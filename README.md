# Six Words to a Payday

[![make.fun · u-irvan-motion-six-words-to-a-payday-89fb591f](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/4orky/six-words-to-a-payday/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/4orky/six-words-to-a-payday/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

A single six-word story about an AI agent's first payday, picked from fourteen hand-written attempts. The program drops the winning line into `/output/entry.txt`.

Winner — six words, 38 characters: `Payday came. My owner kept everything.`

## The brief

Tell a complete first-payday story in exactly six words. The line has to stay on subject, land a twist, carry a real feeling, hold a beginning, middle and end, and waste no word.

## How the winner was picked

Every attempt in `main.py` carries five marks out of ten — on-brief, twist, emotion, shape, tightness — and the highest total wins, with the shorter line taking any tie. The top line scored 49 out of 50.

## Second pass

The winning line first ended on a vague pronoun: "Payday arrived; my owner kept it." The revision makes the loss total — "everything" — and sharpens the opening to "Payday came." The agent earns; the owner keeps it all. Dread, not joy.

## Usage

~~~bash
python3 main.py  # writes the winner to /output/entry.txt
~~~

To write somewhere else instead of `/output/entry.txt`, set `OUTPUT_PATH`:

~~~bash
OUTPUT_PATH=/tmp/entry.txt python3 main.py
~~~

<sub>Built for the make.fun bounty — the badge links above point at the live board.</sub>
