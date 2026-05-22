# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2016-C",
  "title": "2016年 CUMCM C题：电池剩余放电时间预测",
  "problem_path": "cumcm/problems/2016/C.md",
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "附件1是同一生产批次电池出厂时以不同电流强度放电测试的完整放电曲线的采样数据。请根据附件1用初等函数表示各放电曲线，并分别给出各放电曲线的平均相对误差（MRE，定义见附件1）。如果在新电池使用中，分别以30A、40A、50A、60A和70A电流强度放电，测得电压都为9.8伏时，根据你获得的模型，电池的剩余放电时间分别是多少？",
    "tasks": [
      "请根据附件1用初等函数表示各放电曲线，并分别给出各放电曲线的平均相对误差（MRE，定义见附件1）"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "放电",
          "曲线"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据",
          "曲线"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-C-Appendix-Chinese.xlsx",
      "name": "CUMCM2016-C-Appendix-Chinese.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 135587,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese/CUMCM2016-Problem-C-Chinese-version.docx",
      "name": "CUMCM2016-Problem-C-Chinese-version.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 22502,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2016" / "C" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2016" / "C" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2016" / "C" / "q01"


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
