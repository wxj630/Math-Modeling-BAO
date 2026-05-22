# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-C",
  "title": "2021年 CUMCM C题：生产企业原材料的订购与运输",
  "problem_path": "cumcm/problems/2021/C.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "该企业为了压缩生产成本，现计划尽量多地采购 A 类和尽量少地采购 C 类原材 料，以减少转运及仓储的成本，同时希望转运商的转运损耗率尽量少。请制定新的订购 方案及转运方案，并分析方案的实施效果。",
    "tasks": [
      "请制定新的订购 方案及转运方案，并分析方案的实施效果"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "成本",
          "方案"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/CUMCM2021-C.pdf",
      "name": "CUMCM2021-C.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 217723,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx",
      "name": "附件1 近5年402家供应商的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 673200,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx",
      "name": "附件2 近5年8家转运商的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 22122,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx",
      "name": "附件A 订购方案数据结果.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 99251,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx",
      "name": "附件B 转运方案数据结果.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 620902,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "C" / "q03"


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
