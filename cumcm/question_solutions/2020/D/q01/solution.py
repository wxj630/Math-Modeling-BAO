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
  "problem_path": "cumcm/problems/2020/D.md",
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "附件1中的表level是工件1在水平状态下的测量数据，其轮廓线如图4所示，请标注出轮廓线的各项参数值：槽口宽度（如等）、圆弧半径（如等）、圆心之间的距离（如等）、圆弧的长度、水平线段的长度（如等）、斜线线段的长度、斜线与水平线之间的夹角（如等）和人字形线的高度（）。",
    "tasks": [
      "附件1中的表level是工件1在水平状态下的测量数据，其轮廓线如图4所示，请标注出轮廓线的各项参数值：槽口宽度（如等）、圆弧半径（如等）、圆心之间的距离（如等）、圆弧的长度、水平线段的长度（如等）、斜线线段的长度、斜线与水平线之间的夹角（如等）和人字形线的高度（）"
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
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "标注"
        ]
      },
      {
        "key": "signal_text",
        "name": "图像文本与信号",
        "chapter": "CH10",
        "keywords": [
          "轮廓"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/2020D-接触式轮廓仪的自动标注.docx",
      "name": "2020D-接触式轮廓仪的自动标注.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 338796,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件1_工件1的测量数据.xlsx",
      "name": "附件1_工件1的测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 7407027,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件2_工件2的整体测量数据.xlsx",
      "name": "附件2_工件2的整体测量数据.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20515708,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件3_工件2的局部测量数据（圆）.xlsx",
      "name": "附件3_工件2的局部测量数据（圆）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15871647,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2020_05k6B8WT92d3955f5c5e95dd086e59163e5f584b/D/附件4_工件2的局部测量数据（角）.xlsx",
      "name": "附件4_工件2的局部测量数据（角）.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 5941285,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2020" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "D" / "q01"


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
