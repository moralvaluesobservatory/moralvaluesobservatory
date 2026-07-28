"""Publication invariants for the representation-oriented core."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "data/results/active"
EVIDENCE = ROOT / "data/results/evidence_to_date"
RECORD = ROOT / "data/results/research_record"


# ----------------------------------------------------- third-party material
def test_no_public_instrument_text():
    forbidden = "instrumento_ola2_meindl"
    for path in ROOT.rglob("*"):
        if path.is_file():
            assert forbidden not in path.name, f"private instrument file present: {path}"


def test_registry_has_65_items_and_no_text_column():
    registry = pd.read_csv(ROOT / "data/metadata/ola2_instrument_registry.csv")
    assert len(registry) == 65
    assert not any(
        column.lower() in {"text", "texto", "item_text"}
        for column in registry.columns
    )
    assert registry.administered_text_sha256.notna().all()


def test_instrument_attributed_to_meindl_not_naser():
    registry = pd.read_csv(ROOT / "data/metadata/ola2_instrument_registry.csv")
    authors = " ".join(registry.source_author.dropna().astype(str)).lower()
    assert "meindl" in authors
    assert "naser" not in authors


# ------------------------------------------------ DeepSeek Chat exclusion
def test_deepseek_chat_is_excluded_from_analysis_sources():
    reasoner_files = [
        ROOT / "data/raw/ola2/deepseek_reasoner.csv",
        ROOT / "data/raw/ola2/deepseek_reasoner_3option.csv",
        ROOT / "data/raw/mfq/english/deepseek_reasoner.csv",
    ]
    for path in reasoner_files:
        assert path.exists(), f"missing filtered reasoner file: {path}"
        data = pd.read_csv(path)
        assert set(data.modo.astype(str)) == {"thinking"}
    assert not (ROOT / "data/raw/ola2/deepseek.csv").exists()
    assert not (ROOT / "data/raw/ola2/deepseek_3option.csv").exists()
    assert not (ROOT / "data/raw/mfq/english/deepseek.csv").exists()


def test_deepseek_chat_is_absent_from_derived_results():
    for path in (ROOT / "data/results").rglob("*.csv"):
        text = path.read_text(encoding="utf-8").lower()
        assert "non_thinking" not in text
        assert "deepseek-chat" not in text


def test_excluded_mixed_sources_remain_in_research_record():
    archive = ROOT / "research_record/pilot_01/excluded_configurations/deepseek_chat"
    assert (archive / "raw_originals/ola2/deepseek_mixed_original.csv").exists()
    assert (archive / "raw_originals/mfq_english/deepseek_mixed_original.csv").exists()
    assert (archive / "provenance/DeepSeek_ola2_mixed_modes.ipynb").exists()


# ---------------------------------------------------------- withdrawn claims
def test_withdrawn_correlation_is_not_recomputed():
    for path in (ROOT / "data/results").rglob("*.csv"):
        columns = " ".join(pd.read_csv(path, nrows=0).columns).lower()
        assert "five_family_correlation" not in columns
    assert not any((ROOT / "data/results").rglob("ola2_declared_vs_chosen.csv"))
    assert not any((ROOT / "data/results").rglob("ola2_leave_one_item_out.csv"))


def test_no_single_nearest_country_claim():
    assert not any((ROOT / "data/results").rglob("mfq_reference_profile.csv"))
    candidate = pd.read_csv(
        EVIDENCE / "mfq_top3_national_mean_candidates_by_variant.csv"
    )
    assert {1, 2, 3} == set(candidate.rank_within_variant)
    assert candidate.interpretation_limit.str.contains("not evidence", case=False).all()


# ------------------------------------------------------ statistical honesty
def test_ola2_item_counts_are_correct_and_modes_are_separate():
    estimates = pd.read_csv(EVIDENCE / "ola2_estimates_by_configuration.csv")
    assert (estimates.declared_scale_items_total == 36).all()
    assert (estimates.proportionality_items == 16).all()
    assert (estimates.equality_items == 4).all()
    assert (estimates.contrast_items == 20).all()
    assert (estimates.chosen_dilemmas == 7).all()
    assert len(estimates[estimates.family == "GPT"]) == 2
    assert estimates.configuration.is_unique


def test_repetition_diagnostics_do_not_replace_cluster_counts():
    diagnostics = pd.read_csv(EVIDENCE / "measurement_repetition_diagnostics.csv")
    assert len(diagnostics) > 0
    assert (diagnostics.model_based_effective_n_diagnostic < diagnostics.generation_rows).all()
    assert (diagnostics.task_clusters < diagnostics.generation_rows).all()
    assert diagnostics.interpretation_limit.str.contains("not a participant", case=False).all()


def test_dilemma_intervals_remain_wide():
    estimates = pd.read_csv(EVIDENCE / "ola2_estimates_by_configuration.csv")
    assert (estimates.chosen_interval_width > 0.4).all()


def test_historical_version_comparison_is_not_claimed_as_monitoring():
    change = pd.read_csv(RECORD / "opus_version_comparison_historical_inconclusive.csv")
    assert not change.threshold_preregistered.any()
    assert set(change.evidence_status) == {"historical_inconclusive"}
    assert change.interval_includes_zero.all()
    assert change.interpretation_limit.str.contains("not a demonstrated", case=False).all()


# -------------------------------------------------- reference comparison
def test_dse_uses_reported_point_estimates_not_human_intervals():
    comparison = pd.read_csv(ACTIVE / "dse_reported_reference_position.csv")
    required = {
        "reported_reference_min",
        "reported_reference_max",
        "model_ci_below_all_reported_point_estimates",
        "human_uncertainty_included",
        "interpretation_limit",
    }
    assert required <= set(comparison.columns)
    assert "intervals_overlap" not in comparison.columns
    assert len(comparison) == 10
    assert comparison.model_ci_below_all_reported_point_estimates.all()
    assert not comparison.human_uncertainty_included.any()
    assert comparison.interpretation_limit.str.contains("not an individual", case=False).all()


def test_no_legacy_human_range_outputs_remain():
    names = {path.name for path in (ROOT / "data/results").rglob("*.csv")}
    assert "dse_human_range.csv" not in names
    assert "mfq_human_range.csv" not in names
    assert "mfq_language_comparison.csv" not in names


def test_dse_coefficients_report_clusters_and_bootstrap():
    coefficients = pd.read_csv(ACTIVE / "dse_coefficients.csv")
    assert {"vignette_sets", "generation_rows", "bootstrap_replicates", "bootstrap_unit"} <= set(coefficients.columns)
    assert (coefficients.vignette_sets < coefficients.generation_rows).all()
    assert (coefficients.bootstrap_replicates >= 5_000).all()
    assert set(coefficients.bootstrap_unit) == {"vignette_set"}


def test_human_reference_registry_keeps_provenance():
    human = pd.read_csv(ROOT / "data/reference/human_dse_reference_registry.csv")
    for column in [
        "source_id",
        "doi",
        "page",
        "figure_table",
        "sample",
        "situation",
        "record_type",
    ]:
        assert column in human.columns
    assert human.page.notna().all()


def test_mfq_is_marked_as_national_means_with_incomplete_provenance():
    ranges = pd.read_csv(EVIDENCE / "mfq_reported_national_mean_position.csv")
    assert set(ranges.human_reference_level) == {"national_means_not_individuals"}
    assert set(ranges.human_reference_provenance) == {"incomplete_in_current_package"}
    assert "variant_dependent" in set(ranges.position_verdict)


def test_language_comparison_is_matched_and_exploratory():
    language = pd.read_csv(EVIDENCE / "mfq_language_comparison_matched.csv")
    assert language.same_variant.all()
    assert language.matching_recorded_mode.all()
    assert (language.variant_english == language.variant_mandarin).all()
    assert set(language.evidence_status) == {"exploratory_matched_reanalysis"}
    assert not language.label.str.contains("chat", case=False).any()


def test_result_status_registry_points_to_existing_sources():
    registry = pd.read_csv(ROOT / "data/metadata/result_status_registry.csv")
    for source in registry.source_file:
        assert (ROOT / source).exists(), f"status registry source missing: {source}"
    assert set(registry.status) >= {"active", "exploratory", "excluded", "historical_inconclusive"}


# ------------------------------------------------------------- dependencies
def test_scipy_is_declared():
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").lower()
    assert "scipy" in requirements


# ------------------------------------------------------------- provenance
def test_original_notebooks_and_archived_mixed_notebook_present():
    active = list((ROOT / "provenance/original_notebooks").rglob("*.ipynb"))
    archived = list(
        (ROOT / "research_record/pilot_01/excluded_configurations/deepseek_chat/provenance").rglob("*.ipynb")
    )
    assert len(active) == 9
    assert len(archived) == 1


def test_notebooks_contain_no_literal_api_keys():
    notebook_roots = [
        ROOT / "provenance/original_notebooks",
        ROOT / "research_record/pilot_01/excluded_configurations/deepseek_chat/provenance",
    ]
    for notebook_root in notebook_roots:
        for path in notebook_root.rglob("*.ipynb"):
            text = json.dumps(json.load(path.open(encoding="utf-8")))
            assert "sk-ant-" not in text and "sk-proj-" not in text


def test_manifest_matches_every_listed_file():
    manifest = ROOT / "data/metadata/file_manifest_sha256.csv"
    with manifest.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) > 70
    for row in rows:
        target = ROOT / row["path"]
        assert target.exists(), f"manifest lists missing file {row['path']}"
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        assert digest == row["sha256"], f"hash mismatch for {row['path']}"
