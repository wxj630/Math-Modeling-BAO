# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2019-B",
  "title": "2019年 CUMCM B题：同心协力”策略研究",
  "problem_path": "cumcm/problems/2019/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "在现实情形中，队员发力时机和力度不可能做到精确控制，存在一定误 差， 于是鼓面可能出现倾斜。 试建立模型描述队员的发力时机和力度与某一特定 时刻的鼓面倾斜角度的关系。 设队员人数为8， 绳长为1.7m， 鼓面初始时刻是水 平静止的，初始位置较绳子水平时下降 11 cm，表 1 中给出了队员们的不同发力 时机和力度，求 0.1 s 时鼓面的倾斜角度。",
    "tasks": [
      "试建立模型描述队员的发力时机和力度与某一特定 时刻的鼓面倾斜角度的关系",
      "设队员人数为8， 绳长为1.7m， 鼓面初始时刻是水 平静止的，初始位置较绳子水平时下降 11 cm，表 1 中给出了队员们的不同发力 时机和力度，求 0.1 s 时鼓面的倾斜角度"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.docx",
      "name": "CUMCM-1019-Problem-B-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 60187,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/B-2019中文/CUMCM-1019-Problem-B-Chinese.pdf",
      "name": "CUMCM-1019-Problem-B-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 390962,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2019" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2019" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2019" / "B" / "q02"


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
