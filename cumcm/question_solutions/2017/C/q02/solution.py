# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2017-C",
  "title": "2017年 CUMCM C题：颜色与物质浓度辨识",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2017/C.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "对附件Data2.xls中的数据，建立颜色读数和物质浓度的数学模型，并给出模型的误差分析",
    "tasks": [
      "对附件Data2.xls中的数据，建立颜色读数和物质浓度的数学模型，并给出模型的误差分析"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/CUMCM-2017-problem-C.docx",
      "name": "CUMCM-2017-problem-C.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 17043,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data1.xls",
      "name": "Data1.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 146944,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/Data2.xls",
      "name": "Data2.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 13824,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/C/readme.txt",
      "name": "readme.txt",
      "suffix": ".txt",
      "kind": "media_or_archive",
      "size_bytes": 389,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2017" / "C" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2017" / "C" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2017" / "C" / "q02"


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
