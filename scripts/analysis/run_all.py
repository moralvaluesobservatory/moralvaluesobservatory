"""Regenerate every derived result, then rebuild the integrity manifest."""
from __future__ import annotations

from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULTS = ROOT / "data/results"
sys.path.insert(0, str(HERE))

# Remove stale derived CSVs so withdrawn or renamed outputs cannot survive a run.
for path in RESULTS.rglob("*.csv"):
    path.unlink()
for directory in [
    RESULTS / "active",
    RESULTS / "evidence_to_date",
    RESULTS / "research_record",
]:
    directory.mkdir(parents=True, exist_ok=True)

for script in [
    "reliability.py",
    "analyze_ola2.py",
    "analyze_dse.py",
    "analyze_mfq.py",
    "build_manifest.py",
]:
    print(f"\n=== {script} ===")
    runpy.run_path(str(HERE / script), run_name="__main__")

print("\nAll analyses completed.")
