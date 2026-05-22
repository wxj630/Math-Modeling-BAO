# 2021-D q05：音乐革命性跃迁与革命者艺术家

## 题目原问
Identify if there are characteristics that might signify revolutions or major leaps in musical evolution from these data. What artists represent revolutionaries in your network?

## 适合模型
综合网络影响力、出边规模和影响者到追随者的平均标准化特征距离，构建 revolutionary_score，筛选高影响且带来大特征跃迁的艺术家。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
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

### 革命性艺术家候选
- 方法：Rank artists by directed-network influence plus average feature distance to followers, identifying high-impact artists associated with major stylistic jumps.

| artist_name | main_genre | active_start | out_degree | mean_follower_feature_distance | revolutionary_score |
|---|---|---|---|---|---|
| Brian Eno | Pop/Rock | 1970 | 135 | 4.917926 | 0.977773 |
| Pink Floyd | Pop/Rock | 1960 | 142 | 3.715158 | 0.953067 |
| Miles Davis | Jazz | 1940 | 160 | 3.500365 | 0.942815 |
| John Coltrane | Jazz | 1940 | 118 | 3.619001 | 0.942731 |
| Black Flag | Pop/Rock | 1970 | 93 | 3.384994 | 0.918361 |
| My Bloody Valentine | Pop/Rock | 1980 | 51 | 3.826274 | 0.910357 |
| Sonic Youth | Pop/Rock | 1980 | 71 | 3.236479 | 0.907731 |
| Charlie Parker | Jazz | 1930 | 95 | 3.450395 | 0.899958 |
| King Crimson | Pop/Rock | 1960 | 50 | 4.413811 | 0.899811 |
| Ramones | Pop/Rock | 1970 | 127 | 3.052471 | 0.898613 |

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/D/q05/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/D/q05/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/D/q05/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/D/q05`
