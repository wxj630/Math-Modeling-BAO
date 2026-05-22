# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-B",
  "title": "2010年 CUMCM B题：2010年上海世博会影响力的定量评估",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/B.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "2010年上海世博会是首次在中国举办的世界博览会。从1851年伦敦的“万国工业博览会”开始，世博会正日益成为各国人民交流历史文化、展示科技成果、体现合作精神、展望未来发展等的重要舞台。请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力",
    "tasks": [
      "请你们选择感兴趣的某个侧面，建立数学模型，利用互联网数据，定量评估2010年上海世博会的影响力"
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
          "评估"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010B/cumcm2010B.doc",
      "name": "cumcm2010B.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 27136,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010B/cumcm2010B.doc",
      "name": "cumcm2010B.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 27136,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "B" / "q01"


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
