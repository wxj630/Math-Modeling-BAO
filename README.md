# Math-Modeling-World

MCM/ICM 与 CUMCM 建模教程站。仓库当前聚焦三层解法归档：

- Baseline solution：最低可运行建模脚手架，用来快速形成第一版模型、结果和报告。
- Advanced solution：按具体题意、真实数据和约束深化后的逐问解法。
- Outstanding solution：预留论文级表达、鲁棒性分析和可视化打磨位置，后续逐题补充。

在线站点：

[https://wxj630.github.io/Math-Modeling-World/](https://wxj630.github.io/Math-Modeling-World/)

## 内容结构

| 路径 | 说明 |
|---|---|
| `docs/` | VitePress 教程站源码。 |
| `docs/tutorial/` | 总教程入口、baseline、advanced、outstanding 三层说明。 |
| `docs/mcm-track/` | MCM/ICM 学习路线和逐问解法索引。 |
| `docs/cumcm-track/` | CUMCM 学习路线和逐问解法索引。 |
| `docs/case-studies/` | 代表案例拆解。 |
| `docs/reference/` | 归档路径说明和复现命令。 |
| `mcm/` | MCM/ICM baseline 与 advanced 逐问代码、报告、结果和轻量产物。 |
| `cumcm/` | CUMCM baseline 与 advanced 逐问代码、报告、结果和轻量产物。 |
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

## 发布

推送到 `main` 后，GitHub Actions 会自动构建 `docs/` 并发布到 GitHub Pages：

```bash
git push origin main
```

部署目标是：

[https://wxj630.github.io/Math-Modeling-World/](https://wxj630.github.io/Math-Modeling-World/)
