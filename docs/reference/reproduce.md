# 运行与复现

本仓库的 Python 解法建议使用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate
```

依赖安装：

```bash
python -m pip install -r requirements.txt
```

## 运行 MCM/ICM 解法

运行全部逐问 advanced 解法：

```bash
python mcm/scripts/run_question_all.py
```

验证真实数据接入：

```bash
python mcm/scripts/verify_real_data_integration.py
```

重建 baseline 归档：

```bash
python mcm/scripts/archive_generic_baselines.py --all
```

运行正式 outstanding 获奖论文复现：

```bash
python tools/run_outstanding_reproductions.py --formal --keep-going
```

## 运行 CUMCM 解法

运行全部逐问 advanced 解法：

```bash
python cumcm/scripts/run_question_all.py
```

验证逐问产物：

```bash
python cumcm/scripts/verify_question_outputs.py
```

验证附件接入：

```bash
python cumcm/scripts/verify_attachment_integration.py
```

重建 baseline 归档：

```bash
python cumcm/scripts/archive_generic_baselines.py --all
```

只运行 Batch 1（三大题型 × MCM/CUMCM）：

```bash
python tools/run_outstanding_reproductions.py --batch 1 --keep-going
```

只运行 Batch 2（2023-2025 MCM ABC）：

```bash
python tools/run_outstanding_reproductions.py --batch 2 --keep-going
```

## 运行教程站

安装前端依赖：

```bash
npm install
```

本地预览：

```bash
npm run docs:dev
```

构建 GitHub Pages 静态站点：

```bash
npm run docs:build
```

## 重建赛题页

只重建赛题整体索引，不覆盖单题页面：

```bash
python tools/build_problem_pages.py --index-only
```

完整重建赛题整体索引和每道赛题页，不会重跑实验：

```bash
python tools/build_problem_pages.py
```
