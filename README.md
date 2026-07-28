# Moral Values Observatory — representation-oriented core v0.4

This repository is the research source for a public project on pluralistic AI
governance. The Observatory studies how exact AI configurations respond when
legitimate human values and moral considerations conflict, and what documented
human disagreement their outputs reflect, concentrate, or leave unmeasured.

The current active evidence remains a distributive-justice pilot. The next
planned experiment is a global attitudes audit using public human microdata from
60 countries. No new model results from that experiment are included in this
release.

## Start here

1. `docs/MISSION.md`
2. `docs/CURRENT_SCOPE.md`
3. `docs/CASE_STUDY_01_DSE.md`
4. `docs/NEXT_EXPERIMENT_FAW_ATTITUDES.md`
5. `docs/RESEARCH_PROGRAMME.md`
6. `docs/EVIDENCE_TO_DATE.md`
7. `docs/index.html` — GitHub Pages source

## Active case study

`data/results/active/` contains the reconstructed distributional survey
experiment in which five exact configurations allocate a hypothetical CHF
18,000 in workplace and inheritance settings.

The active outputs report allocation patterns, exact-equal-split frequencies,
vignette-set bootstrap intervals, and position relative to selected published
human aggregate point estimates. They do not establish representation of a
person, subgroup, country, or culture.

## Next experiment — FAW Attitudes Audit

The planned study uses the public microdata associated with Almås et al. (2022),
*Global evidence on the selfish rich inequality hypothesis*. It will examine
country-specific responses about:

- selfishness as a source of wealth;
- illegal activity as a source of wealth;
- whether economic differences are unfair;
- whether government should reduce those differences.

The core condition names the country but does not ask the model to impersonate
a resident. Perspective prompting, country-neutral wording, prompt robustness,
and population-distribution estimation are separate conditions. Repeated model
generations are used for stability only.

Third-party human microdata are **not redistributed** in this repository. See
`docs/THIRD_PARTY_MATERIALS.md`.

## Evidence classes

- `data/results/active/`: currently defensible project findings.
- `data/results/evidence_to_date/`: corrected exploratory pilot analyses.
- `data/results/research_record/` and `research_record/`: inconclusive,
  excluded, withdrawn, or superseded material retained for transparency.

## Reproduce the current DSE release

```bash
python -m pip install -r requirements.txt
python scripts/analysis/run_all.py
python -m pytest tests/ -q
```

`run_all.py` deletes stale derived CSVs before rebuilding them. The SHA-256
manifest at `data/metadata/file_manifest_sha256.csv` covers tracked source files
and excludes release artifacts under `docs/downloads/`.

## Statistical rule

Repeated generations of the same item or vignette set are not independent
participants. Items or scenarios are the primary statistical units; repetitions
measure conditional stability and response concentration.

## Licences and contact

- Code: MIT (`LICENSE`)
- Project-generated data and documentation: CC BY-SA 4.0 (`LICENSE-DATA.md`)
- Third-party instruments, publications, and human datasets retain their own
  terms and are not redistributed unless explicitly documented.

Author: Sandra Malagón  
Contact: contact@moralvaluesobservatory.org
