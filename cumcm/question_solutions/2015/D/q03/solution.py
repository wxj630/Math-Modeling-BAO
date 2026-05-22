# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2015-D",
  "title": "2015年 CUMCM D题：众筹筑屋规划方案设计",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2015/D.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "一般而言，投资回报率达到25%以上的众筹项目才会被成功执行。你们所给出的众筹筑屋方案Ⅱ能否被成功执行？如果能，请说明理由。如果不能，应怎样调整才能使此众筹筑屋项目能被成功执行？",
    "tasks": [
      "你们所给出的众筹筑屋方案Ⅱ能否被成功执行？"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/CUMCM-2015-Problem D-Chinese.doc",
      "name": "CUMCM-2015-Problem D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 16384,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件1 赛题所需的相关数据.doc",
      "name": "附件1 赛题所需的相关数据.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 54784,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件2 中华人民共和国土地增值税暂行条例.pdf",
      "name": "附件2 中华人民共和国土地增值税暂行条例.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 222573,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件3 其他相关说明.pdf",
      "name": "附件3 其他相关说明.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 134443,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/CUMCM-2015-Problem D-Chinese.doc",
      "name": "CUMCM-2015-Problem D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 16384,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件1 赛题所需的相关数据.doc",
      "name": "附件1 赛题所需的相关数据.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 54784,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件2 中华人民共和国土地增值税暂行条例.pdf",
      "name": "附件2 中华人民共和国土地增值税暂行条例.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 222573,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/D/附件3 其他相关说明.pdf",
      "name": "附件3 其他相关说明.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 134443,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2015" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2015" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2015" / "D" / "q03"


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
