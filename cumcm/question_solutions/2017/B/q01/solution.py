# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2017-B",
  "title": "2017年 CUMCM B题：拍照赚钱”的任务定价",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2017/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "附件二是会员信息数据，包含了会员的位置、信誉值、参考其信誉给出的任务开始预订时间和预订限额，原则上会员信誉越高，越优先开始挑选任务，其配额也就越大（任务分配时实际上是根据预订限额所占比例进行配发）",
    "tasks": [
      "附件二是会员信息数据，包含了会员的位置、信誉值、参考其信誉给出的任务开始预订时间和预订限额，原则上会员信誉越高，越优先开始挑选任务，其配额也就越大（任务分配时实际上是根据预订限额所占比例进行配发）"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "分配"
        ]
      },
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/CUMCM-2017-problem-B.docx",
      "name": "CUMCM-2017-problem-B.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 19133,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件一：已结束项目任务数据.xls",
      "name": "附件一：已结束项目任务数据.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 105472,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件三：新项目任务数据.xls",
      "name": "附件三：新项目任务数据.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 186880,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2017_IqAO5Qqi8f23d8738a07a0604b8629ce9bb061ad/CUMCM2017Problems/B/附件二：会员信息数据.xlsx",
      "name": "附件二：会员信息数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 102334,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2017" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2017" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2017" / "B" / "q01"


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
