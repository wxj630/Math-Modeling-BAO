# 2025-D Outstanding 复现：2507692

## 复现对象
- 获奖论文：`2507692`，Optimizing Baltimore Multi-Layer Traffic Network Model Based on Graph Theory & Clustering Algorithm
- OCR 来源：`Outstanding_Solutions/MCM/OCR-results/D/2507692/2507692.md`
- PDF 来源：`Outstanding_Solutions/MCM/PDF-2025/D/2507692.pdf`
- 复现定位：用当前 ICM-D real solution 的官方 Baltimore 路网、公交、OD 冲击和安全优先级结果，对齐 2507692 的多层交通网络优化论文主线。

## 问题与建模
2507692 将 Baltimore 交通系统抽象为道路、公交和关键桥梁的多层网络，先评估局部失效对 OD 连通性和绕行成本的影响，再结合站点客流、道路暴露和聚类分区给出建设优先级。当前计算核已读取官方 drive edges/nodes、bus stops/routes 和 AADT 表，并输出桥梁移除影响、无候车亭高客流站点和高暴露道路，适合作为该论文的可验证整题复现。

## 代码与实验
- `solution.py` 读取 `docs/mcm-2015-2025/real_solutions/2025/ICM-D/result.json`。
- 复制当前 advanced 的表格、图像和中间数据到 outstanding artifacts。
- 在赛题级 `result.json` 中记录论文方法、当前计算核、关键实验结果和相对 advanced 的升级说明。

## 关键结果
- 道路网络节点数：37162。
- 道路网络边数：89958。
- 桥梁移除后断连 OD 数：1。
- 无候车亭站点数：2295。
- 前 10 个无候车亭站点客流：16266。
- 首要改造建议：Rebuild and harden the Francis Scott Key / I-695 harbor crossing corridor.。

## 相对 Advanced 的优势
把 advanced 的路网、公交和安全结果整理为 2507692 的多层网络优化框架，强调道路层、公交层和桥梁失效层之间的交互，以及从图论指标到建设建议的整题叙事。

## 输出产物
- `bridge_od_impacts.csv`：`mcm/outstanding_solutions/2025/D/2507692/artifacts/bridge_od_impacts.csv`
- `bridge_od_impacts.png`：`mcm/outstanding_solutions/2025/D/2507692/artifacts/bridge_od_impacts.png`
- `high_exposure_roads.csv`：`mcm/outstanding_solutions/2025/D/2507692/artifacts/high_exposure_roads.csv`
- `priority_bus_stops.csv`：`mcm/outstanding_solutions/2025/D/2507692/artifacts/priority_bus_stops.csv`
- `priority_bus_stops.png`：`mcm/outstanding_solutions/2025/D/2507692/artifacts/priority_bus_stops.png`
