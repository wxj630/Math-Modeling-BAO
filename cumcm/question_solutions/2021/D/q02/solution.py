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
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "在结晶器出现异常时，给出实时的最优切割方案：(1)在钢坯第 1 次出现报废段时，给出此段钢坯的切割方案；(2)在出现新的报废段后 （如图2）， 给出新一段钢坯的切割方案和当前段钢坯切割的调整方案，或声明不作调整。 假设结晶器出现异常的时刻在 0.0、45.6、98.6、131.5、190.8、233.3、 266.0、270.7 和327.9（单位：分钟） ， 用户目标值是9.5 米， 目标范围是9.0~10.0 米。在满足基本要求和正常要求的条件下， 按 “初始切割方案、 调整后的切割方 案、切割损失”等内容列表给出这些时刻具体的最优切割方案。",
    "tasks": [
      "在结晶器出现异常时，给出实时的最优切割方案：",
      "(1)在钢坯第 1 次出现报废段时，给出此段钢坯的切割方案",
      "(2)在出现新的报废段后 （如图2）， 给出新一段钢坯的切割方案和当前段钢坯切割的调整方案，或声明不作调整。 假设结晶器出现异常的时刻在 0.0、45.6、98.6、131.5、190.8、233.3、 266.0、270.7 和327.9（单位：分钟） ， 用户目标值是9.5 米， 目标范围是9.0~10.0 米。在满足基本要求和正常要求的条件下， 按 “初始切割方案、 调整后的切割方 案、切割损失”等内容列表给出这些时刻具体的最优切割方案"
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
RESULT_PATH = ROOT / "question_results" / "2021" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "D" / "q02"


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
