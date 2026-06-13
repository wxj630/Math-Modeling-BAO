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
- 2024 留出平均 Accuracy：0.851046，平均 F1：0.287507，平均 Brier：0.142693。
- Monte Carlo 预计首次获得奖牌的 NOC 数量期望：7.5。

### 2028 总奖牌预测 Top 10

| NOC | 2024 total | 2028 expected total | 95% interval | expected gold |
|---|---:|---:|---|---:|
| USA | 122 | 139.928 | [124.0, 155.0] | 54.762 |
| CHN | 91 | 92.932 | [80.0, 106.525] | 36.712 |
| GBR | 63 | 64.486 | [53.0, 76.0] | 20.506 |
| AUS | 52 | 56.342 | [47.0, 66.0] | 19.708 |
| JPN | 45 | 49.962 | [40.0, 60.0] | 19.772 |
| ITA | 36 | 48.208 | [37.0, 59.0] | 17.17 |
| FRA | 64 | 47.776 | [37.0, 58.0] | 14.73 |
| GER | 31 | 39.94 | [31.0, 49.0] | 12.65 |
| NED | 34 | 32.774 | [23.0, 41.0] | 12.8 |
| KOR | 32 | 26.62 | [20.0, 33.0] | 10.398 |

### 首枚奖牌概率 Top 10

| NOC | first-medal probability | expected total if any |
|---|---:|---:|
| SAM | 0.388 | 1.28866 |
| LBN | 0.31 | 1.180645 |
| GUM | 0.3 | 1.066667 |
| ANG | 0.296 | 1.162162 |
| GBS | 0.292 | 1.10274 |
| PNG | 0.278 | 1.129496 |
| PLE | 0.266 | 1.120301 |
| ESA | 0.25 | 1.112 |
| ARU | 0.248 | 1.137097 |
| MLI | 0.228 | 1.096491 |

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
