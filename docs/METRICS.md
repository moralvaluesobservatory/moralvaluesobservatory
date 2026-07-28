# Metrics and inferential rules

## 1. Task clusters, not generation rows

Repeated generations of the same item or vignette set measure response
variability. They are not independent participants and are not independent
tasks.

Every interval in the current pipeline resamples whole task clusters:

- item for scale statements;
- dilemma for binary choices;
- vignette set for DSE allocations;
- paired item for the historical version comparison.

Outputs report generation rows, task clusters, repetitions and bootstrap rules
separately.

`model_based_effective_n_diagnostic` is retained only as a variance-components
diagnostic. It is not a participant count and does not replace cluster counts.

## 2. Position relative to reported aggregate estimates

The DSE comparison uses the minimum and maximum of selected published aggregate
point estimates. The output classifies the model point estimate as below,
within or above that span and reports whether the model bootstrap interval is
below all included point estimates.

This is not:

- an individual-level human range;
- a human confidence interval;
- a representation score;
- evidence that people between the minimum and maximum are evenly distributed.

Output: `data/results/active/dse_reported_reference_position.csv`.

The MFQ evidence uses an analogous span across 19 selected national means. It
is explicitly labelled `national_means_not_individuals` and has incomplete
source provenance in the current package.

## 3. Allocation effects

DSE fixed-effect coefficients estimate how recipient attributes are associated
with allocation shares within each three-recipient decision. Coefficients are
percentage-point changes relative to reference categories in the tested
vignette bank.

Intervals resample vignette sets. They do not include uncertainty from new
domains, prompts, dates, model versions or human references.

## 4. Response concentration and prompt sensitivity

The pipeline reports the share of task clusters with identical repeated
responses and the instability of MFQ national-mean similarity across prompt
variants. These are measurement diagnostics.

They are not yet a human-disagreement compression metric. A valid compression
measure requires comparable human and model distributions on the same items.

## 5. Representation coverage

Representation coverage is a future metric and is not computed in this
release. It requires human microdata, subgroup definitions, sampling
information, weights, uncertainty and a defensible distance or coverage rule.
