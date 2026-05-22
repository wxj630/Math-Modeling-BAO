# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2022-A",
  "title": "2022年 CUMCM A题：波浪能最大输出功率设计",
  "problem_path": "cumcm/problems/2022/A.md",
  "question_index": 1,
  "question": {
    "label": "问题1",
    "statement": "如图1 所示，中轴底座固定于隔层的中心位置，弹簧和直线阻尼器一端固定在振 子上，一端固定在中轴底座上，振子沿中轴做往复运动。直线阻尼器的阻尼力与浮子和振子的 相对速度成正比，比例系数为直线阻尼器的阻尼系数。考虑浮子在波浪中只做垂荡运动（参见 附件1），建立浮子与振子的运动模型。初始时刻浮子和振子平衡于静水中，利用附件3 和附 件4 提供的参数值（其中波浪频率取1.4005 s−1，这里及以下出现的频率均指圆频率，角度均 采用弧度制），分别对以下两种情况计算浮子和振子在波浪激励力 𝑓cos 𝜔𝑡（𝑓 为波浪激励力 振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移和速度：(1) 直 线阻尼器的阻尼系数为10000 N·s/m；(2) 直线阻尼器的阻尼系数与浮子和振子的相对速度的绝 对值的幂成正比，其中比例系数取10000，幂指数取0.5。将结果存放在result1-1.xlsx 和 result1-2.xlsx 中。在论文中给出10 s、20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移和速 度。",
    "tasks": [
      "如图1 所示，中轴底座固定于隔层的中心位置，弹簧和直线阻尼器一端固定在振 子上，一端固定在中轴底座上，振子沿中轴做往复运动。直线阻尼器的阻尼力与浮子和振子的 相对速度成正比，比例系数为直线阻尼器的阻尼系数。考虑浮子在波浪中只做垂荡运动（参见 附件1），建立浮子与振子的运动模型。初始时刻浮子和振子平衡于静水中，利用附件3 和附 件4 提供的参数值（其中波浪频率取1.4005 s−1，这里及以下出现的频率均指圆频率，角度均 采用弧度制），分别对以下两种情况计算浮子和振子在波浪激励力 𝑓cos 𝜔𝑡（𝑓 为波浪激励力 振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移和速度：",
      "(2) 直线阻尼器的阻尼系数与浮子和振子的相对速度的绝 对值的幂成正比，其中比例系数取10000，幂指数取0.5。将结果存放在result1-1.xlsx 和 result1-2.xlsx 中。在论文中给出10 s、20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移和速 度"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/A题.pdf",
      "name": "A题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 988984,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result1-1.xlsx",
      "name": "result1-1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10168,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result1-2.xlsx",
      "name": "result1-2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10168,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/result3.xlsx",
      "name": "result3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10415,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10771,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 10532,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/A题.rar",
      "name": "A题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 7749890,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 568238,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/C题.rar",
      "name": "C题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 764520,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/D题.pdf",
      "name": "D题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 529148,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2022_5eWlbmTt28f88a0815a79d555da8b7072f971633/E题.rar",
      "name": "E题.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 1278086,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2022" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "A" / "q01"


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
