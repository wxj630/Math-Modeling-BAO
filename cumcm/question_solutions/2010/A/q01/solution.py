# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-A",
  "title": "2010年 CUMCM A题：储油罐的变位识别与罐容表标定",
  "problem_path": "cumcm/problems/2010/A.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "为了掌握罐体变位后对罐容表的影响，利用如图4的小椭圆型储油罐（两端平头的椭圆柱体），分别对罐体无变位和倾斜角为α=4.10的纵向变位两种情况做了实验，实验数据如附件1所示。请建立数学模型研究罐体变位后对罐容表的影响，并给出罐体变位后油位高度间隔为1cm的罐容表标定值。",
    "tasks": [
      "请建立数学模型研究罐体变位后对罐容表的影响，并给出罐体变位后油位高度间隔为1cm的罐容表标定值"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc",
      "name": "cumcm2010A.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 96768,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls",
      "name": "问题A附件1：实验采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 59392,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls",
      "name": "问题A附件2：实际采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 83456,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc",
      "name": "cumcm2010A.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 96768,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls",
      "name": "问题A附件1：实验采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 59392,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls",
      "name": "问题A附件2：实际采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 83456,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "A" / "q01"


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
