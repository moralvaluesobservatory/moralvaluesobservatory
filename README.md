# Moral Values Observatory

A public, reproducible record of the moral profiles of frontier AI models: the pattern of
which values each one weighs more and which less, and how that profile shifts against a
reference — another model, an earlier version, a human population, or a declared standard.

**Live site:** https://moralvaluesobservatory.org
(or, before the domain propagates: `https://<your-github-username>.github.io/<repo-name>/`)

This is a pilot: a first working version, not a finished product. The site explains what
holds up and what doesn't yet.

## Repository structure

```
index.html          the site itself (open directly or visit the live link)
data/
  raw/               raw model responses, one row per answer, as collected
  results/           computed outputs (correlations, bootstraps, integrity checks)
  notes/             working notes from the audit: reconciliations, robustness checks
scripts/
  reproducir_mapa_weird.py         rebuilds the WEIRD-profile correlations (Card 1) from raw/
  reproducir_reclasificacion.py    rebuilds the "declined to rate" classification
  actualizar_piloto_mandarin.py    adds a new Mandarin-language model run and updates the forest plot
docs/
  RESULTADOS_Y_ORGANIZACION.md     the project's own working log and reference doc
  TEORIA_DE_CAMBIO.md              internal theory of change (compass, not a pitch)
  PRE_REGISTRO_gpt_fable_mandarin.md   a pre-registration, written before the data, plus its outcome
```

## Reproducing the published figures

```bash
cd scripts
python3 reproducir_mapa_weird.py
```

This reads `data/raw/*.csv` and regenerates `01_mapa_weird.csv` and `04_bootstrap_weird.csv`.
The five correlations it produces should match the ones shown on the site to three decimals.
An outside reviewer ran this same script against these same files and got that match; the
site's trust section has the details.

## Adding a new model or language run

```bash
cd scripts
python3 actualizar_piloto_mandarin.py <new_model_zh.csv> <another_model_zh.csv> ../data
```

Outputs an updated 10-row (or n-row) table and a ready-to-paste SVG for the language-pilot card.
Same seed (42), same resampling scheme as every number already published, so new and old rows
are directly comparable.

## The raw files

Files under `data/raw/` are one row per model response: which item, which foundation, which
repetition, the score, and whether it parsed cleanly (`estado_parseo`). Nothing here has been
aggregated, filtered, or reclassified — that happens in the scripts, in the open, so anyone can
check the step where a raw answer becomes a published number.

## Contact

contact@moralvaluesobservatory.org
