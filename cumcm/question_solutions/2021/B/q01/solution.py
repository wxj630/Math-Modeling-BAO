# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-B",
  "title": "2021年 CUMCM B题：乙醇偶合制备 C4 烯烃",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "对附件 1 中每种催化剂组合，分别研究乙醇转化率、C4 烯烃的选择性与温 度的关系， 并对附件 2 中 350 度时给定的催化剂组合在一次实验不同时间的测试结 果进行分析。",
    "tasks": [
      "对附件 1 中每种催化剂组合，分别研究乙醇转化率、C4 烯烃的选择性与温 度的关系， 并对附件 2 中 350 度时给定的催化剂组合在一次实验不同时间的测试结 果进行分析"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/CUMCM2021-B.pdf",
      "name": "CUMCM2021-B.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 170032,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20897,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11200,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "B" / "q01"


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
