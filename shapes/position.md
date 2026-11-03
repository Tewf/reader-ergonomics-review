# Shape: position

Step 4 of a review: what is known, what was not found, and what this repository would ask. Its reader asks where the review ends and the work begins. It never confuses nobody has done this with we have not done this here.

## Skeleton

```markdown
# Position

<Step 4 of the review. What is known, what was not found, and what this repository asks. Each "not found" is a statement about these searches, not about the world. Terms are in [frame](frame.md).>

**Shape:** [position](<path to shapes/position.md>)

## Known

- <A finding, with its key.>

## Not found in these searches

- <What was looked for with which string and not found.>

## The questions

| Question | Answer from the evidence | Grade |
|---|---|---|
| <Q1> | <the answer> | <grade> |

## What this repository asks

- <A question the field does not answer.>

## What the shapes must decide

- <A decision the next work takes.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| Known, then not found | positioning: separate what the field has shown from what it has not | convention |
| "Not found" is about the searches | zero results is a statement about the query | convention |
| The questions answered in a table | the questions of the frame, each with a grade | convention |
| What the repository asks | the gap the work fills; never "nobody has done this" | convention |

## Worked example

- Ours, small and complete: [second-reader/position.md](examples/second-reader/position.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/position.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/position.md).

## The rules

1. Known lists findings with their keys; it adds nothing new.
2. Not found lists the string and the source that found nothing; each is about the searches.
3. The questions of the frame are answered in a table, each with a grade.
4. What the repository asks is a question, not a claim of novelty.
5. A decision for the next work goes in the last list.

## The principles it applies

| Part | Principle |
|---|---|
| The answer in a table | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/page/signal-the-structure.md) |
| Known before what is asked | [overview first](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/principles/document/overview-first.md) |

## Checked by

`shape-conformance` (exact): the headings Known, Not found, questions and What this repository asks. Whether a thing is really not found is judgment, and a second search by someone else.
