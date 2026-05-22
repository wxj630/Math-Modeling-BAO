# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2023-D",
  "question_index": 1,
  "title": "2023年 CUMCM D题：圈养湖羊的空间利用率",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2023/D.md",
  "question": {
    "label": "问题 1",
    "statement": "不考虑不确定因素和种羊的淘汰更新，假定自然交配期 20 天，母羊都能受孕，孕 期 149 天，每胎产羔 2 只，哺乳期 40 天，羔羊育肥期 210 天，母羊空怀休整期 20 天。该湖羊 养殖场现有 112 个标准羊栏，在实现连续生产的条件下，试确定养殖场种公羊与基础母羊的合 理数量， 并估算年化出栏羊只数量的范围。 若该养殖场希望每年出栏不少于 1500 只羊，试估算 现有标准羊栏数量的缺口。",
    "tasks": [
      "不考虑不确定因素和种羊的淘汰更新，假定自然交配期 20 天，母羊都能受孕，孕 期 149 天，每胎产羔 2 只，哺乳期 40 天，羔羊育肥期 210 天，母羊空怀休整期 20 天",
      "该湖羊 养殖场现有 112 个标准羊栏，在实现连续生产的条件下，试确定养殖场种公羊与基础母羊的合 理数量， 并估算年化出栏羊只数量的范围"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "通用"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "通用"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2023" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2023" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2023" / "D" / "q01"


def write_generic_report(result: dict, solution_path: Path) -> None:
    f = result["formulation"]
    lines = [
        f"# {result['problem_id']} {result['question_label']} 通用基线报告",
        "",
        "> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。",
        "",
        "## 题目与任务",
        "",
        f"- 题目：{result['title']}",
        f"- 问题：{result['question_label']}",
        f"- 原问：{result['statement']}",
        "",
        "## 通用模型选择",
        "",
        f"- 模型：{result['selected_model']['name']}（{result['selected_model']['chapter']}：{result['selected_model']['chapter_title']}）",
        f"- 教程参考：{result['selected_model']['doc']}",
        f"- 通用方法：`{result['experiment_result'].get('method', 'generic_model')}`",
        "",
        "## 变量、约束与公式",
        "",
        "### 变量定义",
    ]
    lines.extend(f"- {item}" for item in f.get("decision_variables", []))
    lines += ["", "### 约束条件"]
    lines.extend(f"- {item}" for item in f.get("constraints", []))
    lines += ["", "### 模型公式 / 目标函数"]
    lines.extend(f"- `{item}`" for item in f.get("objective_or_equations", []))
    lines += ["", "## 运行与产物", ""]
    lines.append(f"- 通用代码：{solution_path}")
    lines.append(f"- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python {solution_path}`")
    lines.append(f"- 结果 JSON：{RESULT_PATH}")
    lines.append(f"- 实验报告：{REPORT_PATH}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{ROOT / artifact}")
    lines += ["", "## 数据来源", ""]
    ds = result.get("data_source", {})
    lines.append(f"- 类型：{ds.get('source_type', 'unknown')}")
    if ds.get("path"):
        lines.append(f"- 路径：{ds['path']}")
    lines.append(f"- 说明：{ds.get('note', '')}")
    lines += ["", "## 核心结果", "", "```json", json.dumps(result["experiment_result"], ensure_ascii=False, indent=2), "```", ""]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, Path(__file__).resolve())
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
