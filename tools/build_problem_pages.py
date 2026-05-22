from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GITHUB_BLOB = "https://github.com/wxj630/Math-Modeling-World/blob/main/"


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


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
        f"> 这是一个赛题整体入口。先看整题主线，再进入 {total} 个小问的 baseline、advanced 和 outstanding 预留位。",
        "",
        "## 整题主线",
        "",
    ]

    if problem.get("core"):
        lines.extend([cell(problem["core"]), ""])
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
            "## 小问递进链",
            "",
        ]
    )

    for idx, qrow in enumerate(questions, start=1):
        qid = qkey(qrow.get("question") or qrow.get("question_index"))
        base = baselines.get(qid, {})
        label = question_label(qrow)
        statement = qrow.get("statement", "")
        method = base.get("method", "")
        source = qrow.get("source_type", "")
        artifact = qrow.get("artifact_path") or base.get("artifact_dir")

        lines.extend(
            [
                f"### {qid} {label}",
                "",
                f"**递进作用：** {role_for(idx, total, label)}",
                "",
                f"**题意摘要：** {clip(statement, 220) or '见报告正文。'}",
                "",
                f"- Baseline：{cell(method) or 'baseline'}；{repo_link(track, 'report.md', base.get('report_path'))}；{repo_link(track, 'solution.py', base.get('solution_path'))}",
                f"- Advanced：{cell(source) or 'advanced'}；{repo_link(track, 'report.md', qrow.get('report_path'))}；{repo_link(track, 'solution.py', qrow.get('solution_path'))}；{repo_link(track, 'result.json', qrow.get('result_path'))}",
                f"- 实验产物：{repo_link(track, 'artifact', artifact)}",
                "- Outstanding：预留，用来补强鲁棒性、误差分析、论文图表和整题叙事。",
                "",
            ]
        )

    lines.extend(
        [
            "## 复现提示",
            "",
            "本页不复制代码和实验结果；代码、结果和报告仍保存在仓库原目录。需要运行时，回到 [运行与复现](/reference/reproduce) 查看命令。",
            "",
        ]
    )
    return "\n".join(lines)


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


def build_track(track: str, title: str, problem_csv: str, question_csv: str, baseline_csv: str) -> tuple[int, int]:
    problems = read_csv(problem_csv)
    questions = read_csv(question_csv)
    baselines = read_csv(baseline_csv)
    qgroups = group_by_problem(questions)
    bgroups = group_baselines(baselines)

    track_dir = DOCS / track
    problem_dir = track_dir / "problems"
    problem_dir.mkdir(parents=True, exist_ok=True)
    for old in problem_dir.glob("*.md"):
        old.unlink()

    for problem in problems:
        pid = problem["problem_id"]
        page = build_problem_page(track, problem, qgroups.get(pid, []), bgroups.get(pid, {}))
        (problem_dir / f"{pid}.md").write_text(page + "\n", encoding="utf-8")

    index = build_index_page(track, title, problems, qgroups, bgroups)
    (track_dir / "problem-index.md").write_text(index + "\n", encoding="utf-8")
    return len(problems), sum(len(rows) for rows in qgroups.values())


def main() -> None:
    mcm_count, mcm_questions = build_track(
        "mcm-track",
        "MCM/ICM 赛题整体索引",
        "mcm/problem_index.csv",
        "mcm/question_solution_index.csv",
        "mcm/generic_baselines/generic_baseline_index.csv",
    )
    cumcm_count, cumcm_questions = build_track(
        "cumcm-track",
        "CUMCM 赛题整体索引",
        "cumcm/problem_index.csv",
        "cumcm/question_solution_index.csv",
        "cumcm/generic_baselines/generic_baseline_index.csv",
    )
    print(f"MCM/ICM: {mcm_count} problems, {mcm_questions} questions")
    print(f"CUMCM: {cumcm_count} problems, {cumcm_questions} questions")


if __name__ == "__main__":
    main()
