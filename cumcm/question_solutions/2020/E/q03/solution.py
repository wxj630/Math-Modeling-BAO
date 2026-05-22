# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-E",
  "title": "2020年 CUMCM E题：校园供水系统智能管理",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/E.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "管网维修需要一定的人工费和材料费，但同时可以降低管网漏损程度。请根据以上结果和你了解的水价及维修成本确定管网漏损的最优维修决策方案",
    "tasks": [
      "请根据以上结果和你了解的水价及维修成本确定管网漏损的最优维修决策方案"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "成本",
          "决策",
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/2020E-校园供水系统智能管理.docx",
      "name": "2020E-校园供水系统智能管理.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 21902,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_一季度.xlsx",
      "name": "附件_一季度.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 23157112,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_三季度.xlsx",
      "name": "附件_三季度.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 25667855,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_二季度.xlsx",
      "name": "附件_二季度.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 25030494,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_四季度.xlsx",
      "name": "附件_四季度.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 25483604,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/E/附件_水表层级.xlsx",
      "name": "附件_水表层级.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13802,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "E" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "E" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "E" / "q03"


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
