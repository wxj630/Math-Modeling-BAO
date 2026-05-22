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
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2017/A.md",
  "question_index": 5,
  "question": {
    "label": "问题 1",
    "statement": "-(4)中的所有数值结果均保留4位小数。同时提供(2)和(3)重建得到的介质吸收率的数据文件（大小为256×256，格式同附件1，文件名分别为problem2.xls和problem3.xls）",
    "tasks": [
      "-",
      "(4)中的所有数值结果均保留4位小数。同时提供",
      "(2)和",
      "(3)重建得到的介质吸收率的数据文件（大小为256×256，格式同附件1，文件名分别为problem2.xls和problem3.xls）"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/A题附件.xls",
      "name": "A题附件.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 4231680,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/A/CUMCM-2017-problem-A.docx",
      "name": "CUMCM-2017-problem-A.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 106223,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2017" / "A" / "q05" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2017" / "A" / "q05" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2017" / "A" / "q05"


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
