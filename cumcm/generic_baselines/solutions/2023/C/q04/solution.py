# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2023-C",
  "question_index": 4,
  "title": "2023年 CUMCM C题：蔬菜类商品的自动定价与补货决策",
  "problem_path": "cumcm/problems/2023/C.md",
  "question": {
    "label": "问题4",
    "statement": "为了更好地制定蔬菜商品的补货和定价决策，商超还需要采集哪些相关数据， 这些数据对解决上述问题有何帮助，请给出你们的意见和理由。 附件1 6 个蔬菜品类的商品信息 附件2 销售流水明细数据 附件3 蔬菜类商品的批发价格 附件4 蔬菜类商品的近期损耗率 注 (1) 附件1 中，部分单品名称包含的数字编号表示不同的供应来源。 (2) 附件4 中的损耗率反映了近期商品的损耗情况，通过近期盘点周期的数据计算得到。 2023 年高教社杯全国大学生数学建模竞赛题目 （请先阅读“全国大学生数学建模竞赛论文格式规范”）",
    "tasks": [
      "为了更好地制定蔬菜商品的补货和定价决策，商超还需要采集哪些相关数据， 这些数据对解决上述问题有何帮助，请给出你们的意见和理由。 附件1 6 个蔬菜品类的商品信息 附件2 销售流水明细数据 附件3 蔬菜类商品的批发价格 附件4 蔬菜类商品的近期损耗率 注",
      "(2) 附件4 中的损耗率反映了近期商品的损耗情况，通过近期盘点周期的数据计算得到。 2023 年高教社杯全国大学生数学建模竞赛题目 （请先阅读“全国大学生数学建模竞赛论文格式规范”）"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "决策"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 361842,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 17803,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 39150980,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 1150765,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2023_Y20WPner9fa62862794e6dc82731a5561ce1132f/C题/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 18678,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2023" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2023" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2023" / "C" / "q04"


def write_generic_report(result: dict, solution_path: Path) -> None:
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
    lines.append(f"- 通用代码：{solution_path}")
    lines.append(f"- 单问运行：`.venv/bin/python {solution_path}`")
    lines.append(f"- 结果 JSON：{RESULT_PATH}")
    lines.append(f"- 实验报告：{REPORT_PATH}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{ROOT / artifact}")
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
