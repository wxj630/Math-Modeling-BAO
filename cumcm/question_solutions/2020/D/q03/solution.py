# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2020-D",
  "title": "2020年 CUMCM D题：接触式轮廓仪的自动标注",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2020/D.md",
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "在对工件作多次检测时，工件每次放置的角度、测量的起点和终点都会有偏差，这导致了每次测量实际是对整个工件中的某一部分进行检测。附件2提供了对工件2的10次测量数据，请基于这些数据完成：(1) 每次测量时工件2的倾斜角度；(2) 标注出工件2轮廓线的各项参数值（同问题1）；(3) 画出工件2的完整轮廓线。",
    "tasks": [
      "(2) 标注出工件2轮廓线的各项参数值（同问题1）",
      "(3) 画出工件2的完整轮廓线"
    ],
    "models": [
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "标注",
          "检测"
        ]
      },
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/2020D-接触式轮廓仪的自动标注.docx",
      "name": "2020D-接触式轮廓仪的自动标注.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 338796,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件1_工件1的测量数据.xlsx",
      "name": "附件1_工件1的测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 7407027,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件2_工件2的整体测量数据.xlsx",
      "name": "附件2_工件2的整体测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20515708,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件3_工件2的局部测量数据（圆）.xlsx",
      "name": "附件3_工件2的局部测量数据（圆）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15871647,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件4_工件2的局部测量数据（角）.xlsx",
      "name": "附件4_工件2的局部测量数据（角）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 5941285,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "D" / "q03"


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
