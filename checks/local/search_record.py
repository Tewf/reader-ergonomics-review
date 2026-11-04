"""Search record: protocol.md records every search string with its count.

A reader must be able to run the search again and compare. In protocol.md, a table with a column whose header names a
string (`String`, `String as run`, `Filter string`, `String or site`) lists the searches. Each row must give the string
and, in another cell, a count (a number) or say that it was not run. A row that counts several strings together
("4 strings") gives no count per string. A protocol with no such table records no search.

A run with no error guarantees, for every protocol.md of a review folder: it has the table, every row has a string and a
count, and no row hides several strings behind one count. It warns when the protocol never says what was not searched
or never states a stopping rule (Garousi 2019, guideline 8). It does not guarantee that the count is what the engine
returns (a script can re-run an OpenAlex string; this check does not go online). Time O(rows).

Concepts per result. Each such table also needs one column whose header names a concept (`New concept`); each row holds,
in the order the results were screened, one letter per result: y if it added a concept, n if not (`ynnyn`), or the words
not run. When the search tool returns a synthesis and not a list of results, there is nothing to letter: the cell may
say `not recorded`, with a one-line reason in the protocol's Limits section (a line `Not recorded: <reason>`). That is
accepted without a finding: a reason in the cell (`not recorded: ...`, `, ...` or `(...)`) or on that line answers it.
`not recorded` with no reason anywhere is a malformed cell.
Without it no stopping estimator can judge the search (ai-augmented-data-gathering, on-the-family). A missing
column or a malformed cell is an error in a protocol dated on or after 2026-11-04 and a warning before it, so the nine
reviews written earlier are flagged and not failed. The protocol's date is the first ISO date in its text; a protocol
with none counts as written before.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import read, review_folders, sections, tables  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "search-record"
EXACT = True

NOT_RUN = re.compile(r"not run|not searched|n/a|failed|none|zero|no result|timed out|not returned|timeout", re.IGNORECASE)
SEVERAL = re.compile(r"\b(\d+)\s+(?:search\s+)?strings\b", re.IGNORECASE)
CONCEPT_CELL = re.compile(r"^[yn][yn ,]*$", re.IGNORECASE)
ISO_DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
CONCEPT_FROM = "2026-11-04"
NOT_RECORDED = re.compile(r"^not recorded\b", re.IGNORECASE)
INLINE_REASON = re.compile(r"^not recorded\s*[:,(]\s*\S", re.IGNORECASE)
REASON = re.compile(r"not recorded\s*[:;,.\-]\s*(\S.*)", re.IGNORECASE)
IDENTIFIER = re.compile(r"^(id|seed|n|no\.?|#)\b", re.IGNORECASE)


def limits_reason(text: str) -> str | None:
    """The reason given on a `Not recorded:` line under a heading that names the limits, or None."""
    lines = text.splitlines()
    for section in sections(text):
        if "limit" in section.title.lower():
            found = REASON.search("\n".join(lines[section.start:section.end]))
            if found:
                return found.group(1).strip()
    return None


def check_concepts(path: str, table, kind: str, reason: str | None = None) -> list[Finding]:
    """The concept column of a search table: present, and a y/n sequence or a stated failure on each row."""
    column = next((i for i, name in enumerate(table.header) if "concept" in name.lower()), None)
    if column is None:
        return [Finding(NAME, path, table.start, "the table of strings has no column of concepts per result (New concept)", kind)]
    findings = []
    for line, cells in table.rows:
        cell = cells[column].strip() if column < len(cells) else ""
        if NOT_RECORDED.match(cell):
            if INLINE_REASON.match(cell) or reason:
                continue  # answered: the reason is in the cell or on the Limits line
            else:
                findings.append(Finding(NAME, path, line, "the concept cell says not recorded, with no reason on a 'Not recorded:' line in the Limits section", kind))
        elif not (CONCEPT_CELL.match(cell) or NOT_RUN.search(cell)):
            findings.append(Finding(NAME, path, line, "the concept cell is not a y/n sequence over the results screened, nor not run", kind))
    return findings


def check_table(path: str, table) -> list[Finding]:
    column = next(i for i, name in enumerate(table.header) if "string" in name.lower())
    findings = []
    for line, cells in table.rows:
        if column >= len(cells) or not cells[column].strip(" -"):
            findings.append(Finding(NAME, path, line, "a search row with no string"))
            continue
        row = " | ".join(cells)
        several = SEVERAL.search(row)
        if several and int(several.group(1)) > 1:
            findings.append(Finding(NAME, path, line, f"{several.group(1)} strings under one count: give each string its own row"))
            continue
        others = [cell for i, cell in enumerate(cells) if i != column and not (i == 0 and IDENTIFIER.match(table.header[0]))]
        if not any(re.search(r"\d", cell) or NOT_RUN.search(cell) for cell in others):
            findings.append(Finding(NAME, path, line, f"the string '{cells[column][:40]}' has no count"))
    return findings


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for folder in review_folders(root, config):
        path = f"{folder}/protocol.md"
        if not (root / path).is_file():
            continue
        text = read(root, path, inline=True)
        searches = [t for t in tables(text) if any("string" in name.lower() for name in t.header)]
        if not searches:
            findings.append(Finding(NAME, path, 1, "no table of search strings (a column named String) with a count for each"))
        dated = ISO_DATE.search(text)
        kind = "error" if dated and dated.group(1) >= CONCEPT_FROM else "warning"
        reason = limits_reason(text)
        for table in searches:
            findings += check_table(path, table)
            findings += check_concepts(path, table, kind, reason)
        if not re.search(r"not searched", text, re.IGNORECASE):
            findings.append(Finding(NAME, path, 1, "the protocol never says what was not searched", "warning"))
        if not re.search(r"stopping|saturation|exhaust", text, re.IGNORECASE):
            findings.append(Finding(NAME, path, 1, "the protocol states no stopping rule", "warning"))
    return findings
