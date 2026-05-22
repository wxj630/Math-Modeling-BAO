# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2015-A",
  "title": "2015年 CUMCM A题：太阳影子定位",
  "problem_path": "cumcm/problems/2015/A.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "附件4为一根直杆在太阳下的影子变化的视频，并且已通过某种方式估计出直杆的高度为2米。请建立确定视频拍摄地点的数学模型，并应用你们的模型给出若干个可能的拍摄地点。 如果拍摄日期未知，你能否根据视频确定出拍摄地点与日期？",
    "tasks": [
      "请建立确定视频拍摄地点的数学模型，并应用你们的模型给出若干个可能的拍摄地点",
      "如果拍摄日期未知，你能否根据视频确定出拍摄地点与日期？"
    ],
    "models": [
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "日期"
        ]
      },
      {
        "key": "signal_text",
        "name": "图像文本与信号",
        "chapter": "CH10",
        "keywords": [
          "视频"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/CUMCM-2015-problem A-Chinese.doc",
      "name": "CUMCM-2015-problem A-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 23040,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls",
      "name": "附件1-3.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 29184,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件4下载说明.doc",
      "name": "附件4下载说明.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 22528,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/CUMCM-2015-problem A-Chinese.doc",
      "name": "CUMCM-2015-problem A-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 23040,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件1-3.xls",
      "name": "附件1-3.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 29184,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/A/附件4下载说明.doc",
      "name": "附件4下载说明.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 22528,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2015" / "A" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2015" / "A" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2015" / "A" / "q04"


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
