# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-D",
  "title": "2022年 CUMCM D题：气象报文信息卫星通信传输",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2022/D.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "若要求在 𝐾 = 8 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足 条件： 对每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.97， 请给出 𝑁 的 最大值，并给出此时主站间气象报文信息共享的传输方案与副站气象报文信息的传输方案，将 前者按表 1 的格式填报，后者按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站 能成功接收每支分队至少一个副站的气象报文，以及任一个主站平均能成功接收多少个副站的 气象报文。",
    "tasks": [
      "若要求在 𝐾 = 8 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足 条件： 对每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.97， 请给出 𝑁 的 最大值",
      "给出此时主站间气象报文信息共享的传输方案与副站气象报文信息的传输方案，将 前者按表 1 的格式填报，后者按表 2 的格式填报"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "question_results" / "2022" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "D" / "q03"


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
