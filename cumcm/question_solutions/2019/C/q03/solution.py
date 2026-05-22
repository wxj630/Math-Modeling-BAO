# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2019-C",
  "title": "2019年 CUMCM C题：赛题",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2019/C.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "在某些时候，经常会出现出租车排队载客和乘客排队乘车的情况。某机场“乘车区”现有两条并行车道，管理部门应如何设置“上车点”，并合理安排出租车和乘客，在保证车辆和乘客安全的条件下，使得总的乘车效率最高。",
    "tasks": [
      "在某些时候，经常会出现出租车排队载客和乘客排队乘车的情况",
      "某机场“乘车区”现有两条并行车道，管理部门应如何设置“上车点”，并合理安排出租车和乘客，在保证车辆和乘客安全的条件下，使得总的乘车效率最高"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/C-2019中文/CUMCM-2019-Problem-C-Chinese.doc",
      "name": "CUMCM-2019-Problem-C-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 32768,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/C-2019中文/CUMCM-2019-Problem-C-Chinese.pdf",
      "name": "CUMCM-2019-Problem-C-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 154538,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "C" / "q03"


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
