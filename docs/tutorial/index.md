# 从归档到论文

这个教程把仓库中已有的 MCM/ICM 与 CUMCM 解法整理成一条可学习、可复现、可继续深化的路线。每道题可以按三层阅读：

| 层级 | 作用 | 仓库位置 | 适合什么时候看 |
|---|---|---|---|
| Baseline solution | 最低可运行建模脚手架，保留第一版模型选择、变量、约束和结果格式。 | `mcm/generic_baselines/`、`cumcm/generic_baselines/` | 刚读完题、需要快速落地一个能跑的模型时。 |
| Advanced solution | 题意专门化解法，读取官方附件或题面参数，输出逐问结果、报告和实验产物。 | `mcm/question_solutions/`、`cumcm/question_solutions/` | 已经知道基础模型，想看到如何把题面约束接入代码时。 |
| Outstanding solution | 预留给后续论文级解法，强调更强算法、敏感性、误差分析、可视化和写作表达。 | 教程预留结构，后续可新增到 `outstanding_solutions/` 或专题页。 | 准备冲高质量论文或复盘优秀论文时。 |

## 推荐阅读顺序

1. 先读 [Baseline Solution](./baseline.md)，理解为什么要保留通用基线，以及它不能替代最终解法。
2. 再读 [Advanced Solution](./advanced.md)，对照同一小问的 baseline 与进阶版，看数据接入、约束表达和输出结构如何升级。
3. 读 [MCM/ICM 解法教程](/mcm-track/) 或 [CUMCM 解法教程](/cumcm-track/)，选择一个赛道进入。
4. 用代表案例练手：[MCM 2024-C 网球势头](/case-studies/mcm-2024-c) 和 [CUMCM 2024-C 农作物规划](/case-studies/cumcm-2024-c)。
5. 最后读 [Outstanding Solution](./outstanding.md)，把现有 advanced 解法当作骨架，继续补鲁棒性、图表和论文叙事。

## 教程和归档的关系

教程页负责讲“如何读、如何复现、如何升级”。完整逐问产物仍保存在原归档目录中，这样不会把 GitHub Pages 变成上百份重复报告，也便于脚本继续批量更新。
