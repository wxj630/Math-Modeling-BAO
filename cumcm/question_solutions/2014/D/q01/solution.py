# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2014-D",
  "title": "2014年 CUMCM D题：储药柜的设计",
  "problem_path": "cumcm/problems/2014/D.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "药房内的盒装药品种类繁多，药盒尺寸规格差异较大，附件1中给出了一些药盒的规格。请利用附件1的数据，给出竖向隔板间距类型最少的储药柜设计方案，包括类型的数量和每种类型所对应的药盒规格。",
    "tasks": [
      "药房内的盒装药品种类繁多，药盒尺寸规格差异较大，附件1中给出了一些药盒的规格",
      "请利用附件1的数据，给出竖向隔板间距类型最少的储药柜设计方案，包括类型的数量和每种类型所对应的药盒规格"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc",
      "name": "CUMCM-2014D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 524288,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件1-药盒型号.xls",
      "name": "附件1-药盒型号.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 125952,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/D/附件2-药品需求量.xls",
      "name": "附件2-药品需求量.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 97792,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/CUMCM-2014D-Chinese.doc",
      "name": "CUMCM-2014D-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 524288,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件1-药盒型号.xls",
      "name": "附件1-药盒型号.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 125952,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/D/附件2-药品需求量.xls",
      "name": "附件2-药品需求量.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 97792,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2014" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "D" / "q01"


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
