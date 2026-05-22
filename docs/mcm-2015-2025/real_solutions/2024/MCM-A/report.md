# 2024 MCM-A Resource Availability and Sex Ratios

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets_extracted/2024/Resource Availability and Sex Ratios.pdf`。
- 本题无 COMAP 数值附件；脚本只使用官方 PDF 中的性别比例端点和显式系统动力学假设，不使用随机占位数据。

## 官方题面参数
- 低食物环境雄性比例：0.78。
- 高食物环境雄性比例：0.56。

## 每问结果
### Q1 更大生态系统影响
- 模型：lamprey-host-parasite-food-web difference equations with resource-dependent sex ratio and lamprey reduction pressure。
- 七鳃鳗减少情景解释：reducing lampreys relieves host fish but also reduces lamprey food-web value and parasite habitat。

### Q2 七鳃鳗种群优缺点
- 优点：
- male-biased low-food cohorts preserve mating opportunities when larval resources are poor
- resource-sensitive sex ratios prevent overproduction of females when juvenile survival is low
- adaptive ratios can dampen population overshoot relative to a fixed sex ratio
- 缺点：
- strong male bias lowers female availability and can bottleneck reproduction
- sex-ratio plasticity makes population forecasts more sensitive to resource measurement error
- host-fish damage can remain high if lamprey survival is also resource-supported

### Q3 生态系统稳定性
- 自适应 vs 固定性别比稳定性差值：-0.0012。

### Q4 对其他生物的优势
- 权衡：variable sex ratios can indirectly help parasites and lamprey consumers by stabilizing lamprey persistence, but high lamprey density harms host fish。

## 输出产物
- `sex_ratio_response.csv`：资源-雄性比例响应曲线。
- `ecosystem_trajectories.csv`：月度生态状态轨迹。
- `stability_surface.csv`：资源与七鳃鳗控制压力稳定性网格。
- `lamprey_tradeoff_frontier.png`：性别比和稳定性权衡图。
