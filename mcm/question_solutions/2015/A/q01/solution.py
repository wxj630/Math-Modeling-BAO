from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from generic_baseline import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2015-A",
  "year": "2015",
  "code": "A",
  "question": "q01",
  "question_title": "Ebola 传播、药物生产与配送优化模型",
  "statement": "Build a realistic, sensible, and useful model that considers Ebola spread, medicine demand, feasible delivery systems, delivery locations, manufacturing speed, and other critical factors to optimize eradication or containment.",
  "methods": "SEIR 传播动力学、药物库存方程、设施选址、配送路径优化、情景敏感性分析。",
  "source_type": "official_html_statement",
  "solution_path": "question_solutions/2015/A/q01/solution.py",
  "result_path": "question_results/2015/A/q01/result.json",
  "report_path": "question_reports/2015/A/q01/report.md",
  "artifact_path": "question_artifacts/2015/A/q01/experiment_table.csv"
}
RESULT_PATH = ROOT / "question_results" / '2015' / 'A' / 'q01' / "result.json"
REPORT_PATH = ROOT / "question_reports" / '2015' / 'A' / 'q01' / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / '2015' / 'A' / 'q01'


def write_report(result: dict) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {result['problem_id']} {result['question']}：{result['question_title']}",
        "",
        "## 题目原问",
        result.get("statement", ""),
        "",
        "## 适合模型",
        result.get("methods", ""),
        "",
        "## 数据与真实性",
        f"- 数据类型：{result['data_source']['type']}。",
        f"- 官方来源：{result['data_source'].get('source_url')}。",
        "- 本脚本只使用 COMAP 官方网页题面和显式建模假设，不使用随机占位观测。",
        "",
        "## 建模与求解报告",
        f"- 模型族：{result['selected_model']['name']}（{result['selected_model']['chapter']}）。",
        f"- baseline score：{result['experiment_result']['baseline_score']}。",
        f"- 命中关键词：{', '.join(result['selected_model'].get('matched_keywords', []))}。",
        "- 这个 advanced 占位层把 2015 官方 HTML 题面接入教程链路；后续可替换为更细的 SEIR/贝叶斯搜索专用实验。",
        "",
        "## 运行方式",
        f"`.venv/bin/python {Path(__file__).resolve().relative_to(REPO_ROOT)}`",
        "",
        "## 输出",
        f"- `{RESULT_PATH.relative_to(REPO_ROOT)}`",
        f"- `{REPORT_PATH.relative_to(REPO_ROOT)}`",
        f"- `{ARTIFACT_DIR.relative_to(REPO_ROOT)}`",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    result["data_source"] = {
        "type": PAYLOAD["source_type"],
        "root": "https://www.contest.comap.com/undergraduate/contests/mcm/contests/2015/problems/",
        "source_url": "https://www.contest.comap.com/undergraduate/contests/mcm/contests/2015/problems/",
        "note": "COMAP official 2015 MCM problem page provides A/B statements as HTML text rather than downloadable PDFs.",
    }
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
