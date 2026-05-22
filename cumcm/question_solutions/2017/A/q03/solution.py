# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2017-A",
  "title": "2017年 CUMCM A题：CT系统参数标定及成像",
  "problem_path": "cumcm/problems/2017/A.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "附件5是利用上述CT系统得到的另一个未知介质的接收信息。利用(1)中得到的标定参数，给出该未知介质的相关信息。另外，请具体给出图3所给的10个位置处的吸收率。",
    "tasks": [
      "(1)中得到的标定参数，给出该未知介质的相关信息。另外，请具体给出图3所给的10个位置处的吸收率"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "系统"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/A题附件.xls",
      "name": "A题附件.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 4231680,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/CUMCM-2017-problem-A.docx",
      "name": "CUMCM-2017-problem-A.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 106223,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2017" / "A" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2017" / "A" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2017" / "A" / "q03"


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
