# Shape: against

The evidence against what the review assumes, and the disagreements among its sources. Its reader asks what would change the answer. Nothing is deleted to make the claim look stronger; this file is the review's guard against that.

## Skeleton

```markdown
# Against

<The evidence against what the front page assumes, and the disagreements. Sources are in [review](review.md). None is deleted to make the subject look stronger.>

**Shape:** [against](<path to shapes/against.md>)

## Against "<a claim of the front page>"

- <Evidence against it (Author Year, where). Grade.>

## Disagreements

| Point | One side | Other side |
|---|---|---|
| <the point> | <a result (Author Year)> | <a result (Author Year)> |

- <A possible reason for the split, as a hypothesis.>

## Against the sources themselves

- <Preprints, small samples, one group, abstracts only, vendor pages.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| A section per claim, titled with the claim | limitations of the evidence (Page 2021, item 23b) | convention, by consensus |
| A table of disagreements | tables for comparisons help; the point and its two sides in columns | supported with caveat |
| Against the sources themselves | limitations of the evidence and of the review process (Page 2021, items 23b and 23c) | convention, by consensus |
| Keep what contradicts | reporting bias: leaving out results that disagree biases a review (Hopewell 2007 for grey sources) | measured for grey sources, by analogy elsewhere |

## Worked example

- Ours, small and complete: [second-reader/against.md](examples/second-reader/against.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/against.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/against.md).

## The rules

1. One section per claim of the front page that the evidence contradicts, titled with the claim in quotation marks.
2. A disagreement is a table: the point, one side, the other, each with its source.
3. A possible reason for a split is written as a possibility.
4. The last section judges the sources: their kind, size, venue and how far they were read.
5. A result against the claim is not removed when the review changes; it is moved here.

## The principles it applies

| Part | Principle |
|---|---|
| The claim as the heading | [names predict content](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/collection/names-predict-content.md) |
| Disagreements as a table | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/page/signal-the-structure.md) |

## Checked by

`shape-conformance` (exact): the headings Against, Disagreements and Against the sources themselves. Whether the evidence is the strongest against is judgment.
