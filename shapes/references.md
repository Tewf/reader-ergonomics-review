# Shape: references

Every work a review cites, once, with a stable link. Its reader is a person or a script that resolves a citation. A repository may keep one list for all its reviews.

## Skeleton

```markdown
# Bibliography

<Every work cited, once. A key is `Surname Year`. The note after a citation says how far the work was read.>

**Shape:** [references](<path to shapes/references.md>)

| Key | Citation | Link |
|---|---|---|
| <Surname Year> | <Authors (year). Title. Venue. Abstract read> | <DOI, arXiv id or stable URL> |
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| A key of `Surname Year` | one work, one key, across the family | convention |
| A DOI, arXiv id or stable URL | a script can resolve it | convention |
| How far it was read | a figure from an abstract is secondary | convention, untested |
| One list for the repository | each citation has one entry | supported with caveat |

## Worked example

- Ours, small and complete: [second-reader/references.md](examples/second-reader/references.md).
- In the family, at their pinned commits: [the project's bibliography](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/bibliography.md) and [the agents' bibliography](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/bibliography.md).

## The rules

1. One row per work, three columns: Key, Citation, Link.
2. A key is `Surname Year`, one letter after the year at most; an organisation takes a title word after the year.
3. The link is a DOI, an arXiv id or a stable URL; a work reachable only with an identity is marked unverifiable.
4. The list is kept in the review's folder as `references.md`, or once for the repository as `evidence/bibliography.md`; the folder then needs no copy.

## The principles it applies

| Part | Principle |
|---|---|
| Keys that name one work | [names predict content](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/names-predict-content.md) |
| The list kept once | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/one-place-per-fact.md) |

## Checked by

`review-files` (exact): the folder has a `references.md`, or the repository a `bibliography.md` above it. The standard's `citations`, `bibliography-keys` and `references` checks read the list.
