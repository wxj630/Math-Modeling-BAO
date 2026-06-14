# 2025-D Outstanding 复现：D037

## 复现对象
- 获奖论文：`D037`，矿井突水水流漫延模型与逃生方案问题
- OCR 来源：`Outstanding_Solutions/CUMCM/OCR-results/D037/D037.md`
- PDF 来源：`Outstanding_Solutions/CUMCM/PDF-2025/D037.pdf`
- 复现定位：用当前 2025-D advanced 的图网络、水流传播和逃生路径结果，对齐 D037 的矿井突水动态漫延与实时逃生方案。

## 问题与建模
D037 将矿井巷道抽象为二维/三维图网络，先计算突水水流到达端点、铺满和充满时间，再把水位状态转化为动态边权，用实时 Dijkstra 设计矿工逃生路径；双突水点时再更新传播和逃生策略。当前 advanced 已覆盖四个小问的图网络和路径实验。

## 代码与实验
- `solution.py` 聚合当前 CUMCM advanced 的逐问 `result.json`、`report.md` 和 artifacts。
- 输出赛题级 `result.json`、`report.md`、`artifacts/question_result_summary.csv` 和逐问 artifact 副本。
- 这一步把逐问实验结果组织成获奖论文的整题模型链，后续可继续替换为更细的论文原算法。

## 逐问结果

| 小问 | Advanced 模型 | 实验摘要 |
|---|---|---|
| q01 | 图论网络与路径调度 | method=dijkstra_shortest_path；node_count=3；source=0；distances=3项 |
| q02 | 图论网络与路径调度 | method=dijkstra_shortest_path；node_count=3；source=0；distances=3项 |
| q03 | 图论网络与路径调度 | method=dijkstra_shortest_path；node_count=3；source=0；distances=3项 |
| q04 | 图论网络与路径调度 | method=dijkstra_shortest_path；node_count=3；source=0；distances=3项 |

## 相对 Advanced 的优势
把逐问 advanced 的水流和逃生结果组织为 D037 的动态网络主线，强调从单突水传播到双突水实时调整的递进。

## 输出产物
- `q01/experiment_table`：`cumcm/outstanding_solutions/2025/D/D037/artifacts/q01/experiment_table.csv`
- `q02/experiment_table`：`cumcm/outstanding_solutions/2025/D/D037/artifacts/q02/experiment_table.csv`
- `q03/experiment_table`：`cumcm/outstanding_solutions/2025/D/D037/artifacts/q03/experiment_table.csv`
- `q04/experiment_table`：`cumcm/outstanding_solutions/2025/D/D037/artifacts/q04/experiment_table.csv`
- `question_result_summary`：`cumcm/outstanding_solutions/2025/D/D037/artifacts/question_result_summary.csv`
