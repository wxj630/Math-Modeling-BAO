# 数学建模中的求解器与算法库选择

数学建模代码不是“每道题都手写算法”，也不是“所有问题都丢给一个万能优化器”。更稳的做法是先判断题目的数学结构，再选择合适的成熟求解器、机器学习库，或者在状态空间很小的时候直接写 DP、枚举和仿真。

当前仓库里三类典型题的实现可以概括为：

| 题型 | 常见数学形式 | 优先工具 | 什么时候自写 |
|---|---|---|---|
| 微分方程 | 状态变量随时间连续变化，形如 `dy/dt = f(t, y, params)` | `scipy.integrate.solve_ivp` | 需要自己写右端函数、参数、初值、事件和结果解释 |
| 运筹优化 | 线性规划、连续优化、图路径、离散决策、排队/仿真 | `scipy.optimize.linprog`、`scipy.optimize.minimize`、`scipy.sparse.csgraph.dijkstra` | 状态空间小、约束强、题目规则离散时，用 DP、枚举、贪心或仿真更透明 |
| 数据建模 | 回归、分类、聚类、降维、集成学习、预测 | `scikit-learn` | 特征工程、指标体系、业务规则、后处理通常要自己写 |

注意：真实赛题通常不是纯题型。微分方程题后面会接优化、控制和资源分配；运筹优化题前面会接数据估计、情景模拟和风险评价；数据建模题后面会接决策、排序、资源配置和政策建议。更完整的讨论见 [混合题型：真实赛题很少只有一种模型](./mixed-problem-patterns.md)。

## 微分方程类：建方程后交给 `solve_ivp`

微分方程类题目的核心不是写积分器，而是把题意转成状态变量和方程。

典型写法：

```python
from scipy.integrate import solve_ivp

def rhs(t, y, params):
    S, E, I, R = y
    beta, sigma, gamma = params
    N = S + E + I + R
    return [
        -beta * S * I / N,
        beta * S * I / N - sigma * E,
        sigma * E - gamma * I,
        gamma * I,
    ]

sol = solve_ivp(
    rhs,
    (0, 180),
    y0=[S0, E0, I0, R0],
    args=((beta, sigma, gamma),),
    t_eval=range(181),
)
```

在论文里要解释的是：

- `S/E/I/R` 或其它状态变量分别代表什么。
- 参数来自题面、附件、拟合还是论文参考。
- 初值如何设定。
- 积分结果如何转成峰值、阈值、持续时间、风险指标或政策建议。

当前 outstanding 复现中：

| 赛题 | 实现方式 | 是否调用成熟求解器 |
|---|---|---|
| MCM 2015-A Ebola | SEIQR 疫情传播方程 + 药物产量阈值 | 是，调用 `solve_ivp` |
| CUMCM 2018-A 高温服 | 论文参数校准的一维传热厚度搜索 | 主要是自写搜索和校准曲线；完整 PDE 可进一步升级为有限差分矩阵求解 |

对应代码：

```text
Math-Modeling-BAO/outstanding_reproductions/cases.py
Math-Modeling-BAO/mcm/outstanding_solutions/2015/A/35532/solution.py
Math-Modeling-BAO/cumcm/outstanding_solutions/2018/A/A466/solution.py
```

## 运筹优化类：先判断是连续、线性、图，还是离散规则

运筹优化题最容易误解：不是所有优化题都应该上一个“大 solver”。实际建模时常见四种情况。

| 问题结构 | 推荐工具 | 例子 |
|---|---|---|
| 线性目标 + 线性约束 | `scipy.optimize.linprog` | 资源分配、预算分配、生产计划的连续松弛 |
| 非线性连续参数 | `scipy.optimize.minimize`、`minimize_scalar` | 参数拟合、几何残差最小化、热模型校准 |
| 图路径/网络 | `scipy.sparse.csgraph.dijkstra`、自写图搜索 | 最短路、逃生路线、运输路径 |
| 离散策略组合 | DP、枚举、贪心、仿真 | 沙漠穿越、生产检测决策、排班、路径-资源联合决策 |

线性规划的基本形态：

```python
from scipy.optimize import linprog

# max c @ x  通常转成 min -c @ x
res = linprog(
    c=-value,
    A_ub=resource,
    b_ub=capacity,
    bounds=[(0, None)] * n,
    method="highs",
)
```

连续优化的基本形态：

```python
from scipy.optimize import minimize

def loss(theta):
    prediction = model(theta)
    return ((prediction - observed) ** 2).mean()

res = minimize(loss, x0=[1.0, 1.0], method="Nelder-Mead")
```

DP/枚举适合这类题：

- 每天、每个地点、每种行动都有有限状态。
- 策略变量是 0-1 或少量离散选项。
- 题目更关心“规则是否执行正确”，不一定需要通用 MILP。
- 状态数可控，直接枚举能输出完整策略表。

当前 outstanding 复现中：

| 赛题 | 实现方式 | 是否调用成熟求解器 |
|---|---|---|
| MCM 2017-B Toll Plaza | Erlang-C 排队公式 + 合流瓶颈流量 + 事故率敏感性表 | 没有调用通用优化器，核心是公式和表格复现 |
| CUMCM 2020-B 穿越沙漠 | 路线结果表 + 1024 天气枚举 + 随机模拟 + 局部博弈策略 | 没有调用通用优化器，使用自写枚举、仿真和策略表 |

这不是偷懒，反而是运筹题里很常见的选择：当题目结构明确、状态空间不大时，DP/枚举比黑箱 solver 更容易审阅、复现和写进论文。

对应代码：

```text
Math-Modeling-BAO/outstanding_reproductions/cases.py
Math-Modeling-BAO/mcm/outstanding_solutions/2017/B/69427/solution.py
Math-Modeling-BAO/cumcm/outstanding_solutions/2020/B/B108/solution.py
```

## 数据建模类：核心是 `特征工程 + sklearn.fit`

数据建模类通常不需要自己实现随机森林、SVM、逻辑回归。更重要的是：

1. 清洗官方附件或外部数据。
2. 构造和题意一致的特征。
3. 选择模型。
4. 训练、验证、比较指标。
5. 把模型输出转成题目要求的风险、排名、预测、政策或决策。

常用工具：

| 任务 | 常用模型或函数 |
|---|---|
| 线性趋势预测 | `sklearn.linear_model.LinearRegression` |
| 二分类/多分类 | `LogisticRegression`、`SVC` |
| 非线性分类/回归 | `RandomForestClassifier/Regressor`、`GradientBoostingClassifier` |
| 多模型融合 | `VotingClassifier` |
| 聚类 | `KMeans`、`DBSCAN` |
| 降维 | `PCA` |
| 评估 | `accuracy_score`、`roc_auc_score`、`r2_score`、`mean_absolute_error` |

典型写法：

```python
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    features,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)

model = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000)),
        ("rf", RandomForestClassifier(n_estimators=200, random_state=42)),
    ],
    voting="soft",
)

model.fit(x_train, y_train)
pred = model.predict(x_test)
prob = model.predict_proba(x_test)[:, 1]

print(accuracy_score(y_test, pred), roc_auc_score(y_test, prob))
```

当前 outstanding 复现中：

| 赛题 | 实现方式 | 是否调用成熟求解器/模型库 |
|---|---|---|
| MCM 2019-C Opioid Crisis | 官方 NFLIS 县年面板 + 空间 Markov 权重传播 + 县级趋势预测 | 趋势预测调用 `LinearRegression`；传播边权重逻辑自写 |
| CUMCM 2020-C 中小微企业信贷 | 发票特征工程 + 五分类器 + soft voting + 信用评级和贷款分配 | 调用 `LogisticRegression`、`AdaBoostClassifier`、`GradientBoostingClassifier`、`SVC`、`RandomForestClassifier`、`VotingClassifier` |

对应代码：

```text
Math-Modeling-BAO/outstanding_reproductions/cases.py
Math-Modeling-BAO/mcm/outstanding_solutions/2019/C/1901213/solution.py
Math-Modeling-BAO/cumcm/outstanding_solutions/2020/C/C227/solution.py
```

## 如何判断“该不该调用现有求解器”

可以用下面这张判断表。

| 如果你的模型是 | 优先考虑 | 不建议 |
|---|---|---|
| 明确的 ODE/PDE 时间演化 | `solve_ivp`、有限差分、矩阵求解 | 手写欧拉法当最终结果，除非只是 baseline |
| 标准线性规划 | `linprog` | 自己乱写迭代法 |
| 小规模整数/组合策略 | DP、枚举、贪心、局部搜索 | 为了“高级”强行上复杂 MILP |
| 图最短路/连通性 | Dijkstra、Floyd、网络流 | 用机器学习预测路径 |
| 分类/预测 | `scikit-learn` | 自己实现 SVM、随机森林 |
| 指标评价/排名 | 标准化 + 熵权/TOPSIS/AHP/回归 | 只靠主观打分 |

## 写论文时怎么描述

不要只写“本文调用 Python 求解”。更好的写法是：

- 微分方程：说明状态变量、方程、参数、初值、积分方法和步长/容差。
- 运筹优化：说明决策变量、目标函数、约束、可行性检查和求解策略。
- DP/枚举：说明状态、转移、边界条件、剪枝规则和复杂度。
- 数据建模：说明数据来源、特征、训练/测试划分、模型、评价指标和泛化风险。

例如：

```text
本文将疫情传播过程建模为 SEIQR 常微分方程组，使用 scipy.integrate.solve_ivp 进行数值积分。
求解器只负责给定参数下的时间推进；模型有效性主要由状态变量定义、参数校准和敏感性分析保证。
```

```text
本文将沙漠穿越问题写成按天展开的动态规划。状态包含日期、所在节点、剩余资源和可行动作，
转移枚举停留、移动、挖矿和补给。由于状态空间有限，直接 DP 比通用优化器更便于输出完整路径和策略解释。
```

```text
本文从进销项发票中提取经营规模、交易稳定性、作废率、负数发票率和上下游集中度等特征，
调用 scikit-learn 中的多种分类器估计违约风险，并用 soft voting 综合模型输出。
```

## 当前 6 篇 outstanding 的求解器小结

| 题型 | 竞赛 | 赛题 | outstanding 编号 | 主要实现 | 求解器/库 |
|---|---|---|---|---|---|
| 微分方程 | MCM | 2015-A Ebola | `35532` | SEIQR + 药物阈值 + 医疗中心覆盖 | `solve_ivp` + 自写覆盖 |
| 微分方程 | CUMCM | 2018-A 高温服 | `A466` | 传热参数校准 + 厚度搜索 | 自写搜索；可升级有限差分矩阵 |
| 运筹优化 | MCM | 2017-B Toll Plaza | `69427` | 排队公式 + 合流瓶颈 + 事故敏感性 | 自写公式/表格 |
| 运筹优化 | CUMCM | 2020-B 穿越沙漠 | `B108` | DP 思路 + 天气枚举 + 随机模拟 + 博弈 | 自写枚举/仿真 |
| 数据建模 | MCM | 2019-C Opioid | `1901213` | NFLIS 面板 + Markov 传播边 + 趋势预测 | `LinearRegression` + 自写传播 |
| 数据建模 | CUMCM | 2020-C 信贷 | `C227` | 发票特征 + 五分类器 + soft voting | `scikit-learn` 分类器 |

## 运行入口

单篇 outstanding 可以直接运行各自目录下的 `solution.py`。整批运行：

```bash
python Math-Modeling-BAO/tools/run_outstanding_reproductions.py --keep-going
```

共享实现位置：

```text
Math-Modeling-BAO/outstanding_reproductions/cases.py
```

通用题库实现里也大量使用这些工具：

```text
Math-Modeling-BAO/cumcm/lib/question_models.py
Math-Modeling-BAO/mcm/question_solutions/
Math-Modeling-BAO/cumcm/question_solutions/
Math-Modeling-BAO/docs/mcm-2015-2025/real_solutions/
```
