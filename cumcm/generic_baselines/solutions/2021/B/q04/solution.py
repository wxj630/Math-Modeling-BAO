# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2021-B",
  "question_index": 4,
  "title": "2021年 CUMCM B题：乙醇偶合制备 C4 烯烃",
  "problem_path": "cumcm/problems/2021/B.md",
  "question": {
    "label": "问题 4",
    "statement": "如果允许再增加 5 次实验，应如何设计，并给出详细理由。 附录：名词解释与附件说明 温度：反应温度。 选择性：某一个产物在所有产物中的占比。 时间：催化剂在乙醇氛围下的反应时间，单位分钟（min）。 Co 负载量： Co 与 SiO2 的重量之比。例如，“Co 负载量为 1wt%”表示 Co 与 SiO2 的重量之比为 1:100，记作“1wt%Co/SiO2”，依次类推。 HAP：一种催化剂载体，中文名称羟基磷灰石。 Co /SiO2 和 HAP 装料比：指 Co/SiO2 和 HAP 的质量比。 例如附件 1 中编号为 A14 的 催化剂组合 “33mg 1wt%Co/SiO2-67mg HAP -乙 醇浓度 1.68ml/min” 指 Co/SiO2 和 HAP 质量比为 33mg：67mg 且乙醇按每分钟 1.68 毫升加入，依次类推。 乙醇转化率：单位时间内乙醇的单程转化率，其值为 100 %  (乙醇进气量-乙 醇剩余量)/乙醇进气量。 C4 烯烃收率：其值为乙醇转化率  C4 烯烃的选择性。 附件 1：性能数据表。表中乙烯、C4 烯烃、乙醛、碳数为 4-12 脂肪醇等均为 反应的生成物；编号 A1~A14 的催化剂实验中使用装料方式 I，B1～B7 的催化剂实 验中使用装料方式 II。 附件 2：350 度时给定的某种催化剂组合的测试数据。",
    "tasks": [
      "如果允许再增加 5 次实验，应如何设计，并给出详细理由"
    ],
    "models": [
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "温度"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/CUMCM2021-B.pdf",
      "name": "CUMCM2021-B.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 170032,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件1.xlsx",
      "name": "附件1.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 20897,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2021_HtbJEt9Nb655e46bebfa2a66ec63f940e2da156b/B/附件2.xlsx",
      "name": "附件2.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11200,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2021" / "B" / "q04" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2021" / "B" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2021" / "B" / "q04"


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
