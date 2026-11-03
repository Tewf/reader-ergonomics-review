# Checks

The standard's checks run on this repository in CI ([checks.yml](../.github/workflows/checks.yml)). The five below are this repository's own, in `checks/local/`; the standard's runner loads them with its own, and a run fails on any error.

| Check | Kind | Decides |
|---|---|---|
| `review-files` | exact | a review folder holds the eight files and a list of references, in the folder or once for the repository |
| `grey-subtotals` | exact | each grey row has eight subtotals in range, a total equal to their sum, and the words example or practice only under 10 |
| `review-numbers` | heuristic | a line of review.md with a figure holds a source key and a place, or says secondary |
| `search-record` | exact | protocol.md has a table of strings, each with a count; warns when it names no stopping rule or no gap |
| `second-rater` | exact | a review with two raters reports their agreement, or says the second rating was not completed |

What a program cannot decide stays judgment: that a score or a search is right, that a figure is what its source says, that the statistic suits the data.

## Run them on another repository

```sh
python3 checks/audit.py ../ai-augmented-project            # reviews in evidence/*
python3 checks/audit.py ../some-repo --roots 'docs/review-*'
```

`audit.py` reads the repository and changes nothing in it. The tests are `python3 -m unittest discover -s checks`.
