# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2017-D",
  "title": "2017年 CUMCM D题：巡检线路的排班",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2017/D.md",
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "如果巡检人员每巡检2小时左右需要休息一次，休息时间大约是5到10分钟，在中午12时和下午6时左右需要进餐一次，每次进餐时间为30分钟，仍采用每天三班倒，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表。",
    "tasks": [
      "如果巡检人员每巡检2小时左右需要休息一次，休息时间大约是5到10分钟，在中午12时和下午6时左右需要进餐一次，每次进餐时间为30分钟，仍采用每天三班倒，每班需要多少人，巡检线路如何安排，并给出巡检人员的巡检线路和巡检的时间表"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/D/CUMCM-2017-appendix-D.xlsx",
      "name": "CUMCM-2017-appendix-D.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 141022,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/D/CUMCM-2017-problem-D.docx",
      "name": "CUMCM-2017-problem-D.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 19636,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2017" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2017" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2017" / "D" / "q02"


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
