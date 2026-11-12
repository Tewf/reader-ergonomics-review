# Contributing to this repository

For anyone changing this repository, person or language model. To apply the reader-ergonomics standard elsewhere,
read its [standard.md](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/standard.md); this file is about this repository only.

## Before writing

1. Read the standard at the release this repository checks against (v1.21.0), and the front page's scope: what is in,
   what is out, and which neighbour holds what is out.
2. The first job, the review of the genre in [evidence/review-genre/](evidence/review-genre/README.md), is written and
   names its baseline B1. A change to a shape or a check is a change to what the nine reviews of the family are held to:
   run `python3 checks/audit.py` on them before and after, and say what moved.
3. A fact that belongs to a neighbour is linked, never copied. A choice that shapes the repository gets a record in
   [decisions/](decisions/).

## Rules for claims

- Every claim carries a grade: **measured**, **supported with caveat**, **convention** or **not supported**. A grade
  moves only with a cited source.
- Cite as `Author Year`; the entry goes once into `evidence/bibliography.md` when the review starts, with a DOI, an
  arXiv id or a stable URL. A key names one work across the family (reader-ergonomics decision 0003): the family is
  listed under `[bibliography_keys]` in checks/config.toml.
- Evidence against a rule goes into the review's `against.md`, never deleted to make a rule look stronger.
- A number read in a summary rather than in the source is marked "(secondary)".

## Shapes, checks and principles

- A shape in [shapes/](shapes/README.md) has a skeleton, the evidence for each part, a worked example, rules and the
  checks that read it. The headings a check needs are in `[shape_conformance]` of checks/config.toml; keep both in step.
- The five checks are in `checks/local/`, each with its tests in `checks/test_review_checks.py`. A rule gets a test
  that fails where it should and stays silent where it should not.
- A principle names a check on its Check line; what no program decides is said to be judgment there.
- A check reads form, never truth ([decision 0003](decisions/0003-the-checks-read-the-form-not-the-truth.md)).
- Run the tests with `python3 -m unittest discover -s checks`.

## The model's place

- A model explains, proposes, translates and drafts; it decides nothing. Its output is checked by a program or read
  by the maintainer.

## Links

- Down to reader-ergonomics: pinned to the release's commit, as CI is.
- Up: none.

## Before handing back

Run the checks against the release CI uses, extracted inside this repository, in `checks/out/standard`, which git and
the checks both skip:

```sh
rm -rf checks/out/standard && mkdir -p checks/out/standard
git -C ../reader-ergonomics archive 65e4247 | tar -x -C checks/out/standard   # the commit checks.yml pins
python3 checks/out/standard/checks/run.py . --tiers program,meaning --judge flag   # the repository, as CI runs it
```

- Fix every error. Read every warning.
- Answer the questions in `checks/out/needs-judgment.md` in `checks/judgments.toml`, each answer quoting in backticks
  a word or heading of its own file.
- Keep [llms.txt](llms.txt), [README.md](README.md) and [README.fr.md](README.fr.md) in step.
- A pin raise goes in [CHANGELOG.md](CHANGELOG.md), not in decisions/.

## House conventions

- No em dash or en dash in prose; use a comma, a colon, parentheses, or a hyphen for ranges.
- Commit messages follow the standard's commit shape: a subject of at most 72 characters, then why.
- The maintainer decides every push.
