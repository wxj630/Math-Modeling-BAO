from __future__ import annotations

from build_problem_pages import build_problem_page, group_baselines, group_by_problem, read_csv


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


if __name__ == "__main__":
    test_problem_page_contains_global_reports()
    print("ok")
