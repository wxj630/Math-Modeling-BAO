# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-C",
  "title": "2010年 CUMCM C题：输油管的布置",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/C.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "针对两炼油厂到铁路线距离和两炼油厂间距离的各种不同情形，提出你的设计方案。在方案设计时，若有共用管线，应考虑共用管线费用与非共用管线费用相同或不同的情形。",
    "tasks": [
      "针对两炼油厂到铁路线距离和两炼油厂间距离的各种不同情形，提出你的设计方案",
      "在方案设计时，若有共用管线，应考虑共用管线费用与非共用管线费用相同或不同的情形"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "C" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "C" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "C" / "q01"


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
