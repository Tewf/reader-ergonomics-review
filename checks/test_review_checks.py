"""Tests of the local checks in checks/local/: each rule fails where a review breaks it and stays silent where it does not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or extract the release in
checks/out/standard (AGENTS.md), or check reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
sys.path.insert(0, str(REPOSITORY / "checks" / "local"))


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPOSITORY / "checks" / "local" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


files, grey, numbers, search, rater = (load(n) for n in ("review_files", "grey_subtotals", "review_numbers", "search_record", "second_rater"))

SOURCES = """# Sources

## Grey

| Key | Tier | Score | Groups |
|---|---|---|---|
| Anthropic 2024 | 3 | 14 | 4, 3, 2, 1, 1, 2, 1, 0 |
| Weak 2025 | 3 | 6 | 2, 1, 1, 1, 0, 0.5, 0.5, 0 (example of practice only) |
| Cited 2020 | 1 | not scored | |
"""
PROTOCOL = """# Protocol

## Formal search

| Id | String | Hits | New concept |
|---|---|---|---|
| F1 | "snowballing" | 806 | ynnyn |
| F2 | "grey literature" | not run | not run |

## Stopping rule

Saturation: stop after 5 results that add no concept.

## Not searched

Forums.
"""
REVIEW = """# Review

Opening that counts 12 sources and is not read.

## Strand 1

- A team scored g = -0.23 (Vaccaro 2024, abstract, read). Measured.
- A trial found 55.8% faster (Peng 2023, secondary).
"""


class Rules(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)

    def put(self, path: str, text: str) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def review(self, **overrides: str) -> None:
        for name in files.FILES:
            self.put(f"evidence/topic/{name}.md", f"# {name}\n")
        self.put("evidence/bibliography.md", "# Bibliography\n")
        self.put("evidence/topic/sources.md", SOURCES)
        self.put("evidence/topic/protocol.md", PROTOCOL)
        self.put("evidence/topic/review.md", REVIEW)
        for path, text in overrides.items():
            self.put(f"evidence/topic/{path}.md", text)

    def messages(self, module) -> list[str]:
        return [finding.message for finding in module.check(self.root, {})]

    # review-files
    def test_complete_review_passes_every_check(self) -> None:
        self.review()
        for module in (files, grey, numbers, search, rater):
            self.assertEqual(self.messages(module), [], module.NAME)

    def test_missing_file(self) -> None:
        self.review()
        (self.root / "evidence/topic/against.md").unlink()
        self.assertEqual(self.messages(files), ["the review has no against.md"])

    def test_references_in_the_shared_bibliography_or_beside(self) -> None:
        self.review()
        (self.root / "evidence/bibliography.md").unlink()
        self.assertIn("references.md", self.messages(files)[0])
        self.put("evidence/topic/references.md", "# References\n")
        self.assertEqual(self.messages(files), [])

    def test_a_folder_outside_the_roots_is_ignored(self) -> None:
        self.put("notes/topic/frame.md", "# Frame\n")
        self.assertEqual(self.messages(files), [])

    # grey-subtotals
    def test_subtotals_not_adding_up(self) -> None:
        self.review(sources=SOURCES.replace("| 14 |", "| 15 |"))
        self.assertIn("add up to 14, the total says 15", self.messages(grey)[0])

    def test_row_without_subtotals(self) -> None:
        self.review(sources=SOURCES.replace("4, 3, 2, 1, 1, 2, 1, 0", "see text"))
        self.assertIn("no eight subtotals", self.messages(grey)[0])

    def test_subtotal_above_its_group_maximum(self) -> None:
        self.review(sources=SOURCES.replace("4, 3, 2, 1, 1, 2, 1, 0", "4, 3, 2, 2, 0, 2, 1, 0"))
        self.assertIn("date 2 is not a multiple of 0.5 within 0 to 1", self.messages(grey)[0])

    def test_total_under_threshold_must_say_example(self) -> None:
        self.review(sources=SOURCES.replace(" (example of practice only)", ""))
        self.assertIn("under 10: say it is an example", self.messages(grey)[0])

    def test_letters_and_final_total(self) -> None:
        row = "| Chapman 2000 | 1 | final 10; first 12 | A 3, M 3, O 1, D 1, P 0, N 1, I 0.5, T 0.5 |"
        self.review(sources=SOURCES + row + "\n")
        self.assertEqual(self.messages(grey), [])

    def test_total_taken_before_a_colon(self) -> None:
        row = "| Case 2018 | 1, essay | 10.5: 3, 1, 2, 1, 0.5, 1.5, 1, 0.5 |"
        self.review(sources="# Sources\n\n## Grey\n\n| Key | Tier | Score and subtotals |\n|---|---|---|\n" + row + "\n")
        self.assertEqual(self.messages(grey), [])

    def test_grey_section_without_scored_table(self) -> None:
        self.review(sources="# Sources\n\n## Grey\n\n| Key | Kind |\n|---|---|\n| A 2020 | blog |\n")
        self.assertIn("no table with a Score", self.messages(grey)[0])

    def test_no_grey_section_no_finding(self) -> None:
        self.review(sources="# Sources\n\n## Formal\n\n| Key |\n|---|\n| A 2020 |\n")
        self.assertEqual(self.messages(grey), [])

    # review-numbers
    def test_figure_without_key(self) -> None:
        self.review(review=REVIEW + "- The gain was 19% overall.\n")
        self.assertIn("no source key", self.messages(numbers)[0])

    def test_figure_without_location(self) -> None:
        self.review(review=REVIEW + "- Teams lost 23% (Bansal 2021).\n")
        self.assertIn("neither where it was read", self.messages(numbers)[0])

    def test_location_far_from_key_in_parenthesis(self) -> None:
        self.review(review=REVIEW + "- In a study Bansal 2021 tabulates, people scored 51.1% and the model 87.0% (section 2, read).\n")
        self.assertEqual(self.messages(numbers), [])

    def test_labels_years_and_locations_are_not_figures(self) -> None:
        self.review(review=REVIEW + "- Strand 3 sets out Q2 on 2026-11-03, as Garousi 2019 says in Table 7 and guideline 8.\n")
        self.assertEqual(self.messages(numbers), [])

    def test_numbers_findings_are_warnings(self) -> None:
        self.review(review=REVIEW + "- The gain was 19%.\n")
        self.assertEqual({f.kind for f in numbers.check(self.root, {})}, {"warning"})

    # search-record
    def test_string_without_count(self) -> None:
        self.review(protocol=PROTOCOL.replace("| 806 |", "| |"))
        self.assertIn("has no count", self.messages(search)[0])

    def test_no_table_of_strings(self) -> None:
        self.review(protocol="# Protocol\n\nWe searched.\n\nNot searched: forums. Stopping rule: saturation.\n")
        self.assertIn("no table of search strings", self.messages(search)[0])

    def test_several_strings_under_one_count(self) -> None:
        self.review(protocol=PROTOCOL.replace('| F1 | "snowballing" | 806 | ynnyn |', '| F1 | 4 strings on one server | 37 |'))
        self.assertIn("4 strings under one count", self.messages(search)[0])

    def test_missing_not_searched_and_stopping_rule_warn(self) -> None:
        self.review(protocol=PROTOCOL.replace("## Stopping rule", "## Rule").replace("Saturation", "Enough").replace("Not searched", "Elsewhere"))
        kinds = {(f.kind, f.message[:20]) for f in search.check(self.root, {})}
        self.assertEqual({kind for kind, _ in kinds}, {"warning"})
        self.assertEqual(len(kinds), 2)

    def test_no_concept_column_is_a_warning_before_the_date(self) -> None:
        self.review(protocol=PROTOCOL.replace(" | New concept |", " |").replace("---|---|---|---|", "---|---|---|").replace(" | ynnyn |", " |").replace(" | not run | not run |", " | not run |"))
        found = search.check(self.root, {})
        self.assertEqual([(f.kind, "concepts per result" in f.message) for f in found], [("warning", True)])

    def test_no_concept_column_is_an_error_from_the_date(self) -> None:
        bare = PROTOCOL.replace(" | New concept |", " |").replace("---|---|---|---|", "---|---|---|").replace(" | ynnyn |", " |").replace(" | not run | not run |", " | not run |")
        self.review(protocol=bare.replace("# Protocol\n", "# Protocol\n\nRun on 2026-11-04.\n", 1))
        self.assertEqual({f.kind for f in search.check(self.root, {})}, {"error"})

    def test_malformed_concept_cell(self) -> None:
        self.review(protocol=PROTOCOL.replace("| ynnyn |", "| some |").replace("# Protocol\n", "# Protocol\n\nRun on 2026-12-01.\n", 1))
        self.assertIn("not a y/n sequence", self.messages(search)[0])

    def test_not_recorded_with_a_reason_is_a_warning_even_after_the_date(self) -> None:
        text = PROTOCOL.replace("| ynnyn |", "| not recorded |").replace("# Protocol\n", "# Protocol\n\nRun on 2026-12-01.\n", 1)
        self.review(protocol=text.replace("Forums.", "Forums.\n\n## Limits\n\n- Not recorded: the engine returns one synthesis, not a list.\n"))
        found = search.check(self.root, {})
        self.assertEqual([f.kind for f in found], ["warning"])
        self.assertIn("the engine returns one synthesis, not a list", found[0].message)

    def test_not_recorded_without_a_reason_is_a_malformed_cell(self) -> None:
        text = PROTOCOL.replace("| ynnyn |", "| not recorded |").replace("# Protocol\n", "# Protocol\n\nRun on 2026-12-01.\n", 1)
        self.review(protocol=text)
        found = search.check(self.root, {})
        self.assertEqual([f.kind for f in found], ["error"])
        self.assertIn("no reason", found[0].message)

    # second-rater
    def test_two_raters_without_agreement(self) -> None:
        self.review(protocol=PROTOCOL + "\n## Second rater\n\nA model scored the sources too.\n")
        self.assertIn("reports no agreement", self.messages(rater)[0])

    def test_two_raters_with_agreement(self) -> None:
        self.review(protocol=PROTOCOL + "\n## Second rater\n\nAgreement on the threshold: 6 of 9; kappa 0.37.\n")
        self.assertEqual(self.messages(rater), [])

    def test_second_rating_declared_not_completed(self) -> None:
        self.review(protocol=PROTOCOL + "\n## Second rater: not completed\n\nThe second rating was not completed.\n")
        self.assertEqual(self.messages(rater), [])

    def test_agreement_reported_in_the_other_file(self) -> None:
        self.review(sources=SOURCES + "\n### Second rater\n\nSee the protocol.\n",
                    protocol=PROTOCOL + "\n## Second rater\n\nMean absolute difference 5.0 of 20.\n")
        self.assertEqual(self.messages(rater), [])

    def test_no_second_rater_is_not_a_second_rater(self) -> None:
        self.review(protocol=PROTOCOL + "\nLimits: one reviewer, no second rater on the grey scores.\n")
        self.assertEqual(self.messages(rater), [])


if __name__ == "__main__":
    unittest.main()
