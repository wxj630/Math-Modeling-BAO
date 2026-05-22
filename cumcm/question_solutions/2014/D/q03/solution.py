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
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "考虑补药的便利性，储药柜的宽度不超过2.5m、高度不超过2m，传送装置占用的高度为0.5m，即储药柜的最大允许有效高度为1.5m。药盒与两层横向隔板之间的间隙超出2mm的部分可视为高度冗余，平面冗余＝高度冗余×宽度冗余。在问题2计算结果的基础上，确定储药柜横向隔板间距的类型数量，使得储药柜的总平面冗余量尽可能地小，且横向隔板间距的类型数量也尽可能地少。",
    "tasks": [
      "在问题2计算结果的基础上，确定储药柜横向隔板间距的类型数量，使得储药柜的总平面冗余量尽可能地小，且横向隔板间距的类型数量也尽可能地少"
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
RESULT_PATH = ROOT / "question_results" / "2014" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "D" / "q03"


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
