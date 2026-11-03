# Shape: sources

The pool, kept apart from the findings. Its reader asks: how many works were found, how many were kept, how far was each read, and how good is each grey one? It is the audit trail of the review: the flow in and out, one row per source.

## Skeleton

```markdown
# Sources: the pool

<N sources: n formal and n grey, read on <date>. A grey source below 10 of 20 is an example of practice only. Searches are in [protocol](protocol.md).>

**Shape:** [sources](<path to shapes/sources.md>)

## Flow

| Stage | Count |
|---|---|
| Strings run | <n> |
| Screened by title | <n> |
| Included, formal | <n> |
| Included, grey | <n> |
| Grey below 10 of 20, examples only | <n> |
| Read from the abstract (secondary) | <n> |
| Located only, not read | <n> |

## Formal

| Key | Kind | Found via | Grade or use | Used in |
|---|---|---|---|---|
| <Author Year> | <kind> | <string id, snowball, lead> | <grade; how far read> | <file> |

## Grey

Score is out of 20, then the groups in the order authority, methodology, objectivity, date, position, novelty, impact, outlet.

| Key | Kind and tier | Score | Groups | Note |
|---|---|---|---|---|
| <Author Year> | <kind, tier n> | <total> | <a, m, o, d, p, n, i, t> | <what the score rests on> |

## Left out, with the reason

- <What was found and not kept, and why.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| The flow, from strings to included | the flow diagram of the search and selection (Page 2021, item 16a); the same counts in a table | convention, by consensus |
| Studies left out, with the reason | item 16b (Page 2021) | convention, by consensus |
| One row per formal source with its grade | the evidence grades of the standard | convention |
| One row per grey source with a total and eight subtotals | the 20 criteria in eight groups (Garousi 2019, Table 7) | convention; reliability unmeasured |
| How far each source was read | a figure from an abstract is secondary; marking it lets a reader weigh it | convention, untested |
| A grey source below 10 of 20 is an example only | threshold 10 of 20, offered as an example (Garousi 2019, section 5.2) | convention |

## Worked example

- Ours, small and complete: [second-reader/sources.md](examples/second-reader/sources.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/sources.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/sources.md).

## The rules

1. The flow is a table of counts that the later tables add up to.
2. A grey row carries the total and the eight subtotals, in this order: authority, methodology, objectivity, date, position, novelty, impact, outlet. The subtotals add up to the total, within 4, 6, 4, 1, 1, 2, 1, 1.
3. A grey row below 10 says it is an example of practice only.
4. A work that is cited has a row; a work that was found and dropped is in the left-out list.
5. A second rater's score goes beside the first, with the reread that settled it; the agreement is in the protocol.

## The principles it applies

| Part | Principle |
|---|---|
| Tables for counts and for sources | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/page/signal-the-structure.md) |
| The pool stated before its use | [overview first](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/document/overview-first.md) |
| A source's facts in one row | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/one-place-per-fact.md) |

## Checked by

`grey-subtotals` (exact): each grey row has eight subtotals in range and in steps of 0.5, a total equal to their sum, and the words example or practice only under 10. `shape-conformance` (exact): the headings Flow, Formal, Grey and Left out. Whether the counts of the flow match the rows is judgment, and whether a score is right is the second rater's work.
