# Release checks for v0.4.0

Performed on 28 July 2026.

- Analysis pipeline completed without error in the working environment.
- Test suite: 23 passed.
- Every path listed in the research-file manifest is checked by the test suite.
- `CITATION.cff` parses as YAML and declares version 0.4.0.
- No duplicate HTML identifiers were found in `docs/index.html`.
- Every internal anchor and local download link in the website resolves.
- Embedded JavaScript passes `node --check`.
- The standalone research ZIP, GitHub-ready ZIP and website ZIP pass archive
  integrity checks and SHA-256 verification.
- DeepSeek Chat strings and `non_thinking` rows are absent from all derived
  CSVs.
- DSE active results contain five configurations × two tasks.
- The corrected MFQ language output uses the same `lente_A` variant and matching
  recorded modes.
- Third-party Almås human microdata are not redistributed in this release.
- The 2022 attitudes study and the 2025 impartial-spectator experiment are
  identified as separate sources and future study stages.

## Environment used

- NumPy 2.3.5
- pandas 2.2.3
- SciPy 1.17.0
- pytest 9.0.2

A fully isolated dependency download was not repeated because the execution
environment does not expose a reliable package index. Required packages and
compatible version ranges are declared in `requirements.txt`.

Browser screenshot generation could not be completed in the container because
its Chromium runtime was blocked. Structural HTML, link, JavaScript, archive,
manifest and test-suite checks completed successfully.
