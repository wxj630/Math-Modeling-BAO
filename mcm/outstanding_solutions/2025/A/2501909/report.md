# 2025 MCM-A Outstanding 复现：2501909

## 复现对象
- 获奖论文：`2501909`，Stair Wear: Traces of History
- OCR 来源：`Outstanding_Solutions/MCM/OCR-results/A/2501909/2501909.md`
- PDF 来源：`Outstanding_Solutions/MCM/PDF-2025/A/2501909.pdf`
- 复现定位：以当前已验证的 MCM-A real solution 为计算核，对齐论文中的 WVM/WDM、年龄可靠性、修复检测和材料一致性叙事。

## 问题与建模
论文 2501909 将台阶磨损拆成 Wear Volume Model 和 Wear Distribution Model：先用 Archard wear law 把磨损深度、材料硬度、脚步载荷和时间联系起来，再用横向/纵向磨损分布判断行走方向、并排行走人数和修复异常。当前计算核已经包含非破坏测量模板、逆磨损模型、年龄可靠性网格和修复候选检测，因此适合作为该论文的可验证复现版本。

## 代码与实验
- `solution.py` 读取 `docs/mcm-2015-2025/real_solutions/2025/MCM-A/result.json`。
- 复制当前 advanced 的测量模板、年龄网格、磨损剖面、修复候选和可视化 artifacts。
- 在 `result.json` 中补充获奖论文方法、复现范围和相对 advanced 的升级说明。

## 关键结果
- 测量原则：non_destructive, low_cost, small_team_minimal_tools。
- 中位中心磨损深度：4.3 mm。
- 估计日使用人数：72.67。
- 偏好方向：up；并排行走模式：mixed。
- 年龄估计：340.3 年，可靠区间 [283.6, 397.0]。
- 修复候选数量：2。

## 相对 Advanced 的优势
- Advanced 已经给出可运行的逆磨损计算和 artifacts；Outstanding 把这些结果重组为获奖论文的 WVM/WDM 主线。
- 报告显式连接 Archard 磨损、测量矩阵、年龄可靠性、修复检测和材料来源，便于写成完整论文段落。
- 后续可以在此基础上加入真实扫描矩阵和 Gaussian mixture 横向/纵向分布拟合，替代当前 worked example。

## 输出产物
- `age_reliability_grid`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/age_reliability_grid.csv`
- `measurement_template`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/measurement_template.csv`
- `renovation_candidates`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/renovation_candidates.csv`
- `traffic_pattern_summary`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/traffic_pattern_summary.csv`
- `wear_cross_section`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/wear_cross_section.png`
- `wear_profile`：`mcm/outstanding_solutions/2025/A/2501909/artifacts/wear_profile.csv`
