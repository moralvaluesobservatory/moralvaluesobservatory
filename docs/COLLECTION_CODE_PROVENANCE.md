# Collection-code provenance

## DSE

The five DSE collection notebooks remain under
`provenance/original_notebooks/dse/`. The final raw files identify the five
configurations used in the active case.

The DeepSeek DSE notebook contains earlier trial cells that mention
`deepseek-chat`. Those trial cells are not the final complete DSE collection,
and no Chat/Reasoner mode aggregation occurs in the DSE data. This historical
notebook is retained because it is the available provenance for the active
DeepSeek DSE file.

## Ola 2

Active evidence provenance remains for Opus, GPT, GLM and Fable. The original
DeepSeek Ola 2 notebook collected both `deepseek-chat` (`non_thinking`) and
`deepseek-reasoner` (`thinking`). It has been moved to:

`research_record/pilot_01/excluded_configurations/deepseek_chat/provenance/`

The original mixed CSVs are archived beside it. Derived analyses use only
verbatim `thinking` rows copied into `deepseek_reasoner.csv` and
`deepseek_reasoner_3option.csv`.

## MFQ

Raw MFQ response files are present, but the package does not contain the
collection notebooks, exact prompt-construction code, provider parameters or
complete translation provenance. This limitation is attached to every MFQ
output.
