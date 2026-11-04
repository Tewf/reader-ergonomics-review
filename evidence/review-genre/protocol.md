# Protocol: how the pool was built

A first pass of a multivocal literature review to Garousi 2019, run on 2026-11-03 by one reviewer. Terms are in [frame](frame.md).

## 1. Why grey literature

Garousi's seven questions (Table 4), answered for this topic. One yes suggests including grey sources.

| Question | Answer |
|---|---|
| Is the subject complex and not solvable by the formal literature alone? | yes: reviews are run by practice and by research |
| Is there a lack of volume, quality or consensus in the formal literature? | yes: no study of grey-score reliability was found |
| Is the contextual information important? | yes: the software setting matters |
| Is the goal to corroborate science with practice? | yes |
| Is the goal to challenge practice with research, or the reverse? | yes: the family's threshold has a source |
| Would a synthesis of both communities help? | yes |
| Is there a large volume of practitioner sources? | no: two bodies' pages were found |

## 2. Questions

- Q1 files: which do the guidelines ask for, and which do the nine reviews keep?
- Q2 grey score: what grades a grey source, and how reliably?
- Q3 second rater: what does it cost, and what does it catch?
- Q4 checks: what can a program decide?

## 3. Existing reviews (Garousi guideline 2)

- Found: two tertiary studies of multivocal reviews (Neto 2019; Kamei 2021), a mapping of grey use in 138 reviews (Yasin 2020) and a methodological review of single screening (Waffenschmidt 2019).
- Not found: a review of how a review's files are kept, or a study of the reliability of grey scores.

## 4. Formal search

Database: OpenAlex, `title_and_abstract.search`, no key and no identity. Counts are of 2026-11-03.

| Id | String as run | OpenAlex | New concept |
|---|---|---|---|
| F1 | "multivocal literature review" "software engineering" | 77 | not recorded |
| F2 | "snowballing" "systematic literature" | 806 | not recorded |
| F3 | "grey literature" "software engineering" "systematic" | 56 | not recorded |
| F4 | "guidelines" "systematic literature reviews" "software engineering" | 292 | not recorded |
| F5 | "multivocal literature reviews" tertiary study software engineering | 3 | not recorded |
| F6 | "grey literature" "quality assessment" "inter-rater" | 18 | not recorded |
| F7 | "multivocal" "grey literature" "quality assessment" criteria "inter-rater" OR "agreement" | 10 | not recorded |
| F8 | "AACODS" checklist grey literature | 52 | not recorded |
| F9 | "inter-rater agreement" "quality assessment" "systematic reviews" "software engineering" | 1 | not recorded |
| F10 | "second reviewer" OR "second rater" "systematic review" agreement kappa screening | 311 | not recorded |
| F11 | "inter-rater" "systematic review" screening reliability large language model | 22 | not recorded |
| F12 | "large language models" "title and abstract screening" "systematic review" | 46 | not recorded |
| F13 | "PRISMA" adherence "software engineering" systematic reviews reporting quality | 0 | not recorded: no results |
| F14 | "reporting quality" "systematic literature reviews" "software engineering" checklist compliance | 0 | not recorded: no results |
| F15 | automated checking "PRISMA" checklist compliance systematic review tool | 1 | not recorded |
| F16 | "PRISMA-Check" | 37 | not recorded |
| F17 | "PRISMA 2020" adherence assessment tool development protocol | 8 | not recorded |
| F18 | GitHub "systematic review" reproducibility "search strings" reported counts | 0 | not recorded: no results |

- The top 6 to 8 results of each string by citation count were read by title; about 87 titles in all.
- Zero results (F13, F14, F18) are a statement about the query. F16 returned 37 works that mention the word in passing.
- Fifteen named leads were each checked by DOI in OpenAlex.
  - Reporting and screening: Page 2021, Rethlefsen 2021, Waffenschmidt 2019, McHugh 2012, Khraisha 2024.
  - Search: Greenhalgh 2005, Badampudi 2015, Jalali 2012, Wohlin 2016, Zhang 2011.
  - Method and grey sources: Kitchenham 2009, Kuhrmann 2017, Hopewell 2007, Páez 2017, Adams 2017.
- Not run: the forward pass from Garousi 2019 and Wohlin 2014. The free OpenAlex budget was used up, and a key needs an email address, which is an identity.

## 5. Grey search

| Id | Producer | What was read | Result | New concept |
|---|---|---|---|---|
| G1 | Cochrane Handbook, chapter 4 | the page, searched for grey, independent and duplicate | read in part, included (Lefebvre 2025) | not recorded |
| G2 | PRISMA website, 3 pages | the PRISMA 2020 page, the home page, the PRISMA-Check page | included (PRISMA Executive 2026) | not recorded |
| G3 | AACODS checklist (a university repository) | the address returned a web page, not the checklist | not read, not included | not run |
| G4 | Environmental evidence guidelines page | the request was refused by a bot check | unverifiable, not included | not run |

- The bot check was not bypassed.
- Not searched: forums, Q/A sites, talks, videos, blogs, books, theses.

## 6. Stopping rule

- Effort bounded: the top 6 to 8 results per string.
- Saturation: a string stopped when its results added no concept. F9, F13 and F14 returned nothing, and no further string was run on their topic.
- The pool is capped at 25 sources (the contract allows 15 to 25). Works found and dropped at the cap are in [sources](sources.md).

## 7. Selection

- Include: a work that measures or prescribes how a literature review is searched, scored, reported or checked.
- Exclude: reviews of a clinical topic that merely use the method; the search for studies in health databases beyond the two screening studies.
- Quality: formal sources carry an evidence grade; grey sources are scored in section 8.

## 8. Quality of grey sources

Garousi's 20 criteria (Table 7), scored 1, 0.5 or 0 and summed in eight groups: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. The threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- Garousi 2019 was read in its preprint text; Page 2021 in its full text. Eighteen formal works were read from the abstract, and three were located only.
- A figure read from an abstract is marked (secondary) in [review](review.md). Synthesis is narrative by question.

## 10. Not searched, and limits

- One reviewer and no second rater: the two grey scores are one person's judgment.
- Eighteen of 23 formal works were read from the abstract only.
- The searches are English and keyword based, on OpenAlex alone. Google Scholar and the software engineering databases were not searched.
- Counts change with the index; they are those of 2026-11-03.
- Not recorded: the results of each string were read by title and the screening kept no letter per result, so no record of which result added a concept exists; it cannot be rebuilt afterwards.
