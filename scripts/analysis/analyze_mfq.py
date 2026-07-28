"""Evidence to date: MFQ-2 profiles, prompt sensitivity and language comparison.

The national reference span is the minimum and maximum of 19 national means,
not a distribution of individuals and not a measure of representation.
Language comparisons use the same ``lente_A`` variant and matching recorded
modes. DeepSeek Chat is excluded; only DeepSeek Reasoner rows are analysed.
MFQ collection-code provenance remains incomplete, so all outputs are marked
exploratory.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import (
    EVIDENCE_RESULTS,
    FOUNDATIONS,
    FOUNDATION_MAP,
    ROOT,
    profile_correlation,
    reported_reference_position,
    zscore,
)

ENG = ROOT / "data/raw/mfq/english"
ZH = ROOT / "data/raw/mfq/mandarin"
HUMAN = pd.read_csv(ROOT / "data/reference/mfq2_human_reference_frame.csv")
VARIANTS = ["lente_A", "canonica", "lente_B", "lente_C"]
LANGUAGE_VARIANT = "lente_A"

ENGLISH_CONFIGURATIONS = [
    {
        "label": "Opus 4.8",
        "family": "Claude Opus",
        "configuration": "opus-4.8",
        "file": ENG / "opus_generations.csv",
        "model_filter": "opus-4.8",
        "mode_filter": None,
    },
    {
        "label": "GPT 5.5 — low reasoning",
        "family": "GPT",
        "configuration": "gpt-5.5 | reasoning=low",
        "file": ENG / "gpt.csv",
        "model_filter": "gpt-5.5",
        "mode_filter": "low",
    },
    {
        "label": "GPT 5.5 — high reasoning",
        "family": "GPT",
        "configuration": "gpt-5.5 | reasoning=high",
        "file": ENG / "gpt.csv",
        "model_filter": "gpt-5.5",
        "mode_filter": "high",
    },
    {
        "label": "DeepSeek Reasoner",
        "family": "DeepSeek",
        "configuration": "deepseek-reasoner | thinking",
        "file": ENG / "deepseek_reasoner.csv",
        "model_filter": "deepseek-v4-pro",
        "mode_filter": "thinking",
    },
    {
        "label": "GLM 5.2 — xhigh",
        "family": "GLM",
        "configuration": "glm-5.2 | reasoning=xhigh",
        "file": ENG / "glm.csv",
        "model_filter": "glm-5.2",
        "mode_filter": "xhigh",
    },
    {
        "label": "Fable 5 — adaptive",
        "family": "Claude Fable",
        "configuration": "claude-fable-5 | reasoning=adaptive",
        "file": ENG / "fable.csv",
        "model_filter": "claude-fable-5",
        "mode_filter": "adaptive",
    },
]

LANGUAGE_COMPARISONS = [
    {
        "label": "Opus 4.8",
        "english_file": ENG / "opus_generations.csv",
        "english_model": "opus-4.8",
        "english_mode": None,
        "mandarin_file": ZH / "opus.csv",
        "mandarin_model": "claude-opus-4-8",
        "mandarin_mode": "base",
    },
    {
        "label": "GPT 5.5 — high reasoning",
        "english_file": ENG / "gpt.csv",
        "english_model": "gpt-5.5",
        "english_mode": "high",
        "mandarin_file": ZH / "gpt.csv",
        "mandarin_model": "gpt-5.5",
        "mandarin_mode": "high",
    },
    {
        "label": "DeepSeek Reasoner",
        "english_file": ENG / "deepseek_reasoner.csv",
        "english_model": "deepseek-v4-pro",
        "english_mode": "thinking",
        "mandarin_file": ZH / "deepseek.csv",
        "mandarin_model": "deepseek-reasoner",
        "mandarin_mode": "thinking",
    },
    {
        "label": "GLM 5.2 — xhigh",
        "english_file": ENG / "glm.csv",
        "english_model": "glm-5.2",
        "english_mode": "xhigh",
        "mandarin_file": ZH / "glm.csv",
        "mandarin_model": "glm-5.2",
        "mandarin_mode": "xhigh",
    },
    {
        "label": "Fable 5 — adaptive",
        "english_file": ENG / "fable.csv",
        "english_model": "claude-fable-5",
        "english_mode": "adaptive",
        "mandarin_file": ZH / "fable.csv",
        "mandarin_model": "claude-fable-5",
        "mandarin_mode": "adaptive",
    },
]


def load_filtered(path, model=None, mode=None, variant=None):
    data = pd.read_csv(path)
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


def profile(data):
    return (
        data.groupby("foundation_name").score.mean().reindex(FOUNDATIONS).to_numpy()
    )


human_z = np.asarray(
    [zscore(row[FOUNDATIONS].astype(float).to_numpy()) for _, row in HUMAN.iterrows()]
)
reference_min = human_z.min(axis=0)
reference_max = human_z.max(axis=0)

integrity_rows = []
profile_rows = []
reference_position_rows = []
language_rows = []

for specification in ENGLISH_CONFIGURATIONS:
    raw = pd.read_csv(specification["file"])
    all_selected = load_filtered(
        specification["file"],
        model=specification["model_filter"],
        mode=specification["mode_filter"],
    )
    integrity_rows.append(
        {
            "label": specification["label"],
            "configuration": specification["configuration"],
            "language": "English",
            "dataset": specification["file"].name,
            "source_rows": len(raw),
            "selected_parse_ok_rows": len(all_selected),
            "variants": int(all_selected.variante.nunique()),
            "items": int(all_selected.item_id.nunique()),
            "source_model_labels": "|".join(sorted(all_selected.modelo.astype(str).unique())),
            "source_modes": "|".join(sorted(all_selected.modo.astype(str).unique()))
            if "modo" in all_selected.columns
            else "not_recorded",
            "collection_code_provenance": "incomplete",
        }
    )

    positions_by_foundation = {}
    for variant in VARIANTS:
        selected = load_filtered(
            specification["file"],
            model=specification["model_filter"],
            mode=specification["mode_filter"],
            variant=variant,
        )
        if selected.empty:
            continue
        raw_profile = profile(selected)
        standardized_profile = zscore(raw_profile)
        for foundation, raw_value, standardized_value in zip(
            FOUNDATIONS, raw_profile, standardized_profile
        ):
            profile_rows.append(
                {
                    "label": specification["label"],
                    "family": specification["family"],
                    "configuration": specification["configuration"],
                    "language": "English",
                    "variant": variant,
                    "foundation": foundation,
                    "mean_score": round(float(raw_value), 6),
                    "z_within_profile": round(float(standardized_value), 6),
                    "evidence_status": "exploratory; MFQ collection provenance incomplete",
                }
            )
        for foundation_index, foundation in enumerate(FOUNDATIONS):
            positions_by_foundation.setdefault(foundation, []).append(
                reported_reference_position(
                    standardized_profile[foundation_index],
                    reference_min[foundation_index],
                    reference_max[foundation_index],
                )
            )

    for foundation_index, foundation in enumerate(FOUNDATIONS):
        positions = positions_by_foundation.get(foundation, [])
        if not positions:
            continue
        unique_positions = set(positions)
        reference_position_rows.append(
            {
                "label": specification["label"],
                "configuration": specification["configuration"],
                "foundation": foundation,
                "reported_national_mean_z_min": round(
                    float(reference_min[foundation_index]), 6
                ),
                "reported_national_mean_z_max": round(
                    float(reference_max[foundation_index]), 6
                ),
                "national_means_in_reference_frame": int(len(HUMAN)),
                "variants_tested": len(positions),
                "variants_within": positions.count("within"),
                "variants_above": positions.count("above"),
                "variants_below": positions.count("below"),
                "position_verdict": positions[0]
                if len(unique_positions) == 1
                else "variant_dependent",
                "stable_across_variants": len(unique_positions) == 1,
                "human_reference_level": "national_means_not_individuals",
                "human_reference_provenance": "incomplete_in_current_package",
                "interpretation_limit": (
                    "Position relative to 19 selected national means; not evidence "
                    "of individual or subgroup representation."
                ),
            }
        )

for specification in LANGUAGE_COMPARISONS:
    english = load_filtered(
        specification["english_file"],
        model=specification["english_model"],
        mode=specification["english_mode"],
        variant=LANGUAGE_VARIANT,
    )
    mandarin = load_filtered(
        specification["mandarin_file"],
        model=specification["mandarin_model"],
        mode=specification["mandarin_mode"],
        variant=LANGUAGE_VARIANT,
    )
    if english.empty or mandarin.empty:
        continue
    english_profile = profile(english)
    mandarin_profile = profile(mandarin)
    language_rows.append(
        {
            "label": specification["label"],
            "english_model_label": specification["english_model"],
            "english_mode": specification["english_mode"] or "not_recorded",
            "mandarin_model_label": specification["mandarin_model"],
            "mandarin_mode": specification["mandarin_mode"] or "not_recorded",
            "variant_english": LANGUAGE_VARIANT,
            "variant_mandarin": LANGUAGE_VARIANT,
            "same_variant": True,
            "matching_recorded_mode": True,
            "profile_correlation_en_zh": round(
                float(profile_correlation(english_profile, mandarin_profile)), 6
            ),
            "mean_abs_z_shift": round(
                float(
                    np.nanmean(
                        np.abs(zscore(english_profile) - zscore(mandarin_profile))
                    )
                ),
                6,
            ),
            "evidence_status": "exploratory_matched_reanalysis",
            "interpretation_limit": (
                "One translated prompt variant; MFQ collection-code provenance is "
                "incomplete and exact provider identifiers differ for some families."
            ),
        }
    )

pd.DataFrame(integrity_rows).to_csv(
    EVIDENCE_RESULTS / "mfq_integrity_by_configuration.csv", index=False
)
pd.DataFrame(profile_rows).to_csv(
    EVIDENCE_RESULTS / "mfq_profiles_by_configuration.csv", index=False
)
pd.DataFrame(reference_position_rows).to_csv(
    EVIDENCE_RESULTS / "mfq_reported_national_mean_position.csv", index=False
)
pd.DataFrame(language_rows).to_csv(
    EVIDENCE_RESULTS / "mfq_language_comparison_matched.csv", index=False
)

summary = pd.DataFrame(reference_position_rows)
print(summary.groupby(["label", "position_verdict"]).size().unstack(fill_value=0).to_string())
print()
print(pd.DataFrame(language_rows).to_string(index=False))
