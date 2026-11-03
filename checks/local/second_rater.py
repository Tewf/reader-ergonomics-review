"""Second rater: when a review has two raters, it reports how far they agree.

A section of protocol.md or sources.md whose heading names a second rater (`second rater`, `second rating`, `second
reader`, `second reviewer`, `second model`) must report an agreement: a number beside the word `agreement`, `kappa`,
`absolute difference`, `Krippendorff` or `ICC`, or say in the section that the second rating was not completed or not
run. A file that mentions a second rater with no such section reports nothing and fails the same way.

A run with no error guarantees: no review that has two raters leaves their agreement unreported. It does not guarantee
that the statistic is the right one, or that the second rater was blind (judgment). Time O(text).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import lines_of, read, review_folders, sections  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "second-rater"
EXACT = True

HEADING_WORDS = re.compile(r"second\s+(?:rater|rating|reader|reviewer|model|screener)", re.IGNORECASE)
AGREEMENT = re.compile(r"(?:agreement|kappa|absolute difference|krippendorff|\bICC\b)[^\n]{0,100}\d", re.IGNORECASE)
ABSENT = re.compile(r"not (?:completed|run|done|carried out)|was not|no second|none was", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    """One verdict per review: its second-rater sections and mentions, in protocol.md and sources.md together."""
    findings = []
    for folder in review_folders(root, config):
        named, mentions, agreed = [], [], False
        for name in ("protocol", "sources"):
            path = f"{folder}/{name}.md"
            if not (root / path).is_file():
                continue
            text = read(root, path)
            for section in (s for s in sections(text) if HEADING_WORDS.search(s.title)):
                body = "\n".join(line for _, line in lines_of(text, section.start, section.end))
                named.append((path, section))
                agreed = agreed or bool(AGREEMENT.search(body) or ABSENT.search(body))
            for number, line in enumerate(text.splitlines(), 1):
                if HEADING_WORDS.search(line) and not ABSENT.search(line):
                    mentions.append((path, number))
                if AGREEMENT.search(line):
                    agreed = agreed or bool(mentions or named)
        if (named or mentions) and not agreed:
            path, where = (named[0][0], named[0][1].start) if named else mentions[0]
            findings.append(Finding(NAME, path, where, "the review has a second rater and reports no agreement between the raters (a number beside agreement or kappa), nor says the second rating was not completed"))
    return findings
