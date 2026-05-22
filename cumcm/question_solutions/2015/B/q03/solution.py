# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2015-B",
  "title": "2015年 CUMCM B题：互联网+”时代的出租车资源配置",
  "problem_path": "cumcm/problems/2015/B.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "如果要创建一个新的打车软件服务平台，你们将设计什么样的补贴方案，并论证其合理性。",
    "tasks": [
      "如果要创建一个新的打车软件服务平台，你们将设计什么样的补贴方案，并论证其合理性"
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
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "平台"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "合理性"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/B/CUMCM-2015-problem B-Chinese.doc",
      "name": "CUMCM-2015-problem B-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 25088,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2015/2015_m00L7uGp5743fadb9289f545d4ed5a1b300622fa/B/CUMCM-2015-problem B-Chinese.doc",
      "name": "CUMCM-2015-problem B-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 25088,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2015" / "B" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2015" / "B" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2015" / "B" / "q03"


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
