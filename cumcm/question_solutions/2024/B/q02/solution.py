# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-B",
  "title": "2024年 CUMCM B题：生产过程中的决策",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "已知两种零配件和成品次品率，请为企业生产过程的各个阶段作出决策： (1) 对零配件（零配件 1 和/或零配件 2）是否进行检测，如果对某种零配件不检测，这 种零配件将直接进入到装配环节；否则将检测出的不合格零配件丢弃； (2) 对装配好的每一件成品是否进行检测， 如果不检测， 装配后的成品直接进入到市场； 否则只有检测合格的成品进入到市场； (3) 对检测出的不合格成品是否进行拆解，如果不拆解，直接将不合格成品丢弃；否则 对拆解后的零配件，重复步骤(1)和步骤(2)； (4) 对用户购买的不合格品，企业将无条件予以调换，并产生一定的调换损失（如物流 成本、企业信誉等）。对退回的不合格品，重复步骤(3)。 请根据你们所做的决策， 对表 1 中的情形给出具体的决策方案，并给出决策的依据及相 应的指标结果。",
    "tasks": [
      "(3)。 请根据你们所做的决策， 对表 1 中的情形给出具体的决策方案，并给出决策的依据及相 应的指标结果"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "成本",
          "决策",
          "方案"
        ]
      },
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "指标"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "检测"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 636910,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "B" / "q02"


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
