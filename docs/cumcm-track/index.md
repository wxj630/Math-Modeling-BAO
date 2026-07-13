# CUMCM 赛题入口

CUMCM 教程现在以完整赛题为入口。中文赛题尤其常见“附件解析 -> 主模型 -> 不确定性/情景 -> 提交模板/建议”的递进结构，逐问散看会丢掉这条链。PDF 不单独作为学习入口，而是放在赛题整体索引的 `BAO PDF` 列。

## 从这里进入

| 入口 | 用途 |
|---|---|
| [CUMCM 赛题整体索引](./problem-index.md) | 按年份浏览赛题，并直接打开 Baseline / Advanced / Outstanding PDF。 |
| [CUMCM 2018-A 高温作业服装](/best_practie/bao-cumcm-2018-a-heat-clothing) | 微分方程/动态系统的完整 B/A/O 样例。 |
| [CUMCM 2020-B 穿越沙漠](/best_practie/bao-cumcm-2020-b-desert-crossing) | 运筹优化的完整 B/A/O 样例。 |
| [CUMCM 2020-C 中小微企业信贷](/best_practie/bao-cumcm-2020-c-credit) | 数据建模的完整 B/A/O 样例。 |

## 阅读方法

1. 先进入赛题页，确认题目背景、推荐模型族和小问数量。
2. 按顺序读小问递进链，标出哪些变量、附件和约束会被后续问题继承。
3. 在索引的 `BAO PDF` 列先读 Baseline PDF，再读 Advanced PDF，看经典模型入口和题意专门化。
4. 如果题目有 Excel/CSV 附件，优先核对 advanced report 中的数据字段和输出文件。
5. 有正式 O 奖复现的题，再读 Outstanding PDF 和复现报告，检查鲁棒性、敏感性、论文图表和策略解释是否足够。

## 当前覆盖

CUMCM 当前生成 63 个赛题页，覆盖 243 个小问。代码和实验结果仍保存在 `cumcm/` 原目录，教程页只负责把它们组织成完整赛题路径。
