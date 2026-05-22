# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-C",
  "title": "2023年 CUMCM C题：蔬菜类商品的自动定价与补货决策",
  "problem_path": "cumcm/problems/2023/C.md",
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "因蔬菜类商品的销售空间有限，商超希望进一步制定单品的补货计划，要求可 售单品总数控制在27-33 个，且各单品订购量满足最小陈列量2.5 千克的要求。根据2023 年6 月24-30 日的可售品种，给出7 月1 日的单品补货量和定价策略，在尽量满足市场对各 品类蔬菜商品需求的前提下，使得商超收益最大。",
    "tasks": [
      "根据2023 年6 月24-30 日的可售品种，给出7 月1 日的单品补货量和定价策略，在尽量满足市场对各 品类蔬菜商品需求的前提下，使得商超收益最大"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "空间"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "收益"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 361842,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 17803,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 39150980,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 1150765,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 18678,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2023" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "C" / "q03"


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
