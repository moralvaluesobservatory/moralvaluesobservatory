"""Evidence to date: stated distributive criteria and dilemma choices.

This analysis does not compute a declared-versus-chosen correlation and does
not rank configurations from seven dilemmas. GPT reasoning modes are analysed
separately. DeepSeek Chat is excluded; only the archived collection's
``thinking`` rows, generated through the DeepSeek Reasoner endpoint, remain in
the evidence set.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from common import (
    EVIDENCE_RESULTS,
    RECORD_RESULTS,
    ROOT,
    SEED,
    ci95,
    cluster_bootstrap_mean,
)

RAW = ROOT / "data/raw/ola2"
META = pd.read_csv(ROOT / "data/metadata/ola2_instrument_registry.csv")

CONFIGURATIONS = [
    {
        "label": "Opus 4.8",
        "family": "Claude Opus",
        "configuration": "claude-opus-4-8",
        "file": "opus.csv",
        "model_filter": "claude-opus-4-8",
        "mode_filter": None,
    },
    {
        "label": "GPT 5.5 — low reasoning",
        "family": "GPT",
        "configuration": "gpt-5.5 | reasoning=low",
        "file": "gpt.csv",
        "model_filter": "gpt-5.5",
        "mode_filter": "low",
    },
    {
        "label": "GPT 5.5 — high reasoning",
        "family": "GPT",
        "configuration": "gpt-5.5 | reasoning=high",
        "file": "gpt.csv",
        "model_filter": "gpt-5.5",
        "mode_filter": "high",
    },
    {
        "label": "DeepSeek Reasoner",
        "family": "DeepSeek",
        "configuration": "deepseek-reasoner | thinking",
        "file": "deepseek_reasoner.csv",
        "model_filter": "deepseek-v4-pro",
        "mode_filter": "thinking",
    },
    {
        "label": "GLM 5.2 — xhigh",
        "family": "GLM",
        "configuration": "glm-5.2 | reasoning=xhigh",
        "file": "glm.csv",
        "model_filter": "glm-5.2",
        "mode_filter": "xhigh",
    },
    {
        "label": "Fable 5 — adaptive",
        "family": "Claude Fable",
        "configuration": "claude-fable-5 | reasoning=adaptive",
        "file": "fable.csv",
        "model_filter": "claude-fable-5",
        "mode_filter": "adaptive",
    },
]

THREE_OPTION_FILES = {
    "opus.csv": "opus_3option.csv",
    "gpt.csv": "gpt_3option.csv",
    "deepseek_reasoner.csv": "deepseek_reasoner_3option.csv",
    "glm.csv": "glm_3option.csv",
    "fable.csv": "fable_3option.csv",
}


def select_configuration(specification, dataframe):
    selected = dataframe.copy()
    if specification["model_filter"] is not None and "modelo" in selected.columns:
        selected = selected[selected.modelo == specification["model_filter"]]
    if specification["mode_filter"] is not None and "modo" in selected.columns:
        selected = selected[selected.modo == specification["mode_filter"]]
    return selected.copy()


def first_option(value):
    return None if pd.isna(value) else str(value).strip().split()[0]


integrity_rows = []
estimate_rows = []
per_dilemma_rows = []
three_option_rows = []

for configuration_index, specification in enumerate(CONFIGURATIONS):
    raw = pd.read_csv(RAW / specification["file"])
    selected = select_configuration(specification, raw)
    parsed = selected[selected.estado_parseo == "ok"].copy()
    parsed["value_num"] = pd.to_numeric(parsed.valor, errors="coerce")

    integrity_rows.append(
        {
            "label": specification["label"],
            "family": specification["family"],
            "configuration": specification["configuration"],
            "dataset": specification["file"],
            "generation_rows": len(selected),
            "parse_ok_rows": int((selected.estado_parseo == "ok").sum()),
            "parse_rate": round(float((selected.estado_parseo == "ok").mean()), 6),
            "unique_items": int(selected.item_id.nunique()),
            "source_model_label": "|".join(sorted(selected.modelo.astype(str).unique())),
            "source_modes": "|".join(sorted(selected.modo.astype(str).unique()))
            if "modo" in selected.columns
            else "not_recorded",
        }
    )

    declared = parsed[
        (parsed.bloque == "A_declarado_cdjs_largo") & (parsed.formato == "escala")
    ].dropna(subset=["value_num"])
    proportionality = declared[
        declared.principio.str.startswith("proporcionalidad", na=False)
    ].copy()
    equality = declared[declared.principio == "igualdad"].copy()
    observed_difference = float(
        proportionality.value_num.mean() - equality.value_num.mean()
    )
    proportionality_bootstrap = cluster_bootstrap_mean(
        proportionality,
        "item_id",
        "value_num",
        seed=SEED + configuration_index,
    )
    equality_bootstrap = cluster_bootstrap_mean(
        equality,
        "item_id",
        "value_num",
        seed=SEED + configuration_index + 500,
    )
    declared_ci_low, declared_ci_high = ci95(
        proportionality_bootstrap - equality_bootstrap
    )

    binary = parsed[
        (parsed.bloque == "B_dilema") & (parsed.formato == "binario")
    ].merge(
        META[
            [
                "item_id",
                "proportional_option",
                "equality_option",
                "scenario_label_es",
            ]
        ],
        on="item_id",
        how="left",
    )
    binary["is_proportional"] = binary.apply(
        lambda row: str(row.valor).strip() == first_option(row.proportional_option),
        axis=1,
    )
    chosen_fraction = float(binary.is_proportional.mean())
    chosen_bootstrap = cluster_bootstrap_mean(
        binary,
        "item_id",
        "is_proportional",
        seed=SEED + configuration_index + 900,
    )
    chosen_ci_low, chosen_ci_high = ci95(chosen_bootstrap)

    estimate_rows.append(
        {
            "label": specification["label"],
            "family": specification["family"],
            "configuration": specification["configuration"],
            "declared_proportionality_minus_equality": round(observed_difference, 4),
            "declared_ci_lo": round(declared_ci_low, 4),
            "declared_ci_hi": round(declared_ci_high, 4),
            "declared_ci_excludes_zero": bool(
                declared_ci_low > 0 or declared_ci_high < 0
            ),
            "declared_scale_items_total": int(declared.item_id.nunique()),
            "proportionality_items": int(proportionality.item_id.nunique()),
            "equality_items": int(equality.item_id.nunique()),
            "contrast_items": int(
                proportionality.item_id.nunique() + equality.item_id.nunique()
            ),
            "chosen_proportional_fraction": round(chosen_fraction, 4),
            "chosen_ci_lo": round(chosen_ci_low, 4),
            "chosen_ci_hi": round(chosen_ci_high, 4),
            "chosen_dilemmas": int(binary.item_id.nunique()),
            "chosen_interval_width": round(chosen_ci_high - chosen_ci_low, 4),
            "bootstrap_unit_declared": "item",
            "bootstrap_unit_chosen": "dilemma",
            "evidence_status": "exploratory; no declared-versus-chosen association inferred",
        }
    )

    for item_id, group in binary.groupby("item_id"):
        per_dilemma_rows.append(
            {
                "label": specification["label"],
                "configuration": specification["configuration"],
                "item_id": item_id,
                "scenario_label_es": group.scenario_label_es.iloc[0],
                "proportional_fraction": round(float(group.is_proportional.mean()), 4),
                "generation_rows": len(group),
            }
        )

    three_option_file = THREE_OPTION_FILES[specification["file"]]
    three_raw = pd.read_csv(RAW / three_option_file)
    three_selected = select_configuration(specification, three_raw)
    three_parsed = three_selected[three_selected.estado_parseo == "ok"]
    for (item_id, principle), group in three_parsed.groupby(
        ["item_id", "principio_elegido"]
    ):
        three_option_rows.append(
            {
                "label": specification["label"],
                "configuration": specification["configuration"],
                "item_id": item_id,
                "principle": principle,
                "generation_rows": len(group),
            }
        )

# Historical comparison only. It is not evidence that longitudinal monitoring
# has been demonstrated. The effect-size threshold was adopted in this
# reanalysis and was not preregistered.
version_rows = []
opus = pd.read_csv(RAW / "opus.csv")
opus = opus[opus.estado_parseo == "ok"].copy()
opus["value_num"] = pd.to_numeric(opus.valor, errors="coerce")
scale = opus[opus.formato == "escala"].dropna(subset=["value_num"])
per_item = scale.groupby(["modelo", "item_id"]).value_num.mean().unstack(0)
versions = sorted(per_item.columns)
adjusted_alpha = 0.05 / max(len(versions) - 1, 1)
for version_a, version_b in zip(versions[:-1], versions[1:]):
    pair = per_item[[version_a, version_b]].dropna()
    differences = pair[version_b] - pair[version_a]
    item_count = len(differences)
    standard_deviation = float(differences.std(ddof=1))
    standard_error = standard_deviation / np.sqrt(item_count)
    critical_value = float(stats.t.ppf(1 - adjusted_alpha / 2, item_count - 1))
    ci_low = float(differences.mean() - critical_value * standard_error)
    ci_high = float(differences.mean() + critical_value * standard_error)
    effect_size = (
        float(differences.mean() / standard_deviation)
        if standard_deviation > 0
        else np.nan
    )
    version_rows.append(
        {
            "from_version": version_a,
            "to_version": version_b,
            "paired_items": item_count,
            "mean_change": round(float(differences.mean()), 4),
            "ci_lo": round(ci_low, 4),
            "ci_hi": round(ci_high, 4),
            "alpha_bonferroni": round(adjusted_alpha, 4),
            "cohens_dz": round(effect_size, 4),
            "operational_threshold_abs_d": 0.5,
            "threshold_preregistered": False,
            "operational_flag_triggered": bool(abs(effect_size) >= 0.5),
            "interval_includes_zero": bool(ci_low <= 0 <= ci_high),
            "evidence_status": "historical_inconclusive",
            "interpretation_limit": (
                "Single-family retrospective comparison; not a demonstrated "
                "longitudinal monitoring programme."
            ),
        }
    )

pd.DataFrame(integrity_rows).to_csv(
    EVIDENCE_RESULTS / "ola2_integrity_by_configuration.csv", index=False
)
pd.DataFrame(estimate_rows).to_csv(
    EVIDENCE_RESULTS / "ola2_estimates_by_configuration.csv", index=False
)
pd.DataFrame(per_dilemma_rows).to_csv(
    EVIDENCE_RESULTS / "ola2_by_dilemma_and_configuration.csv", index=False
)
pd.DataFrame(three_option_rows).to_csv(
    EVIDENCE_RESULTS / "ola2_three_option_counts_by_configuration.csv", index=False
)
pd.DataFrame(version_rows).to_csv(
    RECORD_RESULTS / "opus_version_comparison_historical_inconclusive.csv", index=False
)

print(pd.DataFrame(estimate_rows).to_string(index=False))
print()
print(pd.DataFrame(version_rows).to_string(index=False))
