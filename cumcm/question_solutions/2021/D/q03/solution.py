# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-D",
  "title": "2021年 CUMCM D题：连铸切割的",
  "problem_path": "cumcm/problems/2021/D.md",
  "question_index": 3,
  "question": {
    "label": "问题 3",
    "statement": "假设实时最优切割方案和结晶器出现异常的时刻均与问题 2 相同， 在满足基本要求和正常要求的条件下，对（1）用户目标值是 8.5 米，目标范围 是 8.0~9.0 米,（2）用户目标值是 11.1 米，目标范围是10.6~11.6 米两种情况 分别按 “初始切割方案、 调整后的切割方案、 切割损失” 等内容给出具体的最优 切割方案。 附录：参数与要求 工艺参数：切割机切断一块钢坯的时间为3 分钟，切割后，返回到工作起点 的时间为 1 分钟。从结晶器中心到切割机工作起点处钢坯的长度是 60.0 米，连 铸拉坯的速度为1.0 米/分钟。当结晶器出现异常时，报废段的长度是 0.8 米。 基本要求：切割后的钢坯长度必须在 4.8~12.6 米之间，否则无法运走，阻 碍生产。下道工序能够接受的钢坯长度是 8.0~11.6 米，如果不在此范围内，可 以将钢坯运走进行二次离线切割，但切割下的部分报废，从而产生损失。例如， 12.6 米的钢坯切掉1.0 米变成 11.6 米，切下来的1.0 米报废；而小于 8.0 米的 钢坯只能全部报废。 正常要求：正常切割是按照用户要求的长度进行切割。 用户要求包含目标值 和目标范围， 钢坯的切割长度应尽量满足目标值，而在目标范围内的长度也是可 以接受的。例如，目标值是 9.5 米，目标范围是 9.0~10.0 米，则切割长度尽量 是 9.5 米，而在 9.0~10.0 米之间的长度是允许的。当钢坯长度不在目标范围内 时，会产生损失。例如，钢坯长度是11.6 米，多出来的1.6 米报废。",
    "tasks": [
      "假设实时最优切割方案和结晶器出现异常的时刻均与问题 2 相同， 在满足基本要求和正常要求的条件下，对（1）用户目标值是 8.5 米，目标范围 是 8.0~9.0 米,（2）用户目标值是 11.1 米，目标范围是10.6~11.6 米两种情况 分别按 “初始切割方案、 调整后的切割方案、 切割损失” 等内容给出具体的最优 切割方案"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/D/CUMCM2021-D.pdf",
      "name": "CUMCM2021-D.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 245779,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "D" / "q03"


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
