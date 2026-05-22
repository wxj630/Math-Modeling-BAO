# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2018-D",
  "title": "2018年 CUMCM D题：汽车总装线的配置",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2018/D.md",
  "question_index": 1,
  "question": {
    "label": "问题 一",
    "statement": "问题背景 某汽车公司生产多种型号的汽车，每种型号由品牌、配置、动力、驱动、颜色5种属性确定。品牌分为A1和A2两种，配置分为B1、B2、B3、B4、B5和B6六种，动力分为汽油和柴油2种，驱动分为两驱和四驱2种，颜色分为黑、白、蓝、黄、红、银、棕、灰、金9种。 公司每天可装配各种型号的汽车460辆，其中白班、晚班（每班12小时）各230辆。每天生产各种型号车辆的具体数量根据市场需求和销售情况确定。附件给出了该企业2018年9月17日至9月23日一周的生产计划。 公司的装配流程如图1所示。待装配车辆按一定顺序排成一列，首先匀速通过总装线依次进行总装作业，随后按序分为C1、C2线进行喷涂作业。",
    "tasks": [
      "问题背景 某汽车公司生产多种型号的汽车，每种型号由品牌、配置、动力、驱动、颜色5种属性确定",
      "每天生产各种型号车辆的具体数量根据市场需求和销售情况确定",
      "附件给出了该企业2018年9月17日至9月23日一周的生产计划"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "动力"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "配置"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "name": "CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 135903,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-problem-D-Chinese.docx",
      "name": "CUMCM-2018-problem-D-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 30849,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "D" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "D" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "D" / "q01"


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
