# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2014-A",
  "title": "2014年 CUMCM A题：嫦娥三号软着陆轨道设计与控制策略",
  "problem_path": "cumcm/problems/2014/A.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "确定嫦娥三号的着陆轨道和在6个阶段的最优控制策略。",
    "tasks": [
      "确定嫦娥三号的着陆轨道和在6个阶段的最优控制策略"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "轨道",
          "着陆"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/A/CUMCM-2014A-Chinese.doc",
      "name": "CUMCM-2014A-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 41472,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/A/附件1 问题的背景与参考资料(9.3定).doc",
      "name": "附件1 问题的背景与参考资料(9.3定).doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 252416,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/A/附件2 嫦娥三号软着陆过程(9.3定).doc",
      "name": "附件2 嫦娥三号软着陆过程(9.3定).doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 1195008,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/A/附件3 距2400m处的数字高程图.tif",
      "name": "附件3 距2400m处的数字高程图.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 12432744,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/A/附件4 距月面100m处的数字高程图.tif",
      "name": "附件4 距月面100m处的数字高程图.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 1021808,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/A/CUMCM-2014A-Chinese.doc",
      "name": "CUMCM-2014A-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 41472,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/A/附件1 问题的背景与参考资料(9.3定).doc",
      "name": "附件1 问题的背景与参考资料(9.3定).doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 252416,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/A/附件2 嫦娥三号软着陆过程(9.3定).doc",
      "name": "附件2 嫦娥三号软着陆过程(9.3定).doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 1195008,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/A/附件3 距2400m处的数字高程图.tif",
      "name": "附件3 距2400m处的数字高程图.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 12432744,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/A/附件4 距月面100m处的数字高程图.tif",
      "name": "附件4 距月面100m处的数字高程图.tif",
      "suffix": ".tif",
      "kind": "media_or_archive",
      "size_bytes": 1021808,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2014" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "A" / "q02"


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
