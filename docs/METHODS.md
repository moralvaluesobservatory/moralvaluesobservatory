# Methods summary

## Source-of-truth order

1. Collection code and exact recorded configuration.
2. Raw response files.
3. Analysis scripts and generated results.
4. Documentation.
5. Public website.

Narrative text never overrides primary artifacts.

## DSE

Usable rows have parse status `ok` or `ajustado`, non-negative allocations,
amounts summing to CHF 18,000 and shares summing to one. Exact-equal-split and
Gini intervals use a vignette-set cluster bootstrap with 10,000 replicates.
Coefficient intervals use 5,000 vignette-set bootstrap replicates.

## Ola 2

GPT low and high reasoning are analysed separately. DeepSeek Chat is excluded;
DeepSeek Reasoner is retained as a separate configuration. The declared
proportionality-minus-equality contrast uses 16 proportionality items and four
equality items. Binary-choice intervals resample seven dilemmas.

## MFQ

English profiles are calculated separately by exact configuration and prompt
variant. The language comparison uses `lente_A` in both languages and matching
recorded modes. Results remain exploratory because MFQ collection-code and
human-reference provenance are incomplete.

## Reproduction

`python scripts/analysis/run_all.py` removes stale result CSVs, regenerates all
classified outputs and rebuilds the SHA-256 manifest.
