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
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "如果本周计划生产的物料只能在两周及以后使用，请重新考虑问题2 和问题3。能 否将你们的方法推广到一般情况，即如果本周计划生产的物料只能在 𝑘 (≥2) 周及以后使用， 应如何制定生产计划。 附件 2019~2022 年的需求数据 附录 说明 (1) 将附件数据第1 次出现的时间（2019 年1 月2 日）所在的周设定为第1 周，以后的每 周从周一开始至周日结束，例如，2019 年1 月7 日至13 日为第2 周，以此类推。 (2) 在制定本周的生产计划时，可以使用任何历史数据、需求特征以及预测数据，但不能 使用本周及本周以后的实际需求数据。 (3) 服务水平= 1 − 缺货量 实际需求量。 (4) 库存量和缺货量分别指物料在周末的库存量和缺货量。",
    "tasks": [
      "(2) 在制定本周的生产计划时，可以使用任何历史数据、需求特征以及预测数据，但不能 使用本周及本周以后的实际需求数据"
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
          "预测"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "E" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "E" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "E" / "q04"


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
