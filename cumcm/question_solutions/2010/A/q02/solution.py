# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-A",
  "title": "2010年 CUMCM A题：储油罐的变位识别与罐容表标定",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/A.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "对于图1所示的实际储油罐，试建立罐体变位后标定罐容表的数学模型，即罐内储油量与油位高度及变位参数（纵向倾斜角度α和横向偏转角度β ）之间的一般关系。请利用罐体变位后在进/出油过程中的实际检测数据（附件2），根据你们所建立的数学模型确定变位参数，并给出罐体变位后油位高度间隔为10cm的罐容表标定值。进一步利用附件2中的实际检测数据来分析检验你们模型的正确性与方法的可靠性。 附件1：小椭圆储油罐的实验数据 附件2：实际储油罐的检测数据 PAGE PAGE 1",
    "tasks": [
      "对于图1所示的实际储油罐，试建立罐体变位后标定罐容表的数学模型，即罐内储油量与油位高度及变位参数（纵向倾斜角度α和横向偏转角度β ）之间的一般关系",
      "请利用罐体变位后在进/出油过程中的实际检测数据（附件2），根据你们所建立的数学模型确定变位参数，并给出罐体变位后油位高度间隔为10cm的罐容表标定值",
      "进一步利用附件2中的实际检测数据来分析检验你们模型的正确性与方法的可靠性"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc",
      "name": "cumcm2010A.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 96768,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls",
      "name": "问题A附件1：实验采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 59392,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls",
      "name": "问题A附件2：实际采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 83456,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/cumcm2010A.doc",
      "name": "cumcm2010A.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 96768,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件1：实验采集数据表.xls",
      "name": "问题A附件1：实验采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 59392,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010A/问题A附件2：实际采集数据表.xls",
      "name": "问题A附件2：实际采集数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 83456,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "A" / "q02"


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
