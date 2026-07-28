# Data dictionary summary

## Classified result folders

- `data/results/active/`: web-eligible active DSE results.
- `data/results/evidence_to_date/`: corrected exploratory Pilot 01 evidence and
  measurement diagnostics.
- `data/results/research_record/`: historical or inconclusive derived results.

## Ola 2 raw files

- `modelo`, `snapshot` and `modo`: recorded configuration fields.
- `item_id`: public identifier linked to the metadata registry.
- `bloque`, `formato`, `principio`, `limpieza`: item metadata.
- `repeticion`: repeated administration index.
- `valor`: parsed score or choice.
- `estado_parseo`, `error`, `respuesta_cruda`, `timestamp`: parsing and
  provenance fields.

GPT modes are analysed separately. `deepseek_reasoner.csv` contains only
`thinking` rows. The original mixed DeepSeek file is in the research record.

## DSE raw files

- `situacion`: `trabajo` or `familia`.
- `set_id`, `repeticion`, `orden`: vignette-set and presentation identifiers.
- `perfil_1`–`perfil_3`: machine-readable recipient attributes.
- `monto_1`–`monto_3`: hypothetical CHF allocations.
- `share_1`–`share_3`: amount divided by CHF 18,000.
- parsing and raw-response fields are retained verbatim.

## MFQ raw files

- `variante`: prompt/format variant.
- `item_id`, `fundamento`: item and six-foundation code.
- `repeticion`, `score`, `estado_parseo`: repeated response and parser status.
- exact model and mode fields are retained.

`deepseek_reasoner.csv` contains only `thinking` rows. The matched language
comparison uses `lente_A`.
