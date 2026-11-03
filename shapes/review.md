# Shape: review

Step 2 of a review: the findings, by strand, surveys first. Its reader asks what the sources say on each question, with how much confidence. Every finding states its figure, its source and where it was read.

## Skeleton

```markdown
# Review: <n strands>

<Step 2 of the review, read on <date>. It groups the N sources by strand and answers Q1 to Qn of [frame](frame.md). Surveys first in each strand.>

**Shape:** [review](<path to shapes/review.md>)

- Each key is in the [bibliography](<path>).
- Grades are the standard's four.
- A figure read in an abstract is marked (secondary).

## Strand 0: existing reviews

- <A finding, with its figure (Author Year, where it was read). Grade.>

## Strand 1: <name> (Q1)

- <A finding, with its figure (Author Year, abstract, secondary). Grade.>
- <No study of X was found (protocol, string F3). Not found, in these searches.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| Strands by question, surveys first | the order of a literature review: existing reviews, then the primary works | convention |
| One finding per line | one idea per line; signalling by lists | measured for signals (the standard's signal-the-structure) |
| Every figure with a key and a place | item 17 (Page 2021): each included study cited with its characteristics | convention, by consensus |
| (secondary) on a figure read in a summary | the family's rule: a figure read in an abstract is secondary | convention |
| A grade on each finding | the four grades of the standard | convention |
| "Not found, in these searches" | an absence is a statement about the query | convention |

## Worked example

- Ours, small and complete: [second-reader/review.md](examples/second-reader/review.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/review.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/review.md).

## The rules

1. Strand 0 is the existing reviews; the other strands answer the questions of the frame, in its order.
2. One finding per line: the claim, then the figure with (Author Year, where), then the grade.
3. A figure read in an abstract or a summary says (secondary).
4. An absence is written "not found, in these searches", with the string that found nothing.
5. The opening before the first section counts the review itself and is not read for figures.
6. Evidence against a finding goes to against, never deleted from here.

## The principles it applies

| Part | Principle |
|---|---|
| One finding per line, in lists | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/page/signal-the-structure.md) |
| The question answered at the head of each strand | [overview first](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/document/overview-first.md) |
| A figure beside the words that explain it | [figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/page/figure-next-to-its-text.md) |

## Checked by

`review-numbers` (heuristic, a warning): a line with a figure holds a source key and, near it, a location or the word secondary. `shape-conformance` (exact): a Strand 0 heading. Whether a figure is what the source says is checked by reading the source again.
