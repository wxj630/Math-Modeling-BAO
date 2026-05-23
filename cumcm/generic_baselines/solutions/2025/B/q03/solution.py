# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2025-B",
  "question_index": 3,
  "title": "2025年 CUMCM B题：碳化硅外延层厚度的确定",
  "problem_path": "cumcm/problems/2025/B.md",
  "question": {
    "label": "问题3",
    "statement": "光波可以在外延层界面和衬底界面产生多次反射和透射（图2），从而产生多光 束干涉。请推导产生多光束干涉的必要条件，以及多光束干涉对外延层厚度计算精度可能产 生的影响。 请根据多光束干涉的必要条件，分析附件3 和附件4 提供的硅晶圆片的测试结果是否 出现多光束干涉，给出确定硅外延层厚度计算的数学模型和算法，以及相应的计算结果。 如果你们认为，多光束干涉也会出现在碳化硅晶圆片的测试结果（附件1 和附件2）中， 从而影响到碳化硅外延层厚度计算的精度，请设法消除其影响，并给出消除影响后的计算结 果。",
    "tasks": [
      "请推导产生多光束干涉的必要条件，以及多光束干涉对外延层厚度计算精度可能产 生的影响",
      "请根据多光束干涉的必要条件，分析附件3 和附件4 提供的硅晶圆片的测试结果是否 出现多光束干涉，给出确定硅外延层厚度计算的数学模型和算法，以及相应的计算结果",
      "如果你们认为，多光束干涉也会出现在碳化硅晶圆片的测试结果（附件1 和附件2）中， 从而影响到碳化硅外延层厚度计算的精度，请设法消除其影响，并给出消除影响后的计算结 果"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "通用"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "通用"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/B题.pdf",
      "name": "B题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 277238,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 187625,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 186957,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件3.xlsx",
      "name": "附件3.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 189278,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/B题/附件/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 189423,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2025" / "B" / "q03" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2025" / "B" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2025" / "B" / "q03"


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
