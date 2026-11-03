# Shape: frame

Step 1 of a review. Its reader is whoever must trust or continue the review, and asks: what is the problem, and what does the field call it? It fixes the words every other file uses. It is a page.

## Skeleton

```markdown
# Frame: <the problem and its names>

<Step 1 of the review, read on <date>. It states the problem, gives the field's names beside the practitioners', and says whether the repository's name matches.>

**Shape:** [frame](<path to shapes/frame.md>)

## The problem in one sentence

<One sentence: the problem, in your own words.>

## What the field calls it

| Level | The field's name | First met in |
|---|---|---|
| <the level> | **<name>**, <acronym> | <Author Year> |

## What practice calls it

- <The practitioners' word>: <what it is, and the field's word for it>.

## Does the repository's name match?

- <Yes or no, and what follows. The name is not changed here; the maintainer decides.>

## Sub-questions

| Question | Strand in review.md |
|---|---|
| <Q1> | <strand> |

## Held elsewhere

- <What a neighbour holds, linked, not repeated.>
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| The problem in one sentence | the method: you cannot search for what you cannot name | convention, untested |
| The field's names, with acronyms and first source | an explicit objective or question (Page 2021, item 4); research questions typed before searching (Garousi 2019, guidelines 4 and 5) | convention, by consensus |
| What practice calls it | the practitioners' word beside the field's: Garousi 2019 motivates grey sources by practice running ahead of research | convention |
| Does the name match | the finding is stated, never acted on by the review | convention, untested |
| Sub-questions with their strand | each question has the strand that answers it, so a reader finds the answer | convention, untested |

## Worked example

- Ours, small and complete: [second-reader/frame.md](examples/second-reader/frame.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/frame.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/frame.md).

## The rules

1. One sentence states the problem; the field's names come in a table, one level per row.
2. Every name the later files use is defined here first, in bold, once.
3. The frame never renames the repository; it reports whether the name matches.
4. Each sub-question points to the strand of review.md that answers it.

## The principles it applies

| Part | Principle |
|---|---|
| The problem first | [overview first](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/document/overview-first.md) |
| Every term defined once | [define before use](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/document/define-before-use.md) |
| One name per thing, across the files | [names predict content](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/names-predict-content.md) |

## Checked by

`review-files` (exact): the file exists. `shape-conformance` (exact), declared in `checks/config.toml`: a frame holds the headings The problem in one sentence, What the field calls it, What practice calls it, Does the repository's name match, and Sub-questions. Whether the names are the field's is judgment.
