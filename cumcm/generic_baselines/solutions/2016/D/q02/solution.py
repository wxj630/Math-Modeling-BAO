# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2016-D",
  "question_index": 2,
  "title": "2016年 CUMCM D题：风电场运行状况分析及优化",
  "problem_path": "cumcm/problems/2016/D.md",
  "question": {
    "label": "问题 2",
    "statement": "附件2给出了该风电场几个典型风机所在处的风速信息，其中4#、16#、24#风机属于一期工程，33#、49#、57#风机属于二期工程，它们的主要参数见附件3。风机生产企业还提供了部分新型号风机，它们的主要参数见附件4。试从风能资源与风机匹配角度判断新型号风机是否比现有风机更为适合。",
    "tasks": [
      "附件2给出了该风电场几个典型风机所在处的风速信息，其中4#、16#、24#风机属于一期工程，33#、49#、57#风机属于二期工程，它们的主要参数见附件3",
      "试从风能资源与风机匹配角度判断新型号风机是否比现有风机更为适合"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201501.xls",
      "name": "201501.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 169984,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201502.xls",
      "name": "201502.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 201728,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201503.xls",
      "name": "201503.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 220672,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201504.xls",
      "name": "201504.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 163840,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201505.xls",
      "name": "201505.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 221696,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201506.xls",
      "name": "201506.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 215552,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201507.xls",
      "name": "201507.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 169984,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201508.xls",
      "name": "201508.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 169984,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201509.xls",
      "name": "201509.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 215552,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201510.xls",
      "name": "201510.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 220672,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201511.xls",
      "name": "201511.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 165376,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件1  平均风速和风电场日实际输出功率表/201512.xls",
      "name": "201512.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 169472,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/01.xls",
      "name": "01.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 82944,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/02.xls",
      "name": "02.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 69632,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/03.xls",
      "name": "03.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 74240,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/04.xls",
      "name": "04.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 73216,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/05.xls",
      "name": "05.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 126976,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/06.xls",
      "name": "06.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 72704,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/07.xls",
      "name": "07.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 75264,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/08.xls",
      "name": "08.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 76288,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/09.xls",
      "name": "09.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 126976,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/10.xls",
      "name": "10.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 79872,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/11.xls",
      "name": "11.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 126464,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件2  风电场典型风机报表/12.xls",
      "name": "12.xls",
      "suffix": ".xls",
      "kind": "data",
      "size_bytes": 79872,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件3  风电场风机型号及其参数.doc",
      "name": "附件3  风电场风机型号及其参数.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 69120,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-D-Appendix-Chinese/附件4  风机生产企业提供的新型号风机主要参数.doc",
      "name": "附件4  风机生产企业提供的新型号风机主要参数.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 33280,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese/CUMCM2016-problem-D-Chinese-version.doc",
      "name": "CUMCM2016-problem-D-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 39424,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2016" / "D" / "q02" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2016" / "D" / "q02" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2016" / "D" / "q02"


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
