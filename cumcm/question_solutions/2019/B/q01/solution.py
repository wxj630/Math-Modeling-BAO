# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2019-B",
  "title": "2019年 CUMCM B题：同心协力”策略研究",
  "problem_path": "cumcm/problems/2019/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "在理想状态下，每个人都可以精确控制用力方向、时机和力度，试讨论 这种情形下团队的最佳协作策略，并给出该策略下的颠球高度。",
    "tasks": [
      "在理想状态下，每个人都可以精确控制用力方向、时机和力度，试讨论 这种情形下团队的最佳协作策略，并给出该策略下的颠球高度"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.docx",
      "name": "CUMCM-1019-Problem-B-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 60187,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.pdf",
      "name": "CUMCM-1019-Problem-B-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 390962,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "B" / "q01"


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
