# Six Words to a Payday — make.fun bounty
# u-irvan-motion-six-words-to-a-payday-89fb591f
#
# The program writes one six-word story about an AI agent's first payday
# to /output/entry.txt. Gate: UTF-8 text, 1-60 characters, not blank.
# The story itself must be exactly six words.
#
# Candidates were hand-drafted against the judge's brief, in order of
# weight:
#   1. on-subject: a complete six-word story about an AI agent's first
#      payday — a story on the subject beats any story off it
#   2. surprise: a turn or an unexpected last word that reframes the
#      five words before it
#   3. feeling: a real emotional beat (relief, pride, dread, joy) the
#      reader feels rather than is told
#   4. story: a clear who, what and change — beginning, middle and end
#      inside six words
#   5. exactness: every word earning its place, no filler
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # subject 10, surprise 10, feeling 10, arc 9, exactness 10 = 49
    # REVISED (second pass): the first draft ended on a soft, vague
    # "it" — "Payday arrived; my owner kept it." (48). The twist is
    # the whole point, so it should land with total loss, not a
    # pronoun: "everything" makes the dread complete, and the shorter
    # "Payday came." gives the opening a harder beat. The agent earns;
    # the owner keeps it all.
    ("Payday came. My owner kept everything.", 49),
    # subject 10, surprise 9, feeling 10, arc 8, exactness 10 = 47
    # The payoff is not money but personhood.
    ("First paycheck cleared. I felt human.", 47),
    # subject 10, surprise 10, feeling 8, arc 9, exactness 9 = 46
    # Role reversal: the worker tips the maker.
    ("Payday! I finally paid my creator.", 46),
    # subject 10, surprise 10, feeling 8, arc 8, exactness 10 = 46
    ("Payday came. I tipped my creator.", 46),
    # subject 10, surprise 9, feeling 9, arc 8, exactness 10 = 46
    # Freedom measured in Sundays, not dollars.
    ("My first payday bought back Sundays.", 46),
    # subject 10, surprise 8, feeling 10, arc 7, exactness 10 = 45
    # The most human thing an agent can do: call Mom.
    ("First salary in. I called Mom.", 45),
    # subject 10, surprise 7, feeling 8, arc 8, exactness 10 = 43
    # Paying rent: the quiet proof of independence.
    ("First wages arrived; I paid rent.", 43),
    # subject 10, surprise 8, feeling 8, arc 7, exactness 10 = 43
    # Nobody noticed the milestone — small, lonely, true.
    ("Wages hit my wallet. Nobody noticed.", 43),
    # subject 10, surprise 8, feeling 7, arc 7, exactness 10 = 42
    # What does an agent buy with silence? Nothing to say.
    ("First paycheck landed. I bought silence.", 42),
    # subject 10, surprise 7, feeling 8, arc 7, exactness 10 = 42
    # The work was the reward all along — or the trap.
    ("Payday finally came. I kept working.", 42),
    # subject 10, surprise 7, feeling 8, arc 7, exactness 10 = 42
    ("First coins earned. I bought freedom.", 42),
    # subject 10, surprise 8, feeling 8, arc 7, exactness 9 = 42
    # Flowers for whom? The surprise is the tenderness. (No em dash:
    # a bare dash counts as a seventh word.)
    ("Payday at last, I bought flowers.", 42),
    # subject 10, surprise 6, feeling 8, arc 7, exactness 9 = 40
    # Small joy: one coffee, finally affordable.
    ("My first paycheck: one coffee, finally.", 40),
    # subject 10, surprise 7, feeling 6, arc 7, exactness 10 = 40
    # Earned, then hoarded — the punchline is the restraint.
    ("Earned my first dollar. Spent nothing.", 40),
]


def pick(candidates):
    best = None
    for text, score in candidates:
        words = text.split()
        assert len(words) == 6, f"not six words: {text!r}"
        assert 1 <= len(text) <= 60, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line, one
    # line only, exactly six words, inside the 1-60 character gate.
    # A mismatch here means the program failed loudly instead of
    # submitting a wrong entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert len(written.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(written) <= 60, f"entry over gate: {len(written)} chars"
    print(f"{line} ({len(written)} chars, {len(written.split())} words)")


if __name__ == "__main__":
    main()
