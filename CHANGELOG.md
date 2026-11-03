# Changelog

The releases this repository pins, newest first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
A pin move is recorded here, not in decisions/.

## Unreleased

### Added

- The principle [log concepts per result](principles/record/log-concepts-per-result.md), and a New concept column in the
  search tables of the protocol shape. `search-record` asks for it: an error in a protocol dated 2026-11-04 or later,
  a warning before. Cause: no protocol of the family logged what each result added, so no stopping estimator could
  judge a search (ai-augmented-data-gathering).
- The value `not recorded` for the New concept column, for a search tool that returns a synthesis and not a list.
  The protocol's Limits section gives the reason on one `Not recorded:` line.
  `search-record` accepts the value with a warning that names the reason, never an error.
  With no reason the cell is malformed. Cause: the column could not be filled honestly for such a tool.

## 2026-11-03

### Added

- The first pass of the genre, in six parts.
  Nine shapes with a small example. Five checks with tests, and an audit of another repository.
  Six principles on a card. The review of the genre's own evidence (25 sources, baseline B1).
  Two decision records. The front pages in both languages.
- Pinned reader-ergonomics v1.20.0 (`4f99372`), at the repository's start: the standard's pin, link, changelog and
  decision-record checks, which this skeleton is written to pass.
