# 2021-D q07：文化影响解释与 ICM Society 一页文档

## 题目原问
How does your work express information about cultural influence of music in time or circumstances? Write a one-page document to the ICM Society about the value of using your approach, how results would change with richer data, and recommendations for further study.

## 适合模型
用 follower active-start decade 分布描述时间环境下的影响网络，并把网络、相似性、演化和数据局限整理成面向 ICM Society 的一页说明。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
- 行数/记录数：{'influence_data.csv': 42770, 'full_music_data.csv': 98340, 'data_by_artist.csv': 5854, 'data_by_year.csv': 100}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 音乐影响网络
- 节点数：5603。
- 边数：42770。
- 弱连通分量：3。
- 最大弱连通分量节点：5599。

#### Top influencers

| artist_name | main_genre | out_degree | in_degree | pagerank | influence_score |
|---|---|---|---|---|---|
| The Beatles | Pop/Rock | 615 | 31 | 0.0002282929 | 4.108035 |
| The Rolling Stones | Pop/Rock | 319 | 39 | 0.0002368474 | 3.891589 |
| Bob Dylan | Pop/Rock | 389 | 29 | 0.0002517577 | 3.88022 |
| Jimi Hendrix | Pop/Rock | 201 | 32 | 0.0002409752 | 3.617318 |
| David Bowie | Pop/Rock | 238 | 25 | 0.0002294209 | 3.609331 |
| Led Zeppelin | Pop/Rock | 221 | 24 | 0.0001898493 | 3.561608 |
| Neil Young | Pop/Rock | 148 | 31 | 0.0003573324 | 3.47193 |
| Ramones | Pop/Rock | 127 | 33 | 0.0005681892 | 3.429004 |
| Nirvana | Pop/Rock | 110 | 39 | 0.0003416334 | 3.417229 |
| Sex Pistols | Pop/Rock | 153 | 23 | 0.0001821943 | 3.382591 |

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

### 时间与文化影响解释
- 1990 年前影响边：25576。
- 1990-2000 影响边：16383。
- 2000 年后影响边：811。
- 解释：Follower active-start decades show how the observed influence network concentrates across eras; this is a network signal, not a causal proof of internet or political effects.

### ICM Society 一页文档
To the ICM Society: our network approach turns the provided artist influence lists into a directed graph and links that graph to the provided Spotify-style audio features. The top network influencers in this run include The Beatles, The Rolling Stones, Bob Dylan. Within-genre similarity (0.276927) is higher than between-genre similarity (0.334467), so genres have measurable feature signatures while still showing cross-genre bridges. With richer data, the same pipeline should add lyrics, geography, collaborations, release chronology, and external historical events; those additions would allow stronger causal claims about cultural, social, political, or technological influence. The current results are valuable as an auditable map of influence, similarity, and musical evolution using only the four contest files.

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/D/q07/solution.py`

## 输出
- `mcm/question_results/2021/D/q07/result.json`
- `mcm/question_reports/2021/D/q07/report.md`
- `mcm/question_artifacts/2021/D/q07`
