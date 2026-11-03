# Protocol: how the pool was built

A cut of the full review's protocol, run on 2026-11-03 by one reviewer. Terms are in [frame](frame.md).

**Shape:** [protocol](../../protocol.md)

## 1. Why grey literature

Garousi's seven questions: one yes suggests including grey sources.

| Question | Answer |
|---|---|
| Is there a lack of volume or quality in the formal literature on this point? | yes: the standard-setters' pages hold the requirement |
| Is the goal to corroborate science with practice? | yes |

## 2. Questions

- Q1 how many eligible reports does one reader miss?
- Q2 what does a standard-setting body require?

## 3. Existing reviews

- Found: a methodological review of single screening (Waffenschmidt 2019).
- Not found: a review of the second rating of a quality score.

## 4. Formal search

Database: OpenAlex, title and abstract, no key and no identity. Counts are of 2026-11-03.

| Id | String as run | OpenAlex | New concept |
|---|---|---|---|
| F10 | "second reviewer" OR "second rater" "systematic review" agreement kappa screening | 311 | not recorded |
| F11 | "inter-rater" "systematic review" screening reliability large language model | 22 | not recorded |

## 5. Grey search

| Id | Producer | What was read | Result |
|---|---|---|---|
| G1 | Cochrane Handbook, chapter 4 | the page, searched for independent | included |
| G2 | PRISMA website | the PRISMA 2020 and PRISMA-Check pages | included |

## 6. Stopping rule

- Effort bounded: the top 6 to 8 results per string by citation count.

## 7. Selection

- Include: a work that measures or requires a second reader.

## 8. Quality of grey sources

Garousi's 20 criteria in eight groups; the threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- Abstracts read; a figure from an abstract is secondary in [review](review.md).

## 10. Not searched, and limits

- Not searched: databases other than OpenAlex, forums, blogs.
- Not recorded: the top results of each string were read together, not one by one, so no letter per result was kept.
- One reviewer, no second rater.
