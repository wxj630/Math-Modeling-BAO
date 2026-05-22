# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2024-A",
  "question_index": 1,
  "title": "2024年 CUMCM A题：板凳龙”  闹元宵",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/A.md",
  "question": {
    "label": "问题 1",
    "statement": "舞龙队沿螺距为 55 cm 的等距螺线顺时针盘入，各把手中心均位于螺线上。龙 头前把手的行进速度始终保持 1 m/s。初始时，龙头位于螺线第 16 圈 A 点处（见图 4）。请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）。 同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）。 27.5 cm 第 2 个孔，孔径 5.5 cm 27.5 cm 第 1 个孔，孔径 5.5 cm 30 cm 27.5 cm 27.5 cm 30 cm 220 cm 第 2 个孔， 孔径 5.5 cm 第 1 个孔， 孔径 5.5 cm 27.5 cm 27.5 cm 前一节龙身后部 后一节龙身前部 前把手 341 cm 2",
    "tasks": [
      "请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）",
      "同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 758066,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 517064,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15292,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result4.xlsx",
      "name": "result4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 346204,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2024" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2024" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2024" / "A" / "q01"


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
