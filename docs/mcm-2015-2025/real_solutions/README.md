# MCM 真实数据解法

本目录只放两类解法：

- 读取 COMAP 官方附件数据（`.zip`、`.xlsx`、`.csv` 等）后运行的实验。
- 只依赖题面明确给出的参数、表格或公式，不额外随机造数的解析/仿真实验。

旧的 `advanced/` 目录和各题根目录 `solution.py` 已被 `../REALITY_CHECK.md` 标记为随机数据烟雾测试，不能当成真实赛题结果。

## 已开始重做

- [2024/MCM-C](2024/MCM-C/report.md)：使用官方 Wimbledon 逐分 CSV，完成发球校正势头流、决赛可视化、随机波动假设评估、换向预测、跨比赛泛化和教练备忘录。
- [2024/ICM-D](2024/ICM-D/report.md)：使用官方 Great Lakes Excel，完成分月目标水位、两坝控制规则、2017 敏感性、环境敏感性、Lake Ontario 专项和 IJC 备忘录。
- [2025/MCM-C](2025/MCM-C/report.md)：使用官方 `2025_Problem_C_Data.zip` 中的 Olympic CSV，完成奖牌榜预测、2024 留出评估、2028 预测区间、首枚奖牌估计、优势运动和教练效应候选分析。
- [2025/ICM-D](2025/ICM-D/report.md)：使用官方 Baltimore 路网、公交站、公交线路和 AADT CSV，完成桥梁走廊移除、公交站优先级、安全暴露和市长备忘录。

## CUMCM 风格逐问归档

顶层 [`mcm/`](https://github.com/wxj630/Math-Modeling-World/tree/main/mcm) 会把这些真实解法拆成逐问 `solution.py`、`result.json`、`report.md` 和实验产物。

当前逐问覆盖：

- `2024-C`：5 个逐问真实实验。
- `2024-D`：6 个逐问真实实验。
- `2025-C`：6 个逐问真实实验。
- `2025-D`：7 个逐问真实实验。

## 运行

```bash
.venv/bin/python docs/mcm-2015-2025/real_solutions/2024/MCM-C/solution.py
.venv/bin/python docs/mcm-2015-2025/real_solutions/2024/ICM-D/solution.py
.venv/bin/python docs/mcm-2015-2025/real_solutions/2025/MCM-C/solution.py
.venv/bin/python docs/mcm-2015-2025/real_solutions/2025/ICM-D/solution.py
.venv/bin/python scripts/build_mcm_real_archive.py
.venv/bin/python mcm/scripts/run_question_all.py
.venv/bin/python mcm/scripts/verify_real_data_integration.py
```
