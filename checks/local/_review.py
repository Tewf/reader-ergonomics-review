"""Shared by the local checks: which folders are reviews, and how a review's markdown is read.

A review folder is a folder that `[review] roots` of checks/config.toml matches (globs on the folder's path, default
`evidence/*`) and that holds at least one of the review's files. The helpers below split a file into its headings
and tables, so each check reads a file the same way. This module has no NAME, so the runner loads it and skips it;
each check puts its folder on sys.path to import it.
"""
from __future__ import annotations

import fnmatch
import posixpath
import re
from pathlib import Path

from framework.check_api import FENCED_BLOCK, files_in_scope, prose_only

FILES = ["frame", "protocol", "sources", "review", "against", "state-of-the-art", "position", "baseline"]
REFERENCES = "references"
DEFAULT_ROOTS = ["evidence/*"]
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
NUMBER = r"\d+(?:\.\d+)?"


class Section:
    """A heading and its extent; `end` is the last line of the section, subsections included."""

    def __init__(self, level: int, title: str, start: int, end: int) -> None:
        self.level, self.title, self.start, self.end = level, title, start, end


class Table:
    """A pipe table: its header cells, its rows as (line number, cells), and the line it starts on."""

    def __init__(self, header: list[str], rows: list, start: int) -> None:
        self.header, self.rows, self.start = header, rows, start


def roots(config: dict) -> list[str]:
    return config.get("review", {}).get("roots", DEFAULT_ROOTS)


def review_folders(root: Path, config: dict) -> list[str]:
    """The folders (POSIX paths from root) that are reviews."""
    folders = {}
    for path in files_in_scope(root, config, {".md"}):
        folder, name = posixpath.split(path)
        stem = name[:-3]
        if folder and (stem in FILES or stem == REFERENCES) and any(fnmatch.fnmatch(folder, pattern) for pattern in roots(config)):
            folders.setdefault(folder, set()).add(stem)
    return sorted(folders)


def read(root: Path, path: str, inline: bool = False) -> str:
    """The file with fenced blocks blanked; inline code too, unless `inline` keeps it (a search string is often in backticks)."""
    text = (root / path).read_text(encoding="utf-8", errors="replace")
    if inline:
        return FENCED_BLOCK.sub(lambda match: "\n" * match.group(0).count("\n"), text)
    return prose_only(text)


def sections(text: str) -> list[Section]:
    lines = text.splitlines()
    found = []
    for number, line in enumerate(lines, 1):
        match = HEADING.match(line)
        if match:
            found.append(Section(len(match.group(1)), match.group(2), number, len(lines)))
    for index, section in enumerate(found):
        for later in found[index + 1:]:
            if later.level <= section.level:
                section.end = later.start - 1
                break
    return found


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", line))


def tables(text: str, first: int = 1, last: int | None = None) -> list[Table]:
    """The pipe tables between two lines: a header row, a separator, then rows."""
    lines = text.splitlines()
    last = last or len(lines)
    found, index = [], first - 1
    while index < last - 1:
        if lines[index].strip().startswith("|") and index + 1 < len(lines) and is_separator(lines[index + 1]):
            table = Table(cells(lines[index]), [], index + 1)
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|") and index < last:
                table.rows.append((index + 1, cells(lines[index])))
                index += 1
            found.append(table)
        else:
            index += 1
    return found


def lines_of(text: str, first: int, last: int) -> list[tuple[int, str]]:
    return [(number, line) for number, line in enumerate(text.splitlines(), 1) if first <= number <= last]
