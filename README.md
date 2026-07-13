# Math-Modeling-BAO

**BAO** 有两层含义：一是 **Baseline -> Advanced -> Outstanding** 的递进建模路线，帮助同一道赛题从能跑的基础模型，逐步进阶到贴近优秀论文的完整模型链；二是中文里的“包”，表示这里是一个面向数学建模学习的材料包，包含教程、真题、模型、代码、结果和论文复现。

在线站点：

[https://wxj630.github.io/Math-Modeling-BAO/](https://wxj630.github.io/Math-Modeling-BAO/)

## 项目主线

这个仓库不是单纯的论文 PDF 集，也不是只放代码的题解仓库。它的阅读顺序是：

1. 先在 [Best Practice](docs/best_practie/index.md) 理解评奖标准、题型、数据、文献和 B/A/O 递进方法。
2. 再进入 [MCM/ICM 赛题索引](docs/mcm-track/problem-index.md) 或 [CUMCM 赛题索引](docs/cumcm-track/problem-index.md)，按完整赛题阅读。
3. 每道赛题先看 Baseline PDF，再看 Advanced PDF；有正式 Outstanding 复现的题，再看 O 奖论文 PDF、复现代码、结果和报告。
4. PDF 下载不单独作为学习入口，而是融入赛题索引的 `BAO PDF` 列；完整下载清单保留在 [PDF 下载清单](docs/reference/report-pdf-library.md)。

当前覆盖：

- MCM/ICM：66 道赛题、371 个逐问 advanced 实验、371 个通用 baseline。
- CUMCM：63 道赛题、243 个逐问 advanced 实验、243 个通用 baseline。
- 纯 PDF 数据集：778 个 PDF，其中 baseline 129、advanced 129、outstanding 520。

## 三层材料

| 层级 | 作用 | 读者应该看什么 |
|---|---|---|
| Baseline | 最低可运行建模脚手架 | 模型入口、变量、最小结果、报告结构 |
| Advanced | 接入题意、数据和约束后的逐问解法 | 真实数据、约束、结果表、图和可复现实验 |
| Outstanding | 复现官方获奖论文中可验证的模型链 | 论文方法、代码复现、结果对齐、敏感性或稳定性分析 |

## 正式 Outstanding 复现

当前对外正式标记的 O 奖复现共 **15 篇**。仓库中可能保留后续候选或实验草稿，但 README、教程入口和 `--formal` runner 只把下面 15 篇作为已复现口径。

### Batch 1：三大题型 × MCM/CUMCM

| 序号 | 题型 | 竞赛题目 | O 论文 | 文档 |
|---:|---|---|---|---|
| 01 | 微分方程/动态系统 | MCM 2015-A Ebola | `35532` | [B/A/O 案例](docs/best_practie/bao-mcm-2015-a-ebola.md) |
| 02 | 微分方程/动态系统 | CUMCM 2018-A 高温作业专用服装 | `A466` | [B/A/O 案例](docs/best_practie/bao-cumcm-2018-a-heat-clothing.md) |
| 03 | 运筹优化 | MCM 2017-B Merge After Toll | `69427` | [B/A/O 案例](docs/best_practie/bao-mcm-2017-b-toll-plaza.md) |
| 04 | 运筹优化 | CUMCM 2020-B 穿越沙漠 | `B108` | [B/A/O 案例](docs/best_practie/bao-cumcm-2020-b-desert-crossing.md) |
| 05 | 数据建模 | MCM 2019-C Opioids | `1901213` | [B/A/O 案例](docs/best_practie/bao-mcm-2019-c-opioid.md) |
| 06 | 数据建模 | CUMCM 2020-C 中小微企业信贷 | `C227` | [B/A/O 案例](docs/best_practie/bao-cumcm-2020-c-credit.md) |

### Batch 2：2023-2025 MCM ABC 代表样例

| 序号 | 年份 | 题目 | O 论文 | 文档 |
|---:|---|---|---|---|
| 07 | 2023 | MCM 2023-A Drought-Stricken Plant Communities | `2309229` | [B/A/O 案例](docs/best_practie/bao-mcm-2023-a-plant-community.md) |
| 08 | 2023 | MCM 2023-B The Maasai Mara | `2315379` | [B/A/O 案例](docs/best_practie/bao-mcm-2023-b-maasai-mara.md) |
| 09 | 2023 | MCM 2023-C Wordle | `2307946` | [B/A/O 案例](docs/best_practie/bao-mcm-2023-c-wordle.md) |
| 10 | 2024 | MCM 2024-A Resource Availability and Sex Ratios | `2407093` | [B/A/O 案例](docs/best_practie/bao-mcm-2024-a-lamprey.md) |
| 11 | 2024 | MCM 2024-B Searching for a Submersible | `2419984` | [B/A/O 案例](docs/best_practie/bao-mcm-2024-b-submersible-search.md) |
| 12 | 2024 | MCM 2024-C Momentum in Tennis | `2401298` | [B/A/O 案例](docs/best_practie/bao-mcm-2024-c-tennis-momentum.md) |
| 13 | 2025 | MCM 2025-A Stair Wear | `2501909` | [B/A/O 案例](docs/best_practie/bao-mcm-2025-a-stair-wear.md) |
| 14 | 2025 | MCM 2025-B Sustainable Tourism in Juneau | `2504448` | [B/A/O 案例](docs/best_practie/bao-mcm-2025-b-juneau-tourism.md) |
| 15 | 2025 | MCM 2025-C Olympic Medal Predictions | `2505964` | [B/A/O 案例](docs/best_practie/bao-mcm-2025-c-olympic-medals.md) |

运行正式 15 篇复现：

```bash
python tools/run_outstanding_reproductions.py --formal --keep-going
```

## PDF 数据集

主 Git 仓库不保存 3GB+ PDF 文件本体。PDF 已整理为独立 ModelScope 数据集，方便国内访问：

[https://www.modelscope.cn/datasets/wuxiaojun/Math-Modeling-BAO](https://www.modelscope.cn/datasets/wuxiaojun/Math-Modeling-BAO)

在教程站里，PDF 的主要入口是 MCM/CUMCM 赛题索引中的 `BAO PDF` 列；[PDF 下载清单](docs/reference/report-pdf-library.md) 只作为完整 manifest、校验和和批量下载入口。

## 内容结构

| 路径 | 说明 |
|---|---|
| `docs/best_practie/` | Best Practice 栏目：评奖标准、B/A/O 方法、数据、文献、混合题型和正式案例。 |
| `docs/tutorial/` | 总教程入口，解释 baseline、advanced、outstanding 三层材料如何使用。 |
| `docs/mcm-track/` | MCM/ICM 赛题入口和整体索引，已融入 BAO PDF 链接。 |
| `docs/cumcm-track/` | CUMCM 赛题入口和整体索引，已融入 BAO PDF 链接。 |
| `docs/reference/` | 复现命令、归档路径、PDF manifest 和覆盖审计。 |
| `mcm/` | MCM/ICM baseline、advanced、outstanding 代码、报告和轻量产物。 |
| `cumcm/` | CUMCM baseline、advanced、outstanding 代码、报告和轻量产物。 |
| `outstanding_reproductions/` | 统一 outstanding 复现 runner 的 case 注册。 |
| `tools/` | 赛题页、PDF 索引、审计和批量复现工具。 |

大体积官方附件、原始压缩包、解压数据、本地实验草稿和 PDF 本体不进入主仓库，相关规则写在 `.gitignore`。

## 本地预览

```bash
npm install
npm run docs:dev
```

构建静态站点：

```bash
npm run docs:build
```

重建赛题整体索引：

```bash
python tools/build_problem_pages.py --index-only
```

完整重建赛题页和索引：

```bash
python tools/build_problem_pages.py
```
