# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2016-A",
  "title": "2016年 CUMCM A题：系泊系统的设计",
  "problem_path": "cumcm/problems/2016/A.md",
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "在问题1的假设下，计算海面风速为36m/s时钢桶和各节钢管的倾斜角度、锚链形状和浮标的游动区域。请调节重物球的质量，使得钢桶的倾斜角度不超过5度，锚链在锚点与海床的夹角不超过16度。",
    "tasks": [
      "在问题1的假设下，计算海面风速为36m/s时钢桶和各节钢管的倾斜角度、锚链形状和浮标的游动区域"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度",
          "形状"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2016" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2016" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2016" / "A" / "q02"


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
