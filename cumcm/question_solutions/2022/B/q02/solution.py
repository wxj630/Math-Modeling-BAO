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
  "problem_path": "cumcm/problems/2022/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "实际飞行中， 无人机集群也可以是其他编队队形，例如锥形编队队形（见图 3，直 线上相邻两架无人机的间距相等，如 50 m）。仍考虑纯方位无源定位的情形，设计无人机位置 调整方案。",
    "tasks": [
      "仍考虑纯方位无源定位的情形，设计无人机位置 调整方案"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "定位",
          "方位"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2022" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "B" / "q02"


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
