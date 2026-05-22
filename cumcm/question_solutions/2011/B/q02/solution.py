# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2011-B",
  "title": "2011年 CUMCM B题：交巡警服务平台的设置与调度",
  "problem_path": "cumcm/problems/2011/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "针对全市（主城六区A，B，C，D，E，F）的具体情况，按照设置交巡警服务平台的原则和任务，分析研究该市现有交巡警服务平台设置方案（参见附件）的合理性。如果有明显不合理，请给出解决方案。 如果该市地点P（第32个节点）处发生了重大刑事案件，在案发3分钟后接到报警，犯罪嫌疑人已驾车逃跑。为了快速搜捕嫌疑犯，请给出调度全市交巡警服务平台警力资源的最佳围堵方案。 附件1：A区和全市六区交通网络与平台设置的示意图。 附件2：全市六区交通网络与平台设置的相关数据表（共5个工作表）。",
    "tasks": [
      "针对全市（主城六区A，B，C，D，E，F）的具体情况，按照设置交巡警服务平台的原则和任务，分析研究该市现有交巡警服务平台设置方案（参见附件）的合理性",
      "如果有明显不合理，请给出解决方案",
      "为了快速搜捕嫌疑犯，请给出调度全市交巡警服务平台警力资源的最佳围堵方案"
    ],
    "models": [
      {
        "key": "graph_network",
        "name": "图论与复杂网络",
        "chapter": "CH4",
        "keywords": [
          "网络",
          "节点",
          "平台"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "调度",
          "方案"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/B/cumcm2011B.doc",
      "name": "cumcm2011B.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 33792,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/B/cumcm2011B附件1_A区和全市六区交通网络与平台设置的示意图.doc",
      "name": "cumcm2011B附件1_A区和全市六区交通网络与平台设置的示意图.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 102912,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2011_LOsf8a1w1cfbe73ef037f2f60e5c144c0f96a94f/B/cumcm2011B附件2_全市六区交通网路和平台设置的数据表.xls",
      "name": "cumcm2011B附件2_全市六区交通网路和平台设置的数据表.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 116736,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2011" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2011" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2011" / "B" / "q02"


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
