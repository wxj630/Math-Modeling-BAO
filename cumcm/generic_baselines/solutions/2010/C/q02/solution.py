# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2010-C",
  "question_index": 2,
  "title": "2010年 CUMCM C题：输油管的布置",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2010/C.md",
  "question": {
    "label": "问题 2",
    "statement": "设计院目前需对一更为复杂的情形进行具体的设计。两炼油厂的具体位置由附图所示，其中A厂位于郊区（图中的I区域），B厂位于城区（图中的II区域），两个区域的分界线用图中的虚线表示。图中各字母表示的距离（单位：千米）分别为a = 5，b = 8，c = 15，l = 20。 若所有管线的铺设费用均为每千米7.2万元。 铺设在城区的管线还需增加拆迁和工程补偿等附加费用，为对此项附加费用进行估计，聘请三家工程咨询公司（其中公司一具有甲级资质，公司二和公司三具有乙级资质）进行了估算。估算结果如下表所示： 工程咨询公司 公司一 公司二 公司三 附加费用（万元/千米） 21 24 20 请为设计院给出管线布置方案及相应的费用。",
    "tasks": [
      "设计院目前需对一更为复杂的情形进行具体的设计",
      "估算结果如下表所示： 工程咨询公司 公司一 公司二 公司三 附加费用（万元/千米） 21 24 20 请为设计院给出管线布置方案及相应的费用"
    ],
    "models": [
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案",
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract/2010/2010_rd4LEPmmd1095c70a7fb9d0898a08495837d8c93/2010C/cumcm2010C.doc",
      "name": "cumcm2010C.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 43008,
      "source_root": "/Users/wuxiaojun/Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2010" / "C" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2010" / "C" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2010" / "C" / "q02"


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
    lines.append(f"- 单问运行：`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python {solution_path}`")
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
