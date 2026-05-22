# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2011-D",
  "title": "2011年 CUMCM D题：天然肠衣搭配",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2011/D.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "某种规格对应原料如果出现剩余，可以降级使用。如长度为14米的原料可以和长度介于7-13.5米的进行捆扎，成品属于7-13.5米的规格；",
    "tasks": [
      "某种规格对应原料如果出现剩余，可以降级使用",
      "如长度为14米的原料可以和长度介于7-13.5米的进行捆扎，成品属于7-13.5米的规格"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/D/cumcm2011D.doc",
      "name": "cumcm2011D.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 54784,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2011" / "D" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2011" / "D" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2011" / "D" / "q04"


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
