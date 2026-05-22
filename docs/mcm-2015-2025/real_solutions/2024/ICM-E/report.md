# 2024 ICM-E Sustainability of Property Insurance

## 数据真实性
- 官方来源：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2024/Sustainability of Property Insurance.pdf`。
- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的宏观数字和显式地区/建筑情景假设，不使用随机占位数据。
- 地区和地标行是 deterministic demonstration scenarios，不是保险公司真实组合数据。

## 官方题面数字
- 近期极端天气损失：超过 $1.0T，事件超过 1000 起。
- 2022 年自然灾害索赔相对 30 年平均增加：115%。
- 2040 年保费预计增加区间：30%-60%。
- 全球保障缺口：57%。

## 每问结果
### Q1-Q2 承保条件与何时承担风险
- 模型：deterministic climate-stress underwriting score balancing net catastrophe loss ratio, affordability, mitigation, and insurer capital buffer。
- 规则：{'score': 'higher is more sustainable to underwrite', 'approve_threshold': 0.62, 'decline_threshold': 0.4, 'approve': 'score >= 0.62', 'conditional': '0.40 <= score < 0.62', 'decline': 'score < 0.40'}。
- 网格摘要：{'rows': 180, 'approve_rows': 37, 'conditional_rows': 84, 'decline_rows': 59}。

### Q3 业主可影响的因素
- 基准风险分：0.78。
- 最优行动：elevate utilities and living floor above design flood，行动后风险分：0.5928。

### Q4 两大洲地区演示
- Florida Gulf Coast hurricane-flood corridor（North America）：score=0.4641，decision=conditional underwriting with mitigation, deductible, and reinsurance trigger。
- Bangladesh delta cyclone-flood corridor（Asia）：score=0.1173，decision=decline new underwriting until community-level risk reduction or public-private backstop exists。

### Q5 建址模型
- elevated inland infill：build_score=0.37，build only after site-specific elevation, drainage, and insurance conditions。
- coastal low-lying expansion：build_score=0.11，avoid new construction or relocate growth inland。
- redeveloped floodplain with green buffers：build_score=0.2655，avoid new construction or relocate growth inland。
- wildland-urban edge subdivision：build_score=0.1445，avoid new construction or relocate growth inland。

### Q6-Q7 历史地标保护
- 选择地标：St. Augustine Lighthouse。
- 推荐计划：{'phase_1': '0-12 months: engineering survey, corrosion/wind inspection, emergency shutters, drainage maintenance, and visitor closure triggers', 'phase_2': '1-3 years: foundation drainage, roof and lantern-room hardening, floodproof utilities, and insurance inspection covenant', 'phase_3': '3-7 years: evaluate managed retreat only if erosion and storm-surge triggers exceed the conditional underwriting band', 'cost_proposal_musd': 8.5, 'benefit_cost_ratio': 2.757}。

## 一页社区信核心
Dear community members, our insurance and preservation models recommend protecting St. Augustine Lighthouse in place over the next seven years, beginning with inspections, floodproof utilities, roof and lantern-room hardening, and clear storm-closure triggers. The plan preserves a high-value cultural and tourism asset while keeping future insurance conditional on verified risk reduction.

## 输出产物
- `underwriting_policy_grid.csv`：承保政策网格。
- `regional_risk_comparison.csv`：两大洲地区演示。
- `mitigation_levers.csv`：业主/社区减灾行动。
- `site_build_decisions.csv`：建址决策表。
- `preservation_priority.csv`：保护优先级表。
- `insurance_preservation_frontier.png`：建址-保护权衡图。
