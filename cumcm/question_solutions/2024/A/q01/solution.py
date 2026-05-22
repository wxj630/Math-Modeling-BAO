# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2024-A",
  "title": "2024年 CUMCM A题：板凳龙”  闹元宵",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2024/A.md",
  "question_index": 1,
  "question": {
    "label": "问题 1",
    "statement": "舞龙队沿螺距为 55 cm 的等距螺线顺时针盘入，各把手中心均位于螺线上。龙 头前把手的行进速度始终保持 1 m/s。初始时，龙头位于螺线第 16 圈 A 点处（见图 4）。请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）。 同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）。 27.5 cm 第 2 个孔，孔径 5.5 cm 27.5 cm 第 1 个孔，孔径 5.5 cm 30 cm 27.5 cm 27.5 cm 30 cm 220 cm 第 2 个孔， 孔径 5.5 cm 第 1 个孔， 孔径 5.5 cm 27.5 cm 27.5 cm 前一节龙身后部 后一节龙身前部 前把手 341 cm 2",
    "tasks": [
      "请 给出从初始时刻到 300 s 为止，每秒整个舞龙队的位置和速度（指龙头、龙身和龙尾各前把 手及龙尾后把手中心的位置和速度，下同），将结果保存到文件 result1.xlsx 中（模板文件见 附件，其中“龙尾 （后）”表示龙尾后把手， 其余的均是前把手，结果保留 6 位小数， 下同）",
      "同时在论文中给出 0 s、60 s、120 s、180 s、240 s、300 s 时，龙头前把手、龙头后面第 1、 51、101、151、201 节龙身前把手和龙尾后把手的位置和速度（格式见表 1 和表 2）"
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
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 758066,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 517064,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 15292,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2024_pmkWxf8H9cfe9984c1a1a5b1263e5dd3b5596ed5/CUMCM2024Problems/A题/附件/result4.xlsx",
      "name": "result4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 346204,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2024" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2024" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2024" / "A" / "q01"


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
