# Shape: state of the art

Step 3 of a review: for each question, who holds the record, by what method, measured how. Its reader asks what is the best that is known and what is merely the most used. The practice most adopted is kept apart from the best evidence, and an upper bound from a limit.

## Skeleton

```markdown
# State of the art

<Step 3 of the review. For each question, the best evidence, kept apart from the practice most adopted. Upper bounds (what was achieved) are kept apart from limits (what was shown not to work). Sources are in [review](review.md).>

**Shape:** [state of the art](<path to shapes/state-of-the-art.md>)

## Q1 <the question>

| Record | Holder | What it says | Grade |
|---|---|---|---|
| Best evidence | <Author Year> | <the result> | <grade> |
| Upper bound | <Author Year> | <what was achieved> | <grade> |
| Limit | <Author Year> | <what was shown not to work> | <grade> |
| Most adopted | <Author Year> | <what practice does> | <grade> |
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| A table per question | a record is the same set of columns each time, which a table shows | supported with caveat (tables for comparisons) |
| Best evidence apart from most adopted | formal evidence is thin where practitioners write much (Garousi 2019, Table 4, questions 2 and 7) | convention |
| Upper bounds apart from limits | the family's method: a result that improves one says nothing about the other | convention, untested |
| "none found" as a holder | an absence is a finding about the searches | convention |

## Worked example

- Ours, small and complete: [second-reader/state-of-the-art.md](examples/second-reader/state-of-the-art.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/state-of-the-art.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/state-of-the-art.md).

## The rules

1. One section per question of the frame, in its order.
2. Each table has the columns Record, Holder, What it says and Grade; the records are best evidence, upper bound, limit and most adopted, as many as the question has.
3. Holder is a key from the bibliography, or the words none found.
4. The best evidence and the most adopted are different rows, even when one source holds both.
5. A limit is a result, not an opinion.

## The principles it applies

| Part | Principle |
|---|---|
| A table per question | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/page/signal-the-structure.md) |
| The holder next to what it says | [figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/page/figure-next-to-its-text.md) |

## Checked by

`shape-conformance` (exact): a Q1 heading. That the holder is the right one is judgment.
