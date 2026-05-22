# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2018-D",
  "title": "2018年 CUMCM D题：汽车总装线的配置",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/D.md",
  "question_index": 4,
  "question": {
    "label": "问题 2",
    "statement": "四驱汽车连续装配数量不得超过2辆，两批四驱汽车之间间隔的两驱汽车的数量至少是10辆；柴油汽车连续装配数量不得超过2辆，两批柴油汽车之间间隔的汽油汽车的数量至少10辆。若间隔数量无法满足要求，仍希望间隔数量越多越好。间隔数量在5-9辆仍是可以接受的，但代价很高。",
    "tasks": [
      "四驱汽车连续装配数量不得超过2辆，两批四驱汽车之间间隔的两驱汽车的数量至少是10辆",
      "柴油汽车连续装配数量不得超过2辆，两批柴油汽车之间间隔的汽油汽车的数量至少10辆",
      "若间隔数量无法满足要求，仍希望间隔数量越多越好",
      "间隔数量在5-9辆仍是可以接受的，但代价很高"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "name": "CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 135903,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-problem-D-Chinese.docx",
      "name": "CUMCM-2018-problem-D-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 30849,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "D" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "D" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "D" / "q04"


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
