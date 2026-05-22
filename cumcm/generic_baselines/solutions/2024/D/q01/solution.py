# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2024-D",
  "question_index": 1,
  "title": "2024年 CUMCM D题：反潜航空深弹命中概率",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/D.md",
  "question": {
    "label": "问题 1",
    "statement": "投射一枚深弹，潜艇中心位置的深度定位没有误差， 两个水平坐标定位均服从 正态分布。分析投弹最大命中概率与投弹落点平面坐标及定深引信引爆深度之间的关系， 并 给出使得投弹命中概率最大的投弹方案，及相应的最大命中概率表达式。 针对以下参数值给出最大命中概率：潜艇长 100 m，宽 20 m，高 25 m，潜艇航向方位 角为 90∘，深弹杀伤半径为 20 m，潜艇中心位置的水平定位标准差 𝜎 = 120 m，潜艇中心 位置的深度定位值为 150 m.",
    "tasks": [
      "分析投弹最大命中概率与投弹落点平面坐标及定深引信引爆深度之间的关系， 并 给出使得投弹命中概率最大的投弹方案，及相应的最大命中概率表达式",
      "针对以下参数值给出最大命中概率：潜艇长 100 m，宽 20 m，高 25 m，潜艇航向方位 角为 90∘，深弹杀伤半径为 20 m，潜艇中心位置的水平定位标准差 𝜎 = 120 m，潜艇中心 位置的深度定位值为 150 m."
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "定位",
          "坐标",
          "方位"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/D题/D题.pdf",
      "name": "D题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 890096,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2024" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2024" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2024" / "D" / "q01"


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
