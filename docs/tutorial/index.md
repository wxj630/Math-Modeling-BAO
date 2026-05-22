# 从赛题到论文

数学建模不是把小问逐个“做完”，而是把一道赛题读成一个完整项目：前几问通常建立主模型和数据口径，中间问题加入情景、约束、预测或优化，最后问题把结果转成论文、备忘录或决策建议。

所以这个教程现在按“赛题入口”组织：

| 阅读层级 | 你要看的问题 | 入口 |
|---|---|---|
| 赛题整体 | 这道题的业务背景、主模型和小问递进链是什么？ | [MCM/ICM 赛题整体索引](/mcm-track/problem-index)、[CUMCM 赛题整体索引](/cumcm-track/problem-index) |
| 小问材料 | 某一问的 baseline、advanced、结果和产物在哪里？ | 每个赛题页中的“小问递进链” |
| 三层解法 | baseline 为什么只是起点，advanced 如何升级，outstanding 应补什么？ | [Baseline](./baseline.md)、[Advanced](./advanced.md)、[Outstanding](./outstanding.md) |
| 复现运行 | 如何用现有代码和实验结果复查某道题？ | [运行与复现](/reference/reproduce) |

## 推荐阅读顺序

1. 先选择一条赛道：[MCM/ICM](/mcm-track/) 或 [CUMCM](/cumcm-track/)。
2. 从赛题整体索引进入某一道题，例如 [MCM/ICM 2015-C](/mcm-track/problems/2015-C)。
3. 在赛题页里按小问递进链阅读：主模型、动态/情景、成本/优化、验证/迁移、报告表达。
4. 对每个小问只把 baseline 和 advanced 当作材料入口，不把它们当成互不相干的页面。
5. 最后用 [Outstanding Solution](./outstanding.md) 的标准检查整题还缺哪些论文级增强。

## 为什么从赛题入口开始

以 2015-C 为例，第 1 问的人力资本网络不是孤立模型；第 2 问要把它变成流失动态，第 3 问把流失转成招聘培训预算，第 4/5 问做压力情景，第 6 问扩展为多层组织网络，第 7 问再把前面全部整理成报告。逐问索引能找到材料，但只有赛题页能保留这条因果链。

## 教程和归档的关系

代码和实验结果不重做。`mcm/`、`cumcm/` 中的 `solution.py`、`result.json`、`report.md` 和 artifacts 仍是唯一材料源；教程只把它们重新组织成更适合学习和写论文的路径。
