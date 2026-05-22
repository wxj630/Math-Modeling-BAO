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
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2019/B.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "当鼓面发生倾斜时， 球跳动方向不再竖直， 于是需要队员调整拉绳策略。 假设人数为 10，绳长为 2m，球的反弹高度为 60cm，相对于竖直方向产生 1 度 的倾斜角度，且倾斜方向在水平面的投影指向某两位队员之间， 与这两位队员的 夹角之比为 1:2。为了将球调整为竖直状态弹跳，请给出在可精确控制条件下所 有队员的发力时机及力度，并分析在现实情形中这种调整策略的实施效果。",
    "tasks": [
      "为了将球调整为竖直状态弹跳，请给出在可精确控制条件下所 有队员的发力时机及力度，并分析在现实情形中这种调整策略的实施效果"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "效果"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.docx",
      "name": "CUMCM-1019-Problem-B-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 60187,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.pdf",
      "name": "CUMCM-1019-Problem-B-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 390962,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "B" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "B" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "B" / "q04"


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
