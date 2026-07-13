# MCM/ICM 赛题入口

MCM/ICM 教程现在以完整赛题为入口。每个赛题页先展示整题主线，再列出小问递进链，并把每一问对应的 baseline、advanced、实验结果和 outstanding 预留位接起来。PDF 不单独作为学习入口，而是放在赛题整体索引的 `BAO PDF` 列。

## 从这里进入

| 入口 | 用途 |
|---|---|
| [MCM/ICM 赛题整体索引](./problem-index.md) | 按年份浏览赛题，并直接打开 Baseline / Advanced / Outstanding PDF。 |
| [MCM 2015-A Ebola](/best_practie/bao-mcm-2015-a-ebola) | 微分方程/动态系统的完整 B/A/O 样例。 |
| [MCM 2017-B Merge After Toll](/best_practie/bao-mcm-2017-b-toll-plaza) | 运筹优化的完整 B/A/O 样例。 |
| [MCM 2019-C Opioids](/best_practie/bao-mcm-2019-c-opioid) | 数据建模的完整 B/A/O 样例。 |
| [MCM 2025-C Olympic Medals](/best_practie/bao-mcm-2025-c-olympic-medals) | 现代数据建模 O 奖复现样例。 |

## 阅读方法

1. 先进入赛题页，读“整题主线”。
2. 按小问顺序看递进作用：主模型、动态、成本、情景、验证、报告。
3. 在索引的 `BAO PDF` 列先读 Baseline PDF，再读 Advanced PDF。
4. 不急着打开所有代码；只有当报告里的变量和结果需要核验时，再进入 `solution.py` 和 `result.json`。
5. 有正式 O 奖复现的题，再读 Outstanding PDF 和复现报告，用评奖标准检查统一假设、鲁棒性和论文图表。

## 当前覆盖

MCM/ICM 当前生成 66 个赛题页，覆盖 371 个小问。代码和实验结果仍保存在 `mcm/` 原目录，教程页只负责把它们组织成适合学习的路径。
