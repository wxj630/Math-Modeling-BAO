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
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "若巷道的某一点发生突水，试分析水流过程，建立突水水流在巷道的流动漫延 模型。 对附件1 和附件2 给出的两个矿井巷道网络，分别给出网络中各巷道水流的变化情况， 其中附件1 中的突水点位置为A1 (5349.03,4931.90,10.00)，附件2 中的突水点位置为A2 (4143.12,4376.28,6.33)。将结果分别保存到文件result1-1.xlsx 和result1-2.xlsx 中（模板文 件在附件3 中，所有结果均保留2 位小数，下同），其中端点水流到达时刻是指突水水流首 次流经该点的时刻，巷道充满水时刻是指巷道中水流的水平面达到巷道最高点的时刻。",
    "tasks": [
      "若巷道的某一点发生突水，试分析水流过程，建立突水水流在巷道的流动漫延 模型",
      "对附件1 和附件2 给出的两个矿井巷道网络，分别给出网络中各巷道水流的变化情况， 其中附件1 中的突水点位置为A1 (5349.03,4931.90,10.00)，附件2 中的突水点位置为A2 (4143.12,4376.28,6.33)",
      "将结果分别保存到文件result1-1.xlsx 和result1-2.xlsx 中（模板文 件在附件3 中，所有结果均保留2 位小数，下同），其中端点水流到达时刻是指突水水流首 次流经该点的时刻，巷道充满水时刻是指巷道中水流的水平面达到巷道最高点的时刻"
    ],
    "models": [
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "网络"
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
RESULT_PATH = ROOT / "question_results" / "2025" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "D" / "q01"


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
