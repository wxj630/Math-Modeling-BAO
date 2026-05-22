# 2021-D q03：流派关系与随时间演化

## 题目原问
Compare similarities and influences between and within genres. What distinguishes a genre and how do genres change over time? Are some genres related to others?

## 适合模型
将 full_music_data.csv 的 artist_id 合并到 influence_data 的流派标签，按 year 和 genre 聚合音频特征，用线性趋势斜率描述流派演化，并用流派中心相似矩阵识别相关流派。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
- 行数/记录数：{'influence_data.csv': 42770, 'full_music_data.csv': 98340, 'data_by_artist.csv': 5854, 'data_by_year.csv': 100}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 音乐特征相似性
- 方法：Standardize official data_by_artist audio features; compare artists to same-genre centroids and compare genre centroids with the same distance-to-similarity transform. The matrix artifact also records cosine similarity between genre centroids.
- 有流派标签艺术家数：5599。
- 同流派平均相似度：0.276927。
- 跨流派平均相似度：0.334467。

#### 最相近流派对

| genre_a | genre_b | centroid_cosine_similarity |
|---|---|---|
| Folk | Vocal | 0.946537 |
| R&B; | Reggae | 0.835508 |
| International | Jazz | 0.822085 |
| Blues | Folk | 0.813213 |
| Blues | International | 0.805344 |
| Folk | International | 0.789064 |
| Blues | Vocal | 0.739653 |
| Latin | R&B; | 0.736557 |

### 流派随时间演化
- 方法：Merge official full_music_data first artist id to official influence genres, then estimate per-year feature slopes by genre.
- 可连接流派的歌曲行数：96065。

#### 流派特征趋势

| main_genre | year_min | year_max | energy_change_1921_2020 | acousticness_change_1921_2020 | instrumentalness_change_1921_2020 |
|---|---|---|---|---|---|
| Country | 1930 | 2020 | 0.459151 | -0.744615 | -0.07451 |
| Pop/Rock | 1925 | 2020 | 0.378059 | -0.794304 | -0.06033 |
| Latin | 1939 | 2020 | 0.359306 | -0.695911 | -0.286096 |
| R&B; | 1927 | 2020 | 0.340159 | -0.801692 | -0.070966 |
| Reggae | 1931 | 2020 | 0.317811 | -0.72639 | -0.469844 |
| International | 1930 | 2017 | 0.30651 | -0.837599 | -0.153673 |
| Vocal | 1924 | 2019 | 0.19685 | -0.319646 | -0.060058 |
| Folk | 1943 | 2014 | 0.173324 | -0.196328 | -0.018158 |
| Jazz | 1924 | 2019 | 0.160764 | -0.535228 | -0.190511 |
| Classical | 1921 | 2018 | -0.082891 | -0.052465 | 0.36474 |

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/D/q03/solution.py`

## 输出
- `mcm/question_results/2021/D/q03/result.json`
- `mcm/question_reports/2021/D/q03/report.md`
- `mcm/question_artifacts/2021/D/q03`
