# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2021-A",
  "title": "2021年 CUMCM A题：FAST”主动反射面的形状调节",
  "problem_path": "cumcm/problems/2021/A.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "当待观测天体𝑆位于𝛼 = 36.795°, 𝛽 = 78.169°时，确定理想抛物面。建立反射面板调节 模型， 调节相关促动器的伸缩量，使反射面尽量贴近该理想抛物面。 将理想抛物面的顶点坐标， 以及调节后反射面 300 米口径内的主索节点编号、位置坐标、各促动器的伸缩量等结果按照规 定的格式（见附件4）保存在“result.xlsx”文件中。",
    "tasks": [
      "当待观测天体𝑆位于𝛼 = 36.795°, 𝛽 = 78.169°时，确定理想抛物面",
      "建立反射面板调节 模型， 调节相关促动器的伸缩量，使反射面尽量贴近该理想抛物面",
      "将理想抛物面的顶点坐标， 以及调节后反射面 300 米口径内的主索节点编号、位置坐标、各促动器的伸缩量等结果按照规 定的格式（见附件4）保存在“result.xlsx”文件中"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "坐标",
          "抛物面"
        ]
      },
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "节点"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/CUMCM2021-A.pdf",
      "name": "CUMCM2021-A.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 481705,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件1.csv",
      "name": "附件1.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 75107,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件2.csv",
      "name": "附件2.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 137593,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件3.csv",
      "name": "附件3.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 65581,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/A/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10110,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2021" / "A" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2021" / "A" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2021" / "A" / "q02"


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
