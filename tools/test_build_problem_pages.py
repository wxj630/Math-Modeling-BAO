from __future__ import annotations

from pathlib import Path

from build_problem_pages import build_problem_page, group_baselines, group_by_problem, group_outstanding, read_csv


ROOT = Path(__file__).resolve().parents[1]


def test_problem_page_contains_global_reports() -> None:
    problems = {row["problem_id"]: row for row in read_csv("mcm/problem_index.csv")}
    questions = group_by_problem(read_csv("mcm/question_solution_index.csv"))
    baselines = group_baselines(read_csv("mcm/generic_baselines/generic_baseline_index.csv"))

    page = build_problem_page("mcm-track", problems["2015-C"], questions["2015-C"], baselines["2015-C"])

    required_fragments = [
        "## Baseline 全局报告",
        "## Advanced 全局报告",
        "## Advanced 相对 Baseline 的优势",
        "代码入口",
        "实验结果",
        "建模优势",
        "结果优势",
        "### q01 ICM 组织人力资本网络模型",
        "Baseline：从 `network_path_baseline`",
        "Advanced：",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in page]
    assert not missing, f"missing fragments: {missing}"


def test_problem_page_renders_outstanding_report_when_available() -> None:
    problems = {row["problem_id"]: row for row in read_csv("mcm/problem_index.csv")}
    questions = group_by_problem(read_csv("mcm/question_solution_index.csv"))
    baselines = group_baselines(read_csv("mcm/generic_baselines/generic_baseline_index.csv"))
    outstanding = {
        "problem_id": "2025-C",
        "paper_id": "2505964",
        "paper_title": "2028 Olympic Medal Predictions Based on Random Forest Model",
        "methods": "athlete ability features + sport random forest + Monte Carlo medal allocation",
        "solution_path": "mcm/outstanding_solutions/2025/C/2505964/solution.py",
        "report_path": "mcm/outstanding_solutions/2025/C/2505964/report.md",
        "result_path": "mcm/outstanding_solutions/2025/C/2505964/result.json",
        "artifact_dir": "mcm/outstanding_solutions/2025/C/2505964/artifacts",
    }

    page = build_problem_page(
        "mcm-track",
        problems["2025-C"],
        questions["2025-C"],
        baselines["2025-C"],
        outstanding,
    )

    required_fragments = [
        "## Outstanding 全局报告",
        "2505964",
        "Monte Carlo",
        "Advanced：",
        "Outstanding：复现 2505964",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in page]
    assert not missing, f"missing fragments: {missing}"
    assert "- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。" not in page


def test_problem_page_summarizes_outstanding_experiment_results() -> None:
    problems = {row["problem_id"]: row for row in read_csv("mcm/problem_index.csv")}
    questions = group_by_problem(read_csv("mcm/question_solution_index.csv"))
    baselines = group_baselines(read_csv("mcm/generic_baselines/generic_baseline_index.csv"))
    outstanding = {
        row["problem_id"]: row
        for row in read_csv("mcm/outstanding_solutions/outstanding_solution_index.csv")
    }

    page = build_problem_page(
        "mcm-track",
        problems["2025-C"],
        questions["2025-C"],
        baselines["2025-C"],
        outstanding["2025-C"],
    )

    required_fragments = [
        "2028 Top1 USA expected_total",
        "首枚奖牌国家期望",
        "2024 holdout accuracy",
        "Poisson USA Swimming beta",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in page]
    assert not missing, f"missing fragments: {missing}"


def test_planned_outstanding_rows_are_not_rendered_as_implemented() -> None:
    rows = [
        {
            "problem_id": "2025-A",
            "status": "planned",
            "paper_id": "2501909",
            "paper_title": "Stair Wear: Traces of History",
        },
        {
            "problem_id": "2025-C",
            "status": "implemented",
            "paper_id": "2505964",
            "paper_title": "2028 Olympic Medal Predictions Based on Random Forest Model",
        },
    ]

    grouped = group_outstanding(rows)

    assert "2025-A" not in grouped
    assert grouped["2025-C"]["paper_id"] == "2505964"


def test_outstanding_index_covers_2025_verifiable_problems() -> None:
    expected = {
        "mcm": {"2025-A", "2025-B", "2025-C", "2025-D", "2025-E", "2025-F"},
        "cumcm": {"2025-A", "2025-B", "2025-C", "2025-D", "2025-E"},
    }

    for track, problem_ids in expected.items():
        rows = {row["problem_id"]: row for row in read_csv(f"{track}/outstanding_solutions/outstanding_solution_index.csv")}
        missing = sorted(problem_ids - set(rows))
        assert not missing, f"{track} missing outstanding rows: {missing}"

        not_implemented = sorted(pid for pid in problem_ids if rows[pid].get("status") != "implemented")
        assert not not_implemented, f"{track} outstanding rows not implemented: {not_implemented}"

        for pid in sorted(problem_ids):
            row = rows[pid]
            for key in ("solution_path", "result_path", "report_path"):
                path = ROOT / row[key]
                assert path.exists(), f"{track} {pid} missing {key}: {row[key]}"


if __name__ == "__main__":
    test_problem_page_contains_global_reports()
    test_problem_page_renders_outstanding_report_when_available()
    test_problem_page_summarizes_outstanding_experiment_results()
    test_planned_outstanding_rows_are_not_rendered_as_implemented()
    test_outstanding_index_covers_2025_verifiable_problems()
    print("ok")
