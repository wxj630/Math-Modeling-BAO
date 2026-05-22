# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2011-A",
  "title": "2011年 CUMCM A题：城市表层土壤重金属污染分析",
  "problem_path": "cumcm/problems/2011/A.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "给出8种主要重金属元素在该城区的空间分布，并分析该城区内不同区域重金属的污染程度。",
    "tasks": [
      "给出8种主要重金属元素在该城区的空间分布，并分析该城区内不同区域重金属的污染程度"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "空间"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/A/cumcm2011A.doc",
      "name": "cumcm2011A.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 33792,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/A/cumcm2011A附件_数据.xls",
      "name": "cumcm2011A附件_数据.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 76288,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2011" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2011" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2011" / "A" / "q01"


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
