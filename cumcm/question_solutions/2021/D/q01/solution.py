# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-D",
  "title": "2021年 CUMCM D题：连铸切割的",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2021/D.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "在满足基本要求和正常要求的条件下，依据尾坯长度制定出最优的 切割方案。假定用户目标值为 9.5 米，目标范围为 9.0~10.0 米，对以下尾坯长 度：109.0、93.4、80.9、72.0、62.7、52.5、44.9、42.7、31.6、22.7、14.5 和13.7（单位：米） ，按“尾坯长度、切割方案、切割损失”等内容列表给出具 体的最优切割方案。",
    "tasks": [
      "假定用户目标值为 9.5 米，目标范围为 9.0~10.0 米，对以下尾坯长 度：109.0、93.4、80.9、72.0、62.7、52.5、44.9、42.7、31.6、22.7、14.5 和13.7（单位：米） ，按“尾坯长度、切割方案、切割损失”等内容列表给出具 体的最优切割方案"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/D/CUMCM2021-D.pdf",
      "name": "CUMCM2021-D.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 245779,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "D" / "q01"


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
