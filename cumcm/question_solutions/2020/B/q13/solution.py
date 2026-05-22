# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-B",
  "title": "2020年 CUMCM B题：穿越沙漠",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/B.md",
  "question_index": 13,
  "question": {
    "label": "问题 2",
    "statement": "假设所有玩家仅知道当天的天气状况，从第天起，每名玩家在当天行动结束后均知道其余玩家当天的行动方案和剩余的资源数量，随后确定各自第二天的行动方案。试给出一般情况下玩家应采取的策略，并对附件中的“第六关”进行具体讨论。 注1：附件所给地图中，有公共边界的两个区域称为相邻，仅有公共顶点而没有公共边界的两个区域不视作相邻。 注2：Result.xlsx中剩余资金数（剩余水量、剩余食物量）指当日所需资源全部消耗完毕后的资金数（水量、食物量）。若当日还有购买行为，则指完成购买后的资金数（水量、食物量）。",
    "tasks": [
      "假设所有玩家仅知道当天的天气状况，从第天起，每名玩家在当天行动结束后均知道其余玩家当天的行动方案和剩余的资源数量，随后确定各自第二天的行动方案",
      "试给出一般情况下玩家应采取的策略，并对附件中的“第六关”进行具体讨论"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/2020B-穿越沙漠.docx",
      "name": "2020B-穿越沙漠.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 44282,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/Result.xlsx",
      "name": "Result.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11164,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/B/附件.docx",
      "name": "附件.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 259622,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "B" / "q13" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "B" / "q13" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "B" / "q13"


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
