# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2015-C",
  "title": "2015年 CUMCM C题：月上柳梢头",
  "problem_path": "cumcm/problems/2015/C.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "根据所建立的模型，分析2016年北京地区“月上柳梢头，人约黄昏后”发生的日期与时间。根据模型判断2016年在哈尔滨、上海、广州、昆明、成都、乌鲁木齐是否能发生这一情景？如果能，请给出相应的日期与时间；如果不能，请给出原因",
    "tasks": [
      "根据所建立的模型，分析2016年北京地区“月上柳梢头，人约黄昏后”发生的日期与时间",
      "根据模型判断2016年在哈尔滨、上海、广州、昆明、成都、乌鲁木齐是否能发生这一情景？",
      "如果能，请给出相应的日期与时间",
      "如果不能，请给出原因"
    ],
    "models": [
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "日期"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/C/CUMCM-2015-problem C-Chinese.docx",
      "name": "CUMCM-2015-problem C-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 15072,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/C/CUMCM-2015-problem C-Chinese.docx",
      "name": "CUMCM-2015-problem C-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 15072,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2015" / "C" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2015" / "C" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2015" / "C" / "q01"


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
