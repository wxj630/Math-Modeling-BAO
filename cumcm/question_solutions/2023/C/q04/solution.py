# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-C",
  "title": "2023年 CUMCM C题：蔬菜类商品的自动定价与补货决策",
  "problem_path": "cumcm/problems/2023/C.md",
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "为了更好地制定蔬菜商品的补货和定价决策，商超还需要采集哪些相关数据， 这些数据对解决上述问题有何帮助，请给出你们的意见和理由。 附件1 6 个蔬菜品类的商品信息 附件2 销售流水明细数据 附件3 蔬菜类商品的批发价格 附件4 蔬菜类商品的近期损耗率 注 (1) 附件1 中，部分单品名称包含的数字编号表示不同的供应来源。 (2) 附件4 中的损耗率反映了近期商品的损耗情况，通过近期盘点周期的数据计算得到。 2023 年高教社杯全国大学生数学建模竞赛题目 （请先阅读“全国大学生数学建模竞赛论文格式规范”）",
    "tasks": [
      "为了更好地制定蔬菜商品的补货和定价决策，商超还需要采集哪些相关数据， 这些数据对解决上述问题有何帮助，请给出你们的意见和理由。 附件1 6 个蔬菜品类的商品信息 附件2 销售流水明细数据 附件3 蔬菜类商品的批发价格 附件4 蔬菜类商品的近期损耗率 注",
      "(2) 附件4 中的损耗率反映了近期商品的损耗情况，通过近期盘点周期的数据计算得到。 2023 年高教社杯全国大学生数学建模竞赛题目 （请先阅读“全国大学生数学建模竞赛论文格式规范”）"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "决策"
        ]
      },
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
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 361842,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 17803,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 39150980,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 1150765,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 18678,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2023" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "C" / "q04"


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
