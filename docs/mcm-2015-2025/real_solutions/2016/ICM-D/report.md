# 2016 ICM-D Society Information Networks 题面参数实验报告

## 数据来源
- 官方 PDF：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Measuring the Evolution and Influence in Society's Information Networks.pdf`。
- 官方题面明确给出五个时期：1870s newspaper/train/telegraph、1920s radio、1970s television、1990s early internet、2010s smartphone。
- 本题没有独立 CSV/XLSX 附件；时代速度、覆盖率、连通性、过滤强度和容量指数均为显式可替换建模假设。

## Q1 信息流和新闻筛选
- 新闻阈值：0.58。
- 排名最高的新闻项：presidential_assassination。

## Q2 过去到今天的验证
- Lincoln 时代高价值事件 24h awareness：0.321169。
- 今日高价值事件 24h awareness：0.8844。
- 今日/历史 24h 比值：2.75369。

## Q3 2050 通信网络容量
- 2050 容量指数：2483.157。
- 相对 2010s multiplier：4.775。

## Q4 公众兴趣和观点影响
- 最高正向观点变化情景：trusted_public_health_warning。

## Q5 因素敏感性
- 最敏感因素：information_value。

## 输出文件
- `result.json`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/result.json
- `era_parameters.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/artifacts/era_parameters.csv
- `diffusion_comparison.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/artifacts/diffusion_comparison.csv
- `opinion_influence_scenarios.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/artifacts/opinion_influence_scenarios.csv
- `communication_capacity_2050.csv`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/artifacts/communication_capacity_2050.csv
- `information_spread_curves.png`：/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/real_solutions/2016/ICM-D/artifacts/information_spread_curves.png
