# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-A",
  "title": "2024年 CUMCM A题：板凳龙”  闹元宵",
  "problem_path": "cumcm/problems/2024/A.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "舞龙队沿问题 1 设定的螺线盘入， 请确定舞龙队盘入的终止时刻， 使得板凳之 间不发生碰撞（即舞龙队不能再继续盘入的时间），并给出此时舞龙队的位置和速度，将结 果存放到文件 result2.xlsx 中（模板文件见附件）。同时在论文中给出此时龙头前把手、龙头 后面第 1、51、101、151、201 条龙身前把手和龙尾后把手的位置和速度。",
    "tasks": [
      "舞龙队沿问题 1 设定的螺线盘入， 请确定舞龙队盘入的终止时刻， 使得板凳之 间不发生碰撞（即舞龙队不能再继续盘入的时间），并给出此时舞龙队的位置和速度，将结 果存放到文件 result2.xlsx 中（模板文件见附件）",
      "同时在论文中给出此时龙头前把手、龙头 后面第 1、51、101、151、201 条龙身前把手和龙尾后把手的位置和速度"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 758066,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 517064,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15292,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result4.xlsx",
      "name": "result4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 346204,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "A" / "q02"


def main() -> None:
    result = solve_question(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_question_report(result, REPORT_PATH)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
