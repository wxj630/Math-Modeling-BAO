# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2023-D",
  "question_index": 3,
  "title": "2023年 CUMCM D题：圈养湖羊的空间利用率",
  "problem_path": "/Users/wuxiaojun/code/Math-Modeling-World/cumcm/problems/2023/D.md",
  "question": {
    "label": "问题 3",
    "statement": "问题 1 和问题 2 中用到的数据都没有考虑不确定性，一旦决定了什么时间开始对 多少可配种的基础母羊进行配种，后续对羊栏的安排和需求也就随之确定。例如，用 3 个羊栏 给 42 只母羊进行配种，孕期需要 6 个羊栏，哺乳期需要 7 个羊栏给怀孕母羊分娩和哺乳， 哺乳 期结束就需要给 84 只断奶羔羊和 42 只母羊共安排 9 个羊栏进行育肥和休整。但实际情况并非 如此，配种成功率、分娩羔羊的数目和死亡率等都有不确定性，哺乳时间也可以调控，这些都 会影响空间需求。 现根据经验作以下考虑： (1) 母羊通过自然交配受孕率为 85%，交配期结束后 30 天可识别出是否成功受孕； (2) 在自然交配的 20 天中受孕母羊的受孕时间并不确知，而孕期会在 147-150 天内波动， 这些因素将影响到预产期范围； (3) 怀孕母羊分娩时一般每胎产羔 2 只，少部分每胎产羔 1 只或 3 只及以上，目前尚没有 实用手段控制或提前得知产羔数。羔羊出生时，有夭折的可能，多羔死亡率高于正常。通常可 以按平均每胎产羔 2.2 只、羔羊平均死亡率 3%估算。 (4) 母羊哺乳期过短不利于羔羊后期的生长，通常是羔羊体重达到一定标准后断奶；而哺乳 期过长，母羊的身体消耗就越大，早点断奶，有利于早恢复、早发情配种。一种经验做法是将 哺乳期控制在 35-45 天内，以 40 天为基准，哺乳期每减少1 天，羔羊的育肥期增加2 天；哺乳 期每增加 1 天， 羔羊的育肥期减少2 天。除此之外， 母羊的空怀休整期可在不少于18 天的前提 下灵活调控。 此外，如有必要，允许分娩日期相差不超过 7 天的哺乳期母羊及所产羔羊同栏，允许断奶 日期相差不超过 7 天的育肥期羔羊同栏，允许断奶日期相差不超过 7 天的休整期母羊同栏。为 简化问题，不考虑母羊流产、死亡以及羔羊在哺乳期或育肥期夭折和个体发育快慢等情况。 在以上不确定性的考虑下，生产计划的制定与问题 1 和问题 2 将有较大的不同：一旦作出 了“什么时间开始对多少可配种的基础母羊进行配种”的决定，后续羊栏的需求和安排不再是 随之确定的， 而是每一步都会出现若干种可能的情况需要作相应的并遵从基本规则的安排处理， 但无法改变或调整上一步。因此，某种意义上，本问题要讨论研究的生产计划将是一个应对多 种可能情况的“预案集”。 请综合考虑可行性和年化出栏羊只数量，制定具体的生产计划，使得整体方案的期望损失 最小。其中整体方案的损失由羊栏使用情况决定，当羊栏空置时， 每栏每天的损失为1； 当羊栏 数量不够时，所缺的羊栏每栏每天的损失（即租用费）为 3。",
    "tasks": [
      "问题 1 和问题 2 中用到的数据都没有考虑不确定性，一旦决定了什么时间开始对 多少可配种的基础母羊进行配种，后续对羊栏的安排和需求也就随之确定。例如，用 3 个羊栏 给 42 只母羊进行配种，孕期需要 6 个羊栏，哺乳期需要 7 个羊栏给怀孕母羊分娩和哺乳， 哺乳 期结束就需要给 84 只断奶羔羊和 42 只母羊共安排 9 个羊栏进行育肥和休整。但实际情况并非 如此，配种成功率、分娩羔羊的数目和死亡率等都有不确定性，哺乳时间也可以调控，这些都 会影响空间需求。 现根据经验作以下考虑：",
      "(4) 母羊哺乳期过短不利于羔羊后期的生长，通常是羔羊体重达到一定标准后断奶；而哺乳 期过长，母羊的身体消耗就越大，早点断奶，有利于早恢复、早发情配种。一种经验做法是将 哺乳期控制在 35-45 天内，以 40 天为基准，哺乳期每减少1 天，羔羊的育肥期增加2 天；哺乳 期每增加 1 天， 羔羊的育肥期减少2 天。除此之外， 母羊的空怀休整期可在不少于18 天的前提 下灵活调控。 此外，如有必要，允许分娩日期相差不超过 7 天的哺乳期母羊及所产羔羊同栏，允许断奶 日期相差不超过 7 天的育肥期羔羊同栏，允许断奶日期相差不超过 7 天的休整期母羊同栏。为 简化问题，不考虑母羊流产、死亡以及羔羊在哺乳期或育肥期夭折和个体发育快慢等情况。 在以上不确定性的考虑下，生产计划的制定与问题 1 和问题 2 将有较大的不同：一旦作出 了“什么时间开始对多少可配种的基础母羊进行配种”的决定，后续羊栏的需求和安排不再是 随之确定的， 而是每一步都会出现若干种可能的情况需要作相应的并遵从基本规则的安排处理， 但无法改变或调整上一步。因此，某种意义上，本问题要讨论研究的生产计划将是一个应对多 种可能情况的“预案集”。 请综合考虑可行性和年化出栏羊只数量，制定具体的生产计划，使得整体方案的期望损失 最小。其中整体方案的损失由羊栏使用情况决定，当羊栏空置时， 每栏每天的损失为1； 当羊栏 数量不够时，所缺的羊栏每栏每天的损失（即租用费）为 3"
    ],
    "models": [
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "波动",
          "日期"
        ]
      },
      {
        "key": "geometry_equations",
        "name": "几何与方程模型",
        "chapter": "CH1",
        "keywords": [
          "空间"
        ]
      },
      {
        "key": "optimization",
        "name": "规划优化模型",
        "chapter": "CH3",
        "keywords": [
          "方案"
        ]
      }
    ]
  },
  "attachments": []
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2023" / "D" / "q03" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2023" / "D" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2023" / "D" / "q03"


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
