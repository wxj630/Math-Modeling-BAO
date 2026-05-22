# 2021-D q04：影响者是否真的影响追随者

## 题目原问
Indicate whether the similarity data, as reported in the influence_data data set, suggest that the identified influencers in fact influence the respective artists. Do the influencers actually affect the music created by the followers? Are some music characteristics more contagious than others?

## 适合模型
把官方 influence edges 与 data_by_artist 特征向量连接，计算同/跨流派影响边相似度、influencer-follower 特征相关和平均绝对差，识别更具传播性的音乐特征。

## 数据与真实性
- 数据类型：official_comap_csv。
- 官方数据目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
- 行数/记录数：{'influence_data.csv': 42770, 'full_music_data.csv': 98340, 'data_by_artist.csv': 5854, 'data_by_year.csv': 100}。
- 本脚本只调用 COMAP 官方附件数据运行结果，不使用随机生成的 `x1/x2/x3` 占位数据。

## 建模与求解报告

### 影响者是否真的影响追随者
- 可连接特征的影响边：42752。
- 同流派影响边相似度：0.292389。
- 跨流派影响边相似度：0.261837。

#### 特征传播性

| feature | influencer_follower_correlation | mean_absolute_gap |
|---|---|---|
| acousticness | 0.612968 | 0.187655 |
| energy | 0.574354 | 0.149097 |
| popularity | 0.474367 | 9.774316 |
| speechiness | 0.459942 | 0.027893 |
| danceability | 0.437535 | 0.09689 |
| instrumentalness | 0.430589 | 0.12431 |
| loudness | 0.423209 | 3.108901 |
| valence | 0.364264 | 0.150469 |
| duration_ms | 0.274204 | 58797.094514 |
| tempo | 0.160258 | 14.137096 |

## 模型限制
- 这是可复现的官方 The Influence of Music CSV 附件实验；只使用 influence_data.csv、full_music_data.csv、data_by_artist.csv 和 data_by_year.csv 四个 COMAP 文件。
- 影响网络来自题面给定的艺术家/专家影响关系，音频特征来自官方子集；相似性和相关性不能单独证明严格因果，正式论文应补充歌词、地理、合作、发行时间线和历史事件数据。

## 运行方式
`/Users/wuxiaojun/code/Math-Modeling-World/.venv/bin/python /Users/wuxiaojun/code/Math-Modeling-World/mcm/question_solutions/2021/D/q04/solution.py`

## 输出
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_results/2021/D/q04/result.json`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_reports/2021/D/q04/report.md`
- `/Users/wuxiaojun/code/Math-Modeling-World/mcm/question_artifacts/2021/D/q04`
