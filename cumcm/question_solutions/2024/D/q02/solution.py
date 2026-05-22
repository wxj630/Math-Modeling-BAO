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
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "仍投射一枚深弹，潜艇中心位置各方向的定位均有误差。 请给出投弹命中概率 的表达式。 针对以下参数，设计定深引信引爆深度， 使得投弹命中概率最大： 潜艇中心位置的深度 定位值为 150 m，标准差 𝜎𝑧 = 40 m，潜艇中心位置实际深度的最小值为 120 m，其他参 数同问题 1。",
    "tasks": [
      "请给出投弹命中概率 的表达式",
      "针对以下参数，设计定深引信引爆深度， 使得投弹命中概率最大： 潜艇中心位置的深度 定位值为 150 m，标准差 𝜎𝑧 = 40 m，潜艇中心位置实际深度的最小值为 120 m，其他参 数同问题 1"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "定位"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
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
RESULT_PATH = ROOT / "question_results" / "2024" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "D" / "q02"


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
