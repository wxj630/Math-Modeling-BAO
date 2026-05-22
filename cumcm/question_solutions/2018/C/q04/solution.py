# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2018-C",
  "title": "2018年 CUMCM C题：大型百货商场会员画像描绘",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/C.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "建立数学模型计算会员生命周期中非活跃会员的激活率，即从非活跃会员转化为活跃会员的可能性，并从实际销售数据出发，确定激活率和商场促销活动之间的关系模型。",
    "tasks": [
      "建立数学模型计算会员生命周期中非活跃会员的激活率，即从非活跃会员转化为活跃会员的可能性，并从实际销售数据出发，确定激活率和商场促销活动之间的关系模型"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-C-Chinese/CUMCM-2018-Problem C-Chinese.docx",
      "name": "CUMCM-2018-Problem C-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 19919,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-C-Chinese/readme.txt",
      "name": "readme.txt",
      "suffix": ".txt",
      "kind": "media_or_archive",
      "size_bytes": 51,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "C" / "q04"


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
