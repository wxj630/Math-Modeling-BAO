# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2020-C",
  "question_index": 8,
  "title": "2020年 CUMCM C题：中小微企业的信贷决策",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/C.md",
  "question": {
    "label": "问题 5",
    "statement": "负数发票：在为交易活动开具发票后，企业已入账记税，之后购方因故发生退货并退款，此时，需开具的负数发票。",
    "tasks": [
      "负数发票：在为交易活动开具发票后，企业已入账记税，之后购方因故发生退货并退款，此时，需开具的负数发票"
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
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/2020C-中小微企业的信贷决策.docx",
      "name": "2020C-中小微企业的信贷决策.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 23624,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx",
      "name": "附件1：123家有信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 21273447,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx",
      "name": "附件2：302家无信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 41682618,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "name": "附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13576,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2020" / "C" / "q08" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2020" / "C" / "q08" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2020" / "C" / "q08"


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
