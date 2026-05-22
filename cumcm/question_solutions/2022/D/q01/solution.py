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
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型。 (2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意消息的完整性，例 如：在“发送信息所属站点序号”一栏中填写“5”，表示本轮所发送消息来自于第 5 号主站，",
    "tasks": [
      "(1) 要求在 𝐾 分钟内完成 𝑁 (≥ 5) 支分队主站间气象报文的信息共享，请研究 𝐾 的最小值与 𝑁 的关系，并建立 𝐾 分钟内实现 𝑁 个主站间气象报文信息共享的一般传输 模型",
      "(2) 在上述模型中， 取 𝑁 = 9， 给出 𝐾 的相应最小值， 并根据一般传输模型给出此时主站 间气象报文的信息共享方案，将结果按表 1 的格式填报。填报结果时，注意消息的完整性，例 如：在“发送信息所属站点序号”一栏中填写“5”，表示本轮所发送消息来自于第 5 号主站，"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "D" / "q01"


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
