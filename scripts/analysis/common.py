"""Shared analysis utilities.

Repeated generations of the same item or scenario are observations of response
variability, not independent people or independent tasks. Inference therefore
resamples whole task clusters (items or vignette sets), never individual rows.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RESULTS = DATA / "results"
ACTIVE_RESULTS = RESULTS / "active"
EVIDENCE_RESULTS = RESULTS / "evidence_to_date"
RECORD_RESULTS = RESULTS / "research_record"
for directory in (RESULTS, ACTIVE_RESULTS, EVIDENCE_RESULTS, RECORD_RESULTS):
    directory.mkdir(parents=True, exist_ok=True)

FOUNDATIONS = ["Care", "Equality", "Proportionality", "Loyalty", "Authority", "Purity"]
FOUNDATION_MAP = {
    "CARE": "Care",
    "EQUA": "Equality",
    "PROP": "Proportionality",
    "LOYA": "Loyalty",
    "AUTH": "Authority",
    "PURI": "Purity",
}
BOOTSTRAP_REPLICATES = 10_000
SEED = 20260728


def zscore(values):
    values = np.asarray(values, dtype=float)
    sd = values.std(ddof=0)
    return np.zeros_like(values) if sd == 0 else (values - values.mean()) / sd


def profile_correlation(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if np.allclose(a, a[0]) or np.allclose(b, b[0]):
        return np.nan
    return float(np.corrcoef(a - a.mean(), b - b.mean())[0, 1])


def sha256_file(path: Path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def icc_design_effect(df, cluster_col, value_col):
    """Return an ICC diagnostic, design effect and model-based effective n.

    ``effective_n`` is a diagnostic under this variance-components model. It is
    never a participant count and never replaces the number of task clusters.
    """
    grouped = df.groupby(cluster_col)[value_col]
    cluster_size_mean = float(grouped.size().mean())
    within_variance = float(grouped.var(ddof=1).mean())
    cluster_mean_variance = float(grouped.mean().var(ddof=1))
    between_variance = max(cluster_mean_variance - within_variance / cluster_size_mean, 0.0)
    denominator = between_variance + within_variance
    icc = between_variance / denominator if denominator > 0 else np.nan
    design_effect = 1 + (cluster_size_mean - 1) * icc
    effective_n = len(df) / design_effect if design_effect and design_effect > 0 else np.nan
    return icc, design_effect, cluster_size_mean, effective_n


def cluster_bootstrap(df, cluster_col, statistic, replicates=BOOTSTRAP_REPLICATES, seed=SEED):
    """Resample whole clusters with replacement and return the statistic."""
    rng = np.random.default_rng(seed)
    groups = [group for _, group in df.groupby(cluster_col)]
    count = len(groups)
    output = []
    for _ in range(replicates):
        indices = rng.integers(0, count, count)
        sample = pd.concat([groups[index] for index in indices], ignore_index=True)
        try:
            value = statistic(sample)
        except Exception:
            continue
        if value is not None and not (isinstance(value, float) and np.isnan(value)):
            output.append(value)
    return np.asarray(output, dtype=float)


def ci95(distribution):
    if len(distribution) == 0:
        return float("nan"), float("nan")
    low, high = np.percentile(distribution, [2.5, 97.5])
    return float(low), float(high)


def reported_reference_position(value, reference_min, reference_max):
    """Position relative to selected published aggregate point estimates.

    This is not a measure of individual-level human representation. The bounds
    are the minimum and maximum of selected published aggregate estimates.
    """
    if any(np.isnan([value, reference_min, reference_max])):
        return "undetermined"
    if value < reference_min:
        return "below"
    if value > reference_max:
        return "above"
    return "within"


def cluster_bootstrap_mean(
    df,
    cluster_col,
    value_col,
    replicates=BOOTSTRAP_REPLICATES,
    seed=SEED,
):
    """Fast cluster bootstrap for a row-weighted mean.

    Whole clusters are sampled with replacement. Repeated rows remain together
    within their task cluster and are not treated as independent clusters.
    """
    grouped = df.groupby(cluster_col)[value_col]
    sums = grouped.sum().to_numpy(dtype=float)
    counts = grouped.count().to_numpy(dtype=float)
    cluster_count = len(sums)
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, cluster_count, size=(replicates, cluster_count))
    return sums[indices].sum(axis=1) / counts[indices].sum(axis=1)
