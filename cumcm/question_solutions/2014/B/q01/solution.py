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
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "给定长方形平板尺寸为120 cm × 50 cm × 3 cm，每根木条宽2.5 cm，连接桌腿木条的钢筋固定在桌腿最外侧木条的中心位置，折叠后桌子的高度为53 cm。试建立模型描述此折叠桌的动态变化过程，在此基础上给出此折叠桌的设计加工参数（例如，桌腿木条开槽的长度等）和桌脚边缘线（图4中红色曲线）的数学描述。",
    "tasks": [
      "试建立模型描述此折叠桌的动态变化过程，在此基础上给出此折叠桌的设计加工参数（例如，桌腿木条开槽的长度等）和桌脚边缘线（图4中红色曲线）的数学描述"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "曲线"
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
          "曲线"
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
RESULT_PATH = ROOT / "question_results" / "2014" / "B" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "B" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "B" / "q01"


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
