# 2016 MCM-C The Goodgrant Challenge：官方 Scorecard/IPEDS 实验报告

## 数据来源
- 官方题面：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/The Goodgrant Challenge.pdf`。
- 官方附件目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2016/Problem Data- The Goodgrant Challenge`。
- Scorecard 行数：7804。
- 候选 UID 行数：2977。
- 本实验不使用随机生成的 x1/x2/x3；ROI 是透明 charitable-return 指数，不声明因果。

## ROI 定义
Charitable ROI = weighted student-success potential, demonstrated need, and scalable leverage per grant dollar. It is appropriate for philanthropy because it values Pell-serving institutions, completion/retention/repayment/earnings outcomes, and students reached rather than private profit.

## 推荐资助组合
- 年预算：100000000 USD，持续 5 年。
- 推荐学校数：10。
| rank | school | state | annual grant | roi score | students reached |
|---:|---|---|---:|---:|---:|
| 1 | University of California-Irvine | CA | 10000000.0 | 82.057599 | 10159.0 |
| 2 | University of California-San Diego | CA | 10000000.0 | 82.032235 | 10169.0 |
| 3 | University of California-Davis | CA | 10000000.0 | 79.77542 | 11380.0 |
| 4 | University of California-Los Angeles | CA | 10000000.0 | 79.370855 | 10389.0 |
| 5 | University of California-Berkeley | CA | 10000000.0 | 77.579122 | 8400.0 |
| 6 | University of California-Riverside | CA | 8900000.0 | 77.54864 | 10497.0 |
| 7 | University of Florida | FL | 10000000.0 | 75.065743 | 10373.0 |
| 8 | Brigham Young University-Provo | UT | 10000000.0 | 74.869283 | 9934.0 |
| 9 | California State University-Long Beach | CA | 10000000.0 | 74.281675 | 14407.0 |
| 10 | University of California-Santa Barbara | CA | 9200000.0 | 74.215957 | 7354.0 |

## 稳健性
| scenario | top school | top20 overlap |
|---|---|---:|
| base | University of California-Irvine | 18 |
| need_priority | California State University-Los Angeles | 13 |
| outcome_priority | University of California-San Diego | 11 |
| scale_priority | University of California-Irvine | 17 |

## CFO letter
Dear Mr. Alpha Chiang: We recommend that the Goodgrant Foundation invest the annual $100 million in a ranked portfolio of candidate institutions selected from the official IPEDS UID list and College Scorecard outcomes. Our ROI is not financial profit; it is a charitable return index combining student success, service to high-need students, and scale per grant dollar. The attached plan funds multiple institutions for five years, avoids duplicating purely prestige-driven giving, and should be re-estimated annually as new Scorecard and IPEDS data arrive.
