# Shape: baseline

Step 5 of a review: the baseline the work is compared against, named. The review is finished when it can name it. Its reader asks what to compare with and by what measure.

## Skeleton

```markdown
# Baseline

<Step 5 of the review: the baseline the work is compared against. Evidence is in [review](review.md).>

**Shape:** [baseline](<path to shapes/baseline.md>)

## B1: <the baseline, named>

<What it is, in a few numbered lines.>

## Compared with what the review found

| Item | In B1 | Fit |
|---|---|---|
| <what the evidence asks> | <what B1 does> | <matches, in part, lacks> |

## What B1 lacks

- <A gap, with the finding that shows it.>

## How it is measured

- <The measure, and what is counted.>

## The review is finished

<One sentence: the baseline is named, and what comes next.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| A named baseline | a method with no baseline cannot be shown to be worth anything | convention |
| Compared item by item with the evidence | the comparator in a review's question (Page 2021, item 4) | convention |
| What B1 lacks | limitations of the review process (Page 2021, item 23c) | convention, by consensus |
| How it is measured | a count a program can repeat | convention |
| The sentence that closes the review | the review is finished only when it names its baseline | convention, untested |

## Worked example

- Ours, small and complete: [second-reader/baseline.md](examples/second-reader/baseline.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/baseline.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/baseline.md).

## The rules

1. The baseline gets a name (B1) and a description in numbered lines.
2. The comparison is a table with the columns Item, In B1 and Fit.
3. The gaps are listed with the finding that shows each.
4. The measure is something that can be repeated.
5. The last sentence says the baseline is named.

## The principles it applies

| Part | Principle |
|---|---|
| The baseline first | [overview first](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/document/overview-first.md) |
| The comparison as a table | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/page/signal-the-structure.md) |

## Checked by

`shape-conformance` (exact): the headings Compared with, lacks, measured and finished. That the baseline is the right one to compare with is judgment.
