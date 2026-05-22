from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
SOURCE_SOLUTION = REPO_ROOT / 'docs/mcm-2015-2025/real_solutions/2017/MCM-C/solution.py'
SOURCE_RESULT = REPO_ROOT / 'docs/mcm-2015-2025/real_solutions/2017/MCM-C/result.json'
SOURCE_ARTIFACTS = REPO_ROOT / 'docs/mcm-2015-2025/real_solutions/2017/MCM-C/artifacts'
ROOT = Path(__file__).resolve().parents[4]
RESULT_PATH = ROOT / "question_results" / '2017' / 'C' / 'q01' / "result.json"
REPORT_PATH = ROOT / "question_reports" / '2017' / 'C' / 'q01' / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / '2017' / 'C' / 'q01'
QUESTION = {
    "problem_id": "2017-C",
    "year": "2017",
    "code": "C",
    "question": "q01",
    "title": "Cooperate and Navigate",
    "question_title": "官方路网画像与交通流模型",
    "statement": "Build a model of traffic-flow effects using the number of lanes, peak and/or average traffic volume, and the percentage of self-driving cooperating vehicles on I-5, I-90, I-405, and SR-520.",
    "methods": "读取官方 2017_MCM_Problem_C_Data.xlsx 的 parsed mile posts 和 definitions 工作表，按 route/milepost/ADT/lanes 构造路段容量、峰小时流量、V/C ratio 和 BPR 速度函数。对应模型：交通流基本图、容量约束、BPR 延误函数、路网分段画像。",
    "result_keys": [
        "network_profile",
        "official_problem_parameters"
    ],
    "source_type": "official_comap_xlsx",
    "artifact_name": "clean_traffic_segments.csv"
}


def markdown_table(rows, columns):
    if not rows:
        return ["无可展示记录。"]
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in rows:
        values = []
        for column in columns:
            value = row.get(column, "")
            values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def filtered_result(full_result: dict) -> dict:
    selected = {
        "problem_id": QUESTION["problem_id"],
        "question": QUESTION["question"],
        "question_title": QUESTION["question_title"],
        "statement": QUESTION["statement"],
        "methods": QUESTION["methods"],
        "data_source": full_result["data_source"],
    }
    for key in QUESTION["result_keys"]:
        selected[key] = full_result.get(key)
    return selected


def source_outputs_current() -> bool:
    if not SOURCE_RESULT.exists() or not SOURCE_ARTIFACTS.exists():
        return False
    source_mtime = SOURCE_SOLUTION.stat().st_mtime
    if SOURCE_RESULT.stat().st_mtime < source_mtime:
        return False
    artifact_files = [path for path in SOURCE_ARTIFACTS.iterdir() if path.is_file()]
    if not artifact_files:
        return False
    return all(path.stat().st_mtime >= source_mtime for path in artifact_files)


def write_question_report(result: dict) -> None:
    if "rows" in result["data_source"]:
        data_rows = result["data_source"]["rows"]
    elif "parameters" in result["data_source"]:
        data_rows = {"official_parameters": len(result["data_source"]["parameters"])}
    elif "official_problem_parameters" in result["data_source"]:
        official_parameters = result["data_source"]["official_problem_parameters"]
        data_rows = {"official_problem_parameters": len(official_parameters)}
        if isinstance(official_parameters.get("periods"), list):
            data_rows["official_periods"] = len(official_parameters["periods"])
    else:
        data_rows = {
            key: result["data_source"].get(key)
            for key in ("records", "level_records", "flow_records", "match_count")
            if result["data_source"].get(key) is not None
        }
    if result["data_source"].get("type") == "official_statement_parameters":
        truth_line = "- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。"
    elif result["data_source"].get("type") == "official_pdf_and_world_bank_csv":
        truth_line = "- 本脚本只使用 COMAP 官方 PDF、题面推荐的 World Bank 官方公共数据和显式规划假设，不使用随机生成的 `x1/x2/x3` 占位数据。"
    elif result["data_source"].get("type") == "official_pdf_and_world_bank_api":
        truth_line = "- 本脚本只使用 COMAP 官方 PDF、World Bank WDI 官方 API/缓存和显式政策响应假设，不使用随机生成的 `x1/x2/x3` 占位数据。"
    else:
        truth_line = "- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。"
    lines = [
        f"# {QUESTION['problem_id']} {QUESTION['question']}：{QUESTION['question_title']}",
        "",
        "## 题目原问",
        QUESTION["statement"],
        "",
        "## 适合模型",
        QUESTION["methods"],
        "",
        "## 数据与真实性",
        f"- 数据类型：{result['data_source']['type']}。",
        f"- 官方数据目录：`{result['data_source']['root']}`。",
        f"- 行数/记录数：{data_rows}。",
        truth_line,
        "",
        "## 建模与求解报告",
    ]
    if "workforce_network" in result and QUESTION["problem_id"] == "2015-C":
        workforce = result["workforce_network"]
        current = workforce.get("current_staffing", {})
        units = workforce.get("organization_units", {})
        lines.extend([
            "",
            "### ICM 人力资本网络",
            f"- 组织单元：{units.get('seven_person_departments')} 个 7 人部门 + {units.get('four_person_offices')} 个 4 人办公室。",
            f"- 岗位核对：{units.get('positions_reconciled')} 个岗位。",
            f"- 当前填补岗位：{current.get('filled_positions_at_85pct')}；空缺：{current.get('vacancies_at_85pct')}。",
            "",
            "#### Level risk table",
            "",
        ])
        lines.extend(markdown_table(workforce.get("level_rows", []), ["level", "positions", "filled_positions", "baseline_attrition_rate", "knowledge_risk_score"]))
    if "attrition_dynamics" in result and QUESTION["problem_id"] == "2015-C":
        dynamics = result["attrition_dynamics"]
        lines.extend([
            "",
            "### 流失动态与生产率影响",
        ])
        lines.extend([f"- {item}" for item in dynamics.get("processes", [])])
        lines.extend(["", "#### Dynamic risk rows", ""])
        lines.extend(markdown_table(dynamics.get("risk_rows", []), ["level", "baseline_attrition_rate", "dynamic_attrition_risk", "expected_annual_leavers", "productivity_loss_sigma"]))
    if "budget_forecast" in result and QUESTION["problem_id"] == "2015-C":
        budget = result["budget_forecast"]
        lines.extend([
            "",
            "### 两年招聘与培训预算",
            f"- 方法：{budget.get('method')}",
            f"- 招聘成本：{budget.get('total_two_year_recruiting_sigma')} sigma。",
            f"- 培训成本：{budget.get('total_two_year_training_sigma')} sigma。",
            f"- 总预算：{budget.get('total_two_year_sigma')} sigma。",
            "",
        ])
        lines.extend(markdown_table(budget.get("rows", []), ["level", "two_year_total_hires", "two_year_recruiting_sigma", "two_year_training_sigma", "two_year_budget_sigma"]))
    if "turnover_scenarios" in result and QUESTION["problem_id"] == "2015-C":
        scenarios = result["turnover_scenarios"]
        lines.extend([
            "",
            "### 25%/35% 流失率情景",
            f"- 方法：{scenarios.get('method')}",
            "",
        ])
        lines.extend(markdown_table(scenarios.get("scenario_rows", []), ["annual_turnover_rate", "annual_leavers_at_full_positions", "estimated_hiring_capacity_per_year", "end_of_year_fill_rate", "sustains_80pct_fill"]))
        lines.extend(["", "#### 间接影响", ""])
        lines.extend([f"- {item}" for item in scenarios.get("indirect_effects_of_high_turnover", [])])
    if "middle_manager_shock" in result and QUESTION["problem_id"] == "2015-C":
        shock = result["middle_manager_shock"]
        health = shock.get("health_impact", {})
        lines.extend([
            "",
            "### 中层 30% 流失与内部晋升",
            f"- 情景：{shock.get('scenario')}",
            f"- 无外部招聘中层填补率：{health.get('no_external_middle_layer_fill_rate')}。",
            f"- 仅内部晋升中层填补率：{health.get('promotions_only_middle_layer_fill_rate')}。",
            f"- 解释：{health.get('interpretation')}",
            "",
        ])
        lines.extend(markdown_table(shock.get("rows", []), ["level", "baseline_filled", "after_30pct_middle_attrition_no_external", "after_internal_promotions_only"]))
    if "team_science_extension" in result and QUESTION["problem_id"] == "2015-C":
        extension = result["team_science_extension"]
        lines.extend([
            "",
            "### 团队科学与多层网络扩展",
        ])
        lines.extend([f"- {item}" for item in extension.get("team_science_summary", [])])
        lines.extend([
            f"- 推荐网络层：{', '.join(extension.get('recommended_next_layers', []))}。",
            f"- 典型模型：{', '.join(extension.get('models', []))}。",
        ])
    if "executive_report" in result and QUESTION["problem_id"] == "2015-C":
        lines.extend([
            "",
            "### Executive summary",
            str(result["executive_report"]),
        ])
    if "sustainability_index" in result and QUESTION["problem_id"] == "2015-D":
        index = result["sustainability_index"]
        lines.extend([
            "",
            "### 国家可持续性评价模型",
            f"- 定义：{index.get('definition')}",
            f"- 基线年份：{index.get('baseline_year')}。",
            f"- 基线得分：{index.get('baseline_score')}。",
            f"- 基线状态：{index.get('baseline_status')}。",
            f"- 阈值规则：{index.get('status_rule')}",
            "",
        ])
        lines.extend(markdown_table(index.get("components", []), ["component", "indicator_id", "latest_year", "latest_value", "weight", "score", "weighted_score", "trend_per_year_raw"]))
    if "development_plan" in result and QUESTION["problem_id"] == "2015-D":
        plan = result["development_plan"]
        lines.extend([
            "",
            "### 20 年可持续发展计划",
            f"- 选定国家：{plan.get('selected_country')}。",
            f"- 规划期：{plan.get('horizon_years')} 年。",
            f"- 策略：{plan.get('strategy')}",
            "",
        ])
        lines.extend(markdown_table(plan.get("programs", []), ["program", "annual_cost_billion_usd", "twenty_year_cost_billion_usd", "estimated_score_gain", "score_gain_per_billion_usd"]))
    if "plan_evaluation" in result and QUESTION["problem_id"] == "2015-D":
        evaluation = result["plan_evaluation"]
        lines.extend([
            "",
            "### 计划影响评估",
            f"- 20 年后得分：{evaluation.get('score_after_20_years')}。",
            f"- 得分增益：{evaluation.get('score_gain')}。",
            f"- 20 年后状态：{evaluation.get('status_after_20_years')}。",
            f"- 说明：{evaluation.get('evaluation_note')}",
            "",
        ])
        lines.extend(markdown_table(evaluation.get("component_projection", []), ["component", "score_after_20_years", "weighted_score_after"]))
    if "bang_for_buck" in result and QUESTION["problem_id"] == "2015-D":
        efficiency = result["bang_for_buck"]
        top = efficiency.get("top_program", {})
        lines.extend([
            "",
            "### 最高性价比政策",
            f"- 排序方法：{efficiency.get('ranking_method')}",
            f"- 最高性价比项目：{top.get('program')}。",
            f"- 单位预算得分增益：{top.get('score_gain_per_billion_usd')}。",
        ])
    if "thermal_strategy" in result and QUESTION["problem_id"] == "2016-A":
        strategy = result["thermal_strategy"]
        best = strategy.get("recommended_strategy", {})
        lines.extend([
            "",
            "### 温度空间-时间模型与推荐策略",
            f"- 目标：{strategy.get('objective')}",
            f"- 推荐流量：{best.get('flow_l_per_min')} L/min。",
            f"- 推荐动作：{best.get('motion')}。",
            f"- 平均温度误差：{best.get('mean_abs_error_c')} C。",
            f"- 平均空间温差：{best.get('mean_spatial_range_c')} C。",
            f"- 40 分钟溢流水量：{best.get('wasted_liters')} L。",
            "",
        ])
        lines.extend(markdown_table(strategy.get("strategy_rows", [])[:12], ["flow_l_per_min", "motion", "mean_abs_error_c", "mean_spatial_range_c", "final_mean_c", "wasted_liters", "comfort_score"]))
    if "shape_person_motion_sensitivity" in result and QUESTION["problem_id"] == "2016-A":
        sensitivity = result["shape_person_motion_sensitivity"]
        lines.extend([
            "",
            "### 形状、人体与动作敏感性",
            f"- 人体影响说明：{sensitivity.get('person_effect_note')}",
            "",
            "#### Tub shape rows",
            "",
        ])
        lines.extend(markdown_table(sensitivity.get("shape_rows", []), ["shape", "surface_area_m2", "water_depth_m", "mean_abs_error_c", "mean_spatial_range_c", "comfort_score"]))
        lines.extend(["", "#### Motion rows", ""])
        lines.extend(markdown_table(sensitivity.get("motion_rows", []), ["motion", "mean_abs_error_c", "mean_spatial_range_c", "comfort_score"]))
    if "bubble_bath_effect" in result and QUESTION["problem_id"] == "2016-A":
        bubble = result["bubble_bath_effect"]
        lines.extend([
            "",
            "### 泡泡浴影响",
            f"- 解释：{bubble.get('interpretation')}",
            "",
        ])
        lines.extend(markdown_table(bubble.get("rows", []), ["bubble_case", "surface_heat_loss_reduction_factor", "mean_abs_error_c", "mean_spatial_range_c", "final_mean_c", "comfort_score"]))
    if "user_explanation" in result and QUESTION["problem_id"] == "2016-A":
        lines.extend([
            "",
            "### 给浴缸用户的一页说明",
            str(result["user_explanation"]),
        ])
    if "alternative_assessment" in result and QUESTION["problem_id"] == "2016-B":
        alternatives = result["alternative_assessment"]
        lines.extend([
            "",
            "### 独立商业方案评估",
            f"- 方法：{alternatives.get('method')}",
            "",
        ])
        lines.extend(markdown_table(alternatives.get("alternatives", []), ["option", "category", "capex_musd", "annual_revenue_musd", "ten_year_debris_removed", "risk_score", "npv_musd", "risk_adjusted_score", "commercially_attractive"]))
    if "combination_assessment" in result and QUESTION["problem_id"] == "2016-B":
        combinations = result["combination_assessment"]
        lines.extend([
            "",
            "### 组合方案评估",
            f"- 方法：{combinations.get('method')}",
            "",
        ])
        lines.extend(markdown_table(combinations.get("combinations", [])[:10], ["combination", "capex_musd", "annual_revenue_musd", "ten_year_debris_removed", "risk_score", "npv_musd", "risk_adjusted_score", "commercially_attractive"]))
    if "what_if_scenarios" in result and QUESTION["problem_id"] == "2016-B":
        scenarios = result["what_if_scenarios"]
        lines.extend([
            "",
            "### What-if 情景",
            f"- 方法：{scenarios.get('method')}",
            "",
        ])
        lines.extend(markdown_table(scenarios.get("rows", []), ["scenario", "debris_multiplier", "revenue_multiplier", "best_option", "best_npv_musd", "best_risk_adjusted_score", "commercially_attractive"]))
    if "commercial_opportunity" in result and QUESTION["problem_id"] == "2016-B":
        opportunity = result["commercial_opportunity"]
        best = opportunity.get("best_candidate", {})
        lines.extend([
            "",
            "### 商业机会判断",
            f"- 推荐动作：{opportunity.get('recommended_action')}。",
            f"- 最佳候选：{best.get('option', best.get('combination'))}。",
            f"- 解释：{opportunity.get('interpretation')}",
        ])
    if "executive_summary" in result and QUESTION["problem_id"] == "2016-B":
        lines.extend([
            "",
            "### Executive summary",
            str(result["executive_summary"]),
        ])
    if "era_model" in result and QUESTION["problem_id"] == "2016-D":
        rows = result["era_model"].get("periods", [])
        lines.extend([
            "",
            "### 官方五时期传播网络参数",
            "- 这些参数是对题面五个时代的显式、可替换归一化假设，不是观测数据。",
            "",
        ])
        lines.extend(markdown_table(rows, ["era", "representative_year", "media_access", "transmission_speed", "network_connectivity", "gatekeeping_filter", "channel_capacity", "diffusion_rate_per_hour", "reachable_population_share"]))
    if "news_filter_model" in result and QUESTION["problem_id"] == "2016-D":
        news = result["news_filter_model"]
        lines.extend([
            "",
            "### 信息流与新闻筛选",
            f"- 阈值：{news.get('threshold')}。",
            f"- 定义：{news.get('definition')}",
            "",
        ])
        lines.extend(markdown_table(news.get("items", []), ["item", "information_value", "source_credibility", "affected_population", "novelty", "shareability", "news_score", "qualifies_as_news"]))
    if "diffusion_comparison" in result and QUESTION["problem_id"] == "2016-D":
        diffusion = result["diffusion_comparison"]
        lines.extend([
            "",
            "### 历史与今日扩散对比",
            f"- Taylor Swift 传闻如果发生在 1860/1870s 代理时代，24h awareness：{diffusion.get('taylor_1860_awareness_24h')}。",
            f"- Lincoln assassination 历史代理 24h awareness：{diffusion.get('lincoln_awareness_24h')}。",
            f"- 今日重要人物遇刺 24h awareness：{diffusion.get('important_assassination_today_awareness_24h')}。",
            "",
        ])
        lines.extend(markdown_table(diffusion.get("rows", [])[:12], ["scenario", "era", "hours", "awareness_share", "information_value", "source_credibility"]))
    if "validation" in result and QUESTION["problem_id"] == "2016-D":
        validation = result["validation"]
        lines.extend([
            "",
            "### 模型可靠性验证",
            f"- 历史代理：{validation.get('historical_proxy')}",
            f"- 今日/历史 24h 比值：{validation.get('today_to_lincoln_ratio_24h')}。",
            f"- 说明：{validation.get('reliability_note')}",
        ])
    if "capacity_2050" in result and QUESTION["problem_id"] == "2016-D":
        capacity = result["capacity_2050"]
        lines.extend([
            "",
            "### 2050 通信网络容量预测",
            f"- 预测年份：{capacity.get('prediction_year')}。",
            f"- 2050 容量指数：{capacity.get('projected_channel_capacity_index')}。",
            f"- 相对 2010s multiplier：{capacity.get('capacity_multiplier_vs_2010s')}。",
        ])
    if "opinion_influence" in result and QUESTION["problem_id"] == "2016-D":
        influence = result["opinion_influence"]
        lines.extend([
            "",
            "### 公众兴趣和观点影响",
            f"- 方法：{influence.get('method')}",
            "",
        ])
        lines.extend(markdown_table(influence.get("scenarios", []), ["scenario", "information_value", "source_credibility", "initial_bias", "message_form_strength", "network_strength", "persuasion_index", "final_support_share", "opinion_shift_from_neutral"]))
    if "factor_sensitivity" in result and QUESTION["problem_id"] == "2016-D":
        sensitivity = result["factor_sensitivity"]
        lines.extend([
            "",
            "### 影响因素敏感性",
            f"- 最敏感因素：{sensitivity.get('top_factor')}。",
            "",
        ])
        lines.extend(markdown_table(sensitivity.get("rows", []), ["factor", "direction", "low_score", "baseline_score", "high_score", "absolute_swing"]))
    if "crisis_metrics" in result and QUESTION["problem_id"] == "2016-F":
        metrics = result["crisis_metrics"]
        lines.extend([
            "",
            "### 难民危机指标体系",
            f"- 官方规模：{metrics.get('official_scale')}。",
            f"- Hungary 未安置压力代理：{metrics.get('hungary_homeless_per_100k_proxy')} / 100k。",
            "",
            "#### 启用因素",
        ])
        lines.extend([f"- {item}" for item in metrics.get("enabling_factors", [])])
        lines.extend(["", "#### 抑制因素"])
        lines.extend([f"- {item}" for item in metrics.get("inhibiting_factors", [])])
    if "flow_model" in result and QUESTION["problem_id"] == "2016-F":
        flow = result["flow_model"]
        lines.extend([
            "",
            "### 六条路线容量约束流动模型",
            f"- 方法：{flow.get('method')}",
            f"- 总分配人数：{flow.get('total_allocated_refugees')}。",
            f"- 临时容量合计：{flow.get('temporary_capacity_total')}。",
            f"- 应急溢出安置人数：{flow.get('emergency_overflow_total')}。",
            "",
        ])
        lines.extend(markdown_table(flow.get("route_allocations", []), ["route", "entry_point", "allocated_refugees", "share_of_total", "safety_score", "accessibility_score", "estimated_processing_days", "capacity_binding", "emergency_overflow_refugees"]))
    if "dynamic_capacity" in result and QUESTION["problem_id"] == "2016-F":
        capacity = result["dynamic_capacity"]
        lines.extend([
            "",
            "### 动态容量与资源前置",
            f"- 方法：{capacity.get('method')}",
            f"- 最高优先资源：{capacity.get('highest_priority_resource')}。",
            f"- 加入 NGO 后 weighted unmet need：{capacity.get('weighted_unmet_need')}。",
            "",
        ])
        lines.extend(markdown_table(capacity.get("resources", []), ["resource", "required_units", "available_units", "unmet_units", "priority_weight", "weighted_gap", "prepositioning_action"]))
    if "ngo_strategy" in result and QUESTION["problem_id"] == "2016-F":
        ngo = result["ngo_strategy"]
        lines.extend([
            "",
            "### 政府与 NGO 策略对比",
            f"- 政府单独未满足需求：{ngo.get('government_only', {}).get('unmet_need')}。",
            f"- 加入 NGO 后未满足需求：{ngo.get('with_ngo', {}).get('unmet_need')}。",
            f"- 策略变化：{ngo.get('strategy_change')}",
        ])
    if "regional_extension" in result and QUESTION["problem_id"] == "2016-F":
        regional = result["regional_extension"]
        lines.extend([
            "",
            "### Canada、China、United States 区域扩展",
            f"- 模型是否可迁移：{regional.get('does_model_transfer')}。",
            f"- 说明：{regional.get('transfer_note')}",
            "",
        ])
        lines.extend(markdown_table(regional.get("destinations", []), ["destination", "distance_penalty", "integration_capacity", "legal_access", "resource_readiness", "model_feasibility_score"]))
    if "policy_package" in result and QUESTION["problem_id"] == "2016-F":
        policy = result["policy_package"]
        lines.extend([
            "",
            "### 支持最优迁移模式的政策包",
            f"- 目标：{policy.get('policy_objective')}",
            f"- 操作指标：{policy.get('operational_metric')}",
            "",
        ])
        lines.extend([f"- {item}" for item in policy.get("recommended_policies", [])])
    if "exogenous_event" in result and QUESTION["problem_id"] == "2016-F":
        event = result["exogenous_event"]
        lines.extend([
            "",
            "### 外生事件压力测试",
            f"- 事件：{event.get('event')}",
            "",
            "#### 参数变化",
        ])
        lines.extend([f"- {item}" for item in event.get("parameter_shifts", [])])
        lines.extend(["", "#### 路线压力", ""])
        lines.extend(markdown_table(event.get("route_stress", []), ["route", "baseline_safety", "post_event_safety", "baseline_daily_capacity", "post_event_daily_capacity", "cascading_effect"]))
        lines.extend(["", "#### 韧性设计"])
        lines.extend([f"- {item}" for item in event.get("resilience_design", [])])
    if "scalability_10x" in result and QUESTION["problem_id"] == "2016-F":
        scale = result["scalability_10x"]
        lines.extend([
            "",
            "### 10 倍规模扩展",
            f"- scale factor：{scale.get('scale_factor')}。",
            f"- scaled refugees：{scale.get('scaled_refugees')}。",
            f"- 不扩容处理天数：{scale.get('scaled_resolution_days_without_capacity_expansion')}。",
            f"- 长期参数触发阈值：{scale.get('time_threshold_days_for_new_considerations')} 天。",
            "",
            "#### 新增参数",
        ])
        lines.extend([f"- {item}" for item in scale.get("new_parameters_needed", [])])
        lines.extend(["", "#### 不可扩展特征"])
        lines.extend([f"- {item}" for item in scale.get("non_scalable_features", [])])
        lines.extend(["", "#### 改变或失效的参数"])
        lines.extend([f"- {item}" for item in scale.get("becomes_irrelevant_or_changes", [])])
    if "policy_letter" in result and QUESTION["problem_id"] == "2016-F":
        lines.extend([
            "",
            "### 给 UN 的政策信",
            str(result["policy_letter"]),
        ])
    if "water_scarcity_model" in result and QUESTION["problem_id"] == "2016-E":
        model = result["water_scarcity_model"]
        lines.extend([
            "",
            "### 清洁水供给能力与缺水诊断",
            f"- 定义：{model.get('definition')}",
            f"- 选定地区：{model.get('selected_region')}。",
            f"- 基线年份：{model.get('baseline_year')}。",
            f"- freshwater withdrawals/internal resources：{model.get('baseline_stress_percent_internal_resources')}%。",
            f"- stress index：{model.get('baseline_stress_index')}。",
            f"- scarcity score/status：{model.get('scarcity_score')} / {model.get('scarcity_status')}。",
            "",
        ])
        lines.extend(markdown_table(model.get("components", []), ["component", "value", "interpretation"]))
    if "no_intervention_forecast" in result and QUESTION["problem_id"] == "2016-E":
        forecast = result["no_intervention_forecast"]
        lines.extend([
            "",
            "### 15 年无干预预测",
            f"- 最近人口增长率：{forecast.get('recent_population_growth_rate')}。",
            f"- 用水增长率假设：{forecast.get('water_use_growth_rate_assumption')}。",
            f"- 15 年后 stress index：{forecast.get('stress_index_after_15_years')}。",
            f"- 居民影响：{forecast.get('citizen_impact')}",
            "",
        ])
        lines.extend(markdown_table(forecast.get("rows", [])[:8], ["year_after_start", "freshwater_withdrawal_pct_internal_resources", "stress_index", "status"]))
    if "intervention_plan" in result and QUESTION["problem_id"] == "2016-E":
        plan = result["intervention_plan"]
        lines.extend([
            "",
            "### 干预计划",
            f"- 策略：{plan.get('strategy')}",
            "",
        ])
        lines.extend(markdown_table(plan.get("programs", []), ["program", "annual_cost_musd", "annual_withdrawal_reduction_pct_points", "annual_quality_gain_pct_points", "efficiency_score_per_billion_usd"]))
    if "intervention_forecast" in result and QUESTION["problem_id"] == "2016-E":
        with_plan = result["intervention_forecast"]
        lines.extend([
            "",
            "### 有干预预测",
            f"- 15 年后 stress index：{with_plan.get('stress_index_after_15_years')}。",
            f"- 相对无干预降低：{with_plan.get('stress_reduction_vs_no_intervention')}。",
            f"- 是否降低易受缺水影响：{with_plan.get('can_become_less_susceptible')}。",
            f"- 无干预是否 critical：{with_plan.get('will_water_be_critical_without_intervention')}。",
        ])
    if "option_assessment" in result and QUESTION["problem_id"] == "2017-A":
        assessment = result["option_assessment"]
        lines.extend([
            "",
            "### Kariba 三方案简短评估",
            f"- 管理建议：{assessment.get('brief_recommendation')}",
            "",
        ])
        lines.extend(markdown_table(assessment.get("options", []), ["option", "description", "normalized_cost", "implementation_years", "construction_disruption", "safety_improvement", "water_management_flexibility", "benefit_score", "benefit_cost_ratio"]))
    if "small_dam_system" in result and QUESTION["problem_id"] == "2017-A":
        system = result["small_dam_system"]
        recommended = system.get("recommended_system", {})
        lines.extend([
            "",
            "### 10-20 座小坝系统设计",
            f"- Kariba reference index：{system.get('kariba_reference_index')}。",
            f"- 推荐小坝数量：{system.get('recommended_dam_count')}。",
            f"- 推荐系统 water management index：{recommended.get('water_management_index')}。",
            f"- 说明：{system.get('recommendation')}",
            "",
            "#### 坝址计划",
            "",
        ])
        lines.extend(markdown_table(system.get("placements", []), ["dam_id", "river_coordinate_0_100", "segment", "local_storage_share_pct", "primary_role"]))
    if "flow_modulation_strategy" in result and QUESTION["problem_id"] == "2017-A":
        strategy = result["flow_modulation_strategy"]
        lines.extend([
            "",
            "### 多坝系统水流调度策略",
            f"- 协调原则：{strategy.get('coordination_principle')}",
            "",
        ])
        lines.extend(markdown_table(strategy.get("rules", []), ["condition", "trigger_flow_index", "release_rule", "safety_cost_tradeoff"]))
    if "extreme_flow_guidance" in result and QUESTION["problem_id"] == "2017-A":
        extreme = result["extreme_flow_guidance"]
        lines.extend([
            "",
            "### 极端流量指导",
            "",
        ])
        lines.extend(markdown_table(extreme.get("scenarios", []), ["scenario", "flow_index", "action", "zra_guidance"]))
    if "exposure_restrictions" in result and QUESTION["problem_id"] == "2017-A":
        exposure = result["exposure_restrictions"]
        lines.extend([
            "",
            "### 极端条件暴露限制",
            "",
        ])
        lines.extend(markdown_table(exposure.get("segments", []), ["segment", "max_flood_exposure_days", "max_low_water_exposure_days", "reason"]))
    if "brief_assessment_report" in result and QUESTION["problem_id"] == "2017-A":
        lines.extend([
            "",
            "### ZRA 管理层简报",
            str(result["brief_assessment_report"]),
        ])
    if "network_profile" in result and QUESTION["problem_id"] == "2017-C":
        profile = result["network_profile"]
        lines.extend([
            "",
            "### 官方路网画像",
            f"- 路段数：{profile.get('segment_count')}。",
            f"- 方向性总里程：{profile.get('total_directional_miles')} miles。",
            "",
            "#### Route summary",
            "",
        ])
        lines.extend(markdown_table(profile.get("route_summary", []), ["route_id", "route_label", "segments", "miles", "weighted_adt_2015", "max_adt_2015", "median_lanes_per_direction", "baseline_congested_segments"]))
        lines.extend(["", "#### Most congested official segments", ""])
        lines.extend(markdown_table(profile.get("most_congested_segments", [])[:10], ["route_id", "start_milepost", "end_milepost", "adt_2015", "avg_lanes_per_direction", "baseline_vc_ratio"]))
    if "official_problem_parameters" in result and QUESTION["problem_id"] == "2017-C":
        params = result["official_problem_parameters"]
        lines.extend([
            "",
            "### 交通流参数与假设",
            f"- peak hour daily share：{params.get('peak_hour_daily_share')}。",
            f"- speed limit：{params.get('speed_limit_mph')} mph。",
            f"- 人类驾驶容量假设：{params.get('human_capacity_per_lane_vph_assumption')} veh/h/lane。",
            f"- AV 专用车道容量假设：{params.get('av_lane_capacity_per_lane_vph_assumption')} veh/h/lane。",
            f"- 说明：{params.get('assumption_note')}",
        ])
    if "adoption_scenarios" in result and QUESTION["problem_id"] == "2017-C":
        scenarios = result["adoption_scenarios"]
        lines.extend([
            "",
            "### 10%/50%/90% 自动驾驶渗透率情景",
            f"- 模型：{scenarios.get('model')}",
            "",
        ])
        lines.extend(markdown_table(scenarios.get("scenario_rows", []), ["av_share", "capacity_multiplier", "mean_vc_ratio", "congested_segment_share_vc_gt_1", "total_peak_vehicle_hours", "vehicle_hours_saved_vs_baseline", "median_speed_mph"]))
    if "tipping_point" in result and QUESTION["problem_id"] == "2017-C":
        tipping = result["tipping_point"]
        lines.extend([
            "",
            "### 性能临界点",
            f"- 判据：{tipping.get('criterion')}",
            f"- AV share：{tipping.get('av_share')}。",
            f"- baseline peak vehicle-hours：{tipping.get('baseline_peak_vehicle_hours')}。",
            f"- target peak vehicle-hours：{tipping.get('target_peak_vehicle_hours')}。",
            f"- achieved peak vehicle-hours：{tipping.get('achieved_peak_vehicle_hours')}。",
        ])
    if "dedicated_lane_policy" in result and QUESTION["problem_id"] == "2017-C":
        lane_policy = result["dedicated_lane_policy"]
        lines.extend([
            "",
            "### 专用车道政策",
            f"- 规则：{lane_policy.get('rule')}",
            f"- 候选路段数：{lane_policy.get('candidate_count')}。",
            "",
        ])
        lines.extend(markdown_table(lane_policy.get("candidate_segments", [])[:12], ["route_id", "start_milepost", "end_milepost", "av_share", "avg_lanes_per_direction", "adt_2015", "vehicle_hours_saved_vs_mixed"]))
    if "governor_letter" in result and QUESTION["problem_id"] == "2017-C":
        lines.extend([
            "",
            "### Governor letter",
            str(result["governor_letter"]),
        ])
    if "baseline_model" in result and QUESTION["problem_id"] == "2017-D":
        baseline = result["baseline_model"]
        lines.extend([
            "",
            "### 安检基线排队模型",
            f"- PreCheck lanes：{baseline.get('precheck_lanes')}；regular lanes：{baseline.get('regular_lanes')}。",
            f"- combined mean wait：{baseline.get('combined_mean_wait_s')} s。",
            f"- combined p90 wait：{baseline.get('combined_p90_wait_s')} s。",
            f"- checkpoint clear time：{baseline.get('checkpoint_clear_time_s')} s。",
            "",
            "#### Queue metrics",
            "",
        ])
        queue_rows = [
            {"queue": "precheck", **baseline.get("precheck", {})},
            {"queue": "regular", **baseline.get("regular", {})},
        ]
        lines.extend(markdown_table(queue_rows, ["queue", "servers", "passenger_count", "mean_wait_s", "p90_wait_s", "max_wait_s", "mean_service_s", "last_finish_s"]))
    if "bottleneck_analysis" in result and QUESTION["problem_id"] == "2017-D":
        bottlenecks = result["bottleneck_analysis"]
        lines.extend([
            "",
            "### 瓶颈分析",
        ])
        lines.extend([f"- {item}" for item in bottlenecks.get("bottlenecks", [])])
        lines.extend(["", "#### Stage service summary", ""])
        lines.extend(markdown_table(bottlenecks.get("stage_service_summary", []), ["stage", "median_s", "p90_s"]))
    if "modification_experiments" in result and QUESTION["problem_id"] == "2017-D":
        modifications = result["modification_experiments"]
        lines.extend([
            "",
            "### 流程修改实验",
            "",
        ])
        lines.extend(markdown_table(modifications.get("modifications", []), ["modification", "precheck_lanes", "regular_lanes", "combined_mean_wait_s", "combined_p90_wait_s", "mean_wait_change_vs_baseline_s", "p90_wait_change_vs_baseline_s", "checkpoint_clear_time_s"]))
    if "cultural_sensitivity" in result and QUESTION["problem_id"] == "2017-D":
        sensitivity = result["cultural_sensitivity"]
        lines.extend([
            "",
            "### 文化/旅客风格敏感性",
            f"- 方法：{sensitivity.get('method')}",
            "",
        ])
        lines.extend(markdown_table(sensitivity.get("traveler_styles", []), ["traveler_style", "property_multiplier", "id_multiplier", "combined_mean_wait_s", "combined_p90_wait_s", "description"]))
    if "security_manager_memo" in result and QUESTION["problem_id"] == "2017-D":
        lines.extend([
            "",
            "### TSA security manager memo",
            str(result["security_manager_memo"]),
        ])
    if "roi_model" in result and QUESTION["problem_id"] == "2016-C":
        roi = result["roi_model"]
        lines.extend([
            "",
            "### Goodgrant ROI 模型",
            f"- 定义：{roi.get('definition')}",
            f"- 过滤规则：{roi.get('filtering')}",
            f"- 过滤后候选行：{roi.get('candidate_rows_after_filters')}；已评分行：{roi.get('candidate_rows_scored')}。",
            f"- 权重：{roi.get('weights')}",
        ])
    if "funding_strategy" in result and QUESTION["problem_id"] == "2016-C":
        strategy = result["funding_strategy"]
        lines.extend([
            "",
            "### 推荐资助组合",
            f"- 年预算：{strategy.get('annual_budget_usd')} USD。",
            f"- 持续年数：{strategy.get('years')}。",
            f"- 五年总预算：{strategy.get('total_five_year_budget_usd')} USD。",
            f"- 推荐学校数：{strategy.get('recommended_school_count')}。",
            "",
        ])
        lines.extend(markdown_table(strategy.get("recommended_schools", [])[:15], ["UNITID", "INSTNM", "STABBR", "annual_grant_usd", "five_year_grant_usd", "roi_score", "expected_students_reached", "rank_score"]))
    if "robustness" in result and QUESTION["problem_id"] == "2016-C":
        robust = result["robustness"]
        lines.extend([
            "",
            "### ROI 权重稳健性",
            "",
        ])
        lines.extend(markdown_table(robust.get("weight_scenarios", []), ["scenario", "success_w", "need_w", "leverage_w", "top20_overlap_with_base", "top_school"]))
    if "cfo_letter" in result and QUESTION["problem_id"] == "2016-C":
        lines.extend([
            "",
            "### CFO letter",
            str(result["cfo_letter"]),
        ])
    if "energy_profiles" in result:
        profiles = result["energy_profiles"]
        lines.extend([
            "",
            "### 四州能源画像",
            f"- 画像年份：{profiles.get('profile_year')}。",
            f"- 评价准则：{profiles.get('criteria')}",
            "",
            "#### 2009 state profiles",
            "",
        ])
        lines.extend(markdown_table(profiles.get("state_profiles", []), ["state", "state_name", "renewable_consumption_share", "renewable_production_share", "nonhydro_renewable_share", "energy_consumption_per_capita_mmbtu", "clean_profile_score"]))
    if "evolution_model" in result:
        evolution = result["evolution_model"]
        lines.extend([
            "",
            "### 历史演化模型",
            f"- 方法：{evolution.get('method')}",
            "",
        ])
        lines.extend(markdown_table(evolution.get("state_trends", []), ["state", "renewable_share_1960", "renewable_share_2009", "change_1960_2009", "recent_slope_per_year", "interpretation"]))
    if "best_profile_2009" in result:
        best = result["best_profile_2009"]
        lines.extend([
            "",
            "### 2009 最佳能源画像",
            f"- 最佳州：{best.get('state')}（{best.get('state_name')}）。",
            f"- renewable consumption share：{best.get('renewable_consumption_share')}。",
            f"- non-hydro renewable share：{best.get('nonhydro_renewable_share')}。",
            f"- clean profile score：{best.get('clean_profile_score')}。",
        ])
    if "baseline_forecast" in result:
        forecast = result["baseline_forecast"]
        lines.extend([
            "",
            "### 2025/2050 无政策基线预测",
            f"- 方法：{forecast.get('method')}",
            "",
        ])
        lines.extend(markdown_table(forecast.get("forecast_rows", []), ["state", "year", "baseline_renewable_consumption_share", "baseline_energy_consumption_per_capita_mmbtu", "model"]))
    if "compact_targets" in result:
        targets = result["compact_targets"]
        lines.extend([
            "",
            "### Interstate Compact 目标",
            f"- 目标规则：{targets.get('target_rule')}",
            "",
        ])
        lines.extend(markdown_table(targets.get("targets", []), ["state", "year", "baseline_renewable_share", "compact_target_share", "required_gap"]))
    if "compact_actions" in result:
        actions = result["compact_actions"]
        lines.extend(["", "### Compact 行动建议"])
        for action in actions.get("actions", []):
            lines.extend([
                f"- 行动：{action.get('action')}",
                f"- 模型依据：{action.get('model_link')}",
            ])
    if "governors_memo" in result:
        lines.extend([
            "",
            "### Governors memo",
            str(result["governors_memo"]),
        ])
    if "evaluation" in result:
        lines.extend([
            "- 训练集：1988-2020 年夏奥国家奖牌与参赛特征。",
            "- 留出检验：2024 年巴黎奥运会。",
            "- 输出目标：Gold 与 Total 两个回归目标。",
            f"- Gold MAE/RMSE：{result['evaluation']['Gold']['mae_2024']} / {result['evaluation']['Gold']['rmse_2024']}。",
            f"- Total MAE/RMSE：{result['evaluation']['Total']['mae_2024']} / {result['evaluation']['Total']['rmse_2024']}。",
        ])
    if "model_features" in result:
        lines.extend(["", "### 特征变量", ""])
        lines.extend([f"- `{feature}`" for feature in result["model_features"]])
    if "prediction_2028_top_total" in result:
        lines.extend(["", "### 2028 总奖牌预测 Top 10", ""])
        table_rows = [
            {
                "NOC": row["NOC"],
                "2024": row["actual_2024_total"],
                "pred_2028_total": row["pred_total"],
                "interval80": row["interval80"],
            }
            for row in result["prediction_2028_top_total"][:10]
        ]
        lines.extend(markdown_table(table_rows, ["NOC", "2024", "pred_2028_total", "interval80"]))
    if "prediction_2028_top_gold" in result:
        lines.extend(["", "### 2028 金牌预测 Top 10", ""])
        table_rows = [
            {
                "NOC": row["NOC"],
                "2024_gold": row["actual_2024_gold"],
                "pred_2028_gold": row["pred_gold"],
                "interval80": row["interval80"],
            }
            for row in result["prediction_2028_top_gold"][:10]
        ]
        lines.extend(markdown_table(table_rows, ["NOC", "2024_gold", "pred_2028_gold", "interval80"]))
    if "most_likely_improve" in result:
        lines.extend(["", "### 最可能进步", ""])
        lines.extend(markdown_table(result["most_likely_improve"][:10], ["NOC", "actual_2024_total", "pred_2028_total", "change"]))
    if "most_likely_decline" in result:
        lines.extend(["", "### 最可能退步", ""])
        lines.extend(markdown_table(result["most_likely_decline"][:10], ["NOC", "actual_2024_total", "pred_2028_total", "change"]))
    if "first_medal_expected_count" in result:
        lines.extend([
            f"- 首枚奖牌国家数量期望：{result['first_medal_expected_count']}。",
            "- 解释：该值是所有未曾获奖但有参赛记录国家的 `P(total>=0.5)` 概率和，不是简单四舍五入的确定数量。",
        ])
    if "trading_strategy" in result:
        strategy = result["trading_strategy"]
        lines.extend([
            "",
            "### 交易策略结果",
            f"- 选定策略：{strategy.get('name')}。",
            f"- 初始资金：{strategy.get('initial_cash')} USD。",
            f"- 期末价值：{strategy.get('final_value')} USD。",
            f"- 总收益率：{strategy.get('total_return_percent')}%。",
            f"- 最大回撤：{strategy.get('max_drawdown')}。",
            f"- 交易次数：{strategy.get('trade_count')}。",
            f"- 是否使用未来价格：{strategy.get('uses_future_prices')}。",
            "",
            "#### 候选策略比较",
            "",
        ])
        lines.extend(markdown_table(result.get("baseline_comparison", [])[:8], ["strategy", "final_value", "total_return_percent", "max_drawdown", "trade_count"]))
    if "transaction_cost_sensitivity" in result:
        lines.extend(["", "### 交易成本敏感性", ""])
        lines.extend(markdown_table(result.get("transaction_cost_sensitivity", []), ["alpha_gold", "alpha_bitcoin", "final_value", "total_return_percent", "trade_count"]))
    if "memo_to_trader" in result:
        lines.extend([
            "",
            "### 给交易员的备忘录",
            str(result["memo_to_trader"]),
        ])
    if "influence_network" in result:
        music_network = result["influence_network"]
        lines.extend([
            "",
            "### 音乐影响网络",
            f"- 节点数：{music_network.get('node_count')}。",
            f"- 边数：{music_network.get('edge_count')}。",
            f"- 弱连通分量：{music_network.get('weak_component_count')}。",
            f"- 最大弱连通分量节点：{music_network.get('largest_weak_component_nodes')}。",
            "",
            "#### Top influencers",
            "",
        ])
        lines.extend(markdown_table(music_network.get("top_influencers", [])[:10], ["artist_name", "main_genre", "out_degree", "in_degree", "pagerank", "influence_score"]))
    if "similarity_model" in result:
        similarity = result["similarity_model"]
        lines.extend([
            "",
            "### 音乐特征相似性",
            f"- 方法：{similarity.get('method')}",
            f"- 有流派标签艺术家数：{similarity.get('artist_count_with_genre')}。",
            f"- 同流派平均相似度：{similarity.get('within_genre_mean_similarity')}。",
            f"- 跨流派平均相似度：{similarity.get('between_genre_mean_similarity')}。",
            "",
            "#### 最相近流派对",
            "",
        ])
        lines.extend(markdown_table(similarity.get("most_similar_genre_pairs", [])[:8], ["genre_a", "genre_b", "centroid_cosine_similarity"]))
    if "genre_evolution" in result:
        evolution = result["genre_evolution"]
        lines.extend([
            "",
            "### 流派随时间演化",
            f"- 方法：{evolution.get('method')}",
            f"- 可连接流派的歌曲行数：{evolution.get('song_rows_with_genre')}。",
            "",
            "#### 流派特征趋势",
            "",
        ])
        lines.extend(markdown_table(evolution.get("genre_profiles", [])[:10], ["main_genre", "year_min", "year_max", "energy_change_1921_2020", "acousticness_change_1921_2020", "instrumentalness_change_1921_2020"]))
    if "influence_evidence" in result:
        evidence = result["influence_evidence"]
        lines.extend([
            "",
            "### 影响者是否真的影响追随者",
            f"- 可连接特征的影响边：{evidence.get('edge_pairs_with_features')}。",
            f"- 同流派影响边相似度：{evidence.get('same_genre_edge_similarity')}。",
            f"- 跨流派影响边相似度：{evidence.get('cross_genre_edge_similarity')}。",
            "",
            "#### 特征传播性",
            "",
        ])
        lines.extend(markdown_table(evidence.get("feature_contagion", [])[:10], ["feature", "influencer_follower_correlation", "mean_absolute_gap"]))
    if "revolutionary_artists" in result:
        revolution = result["revolutionary_artists"]
        lines.extend([
            "",
            "### 革命性艺术家候选",
            f"- 方法：{revolution.get('method')}",
            "",
        ])
        lines.extend(markdown_table(revolution.get("artists", [])[:10], ["artist_name", "main_genre", "active_start", "out_degree", "mean_follower_feature_distance", "revolutionary_score"]))
    if "cultural_influence_context" in result:
        context = result["cultural_influence_context"]
        lines.extend([
            "",
            "### 时间与文化影响解释",
            f"- 1990 年前影响边：{context.get('pre_1990_edges')}。",
            f"- 1990-2000 影响边：{context.get('1990_2000_edges')}。",
            f"- 2000 年后影响边：{context.get('post_2000_edges')}。",
            f"- 解释：{context.get('interpretation')}",
        ])
    if "one_page_icm_society_memo" in result:
        lines.extend([
            "",
            "### ICM Society 一页文档",
            str(result["one_page_icm_society_memo"]),
        ])
    if "spread_model" in result and QUESTION["problem_id"] == "2019-C":
        spread = result["spread_model"]
        lines.extend([
            "",
            "### Opioid Crisis 传播模型",
            f"- 县-年面板行数：{spread.get('county_year_rows')}。",
            f"- 县数量：{spread.get('county_count')}。",
            f"- 物质类别：{spread.get('substance_classes')}。",
            "",
            "#### 各州可能起始县",
            "",
        ])
        origin_rows = []
        for item in spread.get("likely_origins_by_state", []):
            for county in item.get("candidate_counties", [])[:2]:
                origin_rows.append({
                    "state": item.get("state"),
                    "earliest_year": item.get("earliest_year"),
                    "county": county.get("county"),
                    "fips": county.get("fips"),
                    "opioid_reports": county.get("opioid_reports"),
                    "rate_per_1000_drug_reports": county.get("rate_per_1000_drug_reports"),
                })
        lines.extend(markdown_table(origin_rows, ["state", "earliest_year", "county", "fips", "opioid_reports", "rate_per_1000_drug_reports"]))
    if "forecast_concerns" in result:
        forecast = result["forecast_concerns"]
        lines.extend([
            "",
            "### 2020 风险预测与阈值",
            f"- 方法：{forecast.get('method')}",
            f"- high threshold：{forecast.get('high_threshold_reports')} reports。",
            f"- watch threshold：{forecast.get('watch_threshold_reports')} reports。",
            f"- 县级趋势中位 MAE：{forecast.get('median_in_sample_mae')}。",
            "",
            "#### 2020 forecast top counties",
            "",
        ])
        lines.extend(markdown_table(forecast.get("county_forecasts_2020", [])[:10], ["state", "county", "FIPS_Combined", "observed_2017_reports", "forecast_2020_reports", "forecast_threshold"]))
    if "socioeconomic_model" in result:
        socio = result["socioeconomic_model"]
        lines.extend([
            "",
            "### ACS 社会特征关联",
            f"- 合并县-年行数：{socio.get('merged_county_year_rows')}。",
            f"- 目标：{socio.get('target')}。",
            f"- 方法：{socio.get('method')}",
            f"- 谨慎解释：{socio.get('caution')}",
            "",
            "#### Top correlations",
            "",
        ])
        lines.extend(markdown_table(socio.get("top_correlations", [])[:8], ["feature", "correlation_with_opioid_rate_per_1000", "usable_county_year_rows", "interpretation"]))
    if "counter_strategy" in result:
        strategy = result["counter_strategy"]
        lines.extend([
            "",
            "### 反制策略情景",
            f"- 策略：{strategy.get('strategy')}",
            f"- 参数边界：{strategy.get('parameter_bound')}",
            "",
            "#### Strategy scenarios",
            "",
        ])
        lines.extend(markdown_table(strategy.get("strategy_scenarios", []), ["scenario", "affected_high_counties", "affected_watch_counties", "projected_2020_reports", "reduction_vs_baseline_reports", "reduction_vs_baseline_pct"]))
    if "dea_memo" in result:
        lines.extend([
            "",
            "### DEA/NFLIS memo",
            str(result["dea_memo"]),
        ])
    if "passing_network" in result:
        network = result["passing_network"]
        lines.extend([
            "",
            "### Teaming Strategies 传球网络",
            f"- Huskies 球员节点数：{network.get('huskies_player_count')}。",
            f"- Huskies 官方传球数：{network.get('huskies_pass_count')}。",
            f"- 有向边数：{network.get('directed_edge_count')}。",
            f"- 赛季网络密度：{network.get('season_network_density')}；互惠率：{network.get('season_network_reciprocity')}；加权聚类：{network.get('season_weighted_clustering')}。",
            "",
            "#### Top pass pairs",
            "",
        ])
        lines.extend(markdown_table(network.get("top_pass_pairs", [])[:10], ["origin", "destination", "origin_position", "destination_position", "pass_count"]))
        lines.extend(["", "#### Top central players", ""])
        lines.extend(markdown_table(network.get("top_central_players", [])[:10], ["player", "position", "weighted_out_degree", "weighted_in_degree", "pagerank", "teamwork_centrality"]))
    if "formation_patterns" in result:
        patterns = result["formation_patterns"]
        lines.extend([
            "",
            "### 结构、阵型与多尺度模式",
            "",
            "#### 按结果分组的结构指标",
            "",
        ])
        lines.extend(markdown_table(patterns.get("by_outcome", []), ["Outcome", "matches", "avg_passes", "avg_density", "avg_reciprocity", "avg_triads", "avg_forward_share", "avg_midfield_share", "avg_attacking_third", "avg_goal_diff"]))
        lines.extend(["", "#### 多尺度解释", ""])
        lines.extend([f"- {item}" for item in patterns.get("scales_modeled", [])])
        if patterns.get("time_scale_note"):
            lines.append(f"- 时间尺度说明：{patterns.get('time_scale_note')}")
    if "teamwork_model" in result:
        teamwork = result["teamwork_model"]
        lines.extend([
            "",
            "### 团队协作成功模型",
            f"- 目标变量：{teamwork.get('target_definition')}",
            f"- 模型：{teamwork.get('model')}。",
            f"- 训练场次：{teamwork.get('train_matches')}；留出场次：{teamwork.get('holdout_matches')}。",
            f"- 留出 accuracy：{teamwork.get('accuracy')}；balanced accuracy：{teamwork.get('balanced_accuracy')}。",
            "",
            "#### 特征重要性",
            "",
        ])
        lines.extend(markdown_table(teamwork.get("top_feature_importance", [])[:8], ["feature", "importance"]))
        lines.extend(["", "#### 留出预测", ""])
        lines.extend(markdown_table(teamwork.get("holdout_predictions", [])[:8], ["MatchID", "Outcome", "team_success_non_loss", "predicted_success_non_loss"]))
    if "strategy_recommendations" in result:
        recommendations = result["strategy_recommendations"]
        lines.extend([
            "",
            "### 给教练的结构策略建议",
            "",
        ])
        for action in recommendations.get("actions", []):
            lines.extend([
                f"- 建议：{action.get('action')}",
                f"- 证据：{action.get('evidence')}",
                f"- 模型族：{action.get('model_family')}",
            ])
    if "coach_memo" in result:
        lines.extend([
            "",
            "### Huskies coach memo",
            str(result["coach_memo"]),
        ])
    if "generalization_memo" in result:
        lines.extend([
            "",
            "### 一般跨学科团队推广",
            str(result["generalization_memo"]),
        ])
    if "classification_model" in result:
        classification = result["classification_model"]
        metrics = classification.get("holdout_metrics", {})
        lines.extend([
            "",
            "### Hornets 误判分类模型",
            f"- 模型：{classification.get('model')}。",
            f"- 标注样本：{classification.get('labeled_rows')}；Positive ID：{classification.get('positive_id_count')}；Negative ID：{classification.get('negative_id_count')}。",
            f"- 训练行数：{classification.get('train_rows')}；留出行数：{classification.get('holdout_rows')}；留出阳性数：{classification.get('holdout_positive_count')}。",
            f"- ROC-AUC：{metrics.get('roc_auc')}；Average Precision：{metrics.get('average_precision')}。",
            f"- Positive precision/recall/F1 @0.5：{metrics.get('positive_precision_at_0_5')} / {metrics.get('positive_recall_at_0_5')} / {metrics.get('positive_f1_at_0_5')}。",
            f"- 重要警告：{classification.get('assumption_warning')}",
        ])
    if "priority_investigation" in result:
        priority = result["priority_investigation"]
        lines.extend([
            "",
            "### 有限资源调查优先级",
            f"- 待排序 unresolved 报告：{priority.get('unresolved_rows_ranked')}。",
            f"- 评分规则：{priority.get('priority_score')}。",
            "",
            "#### Top priority reports",
            "",
        ])
        lines.extend(markdown_table(priority.get("top_priority_reports", [])[:10], ["GlobalID", "Lab Status", "positive_probability", "distance_to_training_positive_km", "priority_score", "image_count", "has_specimen"]))
    if "spread_model" in result:
        spread = result["spread_model"]
        lines.extend([
            "",
            "### 扩散与空间聚类",
            f"- 题面新蜂后范围：{spread.get('queen_range_km')} km。",
            f"- Positive ID 数：{spread.get('positive_id_count')}。",
            f"- 首个阳性日期：{spread.get('first_positive_detection_date')}；最后阳性日期：{spread.get('last_positive_detection_date')}。",
            f"- 首个阳性到最远阳性距离：{spread.get('max_distance_from_first_positive_km')} km。",
            f"- 精度说明：{spread.get('precision_statement')}",
        ])
    if "model_update_plan" in result:
        update_plan = result["model_update_plan"]
        lines.extend([
            "",
            "### 新报告到来后的更新机制",
            f"- 推荐频率：{update_plan.get('recommended_update_frequency')}。",
            f"- 触发条件：{update_plan.get('trigger')}",
        ])
        lines.extend([f"- {item}" for item in update_plan.get("steps", [])])
    if "eradication_evidence" in result:
        eradication = result["eradication_evidence"]
        lines.extend([
            "",
            "### 根除证据标准",
            f"- 当前数据评估：{eradication.get('current_data_assessment')}",
            f"- 最后阳性到最后提交间隔：{eradication.get('days_between_last_positive_and_last_submission')} 天。",
        ])
        lines.extend([f"- {item}" for item in eradication.get("criteria", [])])
    if "wsda_memo" in result:
        lines.extend([
            "",
            "### WSDA 两页备忘录",
            str(result["wsda_memo"]),
        ])
    if "sport_importance" in result:
        lines.extend(["", "### 国家优势运动", ""])
        rows = []
        for item in result["sport_importance"][:12]:
            top = "; ".join(f"{s['sport']}({s['share']})" for s in item["top_sports"])
            rows.append({"NOC": item["NOC"], "top_sports": top})
        lines.extend(markdown_table(rows, ["NOC", "top_sports"]))
    if "coach_effect_candidates" in result:
        lines.extend(["", "### 伟大教练效应候选", ""])
        lines.extend(markdown_table(result["coach_effect_candidates"][:12], ["NOC", "Sport", "Year", "medal_rows", "jump_vs_recent_mean"]))
        chosen = result["coach_effect_candidates"][:3]
        lines.extend([
            "",
            "### 投资建议",
        ])
        for item in chosen:
            lines.append(
                f"- {item['NOC']}：优先核验并投资 `{item['Sport']}` 高水平教练团队；以异常跃升量 `{item['jump_vs_recent_mean']}` 作为上限型增益参考。"
            )
        lines.extend([
            "- 将候选表中 `jump_vs_recent_mean` 高、且国家已有基础参赛规模的运动作为优先人工核验对象。",
            "- 该数据只能识别异常跃升，不能单独证明教练因果效应；正式论文应补充教练履历时间线作为外部解释。",
        ])
    if "serve_baseline" in result:
        lines.extend([
            "",
            "### 发球基线",
            f"- 全部发球方得分率：{result['serve_baseline']['server_win_rate_all_points']}。",
            f"- 一发发球方得分率：{result['serve_baseline']['server_win_rate_first_serve_points']}。",
            f"- 二发发球方得分率：{result['serve_baseline']['server_win_rate_second_serve_points']}。",
        ])
    if "flow_summary" in result:
        flow = result["flow_summary"]
        lines.extend([
            "",
            "### 势头流结果",
            f"- 比赛：{flow['match_id']}，{flow['player1']} vs {flow['player2']}。",
            f"- 逐分数：{flow['points']}。",
            f"- `momentum_p1` 范围：{flow['momentum_min_p1']} 到 {flow['momentum_max_p1']}。",
            f"- 强势头换向次数：{flow['strong_sign_changes']}。",
            "",
            "#### 最大势头点",
            "",
        ])
        lines.extend(markdown_table(flow["largest_momentum_points"][:8], ["point_index", "set_no", "game_no", "better_player", "momentum_p1"]))
    if "randomness_assessment" in result:
        random_check = result["randomness_assessment"]
        lines.extend([
            "",
            "### 随机波动假设评估",
            f"- 比赛数：{random_check['match_count']}。",
            f"- 发球校正残差 lag-1 平均相关：{random_check['mean_lag1_serve_adjusted_corr']}。",
            f"- 跨比赛 z 值：{random_check['lag1_z_score_across_matches']}。",
            f"- 决赛最长连续得分串：{random_check['final_match_longest_point_streak']}。",
            f"- 解释：{random_check['interpretation']}",
        ])
    if "swing_prediction" in result:
        swing = result["swing_prediction"]
        lines.extend([
            "",
            "### 势头换向预测",
            f"- 预测目标：{swing['target']}。",
            f"- 训练行数：{swing['train_rows']}，留出行数：{swing['holdout_rows']}。",
            f"- 留出 ROC-AUC：{swing['holdout_final_match_metrics']['roc_auc']}。",
            f"- 留出 Brier：{swing['holdout_final_match_metrics']['brier']}。",
            "",
            "#### 关键特征",
            "",
        ])
        lines.extend(markdown_table(swing["top_coefficients_abs"][:10], ["feature", "coefficient"]))
        if "highest_alert_points_final" in swing:
            lines.extend(["", "#### 决赛最高换向预警点", ""])
            lines.extend(markdown_table(swing["highest_alert_points_final"][:8], ["point_index", "set_no", "game_no", "probability", "momentum_p1"]))
    if "generalization" in result:
        general = result["generalization"]
        lines.extend([
            "",
            "### 泛化测试",
            f"- 评估比赛数：{general['evaluated_matches']}。",
            f"- 最后 30 分势头预测点数优势方准确率：{general['last30_momentum_winner_accuracy']}。",
            f"- 决赛留出结果：{general['final_match_prediction']}。",
            f"- 局限：{general['limitation']}",
        ])
    if "coach_memo" in result and isinstance(result["coach_memo"], dict):
        memo = result["coach_memo"]
        lines.extend([
            "",
            "### 教练备忘录",
            f"- 核心建议：{memo['message']}",
            "- 临场监控指标：",
        ])
        lines.extend([f"- `{indicator}`" for indicator in memo.get("recommended_live_indicators", [])])
    if "network_summary" in result:
        network = result["network_summary"]
        lines.extend([
            "",
            "### 路网规模",
            f"- 驾车节点：{network['drive_nodes']}。",
            f"- 驾车边：{network['drive_edges']}。",
            f"- 最大弱连通分量节点：{network['largest_weak_component_nodes']}。",
            f"- 公交线路：{network['bus_routes']}，公交站：{network['bus_stops']}。",
        ])
    if "bridge_impact" in result:
        bridge = result["bridge_impact"]
        lines.extend([
            "",
            "### 桥梁坍塌/重建影响",
            f"- 移除桥梁走廊边数：{bridge['removed_edge_count']}。",
            f"- 移除桥梁走廊总长度：{bridge['removed_total_km']} km。",
            f"- 断连 OD 数：{bridge['disconnected_od_count']}。",
            f"- 最大额外比例：{bridge['max_extra_pct']}%。",
            "",
        ])
        lines.extend(markdown_table(bridge["od_impacts"], ["od_pair", "status_after_removal", "baseline_km", "collapse_km", "extra_km", "extra_pct"]))
    if "bus_project" in result:
        bus = result["bus_project"]
        lines.extend([
            "",
            "### 公交/步行项目",
            f"- 推荐项目：{bus['recommended_project']}",
            f"- 无候车亭站点：{bus['no_shelter_stops']} / {bus['total_stops']}。",
            f"- 无候车亭站点客流占比：{bus['riders_at_no_shelter_share']}。",
            f"- 前 10 个高客流无候车亭站点覆盖客流：{bus['top10_no_shelter_riders']}。",
            "",
        ])
        lines.extend(markdown_table(bus["priority_stops"][:10], ["stop_name", "riders_total", "route_count", "nearest_drive_node"]))
    if "project_recommendations" in result:
        recommendations = result["project_recommendations"]
        lines.extend(["", "### 项目收益、利益相关者与扰动", ""])
        for item in recommendations["recommended_projects"]:
            lines.extend([
                f"#### {item['project']}",
                f"- 主要收益：{item['primary_benefit']}",
                f"- 居民收益：{item['resident_benefit']}",
                f"- 其他利益相关者：{item['other_stakeholders']}",
                f"- 扰动：{item['disruption']}",
            ])
    if "safety_priorities" in result:
        safety = result["safety_priorities"]
        lines.extend([
            "",
            "### 安全优先级",
            f"- 策略：{safety['safety_strategy']}",
            "",
            "#### 高暴露道路",
            "",
        ])
        lines.extend(markdown_table(safety["high_exposure_roads"][:10], ["road_name", "aadt_current", "lanes", "aadt_per_lane", "functional_class"]))
        lines.extend(["", "#### 高客流公交站", ""])
        lines.extend(markdown_table(safety["high_ridership_stops"][:10], ["stop_name", "riders_total", "shelter", "routes"]))
    if "mayor_memo" in result:
        lines.extend([
            "",
            "### 市长备忘录",
            str(result["mayor_memo"]),
        ])
    if "network_model" in result:
        network_model = result["network_model"]
        lines.extend([
            "",
            "### 五大湖网络模型",
            "- 湖泊节点：" + " -> ".join(network_model.get("lakes", [])),
            "- 连接河流：" + " -> ".join(network_model.get("connecting_flows", [])),
            "",
            "#### 控制坝",
            "",
        ])
        lines.extend(markdown_table(network_model.get("control_dams", []), ["lake", "controlled_outflow", "control"]))
    if "target_levels" in result:
        target_levels = result["target_levels"]
        lines.extend([
            "",
            "### 分月最优水位目标",
            f"- 方法：{target_levels['method']}",
            "",
        ])
        lines.extend(markdown_table(target_levels["lake_summary"], ["lake", "annual_target_mean_m", "mean_operating_band_width_m", "seasonal_target_min_m", "seasonal_target_max_m"]))
    if "control_policy" in result:
        control_policy = result["control_policy"]
        lines.extend([
            "",
            "### 控制算法",
            f"- 规则：{control_policy['rule']}",
            "",
        ])
        lines.extend(markdown_table(control_policy["summary"], ["lake", "control_flow", "mean_abs_level_deviation_m", "mean_abs_recommended_change_cms", "max_recommended_change_cms"]))
    if "evaluation_2017" in result:
        evaluation = result["evaluation_2017"]
        lines.extend([
            "",
            "### 2017 年评价",
            f"- 实际 stakeholder cost：{evaluation['actual_total_stakeholder_cost']}。",
            f"- 平均建议控制幅度：{evaluation['mean_control_effort_cms']} cms。",
            f"- 解释：{evaluation['interpretation']}",
            "",
            "#### 2017 最高成本月份",
            "",
        ])
        lines.extend(markdown_table(evaluation["highest_cost_months"][:10], ["lake", "date", "level_m", "target_m", "deviation_m", "cost_total"]))
    if "sensitivity" in result:
        sensitivity = result["sensitivity"]
        lines.extend(["", "### 两坝出流敏感性", ""])
        lines.extend(markdown_table(sensitivity.get("dam_outflow_sensitivity", []), ["lake", "control_flow", "rows", "rmse_m", "standardized_outflow_sensitivity", "interpretation"]))
        lines.extend(["", "### 环境条件敏感性", ""])
        lines.extend(markdown_table(sensitivity.get("environmental_condition_sensitivity", []), ["lake", "mean_monthly_cost", "high_water_months", "low_water_months", "max_abs_deviation_m"]))
    if "lake_ontario_focus" in result:
        ontario = result["lake_ontario_focus"]
        lines.extend([
            "",
            "### Lake Ontario 专项",
            f"- 记录数：{ontario['records']}。",
            f"- 高水位月份：{ontario['high_water_months']}，低水位月份：{ontario['low_water_months']}。",
            f"- 平均绝对偏离：{ontario['mean_abs_deviation_m']} m。",
            f"- 与连接河流流量相关：{ontario['correlation_with_flows']}。",
            "",
            "#### Stakeholder factors",
            "",
        ])
        lines.extend([f"- {item}" for item in ontario.get("stakeholder_factors", [])])
        lines.extend(["", "#### 最高成本月份", ""])
        lines.extend(markdown_table(ontario.get("highest_cost_months", [])[:8], ["date", "level_m", "target_m", "deviation_m", "cost_total"]))
    if "ijc_memo" in result:
        lines.extend([
            "",
            "### IJC 备忘录",
            str(result["ijc_memo"]),
        ])
    if "insurance_model" in result:
        insurance = result["insurance_model"]
        rule = insurance.get("underwriting_rule", {})
        summary = insurance.get("policy_grid_summary", {})
        lines.extend([
            "",
            "### 财产保险承保模型",
            f"- 模型：{insurance.get('model')}。",
            f"- 承保分数解释：{rule.get('score')}。",
            f"- approve 阈值：{rule.get('approve_threshold')}；decline 阈值：{rule.get('decline_threshold')}。",
            f"- 网格行数：{summary.get('rows')}；approve/conditional/decline：{summary.get('approve_rows')}/{summary.get('conditional_rows')}/{summary.get('decline_rows')}。",
            "",
            "#### 最稳健承保情景",
            "",
        ])
        lines.extend(markdown_table(insurance.get("best_cases", [])[:6], ["hazard_frequency_index", "severity_index", "property_vulnerability", "mitigation_effect", "underwriting_viability_score", "decision"]))
        lines.extend(["", "#### 最高风险情景", ""])
        lines.extend(markdown_table(insurance.get("worst_cases", [])[:6], ["hazard_frequency_index", "severity_index", "property_vulnerability", "mitigation_effect", "underwriting_viability_score", "decision"]))
    if "regional_demonstration" in result:
        regional = result["regional_demonstration"]
        lines.extend([
            "",
            "### 两大洲地区演示",
            f"- 说明：{regional.get('description')}。",
            "",
        ])
        lines.extend(markdown_table(regional.get("regions", []), ["region", "continent", "dominant_hazards", "net_loss_ratio", "underwriting_viability_score", "decision"]))
    if "owner_mitigation" in result:
        mitigation = result["owner_mitigation"]
        best = mitigation.get("best_action", {})
        lines.extend([
            "",
            "### 业主可影响承保的减灾措施",
            f"- 基准风险分：{mitigation.get('baseline_risk_score')}。",
            f"- 最优行动：{best.get('action')}；行动后风险分：{best.get('risk_score_after')}；保险信心增益：{best.get('insurer_score_gain')}。",
            f"- 解释：{mitigation.get('interpretation')}。",
            "",
        ])
        lines.extend(markdown_table(mitigation.get("actions", [])[:8], ["action", "risk_reduction", "owner_cost_index", "risk_score_after", "insurer_score_gain"]))
    if "build_site_model" in result:
        build_site = result["build_site_model"]
        lines.extend([
            "",
            "### 建址与增长决策",
            f"- 模型：{build_site.get('model')}。",
            "",
        ])
        lines.extend(markdown_table(build_site.get("site_recommendations", []), ["site", "hazard_index", "service_viability", "resilience_cost", "build_score", "recommendation"]))
    if "preservation_model" in result:
        preservation = result["preservation_model"]
        lines.extend([
            "",
            "### 社区历史建筑保护模型",
            f"- 选择地标：{preservation.get('landmark')}。",
            f"- 模型：{preservation.get('model')}。",
            "",
        ])
        lines.extend(markdown_table(preservation.get("priority_ranking", [])[:8], ["building", "significance_score", "preservation_urgency", "benefit_cost_ratio", "recommended_action"]))
    if "landmark_application" in result:
        application = result["landmark_application"]
        plan = application.get("recommended_plan", {})
        lines.extend([
            "",
            "### 地标应用与保护计划",
            f"- 地标：{application.get('landmark')}。",
            f"- 成本建议：{plan.get('cost_proposal_musd')} million USD。",
            f"- benefit/cost ratio：{plan.get('benefit_cost_ratio')}。",
            f"- Phase 1：{plan.get('phase_1')}。",
            f"- Phase 2：{plan.get('phase_2')}。",
            f"- Phase 3：{plan.get('phase_3')}。",
        ])
    if "community_letter" in result:
        lines.extend([
            "",
            "### 给社区的一页信",
            str(result["community_letter"]),
        ])
    if "client_selection" in result:
        client = result["client_selection"]
        lines.extend([
            "",
            "### 客户选择",
            f"- 选择客户：{client.get('selected_client')}。",
            f"- 选择理由：{client.get('selection_reason')}。",
            f"- 模型：{client.get('model')}。",
            "",
            "#### 候选客户评分",
            "",
        ])
        lines.extend(markdown_table(client.get("candidate_clients", [])[:8], ["client", "mandate_fit", "cross_border_power", "data_access", "implementation_capacity", "client_fit_score"]))
    if "project_design" in result:
        project = result["project_design"]
        lines.extend([
            "",
            "### 五年项目设计",
            f"- 项目名：{project.get('project_name')}。",
            f"- 项目周期：{project.get('duration_years')} 年。",
            f"- 适配性：{project.get('suitability_for_client')}。",
            "",
            "#### 干预组合",
            "",
        ])
        lines.extend(markdown_table(project.get("interventions", []), ["intervention", "annual_cost_musd", "year1_reduction_pct", "maturity_gain_pct_per_year"]))
    if "analysis_support" in result:
        support = result["analysis_support"]
        complexity = support.get("complexity_framework", {})
        lines.extend([
            "",
            "### 分析支持与复杂系统框架",
            "- 建模过程：",
        ])
        lines.extend([f"- {item}" for item in support.get("modeling_processes", [])])
        lines.extend([
            "",
            f"- 使用复杂系统框架：{complexity.get('used')}。",
            "#### 复杂系统边",
            "",
        ])
        lines.extend(markdown_table(support.get("complex_system_edges", [])[:10], ["source", "target", "influence_weight", "relationship"]))
    if "resource_needs" in result:
        resource = result["resource_needs"]
        lines.extend([
            "",
            "### 额外资源与权力需求",
            f"- 5 年新增预算：{resource.get('additional_budget_musd')} million USD。",
            "",
            "#### 额外权力",
        ])
        lines.extend([f"- {item}" for item in resource.get("additional_powers", [])])
        lines.extend(["", "#### 资源计划", ""])
        lines.extend(markdown_table(resource.get("resource_rows", []), ["intervention", "startup_cost_musd", "annual_cost_musd", "five_year_cost_musd"]))
    if "impact_projection" in result:
        impact = result["impact_projection"]
        lines.extend([
            "",
            "### 五年影响预测",
            f"- 方法：{impact.get('method')}。",
            f"- 第 5 年无项目贸易额：{impact.get('baseline_illegal_trade_value_year5_billion_usd')} billion USD。",
            f"- 第 5 年项目贸易额：{impact.get('projected_illegal_trade_value_year5_billion_usd')} billion USD。",
            f"- 第 5 年累计降低：{impact.get('final_trade_reduction_pct')}%。",
            "",
        ])
        lines.extend(markdown_table(impact.get("annual_rows", []), ["year", "baseline_illegal_trade_value_billion_usd", "projected_illegal_trade_value_billion_usd", "cumulative_trade_reduction_pct"]))
    if "goal_probability" in result:
        goal = result["goal_probability"]
        lines.extend([
            "",
            "### 达成目标概率",
            f"- 目标：{goal.get('goal')}。",
            f"- 基础概率：{goal.get('base_probability')}。",
            f"- 达标概率：{goal.get('probability_reach_goal')}。",
        ])
    if "sensitivity_analysis" in result:
        sensitivity = result["sensitivity_analysis"]
        lines.extend([
            "",
            "### 情境化敏感性分析",
            f"- 方法：{sensitivity.get('method')}。",
            "",
            "#### 有利条件",
            "",
        ])
        lines.extend(markdown_table(sensitivity.get("top_helpful_conditions", []), ["condition", "effect_on_goal_probability", "adjusted_probability"]))
        lines.extend(["", "#### 不利条件", ""])
        lines.extend(markdown_table(sensitivity.get("top_harmful_conditions", []), ["condition", "effect_on_goal_probability", "adjusted_probability"]))
    if "client_memo" in result:
        lines.extend([
            "",
            "### 给客户的一页备忘录",
            str(result["client_memo"]),
        ])
    if "report_count_model" in result:
        report_count = result["report_count_model"]
        lines.extend([
            "",
            "### Wordle 报告人数与困难模式模型",
            f"- 模型：{report_count['model']}。",
            f"- 预测日期：{report_count['prediction_date']}，预测词：{report_count['prediction_word']}。",
            f"- 报告人数预测：{report_count['predicted_reported_results']}。",
            f"- 80% 预测区间：{report_count['prediction_interval_80']}。",
            f"- 报告人数留出 MAE/RMSE：{report_count['holdout_mae_reported_results']} / {report_count['holdout_rmse_reported_results']}。",
            f"- 困难模式比例预测：{report_count['predicted_hard_mode_rate']}；困难模式留出 MAE：{report_count['hard_mode_holdout_mae_rate']}。",
            "",
            "#### 困难模式词属性影响",
            "",
        ])
        lines.extend(markdown_table(report_count.get("word_attribute_effects_on_hard_mode", []), ["feature", "coefficient"]))
    if "eerie_prediction" in result:
        prediction = result["eerie_prediction"]
        lines.extend([
            "",
            "### EERIE 分布预测",
            f"- 模型：{prediction['model']}。",
            f"- 预测对象：{prediction['word']} @ {prediction['date']}。",
            f"- 留出平均桶 MAE：{prediction['holdout_mean_bucket_mae_percent_points']} 个百分点。",
            "",
        ])
        rows = []
        for row in prediction.get("table_rows", []):
            interval = prediction.get("prediction_intervals_80", {}).get(row["bucket"], [])
            rows.append(
                {
                    "bucket": row["bucket"],
                    "predicted_percent": row["predicted_percent"],
                    "interval80": interval,
                    "holdout_mae": row["holdout_mae_percent_points"],
                }
            )
        lines.extend(markdown_table(rows, ["bucket", "predicted_percent", "interval80", "holdout_mae"]))
    if "difficulty_model" in result:
        difficulty = result["difficulty_model"]
        lines.extend([
            "",
            "### Wordle 难度分类",
            f"- 模型：{difficulty['model']}。",
            f"- easy/medium 阈值：{difficulty['thresholds_expected_attempts']['easy_max']}；medium/hard 阈值：{difficulty['thresholds_expected_attempts']['medium_max']}。",
            f"- 留出准确率：{difficulty['holdout_accuracy']}。",
            f"- EERIE 期望尝试次数：{difficulty['eerie_expected_attempts_from_distribution']}，难度类别：{difficulty['eerie_class']}。",
            "",
            "#### 重要特征",
            "",
        ])
        lines.extend(markdown_table(difficulty.get("feature_importance", [])[:10], ["feature", "importance"]))
        lines.extend(["", "#### 最难样本", ""])
        lines.extend(markdown_table(difficulty.get("hardest_words", [])[:8], ["date", "word", "expected_attempts", "difficulty_class"]))
    if "interesting_features" in result:
        features = result["interesting_features"]
        lines.extend([
            "",
            "### Wordle 数据集额外特征",
            f"- 前 30 天平均报告人数：{features['reported_results_first30_mean']}。",
            f"- 后 30 天平均报告人数：{features['reported_results_last30_mean']}。",
            f"- 报告人数变化率：{features['reported_results_change_pct_first30_to_last30']}%。",
            f"- 重复字母词数量：{features['repeated_letter_word_count']}；非重复字母词数量：{features['non_repeated_letter_word_count']}。",
            f"- 重复字母词平均期望尝试次数：{features['repeated_letter_expected_attempts_mean']}；非重复字母词：{features['non_repeated_expected_attempts_mean']}。",
            f"- 困难模式平均占比：{features['hard_mode_rate_mean']}。",
            "",
            "#### 星期摘要",
            "",
        ])
        lines.extend(markdown_table(features.get("weekday_summary", []), ["weekday", "mean_reported_results", "mean_expected_attempts"]))
    if "editor_letter" in result:
        lines.extend([
            "",
            "### 给 Puzzle Editor 的摘要信",
            str(result["editor_letter"]),
        ])
    if "price_model" in result:
        price_model = result["price_model"]
        lines.extend([
            "",
            "### 帆船挂牌价模型",
            f"- 模型：{price_model['model']}。",
            f"- 目标变量：{price_model['target']}。",
            f"- 训练行数：{price_model['train_rows']}，留出行数：{price_model['holdout_rows']}。",
            f"- 留出 MAE/RMSE：{price_model['holdout_mae_usd']} / {price_model['holdout_rmse_usd']} USD。",
            f"- 留出 MAPE/Median APE：{price_model['holdout_mape']} / {price_model['holdout_median_ape']}。",
            "",
            "#### 型号价格精度",
            "",
        ])
        lines.extend(
            markdown_table(
                price_model.get("precision_by_variant", [])[:12],
                ["hull_type", "make", "variant", "holdout_count", "observed_median_price", "predicted_median_price", "median_abs_pct_error"],
            )
        )
    if "region_effects" in result:
        region_effects = result["region_effects"]
        lines.extend([
            "",
            "### 区域效应",
            f"- 模型：{region_effects['model']}。",
            f"- 基准区域：{region_effects['baseline_region']}。",
            "",
        ])
        lines.extend(markdown_table(region_effects.get("effects", []), ["region", "hull_type", "price_effect_pct", "p_value", "statistically_significant_5pct"]))
        lines.extend(["", "#### 船型间一致性", ""])
        lines.extend(markdown_table(region_effects.get("consistency_across_hulls", []), ["region", "catamaran_minus_monohull_log_effect", "interaction_p_value", "consistent_at_5pct"]))
    if "hong_kong_market" in result:
        hk_market = result["hong_kong_market"]
        lines.extend([
            "",
            "### 香港市场情景",
            f"- 官方 Excel 中香港行数：{hk_market['official_hk_rows_in_workbook']}。",
            f"- 解释：{hk_market['interpretation']}",
            f"- 补充来源数：{hk_market['supplemental_source_count']}。",
            "",
            "#### 香港可比挂牌样本",
            "",
        ])
        lines.extend(markdown_table(hk_market.get("comparables", [])[:12], ["make", "variant", "hull_type", "length_ft", "year", "listing_price_usd", "known_region_model_price_median_usd", "hk_effect_pct_vs_known_region_model", "source"]))
        lines.extend(["", "#### 按船型汇总", ""])
        lines.extend(markdown_table(hk_market.get("effect_by_hull_type", []), ["hull_type", "sample_count", "median_hk_effect_pct", "mean_hk_effect_pct", "median_listing_price_usd"]))
    if "interesting_inferences" in result:
        inferences = result["interesting_inferences"]
        lines.extend([
            "",
            "### 帆船数据其他推论",
            f"- 双体船中位价：{inferences['catamaran_median_price_usd']} USD。",
            f"- 单体船中位价：{inferences['monohull_median_price_usd']} USD。",
            f"- 双体船中位溢价：{inferences['catamaran_median_premium_pct']}%。",
            f"- 价格与长度相关系数：{inferences['price_length_correlation']}。",
            f"- 价格与船龄相关系数：{inferences['price_age_correlation']}。",
            "",
            "#### 区域-船型摘要",
            "",
        ])
        lines.extend(markdown_table(inferences.get("region_hull_summary", []), ["hull_type", "region", "count", "median_price", "median_length"]))
        lines.extend(["", "#### 高中位价品牌", ""])
        lines.extend(markdown_table(inferences.get("high_median_price_makes", [])[:10], ["hull_type", "make", "count", "median_price"]))
    if "broker_report" in result:
        lines.extend([
            "",
            "### 给香港经纪人的摘要报告",
            str(result["broker_report"]),
        ])
    if "measurement_protocol" in result:
        measurement = result["measurement_protocol"]
        lines.extend([
            "",
            "### 非破坏测量方案",
            f"- 原则：{measurement['principle']}。",
            f"- 测量模板：`{measurement['measurement_template']}`。",
            "",
            "#### 推荐字段",
            "",
        ])
        lines.extend(markdown_table(measurement.get("measurements", [])[:12], ["field", "tool"]))
    if "worked_example_assumptions" in result:
        assumptions = result["worked_example_assumptions"]
        geometry = assumptions.get("stair_geometry", {})
        lines.extend([
            "",
            "### Worked Example 假设",
            f"- 用途：{assumptions.get('purpose')}。",
            f"- 材料：{assumptions.get('material')}。",
            f"- 磨损系数：{assumptions.get('specific_wear_mm_per_100k_passages')} mm / 100k passages。",
            f"- 交通反演候选年龄：{assumptions.get('candidate_age_years_for_traffic_inverse')} 年。",
            f"- 几何：{geometry}。",
            "- 这些数值是确定性演示参数，不是官方观测表。",
        ])
    if "inverse_wear_model" in result:
        inverse = result["inverse_wear_model"]
        usage = inverse.get("usage_frequency", {})
        direction = inverse.get("direction_preference", {})
        simultaneous = inverse.get("simultaneous_use", {})
        lines.extend([
            "",
            "### 磨损反演结果",
            "#### 使用频率",
            f"- 模型：{usage.get('model')}。",
            f"- 中心磨损中位数：{usage.get('median_center_wear_depth_mm')} mm。",
            f"- 累计通行量：{usage.get('estimated_passages_per_tread')}。",
            f"- 日均使用人数：{usage.get('estimated_daily_users')}。",
            "",
            "#### 方向偏好",
            f"- 模型：{direction.get('model')}。",
            f"- 前/后缘圆角比：{direction.get('front_to_back_rounding_ratio')}。",
            f"- 偏好方向：{direction.get('favored_direction')}。",
            "",
            "#### 同时使用",
            f"- 模型：{simultaneous.get('model')}。",
            f"- 侧带/中心磨损比：{simultaneous.get('side_to_center_wear_ratio')}。",
            f"- 模式：{simultaneous.get('pattern')}。",
        ])
    if "consistency_check" in result:
        consistency = result["consistency_check"]
        checks = consistency.get("checks", {})
        lines.extend([
            "",
            "### 一致性检查",
            f"- 总体判断：{consistency.get('overall_consistency')}。",
            f"- 建议：{consistency.get('recommended_action')}。",
            "",
        ])
        lines.extend(markdown_table([{"check": key, "value": value} for key, value in checks.items()], ["check", "value"]))
    if "age_reliability" in result:
        age = result["age_reliability"]
        lines.extend([
            "",
            "### 年龄与可靠性",
            f"- 模型：{age.get('model')}。",
            f"- 年龄估计：{age.get('estimated_age_years')} 年。",
            f"- 合理区间：{age.get('plausible_interval_years')} 年。",
            f"- 可靠性：{age.get('reliability_rating')}。",
            f"- 合理网格数：{age.get('plausible_grid_cells')} / {age.get('total_grid_cells')}。",
        ])
    if "renovation_detection" in result:
        renovation = result["renovation_detection"]
        candidates = renovation.get("repair_candidates", [])
        lines.extend([
            "",
            "### 维修或翻新检测",
            f"- 模型：{renovation.get('model')}。",
            f"- 候选数量：{len(candidates)}。",
            "",
        ])
        lines.extend(markdown_table(candidates[:8], ["step_id", "wear_jump_mm", "patch_boundary_score", "tool_marks_present", "candidate_score"]))
    if "material_source_guidance" in result:
        material = result["material_source_guidance"]
        lines.extend([
            "",
            "### 材料来源判断",
            f"- 总原则：{material.get('material')}。",
            "",
            "#### 石材流程",
            "",
        ])
        lines.extend([f"- {item}" for item in material.get("stone_source_workflow", [])])
        lines.extend(["", "#### 木材流程", ""])
        lines.extend([f"- {item}" for item in material.get("wood_source_workflow", [])])
    if "daily_use_pattern" in result:
        daily = result["daily_use_pattern"]
        lines.extend([
            "",
            "### 典型日使用模式",
            f"- 日均使用人数：{daily.get('estimated_daily_users')}。",
            f"- 峰值时段占比：{daily.get('peak_period_share_of_daily_use')}。",
            f"- 峰值时段人数：{daily.get('peak_period_users')}。",
            f"- 低强度时段每小时人数：{daily.get('regular_hour_users_if_spread_over_10_hours')}。",
            f"- 判断：{daily.get('short_burst_vs_long_duration')}。",
        ])
    if "location_model" in result:
        location = result["location_model"]
        uncertainty = location.get("position_uncertainty", {})
        lines.extend([
            "",
            "### 潜水器位置预测模型",
            f"- 模型：{location.get('model')}。",
            f"- 12 小时不确定区域：{uncertainty.get('area_km2_after_12h')} km^2。",
            f"- 24 小时不确定区域：{uncertainty.get('area_km2_after_24h')} km^2。",
            f"- 12 小时预测中心：{uncertainty.get('center_after_12h_km')} km。",
            "",
            "#### 主要不确定性",
        ])
        lines.extend([f"- {item}" for item in uncertainty.get("dominant_uncertainties", [])])
        lines.extend(["", "#### 降低不确定性的遥测", ""])
        rows = [
            {
                "signal": item.get("signal"),
                "equipment": item.get("equipment"),
                "uncertainty_reduced": item.get("uncertainty_reduced"),
            }
            for item in location.get("telemetry_to_reduce_uncertainty", [])
        ]
        lines.extend(markdown_table(rows, ["signal", "equipment", "uncertainty_reduced"]))
    if "equipment_recommendations" in result:
        equipment = result["equipment_recommendations"]
        lines.extend([
            "",
            "### 搜索装备准备",
            f"- 模型：{equipment.get('model')}。",
            f"- 总建议：{equipment.get('recommendation')}",
            "",
            "#### 主船常备装备",
            "",
        ])
        lines.extend(markdown_table(equipment.get("host_ship_equipment", []), ["asset", "readiness_hours", "usage_cost_index", "coverage_km2_per_hour", "quality", "search_value_score"]))
        lines.extend(["", "#### 救援船增援装备", ""])
        lines.extend(markdown_table(equipment.get("rescue_vessel_equipment", []), ["asset", "reason"]))
    if "search_plan" in result:
        search = result["search_plan"]
        probability = search.get("search_probability", {})
        lines.extend([
            "",
            "### 搜索部署与发现概率",
            f"- 模型：{search.get('model')}。",
            f"- 发现概率公式：`{probability.get('formula')}`。",
            f"- 12 小时发现概率：{probability.get('probability_found_by_12h')}。",
            f"- 24 小时发现概率：{probability.get('probability_found_by_24h')}。",
            "",
            "#### 初始部署点",
            "",
        ])
        lines.extend(markdown_table(search.get("deployment_points", []), ["point", "east_km", "north_km", "purpose"]))
        lines.extend(["", "#### 搜索模式", ""])
        lines.extend([f"- {item}" for item in search.get("search_pattern", [])])
    if "extrapolation" in result:
        extrapolation = result["extrapolation"]
        caribbean = extrapolation.get("caribbean_adjustments", {})
        multi = extrapolation.get("multi_submersible", {})
        lines.extend([
            "",
            "### 迁移到加勒比海与多潜水器",
            f"- 加勒比海洋流不确定性倍数：{caribbean.get('current_uncertainty_multiplier')}。",
            f"- 地形调整：{caribbean.get('terrain_adjustment')}。",
            f"- 通信调整：{caribbean.get('communications_adjustment')}。",
            f"- 多潜水器协调规则：{multi.get('coordination_rule')}。",
            f"- 模型变化：{multi.get('model_change')}。",
        ])
    if "government_memo" in result:
        lines.extend([
            "",
            "### 给 Greek government 的审批备忘录",
            str(result["government_memo"]),
        ])
    if "community_dynamics_model" in result:
        model = result["community_dynamics_model"]
        lines.extend([
            "",
            "### 植物群落动态模型",
            f"- 模型：{model.get('model')}。",
            f"- 模拟年数：{model.get('simulation_years')}。",
            f"- 方程：`{model.get('equation')}`。",
            "",
            "#### 状态变量",
            "",
        ])
        lines.extend([f"- `{item}`" for item in model.get("state_variables", [])])
        lines.extend(["", "#### 题面要求映射", ""])
        lines.extend([f"- {item}" for item in model.get("official_prompt_requirements", [])])
    if "biodiversity_threshold" in result:
        threshold = result["biodiversity_threshold"]
        lines.extend([
            "",
            "### 生物多样性阈值",
            f"- 官方观察：{threshold.get('official_observation')}。",
            f"- 估计受益最少物种数：{threshold.get('estimated_min_species_for_benefit')}。",
            f"- 规则：{threshold.get('benefit_rule')}。",
            f"- 单物种可行性得分：{threshold.get('single_species_viability_score')}。",
            "",
            "#### 物种数敏感性",
            "",
        ])
        lines.extend(markdown_table(threshold.get("species_count_results", [])[:12], ["species_count", "mean_biomass_last20", "mean_persistence_ratio", "viability_score", "improvement_over_single_species_pct"]))
    if "species_type_impact" in result:
        species_type = result["species_type_impact"]
        lines.extend([
            "",
            "### 物种类型影响",
            f"- 模型：{species_type.get('model')}。",
            f"- 解释：{species_type.get('interpretation')}。",
            "",
        ])
        lines.extend(markdown_table(species_type.get("guild_comparison", []), ["guild_mix", "mean_biomass_last20", "mean_persistence_ratio", "drought_generation_biomass", "viability_score"]))
    if "drought_frequency_impact" in result:
        drought = result["drought_frequency_impact"]
        lines.extend([
            "",
            "### 干旱频率和严重度敏感性",
            f"- 低频干旱解释：{drought.get('less_frequent_note')}。",
            f"- 未来天气解释：{drought.get('future_weather_note')}。",
            "",
        ])
        lines.extend(markdown_table(drought.get("frequency_scenarios", []), ["scenario", "interval_years", "severity_multiplier", "mean_biomass_last20", "viability_score"]))
    if "external_stressors" in result:
        stressors = result["external_stressors"]
        lines.extend([
            "",
            "### 污染和栖息地减少",
            f"- 影响摘要：{stressors.get('impact_summary')}。",
            "",
        ])
        lines.extend(markdown_table(stressors.get("stress_scenarios", []), ["scenario", "pollution_load", "habitat_quality", "mean_biomass_last20", "viability_score"]))
    if "long_term_viability_strategy" in result:
        strategy = result["long_term_viability_strategy"]
        lines.extend([
            "",
            "### 长期可行性策略",
            f"- 推荐最少物种数：{strategy.get('recommended_min_species')}。",
            f"- 大环境影响：{strategy.get('environmental_impact')}。",
            "",
            "#### 管理行动",
            "",
        ])
        lines.extend([f"- {item}" for item in strategy.get("actions", [])])
        lines.extend(["", "#### 策略前沿", ""])
        lines.extend(markdown_table(strategy.get("frontier", []), ["species_count", "baseline_viability_score", "restoration_viability_score", "restoration_gain_pct"]))
    if "environment_memo" in result:
        lines.extend([
            "",
            "### 大环境管理备忘录",
            str(result["environment_memo"]),
        ])
    if "zoning_policy_model" in result:
        zoning = result["zoning_policy_model"]
        lines.extend([
            "",
            "### Maasai Mara 分区政策模型",
            f"- 模型：{zoning.get('model')}。",
            f"- 政策原则：{zoning.get('policy_principle')}。",
            "",
            "#### 分区评分",
            "",
        ])
        lines.extend(markdown_table(zoning.get("zones", []), ["zone", "conservation_priority", "community_priority", "balance_need", "management_intensity", "recommended_policy"]))
    if "policy_evaluation" in result:
        policy = result["policy_evaluation"]
        best = policy.get("best_policy", {})
        lines.extend([
            "",
            "### 政策与管理策略排名",
            f"- 方法：{policy.get('methodology')}。",
            f"- 最优政策：{best.get('policy')}；综合得分：{best.get('composite_score')}。",
            "",
            "#### 政策包排名",
            "",
        ])
        lines.extend(markdown_table(policy.get("ranked_policies", []), ["policy", "ecological_score", "resident_score", "economic_score", "governance_feasibility", "implementation_cost_index", "composite_score"]))
    if "interaction_model" in result:
        interaction = result["interaction_model"]
        lines.extend([
            "",
            "### 人兽互动长期投影",
            f"- 模型：{interaction.get('model')}。",
            f"- 选定政策：{interaction.get('selected_policy')}。",
            f"- 确定性说明：{interaction.get('certainty_note')}。",
            "",
            "#### 20 年投影样本",
            "",
        ])
        projection = interaction.get("interaction_projection", [])
        lines.extend(markdown_table(projection[:5] + projection[-5:], ["year", "conflict_index", "wildlife_population_index", "resident_acceptance_index", "implementation_maturity"]))
    if "economic_impact_model" in result:
        economics = result["economic_impact_model"]
        lines.extend([
            "",
            "### 经济影响与社区收益",
            f"- 模型：{economics.get('model')}。",
            f"- 第 20 年净社区收益指数：{economics.get('year20_net_community_benefit_index')}。",
            f"- 解释：{economics.get('economic_interpretation')}。",
            "",
            "#### 收益投影样本",
            "",
        ])
        projection = economics.get("community_revenue_projection", [])
        lines.extend(markdown_table(projection[:5] + projection[-5:], ["year", "tourism_revenue_index", "community_revenue_share", "community_revenue_index", "local_opportunity_cost_index", "net_community_benefit_index"]))
    if "long_term_outcomes" in result:
        outcome = result["long_term_outcomes"]
        lines.extend([
            "",
            "### 长期趋势与风险",
            f"- 投影年限：{outcome.get('projection_years')}。",
            f"- 第 20 年 conflict index：{outcome.get('year20_conflict_index')}。",
            f"- 第 20 年 wildlife index：{outcome.get('year20_wildlife_population_index')}。",
            f"- 第 20 年 resident acceptance：{outcome.get('year20_resident_acceptance_index')}。",
            f"- 长期结果得分：{outcome.get('long_term_outcome_score')}。",
            "",
            "#### 风险登记",
            "",
        ])
        lines.extend([f"- {item}" for item in outcome.get("risk_register", [])])
        lines.extend(["", "#### 监测指标", ""])
        lines.extend([f"- {item}" for item in outcome.get("monitoring_indicators", [])])
    if "transferability" in result:
        transfer = result["transferability"]
        lines.extend([
            "",
            "### 迁移到其他保护区",
            f"- 适用对象：{transfer.get('target_area_type')}。",
            f"- 限制：{transfer.get('limits')}。",
            "",
            "#### 迁移步骤",
            "",
        ])
        lines.extend([f"- {item}" for item in transfer.get("adaptation_steps", [])])
    if "committee_report" in result:
        lines.extend([
            "",
            "### Kenyan Tourism and Wildlife Committee 非技术报告",
            str(result["committee_report"]),
        ])
    if "sdg_network_model" in result:
        sdg = result["sdg_network_model"]
        lines.extend([
            "",
            "### SDG 关系网络",
            f"- 模型：{sdg.get('model')}。",
            f"- 节点数：{len(sdg.get('nodes', []))}。",
            f"- 边数：{len(sdg.get('sdg_network_edges', []))}。",
            f"- 负向权衡边数：{sdg.get('negative_tradeoff_count')}。",
            "",
            "#### 节点",
            "",
        ])
        lines.extend(markdown_table(sdg.get("nodes", []), ["sdg", "name", "category"]))
        lines.extend(["", "#### 关系边样本", ""])
        lines.extend(markdown_table(sdg.get("sdg_network_edges", [])[:14], ["source_sdg", "target_sdg", "weight", "sign", "relationship"]))
    if "priority_model" in result:
        priority = result["priority_model"]
        plan = priority.get("ten_year_plan", {})
        lines.extend([
            "",
            "### UN 优先级与 10 年计划",
            f"- 方法：{priority.get('method')}。",
            f"- 10 年 first-wave priorities：{plan.get('first_wave_priorities')}。",
            f"- 预期网络进展增益：{plan.get('expected_network_progress_gain')}。",
            f"- 评价指标：{plan.get('evaluation_metric')}。",
            "",
            "#### 优先级排序",
            "",
        ])
        lines.extend(markdown_table(priority.get("priority_ranking", [])[:17], ["sdg", "name", "category", "pagerank", "betweenness", "out_strength", "priority_score"]))
    if "achieved_goal_scenario" in result:
        achieved = result["achieved_goal_scenario"]
        new_goal = achieved.get("proposed_new_goal", {})
        lines.extend([
            "",
            "### 达成一个 SDG 后的网络",
            f"- 达成目标：SDG {achieved.get('achieved_goal')}。",
            f"- 情景：{achieved.get('scenario')}。",
            f"- 建议新增目标：SDG {new_goal.get('sdg')} {new_goal.get('name')}；原因：{new_goal.get('reason')}。",
            "",
            "#### 达成后优先级",
            "",
        ])
        lines.extend(markdown_table(achieved.get("resulting_network_priorities", [])[:10], ["sdg", "name", "post_achievement_pagerank"]))
    if "crisis_impact_model" in result:
        crisis = result["crisis_impact_model"]
        lines.extend([
            "",
            "### 危机冲击矩阵",
            f"- 方法：{crisis.get('method')}。",
            f"- 网络视角：{crisis.get('network_perspective')}。",
            "",
        ])
        lines.extend(markdown_table(crisis.get("crisis_impact_matrix", []), ["crisis", "affected_sdgs", "effect_direction", "network_severity_index", "priority_response_sdgs", "risk"]))
    if "organization_transfer" in result:
        transfer = result["organization_transfer"]
        lines.extend([
            "",
            "### 迁移到公司和组织目标管理",
            f"- 模型：{transfer.get('model')}。",
            "",
            "#### 迁移步骤",
            "",
        ])
        lines.extend([f"- {item}" for item in transfer.get("adaptation_steps", [])])
        lines.extend(["", "#### 使用场景", ""])
        lines.extend([f"- {item}" for item in transfer.get("use_cases", [])])
    if "risk_metric" in result:
        metric = result["risk_metric"].get("light_pollution_risk_metric", {})
        lines.extend([
            "",
            "### 光污染风险指标",
            f"- 量表：{metric.get('scale')}。",
            f"- 公式：`{metric.get('formula')}`。",
            f"- 人类与非人类平衡：{metric.get('human_and_nonhuman_balance')}。",
            "",
            "#### 指标组件",
            "",
        ])
        lines.extend([f"- {item}" for item in metric.get("components", [])])
    if "location_assessment" in result:
        assessment = result["location_assessment"]
        lines.extend([
            "",
            "### 四类地点风险评估",
            f"- 解释：{assessment.get('interpretation')}。",
            "",
        ])
        lines.extend(markdown_table(assessment.get("locations", []), ["location_type", "example_location", "light_pollution_risk_score", "risk_level", "sky_glow_component", "ecological_component", "human_health_component"]))
    if "intervention_model" in result:
        intervention = result["intervention_model"]
        lines.extend([
            "",
            "### 干预策略评分",
            "",
        ])
        lines.extend(markdown_table(intervention.get("intervention_strategy_scores", []), ["strategy", "sky_glow_reduction", "trespass_reduction", "clutter_reduction", "safety_penalty", "cost_index", "strategy_value_score"]))
        lines.extend(["", "#### 一般影响", ""])
        lines.extend([f"- {item}" for item in intervention.get("general_impacts", [])])
    if "strategy_selection" in result:
        selection = result["strategy_selection"]
        lines.extend([
            "",
            "### 两类地点最优干预选择",
            f"- 选择规则：{selection.get('selection_rule')}。",
            "",
        ])
        lines.extend(markdown_table(selection.get("selected_locations", []), ["location_type", "strategy", "risk_before", "risk_after", "risk_reduction_points", "specific_actions"]))
    if "promotion_flyer" in result:
        lines.extend([
            "",
            "### 一页宣传 Flyer",
            str(result["promotion_flyer"]),
        ])
    if "sex_ratio_model" in result:
        sex_ratio = result["sex_ratio_model"]
        lines.extend([
            "",
            "### 七鳃鳗资源-性别比模型",
            f"- 模型：{sex_ratio.get('model')}。",
            f"- 公式：`{sex_ratio.get('formula')}`。",
            "",
            "#### 响应曲线样本",
            "",
        ])
        lines.extend(markdown_table(sex_ratio.get("response_curve", [])[:8], ["resource_index", "male_ratio", "female_ratio", "mating_success_index"]))
    if "ecosystem_impact" in result:
        impact = result["ecosystem_impact"]
        reduction = impact.get("lamprey_reduction_effect", {})
        lines.extend([
            "",
            "### 更大生态系统影响",
            f"- 模型：{impact.get('model')}。",
            "",
            "#### 情景比较",
            "",
        ])
        lines.extend(markdown_table(impact.get("scenario_comparison", [])[:8], ["scenario", "mean_resource_index", "mean_male_ratio", "mean_lamprey", "mean_host_fish", "ecosystem_stability_score"]))
        lines.extend([
            "",
            "#### 七鳃鳗减少影响",
            f"- 解释：{reduction.get('interpretation')}。",
            f"- 七鳃鳗均值：{reduction.get('mean_lamprey')}；宿主鱼均值：{reduction.get('mean_host_fish')}。",
        ])
    if "lamprey_population_tradeoffs" in result:
        tradeoff = result["lamprey_population_tradeoffs"]
        lines.extend([
            "",
            "### 七鳃鳗种群优缺点",
            f"- 低食物雄性比例：{tradeoff.get('low_food', {}).get('male_ratio')}。",
            f"- 高食物雄性比例：{tradeoff.get('high_food', {}).get('male_ratio')}。",
            "",
            "#### 优点",
        ])
        lines.extend([f"- {item}" for item in tradeoff.get("advantages", [])])
        lines.extend(["", "#### 缺点"])
        lines.extend([f"- {item}" for item in tradeoff.get("disadvantages", [])])
    if "ecosystem_stability" in result:
        stability = result["ecosystem_stability"]
        lines.extend([
            "",
            "### 生态系统稳定性",
            f"- 自适应 vs 固定性别比稳定性差值：{stability.get('adaptive_vs_fixed_stability_gain')}。",
            "",
            "#### 稳定性最高网格",
            "",
        ])
        lines.extend(markdown_table(stability.get("surface_best_cases", [])[:8], ["resource_index", "lamprey_reduction_pressure", "mean_male_ratio", "mean_lamprey", "mean_host_fish", "ecosystem_stability_score"]))
    if "parasite_and_other_species_effects" in result:
        other = result["parasite_and_other_species_effects"]
        lines.extend([
            "",
            "### 对寄生虫和其他物种的影响",
            f"- 权衡：{other.get('tradeoff')}。",
            "",
        ])
        lines.extend(markdown_table(other.get("beneficiaries", []), ["species_group", "condition"]))
    if "food_web_model" in result:
        food_web = result["food_web_model"]
        lines.extend([
            "",
            "### 农业生态食物网",
            "- 状态变量：" + ", ".join(food_web.get("state_variables", [])),
            f"- 节点数：{len(food_web.get('nodes', []))}。",
            f"- 食物网/影响边数：{len(food_web.get('food_web_edges', []))}。",
            "",
            "#### 关键食物网边",
            "",
        ])
        lines.extend(markdown_table(food_web.get("food_web_edges", [])[:12], ["source", "target", "interaction", "weight"]))
    if "seasonal_dynamics" in result:
        seasonal = result["seasonal_dynamics"]
        lines.extend([
            "",
            "### 季节性系统动力学",
            f"- 模拟长度：{seasonal.get('months')} 个月。",
            f"- 时间步长：{seasonal.get('time_step')}。",
            f"- 季节函数：`{seasonal.get('season_function')}`。",
            f"- 收获月份 mod 12：{seasonal.get('harvest_months_mod_12')}。",
        ])
    if "natural_processes" in result:
        natural = result["natural_processes"]
        lines.extend([
            "",
            "### 自然过程与当前生态系统",
            f"- 模型：{natural.get('model')}。",
            f"- 解释：{natural.get('interpretation')}。",
            "",
            "#### 新清理农田基线",
            "",
        ])
        lines.extend(markdown_table([natural.get("newly_cleared_baseline", {})], ["scenario", "producer_stability", "consumer_stability", "biodiversity_index", "pest_pressure", "crop_yield_index", "ecosystem_stability_score"]))
    if "species_reemergence" in result:
        species = result["species_reemergence"]
        lines.extend([
            "",
            "### 物种重新出现",
            f"- 影响摘要：{species.get('impact_summary')}。",
            "",
            "#### 加入物种",
            "",
        ])
        lines.extend(markdown_table(species.get("species_added", []), ["species", "role", "expected_effect"]))
    if "herbicide_removal" in result:
        herbicide = result["herbicide_removal"]
        lines.extend([
            "",
            "### 去除除草剂与再平衡",
            f"- 生产者稳定性：{herbicide.get('producer_stability_after_removal')}。",
            f"- 消费者稳定性：{herbicide.get('consumer_stability_after_removal')}。",
            f"- 害虫压力：{herbicide.get('pest_pressure_after_removal')}。",
            f"- 解释：{herbicide.get('interpretation')}。",
        ])
    if "organic_scenarios" in result:
        organic = result["organic_scenarios"]
        lines.extend([
            "",
            "### 有机农业情景比较",
            f"- 方法：{organic.get('method')}。",
            f"- 推荐过渡：{organic.get('recommended_transition')}。",
            f"- 理由：{organic.get('reason')}。",
            "",
            "#### 情景排序",
            "",
        ])
        lines.extend(markdown_table(organic.get("scenario_rankings", [])[:8], ["scenario", "crop_yield_index", "pest_pressure", "biodiversity_index", "ecosystem_stability_score", "net_margin_index", "sustainability_score"]))
    if "farmer_letter" in result:
        lines.extend([
            "",
            "### 给农民的一页信",
            str(result["farmer_letter"]),
        ])
    if "policy_advice" in result:
        advice = result["policy_advice"]
        lines.extend([
            "",
            "### 策略建议与政策激励",
            "",
            "#### 推荐策略",
            "",
        ])
        lines.extend([f"- {item}" for item in advice.get("recommended_strategy", [])])
        lines.extend(["", "#### 政策激励", ""])
        lines.extend([f"- {item}" for item in advice.get("policy_incentives", [])])
    if "cybercrime_distribution" in result:
        cyber = result["cybercrime_distribution"]
        lines.extend([
            "",
            "### 网络犯罪分布",
            f"- 模型：{cyber.get('model')}。",
            f"- VCDB 样本记录：{cyber.get('records_used')}。",
            f"- 国家数：{cyber.get('country_count')}。",
            f"- 起诉字段说明：{cyber.get('prosecution_note')}。",
            "",
            "#### Top 目标国家",
            "",
        ])
        lines.extend(markdown_table(cyber.get("top_target_countries", [])[:10], ["iso3", "country", "vcdb_incident_count", "share_of_sample", "confirmed_disclosure_count", "dominant_action_type"]))
        lines.extend(["", "#### 主要模式", ""])
        lines.extend([f"- {item}" for item in cyber.get("patterns", [])])
    if "policy_effectiveness" in result:
        policy = result["policy_effectiveness"]
        lines.extend([
            "",
            "### 政策有效性模式",
            f"- 理论：{policy.get('theory')}。",
            f"- 成熟政策国家平均可见事件：{policy.get('mature_policy_mean_incidents')}。",
            f"- 发展中政策国家平均可见事件：{policy.get('developing_policy_mean_incidents')}。",
            "",
            "#### 政策特征矩阵",
            "",
        ])
        lines.extend(markdown_table(policy.get("policy_feature_matrix", [])[:12], ["iso3", "policy_maturity_score", "mandatory_reporting", "incident_response", "international_cooperation", "vcdb_incident_count"]))
        lines.extend(["", "#### 解释模式", ""])
        lines.extend([f"- {item}" for item in policy.get("effectiveness_patterns", [])])
    if "demographic_correlations" in result:
        demo = result["demographic_correlations"]
        lines.extend([
            "",
            "### 人口统计与混杂因素",
            f"- 面板国家数：{demo.get('panel_countries')}。",
            f"- 混杂警告：{demo.get('confounding_warning')}。",
            "",
            "#### 相关性表",
            "",
        ])
        lines.extend(markdown_table(demo.get("correlations", []), ["variable", "correlation_with_vcdb_incident_count", "usable_countries", "interpretation"]))
    if "leader_memo" in result:
        lines.extend([
            "",
            "### ITU 峰会领导人备忘录",
            str(result["leader_memo"]),
        ])
    if "limitations" in result:
        limits = result["limitations"]
        lines.extend([
            "",
            "### 数据质量限制",
            f"- 样本记录数：{limits.get('sample_record_count')}。",
            f"- 建议验证：{limits.get('recommended_validation')}。",
        ])
        lines.extend([f"- {item}" for item in limits.get("data_quality_concerns", [])])
    if "sustainability_model" in result:
        tourism = result["sustainability_model"]
        lines.extend([
            "",
            "### 朱诺可持续旅游模型",
            f"- 目标：{tourism['objective']}。",
            "",
            "#### 基线",
            "",
        ])
        lines.extend(markdown_table([tourism["baseline"]], ["annual_visitors", "visitors_per_resident", "total_revenue_usd", "hidden_cost_usd", "sustainability_score"]))
        lines.extend(["", "#### 推荐政策", ""])
        lines.extend(markdown_table([tourism["optimal_policy"]], ["daily_cap", "visitor_fee_usd", "conservation_share", "annual_visitors", "total_revenue_usd", "resident_acceptance_index", "environment_index", "sustainability_score"]))
        lines.extend(["", "#### 收入支出反馈", ""])
        for key, value in tourism.get("expenditure_plan", {}).items():
            lines.append(f"- {key}：{value}")
    if "sensitivity_analysis" in result:
        sensitivity = result["sensitivity_analysis"]
        lines.extend([
            "",
            "### 敏感性分析",
            f"- 方法：{sensitivity['method']}。",
            "",
        ])
        lines.extend(markdown_table(sensitivity.get("top_factors", []), ["factor", "correlation_with_score", "score_change_from_p10_to_p90", "interpretation"]))
    if "destination_adaptation" in result:
        adaptation = result["destination_adaptation"]
        lines.extend([
            "",
            "### 迁移到其他过度旅游目的地",
            f"- 目的地：{adaptation['destination']}。",
            f"- 选择理由：{adaptation['reason_for_choice']}",
            "",
            "#### 迁移后的约束",
            "",
        ])
        adapted_rows = [{"constraint": key, "value": value} for key, value in adaptation.get("adapted_constraints", {}).items()]
        lines.extend(markdown_table(adapted_rows, ["constraint", "value"]))
        lines.extend(["", "#### 政策迁移", ""])
        lines.extend([f"- {item}" for item in adaptation.get("policy_transfer", [])])
    if "tourism_board_memo" in result:
        lines.extend([
            "",
            "### Juneau Tourism Board 备忘录",
            str(result["tourism_board_memo"]),
        ])
    if QUESTION["problem_id"] == "2015-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数人力资本网络实验；COMAP 没有提供员工级 CSV/XLSX 附件，因此只使用 PDF 中 370 个岗位、85% 填补率、18% 年流失率、8%-10% 主动招聘范围和岗位层级表。",
            "- 流失影响权重、招聘吞吐折减和内部晋升池比例是显式确定性假设，不是员工观测数据；正式论文应补充员工级组织图、绩效评价、离职历史、招聘流水和匿名关系网络校准。",
        ])
    elif QUESTION["problem_id"] == "2015-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 PDF + World Bank Data 实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面明确列出 World Bank Data 作为可能资源，因此本工作流缓存 Nepal 官方 World Bank API 指标。",
            "- 项目成本和干预效果是显式规划假设，不是历史因果估计；正式论文应补充本地项目成本、气候灾害、治理稳定性、区域贫困和更多国家对比数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数热传导/混合实验；COMAP 没有提供传感器 CSV/XLSX 附件，因此只使用 PDF 中单水龙头、无循环加热、恒定细流、溢流排水、空间-时间温度和泡泡浴等约束。",
            "- 浴缸尺寸、热损失、人体体积/温度、混合强度和泡泡浴隔热系数是显式物理情景假设，不是实测浴缸数据；正式论文应补充浴缸几何和多点温度传感器数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数商业筛选实验；COMAP 没有提供轨道碎片 CSV/XLSX 附件，因此只使用 PDF 中 500,000+ tracked debris、2009 collision 和候选移除方法等约束。",
            "- 成本、收入、技术风险、监管风险、移除能力和协同效应是显式商业情景假设，不是实测轨道/合同数据；正式论文应补充公开 TLE/Space-Track、任务成本、保险费率和监管许可数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数信息网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中五个历史时期、2050 预测要求和信息价值/偏见/来源/拓扑强度等任务约束。",
            "- media access、transmission speed、network connectivity、gatekeeping filter、channel capacity 和观点影响权重是显式归一化假设，不是新闻传播观测数据；正式论文应补充报纸发行、广播/电视普及、互联网使用、智能手机渗透和平台转发级联数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-F":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数难民政策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 715,000+ 申请、Hungary 1,450/100k、32% 批准率、六条路线、最热门/最危险路线、NGO、外生事件和 10 倍扩展等约束。",
            "- 路线安全、可达性、临时容量、日处理能力、资源包和 NGO 增益是显式规划假设，不是边境观测数据；正式论文应补充 UNHCR/IOM/FRONTEX 路线流量、死亡风险、接收容量、庇护审批、公共卫生和本地融合数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 PDF + World Bank Data 水资源实验；COMAP 没有提供独立 CSV/XLSX 附件，但题面要求使用水资源数据源分析缺水，本工作流缓存 Jordan World Bank 官方指标。",
            "- 干预效果、成本和年度降压百分点是显式规划假设，不是历史因果估计；正式论文应补充流域水文、月度供水、地下水、漏损、价格和项目成本数据校准。",
        ])
    elif QUESTION["problem_id"] == "2016-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Goodgrant Scorecard/IPEDS 附件实验；只使用 `ProblemCDATA.zip` 解压出的三份 Excel 和 IPEDS 变量 PDF，不使用随机造数。",
            "- ROI 是慈善投资组合评分，不是严格因果效应；正式论文应补充学校项目执行计划、边际资金吸收能力、地区公平约束、重复资助排除和后续年度 Scorecard 更新。",
        ])
    elif QUESTION["problem_id"] == "2017-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。",
            "- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。",
        ])
    elif QUESTION["problem_id"] == "2017-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Cooperate and Navigate 交通 workbook 实验；只使用 `2017_MCM_Problem_C_Data.xlsx` 的 `parsed mile posts` 与 `definitions` 工作表，不使用随机造数。",
            "- 峰小时占比、每车道容量、AV 容量倍率和 BPR 速度函数是显式交通流假设，用于把官方 ADT/车道数转换成可比较性能指标；正式论文应补充小时级探测器速度、OD 需求和实际 AV 行为数据校准。",
        ])
    elif QUESTION["problem_id"] == "2017-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Airport Security Checkpoint workbook 实验；只使用 `2017_ICM_Problem_D_Data.xlsx` 的 Sheet1 到达和过程样本，不使用随机造数。",
            "- 排队仿真是按官方样本确定性回放；PreCheck 加速、取物时间归一化、文化/旅客风格乘数和流程修改均为显式假设，正式论文应补充小时级真实排队、成本、安检失败率和多机场数据校准。",
        ])
    elif QUESTION["problem_id"] == "2018-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Energy Production SEDS workbook 实验；只使用 `2018_MCM_Problem_C_Data.xlsx` 的 `seseds` 与 `msncodes` 工作表，不使用随机造数或外部能源观测。",
            "- 2025/2050 结果是题目要求的 no-policy baseline 线性外推，不是未来真实观测；compact target 和政策行动是基于官方历史数据的规划建议，正式论文应补充最新 EIA/州能源政策数据做情景校准。",
        ])
    elif QUESTION["problem_id"] == "2019-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 The Opioid Crisis Excel/ACS CSV 附件实验；只使用 MCM_NFLIS_Data.xlsx 与 2010-2016 ACS DP02 官方附件，不使用随机造数。",
            "- 官方 NFLIS workbook 实际包含 KY/OH/PA/VA/WV 五州记录，本脚本不补造题面文字中提到但文件缺失的 Tennessee；ACS 相关性是描述性，不等同于成瘾或流行传播的因果解释。",
        ])
    elif QUESTION["problem_id"] == "2020-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数 Moving North 鱼群迁移实验；本地官方 PDF 文字层不完整，题面要求由 COMAP 2020 problems 官方页面核对，归档仍指向本地官方 PDF 资产。",
            "- COMAP 没有提供海温、鱼群调查或船队成本附件，因此 thermal shift、fleet range、territorial threshold 和策略得分均为显式确定性情景输入；正式论文应补充 ICES/NOAA/UK fisheries 海温和渔业观测校准。",
        ])
    elif QUESTION["problem_id"] == "2020-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数沙堡基础形状实验；COMAP 没有提供波浪水槽、粒径或潮位附件，因此只使用 PDF 中同海滩、同沙量、同水沙比例、降雨和杂志文章等题面约束。",
            "- 形状、比例、降雨和策略参数是显式确定性物理情景输入，不是实测冲刷数据；正式论文应补充沙粒级配、含水率、压实度、潮汐、波速和降雨入渗校准。",
        ])
    elif QUESTION["problem_id"] == "2020-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 A Wealth of Data Amazon TSV 附件实验；只使用 `Problem Data- A Wealth of Data` 官方 ZIP 内 hair_dryer.tsv、microwave.tsv 和 pacifier.tsv。",
            "- 描述词 lift 是透明关键词规则，不是深度语义模型；结果描述历史竞品评论，不是 Sunshine Company 新品的因果销售预测。",
        ])
    elif QUESTION["problem_id"] == "2020-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Teaming Strategies CSV 附件实验；只使用 matches.csv、passingevents.csv、fullevents.csv 和 README.txt，不使用随机造数。",
            "- 球队成功模型使用前 30 场训练、后 8 场留出，只说明官方赛季样本内的协作指标可解释性；正式论文应补充更多赛季、对手强度、球员伤停和战术视频标注。",
        ])
    elif QUESTION["problem_id"] == "2020-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数塑料废弃物规划实验；COMAP 没有提供国家塑料流量表，因此只使用 PDF 中 9% recycling、4-12 million tons ocean input、2050 more plastic than fish 和公平治理等题面约束。",
            "- 区域废弃物流、政策减量率和公平责任分数是显式确定性情景输入，不是 UN/OECD/国家废弃物清单；正式论文应补充塑料生产、贸易、回收、泄漏、替代品和产业影响数据校准。",
        ])
    elif QUESTION["problem_id"] == "2020-F":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数气候迁移与文化保护实验；COMAP 没有提供岛屿高程、人口或迁移附件，因此只使用 PDF 中 Maldives、Tuvalu、Kiribati、Marshall Islands、EDP、人权、文化保护和 UN 响应等题面约束。",
            "- 海平面、人口、文化风险和政策得分是显式确定性情景输入，不是 IPCC/UNHCR/国家人口普查或社区文化档案；正式论文应补充地理、人口、法律、主权和社区主导文化数据校准。",
        ])
    elif QUESTION["problem_id"] == "2021-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数真菌分解实验；COMAP 没有提供数值附件，因此只使用 PDF 中 growth rate、moisture tolerance、五类环境、环境波动和教材文章等题面约束。",
            "- 真菌 trait、环境湿度和竞争参数是显式确定性情景输入，不是原始实验数据；正式论文应补充 PNAS 原文 isolate measurements、温湿度记录和凋落物质量损失校准。",
        ])
    elif QUESTION["problem_id"] == "2021-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数野火无人机采购实验；COMAP 没有提供 GIS/事件附件，因此只使用 PDF 中 AUD 10000、30km、20m/s、2.5h、1.75h、5W、10W、20km 等题面参数。",
            "- 火场等级、地形复杂度和年度频率是显式确定性规划情景，不是 CFA 事件库；正式论文应补充火点 GIS、地形遮挡、风烟、飞行管制和人员部署数据校准。",
        ])
    elif QUESTION["problem_id"] == "2021-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Hornets Excel 附件实验；只使用 sightings workbook、image mapping workbook 和官方 PDF，不下载题面外部大图包，也不使用随机造数。",
            "- Positive ID 只有 14 条，因此分类留出指标不应被解释成根除证明；正式论文应补充主动诱捕、搜巢、季节性监测和实验室复核记录。",
        ])
    elif QUESTION["problem_id"] == "2021-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。",
            "- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。",
        ])
    elif QUESTION["problem_id"] == "2021-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数食物系统再优化实验；COMAP 没有提供国家食物系统 CSV/XLSX 附件，因此只使用 PDF 中 hunger、环境足迹、效率、利润、可持续、公平、发达/发展中国家和可扩展性等题面约束。",
            "- 国家分数、政策收益、成本和 15 年路线图是显式确定性规划输入，不是 FAO/World Bank/国家营养监测实测数据；正式论文应补充粮食安全、营养、生产者收入、排放、水足迹和治理能力数据校准。",
        ])
    elif QUESTION["problem_id"] == "2021-F":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数高等教育系统健康度实验；COMAP 没有提供国家高教 workbook，因此只使用 PDF 中 system health、sustainable system、多国比较、政策时间线和现实影响等题面约束。",
            "- 国家健康维度分、政策增益和利益相关者影响是显式确定性规划输入，不是 UNESCO/OECD/国家教育财政或就业记录；正式论文应补充学费、债务、完成率、就业、科研、国际学生和财政稳定性数据校准。",
        ])
    elif QUESTION["problem_id"] == "2022-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数骑行功率实验；COMAP 没有提供功率计、GPS 或天气附件，因此只使用 PDF 中两类骑手、不同性别、东京/弗兰德斯/自定义路线、天气敏感性、功率偏差和六人团队计时赛等题面约束。",
            "- 骑手 profile、赛道分段、CdA、滚阻和风暴露系数是显式确定性场景输入，不是实测遥测；正式论文应补充真实路线 GPX、功率历史、气象预报和车手疲劳校准。",
        ])
    elif QUESTION["problem_id"] == "2022-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数水库-水电分配实验；COMAP 没有提供水库运行、州需求或机组曲线附件，因此只使用 PDF 中 Powell/Mead 串联、五州、Mexico/Gulf flow、供需变化和不得依赖历史协议等题面约束。",
            "- 水位、库容曲线、部门需水和水电系数是显式确定性场景输入，不是 BOR/电网实测数据；正式论文应补充官方水文、用水、电力、生态和跨境流量数据校准。",
        ])
    elif QUESTION["problem_id"] == "2022-C":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Trading Strategies CSV 附件实验；只使用 LBMA-GOLD.csv 和 BCHAIN-MKPRU.csv 两个 COMAP 文件，不使用随机造数或外部行情。",
            "- 候选策略最优性只在脚本中列出的透明因果规则族内成立；正式论文应扩展到风险约束、效用函数、滚动交叉验证和更严格的在线学习证明。",
        ])
    elif QUESTION["problem_id"] == "2022-P01":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数 D&A 成熟度实验；题面明确 ICM Corporation 不能分享内部人员、技术、流程或数据细节，因此只使用 people/technology/process、海港、卡车公司迁移和客户信等题面约束。",
            "- KPI 当前分、目标分和路线图收益是显式 rubric 输入，不是 ICM 内部审计记录；正式咨询应补充访谈、系统日志、数据目录覆盖率、质量事件和客户满意度调查校准。",
        ])
    elif QUESTION["problem_id"] == "2022-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数森林固碳实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 100 年评估、林产品生命周期、多价值决策和延长 10 年采伐间隔等题面约束。",
            "- 森林样例、产品半衰期、决策权重和管理计划参数是显式确定性情景输入，不是地块清查数据；正式论文应补充当地森林库存、土壤碳、产品流向、扰动风险和社区调查校准。",
        ])
    elif QUESTION["problem_id"] == "2023-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数植物群落动态实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中单物种风险、四个及以上物种受益、不规则干旱、污染和栖息地减少等题面约束。",
            "- 物种性状、干旱时间表、污染负荷和栖息地质量是显式确定性情景参数，不是野外观测；正式论文应补充样方长期监测、降水、土壤、污染和群落功能性状数据校准。",
        ])
    elif QUESTION["problem_id"] == "2023-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数保护区管理实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 Maasai Mara、Wildlife Conservation and Management Act 2013、2020 修订、分区管理、社区利益、人兽冲突和两页委员会报告等题面约束。",
            "- 分区评分、政策收益、冲突变化率、社区收益份额和 20 年投影系数是显式确定性情景参数，不是 Maasai Mara 实地监测数据；正式论文应补充保护区 GIS、野生动物迁徙、冲突事件、旅游收入、社区调查和治理预算数据校准。",
        ])
    elif QUESTION["problem_id"] == "2023-D":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数 SDG 网络实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 17 个 SDGs、网络关系、10 年优先级、达成一个目标后的网络、危机冲击和组织迁移等题面约束。",
            "- 边权、直接需求指数、危机乘数和新增目标情景是显式确定性建模假设，不是 UN 指标数据库观测；正式论文应补充 UN SDG indicator panel、国家分组、资金约束和专家打分校准。",
        ])
    elif QUESTION["problem_id"] == "2023-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数光污染风险实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 light trespass、over-illumination、light clutter、protected/rural/suburban/urban 四类地点、三类干预和 flyer 等题面约束。",
            "- 地点画像、权重、干预降幅、成本和可行性是显式确定性情景参数，不是实地照度、卫星夜光或事故/生态监测数据；正式论文应补充 VIIRS 夜光、地面照度、交通事故、犯罪、睡眠健康和物种迁徙数据校准。",
        ])
    elif QUESTION["problem_id"] == "2023-C-Wordle":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方 Wordle 附件数据基线实验，适合做论文骨架、结果表和图，不应把词属性相关性解释为严格因果。",
            "- 官方数据来自 Twitter 报告样本，不等同于全体玩家；预测 2023-03-01 属于外推，正式论文应补充新日期真实结果或滚动更新检验。",
        ])
    elif QUESTION["problem_id"] == "2023-C-Boats":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方帆船 Excel 基线实验，适合做论文骨架、结果表和图；随机森林和 OLS 区域效应都不应被解释为严格因果。",
            "- COMAP 官方数据不含香港记录；香港部分使用带 URL 的补充挂牌样本做情景比较，正式论文应继续扩充香港本地成交/挂牌样本并记录抓取日期。",
        ])
    elif QUESTION["problem_id"] == "2025-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是外部数据回归。",
            "- 价格弹性、隐性成本和支出反馈是显式建模假设，正式论文应通过城市公开预算、港口客流和居民调查进一步校准。",
        ])
    elif QUESTION["problem_id"] == "2025-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数和测量工作流实验，适合处理没有独立 CSV/XLSX 附件的 MCM 题；它不是随机造数，也不是虚构真实观测。",
            "- `worked_example_assumptions` 只是展示考古队填完非破坏测量表后如何反演；正式论文应把现场测量值替换进模板，并对材料磨损系数做来源校准。",
        ])
    elif QUESTION["problem_id"] == "2025-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数生态系统实验，适合处理没有独立 CSV/XLSX 附件的 ICM 题；它不是随机造数，也不是声称拥有真实农场观测。",
            "- 情景参数、经济指数和系统动力学系数是显式假设；正式论文应补充本地作物、害虫监测、土壤检测、投入成本和有机溢价数据进行校准。",
        ])
    elif QUESTION["problem_id"] == "2025-F":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面 + 题面引用公开源实验；COMAP 没有提供数值附件，因此本脚本缓存 VCDB/World Bank 数据并保留来源 URL。",
            "- VCDB 是公开报告事件样本，不是全球网络犯罪全集；政策特征矩阵是透明 rubric，不应解释为严格因果估计。",
        ])
    elif QUESTION["problem_id"] == "2024-A":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数系统动力学实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 78%/56% 两个性别比例端点。",
            "- 差分方程系数是显式建模假设，用于解释机制和生成论文图表；正式论文应补充本地七鳃鳗、宿主鱼和食物资源监测数据校准。",
        ])
    elif QUESTION["problem_id"] == "2024-B":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数搜索救援实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中的任务约束和显式确定性预案参数。",
            "- 洋流、装备覆盖率和准备时间是可替换的场景参数，不是事故观测数据；正式论文应接入作业海区实时流场、测深、声学设备规格和演练记录校准。",
        ])
    elif QUESTION["problem_id"] == "2024-E":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数保险与保护决策实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 $1T、1000 起事件、115%、30-60%、57% 等宏观参数。",
            "- 两个地区、建址和地标保护行是显式确定性演示情景，不是保险公司真实承保组合；正式论文应补充当地灾害频率、赔付率、建筑清单、工程造价和社区调查数据校准。",
        ])
    elif QUESTION["problem_id"] == "2024-F":
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方题面参数非法野生动物贸易项目设计实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中 26.5B USD/year、第四大非法贸易和 5 年项目要求。",
            "- 客户评分、干预减幅、预算和达标概率是显式确定性项目情景，不是执法数据库观测；正式论文应补充 seizure records、CITES/UNODC 路线资料、平台下架数据和地方伙伴调研校准。",
        ])
    else:
        lines.extend([
            "",
            "## 模型限制",
            "- 这是可复现的官方数据基线实验，适合做论文骨架和结果表，不应把随机森林相关性解释为严格因果。",
            "- 对异常国家/代表队名称、教练履历、项目规则变化等，需要在竞赛论文中追加人工核验和敏感性分析。",
        ])
    lines.extend([
        "",
        "## 运行方式",
        f"`{VENV_PYTHON} {Path(__file__).resolve()}`",
        "",
        "## 输出",
        f"- `{RESULT_PATH}`",
        f"- `{REPORT_PATH}`",
        f"- `{ARTIFACT_DIR}`",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not source_outputs_current():
        subprocess.run([str(VENV_PYTHON), str(SOURCE_SOLUTION)], cwd=str(REPO_ROOT), check=True)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    full_result = json.loads(SOURCE_RESULT.read_text(encoding="utf-8"))
    result = filtered_result(full_result)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_question_report(result)
    for source in SOURCE_ARTIFACTS.iterdir():
        if source.is_file():
            shutil.copy2(source, ARTIFACT_DIR / source.name)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
