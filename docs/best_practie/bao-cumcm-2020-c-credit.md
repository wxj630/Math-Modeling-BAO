# CUMCM 2020-C 中小微企业信贷：Baseline → Advanced → Outstanding 进阶

这道题是数据建模和运筹决策的混合题。前半段要从发票数据估计信用风险，后半段要把风险转成贷款额度、利率和银行收益。

## 材料入口

| 层级 | PDF | 代码 | 结果 |
|---|---|---|---|
| Baseline | `Math-Modeling-World-Reports/cumcm/2020-C/baseline/main.pdf` | `Math-Modeling-World-Reports/cumcm/2020-C/baseline/sections/A_code.tex`；`Math-Modeling-World/cumcm/generic_baselines/solutions/2020/C/q01/solution.py` | `Math-Modeling-World/cumcm/generic_baselines/results/2020/C/q01/result.json` |
| Advanced | `Math-Modeling-World-Reports/cumcm/2020-C/advanced/main.pdf` | `Math-Modeling-World-Reports/cumcm/2020-C/advanced/sections/A_code.tex`；`Math-Modeling-World/cumcm/question_solutions/2020/C/q01/solution.py` | `Math-Modeling-World/cumcm/question_results/2020/C/q01/result.json` |
| Outstanding | `Math-Modeling-World-Reports/outstanding/cumcm/2020-C/C227/pdf/C227.pdf` | `Math-Modeling-World/cumcm/outstanding_solutions/2020/C/C227/solution.py` | `Math-Modeling-World/cumcm/outstanding_solutions/2020/C/C227/result.json` |

## Baseline：从拟合/机器学习分类入口起步

Baseline 将题目识别为数据拟合、机器学习和统计识别问题。

当前模型选择：

```text
q01 = 数据拟合与回归分析
q02 = 数据拟合与回归分析
q03 = 机器学习与统计识别
```

这一层的价值是确认“信贷不是纯优化题”，必须先从数据中估计风险。但 baseline 的特征和策略还比较粗，缺少完整发票特征工程和预算约束下的贷款策略。

## Advanced：信用风险评分 + 授信组合优化

Advanced 读取官方三份附件，聚合进项/销项发票，形成风险评分和贷款策略。

问题 1 结果：

| 指标 | Advanced |
|---|---:|
| 企业数 | 123 |
| 批准贷款企业 | 37 |
| 拒绝企业 | 86 |
| 总授信 | 36447434.64 元 |
| 预算 | 50000000 元 |
| 批准企业平均风险 | 0.258241 |
| 期望利息收入 | 346363.51 元 |
| 平均贷款利率 | 0.051689 |

问题 2 结果：

| 指标 | Advanced |
|---|---:|
| 无信贷企业数 | 302 |
| 批准贷款企业 | 25 |
| 总授信 | 25000000 元 |
| 期望利息收入 | 196244.81 元 |

疫情冲击后：

| 指标 | Advanced |
|---|---:|
| 批准贷款企业 | 14 |
| 总授信 | 14000000 元 |
| 期望利息收入 | 113744.04 元 |

Advanced 的优点是从“预测风险”走到了“能给银行贷款策略”；不足是分类器集成和论文表格对齐还不够。

## Outstanding：五分类器 + Soft Voting + 贷款分级

Outstanding 复现 C227 的集成分类器路线：构造约 20 个发票特征，训练多种分类器，再用 soft voting 综合违约风险。

分类器结果：

| 分类器 | 训练准确率 | 测试准确率 | AUC |
|---|---:|---:|---:|
| Logistic | 0.7717 | 0.7097 | 0.8690 |
| AdaBoost | 1.0000 | 0.9032 | 0.8333 |
| GBDT | 1.0000 | 0.9032 | 0.8244 |
| SVM | 0.8913 | 0.8710 | 0.8571 |
| RF | 1.0000 | 0.8710 | 0.8244 |
| Soft Voting | 1.0000 | 0.9032 | 0.8452 |

无信贷企业结果：

| 指标 | Outstanding 复现 | 论文目标 | 误差 |
|---|---:|---:|---:|
| 高违约风险企业数 | 34 | 34 | 0 |
| 可贷企业数 | 268 | 268 | 0 |
| A 类企业 | 63 | 63 | 0 |
| B 类企业 | 103 | 103 | 0 |
| C 类企业 | 102 | 102 | 0 |
| 总预算 | 5000 万元 | 5000 万元 | 0 |

## 谁模拟/优化得最好

| 层级 | 模拟/优化能力 | 结论 |
|---|---|---|
| Baseline | 识别出数据拟合/机器学习方向 | 特征和决策链不足 |
| Advanced | 风险评分能直接生成授信策略 | 银行决策解释性强 |
| Outstanding | 多分类器验证并对齐 C227 论文数量目标 | 分类效果和获奖论文复现最好 |

结论：这题要分开看两种“最好”。如果看银行策略落地，Advanced 已经有贷款额度、利率和收益；如果看评奖和论文复现，Outstanding 的 soft voting 和分类器对照更强，尤其是可贷企业数量和 A/B/C 分级完全对齐论文。
