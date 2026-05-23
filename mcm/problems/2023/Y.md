# 2023-Y MCM-Y: Understanding Used Sailboat Prices

- 来源目录：`docs/mcm-2015-2025/2023/MCM-C Understanding Used Sailboat Prices`
- 数据状态：见 `mcm/data_manifest.*` 与 `mcm/question_solution_index.*`。

# 题目与问题：MCM-Y: Understanding Used Sailboat Prices

## 每问/小问拆解
| 编号 | 小问/任务 | 适合模型 | 说明 |
|---|---|---|---|
| Q1 | 开发一个数学模型来解释每艘帆船的挂牌价格 提供的电子表格。包括您认为有用的任何预测因素。你可以借鉴 其他来源来了解给定帆船的其他特征（例如横梁、吃水、 排水量、索具、航行面积、船体材料、发动机小时数、睡眠容量、 净空、电子产品等）以及按年份和地区划分的经济数据。识别并 描述所使用的所有数据源。包括对估计精度的讨论 每个帆船型号的价格。 | 图论与网络流、优化规划模型、群体智能与启发式 | 涉及道路、航线、信息流、迁移、配送、网络韧性时，用最短路、最大流、中心性、连通性和 VRP/TSP。 |
| Q2 | 使用您的模型来解释地区对挂牌价格的影响（如果有）。讨论是否 任何区域效应在所有帆船变体中都是一致的。解决实际问题和 所记录的任何区域影响的统计显着性。 | 时间序列预测、统计回归与拟合、机器学习建模 | 问题核心是趋势、周期、波动或未来预测时，用移动平均、指数平滑、ARIMA/GARCH/灰色模型。 |
| Q3 | 讨论您对给定地理区域的建模如何在香港发挥作用 香港（特别行政区）市场。选择信息丰富的帆船子集，分为单体船 和双体船，来自提供的电子表格。查找可比较的挂牌价格数据 来自香港（特别行政区）市场的该子集。模拟香港的区域效应 如果有的话，香港（SAR）将在每艘帆船的价格上 你的子集。双体船和单体帆船的效果相同吗？ | 时间序列预测、统计回归与拟合、机器学习建模 | 问题核心是趋势、周期、波动或未来预测时，用移动平均、指数平滑、ARIMA/GARCH/灰色模型。 |
| Q4 | 确定并讨论您的任何其他有趣且信息丰富的推论或结论。 团队从数据中得出结论。 | 优化规划模型、统计回归与拟合、仿真与蒙特卡洛 | 目标明确且约束清楚时，用线性规划、非线性规划、整数规划或多目标规划求最优方案。 |
| Q5 | 为香港（特别行政区）帆船经纪人准备一份一到两页的报告。包括一个 一些精心挑选的图表可以帮助经纪人理解您的结论。 | 时间序列预测、机器学习建模、统计回归与拟合 | 问题核心是趋势、周期、波动或未来预测时，用移动平均、指数平滑、ARIMA/GARCH/灰色模型。 |

## 中文题面
## 第 1 页

| ©2023 COMAP 公司 | www.comap.com | www.mathmodels.org | | info@comap.com |
2023年MCM
问题 Y：了解二手帆船价格


照片来源：www.pixabay.com

与许多奢侈品一样，帆船的价值随着其老化和市场条件的变化而变化。
随附的“2023_MCM_Problem_Y_Boats.xlsx”文件包含约 3500 个船只的数据
36 至 56 英尺长的帆船在欧洲、加勒比海和美国的销售广告中
2020 年 12 月。一位划船爱好者向 COMAP 提供了这些数据。就像大多数现实世界的数据一样
集，它可能存在数据丢失或其他问题，需要在分析之前进行一些数据清理。

Excel 文件包括两个选项卡，一个用于单体帆船，一个用于双体船。在每个
选项卡，列标有制造商、变体、长度（以英尺为单位）、地理区域、
国家/地区/州、上市价格（以美元为单位）和年份（制造）。

对于给定的品牌、型号和年份，除了提供的 Excel 文件之外，还有许多其他来源
可以提供特定帆船特征的详细描述。你可以
用您选择的任何附加数据补充所提供的数据集；但是，您必须
在建模中包含“2023_MCM_Problem_Y_Boats.xlsx”中的数据。一定要充分
识别并记录所使用的任何补充数据的来源。

帆船经常通过经纪人出售。为了更好地了解帆船
市场，中国香港（特别行政区）的一位帆船经纪人已委托您的团队准备
关于二手帆船定价的报告。经纪人希望您：

• 开发一个数学模型来解释每艘帆船的挂牌价格
提供的电子表格。包括您认为有用的任何预测因素。你可以借鉴
其他来源来了解给定帆船的其他特征（例如横梁、吃水、
排水量、索具、航行面积、船体材料、发动机小时数、睡眠容量、
净空、电子产品等）以及按年份和地区划分的经济数据。识别并
描述所使用的所有数据源。包括对估计精度的讨论
每个帆船型号的价格。

• 使用您的模型来解释地区对挂牌价格的影响（如果有）。讨论是否
任何区域效应在所有帆船变体中都是一致的。解决实际问题和
所记录的任何区域影响的统计显着性。

## 第 2 页

| ©2023 COMAP 公司 | www.comap.com | www.mathmodels.org | | info@comap.com |
• 讨论您对给定地理区域的建模如何在香港发挥作用
香港（特别行政区）市场。选择信息丰富的帆船子集，分为单体船
和双体船，来自提供的电子表格。查找可比较的挂牌价格数据
来自香港（特别行政区）市场的该子集。模拟香港的区域效应
如果有的话，香港（SAR）将在每艘帆船的价格上
你的子集。双体船和单体帆船的效果相同吗？

• 确定并讨论您的任何其他有趣且信息丰富的推论或结论。
团队从数据中得出结论。

• 为香港（特别行政区）帆船经纪人准备一份一到两页的报告。包括一个
一些精心挑选的图表可以帮助经纪人理解您的结论。

## 英文原文
www.comap.com | www.mathmodels.org | info@comap.com |
2023 MCM
Problem Y: Understanding Used Sailboat Prices


Photo Credit: www.pixabay.com

Like many luxury goods, sailboats vary in value as they age and as market conditions change.
The attached “2023_MCM_Problem_Y_Boats.xlsx” file includes data on approximately 3500
sailboats from 36 to 56 feet long advertised for sale in Europe, the Caribbean, and the USA in
December 2020. A boating enthusiast provided these data to COMAP. Like most real-world data
sets, it may have missing data or other issues that require some data cleaning prior to analysis.

The Excel file includes two tabs, one for monohulled sailboats and one for catamarans. In each
tab, columns are labeled Make, Variant, Length (in feet), Geographic Region,
Country/Region/State, Listing Price (in US dollars), and Year (of manufacture).

For a given make, variant, and year, there are many other sources beyond the provided Excel file
that may provide detailed descriptions of the features of a particular sailboat. You may
supplement the data set provided with any additional data you choose; however, you must
include the data in “2023_MCM_Problem_Y_Boats.xlsx” in your modeling. Be sure to fully
identify and document the source of any supplemental data used.

Sailboats are frequently sold through brokers. In a desire to better understand the sailboat
market, one sailboat broker in Hong Kong (SAR), China has commissioned your team to prepare
a report on the pricing of used sailboats. The broker would like you to:

• Develop a mathematical model that explains the listing price of each of the sailboats in
the provided spreadsheet. Include any predictors you consider useful. You may draw on
other sources to understand additional features of a given sailboat (such as beam, draft,
displacement, rigging, sail area, hull materials, engine hours, sleeping capacity,
headroom, electronics, etc.) and for economic data by year and region. Identify and
describe all sources of data used. Include a discussion of the precision of your estimate
for each sailboat variant’s price.

• Use your model to explain the effect, if any, of region on listing prices. Discuss whether
any regional effect is consistent across all sailboat variants. Address the practical and
statistical significance of any regional effects noted.

www.comap.com | www.mathmodels.org | info@comap.com |
• Discuss how your modeling of the given geographic regions can be useful in the Hong
Kong (SAR) market. Choose an informative subset of sailboats, split between monohulls
and catamarans, from the provided spreadsheet. Find comparable listing price data for
that subset from the Hong Kong (SAR) market. Model what the regional effect of Hong
Kong (SAR) would be, if there is one, on each of the sailboat prices for the sailboats in
your subset. Is the effect the same for both catamarans and monohull sailboats?

• Identify and discuss any other interesting and informative inferences or conclusions your
team draws from the data.

• Prepare a one- to two-page report for the Hong Kong (SAR) sailboat broker. Include a
few well-chosen graphics to help the broker understand your conclusions.
