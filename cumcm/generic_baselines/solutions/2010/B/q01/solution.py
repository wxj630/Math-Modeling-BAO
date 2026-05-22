# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2010-B",
  "question_index": 1,
  "title": "2010年 CUMCM B题：2010年上海世博会影响力的定量评估",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/B.md",
  "question": {
    "label": "问题 1",
    "statement": "2010年上海世博会是首次在中国举办的世界博览会。从1851年伦敦的“万国工业博览会”开始，世博会正日益成为各国人民交流历史文化、展示科技成果、体现合作精神、展望未来发展等的重要舞台。请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力",
    "tasks": [
      "请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力"
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
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "评估"
        ]
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "未来"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010B/cumcm2010B.doc",
      "name": "cumcm2010B.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 27136,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010B/cumcm2010B.doc",
      "name": "cumcm2010B.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 27136,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2010" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2010" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2010" / "B" / "q01"


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
