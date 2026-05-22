# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-A",
  "title": "2024年 CUMCM A题：板凳龙”  闹元宵",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/A.md",
  "question_index": 5,
  "question": {
    "label": "问题 5",
    "statement": "舞龙队沿问题 4 设定的路径行进，龙头行进速度保持不变， 请确定龙头的最大 行进速度，使得舞龙队各把手的速度均不超过 2 m/s。 调头空间",
    "tasks": [
      "舞龙队沿问题 4 设定的路径行进，龙头行进速度保持不变， 请确定龙头的最大 行进速度，使得舞龙队各把手的速度均不超过 2 m/s"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "空间"
        ]
      },
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "路径"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 758066,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 517064,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15292,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result4.xlsx",
      "name": "result4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 346204,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "A" / "q05" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "A" / "q05" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "A" / "q05"


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
