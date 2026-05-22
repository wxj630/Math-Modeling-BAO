# 2021-D q02：音乐特征相似性与流派内外比较

## 题目原问
Use full_music_data and/or the two summary data sets of music characteristics, to develop measures of music similarity. Using your measure, are artists within genre more similar than artists between genres?

## 适合模型
读取官方 data_by_artist.csv，对 danceability、energy、valence、tempo、loudness 等音频特征标准化；比较同流派艺术家到流派中心的距离相似度，并输出流派中心相似矩阵。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
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

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/D/q02/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/D/q02/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/D/q02/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/D/q02`
