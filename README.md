# Math-Modeling-BAO

**BAO** 有两层含义：一是 **Baseline -> Advanced -> Outstanding** 的递进建模路线，帮助同一道赛题从能跑的基础模型，逐步进阶到贴近优秀论文的完整模型链；二是中文里的“包”，表示这里是一个面向数学建模学习的材料包，包含教程、真题、模型、代码、结果和论文复现。

MCM/ICM 与 CUMCM 建模教程站。仓库当前以完整赛题为入口，再把每道题的小问递进链连接到三层解法归档：

- Baseline solution：最低可运行建模脚手架，用来快速形成第一版模型、结果和报告。
- Advanced solution：按具体题意、真实数据和约束深化后的逐问解法。
- Outstanding solution：复现官方获奖论文中可验证的模型链、代码、实验结果和论文级分析；当前正式标记 15 篇 O 奖论文复现。

在线站点：

[https://wxj630.github.io/Math-Modeling-BAO/](https://wxj630.github.io/Math-Modeling-BAO/)

当前覆盖：

- MCM/ICM：66 道赛题、371 个逐问 advanced 实验、371 个通用 baseline。
- CUMCM：63 道赛题、243 个逐问 advanced 实验、243 个通用 baseline。

## Outstanding 复现进度

当前对外正式标记的 O 奖复现共 15 篇。仓库中可能保留后续候选或实验草稿，但 README 与教程入口先只把下面 15 篇作为已复现口径。

### Batch 1：三大题型 × MCM/CUMCM

| 题型 | 竞赛题目 | O 论文 | 复现入口 |
|---|---|---|---|
| 微分方程/动态系统 | MCM 2015-A Ebola | `35532` | [report](mcm/outstanding_solutions/2015/A/35532/report.md) |
| 微分方程/动态系统 | CUMCM 2018-A 高温作业专用服装 | `A466` | [report](cumcm/outstanding_solutions/2018/A/A466/report.md) |
| 运筹优化 | MCM 2017-B Merge After Toll | `69427` | [report](mcm/outstanding_solutions/2017/B/69427/report.md) |
| 运筹优化 | CUMCM 2020-B 穿越沙漠 | `B108` | [report](cumcm/outstanding_solutions/2020/B/B108/report.md) |
| 数据建模 | MCM 2019-C Opioids | `1901213` | [report](mcm/outstanding_solutions/2019/C/1901213/report.md) |
| 数据建模 | CUMCM 2020-C 中小微企业信贷 | `C227` | [report](cumcm/outstanding_solutions/2020/C/C227/report.md) |

### Batch 2：2023-2025 ABC 代表样例

| 年份 | 题目 | O 论文 | 复现入口 |
|---|---|---|---|
| 2023 | MCM 2023-A Drought-Stricken Plant Communities | `2309229` | [report](mcm/outstanding_solutions/2023/A/2309229/report.md) |
| 2023 | MCM 2023-B The Maasai Mara | `2315379` | [report](mcm/outstanding_solutions/2023/B/2315379/report.md) |
| 2023 | MCM 2023-C Wordle | `2307946` | [report](mcm/outstanding_solutions/2023/C/2307946/report.md) |
| 2024 | MCM 2024-A Resource Availability and Sex Ratios | `2407093` | [report](mcm/outstanding_solutions/2024/A/2407093/report.md) |
| 2024 | MCM 2024-B Searching for a Submersible | `2419984` | [report](mcm/outstanding_solutions/2024/B/2419984/report.md) |
| 2024 | MCM 2024-C Momentum in Tennis | `2401298` | [report](mcm/outstanding_solutions/2024/C/2401298/report.md) |
| 2025 | MCM 2025-A Stair Wear | `2501909` | [report](mcm/outstanding_solutions/2025/A/2501909/report.md) |
| 2025 | MCM 2025-B Sustainable Tourism in Juneau | `2504448` | [report](mcm/outstanding_solutions/2025/B/2504448/report.md) |
| 2025 | MCM 2025-C Olympic Medal Predictions | `2505964` | [report](mcm/outstanding_solutions/2025/C/2505964/report.md) |

## 大文件和 PDF 报告

`../Math-Modeling-BAO-Reports/` 是本地/外部资料库，不进入主 Git 仓库。主仓库只保存教程源码、建模代码、轻量结果、复现说明和索引；PDF 原文、OCR 全量结果、压缩包和大体积附件保留在本机、服务器或对象存储中。

当前纯 PDF 数据集已整理到 ModelScope，方便国内访问：

[https://www.modelscope.cn/datasets/wuxiaojun/Math-Modeling-BAO](https://www.modelscope.cn/datasets/wuxiaojun/Math-Modeling-BAO)

PDF 索引页见 [PDF 论文库](docs/reference/report-pdf-library.md)。主仓库只放 manifest、来源链接、校验和和下载脚本；只有在确实需要二进制版本管理时，才考虑单独建 data repo 并使用 Git LFS，不把 3GB+ 的报告资料放进主仓库历史。

## 内容结构

| 路径 | 说明 |
|---|---|
| `docs/` | VitePress 教程站源码。 |
| `docs/best_practie/` | Best Practice 栏目，沉淀评奖标准、B/A/O 递进、数据与文献、混合题型、求解器选择和典型赛题案例。 |
| `docs/tutorial/` | 总教程入口、赛题阅读方法、baseline、advanced、outstanding 三层说明。 |
| `docs/mcm-track/` | MCM/ICM 赛题入口、赛题整体索引、逐问材料附录。 |
| `docs/cumcm-track/` | CUMCM 赛题入口、赛题整体索引、逐问材料附录。 |
| `docs/case-studies/` | 代表案例拆解。 |
| `docs/reference/` | 归档路径说明和复现命令。 |
| `mcm/` | MCM/ICM baseline 与 advanced 逐问代码、报告、结果和轻量产物。 |
| `mcm/outstanding_solutions/` | MCM/ICM 获奖论文复现代码、报告、结果和轻量产物。 |
| `cumcm/` | CUMCM baseline 与 advanced 逐问代码、报告、结果和轻量产物。 |
| `tools/build_problem_pages.py` | 从现有 CSV 生成赛题整体索引和每道赛题页。 |
| `.github/workflows/deploy.yml` | GitHub Pages 自动部署 workflow。 |

大体积官方附件、原始压缩包、解压数据和本地实验草稿不进入 Git，相关规则写在 `.gitignore`。教程页保留路径说明，但线上仓库只保存阅读和复现教程需要的轻量内容。

## 本地预览

安装前端依赖：

```bash
npm install
```

启动 VitePress：

```bash
npm run docs:dev
```

构建静态站点：

```bash
npm run docs:build
```

## 复现解法

Python 逐问解法依赖保留在 `requirements.txt`，只包含教程复现需要的数值计算、数据处理、绘图和测试包。

```bash
python -m pip install -r requirements.txt
```

常用命令见：

- [运行与复现](docs/reference/reproduce.md)
- [归档路径说明](docs/reference/archive-map.md)

重建赛题页：

```bash
python tools/build_problem_pages.py
```

## 发布

推送到 `main` 后，GitHub Actions 会自动构建 `docs/` 并发布到 GitHub Pages：

```bash
git push origin main
```

部署目标是：

[https://wxj630.github.io/Math-Modeling-BAO/](https://wxj630.github.io/Math-Modeling-BAO/)
