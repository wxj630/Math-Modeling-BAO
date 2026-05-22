# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2016-B",
  "title": "2016年 CUMCM B题：小区开放对道路通行的影响",
  "problem_path": "cumcm/problems/2016/B.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "小区开放产生的效果，可能会与小区结构及周边道路结构、车流量有关。请选取或构建不同类型的小区，应用你们建立的模型，定量比较各类型小区开放前后对道路通行的影响。",
    "tasks": [
      "请选取或构建不同类型的小区，应用你们建立的模型，定量比较各类型小区开放前后对道路通行的影响"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "比较",
          "效果"
        ]
      },
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "流量"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2016" / "B" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2016" / "B" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2016" / "B" / "q03"


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
