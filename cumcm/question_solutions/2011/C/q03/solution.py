# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2011-C",
  "title": "2011年 CUMCM C题：企业退休职工养老金制度的改革",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2011/C.md",
  "question_index": 3,
  "question": {
    "label": "问题三",
    "statement": "假设该企业某职工自 2000年起从30岁开始缴养老保险，一直缴费到退休（55岁，60岁，65岁），并从退休后一直领取养老金，至75岁死亡。计算养老保险基金的缺口情况，并计算该职工领取养老金到多少岁时，其缴存的养老保险基金与其领取的养老金之间达到收支平衡。",
    "tasks": [
      "计算养老保险基金的缺口情况，并计算该职工领取养老金到多少岁时，其缴存的养老保险基金与其领取的养老金之间达到收支平衡"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C.doc",
      "name": "cumcm2011C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 34816,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件1_山东省职工平均工资.xls",
      "name": "cumcm2011C附件1_山东省职工平均工资.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 16384,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件2_某企业分年龄职工数量及薪酬分布表.xls",
      "name": "cumcm2011C附件2_某企业分年龄职工数量及薪酬分布表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 16384,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/C/cumcm2011C附件3_养老金的计算办法.doc",
      "name": "cumcm2011C附件3_养老金的计算办法.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 62464,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2011" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2011" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2011" / "C" / "q03"


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
