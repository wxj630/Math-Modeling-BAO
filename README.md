# Math-Modeling-BAO

MCM/ICM 与 CUMCM 建模教程站。仓库当前以完整赛题为入口，再把每道题的小问递进链连接到三层解法归档：

- Baseline solution：最低可运行建模脚手架，用来快速形成第一版模型、结果和报告。
- Advanced solution：按具体题意、真实数据和约束深化后的逐问解法。
- Outstanding solution：复现官方获奖论文中可验证的模型链、代码、实验结果和论文级分析；当前已落地 MCM 2025-C / 2505964。

在线站点：

[https://wxj630.github.io/Math-Modeling-BAO/](https://wxj630.github.io/Math-Modeling-BAO/)

当前覆盖：

- MCM/ICM：66 道赛题、371 个逐问 advanced 实验、371 个通用 baseline。
- CUMCM：63 道赛题、243 个逐问 advanced 实验、243 个通用 baseline。

## 内容结构

| 路径 | 说明 |
|---|---|
| `docs/` | VitePress 教程站源码。 |
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
