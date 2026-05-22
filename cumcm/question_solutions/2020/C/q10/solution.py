# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-C",
  "title": "2020年 CUMCM C题：中小微企业的信贷决策",
  "problem_path": "cumcm/problems/2020/C.md",
  "question_index": 10,
  "question": {
    "label": "问题 7",
    "statement": "客户流失率：因为贷款利率等因素银行失去潜在客户的比率。",
    "tasks": [
      "客户流失率：因为贷款利率等因素银行失去潜在客户的比率"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "通用"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "通用"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/2020C-中小微企业的信贷决策.docx",
      "name": "2020C-中小微企业的信贷决策.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 23624,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx",
      "name": "附件1：123家有信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 21273447,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx",
      "name": "附件2：302家无信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 41682618,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "name": "附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13576,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "C" / "q10" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "C" / "q10" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "C" / "q10"


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
