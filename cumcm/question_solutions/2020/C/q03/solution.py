# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-C",
  "title": "2020年 CUMCM C题：中小微企业的信贷决策",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/C.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "企业的生产经营和经济效益可能会受到一些突发因素影响，而且突发因素往往对不同行业、不同类别的企业会有不同的影响。综合考虑附件2中各企业的信贷风险和可能的突发因素（例如：新冠病毒疫情）对各企业的影响，给出该银行在年度信贷总额为1亿元时的信贷调整策略。 附件1 123家有信贷记录企业的相关数据 附件2 302家无信贷记录企业的相关数据 附件3 银行贷款年利率与客户流失率关系的2019年统计数据 附件中数据说明：",
    "tasks": [
      "综合考虑附件2中各企业的信贷风险和可能的突发因素（例如：新冠病毒疫情）对各企业的影响，给出该银行在年度信贷总额为1亿元时的信贷调整策略"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
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
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "统计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/2020C-中小微企业的信贷决策.docx",
      "name": "2020C-中小微企业的信贷决策.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 23624,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件1：123家有信贷记录企业的相关数据.xlsx",
      "name": "附件1：123家有信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 21273447,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件2：302家无信贷记录企业的相关数据.xlsx",
      "name": "附件2：302家无信贷记录企业的相关数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 41682618,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/C/附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "name": "附件3：银行贷款年利率与客户流失率关系的统计数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 13576,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "C" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "C" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "C" / "q03"


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
