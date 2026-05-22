# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2023-E",
  "title": "2023年 CUMCM E题：黄河水沙监测数据分析",
  "problem_path": "cumcm/problems/2023/E.md",
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "根据该水文站的水沙通量和河底高程的变化情况，分析每年6-7 月小浪底水库进 行“调水调沙”的实际效果。如果不进行“调水调沙”，10 年以后该水文站的河底高程会如何？ 附件1 2016-2021 年黄河水沙监测数据 附件2 黄河断面的测量数据 附件3 黄河部分监测点的监测数据 附录 说明 (1) “水位”和“河底高程”均以“1985 国家高程基准”（海拔72.26 米）为基准面。 (2) 附件中的“起点距离”以河岸边某定点作为起点。",
    "tasks": [
      "根据该水文站的水沙通量和河底高程的变化情况，分析每年6-7 月小浪底水库进 行“调水调沙”的实际效果。如果不进行“调水调沙”，10 年以后该水文站的河底高程会如何？ 附件1 2016-2021 年黄河水沙监测数据 附件2 黄河断面的测量数据 附件3 黄河部分监测点的监测数据 附录 说明"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "效果"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/A题.rar",
      "name": "A题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 877589,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题.rar",
      "name": "B题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 1168748,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题.rar",
      "name": "C题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 38172817,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/D题.pdf",
      "name": "D题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 416221,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/E题.pdf",
      "name": "E题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 480525,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 660315,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 26402,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 38257,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/E题.rar",
      "name": "E题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 1163790,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2023" / "E" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2023" / "E" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2023" / "E" / "q04"


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
