# 0002: References may be one list for the repository

**Decision:** a review has nine files, and the ninth, its references, is either a `references.md` in the review's folder or the repository's one `evidence/bibliography.md`; the check accepts both.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/shapes/decision-record.md).

## Context

- The maintainer's contract for a review names nine files, the last of them `references.md`.
- The nine reviews of the family keep none. Each repository holds one `evidence/bibliography.md` that all its reviews cite, and the standard's `citations` and `bibliography-keys` checks read that file.
- A file on disk and a contract disagree. The family's rule is that the repository wins over a stale instruction.

## Decision

- The ninth file is the list of references. Its place is the review's folder, or the repository's one bibliography in the folder above.
- `review-files` fails a review that has neither.
- The [references shape](../shapes/references.md) describes both.

## Options

| Option | Why it lost, or won |
|---|---|
| A `references.md` in every review folder | lost: it copies a work's row into each folder, so one fact lives in two places, and the standard's checks read the one list |
| Only the shared bibliography | lost: a repository with one review would have a folder without its ninth file |
| Either, as chosen | won: it matches the nine reviews as they are, and costs a repository nothing |

## Consequences

- **Good:** the nine reviews pass `review-files` as they stand.
- **Bad:** a reader of a review folder alone does not see its references; the shape says where to look.
- **To keep it true:** a review that moves to another repository takes its rows with it.

## See also

[Decisions](README.md); the [references shape](../shapes/references.md); [the check](../checks/README.md).
