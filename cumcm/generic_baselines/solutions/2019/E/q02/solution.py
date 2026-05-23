# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2019-E",
  "question_index": 2,
  "title": "2019年 CUMCM E题：薄利多销”分析",
  "problem_path": "cumcm/problems/2019/E.md",
  "question": {
    "label": "问题 2",
    "statement": "建立适当的指标衡量商场每天的打折力度，并计算该商场从2016年11月30日到2019年1月2日每天的打折力度",
    "tasks": [
      "建立适当的指标衡量商场每天的打折力度，并计算该商场从2016年11月30日到2019年1月2日每天的打折力度"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "指标"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/CUMCM-2019-Problem-E-Chinese.docx",
      "name": "CUMCM-2019-Problem-E-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 21724,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/CUMCM-2019-Problem-E-Chinese.pdf",
      "name": "CUMCM-2019-Problem-E-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 215893,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件1.csv",
      "name": "附件1.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 54635677,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件2.csv",
      "name": "附件2.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 61806709,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件3.csv",
      "name": "附件3.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 2166871,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件4.csv",
      "name": "附件4.csv",
      "suffix": ".csv",
      "kind": "data",
      "size_bytes": 589429,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/E-2019中文/data/附件5.xlsx",
      "name": "附件5.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 14738,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2019" / "E" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2019" / "E" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2019" / "E" / "q02"


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
