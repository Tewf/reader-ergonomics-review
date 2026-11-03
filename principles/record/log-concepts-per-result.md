# Log concepts per result

**Claim:** the protocol records, for each result screened and in order, whether it added a concept, so that a stopping estimator or a rule can judge when the search may stop.

- **Grade:** supported with caveat for the estimator, as the data-gathering review graded it. A coverage estimate from singletons and doubletons (Chao, read in the linked review) is established in ecology. It was never applied to a literature search. Measured, descriptive, for the finding that none of the family's logs could feed it.
- **Evidence:** [state of the art, best evidence](https://github.com/Tewf/ai-augmented-data-gathering/blob/68aaf56083e729695242ed6e93f5fa5821d559b0/evidence/foraging-and-stopping/state-of-the-art.md); [on the family](https://github.com/Tewf/ai-augmented-data-gathering/blob/68aaf56083e729695242ed6e93f5fa5821d559b0/evidence/foraging-and-stopping/on-the-family.md).
- **Check:** `search-record` (exact): each table of strings has a New concept column, a sequence of y and n or the words not run. An error in a protocol dated 2026-11-04 or later, a warning before.
- **Reader styles:** none.

## What it asks

- One column in each search table, New concept.
- One letter per result screened, in the order seen: y if it added a concept, n if not (`ynnyn`).
- A string that was not run says so.

## Why

- A stopping rule that counts results with no new concept needs to see them. The family's logs held only the route that first found each source.
- Run on three of the family's protocols as they stand, the estimator gives coverage 0.00 to 0.05, which follows from the form of the log and not from the searches.

## Limits

- The check reads that the column is there, not that a result added a concept; that stays the reviewer's judgment.
- A letter per result is the least that feeds a rule. An estimator also needs the concepts themselves, kept as the data-gathering review describes.
- The nine reviews written before 2026-11-04 are flagged with a warning and not failed.
