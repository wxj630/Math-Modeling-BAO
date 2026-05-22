# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2010-C",
  "title": "2010年 CUMCM C题：输油管的布置",
  "problem_path": "cumcm/problems/2010/C.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "设计院目前需对一更为复杂的情形进行具体的设计。两炼油厂的具体位置由附图所示，其中A厂位于郊区（图中的I区域），B厂位于城区（图中的II区域），两个区域的分界线用图中的虚线表示。图中各字母表示的距离（单位：千米）分别为a = 5，b = 8，c = 15，l = 20。 若所有管线的铺设费用均为每千米7.2万元。 铺设在城区的管线还需增加拆迁和工程补偿等附加费用，为对此项附加费用进行估计，聘请三家工程咨询公司（其中公司一具有甲级资质，公司二和公司三具有乙级资质）进行了估算。估算结果如下表所示： 工程咨询公司 公司一 公司二 公司三 附加费用（万元/千米） 21 24 20 请为设计院给出管线布置方案及相应的费用。",
    "tasks": [
      "设计院目前需对一更为复杂的情形进行具体的设计",
      "估算结果如下表所示： 工程咨询公司 公司一 公司二 公司三 附加费用（万元/千米） 21 24 20 请为设计院给出管线布置方案及相应的费用"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2010" / "C" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2010" / "C" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2010" / "C" / "q02"


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
