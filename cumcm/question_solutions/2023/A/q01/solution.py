# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-A",
  "title": "2023年 CUMCM A题：定日镜场的优化设计",
  "problem_path": "cumcm/problems/2023/A.md",
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "若将吸收塔建于该圆形定日镜场中心，定日镜尺寸均为 6 m×6 m，安装高度均为 4 m，且给定所有定日镜中心的位置（以下简称为定日镜位置，相关数据见附件），请计算该定 日镜场的年平均光学效率、年平均输出热功率，以及单位镜面面积年平均输出热功率（光学效 率及输出热功率的定义见附录）。请将结果分别按表1 和表2 的格式填入表格。",
    "tasks": [
      "若将吸收塔建于该圆形定日镜场中心，定日镜尺寸均为 6 m×6 m，安装高度均为 4 m，且给定所有定日镜中心的位置（以下简称为定日镜位置，相关数据见附件），请计算该定 日镜场的年平均光学效率、年平均输出热功率，以及单位镜面面积年平均输出热功率（光学效 率及输出热功率的定义见附录）"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 882999,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9113,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/result3.xlsx",
      "name": "result3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9113,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 41752,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2023" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "A" / "q01"


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
