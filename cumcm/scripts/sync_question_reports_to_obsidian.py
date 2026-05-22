# -*- coding: utf-8 -*-
"""Append per-question code/result/report links to the CUMCM Obsidian notes."""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path("/Users/wuxiaojun/code/Math-Modeling-World")
CUMCM = REPO / "cumcm"
VAULT = Path("/Users/wuxiaojun/Documents/Obsidian Vault/数学建模/CUMCM")
START = "<!-- CUMCM_QUESTION_SOLUTIONS_START -->"
END = "<!-- CUMCM_QUESTION_SOLUTIONS_END -->"


def replace_block(text: str, block: str) -> str:
    if START in text and END in text:
        before = text.split(START, 1)[0].rstrip()
        after = text.split(END, 1)[1].lstrip()
        return before + "\n\n" + block + "\n\n" + after
    return text.rstrip() + "\n\n" + block + "\n"


def load_result(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main() -> None:
    rows = json.loads((CUMCM / "question_solution_index.json").read_text(encoding="utf-8"))
    generic_index_path = CUMCM / "generic_baselines" / "generic_baseline_index.json"
    generic_rows = json.loads(generic_index_path.read_text(encoding="utf-8")) if generic_index_path.exists() else []
    generic_by_question = {
        (row["year"], row["code"], int(row["question_index"])): row
        for row in generic_rows
    }
    grouped: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        grouped.setdefault((row["year"], row["code"]), []).append(row)

    touched = 0
    for (year, code), items in sorted(grouped.items()):
        note = VAULT / year / f"{code}题.md"
        if not note.exists():
            continue
        lines = [START, "", "## 逐问代码、结果与实验报告", ""]
        lines.append("下面链接来自 `Math-Modeling-World/cumcm`，每一问均可用仓库 `.venv` 单独运行并复现实验结果。")
        if generic_rows:
            lines.append("通用解法集中保存在 `/Users/wuxiaojun/code/Math-Modeling-World/cumcm/generic_baselines`，这里仅链接对应基线，避免把过程稿和专用解法混在一起。")
        lines.append("")
        for item in sorted(items, key=lambda x: int(x["question_index"])):
            q = int(item["question_index"])
            solution = REPO / item["solution_path"]
            result = REPO / item["result_path"]
            report = REPO / item["report_path"]
            artifact = REPO / item.get("artifact_path", f"cumcm/question_artifacts/{year}/{code}/q{q:02d}/experiment_table.csv")
            result_data = load_result(result)
            data_source = result_data.get("data_source", {})
            selected_model = result_data.get("selected_model", {})
            experiment = result_data.get("experiment_result", {})
            lines.append(f"### 第 {q:02d} 条：{item['question_label']}")
            lines.append(f"- 原问摘录：{item['statement'][:220]}{'…' if len(item['statement']) > 220 else ''}")
            if selected_model:
                lines.append(f"- 适配模型：{selected_model.get('name', '')}（{selected_model.get('chapter', '')}）")
            if data_source:
                source_type = data_source.get("source_type", "unknown")
                source_label = {"attachment": "官方附件数值", "problem_statement": "题目原文参数/表格", "synthetic": "确定性实验数据"}.get(source_type, source_type)
                lines.append(f"- 数据来源：{source_label}；规模 {data_source.get('rows', 0)} 行 x {data_source.get('columns', 0)} 列")
                if data_source.get("path"):
                    lines.append(f"- 数据路径：{data_source['path']}")
            if experiment:
                lines.append(f"- 求解方法：`{experiment.get('method', 'model_experiment')}`")
                if experiment.get("method") == "credit_attachment_data_dictionary_audit":
                    lines.append("- 说明：该条是题面附件术语/字段说明的解析保留项，不是官方新增竞赛小问；正式建模集中在本题前三问。")
            lines.append(f"- Python 代码：[{solution.name}]({solution})")
            lines.append(f"- 运行结果：[{result.name}]({result})")
            lines.append(f"- 实验报告：[{report.name}]({report})")
            lines.append(f"- 实验表：[{artifact.name}]({artifact})")
            generic = generic_by_question.get((year, code, q))
            if generic:
                generic_solution = REPO / generic["solution_path"]
                generic_result = REPO / generic["result_path"]
                generic_report = REPO / generic["report_path"]
                lines.append(f"- 通用基线：`{generic.get('method', 'generic_model')}`；[代码]({generic_solution}) / [结果]({generic_result}) / [报告]({generic_report})")
            lines.append(f"- 官方附件数：{item.get('attachment_count', 0)}")
            lines.append("")
        lines.append(END)
        original = note.read_text(encoding="utf-8", errors="ignore")
        note.write_text(replace_block(original, "\n".join(lines)), encoding="utf-8")
        touched += 1
    print(f"updated {touched} Obsidian CUMCM notes")


if __name__ == "__main__":
    main()
