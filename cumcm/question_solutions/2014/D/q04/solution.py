# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2014-D",
  "title": "2014年 CUMCM D题：储药柜的设计",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2014/D.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "附件2给出了每一种药品编号对应的最大日需求量。在储药槽的长度为1.5m、每天仅集中补药一次的情况下，请计算每一种药品需要的储药槽个数。为保证药房储药满足需求，根据问题3中单个储药柜的规格，计算最少需要多少个储药柜。",
    "tasks": [
      "附件2给出了每一种药品编号对应的最大日需求量",
      "在储药槽的长度为1.5m、每天仅集中补药一次的情况下，请计算每一种药品需要的储药槽个数",
      "为保证药房储药满足需求，根据问题3中单个储药柜的规格，计算最少需要多少个储药柜"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc",
      "name": "CUMCM-2014D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 524288,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件1-药盒型号.xls",
      "name": "附件1-药盒型号.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 125952,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件2-药品需求量.xls",
      "name": "附件2-药品需求量.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 97792,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc",
      "name": "CUMCM-2014D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 524288,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件1-药盒型号.xls",
      "name": "附件1-药盒型号.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 125952,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件2-药品需求量.xls",
      "name": "附件2-药品需求量.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 97792,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2014" / "D" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "D" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "D" / "q04"


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
