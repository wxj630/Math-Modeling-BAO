# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2016-A",
  "title": "2016年 CUMCM A题：系泊系统的设计",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2016/A.md",
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "由于潮汐等因素的影响，布放海域的实测水深介于16m~20m之间。布放点的海水速度最大可达到1.5m/s、风速最大可达到36m/s。请给出考虑风力、水流力和水深情况下的系泊系统设计，分析不同情况下钢桶、钢管的倾斜角度、锚链形状、浮标的吃水深度和游动区域。 说明 近海风荷载可通过近似公式F=0.625×Sv2(N) QUOTE \\* MERGEFORMAT 计算，其中S为物体在风向法平面的投影面积(m2)，v为风速(m/s）。近海水流力可通过近似公式F=374×Sv2(N)计算，其中S为物体在水流速度法平面的投影面积(m2)，v为水流速度(m/s）。 附表 锚链型号和参数表 型号 长度(mm) 单位长度的质量(kg/m) I 78 3.2 II 105 7 III 120 12.5 IV 150 19.5 V 180 28.12 表注：长度是指每节链环的长度。",
    "tasks": [
      "请给出考虑风力、水流力和水深情况下的系泊系统设计，分析不同情况下钢桶、钢管的倾斜角度、锚链形状、浮标的吃水深度和游动区域",
      "说明 近海风荷载可通过近似公式F=0.625×Sv2(N) QUOTE \\* MERGEFORMAT 计算，其中S为物体在风向法平面的投影面积(m2)，v为风速(m/s）",
      "近海水流力可通过近似公式F=374×Sv2(N)计算，其中S为物体在水流速度法平面的投影面积(m2)，v为水流速度(m/s）"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度",
          "形状"
        ]
      },
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "系统"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2016" / "A" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2016" / "A" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2016" / "A" / "q03"


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
