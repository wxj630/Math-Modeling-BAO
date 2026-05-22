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
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "如果按照物料需求量的预测值来安排生产，可能会产生较大的库存，或者出现较 多的缺货，给企业带来经济和信誉方面的损失。企业希望从需求量的预测值、需求特征、库存 量和缺货量等方面综合考虑，以便更合理地安排生产。 请提供一种制定生产计划的方法，从第101 周（见附录(1)）开始，在每周初，制定本周的 物料生产计划（见附录(2)），安排生产，直至第177 周为止，使得平均服务水平不低于85%（见 附录(3)）。这里假设：本周计划生产的物料，只能在下周及以后使用。为便于统一计算结果， 进一步假设第100 周末的库存量和缺货量均为零，第100 周的生产计划数恰好等于第101 周的 实际需求数。 请在问题1 选定的6 种物料中选择一种物料，将其第 101 ∼110 周的生产计划数、实际 需求量、库存量、缺货量（见附录(4)）和服务水平按表1 的形式填写，放在正文中。",
    "tasks": [
      "如果按照物料需求量的预测值来安排生产，可能会产生较大的库存，或者出现较 多的缺货，给企业带来经济和信誉方面的损失。企业希望从需求量的预测值、需求特征、库存 量和缺货量等方面综合考虑，以便更合理地安排生产。 请提供一种制定生产计划的方法，从第101 周（见附录",
      "(3)）。这里假设：本周计划生产的物料，只能在下周及以后使用。为便于统一计算结果， 进一步假设第100 周末的库存量和缺货量均为零，第100 周的生产计划数恰好等于第101 周的 实际需求数。 请在问题1 选定的6 种物料中选择一种物料，将其第 101 ∼110 周的生产计划数、实际 需求量、库存量、缺货量（见附录"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "预测"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "综合"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "E" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "E" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "E" / "q02"


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
