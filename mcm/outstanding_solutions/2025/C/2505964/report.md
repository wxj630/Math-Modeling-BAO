# 2025 MCM-C Outstanding 复现：2505964

## 复现对象
- 获奖论文：`2505964`，2028 Olympic Medal Predictions Based on Random Forest Model
- OCR 来源：`Outstanding_Solutions/MCM/OCR-results/C/2505964/2505964.md`
- PDF 来源：`Outstanding_Solutions/MCM/PDF-2025/C/2505964.pdf`
- 复现定位：不复制论文排版和私有中间表，而是用 COMAP 官方 CSV 复现其可验证模型链。

## 问题与建模主线
本题要求预测 2028 洛杉矶奥运奖牌榜、首次获奖国家概率、关键项目变化和“伟大教练”效应。论文 2505964 的主线不是只在国家层面外推奖牌数，而是先在运动员/团队参赛条目上构造能力特征，再按项目预测获奖概率，最后用 Monte Carlo 把单项概率分配成国家奖牌表。

## 代码实现
- `solution.py` 读取官方 `2025_Problem_C_Data.zip` 的运动员、奖牌榜、东道主和项目表。
- 对团队项目按 `Year/NOC/Sport/Event` 合并，避免把同一团队奖牌重复计入国家奖牌。
- 构造四维能力特征：历史总奖牌、历史金牌、历史最好成绩、历史加权成绩均值。
- 对每个 2024 仍有参赛样本的运动训练运动级随机森林分类器，得到 `Prob_Medal` 与 `Prob_Gold`。
- 在每个单项中按概率权重的 4 次幂做保守抽样：先抽 1 个金牌，再抽 2 个其他奖牌，重复 Monte Carlo 500 次。
- 对 USA Swimming 与 CHN Table Tennis 拟合 Poisson 事件弹性；对东道主效应用线性回归做补充；对 Great Coach 用近三届滚动成绩突增做候选筛选。

## 实验结果
- 2024 留出平均 Accuracy：0.850591，平均 F1：0.287348，平均 Brier：0.142806。
- Monte Carlo 预计首次获得奖牌的 NOC 数量期望：7.574。

### 2028 总奖牌预测 Top 10

| NOC | 2024 total | 2028 expected total | 95% interval | expected gold |
|---|---:|---:|---|---:|
| USA | 122 | 139.012 | [123.475, 155.0] | 53.846 |
| CHN | 91 | 92.274 | [80.0, 104.0] | 36.554 |
| GBR | 63 | 64.286 | [52.0, 77.0] | 20.546 |
| AUS | 52 | 56.168 | [45.0, 67.0] | 19.652 |
| JPN | 45 | 50.126 | [41.475, 60.0] | 19.756 |
| FRA | 64 | 47.986 | [36.0, 58.0] | 14.686 |
| ITA | 36 | 47.918 | [37.0, 59.0] | 17.078 |
| GER | 31 | 40.318 | [30.475, 50.0] | 12.716 |
| NED | 34 | 32.54 | [24.0, 41.0] | 12.76 |
| KOR | 32 | 26.632 | [19.475, 34.0] | 10.6 |

### 首枚奖牌概率 Top 10

| NOC | first-medal probability | expected total if any |
|---|---:|---:|
| SAM | 0.41 | 1.219512 |
| GUM | 0.322 | 1.15528 |
| LBN | 0.322 | 1.180124 |
| ANG | 0.284 | 1.15493 |
| GBS | 0.258 | 1.100775 |
| PNG | 0.254 | 1.149606 |
| PLE | 0.25 | 1.088 |
| MLI | 0.226 | 1.097345 |
| ESA | 0.22 | 1.172727 |
| NCA | 0.212 | 1.113208 |

### 关键项目 Poisson 弹性

| Case | beta(events) | event multiplier | one more event gain | LOO beta range |
|---|---:|---:|---:|---|
| USA Swimming | 0.051988 | 1.053363 | 1.964675 | [0.048686, 0.054667] |
| CHN Table Tennis | -0.019052 | 0.981129 | -0.122663 | [-0.099094, 0.05506] |

### Great Coach 复现结果

- Lang Ping / USA Volleyball 2008：成绩分 5.0，前三届均值 0.0，突增 5.0。
- Lang Ping / CHN Volleyball 2016：成绩分 3.0，前三届均值 1.333333，突增 1.666667。

| NOC | Sport | estimated medal-count gain | basis |
|---|---|---:|---|
| IND | Badminton | 1.666667 | benchmark jump score 5.0 |
| IND | Hockey | 2.0 | benchmark jump score 6.0 |
| SWE | Swimming | 3.0 | benchmark jump score 9.416667 |
| ROU | Rowing | 1.777778 | benchmark jump score 5.333333 |

## 相对 Advanced 的优势
- Advanced 当前主要是国家-年份层面的随机森林回归，能给出奖牌榜预测和粗粒度区间。
- Outstanding 复现进一步下钻到运动员/团队-项目层面，把“谁在什么项目上获奖”的概率转成国家奖牌表，因此更接近论文的建模叙事。
- Monte Carlo 分配强制每个项目产生固定数量奖牌，输出 95% 区间和首枚奖牌概率，比直接回归总数更适合解释不确定性。
- Poisson 事件弹性和 Great Coach 候选把奖牌预测连接到项目设置和训练投资建议，论文表达空间更完整。

## 输出产物
- `athlete_probability_table`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/athlete_probability_table.csv`
- `monte_carlo_summary`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/monte_carlo_summary.csv`
- `first_medal_probabilities`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/first_medal_probabilities.csv`
- `poisson_event_elasticity`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/poisson_event_elasticity.csv`
- `coach_recommendations`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/coach_recommendations.csv`
- `monte_carlo_top_total_chart`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/monte_carlo_top_total.png`
- `first_medal_chart`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/first_medal_probabilities.png`
- `poisson_chart`：`mcm/outstanding_solutions/2025/C/2505964/artifacts/poisson_event_elasticity.png`
