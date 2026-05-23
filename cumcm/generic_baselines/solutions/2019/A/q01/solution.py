# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2019-A",
  "question_index": 1,
  "title": "2019年 CUMCM A题：高压油管的压力控制",
  "problem_path": "cumcm/problems/2019/A.md",
  "question": {
    "label": "问题1",
    "statement": "某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms。喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示。高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa。如果要将高压油管内的压力尽可能稳定在100 MPa左右，如何设置单向阀每次开启的时长？如果要将高压油管内的压力从100 MPa增加到150 MPa，且分别经过约2 s、5 s和10 s的调整过程后稳定在150 MPa，单向阀开启的时长应如何调整？",
    "tasks": [
      "某型号高压油管的内腔长度为500mm，内直径为10mm，供油入口A处小孔的直径为1.4mm，通过单向阀开关控制供油时间的长短，单向阀每打开一次后就要关闭10ms",
      "喷油器每秒工作10次，每次工作时喷油时间为2.4ms，喷油器工作时从喷油嘴B处向外喷油的速率如图2所示",
      "高压油泵在入口A处提供的压力恒为160 MPa，高压油管内的初始压力为100 MPa",
      "如果要将高压油管内的压力尽可能稳定在100 MPa左右，如何设置单向阀每次开启的时长？",
      "如果要将高压油管内的压力从100 MPa增加到150 MPa，且分别经过约2 s、5 s和10 s的调整过程后稳定在150 MPa，单向阀开启的时长应如何调整？"
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
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/CUMCM-2019-Problem-A-Chinese.docx",
      "name": "CUMCM-2019-Problem-A-Chinese.docx",
      "suffix": ".docx",
      "kind": "document",
      "size_bytes": 72736,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/CUMCM-2019-Problem-A-Chinese.pdf",
      "name": "CUMCM-2019-Problem-A-Chinese.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 558858,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件1-凸轮边缘曲线.xlsx",
      "name": "附件1-凸轮边缘曲线.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 23145,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件2-针阀运动曲线.xlsx",
      "name": "附件2-针阀运动曲线.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 12607,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2019_TSIsGxZuf258d48a22a7c7e628cd90482e1c25a2/A-2019中文/附件3-弹性模量与压力.xlsx",
      "name": "附件3-弹性模量与压力.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 17165,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2019" / "A" / "q01" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2019" / "A" / "q01" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2019" / "A" / "q01"


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
