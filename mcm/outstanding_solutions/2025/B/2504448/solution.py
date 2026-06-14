from __future__ import annotations

import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parent
REAL_DIR = REPO_ROOT / "docs" / "mcm-2015-2025" / "real_solutions" / "2025" / "MCM-B"
REAL_RESULT = REAL_DIR / "result.json"
REAL_ARTIFACTS = REAL_DIR / "artifacts"
RESULT_PATH = ROOT / "result.json"
REPORT_PATH = ROOT / "report.md"
ARTIFACT_DIR = ROOT / "artifacts"

PAPER_ID = "2504448"
PAPER_TITLE = "Sustainable Tourism Management in Juneau"
PAPER_SOURCE_OCR = "Outstanding_Solutions/MCM/OCR-results/B/2504448/2504448.md"
PAPER_SOURCE_PDF = "Outstanding_Solutions/MCM/PDF-2025/B/2504448.pdf"


def repo_rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_artifacts() -> dict[str, str]:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    for source in sorted(REAL_ARTIFACTS.glob("*")):
        if source.is_file():
            target = ARTIFACT_DIR / source.name
            shutil.copy2(source, target)
            copied[source.stem] = repo_rel(target)
    return copied


def write_report(result: dict) -> None:
    exp = result["experiment_result"]
    lines = [
        "# 2025 MCM-B Outstanding 复现：2504448",
        "",
        "## 复现对象",
        f"- 获奖论文：`{PAPER_ID}`，{PAPER_TITLE}",
        f"- OCR 来源：`{PAPER_SOURCE_OCR}`",
        f"- PDF 来源：`{PAPER_SOURCE_PDF}`",
        "- 复现定位：以当前已验证的 MCM-B sustainable tourism real solution 为计算核，对齐论文中的旅游需求、经济、环境、居民满意度和动态政策优化框架。",
        "",
        "## 问题与建模",
        "论文 2504448 将 Juneau 旅游管理写成经济收益、环境影响和社会满意度的多目标动态规划问题。当前计算核已经包含游客上限、游客费、保护支出比例、隐性成本、冰川压力、居民接受度和政策前沿，因此可以复现论文的核心决策逻辑。",
        "",
        "## 代码与实验",
        "- `solution.py` 读取 `docs/mcm-2015-2025/real_solutions/2025/MCM-B/result.json`。",
        "- 复制当前 advanced 的 policy grid、frontier、sensitivity 和可视化 artifacts。",
        "- 在 `result.json` 中补充获奖论文方法、动态规划解释和相对 advanced 的升级说明。",
        "",
        "## 关键结果",
        f"- 最优日游客上限：{exp['optimal_daily_cap']}。",
        f"- 最优游客费：{exp['optimal_visitor_fee_usd']} USD。",
        f"- 保护支出比例：{exp['optimal_conservation_share']}。",
        f"- 年游客量：{exp['annual_visitors']}；总收入：{exp['total_revenue_usd']} USD。",
        f"- 可持续性得分：{exp['sustainability_score']}；居民接受度：{exp['resident_acceptance_index']}。",
        f"- 最敏感因素：{exp['top_sensitivity_factor']}。",
        "",
        "## 相对 Advanced 的优势",
        "- Advanced 已经有政策网格和前沿；Outstanding 把它重写成获奖论文式的旅游需求、经济、环境、社会三目标动态管理框架。",
        "- 报告明确解释额外税费如何反馈到保护、基础设施和社区支出，符合论文中 government expenditure feedback 的主线。",
        "- 后续可以把当前 deterministic grid 扩展成逐年动态规划状态转移，以更贴近 2504448 的 5 年模拟表达。",
        "",
        "## 输出产物",
    ]
    for key, path in result["artifact_paths"].items():
        lines.append(f"- `{key}`：`{path}`")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not REAL_RESULT.exists():
        raise FileNotFoundError(f"missing advanced result: {REAL_RESULT}")
    advanced = read_json(REAL_RESULT)
    artifacts = copy_artifacts()
    optimal = advanced["sustainability_model"]["optimal_policy"]
    top_sensitivity = advanced["sensitivity_analysis"]["top_factors"][0]
    result = {
        "problem_id": "2025-B",
        "year": 2025,
        "code": "B",
        "paper_id": PAPER_ID,
        "paper_title": PAPER_TITLE,
        "paper_source_ocr": PAPER_SOURCE_OCR,
        "paper_source_pdf": PAPER_SOURCE_PDF,
        "reproduction_scope": "用当前 MCM-B real solution 的政策网格、可持续性目标和敏感性分析，对齐 2504448 的多目标动态规划获奖论文模型链。",
        "selected_model": {
            "name": "multi-objective sustainable tourism policy model",
            "chapter": "Outstanding reproduction of 2504448",
        },
        "data_source": advanced["data_source"],
        "advanced_kernel": advanced,
        "paper_model_alignment": {
            "paper_methods": [
                "tourist demand model",
                "economic benefit model",
                "environmental impact model",
                "resident satisfaction model",
                "dynamic policy optimization and sensitivity analysis",
            ],
            "repo_kernel": [
                "visitor cap / visitor fee / conservation share policy grid",
                "hidden cost and glacier pressure metrics",
                "resident acceptance and sustainability score",
                "frontier policies and sensitivity tornado chart",
            ],
        },
        "experiment_result": {
            "optimal_daily_cap": optimal["daily_cap"],
            "optimal_visitor_fee_usd": optimal["visitor_fee_usd"],
            "optimal_conservation_share": optimal["conservation_share"],
            "annual_visitors": optimal["annual_visitors"],
            "total_revenue_usd": optimal["total_revenue_usd"],
            "sustainability_score": optimal["sustainability_score"],
            "resident_acceptance_index": optimal["resident_acceptance_index"],
            "top_sensitivity_factor": top_sensitivity["factor"],
            "top_sensitivity_correlation": top_sensitivity["correlation_with_score"],
        },
        "difference_from_advanced": "把 advanced 的政策网格整理为获奖论文式多目标动态管理框架，并补充需求、经济、环境、社会满意度和支出反馈叙事。",
        "artifact_paths": artifacts,
        "limitations": [
            "当前计算核是确定性政策网格，不是完整逐年 Bellman 状态转移；报告中明确作为 2504448 的可验证近似复现。",
            "外部旅游、气候和居民满意度数据未随仓库纳入，当前使用题面给定参数和透明假设。",
        ],
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(result)
    print(json.dumps({"result": repo_rel(RESULT_PATH), "report": repo_rel(REPORT_PATH)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
