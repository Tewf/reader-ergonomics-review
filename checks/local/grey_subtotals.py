"""Grey subtotals: each grey source in sources.md carries Garousi 2019's eight subtotals and a total that adds up.

Garousi, Felderer and Mantyla (2019, Table 7) grade a grey source on 20 criteria in eight groups: authority 4,
methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet type 1. In sources.md, under a heading
that names the grey sources, each row of a table that has a Score, Subtotals or Groups column is one source. Its row
must hold, in the order above, eight numbers separated by commas or slashes (or the same eight with the letters
A M O D P N I T before them), and a total: after the word `final`, or before a colon that precedes the eight, or the
first number of the Score column; `18.5 of 20` also gives it. Rows that say `not scored`, `located only` or `method of this review` are exempt.

A run with no error guarantees, for every grey row: the eight subtotals are there, each within its group's maximum and a
multiple of 0.5, they add up to the total, and a total under 10 (the family's threshold, Garousi's own example) says
the source is an example of practice only. It does not guarantee that a subtotal is the right one (that is judgment,
and the second rater's work). Time O(rows).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import NUMBER, read, review_folders, sections, tables  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "grey-subtotals"
EXACT = True

GROUPS = ["authority", "methodology", "objectivity", "date", "position", "novelty", "impact", "outlet"]
MAXIMA = [4, 6, 4, 1, 1, 2, 1, 1]
THRESHOLD = 10
BARE = re.compile(rf"(?<![\d.])({NUMBER})(?:\s*[,/]\s*({NUMBER})){{7}}(?![\d])")
LABELLED = re.compile(r"\bA\s+(NUM)[,;]?\s*M\s+(NUM)[,;]?\s*O\s+(NUM)[,;]?\s*D\s+(NUM)[,;]?\s*P\s+(NUM)[,;]?\s*N\s+(NUM)[,;]?\s*I\s+(NUM)[,;]?\s*T\s+(NUM)".replace("NUM", NUMBER))
EXEMPT = re.compile(r"not scored|located only|method of this review|not opened", re.IGNORECASE)
EXAMPLE = re.compile(r"example|practice only|below|not used|excluded|dropped", re.IGNORECASE)
GREY_HEADING = re.compile(r"^(?!.*(?:flow|search|quer|string|producer|left out)).*(?:grey|gray)", re.IGNORECASE)


def eight(row: str) -> tuple[list[float], int] | None:
    """The first eight subtotals of a row, and the offset where they start."""
    match = LABELLED.search(row)
    if match:
        return [float(value) for value in match.groups()], match.start()
    match = BARE.search(row)
    if match:
        return [float(value) for value in re.findall(NUMBER, match.group(0))], match.start()
    return None


def total_of(row: str, before: str, score_cell: str) -> float | None:
    final = re.search(rf"\bfinal\s+({NUMBER})", row, re.IGNORECASE)
    if final:
        return float(final.group(1))
    of_twenty = re.search(rf"({NUMBER})\s+of\s+20\b", row)
    if of_twenty:
        return float(of_twenty.group(1))
    colon = re.search(rf"({NUMBER})\s*:\s*$", before)
    if colon:
        return float(colon.group(1))
    first = re.search(NUMBER, score_cell)
    return float(first.group(0)) if first else None


def check_row(path: str, line: int, header: list[str], cells: list[str]) -> list[Finding]:
    row = " | ".join(cells)
    if EXEMPT.search(row):
        return []
    key = cells[0] if cells else "?"
    found = eight(row)
    if not found:
        return [Finding(NAME, path, line, f"{key}: no eight subtotals (authority, methodology, objectivity, date, position, novelty, impact, outlet)")]
    values, start = found
    score_column = next((i for i, name in enumerate(header) if "score" in name.lower() and i < len(cells)), None)
    total = total_of(row, row[:start], cells[score_column] if score_column is not None else "")
    findings = []
    if total is None:
        return [Finding(NAME, path, line, f"{key}: the eight subtotals have no total")]
    if abs(sum(values) - total) > 0.01:
        findings.append(Finding(NAME, path, line, f"{key}: the subtotals add up to {sum(values):g}, the total says {total:g}"))
    for value, maximum, group in zip(values, MAXIMA, GROUPS):
        if value > maximum or value < 0 or (value * 2) % 1:
            findings.append(Finding(NAME, path, line, f"{key}: {group} {value:g} is not a multiple of 0.5 within 0 to {maximum}"))
    if total < THRESHOLD and not EXAMPLE.search(row):
        findings.append(Finding(NAME, path, line, f"{key}: scores {total:g}, under {THRESHOLD}: say it is an example of practice only"))
    return findings


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for folder in review_folders(root, config):
        path = f"{folder}/sources.md"
        if not (root / path).is_file():
            continue
        text = read(root, path, inline=True)
        for section in (s for s in sections(text) if GREY_HEADING.search(s.title)):
            graded = [t for t in tables(text, section.start, section.end)
                      if re.search(r"score|subtotal|groups|quality", " ".join(t.header), re.IGNORECASE)]
            rows = [r for t in graded for r in t.rows]
            if not graded:
                findings.append(Finding(NAME, path, section.start, f"'{section.title}' has no table with a Score, Subtotals or Groups column"))
            for table in graded:
                for line, cells in table.rows:
                    findings += check_row(path, line, table.header, cells)
            if graded and not rows:
                findings.append(Finding(NAME, path, section.start, f"'{section.title}' lists no grey source"))
    return findings
