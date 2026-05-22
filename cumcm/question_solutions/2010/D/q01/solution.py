# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-D",
  "title": "2010年 CUMCM D题：对学生宿舍设计方案的评价",
  "problem_path": "cumcm/problems/2010/D.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "附件是四种比较典型的学生宿舍的设计方案。请你们用数学建模的方法就它们的经济性、舒适性和安全性作出综合量化评价和比较",
    "tasks": [
      "附件是四种比较典型的学生宿舍的设计方案",
      "请你们用数学建模的方法就它们的经济性、舒适性和安全性作出综合量化评价和比较"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "评价",
          "综合",
          "比较"
        ]
      },
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
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design1.tif",
      "name": "Design1.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design2.tif",
      "name": "Design2.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design3.tif",
      "name": "Design3.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design4.tif",
      "name": "Design4.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8200476,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/cumcm2010D.doc",
      "name": "cumcm2010D.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 28160,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design1.tif",
      "name": "Design1.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design2.tif",
      "name": "Design2.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design3.tif",
      "name": "Design3.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8187386,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/Design4.tif",
      "name": "Design4.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 8200476,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010D/cumcm2010D.doc",
      "name": "cumcm2010D.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 28160,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "D" / "q01"


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
