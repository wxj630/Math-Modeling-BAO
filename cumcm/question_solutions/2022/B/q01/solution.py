# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-B",
  "title": "2022年 CUMCM B题：无人机遂行编队飞行中的纯方位无源定位",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）。无人机基于自身感知 的高度信息，均保持在同一个高度上飞行。",
    "tasks": [
      "编队由 10 架无人机组成，形成圆形编队，其中 9 架无人机（编号 FY01~FY09）均 匀分布在某一圆周上，另 1 架无人机（编号 FY00）位于圆心（见图 2）",
      "无人机基于自身感知 的高度信息，均保持在同一个高度上飞行"
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
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2022" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "B" / "q01"


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
