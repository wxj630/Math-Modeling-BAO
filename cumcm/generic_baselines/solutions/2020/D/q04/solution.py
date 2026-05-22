# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2020-D",
  "question_index": 4,
  "title": "2020年 CUMCM D题：接触式轮廓仪的自动标注",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/D.md",
  "question": {
    "label": "问题4",
    "statement": "为了更准确地标注出工件2的各项参数值，附件3和附件4分别提供了工件2关于圆和角的9次局部测量数据，请利用这些数据修正问题3的结论，并对该工件的完整轮廓线作进一步修正。",
    "tasks": [
      "为了更准确地标注出工件2的各项参数值，附件3和附件4分别提供了工件2关于圆和角的9次局部测量数据，请利用这些数据修正问题3的结论，并对该工件的完整轮廓线作进一步修正"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "标注"
        ]
      },
      {
        "key": "signal_text",
        "name": "图像文本与信号",
        "chapter": "CH10",
        "keywords": [
          "轮廓"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/2020D-接触式轮廓仪的自动标注.docx",
      "name": "2020D-接触式轮廓仪的自动标注.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 338796,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件1_工件1的测量数据.xlsx",
      "name": "附件1_工件1的测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 7407027,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件2_工件2的整体测量数据.xlsx",
      "name": "附件2_工件2的整体测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20515708,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件3_工件2的局部测量数据（圆）.xlsx",
      "name": "附件3_工件2的局部测量数据（圆）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15871647,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件4_工件2的局部测量数据（角）.xlsx",
      "name": "附件4_工件2的局部测量数据（角）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 5941285,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2020" / "D" / "q04" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2020" / "D" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2020" / "D" / "q04"


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
