# Withdrawn and superseded claims

Review date: 28 July 2026. Claims remain on the record so that corrections can
be inspected.

## 1. Declared-versus-chosen association

**Withdrawn claim:** an inverse association between stated proportionality and
proportional choices across five model-family aggregates.

**Reason:** only five aggregate points, wide uncertainty, strong item
dependence and initial mixing of distinct configurations.

**Current status:** no association is estimated. Stated and chosen results are
reported separately by exact configuration.

## 2. A single nearest human country for each model

**Withdrawn claim:** each system could be assigned one closest national-mean
profile.

**Reason:** the nearest national mean changes with prompt variant and the gaps
between candidates are small.

**Current status:** prompt sensitivity and top-three candidate national means
are reported with an explicit warning that national-mean similarity is not
human representation.

## 3. Ranking systems by seven dilemma choices

**Withdrawn claim:** systems can be ordered by proportional-choice frequency.

**Reason:** intervals resampling seven dilemmas are too wide to resolve such an
ordering.

**Current status:** point estimates and intervals remain exploratory and no
ranking is produced.

## 4. Demonstrated version drift

**Withdrawn claim:** the Opus series demonstrated meaningful longitudinal
drift.

**Reason:** all adjusted intervals include zero; the effect-size threshold was
adopted during reanalysis rather than preregistered; the comparison covers one
family and was not a purpose-built longitudinal programme.

**Current status:** retained only as
`data/results/research_record/opus_version_comparison_historical_inconclusive.csv`.
The current release states that longitudinal monitoring has not yet been
measured.

## 5. Generation rows as sample size

**Superseded presentation:** large row counts were displayed where readers
could interpret them as independent sample size.

**Reason:** repeated generations belong to the same items or vignette sets.

**Current status:** every estimate reports generation rows, task clusters,
repetitions and bootstrap unit separately. Effective n is a secondary model-
based diagnostic only.

## 6. The original English–Mandarin comparison

**Withdrawn result:** a comparison between English `canonica` and Mandarin
`lente_A`, with GPT and DeepSeek English modes aggregated.

**Reason:** instrument variants and configurations were not matched.

**Current status:** replaced by
`mfq_language_comparison_matched.csv`, which uses `lente_A` and matching
recorded modes. The replacement remains exploratory.

## 7. Aggregated DeepSeek Chat and Reasoner results

**Withdrawn result:** Ola 2, MFQ and response-concentration figures that treated
`non_thinking` and `thinking` as repeated observations of one configuration.

**Reason:** the rows came from distinct DeepSeek API endpoints.

**Current status:** DeepSeek Chat is excluded from derived results. DeepSeek
Reasoner is reported independently. Original mixed files remain only in the
research record.

## 8. “Human range” as representation

**Withdrawn interpretation:** falling outside the minimum and maximum of
published aggregates demonstrates failure to represent a human population.

**Reason:** the bounds are aggregate point estimates, not individual
distributions or human uncertainty intervals.

**Current status:** outputs use “reported aggregate point-estimate span” and
explicitly state that representation is not measured.

## Results retained as active

- task-dependent DSE allocation effects;
- exact-equal-split estimates and model cluster-bootstrap intervals;
- the finding that model intervals are below all selected published human
  aggregate point estimates included in the DSE comparison;
- transparent reference limitations and source discrepancies.
