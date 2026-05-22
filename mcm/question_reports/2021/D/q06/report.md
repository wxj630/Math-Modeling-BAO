# 2021-D q06：单一流派的动态影响过程

## 题目原问
Analyze the influence processes of musical evolution that occurred over time in one genre. Can your team identify indicators that reveal the dynamic influencers, and explain how the genres or artists changed over time?

## 适合模型
以官方数据中记录最多的 Pop/Rock 流派作为子网络示例，结合活跃年代、网络中心性和 genre/year 特征斜率，解释动态影响者与音频特征变化。

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

### 时间与文化影响解释
- 1990 年前影响边：25576。
- 1990-2000 影响边：16383。
- 2000 年后影响边：811。
- 解释：Follower active-start decades show how the observed influence network concentrates across eras; this is a network signal, not a causal proof of internet or political effects.

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`.venv/bin/python mcm/question_solutions/2021/D/q06/solution.py`

## 输出
- `mcm/question_results/2021/D/q06/result.json`
- `mcm/question_reports/2021/D/q06/report.md`
- `mcm/question_artifacts/2021/D/q06`
