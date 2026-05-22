# 2025 ICM-E Making Room for Agriculture

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2025/2025_ICM_Problem_E.pdf`。
- 本题无官方 CSV/XLSX 附件；代码只使用官方题面结构和显式情景参数，不使用随机生成样本。
- 月度轨迹是确定性系统动力学实验，用来展示模型求解过程和可替换参数接口。

## 食物网模型
- 节点数：11。
- 边数：12。
- 核心机制：作物-害虫-天敌-授粉者-土壤健康-化学压力之间的月度反馈。

## 每问结果

### Q1/Q2 自然过程与当前生态系统
- 模型：monthly deterministic food-web difference equations with crop seasonality, chemical pressure, soil recovery, and consumer feedbacks。
- 解释：a newly converted field can maintain crop output under chemical control, but low wild-plant habitat keeps biodiversity and biological pest control weak。

### Q3 物种重新出现
- 加入物种：bats, insectivorous birds。
- 影响：bat and bird reemergence raises biological control and biodiversity; full organic transition improves long-term stability but has a larger transition-cost penalty。

### Q4 去除除草剂与蝙蝠再平衡
- 去除除草剂后生产者稳定度：0.542。
- 去除除草剂后消费者稳定度：0.0645。
- 解释：removing herbicide alone helps wild plants and soil but leaves pesticide pressure and pest dependence; adding bats and edge habitat improves balance more robustly。

### Q5 有机农业情景
- 推荐过渡：organic_partial。
- 理由：partial organic practices capture most biodiversity and stability gains while preserving a stronger net-margin index during transition。

### Q6 给农民的一页信
Dear farmer,

Our model treats your converted forest field as a living food web, not just as a crop-production surface. The main result is that immediately eliminating all chemical tools can raise ecological health, but it also exposes you to a transition period with cost and pest-control risk. The strongest practical first step is the organic partial path: reduce broad-spectrum chemicals, add organic soil inputs, restore field-edge habitat, and support bats and insectivorous birds. This keeps crop health in a workable range while rebuilding natural pest control, pollination, and soil recovery.

A good implementation plan is to monitor crop vigor, pest pressure, beneficial insects, bat activity, bird counts, and soil health monthly. If pest pressure stays controlled and your net margin remains acceptable, expand the organic components. You should also seek conservation incentives for habitat strips, bat boxes, and transition costs, because the ecological benefits extend beyond your farm.

Sincerely,
COMAP ecosystem modeling team

### Q7 策略与政策建议
- phase down herbicide and broad-spectrum pesticide over 3-5 growing seasons rather than removing all chemical control at once
- install bat boxes and restore edge habitat/wildflower strips to rebuild biological pest control
- use partial organic input first, track pest pressure and crop-yield index monthly, then expand to full organic if margins remain stable
- advocate cost-share payments or ecosystem-service credits for habitat strips, biological pest control, and transition certification costs

## 输出产物
- `food_web_edges.csv`：食物网有向/影响边。
- `state_trajectories.csv`：各情景 120 个月状态轨迹。
- `scenario_summary.csv`：生态稳定、产量、经济指标汇总。
- `organic_tradeoff_frontier.csv`：有机农业权衡前沿。
- `ecosystem_stability.png`：稳定性轨迹图。
