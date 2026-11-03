"""Review files: a review folder holds the nine files of the genre, each once.

A review is a folder that `[review] roots` matches. It holds frame, protocol, sources, review, against, state-of-the-art,
position and baseline as markdown files, and its references: a `references.md` beside them, or the repository's one
`bibliography.md` in the folder above (one place per fact, so a repository may keep a single list for all its reviews).

A run with no error guarantees, for every such folder: the eight files exist, and so does the list of references. It
does not guarantee that a file holds what its shape asks (the other checks read some of that; the rest is judgment).
Time O(files).
"""
from __future__ import annotations

import posixpath
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _review import FILES, REFERENCES, review_folders  # noqa: E402
from framework.check_api import Finding, files_in_scope  # noqa: E402

NAME = "review-files"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    present = set(files_in_scope(root, config, {".md"}))
    findings = []
    for folder in review_folders(root, config):
        for name in FILES:
            if f"{folder}/{name}.md" not in present:
                findings.append(Finding(NAME, folder, 1, f"the review has no {name}.md"))
        shared = posixpath.join(posixpath.dirname(folder), "bibliography.md")
        if f"{folder}/{REFERENCES}.md" not in present and shared not in present:
            findings.append(Finding(NAME, folder, 1, f"the review has no {REFERENCES}.md, and no bibliography.md in {posixpath.dirname(folder) or '.'}"))
    return findings
