# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2025-D",
  "title": "2025年 CUMCM D题：矿井突水水流漫延模型与逃生方案",
  "problem_path": "cumcm/problems/2025/D.md",
  "question_index": 2,
  "question": {
    "label": "问题2",
    "statement": "当矿井发生突水后，安全生产部门即刻监控到突水情况，并应尽快为每个工人 的制订出有效逃生方案。请根据问题1 中所建水流漫延模型，协助安全生产部门为各矿工设 计最佳逃生路径。 假设工人在无突水水流巷道时，前进速度为4 m/s；巷道内水面高度小于等于0.3 m 时， 工人逆水行进速度为1 m/s，顺水行进速度为2 m/s；当巷道内水面高度为超过0.3 m 时，不 建议涉水通行。 假设在突水1 分钟时发布逃生通知，请对附件1 和附件2 给出的两个矿井巷道网络，分 别给出各矿工的最佳逃生路径，其中附件1 中的出入口位置分别为 (3252.16,3326.63,10.00)， (3173.10,2819.97,10.00)，矿工的位置分别为 (5808.18,5367.75,10.00)，(5194.00,4785.31, 10.00)，(6190.81,3434.29,10.00)；附件2中的出入口位置分别为 (6336.99,6073.22,36.15)， (6416.05,6579.88,8.69)，矿工的位置分别为 (4395.15,4614.53,6.59)，(3398.34,5965.56, 1.31)，(3879.44,4125.47,6.22)。将结果分别保存到文件result2-1.xlsx 和result2-2.xlsx 中（模 板文件在附件3 中）。",
    "tasks": [
      "假设在突水1 分钟时发布逃生通知，请对附件1 和附件2 给出的两个矿井巷道网络，分 别给出各矿工的最佳逃生路径，其中附件1 中的出入口位置分别为 (3252.16,3326.63,10.00)， (3173.10,2819.97,10.00)，矿工的位置分别为 (5808.18,5367.75,10.00)，(5194.00,4785.31, 10.00)，(6190.81,3434.29,10.00)",
      "将结果分别保存到文件result2-1.xlsx 和result2-2.xlsx 中（模 板文件在附件3 中）"
    ],
    "models": [
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "网络",
          "路径"
        ]
      },
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
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/D题.pdf",
      "name": "D题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 359362,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 56691,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 57596,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result1-1.xlsx",
      "name": "result1-1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 35128,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result1-2.xlsx",
      "name": "result1-2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 35128,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result2-1.xlsx",
      "name": "result2-1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 12174,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result2-2.xlsx",
      "name": "result2-2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 12206,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result3-1.xlsx",
      "name": "result3-1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 35128,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result3-2.xlsx",
      "name": "result3-2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 35128,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result4-1.xlsx",
      "name": "result4-1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 12172,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/D题/附件/附件3/result4-2.xlsx",
      "name": "result4-2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 12155,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2025" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "D" / "q02"


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
