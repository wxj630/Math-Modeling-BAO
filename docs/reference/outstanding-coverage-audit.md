# Outstanding 覆盖清单

本页记录官方获奖论文复现的当前对外口径。规则是：只有已经进入 README、Best Practice、统一 runner `--formal` 的条目，才标记为“正式复现”。其它已经整理 PDF/OCR、甚至已有实验脚本的条目，先归为候选或实验材料，避免完成数口径混乱。

## 正式复现：15 篇

### Batch 1：三大题型 × MCM/CUMCM

| 序号 | 赛题 | 类型 | O 论文 | 入口 |
|---:|---|---|---|---|
| 01 | MCM 2015-A | 微分方程/动态系统 | `35532` Containing Ebola and Future Infectious Diseases | [Best Practice](/best_practie/bao-mcm-2015-a-ebola) |
| 02 | CUMCM 2018-A | 微分方程/动态系统 | `A466` 高温作业专用服装设计 | [Best Practice](/best_practie/bao-cumcm-2018-a-heat-clothing) |
| 03 | MCM 2017-B | 运筹优化 | `69427` Merge After Toll | [Best Practice](/best_practie/bao-mcm-2017-b-toll-plaza) |
| 04 | CUMCM 2020-B | 运筹优化 | `B108` 穿越沙漠 | [Best Practice](/best_practie/bao-cumcm-2020-b-desert-crossing) |
| 05 | MCM 2019-C | 数据建模 | `1901213` Opioids Spread as a Contagious Disease | [Best Practice](/best_practie/bao-mcm-2019-c-opioid) |
| 06 | CUMCM 2020-C | 数据建模 | `C227` 中小微企业的信贷决策 | [Best Practice](/best_practie/bao-cumcm-2020-c-credit) |

### Batch 2：2023-2025 MCM ABC

| 序号 | 赛题 | 类型 | O 论文 | 入口 |
|---:|---|---|---|---|
| 07 | MCM 2023-A | 动态系统/生态模型 | `2309229` | [Best Practice](/best_practie/bao-mcm-2023-a-plant-community) |
| 08 | MCM 2023-B | 运筹优化/空间分区 | `2315379` | [Best Practice](/best_practie/bao-mcm-2023-b-maasai-mara) |
| 09 | MCM 2023-C | 数据建模/预测分类 | `2307946` | [Best Practice](/best_practie/bao-mcm-2023-c-wordle) |
| 10 | MCM 2024-A | 动态系统/生态模型 | `2407093` | [Best Practice](/best_practie/bao-mcm-2024-a-lamprey) |
| 11 | MCM 2024-B | 运筹优化/搜索救援 | `2419984` | [Best Practice](/best_practie/bao-mcm-2024-b-submersible-search) |
| 12 | MCM 2024-C | 数据建模/统计推断 | `2401298` | [Best Practice](/best_practie/bao-mcm-2024-c-tennis-momentum) |
| 13 | MCM 2025-A | 物理反演/动态磨损 | `2501909` | [Best Practice](/best_practie/bao-mcm-2025-a-stair-wear) |
| 14 | MCM 2025-B | 运筹优化/可持续旅游 | `2504448` | [Best Practice](/best_practie/bao-mcm-2025-b-juneau-tourism) |
| 15 | MCM 2025-C | 数据建模/预测排序 | `2505964` | [Best Practice](/best_practie/bao-mcm-2025-c-olympic-medals) |

运行命令：

```bash
python tools/run_outstanding_reproductions.py --formal --keep-going
```

## 候选与实验材料

下面这些条目有 PDF/OCR、文档或实验脚本，但当前不计入正式 15 篇。后续如果转正，需要同步更新 README、Best Practice、runner 和赛题页。

| 类别 | 条目 |
|---|---|
| CUMCM 2023 ABC 候选 | `A175` 定日镜场、`B226` 多波束测线、`C050` 蔬菜定价 |
| CUMCM 2024 ABC 候选 | `A016` 板凳龙、`B159` 生产决策、`C038` 农作物规划 |
| CUMCM 2025 ABC 候选 | `A196` 烟幕遮蔽、`B157` 碳化硅测厚、`C023` NIPT |
| 2024/2025 扩展题候选 | MCM 2024-D、CUMCM 2024-D/E、MCM 2025-D/E/F、CUMCM 2025-D/E 等 |

## 读者如何判断状态

- README 和 Best Practice 中列出的 15 篇，是当前正式复现口径。
- 赛题索引的 `BAO PDF` 列会显示该题所有可读 PDF，不代表每一篇 O 奖 PDF 都已经代码复现。
- `tools/run_outstanding_reproductions.py --formal --list` 会列出当前正式 runner 覆盖范围。
- 候选案例可以阅读，但不能在教程正文里写成“已经完成的 O 奖复现”。
