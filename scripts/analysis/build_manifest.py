"""SHA-256 manifest of every tracked file, for third-party integrity checks."""
from __future__ import annotations
import csv
from common import ROOT, sha256_file

SKIP_DIRS = {"__pycache__", ".pytest_cache", ".venv", ".git", "downloads"}
rows = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    if any(part in SKIP_DIRS for part in path.parts) or path.suffix == ".pyc":
        continue
    if path.name == "file_manifest_sha256.csv":
        continue
    rows.append({"path": path.relative_to(ROOT).as_posix(),
                 "bytes": path.stat().st_size,
                 "sha256": sha256_file(path)})

out = ROOT / "data/metadata/file_manifest_sha256.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256"])
    writer.writeheader(); writer.writerows(rows)
print(f"Manifest: {len(rows)} files")
