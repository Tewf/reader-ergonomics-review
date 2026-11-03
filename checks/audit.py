"""Run this repository's review checks on any repository, read-only: `python3 checks/audit.py ROOT [--roots GLOB ...]`.

It needs the standard's checks importable (the same locations as the tests: READER_ERGONOMICS_CHECKS, checks/out/standard,
or reader-ergonomics beside this repository). It prints each finding and a count per check, and changes nothing in ROOT.
"""
import importlib.util
import os
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
sys.path.insert(0, str(REPOSITORY / "checks" / "local"))


def load_checks():
    modules = []
    for path in sorted((REPOSITORY / "checks" / "local").glob("*.py")):
        if path.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    return modules


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    root, roots = Path(argv[0]).resolve(), []
    rest = argv[1:]
    while rest:
        if rest[0] == "--roots":
            roots.append(rest[1])
            rest = rest[2:]
        else:
            rest = rest[1:]
    config = {"review": {"roots": roots}} if roots else {}
    counts = Counter()
    for module in load_checks():
        for finding in module.check(root, config):
            counts[finding.check] += 1
            print(f"{finding.check}: {finding.path}:{finding.line}: {finding.message}")
    print(dict(counts) or "no finding")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
