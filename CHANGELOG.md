# Changelog

## 0.4.0 — 2026-07-28

### Research programme

- Made the FAW Attitudes Audit the next planned experiment.
- Separated the 2022 global inequality-attitudes dataset from the 2025 global
  impartial-spectator experiment.
- Added a staged protocol for country-explicit responses, perspective prompting,
  prompt robustness, and a separate population-estimation task.
- Replaced percentile and synthetic-coverage language with selected-category
  human mass, ordinal distance, joint-cell typicality, and stability metrics.
- Kept DSE as the only active result and moved its matched confirmatory extension
  to a later stage.

### Web and repository

- Added a GitHub Pages site at `docs/index.html`.
- Added `NEXT_EXPERIMENT_FAW_ATTITUDES.md` and `RESEARCH_PROGRAMME.md`.
- Added explicit third-party-data and contamination limits.
- Updated the package and web release identifiers to v0.4 and v2.3.


## 0.3.0 — 2026-07-28

### Architecture

- Made DSE the only active case study.
- Added separate `active`, `evidence_to_date` and `research_record` result
  folders.
- Added a web content map and result-status registry.

### Statistical and analytical corrections

- Preserved cluster-level inference for repeated generations.
- Corrected Ola 2 contrast counts to 16 proportionality + 4 equality = 20.
- Separated GPT low and high reasoning modes.
- Excluded DeepSeek Chat / `non_thinking` from all derived results.
- Retained DeepSeek Reasoner as an independent configuration.
- Replaced “human range” outputs with position relative to selected published
  aggregate point estimates or national means.
- Removed `intervals_overlap` language that implied human confidence intervals.
- Matched English and Mandarin MFQ on `lente_A` and recorded mode.
- Added vignette-set counts and 5,000 bootstrap replicates to DSE coefficients.
- Added SciPy to dependencies.

### Interpretation corrections

- Representation coverage and human disagreement compression are marked as
  future metrics, not current results.
- Longitudinal monitoring is explicitly not yet demonstrated.
- MFQ and language outputs are classified as exploratory due to incomplete
  provenance.
- The fixed CHF 18,000 deviation and reconstructed DSE wording are restored as
  visible limitations.

### Reproducibility

- `run_all.py` deletes stale derived CSVs before regeneration.
- Tests check every manifest entry, mode separation, result classification and
  removal of legacy outputs.
