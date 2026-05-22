# MCM/ICM 赛题入口

MCM/ICM 教程现在以完整赛题为入口。每个赛题页先展示整题主线，再列出小问递进链，并把每一问对应的 baseline、advanced、实验结果和 outstanding 预留位接起来。

## 从这里进入

| 入口 | 用途 |
|---|---|
| [MCM/ICM 赛题整体索引](./problem-index.md) | 按年份浏览每一道赛题，进入赛题页。 |
| [MCM/ICM 逐问材料索引](./solution-index.md) | 作为附录快速查找某个小问的 baseline/advanced report。 |
| [2015-C 人力资本网络案例](/case-studies/mcm-2015-c) | 重点示范同一赛题的小问如何递进。 |
| [2024-C 网球势头案例](/case-studies/mcm-2024-c) | 展示真实附件数据如何支撑整题模型链。 |

## 阅读方法

1. 先进入赛题页，读“整题主线”。
2. 按小问顺序看递进作用：主模型、动态、成本、情景、验证、报告。
3. 每一问先读 baseline report，再读 advanced report。
4. 不急着打开所有代码；只有当报告里的变量和结果需要核验时，再进入 `solution.py` 和 `result.json`。
5. 用 outstanding 标准检查整题还缺哪些统一假设、鲁棒性和论文图表。

## 当前覆盖

MCM/ICM 当前生成 64 个赛题页，覆盖 367 个小问。代码和实验结果仍保存在 `mcm/` 原目录，教程页只负责把它们组织成适合学习的路径。
