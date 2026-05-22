# 2021-D q01：有向音乐影响网络与影响力参数

## 题目原问
Use the influence_data data set or portions of it to create a directed network of musical influence, where influencers are connected to followers. Develop parameters that capture music influence in this network. Explore a subset of musical influence by creating a subnetwork of your directed influencer network.

## 适合模型
读取 COMAP 官方 influence_data.csv，构建 influencer -> follower 有向图，计算入度、出度、PageRank、综合 influence_score，并给出 Pop/Rock 子网络规模；对应教程模型：图论网络中心性、复杂网络分析。

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

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/D/q01/solution.py`

## 输出
- `mcm/question_results/2021/D/q01/result.json`
- `mcm/question_reports/2021/D/q01/report.md`
- `mcm/question_artifacts/2021/D/q01`
