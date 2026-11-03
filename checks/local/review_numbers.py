"""Review numbers: every number in review.md names its source and where it was read, or says it is secondary.

review.md is the file where a finding is stated with its figure ("g = -0.23", "19% slower", "over 60,000 projects").
The rule of the genre: a number is read in its source, and the line says where (an abstract, a section, a table), or it
is marked `(secondary)` when it was read in a summary, an abstract or another work's account. A number with no source key
(`Surname Year`) cannot be traced at all.

The opening, before the first `##` heading, states the review itself (how many sources it holds) and is not read. The unit is one line: a list item with its continuation lines, a table row, or a paragraph. Years, dates, versions,
question and strand labels (Q1, strand 2), ordinals and the numbers of a location (section 4.2, Table 7) are not
counted as figures. A location is looked for in any parenthesis (`abstract`, `section 4.2`, `read`) or in the 60 characters after a key.

A run with no warning guarantees: every line with a figure holds a key and, after a key, a location word or
`secondary`. Warnings only, since a figure's role (a count of the review's own sources, a rule's constant) is a
judgment. It does not guarantee that the number is what the source says (a reader or a second pass checks that).
Time O(text).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import HEADING, read, review_folders, sections  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "review-numbers"
EXACT = False

KEY = re.compile(r"(?:[A-Z][\w'’.&-]*\s+)+(?:19|20)\d\d[a-z]?\b")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
URL = re.compile(r"https?://\S+")
LOCATION_PHRASE = re.compile(
    r"\b(?:sections?|tables?|figures?|fig\.|pages?|pp?\.|chapters?|appendix|guidelines?|criteri(?:on|a)|items?|steps?|strands?|"
    r"questions?|rows?|lines?|part|parts|stages?|phases?|Q|F|S|E|G|B|V|R)\s*\d+(?:\.\d+)*(?:\s*(?:and|to|,|-)\s*\d+(?:\.\d+)*)*", re.IGNORECASE)
IDENTIFIER = re.compile(r"\b\d+(?:\.\d+)? of 20\b|\b\d+\.\d+\.\d+\b|\b[A-Z]{1,3}\d+[a-z]?\b|\bW\d{6,}\b|\bv\d+(?:\.\d+)+\b|\barXiv\s*\d+\.\d+|\b\d{4}-\d{2}-\d{2}\b|\b(?:19|20)\d\d\b")
FIGURE = re.compile(r"\d")
WHERE = re.compile(r"\b(?:abstract|introduction|results?|sections?|tables?|figures?|pages?|chapters?|appendix|methods?|conclusions?|"
                   r"discussion|full text|text|secondary)\b", re.IGNORECASE)


def units(text: str) -> list[tuple[int, str]]:
    """Each statement of the file as (first line, joined text): list items with their continuation, rows, paragraphs."""
    found, current = [], None
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or HEADING.match(line) or re.match(r"^\s*\|?\s*:?-{2,}", line):
            current = None
            continue
        item = re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line)
        if current is not None and line.startswith((" ", "\t")) and not item:
            found[current] = (found[current][0], found[current][1] + " " + line.strip())
            continue
        found.append((number, re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", line.strip())))
        current = len(found) - 1
    return found


def figures_of(statement: str) -> list[str]:
    text = URL.sub(" ", LINK.sub(r"\1", statement))
    text = KEY.sub(" KEY ", text)
    text = LOCATION_PHRASE.sub(" ", text)
    text = IDENTIFIER.sub(" ", text)
    return re.findall(r"\d[\d,.]*\d|\d", text)


def traced(statement: str) -> tuple[bool, bool]:
    """(has a key, a key is followed by a location word or 'secondary' or the statement says secondary)."""
    text = LINK.sub(r"\1", statement)
    keys = list(KEY.finditer(text))
    if not keys:
        return False, False
    if re.search(r"\(secondary\)|\bsecondary\b", text, re.IGNORECASE):
        return True, True
    for group in re.findall(r"\(([^()]*)\)", text):
        if WHERE.search(group) or re.search(r"\bread\b", group):
            return True, True
    for match in keys:
        if WHERE.search(text[match.end():match.end() + 60].split(")")[0]):
            return True, True
    return True, False


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for folder in review_folders(root, config):
        path = f"{folder}/review.md"
        if not (root / path).is_file():
            continue
        text = read(root, path)
        opening = next((s.start for s in sections(text) if s.level == 2), 0)
        for number, statement in units(text):
            if number < opening:
                continue
            numbers = figures_of(statement)
            if not numbers:
                continue
            has_key, has_where = traced(statement)
            shown = ", ".join(numbers[:3])
            if not has_key:
                findings.append(Finding(NAME, path, number, f"the figure {shown} has no source key (Surname Year)", "warning"))
            elif not has_where:
                findings.append(Finding(NAME, path, number, f"the figure {shown} says neither where it was read nor (secondary)", "warning"))
    return findings
