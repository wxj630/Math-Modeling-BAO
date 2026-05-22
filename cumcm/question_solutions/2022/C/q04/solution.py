# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-C",
  "title": "2022年 CUMCM C题：古代玻璃制品的成分分析与鉴别",
  "problem_path": "cumcm/problems/2022/C.md",
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "针对不同类别的玻璃文物样品，分析其化学成分之间的关联关系，并比较不同类 别之间的化学成分关联关系的差异性。 附件 表单1 玻璃文物的基本信息 表单2 已分类玻璃文物的化学成分比例，其中 (1) 文物采样点为该编号文物表面某部位的随机采样，其风化属性与附件表单1 中相应文 物一致。 (2) 部位1 和部位2 是文物造型上不同的两个部位，其成分与含量可能存在差异。 (3) 未风化点是风化文物表面未风化区域内的点。 (4) 严重风化点取自风化层。 表单3 未分类玻璃文物的化学成分比例",
    "tasks": [
      "针对不同类别的玻璃文物样品，分析其化学成分之间的关联关系，并比较不同类 别之间的化学成分关联关系的差异性。 附件 表单1 玻璃文物的基本信息 表单2 已分类玻璃文物的化学成分比例，其中"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "比较"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "分类"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 708530,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/C题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 94507,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2022" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "C" / "q04"


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
