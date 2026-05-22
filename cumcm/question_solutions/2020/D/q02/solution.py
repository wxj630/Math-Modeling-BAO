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
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "同一工件在不同次测量时，由于工件放置的角度和位置不同，轮廓线参数的计算值也会存在差异。附件1中的表down给出了工件1在倾斜一个角度和有一些水平位移状态下轮廓线的测量数据。请计算该工件测量时的倾斜角度，并作水平校正。在数据校正后，完成问题1的任务，并比较两种测量状态下工件1各项参数计算值之间的差异。",
    "tasks": [
      "同一工件在不同次测量时，由于工件放置的角度和位置不同，轮廓线参数的计算值也会存在差异",
      "附件1中的表down给出了工件1在倾斜一个角度和有一些水平位移状态下轮廓线的测量数据",
      "请计算该工件测量时的倾斜角度，并作水平校正",
      "在数据校正后，完成问题1的任务，并比较两种测量状态下工件1各项参数计算值之间的差异"
    ],
    "models": [
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
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "比较"
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
RESULT_PATH = ROOT / "question_results" / "2020" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2020" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2020" / "D" / "q02"


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
