# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2014-B",
  "title": "2014年 CUMCM B题：创意平板折叠桌",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2014/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "折叠桌的设计应做到产品稳固性好、加工方便、用材最少。对于任意给定的折叠桌高度和圆形桌面直径的设计要求，讨论长方形平板材料和折叠桌的最优设计加工参数，例如，平板尺寸、钢筋位置、开槽长度等。对于桌高70 cm，桌面直径80 cm的情形，确定最优设计加工参数。",
    "tasks": [
      "折叠桌的设计应做到产品稳固性好、加工方便、用材最少",
      "对于任意给定的折叠桌高度和圆形桌面直径的设计要求，讨论长方形平板材料和折叠桌的最优设计加工参数，例如，平板尺寸、钢筋位置、开槽长度等",
      "对于桌高70 cm，桌面直径80 cm的情形，确定最优设计加工参数"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/B/CUMCM-2014B-Chinese.doc",
      "name": "CUMCM-2014B-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 1233408,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/B/CUMCM-2014B-附件.mp4",
      "name": "CUMCM-2014B-附件.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 2876285,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/B/CUMCM-2014B-Chinese.doc",
      "name": "CUMCM-2014B-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 1233408,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/B/CUMCM-2014B-附件.mp4",
      "name": "CUMCM-2014B-附件.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 2876285,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2014" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "B" / "q02"


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
