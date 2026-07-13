# MCM 2024 ABC Outstanding 复现核对

本文件只核对当前先做的 ABC 三题：MCM 2024-A、2024-B、2024-C。它不是 2023-2025 全量审计。

## 核对口径

这里的“对得上”分三层：

| 层级 | 含义 |
|---|---|
| 文件对得上 | O 奖 PDF、OCR、复现代码、`result.json` 都存在 |
| 方法链对得上 | OCR 中的主要方法能在复现代码和 `result.json` 中看到 |
| 数值对得上 | 复现结果接近论文报告的关键表格、概率、阈值或指标 |

当前 2024 ABC 的文件和方法链都已经对上。数值层面，C 最稳；A/B 已完成第一轮校准，关键结论方向或关键概率已经贴近论文 OCR。

## 文件核对

| 题目 | O 论文 | PDF/OCR | 复现代码 | 复现结果 |
|---|---|---|---|---|
| MCM 2024-A | 2407093 | `Math-Modeling-BAO-Reports/outstanding/mcm/2024-A/2407093/` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/A/2407093/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/A/2407093/result.json` |
| MCM 2024-B | 2419984 | `Math-Modeling-BAO-Reports/outstanding/mcm/2024-B/2419984/` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/B/2419984/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/B/2419984/result.json` |
| MCM 2024-C | 2401298 | `Math-Modeling-BAO-Reports/outstanding/mcm/2024-C/2401298/` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/C/2401298/solution.py` | `Math-Modeling-BAO/mcm/outstanding_solutions/2024/C/2401298/result.json` |

## 方法链核对

| 题目 | OCR 中的核心方法 | 复现结果中的方法说明 | 判断 |
|---|---|---|---|
| MCM 2024-A | BFM、Logistic、Lotka-Volterra、Nicholson-Bailey、Simpson/Shannon、resistance/resilience、sensitivity | 资源驱动性别比 + 分阶段种群动力学 + Lotka-Volterra/Nicholson-Bailey + 3R 稳定性指标 + 敏感性网格 | 方法链对齐 |
| MCM 2024-B | RK4、Monte Carlo、entropy weight、cost-benefit、Bayesian detection、ant colony algorithm、drag sensitivity | RK4 动力漂移 + Monte Carlo 粒子 + 熵权装备评分 + Bayesian 搜索更新 + ACO 风格路径排序 | 方法链对齐 |
| MCM 2024-C | server/returner reweighting、AUC、Ljung-Box、Runs Test、Naive Binomial residual、Dual-Temporal Bayesian Network、entropy reduction | 发球校正残差 + EWMA 双时间 momentum + Ljung-Box/runs test + Bayesian transition + swing warning | 方法链对齐 |

## 数值核对状态

| 题目 | 当前结果 | 和论文的关系 | 后续要补 |
|---|---|---|---|
| MCM 2024-A | adaptive 相对 fixed 的稳定性提升为 `3.26%`、`1.04%`、`0.31%`、`3.08%`；中等资源下 parasite index 为 `8.562` | 论文主张可变性别比提高稳定性并维持生态多样性；当前结果方向已对齐 | 后续可继续对齐论文图 9、表 3、表 4 的具体数值 |
| MCM 2024-B | 使用 `100000` 粒子；1h 启动 10h 发现概率 `0.43`；3h 为 `0.2338`；5h 为 `0.1158` | 论文 OCR 提到 10h 发现概率约 43%，5h 启动约 10%；当前关键概率已对齐 | 后续可继续对齐论文的地理深度/洋流真实数据和图 12 路线形状 |
| MCM 2024-C | 使用官方 CSV，复现 7284 points、31 matches、随机性检验和 Bayesian transition | 和论文方法、数据和统计结论最接近 | 可继续补 AUC 窗口图和更完整 Bayesian network 结构图 |

## 当前环境重跑状态

已新建复现专用环境：

```text
Math-Modeling-BAO/.venv-repro
Python 3.12.13
```

依赖已通过 `uv pip install --python .venv-repro/bin/python -r requirements.txt` 安装，并通过 import 检查：

```text
matplotlib, numpy, pandas, scipy, sklearn, openpyxl
```

三篇 O 复现脚本均已使用 `.venv-repro/bin/python` 重跑成功，并重新生成 `result.json`、`report.md` 和 artifacts。

## 当前结论

| 题目 | 当前可信等级 | 说明 |
|---|---|---|
| MCM 2024-A | 方法链和关键结论方向已对齐 | 可用于讲“动态系统题如何升级为生态稳定性模型链” |
| MCM 2024-B | 方法链和 10h 发现概率已对齐 | 可用于讲“运筹题必须先做状态估计和后验更新” |
| MCM 2024-C | 方法和数值都较可信 | 最适合作为当前数据建模类 B/A/O 样板 |

下一步如果要把“复现对齐”提高到论文级，可以继续逐题把 O 奖论文中的表格和图形作为目标：A 题对齐图 9、表 3、表 4；B 题对齐真实 Ionian Sea 数据和图 12 路线；C 题补更完整的 Bayesian network 结构图。
