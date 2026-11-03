"""Search record: protocol.md records every search string with its count.

A reader must be able to run the search again and compare. In protocol.md, a table with a column whose header names a
string (`String`, `String as run`, `Filter string`, `String or site`) lists the searches. Each row must give the string
and, in another cell, a count (a number) or say that it was not run. A row that counts several strings together
("4 strings") gives no count per string. A protocol with no such table records no search.

A run with no error guarantees, for every protocol.md of a review folder: it has the table, every row has a string and a
count, and no row hides several strings behind one count. It warns when the protocol never says what was not searched
or never states a stopping rule (Garousi 2019, guideline 8). It does not guarantee that the count is what the engine
returns (a script can re-run an OpenAlex string; this check does not go online). Time O(rows).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import read, review_folders, tables  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "search-record"
EXACT = True

NOT_RUN = re.compile(r"not run|not searched|n/a|failed|none|zero|no result|timed out|not returned|timeout", re.IGNORECASE)
SEVERAL = re.compile(r"\b(\d+)\s+(?:search\s+)?strings\b", re.IGNORECASE)
IDENTIFIER = re.compile(r"^(id|seed|n|no\.?|#)\b", re.IGNORECASE)


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
        for table in searches:
            findings += check_table(path, table)
        if not re.search(r"not searched", text, re.IGNORECASE):
            findings.append(Finding(NAME, path, 1, "the protocol never says what was not searched", "warning"))
        if not re.search(r"stopping|saturation|exhaust", text, re.IGNORECASE):
            findings.append(Finding(NAME, path, 1, "the protocol states no stopping rule", "warning"))
    return findings
