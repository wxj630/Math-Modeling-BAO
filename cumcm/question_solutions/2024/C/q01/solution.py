# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-C",
  "title": "2024年 CUMCM C题：农作物的种植策略",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/C.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板文件见附件 3）。 (1) 超过部分滞销，造成浪费； (2) 超过部分按 2023 年销售价格的 50%降价出售。",
    "tasks": [
      "假定各种农作物未来的预期销售量、种植成本、亩产量和销售价格相对于 2023 年保持 稳定，每季种植的农作物在当季销售。如果某种作物每季的总产量超过相应的预期销售量，超过部 分不能正常销售。请针对以下两种情况，分别给出该乡村 2024~2030 年农作物的最优种植方案，将 结果分别填入 result1_1.xlsx 和 result1_2.xlsx 中（模板文件见附件 3）"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "成本",
          "方案"
        ]
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "未来"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 558863,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 17147,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 21976,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件3/result1_1.xlsx",
      "name": "result1_1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 81837,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件3/result1_2.xlsx",
      "name": "result1_2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 81836,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/C题/附件3/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 81836,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "C" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "C" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "C" / "q01"


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
