# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-E",
  "title": "2021年 CUMCM E题：中药材的鉴别",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/E.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "根据附件 1 中几种药材的中红外光谱数据，研究不同种类药材的特 征和差异性，并鉴别药材的种类。",
    "tasks": [
      "根据附件 1 中几种药材的中红外光谱数据，研究不同种类药材的特 征和差异性，并鉴别药材的种类"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "鉴别"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/CUMCM2021-E.pdf",
      "name": "CUMCM2021-E.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 607884,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9195442,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15610996,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13464909,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/E/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13314618,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "E" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "E" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "E" / "q01"


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
