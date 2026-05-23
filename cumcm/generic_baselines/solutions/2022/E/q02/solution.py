# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2022-E",
  "question_index": 2,
  "title": "2022年 CUMCM E题：小批量物料的生产安排",
  "problem_path": "cumcm/problems/2022/E.md",
  "question": {
    "label": "问题2",
    "statement": "如果按照物料需求量的预测值来安排生产，可能会产生较大的库存，或者出现较 多的缺货，给企业带来经济和信誉方面的损失。企业希望从需求量的预测值、需求特征、库存 量和缺货量等方面综合考虑，以便更合理地安排生产。 请提供一种制定生产计划的方法，从第101 周（见附录(1)）开始，在每周初，制定本周的 物料生产计划（见附录(2)），安排生产，直至第177 周为止，使得平均服务水平不低于85%（见 附录(3)）。这里假设：本周计划生产的物料，只能在下周及以后使用。为便于统一计算结果， 进一步假设第100 周末的库存量和缺货量均为零，第100 周的生产计划数恰好等于第101 周的 实际需求数。 请在问题1 选定的6 种物料中选择一种物料，将其第 101 ∼110 周的生产计划数、实际 需求量、库存量、缺货量（见附录(4)）和服务水平按表1 的形式填写，放在正文中。",
    "tasks": [
      "如果按照物料需求量的预测值来安排生产，可能会产生较大的库存，或者出现较 多的缺货，给企业带来经济和信誉方面的损失。企业希望从需求量的预测值、需求特征、库存 量和缺货量等方面综合考虑，以便更合理地安排生产。 请提供一种制定生产计划的方法，从第101 周（见附录",
      "(3)）。这里假设：本周计划生产的物料，只能在下周及以后使用。为便于统一计算结果， 进一步假设第100 周末的库存量和缺货量均为零，第100 周的生产计划数恰好等于第101 周的 实际需求数。 请在问题1 选定的6 种物料中选择一种物料，将其第 101 ∼110 周的生产计划数、实际 需求量、库存量、缺货量（见附录"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "预测"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "综合"
        ]
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "预测"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/E题.pdf",
      "name": "E题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 640657,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 675320,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2022" / "E" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2022" / "E" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2022" / "E" / "q02"


def write_generic_report(result: dict, solution_path: Path) -> None:
    def repo_rel(path: Path | str) -> str:
        path = Path(path)
        try:
            return str(path.resolve().relative_to(ROOT.parent.resolve()))
        except ValueError:
            return str(path)

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
    lines.append(f"- 通用代码：{repo_rel(solution_path)}")
    lines.append(f"- 单问运行：`.venv/bin/python {repo_rel(solution_path)}`")
    lines.append(f"- 结果 JSON：{repo_rel(RESULT_PATH)}")
    lines.append(f"- 实验报告：{repo_rel(REPORT_PATH)}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{repo_rel(ROOT / artifact)}")
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
