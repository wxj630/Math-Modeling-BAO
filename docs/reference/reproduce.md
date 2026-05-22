# 运行与复现

本仓库的 Python 解法建议使用已有虚拟环境：

```bash
source /Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/activate
```

依赖安装：

```bash
uv pip install -e /Users/wuxiaojun/code/Math-Modeling-World
uv pip install -r /Users/wuxiaojun/code/Math-Modeling-World/requirements.txt
```

## 运行 MCM/ICM 解法

运行全部逐问 advanced 解法：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/scripts/run_question_all.py
```

验证真实数据接入：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/scripts/verify_real_data_integration.py
```

重建 baseline 归档：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/scripts/archive_generic_baselines.py --all
```

## 运行 CUMCM 解法

运行全部逐问 advanced 解法：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/run_question_all.py
```

验证逐问产物：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/verify_question_outputs.py
```

验证附件接入：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/verify_attachment_integration.py
```

重建 baseline 归档：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/cumcm/scripts/archive_generic_baselines.py --all
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
