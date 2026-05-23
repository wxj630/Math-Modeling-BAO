# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2021-D",
  "question_index": 2,
  "title": "2021年 CUMCM D题：连铸切割的",
  "problem_path": "cumcm/problems/2021/D.md",
  "question": {
    "label": "问题 2",
    "statement": "在结晶器出现异常时，给出实时的最优切割方案：(1)在钢坯第 1 次出现报废段时，给出此段钢坯的切割方案；(2)在出现新的报废段后 （如图2）， 给出新一段钢坯的切割方案和当前段钢坯切割的调整方案，或声明不作调整。 假设结晶器出现异常的时刻在 0.0、45.6、98.6、131.5、190.8、233.3、 266.0、270.7 和327.9（单位：分钟） ， 用户目标值是9.5 米， 目标范围是9.0~10.0 米。在满足基本要求和正常要求的条件下， 按 “初始切割方案、 调整后的切割方 案、切割损失”等内容列表给出这些时刻具体的最优切割方案。",
    "tasks": [
      "在结晶器出现异常时，给出实时的最优切割方案：",
      "(1)在钢坯第 1 次出现报废段时，给出此段钢坯的切割方案",
      "(2)在出现新的报废段后 （如图2）， 给出新一段钢坯的切割方案和当前段钢坯切割的调整方案，或声明不作调整。 假设结晶器出现异常的时刻在 0.0、45.6、98.6、131.5、190.8、233.3、 266.0、270.7 和327.9（单位：分钟） ， 用户目标值是9.5 米， 目标范围是9.0~10.0 米。在满足基本要求和正常要求的条件下， 按 “初始切割方案、 调整后的切割方 案、切割损失”等内容列表给出这些时刻具体的最优切割方案"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "最优",
          "方案"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/D/CUMCM2021-D.pdf",
      "name": "CUMCM2021-D.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 245779,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2021" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2021" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2021" / "D" / "q02"


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
