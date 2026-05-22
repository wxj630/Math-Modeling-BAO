# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2019-E",
  "title": "2019年 CUMCM E题：薄利多销”分析",
  "problem_path": "cumcm/problems/2019/E.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "分析打折力度与商品销售额以及利润率的关系",
    "tasks": [
      "分析打折力度与商品销售额以及利润率的关系"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "利润"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/CUMCM-2019-Problem-E-Chinese.docx",
      "name": "CUMCM-2019-Problem-E-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 21724,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/CUMCM-2019-Problem-E-Chinese.pdf",
      "name": "CUMCM-2019-Problem-E-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 215893,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件1.csv",
      "name": "附件1.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 54635677,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件2.csv",
      "name": "附件2.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 61806709,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件3.csv",
      "name": "附件3.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 2166871,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件4.csv",
      "name": "附件4.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 589429,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件5.xlsx",
      "name": "附件5.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 14738,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "E" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "E" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "E" / "q03"


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
