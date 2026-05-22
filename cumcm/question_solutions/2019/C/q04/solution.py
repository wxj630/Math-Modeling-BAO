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
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "机场的出租车载客收益与载客的行驶里程有关，乘客的目的地有远有近，出租车司机不能选择乘客和拒载，但允许出租车多次往返载客。管理部门拟对某些短途载客再次返回的出租车给予一定的“优先权”，使得这些出租车的收益尽量均衡，试给出一个可行的“优先”安排方案。",
    "tasks": [
      "管理部门拟对某些短途载客再次返回的出租车给予一定的“优先权”，使得这些出租车的收益尽量均衡，试给出一个可行的“优先”安排方案"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "收益",
          "方案"
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
RESULT_PATH = ROOT / "question_results" / "2019" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "C" / "q04"


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
