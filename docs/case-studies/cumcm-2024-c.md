# CUMCM 2024-C 农作物规划案例

这个案例展示 CUMCM 赛道中最典型的 advanced 工作流：从通用线性规划 baseline，升级到读取附件 Excel、生成 2024-2030 种植方案和提交模板文件。

## 题目任务

第 1 问要求在 2024-2030 年内给出农作物最优种植方案，并分别考虑：

- 超过预期销售量的部分滞销浪费。
- 超过预期销售量的部分按 2023 年价格的 50% 降价出售。

## Baseline 层

路径：

```text
cumcm/generic_baselines/reports/2024/C/q01/report.md
cumcm/generic_baselines/solutions/2024/C/q01/solution.py
```

Baseline 使用 `linear_programming`，把题目抽象成：

```text
max sum_i c_i * x_i
s.t. A * x <= b, x >= 0
```

它保留了“这是规划优化题”的正确方向，但变量仍是 `x_i`、`c_i`、`A_ji` 这类通用符号，没有完整表达地块、季次、作物、轮作和销售上限。

## Advanced 层

路径：

```text
cumcm/question_reports/2024/C/q01/report.md
cumcm/question_solutions/2024/C/q01/solution.py
cumcm/question_artifacts/2024/C/q01/result1_1.xlsx
cumcm/question_artifacts/2024/C/q01/result1_2.xlsx
```

Advanced 解法把题目变量专门化为：

```text
x_{y,l,s,c}: 第 y 年地块 l 在季次 s 种植作物 c 的面积
Y_{l,c,s}: 地块类型-作物-季次亩产量
C_{l,c,s}: 种植成本
P_{c,s}: 销售单价区间中点
D_{y,c,s}: 预期销售量上限
```

同时接入题目约束：

- 地块类型决定可种植作物和季次。
- 同一地块相邻季次不重茬。
- 任意连续三年窗口内至少安排一次豆类作物。
- 按滞销浪费或 50% 折价规则计算收益。
- 导出 `result1_1.xlsx` 和 `result1_2.xlsx`。

## 从 baseline 到 advanced 的差距

| 对照项 | Baseline | Advanced |
|---|---|---|
| 数据 | 使用附件中的数值表生成通用实验。 | 读取附件 1 地块/作物清单和附件 2 的 2023 种植、亩产、成本、价格。 |
| 变量 | 抽象资源选择强度 `x_i`。 | 年份、地块、季次、作物四维决策变量。 |
| 约束 | `A x <= b`。 | 地块类型、季次、轮作、豆类窗口、销售上限和折价收益。 |
| 输出 | `objective_max` 和资源松弛量。 | 两种情形的总利润、剩余产量、年度计划、CSV 和提交 Excel。 |

## Outstanding 预留

后续可补的 outstanding 方向：

- 用混合整数规划或更系统的元启发式替代贪心搜索。
- 对销售量、亩产量、成本、价格做相关 Monte Carlo 和稳健优化。
- 生成论文中的关键热力图、年度利润曲线和作物结构图。
- 把结果解释写成“策略建议 + 风险提示 + 管理启示”的完整章节。
