# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2016-C",
  "title": "2016年 CUMCM C题：电池剩余放电时间预测",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2016/C.md",
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "试建立以20A到100A之间任一恒定电流强度放电时的放电曲线的数学模型，并用MRE评估模型的精度。用表格和图形给出电流强度为55A时的放电曲线。",
    "tasks": [
      "试建立以20A到100A之间任一恒定电流强度放电时的放电曲线的数学模型，并用MRE评估模型的精度",
      "用表格和图形给出电流强度为55A时的放电曲线"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "放电",
          "曲线"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "曲线"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "评估"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-C-Appendix-Chinese.xlsx",
      "name": "CUMCM2016-C-Appendix-Chinese.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 135587,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-Problem-C-Chinese-version.docx",
      "name": "CUMCM2016-Problem-C-Chinese-version.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 22502,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2016" / "C" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2016" / "C" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2016" / "C" / "q02"


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
