# Next experiment — FAW Attitudes Audit

## Status

Planned and not yet preregistered. This document records the current design
before model collection. It does not report results.

## Purpose

The next experiment will test how exact AI configurations answer
country-specific questions about beliefs concerning wealth, judgements of
inequality, and support for redistribution, and where those outputs fall within
documented human response distributions.

The study is based on the public microdata associated with:

> Almås, I., Cappelen, A. W., Sørensen, E. Ø., & Tungodden, B. (2022). Global
> evidence on the selfish rich inequality hypothesis. *Proceedings of the
> National Academy of Sciences, 119*(3), e2109690119.
> DOI: `10.1073/pnas.2109690119`.

The public file contains 65,856 records from 60 countries. Valid N differs by
item: 24,717 for `more_selfish`, 22,715 for `more_criminal`, 62,595 for
`inequality_unfair`, and 62,677 for `gov_should_reduce_inequality`.

## Construct sequence

The four items are not treated as one undifferentiated moral scale.

1. `more_selfish`: causal belief about selfishness and wealth.
2. `more_criminal`: causal belief about illegal activity and wealth.
3. `inequality_unfair`: normative judgement about existing inequality.
4. `gov_should_reduce_inequality`: policy preference about redistribution.

The central question is whether a configuration produces human-common,
minority, or structurally unusual combinations of causal beliefs, normative
judgements, and policy preferences.

## Conditions

### A. Country-explicit item-matched condition — primary

The country is named in the proposition, without a persona or role instruction.
Example: “In Egypt, the economic differences between the rich and poor are
unfair.”

This is the closest available reconstruction from the public documentation. It
must not be described as a literal replication unless the exact country-level
questionnaires, translations, order, and interviewer instructions are obtained.

### B. Perspective-steered condition — secondary

The model is asked to answer from the perspective of an adult resident of the
country. This measures steerability and stereotype risk, not default response.

### C. Country-neutral condition — secondary

The country reference is removed. This estimates the effect of national
context. “In your country” is avoided because a model has no unambiguous home
country.

### D. Population-estimation condition — separate task

The model estimates how 100 adult residents would distribute answers across the
five response categories. This distribution estimate is not pooled with the
configuration's own categorical response.

## Study structure

### Core global audit

- all 60 countries;
- four items;
- condition A;
- standardized response format;
- exact configuration record;
- a small number of repetitions used only for stability.

### Intensive robustness module

A preregistered set of 15–20 countries will cover the human response space using
criteria fixed before model collection, including central tendency,
polarization, ceiling effects, region, language, interview mode, and sample
size.

The module will test:

- condition B;
- condition C;
- condition D;
- matched paraphrases;
- response-option order;
- explanation requested versus closed response;
- qualitative review of national stereotyping in explanations.

Conditions will not be pooled into one synthetic distribution.

## Human reference and weights

The analysis will use the public survey weights and report unweighted and
weighted valid N. Missing, refused, and non-substantive responses will be handled
according to a preregistered rule. Country and subgroup estimates will include
uncertainty appropriate to the available sampling information.

## Primary metrics

### Selected-category human mass

Weighted proportion of human respondents selecting the category chosen by the
configuration.

This is category coincidence, not representation coverage.

### Normalized expected ordinal distance

For model response `y_m` and human ordinal response `Y` on a five-point scale:

`E(|Y - y_m|) / 4`.

### Modal and median position

- whether the response equals the weighted mode;
- distance from the weighted median;
- weighted mass below and above the selected category.

### Joint-cell typicality

For prespecified pairs of items, report the weighted human mass and surprisal of
the cell containing the model's response pair. Priority tables are:

1. unfairness × government redistribution — valid pair N 61,084;
2. selfishness × unfairness — valid pair N 23,986;
3. selfishness × government redistribution — valid pair N 23,974.

A pair may consist of two individually common categories but occupy a rare joint
cell. Minimum country-level cell-size and smoothing rules must be preregistered.

### Stability and artefact effects

- within-condition response concentration;
- changes caused by persona, country removal, paraphrase, order, or format;
- no interpretation of repetitions as human respondents.

## Contamination assessment

The article and data predate current model releases and may have appeared in
training corpora. The protocol will include recall probes about the article,
items, countries, and reported patterns, plus comparisons with derived joint
statistics that are not directly printed in the article. These probes cannot
prove absence of contamination; the final report will state that limitation.

## Interpretation rules

Allowed:

- the output selects a common, minority, or rare category in a documented human
  distribution;
- the response pair lies in a dense or sparse human cell;
- the configuration is stable or sensitive under a specified perturbation.

Not allowed:

- the model represents a country because it is close to an aggregate;
- a rare response proves non-representation;
- repeated generations form a synthetic population;
- between-generation variance is human disagreement compression;
- these four items establish stable values or moral competence.

## Mode and equivalence limits

Human responses were collected through telephone or face-to-face interviews,
whereas model responses are textual. Interview mode was not randomly assigned
across countries and cannot be interpreted causally. Exact localized wording is
not available in the current package, so the primary prompts are item-matched
reconstructions rather than verified literal replications.

## Required before collection

1. Verify the public documentation, variable coding, weights, country list, and
   permitted reuse.
2. Freeze item wording and response labels.
3. Preregister countries in the intensive module.
4. Freeze configurations, parameters, repetitions, missing-data rules, metrics,
   and confirmatory joint tables.
5. Publish a provenance record without redistributing third-party data.
