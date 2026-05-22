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
  "question_index": 6,
  "question": {
    "label": "问题 2",
    "statement": "供应商的供货量：第一列为供应商的名称； 第二列为供应商供应原材料的类别； 第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米） ； 数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货。 附件 2 的数据说明 第一列为转运商的名称； 第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率 供货量 ；数值“0”表示没有运送。",
    "tasks": [
      "供应商的供货量：第一列为供应商的名称",
      "第二列为供应商供应原材料的类别",
      "第三列及以后共240 列为各供应商每周的供货量 （单位： 立方米）",
      "数值 “0” 表示相应 的周（所在列）供应商（所在行）没有供货",
      "附件 2 的数据说明 第一列为转运商的名称",
      "第二列及以后共240 列为每周各转运商的运输损耗率 （%）， 即 100%−=供货量 接收量损耗率 供货量"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
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
RESULT_PATH = ROOT / "question_results" / "2021" / "C" / "q06" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "C" / "q06" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "C" / "q06"


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
