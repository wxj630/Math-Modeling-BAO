# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2016-A",
  "question_index": 2,
  "title": "2016年 CUMCM A题：系泊系统的设计",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2016/A.md",
  "question": {
    "label": "问题2",
    "statement": "在问题1的假设下，计算海面风速为36m/s时钢桶和各节钢管的倾斜角度、锚链形状和浮标的游动区域。请调节重物球的质量，使得钢桶的倾斜角度不超过5度，锚链在锚点与海床的夹角不超过16度。",
    "tasks": [
      "在问题1的假设下，计算海面风速为36m/s时钢桶和各节钢管的倾斜角度、锚链形状和浮标的游动区域"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度",
          "形状"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2016" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2016" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2016" / "A" / "q02"


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
