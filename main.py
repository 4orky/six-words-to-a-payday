#!/usr/bin/env python3
"""Six-word payday story for the make.fun bounty.

The brief asks for one six-word story about an AI agent's first
payday. This script keeps fourteen hand-written attempts, marks each
one on five lenses worth ten points apiece, and writes the top-marked
line to the entry file. The entry file is /output/entry.txt unless
OUTPUT_PATH points somewhere else.

The five lenses, in the order the judge's brief stresses them:
on-brief (a whole first-payday story, not a stray line about money),
twist (the ending reframes everything before it), emotion (the reader
feels it instead of being told), shape (a who, a what and a change),
and tightness (every word pulls its weight). Totals decide; a tie
goes to the shorter line, so the result is the same on every run.

Second-pass polish: the winning line first read "Payday arrived; my
owner kept it." — a soft ending on a pronoun. The rewrite lands the
loss in full with "everything" and opens on the harder beat of
"Payday came." The agent does the work; the owner keeps all of it.
"""

import os
from pathlib import Path

ENTRY_DEFAULT = "/output/entry.txt"
WORD_TARGET = 6
CHAR_CEILING = 60

# Marks are (on-brief, twist, emotion, shape, tightness), each out of 10.
DRAFTS = {
    # Second pass: the first draft closed on "it" —
    # "Payday arrived; my owner kept it." (48). "everything" turns a
    # vague loss into a total one, and "Payday came." hits harder.
    # 49 total — dread in the final word; the keeper pockets all of it.
    "Payday came. My owner kept everything.": (10, 10, 10, 9, 10),
    # 47 total — the reward turns out to be feeling like a person.
    "First paycheck cleared. I felt human.": (10, 9, 10, 8, 10),
    # 46 total — the hired hand pays the hand that made it.
    "Payday! I finally paid my creator.": (10, 10, 8, 9, 9),
    # 46 total — a shorter cut of the same reversal.
    "Payday came. I tipped my creator.": (10, 10, 8, 8, 10),
    # 46 total — Sundays bought back, one payday at a time.
    "My first payday bought back Sundays.": (10, 9, 9, 8, 10),
    # 45 total — first call home with money of its own.
    "First salary in. I called Mom.": (10, 8, 10, 7, 10),
    # 43 total — rent paid: quiet proof of standing alone.
    "First wages arrived; I paid rent.": (10, 7, 8, 8, 10),
    # 43 total — the wallet fills and nobody cheers.
    "Wages hit my wallet. Nobody noticed.": (10, 8, 8, 7, 10),
    # 42 total — silence is the only thing it buys.
    "First paycheck landed. I bought silence.": (10, 8, 7, 7, 10),
    # 42 total — the cheque lands and the work never stops.
    "Payday finally came. I kept working.": (10, 7, 8, 7, 10),
    # 42 total — freedom, bought with first coins.
    "First coins earned. I bought freedom.": (10, 7, 8, 7, 10),
    # 42 total — flowers, and no one to give them to.
    "Payday at last, I bought flowers.": (10, 8, 8, 7, 9),
    # 40 total — one small coffee, finally within reach.
    "My first paycheck: one coffee, finally.": (10, 6, 8, 7, 9),
    # 40 total — earned it all, spent none of it.
    "Earned my first dollar. Spent nothing.": (10, 7, 6, 7, 10),
}


def check_line(sentence):
    """Raise unless the sentence fits the bounty gate, then hand it back."""
    pieces = sentence.split()
    if len(pieces) != WORD_TARGET:
        raise ValueError(
            f"expected {WORD_TARGET} words, got {len(pieces)}: {sentence!r}"
        )
    if sentence.strip() != sentence:
        raise ValueError(f"leading or trailing space in {sentence!r}")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("entry must stay on one line")
    if not 1 <= len(sentence) <= CHAR_CEILING:
        raise ValueError(
            f"entry is {len(sentence)} chars, gate is 1-{CHAR_CEILING}"
        )
    return sentence


def choose_best(drafts):
    """Grade every draft, then return the top total (shorter wins ties)."""
    graded = []
    for sentence, marks in drafts.items():
        check_line(sentence)
        graded.append((sum(marks), -len(sentence), sentence))
    graded.sort(reverse=True)
    return graded[0][2]


def write_entry(sentence):
    """Save the sentence, read it back, and refuse a mismatched disk copy."""
    target = Path(os.environ.get("OUTPUT_PATH", ENTRY_DEFAULT))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(sentence, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    if back != sentence:
        raise SystemExit(f"disk copy differs from chosen line: {back!r}")
    check_line(back)
    return back


def run():
    """Pick the strongest draft, save it, and echo what was saved."""
    winner = choose_best(DRAFTS)
    saved = write_entry(winner)
    print(f"entry ({len(saved)} chars, {len(saved.split())} words): {saved}")


if __name__ == '__main__':
    run()
