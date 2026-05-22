# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-B",
  "title": "2021年 CUMCM B题：乙醇偶合制备 C4 烯烃",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "探讨不同催化剂组合及温度对乙醇转化率以及 C4 烯烃选择性大小的影响。",
    "tasks": [
      "探讨不同催化剂组合及温度对乙醇转化率以及 C4 烯烃选择性大小的影响"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/CUMCM2021-B.pdf",
      "name": "CUMCM2021-B.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 170032,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20897,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11200,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "B" / "q02"


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
