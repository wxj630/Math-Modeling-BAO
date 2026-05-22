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
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/C.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "参考问题1， 该企业应至少选择多少家供应商供应原材料才可能满足生产的需求？ 针对这些供应商，为该企业制定未来 24 周每周最经济的原材料订购方案，并据此制定 损耗最少的转运方案。试对订购方案和转运方案的实施效果进行分析。",
    "tasks": [
      "试对订购方案和转运方案的实施效果进行分析"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
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
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "未来"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/CUMCM2021-C.pdf",
      "name": "CUMCM2021-C.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 217723,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件1 近5年402家供应商的相关数据.xlsx",
      "name": "附件1 近5年402家供应商的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 673200,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件2 近5年8家转运商的相关数据.xlsx",
      "name": "附件2 近5年8家转运商的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 22122,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件A 订购方案数据结果.xlsx",
      "name": "附件A 订购方案数据结果.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 99251,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/C/附件B 转运方案数据结果.xlsx",
      "name": "附件B 转运方案数据结果.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 620902,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "C" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "C" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "C" / "q02"


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
