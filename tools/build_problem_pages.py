from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GITHUB_BLOB = "https://github.com/wxj630/Math-Modeling-World/blob/main/"


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def read_optional_csv(path: str) -> list[dict[str, str]]:
    file_path = ROOT / path
    if not file_path.exists():
        return []
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def read_json(track: str, path: str | None) -> dict:
    local_path = repo_path(track, path)
    if not local_path:
        return {}
    file_path = ROOT / local_path
    if not file_path.exists():
        return {}
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def cell(value: str | None) -> str:
    text = (value or "").replace("\n", " ").replace("\r", " ").strip()
    return text.replace("|", "\\|")


def clip(value: str | None, limit: int = 130) -> str:
    text = cell(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def repo_path(track: str, path: str | None) -> str | None:
    if not path:
        return None
    if path.startswith(("mcm/", "cumcm/", "docs/", ".github/", "tools/")):
        return path
    if track == "mcm-track":
        return f"mcm/{path}"
    if track == "cumcm-track":
        return f"cumcm/{path}"
    return path


def repo_link(track: str, label: str, path: str | None) -> str:
    path = repo_path(track, path)
    if not path:
        return "—"
    return f"[{label}]({GITHUB_BLOB}{quote(path, safe='/._-')})"


def qkey(value: str | None) -> str:
    value = (value or "").strip()
    if not value:
        return "q00"
    if value.startswith("q"):
        return value
    return f"q{int(value):02d}"


def qsort_key(row: dict[str, str]) -> int:
    raw = row.get("question") or row.get("question_index") or "0"
    return int(raw.replace("q", "") or "0")


def question_label(row: dict[str, str]) -> str:
    return row.get("title") or row.get("question_label") or row.get("question") or row.get("question_index") or "问题"


def readable_sentence(text: str) -> str:
    text = cell(text)
    if text and text[-1] not in "。.!?！？…":
        return text + "…"
    return text


def scalar(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.6g}"
    if isinstance(value, (int, bool)):
        return str(value)
    return clip(str(value), 70)


def summarize_list(values: list, limit: int = 2) -> str:
    if not values:
        return "0项"
    if all(isinstance(item, (int, float, str, bool)) for item in values[:limit]):
        return "、".join(scalar(item) for item in values[:limit]) + ("…" if len(values) > limit else "")
    if isinstance(values[0], dict):
        sample = summarize_mapping(values[0], limit=3)
        return f"{len(values)}项，例：{sample}"
    return f"{len(values)}项"


def summarize_mapping(mapping: dict, limit: int = 5) -> str:
    parts: list[str] = []
    skip_keys = {
        "statement",
        "tasks",
        "columns",
        "candidate_models",
        "sample_plan_rows",
        "component_rows",
        "outline",
        "extracted_numeric_tokens",
    }
    for key, value in mapping.items():
        if key in skip_keys:
            continue
        if isinstance(value, (str, int, float, bool)):
            parts.append(f"{key}={scalar(value)}")
        elif isinstance(value, list):
            parts.append(f"{key}={summarize_list(value)}")
        elif isinstance(value, dict):
            scalar_items = {
                sub_key: sub_value
                for sub_key, sub_value in value.items()
                if isinstance(sub_value, (str, int, float, bool))
            }
            if scalar_items:
                parts.append(f"{key}: {summarize_mapping(scalar_items, limit=3)}")
            else:
                parts.append(f"{key}={len(value)}项")
        if len(parts) >= limit:
            break
    return cell("；".join(parts) or "见 result.json")


def data_source_summary(result: dict, fallback: str = "") -> str:
    data = result.get("data_source") if isinstance(result.get("data_source"), dict) else {}
    if not data:
        return cell(fallback or "见报告正文")
    source_type = data.get("type") or data.get("source_type") or "数据源"
    details: list[str] = [str(source_type)]
    for key in ("rows", "columns", "match_count", "attachment_count"):
        value = data.get(key)
        if value is None:
            continue
        if isinstance(value, dict):
            details.append(f"{key}: {summarize_mapping(value, limit=2)}")
        elif isinstance(value, list):
            details.append(f"{key}: {len(value)}项")
        else:
            details.append(f"{key}: {scalar(value)}")
    root = data.get("root") or data.get("path") or data.get("indexed_result_path")
    if root:
        details.append(f"路径: {clip(str(root), 58)}")
    return cell("；".join(details))


def model_summary(result: dict, row: dict[str, str], baseline: dict[str, str] | None = None) -> str:
    selected = result.get("selected_model") if isinstance(result.get("selected_model"), dict) else {}
    if selected:
        name = selected.get("name") or selected.get("method") or selected.get("key")
        chapter = selected.get("chapter")
        if name and chapter:
            return cell(f"{name}（{chapter}）")
        if name:
            return cell(str(name))
    if row.get("methods"):
        return cell(row["methods"])
    if baseline and baseline.get("method"):
        return cell(baseline["method"])
    return "见报告正文"


def result_summary(result: dict) -> str:
    if isinstance(result.get("monte_carlo_summary_top_total"), list):
        top_rows = result.get("monte_carlo_summary_top_total") or []
        top = top_rows[0] if top_rows and isinstance(top_rows[0], dict) else {}
        parts = []
        if top:
            parts.append(
                f"2028 Top1 {top.get('NOC')} expected_total={scalar(top.get('expected_total'))}, "
                f"expected_gold={scalar(top.get('expected_gold'))}"
            )
        if result.get("expected_first_medal_countries") is not None:
            parts.append(f"首枚奖牌国家期望={scalar(result.get('expected_first_medal_countries'))}")
        evaluation = result.get("model_evaluation") if isinstance(result.get("model_evaluation"), dict) else {}
        if evaluation:
            parts.append(
                f"2024 holdout accuracy={scalar(evaluation.get('mean_accuracy_2024'))}, "
                f"F1={scalar(evaluation.get('mean_f1_2024'))}"
            )
        poisson = result.get("poisson_event_elasticity") if isinstance(result.get("poisson_event_elasticity"), list) else []
        if poisson and isinstance(poisson[0], dict):
            parts.append(f"Poisson {poisson[0].get('case')} beta={scalar(poisson[0].get('beta_num_events'))}")
        return cell("；".join(parts) or "见 result.json")

    ordered_keys = [
        "experiment_result",
        "flow_summary",
        "serve_baseline",
        "workforce_network",
        "model_features",
        "formulation",
    ]
    for key in ordered_keys:
        value = result.get(key)
        if isinstance(value, dict):
            return summarize_mapping(value)
    excluded = {
        "problem_id",
        "year",
        "code",
        "question",
        "question_index",
        "question_title",
        "title",
        "statement",
        "methods",
        "data_source",
        "selected_model",
        "candidate_models",
        "tasks",
        "artifact_paths",
        "limitations",
        "baseline_note",
    }
    fallback = {key: value for key, value in result.items() if key not in excluded}
    return summarize_mapping(fallback) if fallback else "见 result.json"


def build_baseline_global_report(
    track: str,
    questions: list[dict[str, str]],
    baselines: dict[str, dict[str, str]],
) -> list[str]:
    method_counts = Counter(base.get("method", "baseline") for base in baselines.values())
    method_text = "；".join(f"{method}×{count}" for method, count in sorted(method_counts.items())) or "baseline"
    lines = [
        "## Baseline 全局报告",
        "",
        f"Baseline 层把整题拆成 {len(questions)} 个最低可运行脚手架，覆盖的通用模型族为：{cell(method_text)}。它的价值不是给出最终答案，而是快速回答三个问题：题面有哪些可用数字，应该从哪个经典模型族切入，代码、结果和报告是否能跑通。",
        "",
    ]
    for qrow in questions:
        qid = qkey(qrow.get("question") or qrow.get("question_index"))
        base = baselines.get(qid, {})
        method = base.get("method", "baseline")
        result = read_json(track, base.get("result_path"))
        code_links = (
            f"{repo_link(track, 'solution.py', base.get('solution_path'))} / "
            f"{repo_link(track, 'report.md', base.get('report_path'))} / "
            f"{repo_link(track, 'result.json', base.get('result_path'))}"
        )
        lines.extend(
            [
                f"**{qid} {cell(question_label(qrow))}**",
                "",
                f"- 问题：{clip(qrow.get('statement', ''), 180) or '见报告正文。'}",
                f"- 建模：从 `{cell(method)}` 建立通用变量、约束和可运行脚手架。",
                f"- 代码入口：{code_links}",
                f"- 实验结果：{result_summary(result)}",
                f"- 分析：baseline 适合作为建模起点和覆盖检查；它还没有充分吸收题目专用数据、业务约束和论文表达要求。",
                "",
            ]
        )
    lines.extend(
        [
            "**Baseline 读法。** 先看它选择的模型族和 baseline score/实验表，再回到题面判断它漏掉了哪些真实约束。凡是只停留在通用评分、关键词匹配或线性脚手架的地方，就是 advanced 需要升级的地方。",
            "",
        ]
    )
    return lines


def build_advanced_global_report(
    track: str,
    questions: list[dict[str, str]],
    baselines: dict[str, dict[str, str]],
) -> list[str]:
    source_counts: Counter[str] = Counter()
    for qrow in questions:
        result = read_json(track, qrow.get("result_path"))
        data = result.get("data_source") if isinstance(result.get("data_source"), dict) else {}
        source = data.get("type") or data.get("source_type") or qrow.get("source_type") or "见报告正文"
        source_counts[str(source)] += 1
    source_text = "；".join(f"{source}×{count}" for source, count in sorted(source_counts.items()))
    lines = [
        "## Advanced 全局报告",
        "",
        f"Advanced 层使用当前仓库已有的题目专用代码和实验结果，把小问串成一条整题模型链。数据来源覆盖：{cell(source_text or '见各问报告')}。阅读时重点看每问如何继承前问变量、约束、附件字段或情景设定。",
        "",
    ]
    for qrow in questions:
        qid = qkey(qrow.get("question") or qrow.get("question_index"))
        result = read_json(track, qrow.get("result_path"))
        code_links = (
            f"{repo_link(track, 'solution.py', qrow.get('solution_path'))} / "
            f"{repo_link(track, 'report.md', qrow.get('report_path'))} / "
            f"{repo_link(track, 'result.json', qrow.get('result_path'))}"
        )
        artifact = qrow.get("artifact_path") or baselines.get(qid, {}).get("artifact_dir")
        lines.extend(
            [
                f"**{qid} {cell(question_label(qrow))}**",
                "",
                f"- 问题：{clip(qrow.get('statement', ''), 180) or '见报告正文。'}",
                f"- 建模：{cell(qrow.get('methods') or model_summary(result, qrow))}",
                f"- 代码入口：{code_links}",
                f"- 数据：{data_source_summary(result, qrow.get('source_type', ''))}",
                f"- 实验结果：{result_summary(result)}",
                f"- 产物：{repo_link(track, 'artifact', artifact)}",
                f"- 分析：advanced 已把当前小问落到可复现实验，读者可以直接沿 result.json、report.md 和 artifact 把结论改写成论文段落。",
                "",
            ]
        )
    lines.extend(
        [
            "**Advanced 读法。** 先读模型升级列，确认它把题面数据、附件字段、情景假设或输出模板写进了变量和约束；再读实验结果列，确认 result.json 与 artifact 中已经留下可复现的表、图或决策结果。",
            "",
        ]
    )
    return lines


def build_advantage_report(
    track: str,
    questions: list[dict[str, str]],
    baselines: dict[str, dict[str, str]],
) -> list[str]:
    lines = [
        "## Advanced 相对 Baseline 的优势",
        "",
    ]
    for qrow in questions:
        qid = qkey(qrow.get("question") or qrow.get("question_index"))
        base = baselines.get(qid, {})
        base_result = read_json(track, base.get("result_path"))
        adv_result = read_json(track, qrow.get("result_path"))
        base_method = base.get("method", "baseline")
        adv_model = model_summary(adv_result, qrow)
        modeling = (
            f"Baseline 从 `{base_method}` 的通用变量和评分出发；Advanced 升级为 {adv_model}，并把题面/附件里的真实数据、约束和输出格式纳入模型。"
        )
        result = (
            f"Baseline 主要给出 {result_summary(base_result)}；Advanced 进一步给出 {result_summary(adv_result)}，可直接支撑论文中的表格、图或策略解释。"
        )
        lines.extend(
            [
                f"**{qid} {cell(question_label(qrow))}**",
                "",
                f"- 建模优势：{cell(modeling)}",
                f"- 结果优势：{cell(result)}",
                "",
            ]
        )
    lines.extend(["", ""])
    return lines


def build_outstanding_global_report(
    track: str,
    problem: dict[str, str],
    outstanding: dict[str, str],
) -> list[str]:
    result = read_json(track, outstanding.get("result_path"))
    paper_id = cell(outstanding.get("paper_id") or "outstanding")
    paper_title = cell(outstanding.get("paper_title") or "获奖论文复现")
    methods = cell(outstanding.get("methods") or model_summary(result, outstanding))
    source = cell(
        outstanding.get("source_path")
        or result.get("paper_source_ocr")
        or result.get("paper_source_pdf")
        or "见本地获奖论文 OCR/PDF"
    )
    code_links = (
        f"{repo_link(track, 'solution.py', outstanding.get('solution_path'))} / "
        f"{repo_link(track, 'report.md', outstanding.get('report_path'))} / "
        f"{repo_link(track, 'result.json', outstanding.get('result_path'))}"
    )
    artifact = outstanding.get("artifact_dir")
    scope = cell(result.get("reproduction_scope") or outstanding.get("scope") or "复现获奖论文的可验证模型链和主要实验产物")
    advantage = cell(
        result.get("difference_from_advanced")
        or outstanding.get("difference_from_advanced")
        or "在 advanced 的整题预测基础上，进一步对齐获奖论文的特征工程、仿真、不确定性和论文叙事。"
    )
    lines = [
        "## Outstanding 全局报告",
        "",
        f"本层复现 `{paper_id}`：{paper_title}。它是 `{problem['problem_id']}` 的第一篇获奖论文复现样例，用来示范如何从 baseline/advanced 继续走到可验证的获奖论文级模型链。",
        "",
        f"- 论文来源：{source}",
        f"- 复现范围：{scope}",
        f"- 核心方法：{methods}",
        f"- 代码入口：{code_links}",
        f"- 实验产物：{repo_link(track, 'artifact', artifact)}",
        f"- 关键结果：{result_summary(result)}",
        f"- 相对 advanced 的优势：{advantage}",
        "",
    ]
    return lines


def role_for(index: int, total: int, label: str) -> str:
    label_lower = label.lower()
    if total == 1:
        return "整题唯一任务，需要把建模、求解、解释和结果产出放在同一条链路里看。"
    if index == 1:
        return "建立整题主模型或数据入口，后续小问通常都继承这里的变量、指标或数据清洗结果。"
    if index == total:
        if any(key in label_lower for key in ["报告", "memo", "summary", "摘要", "建议", "explanation"]):
            return "把前面模型、实验和限制收束成论文或备忘录，是整题表达质量的出口。"
        return "整合前面结论并处理最后的验证、迁移或决策要求。"
    if any(key in label for key in ["敏感", "情景", "不确定", "风险", "检验", "测试", "what-if"]):
        return "在前面模型基础上做情景、敏感性或可靠性检查。"
    if any(key in label for key in ["预算", "成本", "收益", "利润", "费用"]):
        return "把前面模型转成成本、收益或资源配置结果，连接业务决策。"
    if any(key in label for key in ["预测", "未来", "动态", "演化", "流失"]):
        return "把静态模型推进到时间演化或预测，形成递进分析。"
    return "在前问基础上加入新的约束、数据或评价口径，推进整题模型链。"


def build_problem_page(
    track: str,
    problem: dict[str, str],
    questions: list[dict[str, str]],
    baselines: dict[str, dict[str, str]],
    outstanding: dict[str, str] | None = None,
) -> str:
    pid = problem["problem_id"]
    title = problem["title"]
    total = len(questions)
    model_text = problem.get("recommended_models") or "；".join(
        sorted({row.get("method", "") for row in baselines.values() if row.get("method")})
    )
    source_text = "；".join(sorted({row.get("source_type", "") for row in questions if row.get("source_type")}))

    lines: list[str] = [
        f"# {pid} {title}",
        "",
        f"> 这是一个赛题整体入口。先看整题主线，再进入 {total} 个小问的 baseline、advanced"
        + (" 和 outstanding 获奖论文复现。" if outstanding else " 和 outstanding 预留位。"),
        "",
        "## 整题主线",
        "",
    ]

    if problem.get("core"):
        lines.extend([readable_sentence(problem["core"]), ""])
    else:
        first = question_label(questions[0]) if questions else "第一问"
        last = question_label(questions[-1]) if questions else "最后一问"
        lines.extend(
            [
                f"本题共 {total} 个小问。阅读时不要把小问拆成孤岛：`{first}` 通常给出主模型或数据入口，后续小问逐步加入动态、情景、评价、决策或论文表达要求，最后由 `{last}` 收束成整题结论。",
                "",
            ]
        )

    lines.extend(
        [
            "## 赛题材料",
            "",
            "| 项目 | 内容 |",
            "|---|---|",
            f"| 赛题 | `{pid}` |",
            f"| 小问数 | {total} |",
            f"| 推荐模型族 | {cell(model_text) or '见各小问方法'} |",
            f"| 数据来源 | {cell(source_text) or '见各小问报告'} |",
            "",
        ]
    )

    lines.extend(build_baseline_global_report(track, questions, baselines))
    lines.extend(build_advanced_global_report(track, questions, baselines))
    lines.extend(build_advantage_report(track, questions, baselines))
    if outstanding:
        lines.extend(build_outstanding_global_report(track, problem, outstanding))
    lines.extend(["## 小问递进链", ""])

    for idx, qrow in enumerate(questions, start=1):
        qid = qkey(qrow.get("question") or qrow.get("question_index"))
        base = baselines.get(qid, {})
        base_result = read_json(track, base.get("result_path"))
        advanced_result = read_json(track, qrow.get("result_path"))
        label = question_label(qrow)
        statement = qrow.get("statement", "")
        method = base.get("method", "")
        source = qrow.get("source_type", "")
        advanced_label = cell(source) or model_summary(advanced_result, qrow)
        artifact = qrow.get("artifact_path") or base.get("artifact_dir")

        if outstanding:
            outstanding_line = (
                f"- Outstanding：复现 {cell(outstanding.get('paper_id')) or '获奖论文'} 的整题模型链；"
                f"核心方法：{cell(outstanding.get('methods')) or '见 outstanding 全局报告'}；"
                f"代码入口：{repo_link(track, 'solution.py', outstanding.get('solution_path'))} / "
                f"{repo_link(track, 'report.md', outstanding.get('report_path'))} / "
                f"{repo_link(track, 'result.json', outstanding.get('result_path'))}"
            )
        else:
            outstanding_line = "- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。"

        lines.extend(
            [
                f"### {qid} {label}",
                "",
                f"**递进作用：** {role_for(idx, total, label)}",
                "",
                f"**题意摘要：** {clip(statement, 220) or '见报告正文。'}",
                "",
                f"- Baseline：从 `{cell(method) or 'baseline'}` 的通用脚手架开始；代码入口：{repo_link(track, 'solution.py', base.get('solution_path'))} / {repo_link(track, 'report.md', base.get('report_path'))} / {repo_link(track, 'result.json', base.get('result_path'))}；实验结果：{result_summary(base_result)}",
                f"- Advanced：{advanced_label}；代码入口：{repo_link(track, 'solution.py', qrow.get('solution_path'))} / {repo_link(track, 'report.md', qrow.get('report_path'))} / {repo_link(track, 'result.json', qrow.get('result_path'))}；实验结果：{result_summary(advanced_result)}",
                f"- 实验产物：{repo_link(track, 'artifact', artifact)}",
                outstanding_line,
                "",
            ]
        )

    lines.extend(
        [
            "## 复现提示",
            "",
            "本页只抽取代码、结果和报告中的关键摘要；完整代码、result.json、report.md 和 artifact 仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_index_page(
    track: str,
    title: str,
    problems: list[dict[str, str]],
    qgroups: dict[str, list[dict[str, str]]],
    bgroups: dict[str, dict[str, dict[str, str]]],
) -> str:
    lines = [
        f"# {title}",
        "",
        "这个索引以完整赛题为入口。进入某个赛题页后，再沿着小问递进链查看 baseline、advanced、实验结果和 outstanding 预留位。",
        "",
    ]

    by_year: dict[str, list[dict[str, str]]] = defaultdict(list)
    for problem in problems:
        by_year[problem["year"]].append(problem)

    for year in sorted(by_year):
        lines.extend([f"## {year}", "", "| 赛题 | 题名 | 小问 | 第一问入口 | 模型/主题 |", "|---|---|---:|---|---|"])
        for problem in sorted(by_year[year], key=lambda row: row["problem_id"]):
            pid = problem["problem_id"]
            questions = sorted(qgroups.get(pid, []), key=qsort_key)
            first = question_label(questions[0]) if questions else ""
            model = problem.get("recommended_models") or "；".join(
                sorted({row.get("method", "") for row in bgroups.get(pid, {}).values() if row.get("method")})
            )
            lines.append(
                f"| [{pid}](./problems/{pid}.md) | {cell(problem['title'])} | {len(questions)} | {cell(first)} | {clip(model, 95)} |"
            )
        lines.append("")
    return "\n".join(lines)


def group_by_problem(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["problem_id"]].append(row)
    for pid in grouped:
        grouped[pid].sort(key=qsort_key)
    return grouped


def group_baselines(rows: list[dict[str, str]]) -> dict[str, dict[str, dict[str, str]]]:
    grouped: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        grouped[row["problem_id"]][qkey(row.get("question") or row.get("question_index"))] = row
    return grouped


def group_outstanding(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    grouped: dict[str, dict[str, str]] = {}
    for row in rows:
        if row.get("problem_id"):
            grouped[row["problem_id"]] = row
    return grouped


def build_track(
    track: str,
    title: str,
    problem_csv: str,
    question_csv: str,
    baseline_csv: str,
    outstanding_csv: str | None = None,
) -> tuple[int, int]:
    problems = read_csv(problem_csv)
    questions = read_csv(question_csv)
    baselines = read_csv(baseline_csv)
    outstanding = group_outstanding(read_optional_csv(outstanding_csv)) if outstanding_csv else {}
    qgroups = group_by_problem(questions)
    bgroups = group_baselines(baselines)

    track_dir = DOCS / track
    problem_dir = track_dir / "problems"
    problem_dir.mkdir(parents=True, exist_ok=True)
    for old in problem_dir.glob("*.md"):
        old.unlink()

    for problem in problems:
        pid = problem["problem_id"]
        page = build_problem_page(track, problem, qgroups.get(pid, []), bgroups.get(pid, {}), outstanding.get(pid))
        (problem_dir / f"{pid}.md").write_text(page.rstrip() + "\n", encoding="utf-8")

    index = build_index_page(track, title, problems, qgroups, bgroups)
    (track_dir / "problem-index.md").write_text(index.rstrip() + "\n", encoding="utf-8")
    return len(problems), sum(len(rows) for rows in qgroups.values())


def main() -> None:
    mcm_count, mcm_questions = build_track(
        "mcm-track",
        "MCM/ICM 赛题整体索引",
        "mcm/problem_index.csv",
        "mcm/question_solution_index.csv",
        "mcm/generic_baselines/generic_baseline_index.csv",
        "mcm/outstanding_solutions/outstanding_solution_index.csv",
    )
    cumcm_count, cumcm_questions = build_track(
        "cumcm-track",
        "CUMCM 赛题整体索引",
        "cumcm/problem_index.csv",
        "cumcm/question_solution_index.csv",
        "cumcm/generic_baselines/generic_baseline_index.csv",
        "cumcm/outstanding_solutions/outstanding_solution_index.csv",
    )
    print(f"MCM/ICM: {mcm_count} problems, {mcm_questions} questions")
    print(f"CUMCM: {cumcm_count} problems, {cumcm_questions} questions")


if __name__ == "__main__":
    main()
