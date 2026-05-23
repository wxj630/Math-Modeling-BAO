# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2016-A",
  "question_index": 3,
  "title": "2016年 CUMCM A题：系泊系统的设计",
  "problem_path": "cumcm/problems/2016/A.md",
  "question": {
    "label": "问题3",
    "statement": "由于潮汐等因素的影响，布放海域的实测水深介于16m~20m之间。布放点的海水速度最大可达到1.5m/s、风速最大可达到36m/s。请给出考虑风力、水流力和水深情况下的系泊系统设计，分析不同情况下钢桶、钢管的倾斜角度、锚链形状、浮标的吃水深度和游动区域。 说明 近海风荷载可通过近似公式F=0.625×Sv2(N) QUOTE \\* MERGEFORMAT 计算，其中S为物体在风向法平面的投影面积(m2)，v为风速(m/s）。近海水流力可通过近似公式F=374×Sv2(N)计算，其中S为物体在水流速度法平面的投影面积(m2)，v为水流速度(m/s）。 附表 锚链型号和参数表 型号 长度(mm) 单位长度的质量(kg/m) I 78 3.2 II 105 7 III 120 12.5 IV 150 19.5 V 180 28.12 表注：长度是指每节链环的长度。",
    "tasks": [
      "请给出考虑风力、水流力和水深情况下的系泊系统设计，分析不同情况下钢桶、钢管的倾斜角度、锚链形状、浮标的吃水深度和游动区域",
      "说明 近海风荷载可通过近似公式F=0.625×Sv2(N) QUOTE \\* MERGEFORMAT 计算，其中S为物体在风向法平面的投影面积(m2)，v为风速(m/s）",
      "近海水流力可通过近似公式F=374×Sv2(N)计算，其中S为物体在水流速度法平面的投影面积(m2)，v为水流速度(m/s）"
    ],
    "models": [
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "角度",
          "形状"
        ]
      },
      {
        "key": "ode_dynamics",
        "name": "微分方程与动力系统",
        "chapter": "CH2",
        "keywords": [
          "系统"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "设计"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016C-Chinese.rar",
      "name": "CUMCM-2016C-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 125596,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM-2016D-Chinese.rar",
      "name": "CUMCM-2016D-Chinese.rar",
      "suffix": ".rar",
      "kind": "media_or_archive",
      "size_bytes": 474125,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-A-Chinese-version.doc",
      "name": "CUMCM2016-problem-A-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 75264,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    },
    {
      "path": "../../Documents/Playground/cumcm_reextract/2016/2016_UxYMjfW4fd0a5cd7a21951b49232088d2af3f4e8/CUMCM2016-problem-B-Chinese-version.doc",
      "name": "CUMCM2016-problem-B-Chinese-version.doc",
      "suffix": ".doc",
      "kind": "document",
      "size_bytes": 40448,
      "source_root": "../../Documents/Playground/cumcm_reextract"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2016" / "A" / "q03" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2016" / "A" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2016" / "A" / "q03"


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
