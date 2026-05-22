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
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "按设计要求，定日镜场的额定年平均输出热功率（以下简称额定功率）为60 MW。 若所有定日镜尺寸及安装高度相同，请设计定日镜场的以下参数：吸收塔的位置坐标、定日镜 尺寸、安装高度、定日镜数目、定日镜位置，使得定日镜场在达到额定功率的条件下，单位镜 面面积年平均输出热功率尽量大。请将结果分别按表1、2、3 的格式填入表格，并将吸收塔 的位置坐标、定日镜尺寸、安装高度、位置坐标按模板规定的格式保存到result2.xlsx 文件中。",
    "tasks": [
      "按设计要求，定日镜场的额定年平均输出热功率（以下简称额定功率）为60 MW",
      "若所有定日镜尺寸及安装高度相同，请设计定日镜场的以下参数：吸收塔的位置坐标、定日镜 尺寸、安装高度、定日镜数目、定日镜位置，使得定日镜场在达到额定功率的条件下，单位镜 面面积年平均输出热功率尽量大",
      "请将结果分别按表1、2、3 的格式填入表格，并将吸收塔 的位置坐标、定日镜尺寸、安装高度、位置坐标按模板规定的格式保存到result2.xlsx 文件中"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "坐标"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
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
RESULT_PATH = ROOT / "question_results" / "2023" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "A" / "q02"


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
