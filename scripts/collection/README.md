# Collection-code policy

Collection notebooks document what was run but are not the analytical source
of truth. Raw files and exact selection rules in the analysis scripts govern
derived results.

The complete Meindl-derived prompt file is deliberately absent. A lawful local
copy may be checked with `validate_private_meindl_file.py` against the public
item identifiers and normalized SHA-256 hashes.

## Active provenance

- Five DSE notebooks remain in `provenance/original_notebooks/dse/`.
- Ola 2 notebooks for Opus, GPT, GLM and Fable remain in
  `provenance/original_notebooks/ola2/`.

## Excluded mixed DeepSeek collection

The original DeepSeek Ola 2 notebook collected both `deepseek-chat` and
`deepseek-reasoner`. It and the mixed raw files are retained only in
`research_record/pilot_01/excluded_configurations/deepseek_chat/`.

The current pipeline uses filtered verbatim `thinking` rows in
`deepseek_reasoner.csv` files and never analyses `non_thinking` rows.

The DeepSeek DSE notebook contains earlier trial cells mentioning
`deepseek-chat`; its final collection and raw DSE file are treated separately
from the excluded Ola 2/MFQ mode aggregation. This limitation is documented in
`docs/COLLECTION_CODE_PROVENANCE.md`.
