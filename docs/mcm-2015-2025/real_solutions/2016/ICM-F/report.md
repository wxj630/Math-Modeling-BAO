# 2016 ICM-F Modeling Refugee Immigration Policies 题面参数实验报告

## 数据来源
- 官方 PDF：`docs/mcm-2015-2025/official_assets_extracted/2016/Modeling Refugee Immigration Policies.pdf`。
- 官方题面参数：2015 年 10 月底欧洲收到超过 715,000 份庇护申请；Hungary 约 1,450/100k；2014 年批准率 32%；六条路线；Eastern Mediterranean 最热门，Central Mediterranean 最危险。
- 本题没有独立 CSV/XLSX 附件；路线容量、资源包和 NGO 增益是显式可替换规划假设。

## Q1 危机指标
- Hungary 未安置压力代理：986.0 / 100k。

## Q2 最优难民流动
- 总分配人数：715,000。
- 安全高容量路线：Eastern Mediterranean。

## Q3 动态容量和资源前置
- 最高优先资源：shelter。
- 加入 NGO 后未满足需求：0.0。

## Q4 政策包
- 目标：minimize unsafe movement and unmet basic needs while respecting legal and cultural constraints of affected countries。

## Q5 外生事件
- 事件：major terrorist attack linked in public debate to the refugee crisis。

## Q6 十倍扩展
- 10x 难民规模：7,150,000。
- 若不扩容，处理天数：352.22。

## 给 UN 的一页政策信摘要
To the UN Secretary General and the Chief of Migration:

ICM-RUN recommends a capacity-triggered refugee movement policy for the 715,000 applications reported by the end of October 2015. The model keeps the official six routes visible, shifts volume toward safer capacity such as Eastern Mediterranean, and flags shelter as the current priority resource. The UN should authorize multiple entry points, preposition shelter and healthcare, give NGOs formal logistics roles, and use quota triggers before Germany and France absorb a disproportionate burden. The policy should remain resilient to external security shocks by maintaining contingency entry points, humanitarian screening lanes, and transparent public health communication.

## 输出文件
- `result.json`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/result.json
- `route_flow_plan.csv`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/route_flow_plan.csv
- `resource_prepositioning.csv`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/resource_prepositioning.csv
- `ngo_strategy_comparison.csv`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/ngo_strategy_comparison.csv
- `exogenous_event_stress.csv`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/exogenous_event_stress.csv
- `scalability_10x.csv`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/scalability_10x.csv
- `refugee_flow_network.png`：docs/mcm-2015-2025/real_solutions/2016/ICM-F/artifacts/refugee_flow_network.png
