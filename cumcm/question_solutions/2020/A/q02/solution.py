# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-A",
  "title": "2020年 CUMCM A题：炉温曲线",
  "problem_path": "cumcm/problems/2020/A.md",
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度。",
    "tasks": [
      "假设各温区温度的设定值分别为182ºC（小温区1~5）、203ºC（小温区6）、237ºC（小温区7）、254ºC（小温区8~9），请确定允许的最大传送带过炉速度"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "温度"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/2020A-炉温曲线.docx",
      "name": "2020A-炉温曲线.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 385398,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/result.csv",
      "name": "result.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 32,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/A/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 22940,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "A" / "q02"


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
