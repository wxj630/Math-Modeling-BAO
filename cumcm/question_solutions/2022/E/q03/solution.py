# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-E",
  "title": "2022年 CUMCM E题：小批量物料的生产安排",
  "problem_path": "cumcm/problems/2022/E.md",
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "考虑到物料的价格，物料的库存需要占用资金。为了在库存量与服务水平之间达 到某种平衡，如何调整现有的周生产计划，并说明理由。请根据新的周生产计划，对问题1 选 定的6 种物料重新计算，并将全部计算结果以表1 的形式填写在Excel 表中，通过支撑材料提 交，将综合结果按表2 的形式填写，放在正文中。对问题2 选择的1 种物料，将其第 101 ∼110 周的生产计划数、实际需求量、库存量、缺货量和服务水平按表1 的形式填写，放在正文中。",
    "tasks": [
      "请根据新的周生产计划，对问题1 选 定的6 种物料重新计算，并将全部计算结果以表1 的形式填写在Excel 表中，通过支撑材料提 交，将综合结果按表2 的形式填写，放在正文中"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "综合"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/E题.pdf",
      "name": "E题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 640657,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 675320,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2022" / "E" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "E" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "E" / "q03"


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
