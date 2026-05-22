# CUMCM 可运行教程

本目录把 CUMCM 题面整理、模型参考、经典模型代码实现和可复现实验结果放在一个地方。

## 目录

- `problems/`：每题题面、每问/小问、模型参考。
- `solutions/`：每题独立 `solution.py`。
- `results/`：脚本运行得到的 `result.json`。
- `reports/`：由结果生成的实验报告。
- `lib/`：可复用经典模型实现。
- `problem_index.csv`：每题核心、推荐模型、代码/结果/报告路径总表。
- `question_tasks.csv`：逐问任务拆解、适合模型与可运行脚本路径。
- `source_materials/`：赛题原文件、官网下载压缩包、解压附件、重抽取材料与清洗 markdown 的统一归档。

## 运行

运行全部题目：

```bash
python cumcm/scripts/run_all.py
```

本仓库当前推荐使用已有虚拟环境运行：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/run_all.py
```

依赖安装统一使用 `uv`，例如旧版 `.xls` 附件读取依赖 `xlrd`：

```bash
uv pip install --python /Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python -r requirements.txt
```

运行单题示例：

```bash
python cumcm/solutions/2020/A/solution.py
```

## 说明

当前代码为每题生成与题面模型匹配的经典模型基线实验。对于有附件数据的题目，可以在对应 `solution.py` 中替换数据读取和目标函数，报告结构会保持稳定。

## 题目索引

- `2010-A`：[cumcm/problems/2010/A.md](cumcm/problems/2010/A.md) / [cumcm/solutions/2010/A/solution.py](cumcm/solutions/2010/A/solution.py) / [cumcm/reports/2010/A/report.md](cumcm/reports/2010/A/report.md)
- `2010-B`：[cumcm/problems/2010/B.md](cumcm/problems/2010/B.md) / [cumcm/solutions/2010/B/solution.py](cumcm/solutions/2010/B/solution.py) / [cumcm/reports/2010/B/report.md](cumcm/reports/2010/B/report.md)
- `2010-C`：[cumcm/problems/2010/C.md](cumcm/problems/2010/C.md) / [cumcm/solutions/2010/C/solution.py](cumcm/solutions/2010/C/solution.py) / [cumcm/reports/2010/C/report.md](cumcm/reports/2010/C/report.md)
- `2010-D`：[cumcm/problems/2010/D.md](cumcm/problems/2010/D.md) / [cumcm/solutions/2010/D/solution.py](cumcm/solutions/2010/D/solution.py) / [cumcm/reports/2010/D/report.md](cumcm/reports/2010/D/report.md)
- `2011-A`：[cumcm/problems/2011/A.md](cumcm/problems/2011/A.md) / [cumcm/solutions/2011/A/solution.py](cumcm/solutions/2011/A/solution.py) / [cumcm/reports/2011/A/report.md](cumcm/reports/2011/A/report.md)
- `2011-B`：[cumcm/problems/2011/B.md](cumcm/problems/2011/B.md) / [cumcm/solutions/2011/B/solution.py](cumcm/solutions/2011/B/solution.py) / [cumcm/reports/2011/B/report.md](cumcm/reports/2011/B/report.md)
- `2011-C`：[cumcm/problems/2011/C.md](cumcm/problems/2011/C.md) / [cumcm/solutions/2011/C/solution.py](cumcm/solutions/2011/C/solution.py) / [cumcm/reports/2011/C/report.md](cumcm/reports/2011/C/report.md)
- `2011-D`：[cumcm/problems/2011/D.md](cumcm/problems/2011/D.md) / [cumcm/solutions/2011/D/solution.py](cumcm/solutions/2011/D/solution.py) / [cumcm/reports/2011/D/report.md](cumcm/reports/2011/D/report.md)
- `2014-A`：[cumcm/problems/2014/A.md](cumcm/problems/2014/A.md) / [cumcm/solutions/2014/A/solution.py](cumcm/solutions/2014/A/solution.py) / [cumcm/reports/2014/A/report.md](cumcm/reports/2014/A/report.md)
- `2014-B`：[cumcm/problems/2014/B.md](cumcm/problems/2014/B.md) / [cumcm/solutions/2014/B/solution.py](cumcm/solutions/2014/B/solution.py) / [cumcm/reports/2014/B/report.md](cumcm/reports/2014/B/report.md)
- `2014-C`：[cumcm/problems/2014/C.md](cumcm/problems/2014/C.md) / [cumcm/solutions/2014/C/solution.py](cumcm/solutions/2014/C/solution.py) / [cumcm/reports/2014/C/report.md](cumcm/reports/2014/C/report.md)
- `2014-D`：[cumcm/problems/2014/D.md](cumcm/problems/2014/D.md) / [cumcm/solutions/2014/D/solution.py](cumcm/solutions/2014/D/solution.py) / [cumcm/reports/2014/D/report.md](cumcm/reports/2014/D/report.md)
- `2015-A`：[cumcm/problems/2015/A.md](cumcm/problems/2015/A.md) / [cumcm/solutions/2015/A/solution.py](cumcm/solutions/2015/A/solution.py) / [cumcm/reports/2015/A/report.md](cumcm/reports/2015/A/report.md)
- `2015-B`：[cumcm/problems/2015/B.md](cumcm/problems/2015/B.md) / [cumcm/solutions/2015/B/solution.py](cumcm/solutions/2015/B/solution.py) / [cumcm/reports/2015/B/report.md](cumcm/reports/2015/B/report.md)
- `2015-C`：[cumcm/problems/2015/C.md](cumcm/problems/2015/C.md) / [cumcm/solutions/2015/C/solution.py](cumcm/solutions/2015/C/solution.py) / [cumcm/reports/2015/C/report.md](cumcm/reports/2015/C/report.md)
- `2015-D`：[cumcm/problems/2015/D.md](cumcm/problems/2015/D.md) / [cumcm/solutions/2015/D/solution.py](cumcm/solutions/2015/D/solution.py) / [cumcm/reports/2015/D/report.md](cumcm/reports/2015/D/report.md)
- `2016-A`：[cumcm/problems/2016/A.md](cumcm/problems/2016/A.md) / [cumcm/solutions/2016/A/solution.py](cumcm/solutions/2016/A/solution.py) / [cumcm/reports/2016/A/report.md](cumcm/reports/2016/A/report.md)
- `2016-B`：[cumcm/problems/2016/B.md](cumcm/problems/2016/B.md) / [cumcm/solutions/2016/B/solution.py](cumcm/solutions/2016/B/solution.py) / [cumcm/reports/2016/B/report.md](cumcm/reports/2016/B/report.md)
- `2016-C`：[cumcm/problems/2016/C.md](cumcm/problems/2016/C.md) / [cumcm/solutions/2016/C/solution.py](cumcm/solutions/2016/C/solution.py) / [cumcm/reports/2016/C/report.md](cumcm/reports/2016/C/report.md)
- `2016-D`：[cumcm/problems/2016/D.md](cumcm/problems/2016/D.md) / [cumcm/solutions/2016/D/solution.py](cumcm/solutions/2016/D/solution.py) / [cumcm/reports/2016/D/report.md](cumcm/reports/2016/D/report.md)
- `2017-A`：[cumcm/problems/2017/A.md](cumcm/problems/2017/A.md) / [cumcm/solutions/2017/A/solution.py](cumcm/solutions/2017/A/solution.py) / [cumcm/reports/2017/A/report.md](cumcm/reports/2017/A/report.md)
- `2017-B`：[cumcm/problems/2017/B.md](cumcm/problems/2017/B.md) / [cumcm/solutions/2017/B/solution.py](cumcm/solutions/2017/B/solution.py) / [cumcm/reports/2017/B/report.md](cumcm/reports/2017/B/report.md)
- `2017-C`：[cumcm/problems/2017/C.md](cumcm/problems/2017/C.md) / [cumcm/solutions/2017/C/solution.py](cumcm/solutions/2017/C/solution.py) / [cumcm/reports/2017/C/report.md](cumcm/reports/2017/C/report.md)
- `2017-D`：[cumcm/problems/2017/D.md](cumcm/problems/2017/D.md) / [cumcm/solutions/2017/D/solution.py](cumcm/solutions/2017/D/solution.py) / [cumcm/reports/2017/D/report.md](cumcm/reports/2017/D/report.md)
- `2018-A`：[cumcm/problems/2018/A.md](cumcm/problems/2018/A.md) / [cumcm/solutions/2018/A/solution.py](cumcm/solutions/2018/A/solution.py) / [cumcm/reports/2018/A/report.md](cumcm/reports/2018/A/report.md)
- `2018-B`：[cumcm/problems/2018/B.md](cumcm/problems/2018/B.md) / [cumcm/solutions/2018/B/solution.py](cumcm/solutions/2018/B/solution.py) / [cumcm/reports/2018/B/report.md](cumcm/reports/2018/B/report.md)
- `2018-C`：[cumcm/problems/2018/C.md](cumcm/problems/2018/C.md) / [cumcm/solutions/2018/C/solution.py](cumcm/solutions/2018/C/solution.py) / [cumcm/reports/2018/C/report.md](cumcm/reports/2018/C/report.md)
- `2018-D`：[cumcm/problems/2018/D.md](cumcm/problems/2018/D.md) / [cumcm/solutions/2018/D/solution.py](cumcm/solutions/2018/D/solution.py) / [cumcm/reports/2018/D/report.md](cumcm/reports/2018/D/report.md)
- `2019-A`：[cumcm/problems/2019/A.md](cumcm/problems/2019/A.md) / [cumcm/solutions/2019/A/solution.py](cumcm/solutions/2019/A/solution.py) / [cumcm/reports/2019/A/report.md](cumcm/reports/2019/A/report.md)
- `2019-B`：[cumcm/problems/2019/B.md](cumcm/problems/2019/B.md) / [cumcm/solutions/2019/B/solution.py](cumcm/solutions/2019/B/solution.py) / [cumcm/reports/2019/B/report.md](cumcm/reports/2019/B/report.md)
- `2019-C`：[cumcm/problems/2019/C.md](cumcm/problems/2019/C.md) / [cumcm/solutions/2019/C/solution.py](cumcm/solutions/2019/C/solution.py) / [cumcm/reports/2019/C/report.md](cumcm/reports/2019/C/report.md)
- `2019-D`：[cumcm/problems/2019/D.md](cumcm/problems/2019/D.md) / [cumcm/solutions/2019/D/solution.py](cumcm/solutions/2019/D/solution.py) / [cumcm/reports/2019/D/report.md](cumcm/reports/2019/D/report.md)
- `2019-E`：[cumcm/problems/2019/E.md](cumcm/problems/2019/E.md) / [cumcm/solutions/2019/E/solution.py](cumcm/solutions/2019/E/solution.py) / [cumcm/reports/2019/E/report.md](cumcm/reports/2019/E/report.md)
- `2020-A`：[cumcm/problems/2020/A.md](cumcm/problems/2020/A.md) / [cumcm/solutions/2020/A/solution.py](cumcm/solutions/2020/A/solution.py) / [cumcm/reports/2020/A/report.md](cumcm/reports/2020/A/report.md)
- `2020-B`：[cumcm/problems/2020/B.md](cumcm/problems/2020/B.md) / [cumcm/solutions/2020/B/solution.py](cumcm/solutions/2020/B/solution.py) / [cumcm/reports/2020/B/report.md](cumcm/reports/2020/B/report.md)
- `2020-C`：[cumcm/problems/2020/C.md](cumcm/problems/2020/C.md) / [cumcm/solutions/2020/C/solution.py](cumcm/solutions/2020/C/solution.py) / [cumcm/reports/2020/C/report.md](cumcm/reports/2020/C/report.md)
- `2020-D`：[cumcm/problems/2020/D.md](cumcm/problems/2020/D.md) / [cumcm/solutions/2020/D/solution.py](cumcm/solutions/2020/D/solution.py) / [cumcm/reports/2020/D/report.md](cumcm/reports/2020/D/report.md)
- `2020-E`：[cumcm/problems/2020/E.md](cumcm/problems/2020/E.md) / [cumcm/solutions/2020/E/solution.py](cumcm/solutions/2020/E/solution.py) / [cumcm/reports/2020/E/report.md](cumcm/reports/2020/E/report.md)
- `2021-A`：[cumcm/problems/2021/A.md](cumcm/problems/2021/A.md) / [cumcm/solutions/2021/A/solution.py](cumcm/solutions/2021/A/solution.py) / [cumcm/reports/2021/A/report.md](cumcm/reports/2021/A/report.md)
- `2021-B`：[cumcm/problems/2021/B.md](cumcm/problems/2021/B.md) / [cumcm/solutions/2021/B/solution.py](cumcm/solutions/2021/B/solution.py) / [cumcm/reports/2021/B/report.md](cumcm/reports/2021/B/report.md)
- `2021-C`：[cumcm/problems/2021/C.md](cumcm/problems/2021/C.md) / [cumcm/solutions/2021/C/solution.py](cumcm/solutions/2021/C/solution.py) / [cumcm/reports/2021/C/report.md](cumcm/reports/2021/C/report.md)
- `2021-D`：[cumcm/problems/2021/D.md](cumcm/problems/2021/D.md) / [cumcm/solutions/2021/D/solution.py](cumcm/solutions/2021/D/solution.py) / [cumcm/reports/2021/D/report.md](cumcm/reports/2021/D/report.md)
- `2021-E`：[cumcm/problems/2021/E.md](cumcm/problems/2021/E.md) / [cumcm/solutions/2021/E/solution.py](cumcm/solutions/2021/E/solution.py) / [cumcm/reports/2021/E/report.md](cumcm/reports/2021/E/report.md)
- `2022-B`：[cumcm/problems/2022/B.md](cumcm/problems/2022/B.md) / [cumcm/solutions/2022/B/solution.py](cumcm/solutions/2022/B/solution.py) / [cumcm/reports/2022/B/report.md](cumcm/reports/2022/B/report.md)
- `2022-D`：[cumcm/problems/2022/D.md](cumcm/problems/2022/D.md) / [cumcm/solutions/2022/D/solution.py](cumcm/solutions/2022/D/solution.py) / [cumcm/reports/2022/D/report.md](cumcm/reports/2022/D/report.md)
- `2023-D`：[cumcm/problems/2023/D.md](cumcm/problems/2023/D.md) / [cumcm/solutions/2023/D/solution.py](cumcm/solutions/2023/D/solution.py) / [cumcm/reports/2023/D/report.md](cumcm/reports/2023/D/report.md)
- `2024-A`：[cumcm/problems/2024/A.md](cumcm/problems/2024/A.md) / [cumcm/solutions/2024/A/solution.py](cumcm/solutions/2024/A/solution.py) / [cumcm/reports/2024/A/report.md](cumcm/reports/2024/A/report.md)
- `2024-B`：[cumcm/problems/2024/B.md](cumcm/problems/2024/B.md) / [cumcm/solutions/2024/B/solution.py](cumcm/solutions/2024/B/solution.py) / [cumcm/reports/2024/B/report.md](cumcm/reports/2024/B/report.md)
- `2024-C`：[cumcm/problems/2024/C.md](cumcm/problems/2024/C.md) / [cumcm/solutions/2024/C/solution.py](cumcm/solutions/2024/C/solution.py) / [cumcm/reports/2024/C/report.md](cumcm/reports/2024/C/report.md)
- `2024-D`：[cumcm/problems/2024/D.md](cumcm/problems/2024/D.md) / [cumcm/solutions/2024/D/solution.py](cumcm/solutions/2024/D/solution.py) / [cumcm/reports/2024/D/report.md](cumcm/reports/2024/D/report.md)
- `2024-E`：[cumcm/problems/2024/E.md](cumcm/problems/2024/E.md) / [cumcm/solutions/2024/E/solution.py](cumcm/solutions/2024/E/solution.py) / [cumcm/reports/2024/E/report.md](cumcm/reports/2024/E/report.md)

## 逐问代码、结果和报告

本目录已经把每道题拆到“每一问”级别：

- `question_solutions/`：每一问一个独立 `solution.py`，例如 `question_solutions/2024/A/q01/solution.py`。
- `question_results/`：每一问脚本运行得到的 `result.json`。
- `question_reports/`：每一问的建模求解实验报告，包含任务、建模假设、变量、公式/目标函数、求解过程、运行结果。
- `question_artifacts/`：每一问脚本生成的实验表 `experiment_table.csv`，用于论文表格、画图或继续导出 `result*.xlsx`。
- `generic_baselines/`：每一问的第一版通用基线代码、结果、报告和实验表，用来保留从通用模型到题意专用模型的改进过程。
- `question_solution_index.csv`：逐问代码、结果、报告路径总表。
- `question_solution_index.json`：同上，JSON 版本。
- `attachment_manifest.json` / `attachment_manifest.csv`：从 `/Users/wuxiaojun/Documents/Playground/cumcm_unzipped` 与 `cumcm_reextract` 扫描得到的官方附件清单。

运行全部逐问实验：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/run_question_all.py
```

重新生成逐问脚本：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/build_question_solutions.py
```

重新扫描官方附件：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/build_attachment_manifest.py
```

整理赛题原文件、下载数据和附件：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/organize_source_materials.py
```

验证逐问产物是否齐全：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/verify_question_outputs.py
```

验证附件是否接入逐问实验：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/verify_attachment_integration.py
```

归档或重建通用基线：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/archive_generic_baselines.py --all
```

同步逐问报告链接到 Obsidian：

```bash
/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python cumcm/scripts/sync_question_reports_to_obsidian.py
```

### 当前完成度说明

逐问层已经覆盖 196 个问题，每一问均有独立 Python 入口、`result.json`、`report.md` 和 `experiment_table.csv`。报告会写明题目原问、任务拆解、适配模型、变量、约束、公式、运行方式、数据来源、实验结果与解释。

通用基线归档已经覆盖 196 个问题，保存在 `generic_baselines/`。这些基线代表专用化之前的第一版可运行模型，后续深化某道题时不再删除通用解法，而是保留为“旧版思路/对照实验”。

附件接入状态：当前附件清单覆盖 47 道题、209 个附件；逐问结果中 123 问已经读取真实 CSV/XLSX/XLS 数值附件，73 问使用题目原文中的参数或表格数字建模，0 问使用 synthetic 占位数据。

已做题意专门化的题目包括：
- `2022-B`：无人机纯方位无源定位、夹角残差最小二乘、匿名发射机枚举、圆形编队多轮调整和锥形编队投影调整。
- `2022-D`：气象报文卫星通信传输、主站轮转共享、便携副站重复发送概率覆盖、K=7/K=8 最大 N 搜索和可行时隙排程校验。
- `2023-D`：圈养湖羊繁殖周期、基础母羊/种公羊规模、羊栏日历排程、年化出栏和不确定性期望损失预案。
- `2024-A`：板凳龙螺线运动学、碰撞扫描、调头路径和速度约束。
- `2024-B`：生产过程中的抽样检测、零配件/成品检测、拆解决策、多工序装配树和抽样不确定性鲁棒重算。
- `2024-C`：农作物种植策略、附件 Excel 语义解析、轮作/豆类窗口约束、滞销/半价销售收益、趋势风险和相关 Monte Carlo 策略比较。
- `2024-D`：航空深弹命中概率、触发/定深引信几何事件、截尾正态深度误差和 9 枚阵列投弹优化。
- `2024-E`：交通流量管控、884 万条车辆记录分块摘要、交叉口分时段相位流量、信号配时优化、五一巡游车识别和临时管控效果评价。

需要注意：其余多数题仍是按题面语义生成的经典模型可运行实验，不等同于完整竞赛级最优论文解。后续若要冲竞赛论文质量，应按题目逐个深化专用算法、补充图表和敏感性分析。
