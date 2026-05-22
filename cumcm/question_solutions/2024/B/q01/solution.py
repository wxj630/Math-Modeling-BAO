# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-B",
  "title": "2024年 CUMCM B题：生产过程中的决策",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "供应商声称一批零配件（零配件 1 或零配件 2）的次品率不会超过某个标称值。 企业准备采用抽样检测方法决定是否接收从供应商购买的这批零配件， 检测费用由企业自行 承担。请为企业设计检测次数尽可能少的抽样检测方案。 如果标称值为 10%，根据你们的抽样检测方案， 针对以下两种情形， 分别给出具体结果： (1) 在 95%的信度下认定零配件次品率超过标称值，则拒收这批零配件； (2) 在 90%的信度下认定零配件次品率不超过标称值，则接收这批零配件。",
    "tasks": [
      "供应商声称一批零配件（零配件 1 或零配件 2）的次品率不会超过某个标称值。 企业准备采用抽样检测方法决定是否接收从供应商购买的这批零配件， 检测费用由企业自行 承担。请为企业设计检测次数尽可能少的抽样检测方案。 如果标称值为 10%，根据你们的抽样检测方案， 针对以下两种情形， 分别给出具体结果："
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "检测"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 636910,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "B" / "q01"


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
