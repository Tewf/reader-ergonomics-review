# Shape: protocol

How the pool was built, so that a reader can run the search again. Its reader is a reviewer or a program that asks: what was searched, with which string, how many came back, when was it stopped, and what was left out? It is the file most guidelines ask for.

## Skeleton

```markdown
# Protocol: how the pool was built

<A first pass, run on <date> by <n> reviewers. Terms are in [frame](frame.md).>

**Shape:** [protocol](<path to shapes/protocol.md>)

## 1. Why grey literature

<Garousi's seven questions (Table 4), answered for this topic.>

## 2. Questions

- Q1 <the question>

## 3. Existing reviews

- Found: <reviews already on the topic>. Not found: <what no review covers>.

## 4. Formal search

<Database, field searched, identity sent (none), date of the counts.>

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | <the string, exactly> | <n> | <one letter per result screened, in order: y if it added a concept, n if not; `ynnyn`> |

## 5. Grey search

| Id | Producer or engine | String or what was read | Result | New concept |
|---|---|---|---|---|
| G1 | <where> | <string or page> | <screened, included> | <y or n per result, in order> |

## 6. Stopping rule

- <Effort bounded, saturation or evidence exhaustion, with N or k, stated before the search.>

## 7. Selection

- Include: <criterion>. Exclude: <criterion>.

## 8. Quality of grey sources

<The 20 criteria of Garousi 2019, Table 7, in eight groups; the threshold.>

## 9. Extraction and synthesis

<What was read, how far, how a figure is marked, how the synthesis was done.>

## 10. Not searched, and limits

- Not searched: <what>. Limits: <reviewers, dates, engines>.
- Not recorded: <one-line reason>. Only when a search tool returns a synthesis and not a list of results; the New concept cells then say `not recorded`.
```

## Where each part comes from

| Part | Evidence | Grade |
|---|---|---|
| Why grey literature | seven yes/no questions to decide (Garousi 2019, Table 4) | convention |
| Questions | explicit objectives (Page 2021, item 4); guideline 4 and 5 (Garousi 2019) | convention, by consensus |
| Existing reviews first | guideline 2 (Garousi 2019) | convention |
| Every string with its count and date | item 7 and item 6 (Page 2021); the 16 items of PRISMA-S (Rethlefsen 2021) | convention, by consensus |
| The stopping rule, stated before | guideline 8: saturation, effort bounded or evidence exhaustion (Garousi 2019) | convention |
| Selection criteria | item 5 (Page 2021); guidelines 9 and 10 (Garousi 2019) | convention |
| The grey score | Table 7 and section 5.2 (Garousi 2019) | convention; reliability unmeasured |
| How many reviewers, independently | item 8 (Page 2021); the evidence for a second reader (Edwards 2002; Waffenschmidt 2019) | measured for screening in health |
| What was not searched | limits of the review process (Page 2021, item 23c) | convention |
| A letter per result screened: did it add a concept | a stopping estimator needs the new concepts of each result; no log of the family held them ([log concepts per result](../principles/record/log-concepts-per-result.md)) | supported with caveat |
| The forward pass and the second rater, as later sections | snowballing found more than the protocol's searches (Greenhalgh 2005; Wohlin 2022) | measured, descriptive |

## Worked example

- Ours, small and complete: [second-reader/protocol.md](examples/second-reader/protocol.md).
- In the family, at their pinned commits: [human-ai-teaming](https://github.com/Tewf/ai-augmented-project/blob/cf2216058daf3e2ccd82328864ac4d3ff6de2ced/evidence/human-ai-teaming/protocol.md) and [multi-agent-teams](https://github.com/Tewf/ai-augmented-agents/blob/8a05e7eb88a41cfb53c8188fc9faacac94e79d02/evidence/multi-agent-teams/protocol.md).

## The rules

1. One row per string, as run, with the database and the date of the count; a string that failed says so (`timed out`, `not run`).
2. A row never counts several strings together.
3. The stopping rule is stated before the search and applied.
4. The protocol says what was not searched, and names its limits.
5. Each search table has a column New concept: one letter per result screened, in order, y if it added a concept and n if not, or the words not run. A tool that returns a synthesis gives no list to letter: the cell says `not recorded`, and the Limits section gives the reason in one line.
6. A later pass (forward citations, a second rater) is a numbered section of its own; a second rater's section reports the agreement.
7. Identity is not sent to any service; a source reachable only that way is called unverifiable.

## The principles it applies

| Part | Principle |
|---|---|
| Strings in a table, counts beside | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/page/signal-the-structure.md) |
| Numbered sections in the order of the work | [define before use](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/document/define-before-use.md) |
| Nothing repeated from the guidelines | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/principles/collection/one-place-per-fact.md) |

## Checked by

- `search-record` (exact): a table with a String column, a count or a stated failure on each row, and no row for several strings. It warns when the protocol never says what was not searched or states no stopping rule.
- `search-record` also asks the New concept column: an error in a protocol dated 2026-11-04 or later, a warning before. A cell saying `not recorded` is accepted with a warning that names the reason given in the Limits section, never an error; with no reason it is a malformed cell.
- `second-rater` (exact): a second-rater section reports an agreement.
- `shape-conformance` (exact): the ten headings.
- That the count is what the engine returns is checked by running the search again, not here.
