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
  "problem_path": "cumcm/problems/2022/D.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "为了提高气象信息的地理密度，除了实现主站间气象报文的信息共享外，还需要 使用副站气象信息加以补充。 (1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的信息传输的一般模型。若主 站间气象报文信息共享的传输方案与问题 1 相同，则只需给出副站气象报文的传输方案。 (2) 对于 𝐾 = 7， 给出 𝑁 的最大值， 并根据一般传输模型给出此时副站气象报文的传输方 案，将结果按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站能成功接收每支分 队至少一个副站的气象报文，以及任一主站平均能成功接收多少个副站的气象报文。",
    "tasks": [
      "(1) 若要求在 𝐾 分钟内完成 𝑁 个主站间气象报文的信息共享，且每个主站满足条件：对 每支分队， 成功接收该分队至少一个副站的气象报文的概率不低于0.9。 请就 𝐾 (≥ 5) 的情形， 研究 𝑁 的最大值与 𝐾 的关系，并建立 𝐾 分钟内满足以上条件的信息传输的一般模型。若主 站间气象报文信息共享的传输方案与问题 1 相同，则只需给出副站气象报文的传输方案",
      "(2) 对于 𝐾 = 7， 给出 𝑁 的最大值， 并根据一般传输模型给出此时副站气象报文的传输方 案，将结果按表 2 的格式填报。求出在你们的传输方案下平均有多少个主站能成功接收每支分 队至少一个副站的气象报文，以及任一主站平均能成功接收多少个副站的气象报文"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "D" / "q02"


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
