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
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "当矿井出现第二个突水点后，安全生产部门即刻监控到突水情况，并尽快调整 逃生方案。请协助安全生产部门调整最佳逃生路径。 在前面问题的基础上，假设在第二突水点突水1 分钟后，安全生产部门发布调整后的逃 生方案。对附件1 和附件2 给出的两个矿井巷道网络，分别给出各矿工调整后的最佳逃生路 径。请将结果分别保存到文件result4-1.xlsx 和result4-2.xlsx 中（模板文件在附件3 中）。 附件说明 附件1.xlsx、附件2.xlsx 两个矿井的巷道网络数据，均包含“端点”和“巷道”两个 工作表。“端点”工作表记录了巷道中各端点的三维坐标 (X, Y, Z)（其中 XY 为水平面，Z 为 高程）；“巷道”工作表记录了各巷道的两个端点编号。 附件3 计算结果模板文件夹，其中 result𝑖-𝑗.xlsx 问题 𝑖 中矿井 𝑗 的结果文件模板",
    "tasks": [
      "对附件1 和附件2 给出的两个矿井巷道网络，分别给出各矿工调整后的最佳逃生路 径",
      "请将结果分别保存到文件result4-1.xlsx 和result4-2.xlsx 中（模板文件在附件3 中）",
      "附件3 计算结果模板文件夹，其中 result𝑖-𝑗.xlsx 问题 𝑖 中矿井 𝑗 的结果文件模板"
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
RESULT_PATH = ROOT / "question_results" / "2025" / "D" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "D" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "D" / "q04"


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
