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
  "problem_path": "cumcm/problems/2018/D.md",
  "question_index": 6,
  "question": {
    "label": "问题 4",
    "statement": "对于颜色有如下要求： 1）蓝、黄、红三种颜色汽车的喷涂只能在C1线上进行，金色汽车的喷涂只能在C2线上进行，其他颜色汽车的喷涂可以在C1和C2任意一条喷涂线上进行。 2）除黑、白两种颜色外，在同一条喷涂线上，同种颜色的汽车应尽量连续喷涂作业。 3）喷涂线上不同颜色汽车之间的切换次数尽可能少，特别地，黑色汽车与其它颜色的汽车之间的切换代价很高。 4）不同颜色汽车在总装线上排列时的具体要求如下： （a）黑色汽车连续排列的数量在50-70辆之间，两批黑色汽车在总装线上需间隔至少20辆。 （b）白色汽车可以连续排列，也可以与颜色为蓝或棕的汽车间隔排列； （c）颜色为黄或红的汽车必须与颜色为银、灰、棕、金中的一种颜色的汽车间隔排列； （d）蓝色汽车必须与白色汽车间隔排列； （e）金色汽车要求与颜色为黄或红的汽车间隔排列；若无法满足要求，也可以与颜色为灰、棕、银中的一种颜色的汽车间隔排列； （f）颜色为灰或银的汽车可以连续排列，也可以与颜色为黄、红、金中的一种颜色的汽车间隔排列； （g）棕色汽车可以连续排列，也可以与颜色为黄、红、金、白中的一种颜色的汽车间隔排列。 （h）关于其他颜色的搭配，遵循“没有允许即为禁止”的原则。 由于该公司的生产线24小时不间断作业，以上总装线和喷涂线的各项要求对相邻班次（包括当日晚班与次日白班）的车辆同样适用。",
    "tasks": [
      "对于颜色有如下要求： 1）蓝、黄、红三种颜色汽车的喷涂只能在C1线上进行，金色汽车的喷涂只能在C2线上进行，其他颜色汽车的喷涂可以在C1和C2任意一条喷涂线上进行",
      "2）除黑、白两种颜色外，在同一条喷涂线上，同种颜色的汽车应尽量连续喷涂作业",
      "3）喷涂线上不同颜色汽车之间的切换次数尽可能少，特别地，黑色汽车与其它颜色的汽车之间的切换代价很高",
      "4）不同颜色汽车在总装线上排列时的具体要求如下： （a）黑色汽车连续排列的数量在50-70辆之间，两批黑色汽车在总装线上需间隔至少20辆",
      "（b）白色汽车可以连续排列，也可以与颜色为蓝或棕的汽车间隔排列",
      "（c）颜色为黄或红的汽车必须与颜色为银、灰、棕、金中的一种颜色的汽车间隔排列"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "name": "CUMCM-2018-Problem-D-Chinese-Appendix.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 135903,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2018_lcGi8NeCd14458641de55ec1d705ea01714ff2dd/2018-D-Chinese/CUMCM-2018-problem-D-Chinese.docx",
      "name": "CUMCM-2018-problem-D-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 30849,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2018" / "D" / "q06" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2018" / "D" / "q06" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2018" / "D" / "q06"


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
