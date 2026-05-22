# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2019-D",
  "title": "2019年 CUMCM D题：空气质量数据的校准",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2019/D.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "对自建点数据与国控点数据进行探索性数据分析。",
    "tasks": [
      "对自建点数据与国控点数据进行探索性数据分析"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/CUMCM-2019-Problem-D-Chinese.docx",
      "name": "CUMCM-2019-Problem-D-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 397135,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/CUMCM-2019-Problem-D-Chinese.pdf",
      "name": "CUMCM-2019-Problem-D-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 327274,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件1.csv",
      "name": "附件1.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 154092,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件2.csv",
      "name": "附件2.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 13524487,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/D-2019中文/附件3.docx",
      "name": "附件3.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 17970,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "D" / "q01"


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
