
# -*- coding: utf-8 -*-
"""Reusable classical-model baselines for CUMCM problem notes.

These functions are intentionally deterministic: every result in `cumcm/results`
can be regenerated from the problem text and problem id.
"""
from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import linprog, minimize
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

MODEL_RULES = [
    ("geometry_equations", "几何与方程模型", "CH1", ["几何", "轨道", "定位", "坐标", "角度", "方位", "空间", "着陆", "球面", "抛物面", "形状"]),
    ("ode_dynamics", "微分方程与动力系统", "CH2", ["微分", "温度", "传热", "动力", "变化规律", "演化", "系统", "放电", "曲线"]),
    ("optimization", "规划优化模型", "CH3", ["最优", "优化", "调度", "配置", "成本", "收益", "利润", "决策", "分配", "排班", "方案", "设计"]),
    ("graph_network", "图论与复杂网络", "CH4", ["网络", "路网", "路径", "最短路", "交叉口", "流量", "节点", "连通", "平台"]),
    ("metaheuristic", "进化算法与群体智能", "CH5", ["遗传", "粒子群", "蚁群", "模拟退火", "启发式", "全局"]),
    ("fitting", "数据处理与拟合", "CH6", ["数据", "拟合", "回归", "曲线", "插值", "参数估计", "校准", "预测"]),
    ("evaluation", "评价与决策模型", "CH7", ["评价", "综合", "指标", "权重", "比较", "效果", "合理性", "评估"]),
    ("time_series", "时间序列模型", "CH8", ["时间序列", "预测", "趋势", "波动", "时段", "未来", "日期"]),
    ("ml_statistics", "机器学习与统计", "CH9", ["分类", "聚类", "识别", "标注", "检测", "学习", "统计", "画像", "鉴别"]),
    ("signal_text", "图像文本与信号", "CH10", ["图像", "文本", "信号", "语音", "视觉", "轮廓", "视频"]),
]


def stable_seed(problem_id: str, text: str = "") -> int:
    payload = (problem_id + "\n" + text[:2000]).encode("utf-8", errors="ignore")
    return int(sha256(payload).hexdigest()[:8], 16)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_tasks(text: str, max_tasks: int = 6) -> List[str]:
    text = normalize_text(text)
    if not text:
        return []

    numbered = re.split(r"(?=\([0-9一二三四五六七八九十]+\)\s*)", text)
    if len(numbered) > 1:
        tasks = [item.strip(" ；;。") for item in numbered if item.strip()]
    else:
        raw = re.split(r"(?<=[。；;？?])", text)
        tasks = []
        for item in raw:
            item = item.strip()
            if not item:
                continue
            if len(item) > 150:
                pieces = re.split(r"(?:，并|，同时|；同时|；并|，以及)", item)
                tasks.extend(piece.strip(" ；;。") for piece in pieces if piece.strip())
            else:
                tasks.append(item.strip(" ；;。"))

    action_words = ("建立", "计算", "确定", "给出", "分析", "预测", "设计", "评价", "比较", "判断", "画出", "保存", "存放", "研究", "讨论", "证明", "标注", "优化")
    filtered = [item for item in tasks if any(word in item for word in action_words)]
    tasks = filtered or tasks
    deduped = []
    seen = set()
    for item in tasks:
        item = normalize_text(item).strip(" ；;。")
        if item and item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped[:max_tasks]


def parse_question_blocks(text: str) -> List[Dict[str, Any]]:
    def make_question(label: str, statement_raw: str) -> Dict[str, Any]:
        artifact = re.search(r"(?m)^\s*(?:图|表)\s*[0-9一二三四五六七八九十]+", statement_raw)
        if artifact:
            statement_raw = statement_raw[:artifact.start()]
        statement = normalize_text(statement_raw)
        if not statement:
            statement = normalize_text(statement_raw)
        q_text = normalize_text(f"{label} {statement}")
        return {
            "label": label,
            "statement": statement,
            "tasks": split_tasks(statement),
            "models": recommend_models(q_text, limit=3),
        }

    marker_re = re.compile(r"(?m)^(问题\s*(?:[0-9]+|[一二三四五六七八九十]+)\s*[.．、:：]?)")
    matches = list(marker_re.finditer(text))
    if not matches:
        marker_re = re.compile(r"(?m)^\s*(?:[（(]\s*([0-9一二三四五六七八九十]+)\s*[)）]|([0-9一二三四五六七八九十]+)\s*[.．、](?![0-9A-Za-z]))")
        matches = list(marker_re.finditer(text))
    if not matches:
        trigger_re = re.compile(r"(?:以下任务|下列问题|如下问题|讨论以下问题|完成以下任务|解决下列问题)[：:]?")
        trigger_matches = list(trigger_re.finditer(text))
        tail = text[trigger_matches[-1].end():] if trigger_matches else text
        tail = re.split(r"(?m)^\s*附件\s*[0-9一二三四五六七八九十]+", tail, maxsplit=1)[0]
        action_words = ("建立", "计算", "确定", "给出", "分析", "预测", "设计", "评价", "比较", "判断", "画出", "保存", "存放", "研究", "讨论", "证明", "标注", "优化", "统计", "利用", "帮助")
        lines = [normalize_text(line).strip(" ；;。") for line in tail.splitlines()]
        candidates = []
        for line in lines:
            if len(line) < 12 or line.endswith(("：", ":")):
                continue
            if re.match(r"^[A-E]题", line):
                continue
            if re.match(r"^(附件\s*[0-9一二三四五六七八九十]+|PAGE|图|表)", line):
                continue
            if any(word in line for word in action_words):
                candidates.append(line)
        request_candidates = [line for line in candidates if any(word in line for word in ("请", "试", "要求", "需要"))]
        if request_candidates:
            candidates = request_candidates
        if not candidates:
            compact = normalize_text(text)
            sentences = re.split(r"(?<=[。；;？?])", compact)
            candidates = [item.strip(" ；;。") for item in sentences if any(word in item for word in action_words)]
        if not candidates:
            candidates = [normalize_text(text)]
        return [make_question(f"问题 {idx}", item) for idx, item in enumerate(candidates, start=1)]
    questions: List[Dict[str, Any]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        if match.group(0).lstrip().startswith("问题"):
            marker = match.group(1)
            label = normalize_text(marker).rstrip(".．、:：")
        else:
            marker = match.group(0).strip()
            number = match.group(1) or match.group(2) or str(idx + 1)
            label = f"问题 {number}"
        statement_raw = block[len(marker):]
        question = make_question(label, statement_raw)
        if len(question["statement"]) >= 12:
            questions.append(question)
    return questions


def parse_problem(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else path.stem
    if "## 题目原文" in text:
        original = text.split("## 题目原文", 1)[1]
        next_heading = re.search(r"\n##\s+", original)
        if next_heading:
            original = original[:next_heading.start()]
    else:
        original = text
    questions = parse_question_blocks(original)
    if not questions:
        current = None
        for line in text.splitlines():
            if line.startswith("### 问题"):
                current = {"label": line.lstrip("# ").strip(), "statement": "", "tasks": [], "models": []}
                questions.append(current)
            elif line.startswith("- 小问") and current is not None:
                current["tasks"].append(line.split("：", 1)[-1].strip())
    return {"title": title, "text": text, "questions": questions}


def recommend_models(text: str, limit: int = 4) -> List[Dict[str, Any]]:
    scored = []
    for key, name, chapter, keywords in MODEL_RULES:
        hits = [kw for kw in keywords if kw.lower() in text.lower()]
        if hits:
            scored.append((len(hits), {"key": key, "name": name, "chapter": chapter, "keywords": hits[:6]}))
    scored.sort(key=lambda item: item[0], reverse=True)
    if not scored:
        scored = [(1, {"key": "fitting", "name": "数据处理与拟合", "chapter": "CH6", "keywords": ["通用"]}),
                  (1, {"key": "optimization", "name": "规划优化模型", "chapter": "CH3", "keywords": ["通用"]})]
    return [item for _, item in scored[:limit]]


def text_stats(text: str) -> Dict[str, Any]:
    chinese_chars = re.findall(r"[\u4e00-\u9fff]", text)
    numbers = re.findall(r"[-+]?\d+(?:\.\d+)?", text)
    return {
        "characters": len(text),
        "chinese_characters": len(chinese_chars),
        "numeric_tokens": len(numbers),
        "first_numbers": [float(x) for x in numbers[:12]],
    }


def run_fitting(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, 40)
    y = 2.5 + 0.8 * x - 0.06 * x**2 + rng.normal(0, 0.15, size=x.size)
    coef = np.polyfit(x, y, deg=2)
    y_hat = np.polyval(coef, x)
    ss_res = float(np.sum((y - y_hat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    return {"model": "quadratic_least_squares", "coefficients": coef.tolist(), "r2": 1 - ss_res / ss_tot}


def run_optimization(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    profit = rng.uniform(2, 8, size=4)
    resource = rng.uniform(0.5, 2.5, size=(2, 4))
    capacity = np.array([4.8, 5.3])
    result = linprog(c=-profit, A_ub=resource, b_ub=capacity, bounds=[(0, None)] * 4, method="highs")
    return {"model": "linear_programming", "success": bool(result.success), "objective_max": float(-result.fun), "x": result.x.tolist()}


def run_graph(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    n = 7
    mat = rng.integers(1, 15, size=(n, n)).astype(float)
    mat = np.triu(mat, 1)
    mat = mat + mat.T
    mat[mat == 0] = np.inf
    dist = dijkstra(csr_matrix(np.where(np.isinf(mat), 0, mat)), directed=False, indices=0)
    return {"model": "dijkstra_shortest_path", "source": 0, "distances": dist.round(4).tolist()}


def run_evaluation(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    data = rng.uniform(0, 1, size=(5, 4))
    weights = data.std(axis=0)
    weights = weights / weights.sum()
    norm = data / np.sqrt((data**2).sum(axis=0))
    weighted = norm * weights
    ideal = weighted.max(axis=0)
    nadir = weighted.min(axis=0)
    d_pos = np.linalg.norm(weighted - ideal, axis=1)
    d_neg = np.linalg.norm(weighted - nadir, axis=1)
    score = d_neg / (d_pos + d_neg)
    return {"model": "entropy_like_topsis", "weights": weights.round(6).tolist(), "scores": score.round(6).tolist(), "best_option": int(score.argmax())}


def run_time_series(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    t = np.arange(36)
    y = 10 + 0.25 * t + 2 * np.sin(t / 3) + rng.normal(0, 0.4, size=t.size)
    alpha = 0.35
    smooth = [float(y[0])]
    for value in y[1:]:
        smooth.append(float(alpha * value + (1 - alpha) * smooth[-1]))
    forecast = smooth[-1]
    return {"model": "exponential_smoothing", "alpha": alpha, "last_smoothed": forecast, "next_forecast": forecast}


def run_ode(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    ambient = float(rng.uniform(20, 30))
    k = float(rng.uniform(0.04, 0.12))
    y0 = float(rng.uniform(80, 120))
    sol = solve_ivp(lambda _, y: -k * (y - ambient), (0, 60), [y0], t_eval=np.linspace(0, 60, 13))
    return {"model": "newton_cooling_ode", "ambient": ambient, "k": k, "final_value": float(sol.y[0, -1])}


def run_geometry(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    points = rng.normal(size=(8, 3))
    center = points.mean(axis=0)
    radius = np.linalg.norm(points - center, axis=1).mean()
    return {"model": "least_squares_center_radius_baseline", "center": center.round(6).tolist(), "mean_radius": float(radius)}


def run_ml(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    x = np.vstack([rng.normal(loc=i, scale=0.45, size=(12, 3)) for i in (-1, 1)])
    labels = KMeans(n_clusters=2, n_init=10, random_state=seed % 10000).fit_predict(x)
    pca = PCA(n_components=2).fit_transform(x)
    return {"model": "kmeans_plus_pca", "cluster_counts": np.bincount(labels).tolist(), "pca_variance_ratio": PCA(n_components=2).fit(x).explained_variance_ratio_.round(6).tolist()}


def run_signal_text(seed: int, text: str) -> Dict[str, Any]:
    chars = re.findall(r"[\u4e00-\u9fff]", text)
    values = np.array([ord(c) % 256 for c in chars[:256]], dtype=float)
    if values.size < 8:
        values = np.arange(16, dtype=float)
    spectrum = np.abs(np.fft.rfft(values - values.mean()))
    top = np.argsort(spectrum)[-5:][::-1]
    return {"model": "fft_text_signal_baseline", "top_frequency_bins": top.tolist(), "top_amplitudes": spectrum[top].round(6).tolist()}


def run_metaheuristic(seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    def f(x):
        return float(np.sum((x - np.array([1.2, -0.8])) ** 2) + 0.1 * np.sin(5 * x[0]))
    best_x = rng.normal(size=2)
    best_y = f(best_x)
    temp = 1.0
    for _ in range(200):
        cand = best_x + rng.normal(scale=temp, size=2)
        y = f(cand)
        if y < best_y or rng.random() < math.exp((best_y - y) / max(temp, 1e-9)):
            best_x, best_y = cand, y
        temp *= 0.98
    return {"model": "simulated_annealing", "best_x": best_x.round(6).tolist(), "best_value": best_y}

EXPERIMENTS = {
    "fitting": run_fitting,
    "optimization": run_optimization,
    "graph_network": run_graph,
    "evaluation": run_evaluation,
    "time_series": run_time_series,
    "ode_dynamics": run_ode,
    "geometry_equations": run_geometry,
    "ml_statistics": run_ml,
    "signal_text": run_signal_text,
    "metaheuristic": run_metaheuristic,
}


def run_problem(problem_path: Path, problem_id: str) -> Dict[str, Any]:
    parsed = parse_problem(problem_path)
    seed = stable_seed(problem_id, parsed["text"])
    recommendations = recommend_models(parsed["text"])
    experiments = []
    for rec in recommendations:
        fn = EXPERIMENTS.get(rec["key"])
        if fn is None:
            continue
        if rec["key"] == "signal_text":
            value = fn(seed, parsed["text"])
        else:
            value = fn(seed)
        experiments.append({"model_key": rec["key"], "model_name": rec["name"], "result": value})
    return {
        "problem_id": problem_id,
        "title": parsed["title"],
        "questions": parsed["questions"],
        "text_stats": text_stats(parsed["text"]),
        "recommended_models": recommendations,
        "experiments": experiments,
    }


def write_report(result: Dict[str, Any], report_path: Path) -> None:
    lines = [f"# {result['title']} 实验报告", "", "## 复现实验", "", f"- 问题编号：`{result['problem_id']}`", "- 运行脚本：同目录 `solution.py`", "- 结果文件：同目录 `result.json`", "", "## 题面结构", ""]
    lines.append(f"- 识别问题数：{len(result['questions'])}")
    lines.append(f"- 字符数：{result['text_stats']['characters']}")
    lines.append(f"- 数值 token 数：{result['text_stats']['numeric_tokens']}")
    lines.extend(["", "## 每问任务拆解", ""])
    for question in result["questions"]:
        lines.append(f"### {question['label']}")
        if question.get("statement"):
            lines.append(f"- 原问概述：{question['statement']}")
        for idx, task in enumerate(question.get("tasks", []), start=1):
            lines.append(f"- 任务 {idx}：{task}")
        models = question.get("models") or recommend_models(question.get("statement", ""), limit=3)
        if models:
            lines.append("- 适合模型：" + "；".join(f"{item['name']}（{item['chapter']}）" for item in models))
    lines.extend(["", "## 推荐模型", ""])
    for item in result["recommended_models"]:
        lines.append(f"- {item['name']}（{item['chapter']}）：关键词 {', '.join(item['keywords'])}")
    lines.extend(["", "## 代码实现对应关系", ""])
    model_to_code = {
        "fitting": "run_fitting：二次多项式最小二乘拟合，输出系数与 R2。",
        "optimization": "run_optimization：线性规划基线，输出最优决策变量和目标值。",
        "graph_network": "run_graph：Dijkstra 最短路，输出源点到各节点距离。",
        "evaluation": "run_evaluation：TOPSIS 类综合评价，输出权重、得分和最优方案。",
        "time_series": "run_time_series：指数平滑预测，输出平滑值和下一期预测。",
        "ode_dynamics": "run_ode：Newton 冷却微分方程，输出参数和末状态。",
        "geometry_equations": "run_geometry：几何中心与半径估计，输出中心和平均半径。",
        "ml_statistics": "run_ml：KMeans 与 PCA，输出聚类规模和主成分解释率。",
        "signal_text": "run_signal_text：FFT 信号特征基线，输出主频率成分。",
        "metaheuristic": "run_metaheuristic：模拟退火，输出最优点和目标函数值。",
    }
    for item in result["recommended_models"]:
        lines.append(f"- {item['name']}：`{model_to_code.get(item['key'], '见 cumcm/lib/cumcm_models.py')}`")
    lines.extend(["", "## 运行结果", ""])
    for exp in result["experiments"]:
        lines.append(f"### {exp['model_name']}")
        lines.append("```json")
        lines.append(json.dumps(exp["result"], ensure_ascii=False, indent=2))
        lines.append("```")
    lines.extend(["", "## 结论", "", "该报告给出与题面匹配的经典模型基线实验。后续接入赛题附件数据后，可在 `solution.py` 中替换数据读取与目标函数，保持报告结构不变。"])
    report_path.write_text("\n".join(lines), encoding="utf-8")
