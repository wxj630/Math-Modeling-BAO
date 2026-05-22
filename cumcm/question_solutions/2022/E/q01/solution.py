# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-E",
  "title": "2022年 CUMCM E题：小批量物料的生产安排",
  "problem_path": "cumcm/problems/2022/E.md",
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "请对附件中的历史数据进行分析，选择6 种应当重点关注的物料（可从物料需求 出现的频数、数量、趋势和销售单价等方面考虑），建立物料需求的周预测模型（即以周为基 本时间单位，预测物料的周需求量，见附录(1)），并利用历史数据对预测模型进行评价。",
    "tasks": [
      "请对附件中的历史数据进行分析，选择6 种应当重点关注的物料（可从物料需求 出现的频数、数量、趋势和销售单价等方面考虑），建立物料需求的周预测模型（即以周为基 本时间单位，预测物料的周需求量，见附录",
      "(1)），并利用历史数据对预测模型进行评价"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据",
          "预测"
        ]
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "预测",
          "趋势"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "评价"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/E题.pdf",
      "name": "E题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 640657,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 675320,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2022" / "E" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "E" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "E" / "q01"


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
