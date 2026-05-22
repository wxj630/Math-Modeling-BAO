# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2018-B",
  "title": "2018年 CUMCM B题：赛题",
  "problem_path": "cumcm/problems/2018/B.md",
  "question_index": 2,
  "question": {
    "label": "问题 2",
    "statement": "两道工序的物料加工作业情况，每个物料的第一和第二道工序分别由两台不同的CNC依次加工完成；",
    "tasks": [
      "两道工序的物料加工作业情况，每个物料的第一和第二道工序分别由两台不同的CNC依次加工完成"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "通用"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "通用"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_1_result.xls",
      "name": "Case_1_result.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 37376,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_2_result.xls",
      "name": "Case_2_result.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 31744,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_1.xls",
      "name": "Case_3_result_1.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 35840,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2/Case_3_result_2.xls",
      "name": "Case_3_result_2.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 37888,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix-2.rar",
      "name": "CUMCM-2018-Problem-B-Chinese-Appendix-2.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 32472,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese-Appendix1.doc",
      "name": "CUMCM-2018-Problem-B-Chinese-Appendix1.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 1284608,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-B-Chinese/CUMCM-2018-Problem-B-Chinese.doc",
      "name": "CUMCM-2018-Problem-B-Chinese.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 119808,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "B" / "q02" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "B" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "B" / "q02"


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
