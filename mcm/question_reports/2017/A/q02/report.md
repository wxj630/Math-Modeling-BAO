# 2017-A q02：10-20 座小坝数量与坝址推荐

## 题目原问
Provide a detailed analysis of removing Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River; support a recommendation for number and placement.

## 适合模型
在官方 10-20 座小坝范围内扫描 dam_count frontier，用 storage、flood attenuation、low-flow support、redundancy 和 coordination penalty 得到 water management index，并给出 0-100 归一化河道坐标坝址。对应模型：离散优化、设施选址、容量规划、多目标权衡。

## 数据与真实性
- 数据类型：official_statement_parameters。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2017`。
- 行数/记录数：{'official_problem_parameters': 5}。
- 本脚本只使用 COMAP 官方题面参数和显式建模假设，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 10-20 座小坝系统设计
- Kariba reference index：100.0。
- 推荐小坝数量：15。
- 推荐系统 water management index：103.110093。
- 说明：Use a distributed 15-dam system: enough redundancy to match Kariba-level management while avoiding the coordination penalty of 18-20 dams.

#### 坝址计划

| dam_id | river_coordinate_0_100 | segment | local_storage_share_pct | primary_role |
|---|---|---|---|---|
| D01 | 6.0 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D02 | 12.29 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D03 | 18.57 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D04 | 24.86 | upstream_lake_control | 7.2 | replace Kariba storage and regulate lake-level transitions |
| D05 | 31.14 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D06 | 37.43 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D07 | 43.71 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D08 | 50.0 | mid_river_flood_buffer | 7.2 | attenuate flood peaks and distribute release timing |
| D09 | 56.29 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D10 | 62.57 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D11 | 68.86 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D12 | 75.14 | downstream_power_and_irrigation | 6.133 | support low-flow releases for users |
| D13 | 81.43 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |
| D14 | 87.71 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |
| D15 | 94.0 | delta_ecology_protection | 6.133 | limit extreme exposure in sensitive downstream reaches |

## 模型限制
- 这是可复现的官方题面参数 Zambezi River 水库群规划实验；COMAP 没有提供独立 CSV/XLSX 附件，因此只使用 PDF 中三种选项、10-20 座小坝、同等或更高水量管理能力、正常/极端流量和暴露限制等要求。
- 成本、坝址坐标、容量、流量指数和暴露天数是显式工程规划假设，不是实测水文或施工数据；正式论文应补充 Zambezi 历史径流、Kariba 库容曲线、生态影响、地形地质、移民和工程造价数据校准。

## 运行方式
`.venv/bin/python mcm/question_solutions/2017/A/q02/solution.py`

## 输出
- `mcm/question_results/2017/A/q02/result.json`
- `mcm/question_reports/2017/A/q02/report.md`
- `mcm/question_artifacts/2017/A/q02`
