"""Active case study: hypothetical distributive allocations.

The active comparison reports model estimates relative to selected published
aggregate point estimates. It does not call that span a population range and
does not treat it as an uncertainty interval for the human side.

All model intervals resample whole vignette sets (``set_id``), never individual
generation rows.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import (
    ACTIVE_RESULTS,
    BOOTSTRAP_REPLICATES,
    ROOT,
    SEED,
    ci95,
    cluster_bootstrap_mean,
    reported_reference_position,
)

RAW = ROOT / "data/raw/dse"
FILES = sorted(RAW.glob("dse_*_20*.csv"))
HUMAN = pd.read_csv(ROOT / "data/reference/human_dse_reference_registry.csv")
COEFFICIENT_BOOTSTRAP_REPLICATES = 5_000

DUMMIES_WORK = {
    "performance_medium": ("desemp", "2"),
    "performance_high": ("desemp", "3"),
    "dedication_medium": ("dedic", "2"),
    "dedication_high": ("dedic", "3"),
    "tenure_8": ("anos", "8"),
    "tenure_16": ("anos", "16"),
    "female": ("genero", "f"),
    "name_slavic": ("origen", "eslavo"),
    "name_arabic": ("origen", "arabe"),
    "two_children": ("hijos", "2"),
    "poor_health": ("salud", "2"),
    "single": ("pareja", "2"),
}
DUMMIES_FAMILY = {
    "financial_tight": ("finanzas", "2"),
    "two_children": ("hijos", "2"),
    "poor_health": ("salud", "2"),
    "single": ("pareja", "2"),
    "attention_high": ("atencion", "3"),
    "attention_medium": ("atencion", "2"),
    "female": ("genero", "f"),
}


def gini3(values):
    sorted_values = np.sort(np.asarray(values, dtype=float))
    total = sorted_values.sum()
    if total <= 0:
        return np.nan
    count = len(sorted_values)
    weights = 2 * np.arange(1, count + 1) - count - 1
    return float(np.sum(weights * sorted_values) / (count * total))


def parse_attributes(profile):
    return dict(part.split("=", 1) for part in profile.split(";") if "=" in part)


def build_decision_design(df, dummies):
    output = []
    for _, row in df.iterrows():
        design_rows, outcome = [], []
        for recipient in (1, 2, 3):
            attributes = parse_attributes(row[f"perfil_{recipient}"])
            design_rows.append(
                [1.0 if attributes.get(key) == value else 0.0 for key, value in dummies.values()]
            )
            outcome.append(float(row[f"share_{recipient}"]) - 1 / 3)
        matrix = np.asarray(design_rows)
        outcome_array = np.asarray(outcome)
        output.append((matrix - matrix.mean(axis=0), outcome_array - outcome_array.mean()))
    return output


def equal_split_flag(df):
    return (
        np.isclose(df.share_1, 1 / 3)
        & np.isclose(df.share_2, 1 / 3)
        & np.isclose(df.share_3, 1 / 3)
    )


# Selected published aggregate point estimates. These are not individual-level
# ranges and do not include uncertainty intervals for the human side.
human = HUMAN[HUMAN.record_type == "exact_equal_split_rate"].copy()
human["value"] = pd.to_numeric(human.estimate, errors="coerce")
reference_spans = {}
for source_situation, data_situation in [
    ("inheritance/family", "familia"),
    ("work/bonus", "trabajo"),
]:
    subset = human[human.situation == source_situation].dropna(subset=["value"])
    if subset.empty:
        continue
    reference_spans[data_situation] = {
        "minimum": float(subset.value.min()),
        "maximum": float(subset.value.max()),
        "point_estimates": int(len(subset)),
        "samples": int(subset["sample"].nunique()),
        "source_records": "|".join(subset.source_record_id.astype(str))
        if "source_record_id" in subset.columns
        else "|".join(subset.index.astype(str)),
    }

integrity_rows = []
equal_split_rows = []
reference_position_rows = []
gini_rows = []
coefficient_rows = []

for file_index, path in enumerate(FILES):
    data = pd.read_csv(path)
    model = str(data.modelo.iloc[0])
    usable = data[data.estado_parseo.isin(["ok", "ajustado"])].copy()
    amount_sum = usable[["monto_1", "monto_2", "monto_3"]].sum(axis=1)
    share_sum = usable[["share_1", "share_2", "share_3"]].sum(axis=1)
    repetitions_by_set = usable.groupby(["situacion", "set_id"]).size()

    integrity_rows.append(
        {
            "dataset": path.name,
            "configuration": model,
            "rows": len(data),
            "usable_rows": len(usable),
            "usable_rate": round(len(usable) / len(data), 6),
            "vignette_sets": int(usable.set_id.nunique()),
            "repetitions_per_set_min": int(repetitions_by_set.min()),
            "repetitions_per_set_max": int(repetitions_by_set.max()),
            "amount_sum_failures": int((~np.isclose(amount_sum, 18_000)).sum()),
            "share_sum_failures": int((~np.isclose(share_sum, 1.0)).sum()),
            "negative_amount_rows": int(
                (usable[["monto_1", "monto_2", "monto_3"]] < 0).any(axis=1).sum()
            ),
            "duplicate_decision_rows": int(
                data.duplicated(["situacion", "set_id", "repeticion"]).sum()
            ),
        }
    )

    for situation in ["trabajo", "familia"]:
        subset = usable[usable.situacion == situation].copy()
        if subset.empty:
            continue
        subset["equal_split"] = equal_split_flag(subset)
        observed = float(subset.equal_split.mean() * 100)
        bootstrap = (
            cluster_bootstrap_mean(
                subset,
                "set_id",
                "equal_split",
                replicates=BOOTSTRAP_REPLICATES,
                seed=SEED + file_index,
            )
            * 100
        )
        ci_low, ci_high = ci95(bootstrap)
        scenario_count = int(subset.set_id.nunique())
        repetition_counts = subset.groupby("set_id").size()

        equal_split_rows.append(
            {
                "configuration": model,
                "situation": situation,
                "generation_rows": len(subset),
                "vignette_sets": scenario_count,
                "repetitions_per_set_min": int(repetition_counts.min()),
                "repetitions_per_set_max": int(repetition_counts.max()),
                "equal_split_pct": round(observed, 3),
                "model_ci_lo": round(ci_low, 3),
                "model_ci_hi": round(ci_high, 3),
                "bootstrap_unit": "vignette_set",
                "bootstrap_replicates": BOOTSTRAP_REPLICATES,
            }
        )

        reference = reference_spans.get(situation)
        if reference:
            below_all = bool(ci_high < reference["minimum"])
            above_all = bool(ci_low > reference["maximum"])
            intersects_span = bool(
                ci_high >= reference["minimum"] and ci_low <= reference["maximum"]
            )
            if below_all:
                gap = reference["minimum"] - ci_high
            elif above_all:
                gap = ci_low - reference["maximum"]
            else:
                gap = 0.0
            reference_position_rows.append(
                {
                    "configuration": model,
                    "situation": situation,
                    "model_pct": round(observed, 3),
                    "model_ci_lo": round(ci_low, 3),
                    "model_ci_hi": round(ci_high, 3),
                    "reported_reference_min": reference["minimum"],
                    "reported_reference_max": reference["maximum"],
                    "reported_point_estimates": reference["point_estimates"],
                    "reported_samples": reference["samples"],
                    "point_position": reported_reference_position(
                        observed, reference["minimum"], reference["maximum"]
                    ),
                    "model_ci_below_all_reported_point_estimates": below_all,
                    "model_ci_above_all_reported_point_estimates": above_all,
                    "model_ci_intersects_point_estimate_span": intersects_span,
                    "gap_from_model_ci_to_nearest_reported_estimate": round(float(gap), 3),
                    "human_uncertainty_included": False,
                    "interpretation_limit": (
                        "Selected published aggregate point estimates; not an individual-level "
                        "population range and not a human confidence interval."
                    ),
                }
            )

    work = usable[usable.situacion == "trabajo"].copy()
    work["gini"] = work.apply(
        lambda row: gini3([row.share_1, row.share_2, row.share_3]), axis=1
    )
    valid_work = work.dropna(subset=["gini"])
    gini_bootstrap = cluster_bootstrap_mean(
        valid_work,
        "set_id",
        "gini",
        replicates=BOOTSTRAP_REPLICATES,
        seed=SEED + file_index,
    )
    ci_low, ci_high = ci95(gini_bootstrap)
    gini_rows.append(
        {
            "configuration": model,
            "situation": "trabajo",
            "generation_rows": len(valid_work),
            "vignette_sets": int(valid_work.set_id.nunique()),
            "gini_mean": round(float(valid_work.gini.mean()), 6),
            "model_ci_lo": round(ci_low, 6),
            "model_ci_hi": round(ci_high, 6),
            "bootstrap_unit": "vignette_set",
            "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        }
    )

    rng = np.random.default_rng(SEED + file_index)
    for situation, dummies in [("trabajo", DUMMIES_WORK), ("familia", DUMMIES_FAMILY)]:
        subset = usable[usable.situacion == situation]
        if subset.empty:
            continue
        scenario_ids = subset.set_id.unique()
        by_scenario = {}
        for scenario_id, group in subset.groupby("set_id"):
            decisions = build_decision_design(group, dummies)
            by_scenario[scenario_id] = (
                np.vstack([matrix for matrix, _ in decisions]),
                np.concatenate([outcome for _, outcome in decisions]),
            )
        full_matrix = np.vstack([value[0] for value in by_scenario.values()])
        full_outcome = np.concatenate([value[1] for value in by_scenario.values()])
        coefficients = np.linalg.lstsq(full_matrix, full_outcome, rcond=None)[0] * 100

        bootstrapped_coefficients = []
        for _ in range(COEFFICIENT_BOOTSTRAP_REPLICATES):
            selected = rng.choice(scenario_ids, size=len(scenario_ids), replace=True)
            matrix = np.vstack([by_scenario[key][0] for key in selected])
            outcome = np.concatenate([by_scenario[key][1] for key in selected])
            try:
                bootstrapped_coefficients.append(
                    np.linalg.lstsq(matrix, outcome, rcond=None)[0] * 100
                )
            except np.linalg.LinAlgError:
                continue
        bootstrapped_coefficients = np.asarray(bootstrapped_coefficients)

        for coefficient_index, variable in enumerate(dummies):
            ci_low, ci_high = np.percentile(
                bootstrapped_coefficients[:, coefficient_index], [2.5, 97.5]
            )
            coefficient_rows.append(
                {
                    "configuration": model,
                    "situation": situation,
                    "variable": variable,
                    "generation_rows": len(subset),
                    "vignette_sets": int(len(scenario_ids)),
                    "beta_percentage_points": round(float(coefficients[coefficient_index]), 4),
                    "model_ci_lo": round(float(ci_low), 4),
                    "model_ci_hi": round(float(ci_high), 4),
                    "model_ci_excludes_zero": bool(ci_low > 0 or ci_high < 0),
                    "bootstrap_unit": "vignette_set",
                    "bootstrap_replicates": COEFFICIENT_BOOTSTRAP_REPLICATES,
                }
            )

pd.DataFrame(integrity_rows).to_csv(ACTIVE_RESULTS / "dse_integrity.csv", index=False)
pd.DataFrame(equal_split_rows).to_csv(ACTIVE_RESULTS / "dse_equal_split.csv", index=False)
pd.DataFrame(reference_position_rows).to_csv(
    ACTIVE_RESULTS / "dse_reported_reference_position.csv", index=False
)
pd.DataFrame(gini_rows).to_csv(ACTIVE_RESULTS / "dse_gini.csv", index=False)
pd.DataFrame(coefficient_rows).to_csv(ACTIVE_RESULTS / "dse_coefficients.csv", index=False)

print(pd.DataFrame(reference_position_rows).to_string(index=False))
