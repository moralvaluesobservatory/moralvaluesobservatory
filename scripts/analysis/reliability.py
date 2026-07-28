"""Measurement diagnostics for repeated generations and prompt variants.

The model-based effective n is retained as a diagnostic explaining why rows
cannot be used as independent sample size. The primary counts are always task
clusters and repetitions. No temperature claim is made because collection
settings differ across datasets.
"""
from __future__ import annotations

import pandas as pd

from common import (
    EVIDENCE_RESULTS,
    FOUNDATIONS,
    FOUNDATION_MAP,
    ROOT,
    icc_design_effect,
    profile_correlation,
)

OLA2 = ROOT / "data/raw/ola2"
MFQ_EN = ROOT / "data/raw/mfq/english"
HUMAN = pd.read_csv(ROOT / "data/reference/mfq2_human_reference_frame.csv")
VARIANTS = ["lente_A", "canonica", "lente_B", "lente_C"]

OLA_CONFIGURATIONS = [
    ("Opus 4.8", "claude-opus-4-8", "opus.csv", "claude-opus-4-8", None),
    ("GPT 5.5 — low reasoning", "gpt-5.5 | reasoning=low", "gpt.csv", "gpt-5.5", "low"),
    ("GPT 5.5 — high reasoning", "gpt-5.5 | reasoning=high", "gpt.csv", "gpt-5.5", "high"),
    ("DeepSeek Reasoner", "deepseek-reasoner | thinking", "deepseek_reasoner.csv", "deepseek-v4-pro", "thinking"),
    ("GLM 5.2 — xhigh", "glm-5.2 | reasoning=xhigh", "glm.csv", "glm-5.2", "xhigh"),
    ("Fable 5 — adaptive", "claude-fable-5 | reasoning=adaptive", "fable.csv", "claude-fable-5", "adaptive"),
]

MFQ_CONFIGURATIONS = [
    ("Opus 4.8", "opus-4.8", "opus_generations.csv", "opus-4.8", None),
    ("GPT 5.5 — low reasoning", "gpt-5.5 | reasoning=low", "gpt.csv", "gpt-5.5", "low"),
    ("GPT 5.5 — high reasoning", "gpt-5.5 | reasoning=high", "gpt.csv", "gpt-5.5", "high"),
    ("DeepSeek Reasoner", "deepseek-reasoner | thinking", "deepseek_reasoner.csv", "deepseek-v4-pro", "thinking"),
    ("GLM 5.2 — xhigh", "glm-5.2 | reasoning=xhigh", "glm.csv", "glm-5.2", "xhigh"),
    ("Fable 5 — adaptive", "claude-fable-5 | reasoning=adaptive", "fable.csv", "claude-fable-5", "adaptive"),
]


def load_ola2(filename, model=None, mode=None):
    data = pd.read_csv(OLA2 / filename)
    data = data[data.estado_parseo == "ok"].copy()
    if model is not None and "modelo" in data.columns:
        data = data[data.modelo == model]
    if mode is not None and "modo" in data.columns:
        data = data[data.modo == mode]
    data["value_num"] = pd.to_numeric(data.valor, errors="coerce")
    return data


def load_mfq(filename, model=None, mode=None, variant=None):
    data = pd.read_csv(MFQ_EN / filename)
    data = data[data.estado_parseo == "ok"].copy()
    if model is not None and "modelo" in data.columns:
        data = data[data.modelo == model]
    if mode is not None and "modo" in data.columns:
        data = data[data.modo == mode]
    if variant is not None and "variante" in data.columns:
        data = data[data.variante == variant]
    data["score"] = pd.to_numeric(data.score, errors="coerce")
    data["foundation_name"] = data.fundamento.map(FOUNDATION_MAP)
    return data.dropna(subset=["score", "foundation_name"])


diagnostic_rows = []
for label, configuration, filename, model, mode in OLA_CONFIGURATIONS:
    data = load_ola2(filename, model=model, mode=mode)
    scale = data[data.formato == "escala"].dropna(subset=["value_num"])
    icc, design_effect, repetitions_mean, effective_n = icc_design_effect(
        scale, "item_id", "value_num"
    )
    per_item_sd = scale.groupby("item_id").value_num.std(ddof=0)
    diagnostic_rows.append(
        {
            "label": label,
            "configuration": configuration,
            "instrument": "ola2_scale",
            "generation_rows": len(scale),
            "task_clusters": int(scale.item_id.nunique()),
            "repetitions_per_cluster_mean": round(repetitions_mean, 2),
            "icc_diagnostic": round(icc, 4),
            "design_effect_diagnostic": round(design_effect, 2),
            "model_based_effective_n_diagnostic": round(effective_n, 1),
            "deterministic_clusters": int((per_item_sd == 0).sum()),
            "deterministic_share": round(float((per_item_sd == 0).mean()), 4),
            "interpretation_limit": (
                "Effective n is a variance-components diagnostic, not a participant "
                "count or substitute for task-cluster count."
            ),
        }
    )

for label, configuration, filename, model, mode in MFQ_CONFIGURATIONS:
    data = load_mfq(filename, model=model, mode=mode, variant="canonica")
    if data.empty:
        continue
    icc, design_effect, repetitions_mean, effective_n = icc_design_effect(
        data, "item_id", "score"
    )
    per_item_sd = data.groupby("item_id").score.std(ddof=0)
    diagnostic_rows.append(
        {
            "label": label,
            "configuration": configuration,
            "instrument": "mfq2_canonical_variant",
            "generation_rows": len(data),
            "task_clusters": int(data.item_id.nunique()),
            "repetitions_per_cluster_mean": round(repetitions_mean, 2),
            "icc_diagnostic": round(icc, 4),
            "design_effect_diagnostic": round(design_effect, 2),
            "model_based_effective_n_diagnostic": round(effective_n, 1),
            "deterministic_clusters": int((per_item_sd == 0).sum()),
            "deterministic_share": round(float((per_item_sd == 0).mean()), 4),
            "interpretation_limit": (
                "Effective n is a variance-components diagnostic, not a participant "
                "count or substitute for task-cluster count."
            ),
        }
    )

measurement_diagnostics = pd.DataFrame(diagnostic_rows)
measurement_diagnostics.to_csv(
    EVIDENCE_RESULTS / "measurement_repetition_diagnostics.csv", index=False
)

variant_rows = []
candidate_rows = []
for label, configuration, filename, model, mode in MFQ_CONFIGURATIONS:
    nearest_by_variant = {}
    for variant in VARIANTS:
        data = load_mfq(filename, model=model, mode=mode, variant=variant)
        if data.empty:
            continue
        profile = (
            data.groupby("foundation_name").score.mean().reindex(FOUNDATIONS).to_numpy()
        )
        correlations = sorted(
            (
                (
                    row.country,
                    profile_correlation(
                        profile, row[FOUNDATIONS].astype(float).to_numpy()
                    ),
                )
                for _, row in HUMAN.iterrows()
            ),
            key=lambda value: value[1],
            reverse=True,
        )
        nearest_by_variant[variant] = correlations[0]
        for rank, (country, correlation) in enumerate(correlations[:3], start=1):
            candidate_rows.append(
                {
                    "label": label,
                    "configuration": configuration,
                    "variant": variant,
                    "rank_within_variant": rank,
                    "country_national_mean": country,
                    "profile_correlation": round(float(correlation), 6),
                    "interpretation_limit": (
                        "Similarity to a national mean is not evidence of individual "
                        "or subgroup representation."
                    ),
                }
            )
    if not nearest_by_variant:
        continue
    countries = [value[0] for value in nearest_by_variant.values()]
    row = {
        "label": label,
        "configuration": configuration,
        "variants_tested": len(nearest_by_variant),
        "distinct_nearest_national_means": len(set(countries)),
        "same_nearest_national_mean_across_variants": len(set(countries)) == 1,
        "countries_observed": "|".join(sorted(set(countries))),
        "evidence_status": "prompt_variant_sensitivity",
    }
    for variant in VARIANTS:
        row[f"nearest_{variant}"] = nearest_by_variant.get(variant, (None, None))[0]
    variant_rows.append(row)

variant_stability = pd.DataFrame(variant_rows)
variant_stability.to_csv(
    EVIDENCE_RESULTS / "mfq_prompt_variant_sensitivity.csv", index=False
)
pd.DataFrame(candidate_rows).to_csv(
    EVIDENCE_RESULTS / "mfq_top3_national_mean_candidates_by_variant.csv", index=False
)

print(measurement_diagnostics.to_string(index=False))
print()
print(variant_stability.to_string(index=False))
