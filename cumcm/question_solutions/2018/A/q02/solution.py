# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2018-A",
  "title": "2018年 CUMCM A题：高温作业专用服装设计",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/A.md",
  "question_index": 2,
  "question": {
    "label": "问题 3",
    "statement": "当环境温度为80时，确定II层和IV层的最优厚度，确保工作30分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟。 附件1. 专用服装材料的参数值 附件2. 假人皮肤外侧的测量温度",
    "tasks": [
      "当环境温度为80时，确定II层和IV层的最优厚度，确保工作30分钟时，假人皮肤外侧温度不超过47ºC，且超过44ºC的时间不超过5分钟"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "温度"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-A-Chinese/CUMCM-2018-Problem-A-Chinese-Appendix.xlsx",
      "name": "CUMCM-2018-Problem-A-Chinese-Appendix.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 79229,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-A-Chinese/CUMCM-2018-Problem-A-Chinese.docx",
      "name": "CUMCM-2018-Problem-A-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 27099,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "A" / "q02"


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
