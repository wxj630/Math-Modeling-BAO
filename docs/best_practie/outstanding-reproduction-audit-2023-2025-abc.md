# 2023-2025 MCM ABC Outstanding 复现审计

审计日期：2026-07-13。

本文件只记录当前正式口径中的 Batch 2：2023、2024、2025 三年 MCM A/B/C 共 9 篇。CUMCM 2023-2025 ABC 的材料已整理为候选案例，但不计入当前正式 15 篇 O 奖复现。

统一 runner 命令：

```bash
python tools/run_outstanding_reproductions.py --batch 2 --keep-going
```

## 总表

| Case | 类型 | O 论文 | 复现代码 | 关键输出/对齐 | 状态 |
|---|---|---|---|---|---|
| `mcm-2023-A-2309229` | 动态系统/生态微分方程 | `2309229` | `mcm/outstanding_solutions/2023/A/2309229/solution.py` | `optimal_species_count`=2；Pielou 指数约 0.8826；beta 敏感性下降约 32% | PASS |
| `mcm-2023-B-2315379` | 运筹优化/空间分区 | `2315379` | `mcm/outstanding_solutions/2023/B/2315379/solution.py` | 36 网格分区、scenario 2 收益、保护区/旅游区空间距离 | PASS |
| `mcm-2023-C-2307946` | 数据建模/预测与分类 | `2307946` | `mcm/outstanding_solutions/2023/C/2307946/solution.py` | 2023-03-01 参与人数区间、EERIE 难度分布、Wordle 特征模型 | PASS |
| `mcm-2024-A-2407093` | 动态系统/生态模型 | `2407093` | `mcm/outstanding_solutions/2024/A/2407093/solution.py` | 资源驱动性别比、阶段种群动力学、3R 稳定性指标 | PASS |
| `mcm-2024-B-2419984` | 运筹优化/搜索救援 | `2419984` | `mcm/outstanding_solutions/2024/B/2419984/solution.py` | RK4 漂移、Monte Carlo 粒子、Bayesian 搜索更新 | PASS |
| `mcm-2024-C-2401298` | 数据建模/统计推断 | `2401298` | `mcm/outstanding_solutions/2024/C/2401298/solution.py` | 官方逐分数据、发球校正残差、随机性检验、Bayesian transition | PASS |
| `mcm-2025-A-2501909` | 物理反演/动态磨损 | `2501909` | `mcm/outstanding_solutions/2025/A/2501909/solution.py` | WVM/WDM 磨损体积与人流反演、不确定性分析 | PASS |
| `mcm-2025-B-2504448` | 运筹优化/可持续旅游 | `2504448` | `mcm/outstanding_solutions/2025/B/2504448/solution.py` | 多目标旅游政策、容量/收费前沿、敏感性分析 | PASS |
| `mcm-2025-C-2505964` | 数据建模/预测排序 | `2505964` | `mcm/outstanding_solutions/2025/C/2505964/solution.py` | 随机森林、Monte Carlo 奖牌分配、Poisson 项目弹性 | PASS |

## 审计结论

- 这 9 篇构成当前 2023-2025 现代样板：A 偏机制/动态，B 偏优化/决策，C 偏数据建模。
- 每篇都有 `solution.py`、`result.json`、`report.md` 和 `artifacts/`，可以由统一 runner 批量执行。
- 复现验收重点是：脚本能跑、结果可追、关键数值或方向能和论文目标对齐，差异和校准来源写清楚。

## 注意事项

- Outstanding 复现是竞赛论文级复现，不等同于科研级独立复现实验。
- 部分外部数据和论文未公开参数采用论文表格/OCR 目标做校准。
- CUMCM 2023-2025 ABC 的文档和代码保留为候选材料，后续如果转正，需要单独纳入正式 batch 并更新 README、Best Practice 和 runner 口径。
