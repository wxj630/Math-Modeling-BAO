# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-B",
  "title": "2023年 CUMCM B题：多波束测线问题",
  "problem_path": "cumcm/problems/2023/B.md",
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "海水深度数据（附件.xlsx）是若干年前某海域（南北长5 海里、东西宽4 海里） 单波束测量的测深数据，现希望利用这组数据为多波束测量船的测量布线提供帮助。在设计测 线时，有如下要求：(1) 沿测线扫描形成的条带尽可能地覆盖整个待测海域；(2) 相邻条带之间 的重叠率尽量控制在20% 以下；(3) 测线的总长度尽可能短。在设计出具体的测线后，请计算 如下指标：(1) 测线的总长度；(2) 漏测海区占总待测海域面积的百分比；(3) 在重叠区域中， 重叠率超过20% 部分的总长度。 注 在附件中，横、纵坐标的单位是海里，海水深度的单位是米。1 海里=1852 米。 附件 海水深度数据",
    "tasks": [
      "海水深度数据（附件.xlsx）是若干年前某海域（南北长5 海里、东西宽4 海里） 单波束测量的测深数据，现希望利用这组数据为多波束测量船的测量布线提供帮助。在设计测 线时，有如下要求：",
      "(3) 测线的总长度尽可能短。在设计出具体的测线后，请计算 如下指标："
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "坐标"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 899651,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9222,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9445,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 313543,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2023" / "B" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "B" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "B" / "q04"


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
