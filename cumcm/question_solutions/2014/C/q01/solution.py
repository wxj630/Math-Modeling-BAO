# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2014-C",
  "title": "2014年 CUMCM C题：生猪养殖场的经营管理",
  "problem_path": "cumcm/problems/2014/C.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "已知从母猪配种到所产的猪仔长成肉猪出栏需要约9个月时间。假设该养猪场估计9个月后三年内生猪价格变化的预测曲线如图2所示，请根据此价格预测确定该养猪场的最佳经营策略，计算这三年内的平均年利润，并给出在此策略下的母猪及肉猪存栏数曲线",
    "tasks": [
      "假设该养猪场估计9个月后三年内生猪价格变化的预测曲线如图2所示，请根据此价格预测确定该养猪场的最佳经营策略，计算这三年内的平均年利润，并给出在此策略下的母猪及肉猪存栏数曲线"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "曲线",
          "预测"
        ]
      },
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
          "利润"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2014_cumcm2014problems/C/CUMCM2014C-Chinese.docx",
      "name": "CUMCM2014C-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 40568,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2014/2014_cumcm2014problems/C/CUMCM2014C-Chinese.docx",
      "name": "CUMCM2014C-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 40568,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2014" / "C" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2014" / "C" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2014" / "C" / "q01"


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
