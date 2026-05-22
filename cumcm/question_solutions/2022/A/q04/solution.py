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
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "考虑浮子在波浪中只做垂荡和纵摇的情形，针对直线阻尼器和旋转阻尼器的阻尼 系数均为常量的情况，建立确定直线阻尼器和旋转阻尼器最优阻尼系数的数学模型，直线阻尼 器和旋转阻尼器的阻尼系数均在区间 [0,100000] 内取值。利用附件3 和附件4 提供的参数值 （波浪频率取1.9806 s−1）计算最大输出功率及相应的最优阻尼系数。 附件1 垂荡的动画 附件2 垂荡和纵摇的动画 附件3 不同入射波浪频率下的附加质量、附加转动惯量、兴波阻尼系数、波浪激励力（矩） 振幅 附件4 浮子和振子的物理参数和几何参数值 附录 术语 浮体在波浪的作用下做摇荡运动时，会受到海水的作用，包括附加惯性力（矩）、兴波阻 尼力（矩）和静水恢复力（矩）。 附加惯性力（矩） 推动浮体做摇荡运动的力（矩）不仅要推动浮体运动，还要推动浮体 周围的流体运动。因此，要使浮体在海水中获得（角）加速度，需要施加额外的力（矩），称 为附加惯性力（矩）。附加惯性力（矩）对应产生一个虚拟质量（虚拟转动惯量），即为附加 质量（附加转动惯量）。 兴波阻尼力（矩） 浮体在海水中做摇荡运动时，会兴起波浪，从而产生对浮体摇荡运动 的阻力（矩），称为兴波阻尼力（矩）。兴波阻尼力（矩）与摇荡运动的（角）速度成正比， 方向相反，比例系数称为兴波阻尼系数。 静水恢复力 浮体在海水中做垂荡运动时，会受到使浮体回到平衡位置的作用力，称为静 水恢复力。静水恢复力实际上是由浮体在垂荡运动时所受到的浮力变化引起的。 静水恢复力矩 浮体在海水中做纵摇运动时，会受到使浮体转正的力矩，称为静水恢复力 矩，其大小与浮体相对于静水面的转角成正比，比例系数称为静水恢复力矩系数。",
    "tasks": [
      "考虑浮子在波浪中只做垂荡和纵摇的情形，针对直线阻尼器和旋转阻尼器的阻尼 系数均为常量的情况，建立确定直线阻尼器和旋转阻尼器最优阻尼系数的数学模型，直线阻尼 器和旋转阻尼器的阻尼系数均在区间 [0,100000] 内取值",
      "利用附件3 和附件4 提供的参数值 （波浪频率取1.9806 s−1）计算最大输出功率及相应的最优阻尼系数"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "几何"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优"
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
RESULT_PATH = ROOT / "question_results" / "2022" / "A" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2022" / "A" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2022" / "A" / "q04"


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
