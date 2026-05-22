# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-D",
  "title": "2024年 CUMCM D题：反潜航空深弹命中概率",
  "problem_path": "cumcm/problems/2024/D.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "由于单枚深弹命中率较低，为了增强杀伤效果，通常需要投掷多枚深弹。若一 架反潜飞机可携带 9 枚航空深弹， 所有深弹的定深引信引爆深度均相同， 投弹落点在平面上 呈阵列形状（见图 2） 。在问题2 的参数下，请设计投弹方案（包括定深引信引爆深度，以 及投弹落点之间的平面间隔） ，使得投弹命中（指至少一枚深弹命中潜艇）的概率最大。",
    "tasks": [
      "在问题2 的参数下，请设计投弹方案（包括定深引信引爆深度，以 及投弹落点之间的平面间隔） ，使得投弹命中（指至少一枚深弹命中潜艇）的概率最大"
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
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "形状"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/D题/D题.pdf",
      "name": "D题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 890096,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "D" / "q03"


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
