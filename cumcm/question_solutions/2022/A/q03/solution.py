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
  "question_index": 3,
  "question": {
    "label": "问题3",
    "statement": "如图2 所示，中轴底座固定于隔层的中心位置，中轴架通过转轴铰接于中轴底座 中心，中轴绕转轴转动，PTO 系统连接振子和转轴架，并处于中轴与转轴所在的平面。除了直 线阻尼器，在转轴上还安装了旋转阻尼器和扭转弹簧，直线阻尼器和旋转阻尼器共同做功输出 能量。在波浪的作用下，浮子进行摇荡运动，并通过转轴及扭转弹簧和旋转阻尼器带动中轴转 动。振子随中轴转动，同时沿中轴进行滑动。扭转弹簧的扭矩与浮子和振子的相对角位移成正 比，比例系数为扭转弹簧的刚度。旋转阻尼器的扭矩与浮子和振子的相对角速度成正比，比例 系数为旋转阻尼器的旋转阻尼系数。考虑浮子只做垂荡和纵摇运动（参见附件2），建立浮子 与振子的运动模型。初始时刻浮子和振子平衡于静水中，利用附件3 和附件4 提供的参数值（波 浪频率取1.7152 s−1），假定直线阻尼器和旋转阻尼器的阻尼系数均为常量，分别为10000 N·s/m 和1000 N·m·s，计算浮子与振子在波浪激励力和波浪激励力矩 𝑓cos 𝜔𝑡，𝐿cos 𝜔𝑡（𝑓 为波浪激 励力振幅，𝐿 为波浪激励力矩振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移与速度和纵摇角位移与角速度。将结果存放在result3.xlsx 中。在论文中给出10 s、 20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移与速度和纵摇角位移与角速度。",
    "tasks": [
      "考虑浮子只做垂荡和纵摇运动（参见附件2），建立浮子 与振子的运动模型",
      "初始时刻浮子和振子平衡于静水中，利用附件3 和附件4 提供的参数值（波 浪频率取1.7152 s−1），假定直线阻尼器和旋转阻尼器的阻尼系数均为常量，分别为10000 N·s/m 和1000 N·m·s，计算浮子与振子在波浪激励力和波浪激励力矩 𝑓cos 𝜔𝑡，𝐿cos 𝜔𝑡（𝑓 为波浪激 励力振幅，𝐿 为波浪激励力矩振幅，𝜔 为波浪频率）作用下前40 个波浪周期内时间间隔为0.2 s 的垂荡位移与速度和纵摇角位移与角速度",
      "将结果存放在result3.xlsx 中",
      "在论文中给出10 s、 20 s、40 s、60 s、100 s 时，浮子与振子的垂荡位移与速度和纵摇角位移与角速度"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "系统"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "A" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "A" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "A" / "q03"


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
