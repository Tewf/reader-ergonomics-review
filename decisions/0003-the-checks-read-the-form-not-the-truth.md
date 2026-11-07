# 0003: The checks read the form, not the truth

**Decision:** the five review checks decide only what a program can decide exactly: which files exist, whether subtotals add up, whether a string has a count. The truth of a score, a figure or a search stays with a reader.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/shapes/decision-record.md).

## Context

- The maintainer's rule: what a program can check, a program checks; a model is asked only what no program can decide, and never reviews its own output in place of the checks.
- The nine reviews were written by a model under a contract and spot-checked by the maintainer. Their errors were of form (a total that did not add up, a score under the threshold not labelled) and of content (a number misread).
- The review of the genre found no program that checks a review's report; the standard-setting body's own checker is in development ([review, strand 5](../evidence/review-genre/review.md)).

## Decision

- Four checks are exact and fail a run: `review-files`, `grey-subtotals`, `search-record` and `second-rater`.
- `review-numbers` is a heuristic and warns, since whether a figure needs a source depends on its role.
- No check goes online or asks a model. A claim that a figure is what its source says stays a reading.
- `checks/audit.py` runs them on another repository, read-only.

## Options

| Option | Why it lost, or won |
|---|---|
| A model reads each review for fit to its shape | lost: a wrong verdict would not be obvious, and a model's verdict would stand in for the checks |
| Check each figure against its source online | lost: it needs an identity at some services, and a paper's abstract is not always open |
| Form only, by program | won: it costs nothing, runs on every push, and is exact where it speaks |

## Consequences

- **Good:** a review that passes has its files, its arithmetic, its counts and its agreement report, and says so by exit code.
- **Bad:** a review can pass and still be wrong; the checks say nothing of a subtotal's rightness.
- **To keep it true:** a new check names its principle, and a principle names a check or says what is judgment.

## See also

[Decisions](README.md); [the checks](../checks/README.md); [the principles](../principles/README.md).
