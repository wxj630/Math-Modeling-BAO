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
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "公司计划开发一种折叠桌设计软件，根据客户任意设定的折叠桌高度、桌面边缘线的形状大小和桌脚边缘线的大致形状，给出所需平板材料的形状尺寸和切实可行的最优设计加工参数，使得生产的折叠桌尽可能接近客户所期望的形状。你们团队的任务是帮助给出这一软件设计的数学模型，并根据所建立的模型给出几个你们自己设计的创意平板折叠桌。要求给出相应的设计加工参数，画出至少8张动态变化过程的示意图。",
    "tasks": [
      "公司计划开发一种折叠桌设计软件，根据客户任意设定的折叠桌高度、桌面边缘线的形状大小和桌脚边缘线的大致形状，给出所需平板材料的形状尺寸和切实可行的最优设计加工参数，使得生产的折叠桌尽可能接近客户所期望的形状",
      "你们团队的任务是帮助给出这一软件设计的数学模型，并根据所建立的模型给出几个你们自己设计的创意平板折叠桌",
      "要求给出相应的设计加工参数，画出至少8张动态变化过程的示意图"
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
      },
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "形状"
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
RESULT_PATH = ROOT / "question_results" / "2014" / "B" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "B" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "B" / "q03"


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
