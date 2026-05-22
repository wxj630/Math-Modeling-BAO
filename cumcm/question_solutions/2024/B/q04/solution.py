# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-B",
  "title": "2024年 CUMCM B题：生产过程中的决策",
  "problem_path": "cumcm/problems/2024/B.md",
  "question_index": 4,
  "question": {
    "label": "问题 4",
    "statement": "假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明 (1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率； (2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等） 。 (3) 购买单价、 检测成本、 装配成本、 市场售价、 调换损失和拆解费用的单位均为元/件。",
    "tasks": [
      "假设问题 2 和问题 3 中零配件、 半成品和成品的次品率均是通过抽样检测方法 （例如，你在问题 1 中使用的方法）得到的，请重新完成问题 2 和问题 3。 附录 说明",
      "(1) 半成品、成品的次品率是将正品零配件（或者半成品）装配后的产品次品率",
      "(2) 不合格成品中的调换损失是指除调换次品之外的损失 （如： 物流成本、企业信誉等）",
      "(3) 购买单价、 检测成本、 装配成本、 市场售价、 调换损失和拆解费用的单位均为元/件"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "成本"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "检测"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 636910,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "B" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "B" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "B" / "q04"


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
