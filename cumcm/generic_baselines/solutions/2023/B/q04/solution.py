# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2023-B",
  "question_index": 4,
  "title": "2023年 CUMCM B题：多波束测线问题",
  "problem_path": "cumcm/problems/2023/B.md",
  "question": {
    "label": "问题4",
    "statement": "海水深度数据（附件.xlsx）是若干年前某海域（南北长5 海里、东西宽4 海里） 单波束测量的测深数据，现希望利用这组数据为多波束测量船的测量布线提供帮助。在设计测 线时，有如下要求：(1) 沿测线扫描形成的条带尽可能地覆盖整个待测海域；(2) 相邻条带之间 的重叠率尽量控制在20% 以下；(3) 测线的总长度尽可能短。在设计出具体的测线后，请计算 如下指标：(1) 测线的总长度；(2) 漏测海区占总待测海域面积的百分比；(3) 在重叠区域中， 重叠率超过20% 部分的总长度。 注 在附件中，横、纵坐标的单位是海里，海水深度的单位是米。1 海里=1852 米。 附件 海水深度数据",
    "tasks": [
      "海水深度数据（附件.xlsx）是若干年前某海域（南北长5 海里、东西宽4 海里） 单波束测量的测深数据，现希望利用这组数据为多波束测量船的测量布线提供帮助。在设计测 线时，有如下要求：",
      "(3) 测线的总长度尽可能短。在设计出具体的测线后，请计算 如下指标："
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "坐标"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 899651,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result1.xlsx",
      "name": "result1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9222,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/result2.xlsx",
      "name": "result2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 9445,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/B题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 313543,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2023" / "B" / "q04" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2023" / "B" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2023" / "B" / "q04"


def write_generic_report(result: dict, solution_path: Path) -> None:
    def repo_rel(path: Path | str) -> str:
        path = Path(path)
        try:
            return str(path.resolve().relative_to(ROOT.parent.resolve()))
        except ValueError:
            return str(path)

    f = result["formulation"]
    lines = [
        f"# {result['problem_id']} {result['question_label']} 通用基线报告",
        "",
        "> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。",
        "",
        "## 题目与任务",
        "",
        f"- 题目：{result['title']}",
        f"- 问题：{result['question_label']}",
        f"- 原问：{result['statement']}",
        "",
        "## 通用模型选择",
        "",
        f"- 模型：{result['selected_model']['name']}（{result['selected_model']['chapter']}：{result['selected_model']['chapter_title']}）",
        f"- 教程参考：{result['selected_model']['doc']}",
        f"- 通用方法：`{result['experiment_result'].get('method', 'generic_model')}`",
        "",
        "## 变量、约束与公式",
        "",
        "### 变量定义",
    ]
    lines.extend(f"- {item}" for item in f.get("decision_variables", []))
    lines += ["", "### 约束条件"]
    lines.extend(f"- {item}" for item in f.get("constraints", []))
    lines += ["", "### 模型公式 / 目标函数"]
    lines.extend(f"- `{item}`" for item in f.get("objective_or_equations", []))
    lines += ["", "## 运行与产物", ""]
    lines.append(f"- 通用代码：{repo_rel(solution_path)}")
    lines.append(f"- 单问运行：`.venv/bin/python {repo_rel(solution_path)}`")
    lines.append(f"- 结果 JSON：{repo_rel(RESULT_PATH)}")
    lines.append(f"- 实验报告：{repo_rel(REPORT_PATH)}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{repo_rel(ROOT / artifact)}")
    lines += ["", "## 数据来源", ""]
    ds = result.get("data_source", {})
    lines.append(f"- 类型：{ds.get('source_type', 'unknown')}")
    if ds.get("path"):
        lines.append(f"- 路径：{ds['path']}")
    lines.append(f"- 说明：{ds.get('note', '')}")
    lines += ["", "## 核心结果", "", "```json", json.dumps(result["experiment_result"], ensure_ascii=False, indent=2), "```", ""]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, Path(__file__).resolve())
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
