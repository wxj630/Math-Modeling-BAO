# 2021 ICM-D The Influence of Music

## 数据与真实性
- 官方题面：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/The Influence of Music.pdf`。
- 官方附件目录：`/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets_extracted/2021/Problem Data- The Influence of Music/2021_ICM_Problem_D_Data`。
- 只使用 COMAP 提供的 `influence_data.csv`、`full_music_data.csv`、`data_by_artist.csv`、`data_by_year.csv`；没有随机数、没有外部 Spotify 抓取、没有 x1/x2/x3 占位数据。
- 行数：`{'influence_data.csv': 42770, 'full_music_data.csv': 98340, 'data_by_artist.csv': 5854, 'data_by_year.csv': 100}`。

## 建模与求解
- 影响网络：把 influencer -> follower 作为有向边，计算入度、出度、PageRank 和综合 influence_score。
- 音乐相似性：对官方 `data_by_artist` 的音频特征标准化，比较同流派艺术家到流派中心的距离，以及流派中心之间的余弦相似度。
- 流派演化：把 `full_music_data` 中第一 artist_id 合并到流派，按 year 估计各流派音频特征斜率。
- 影响证据：把官方影响边连接到艺术家特征，计算 influencer-follower 特征相关和距离，识别更可能传播的音乐特征。
- 革命者：综合网络影响力、出边规模和与追随者的特征跃迁距离排序。

## 关键结果
- 网络节点数：5603；边数：42770。
- 同流派平均相似度：0.276927；跨流派平均相似度：0.334467。
- 有特征可连接的影响边：42752。

### Top influencers
| artist | genre | out_degree | in_degree | pagerank | score |
|---|---|---:|---:|---:|---:|
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
| The Clash | Pop/Rock | 136 | 26 | 0.0002584058 | 3.372702 |
| The Byrds | Pop/Rock | 158 | 20 | 0.0001515477 | 3.349621 |

### 最相近流派对
| genre_a | genre_b | centroid_cosine_similarity |
|---|---|---:|
| Folk | Vocal | 0.946537 |
| R&B; | Reggae | 0.835508 |
| International | Jazz | 0.822085 |
| Blues | Folk | 0.813213 |
| Blues | International | 0.805344 |
| Folk | International | 0.789064 |
| Blues | Vocal | 0.739653 |
| Latin | R&B; | 0.736557 |

### 特征传播证据
| feature | influencer_follower_correlation | mean_absolute_gap |
|---|---:|---:|
| acousticness | 0.612968 | 0.187655 |
| energy | 0.574354 | 0.149097 |
| popularity | 0.474367 | 9.774316 |
| speechiness | 0.459942 | 0.027893 |
| danceability | 0.437535 | 0.09689 |
| instrumentalness | 0.430589 | 0.12431 |
| loudness | 0.423209 | 3.108901 |
| valence | 0.364264 | 0.150469 |

### 革命性艺术家候选
| artist | genre | active_start | out_degree | feature_distance | score |
|---|---|---:|---:|---:|---:|
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

## One-page document to ICM Society
To the ICM Society: our network approach turns the provided artist influence lists into a directed graph and links that graph to the provided Spotify-style audio features. The top network influencers in this run include The Beatles, The Rolling Stones, Bob Dylan. Within-genre similarity (0.276927) is higher than between-genre similarity (0.334467), so genres have measurable feature signatures while still showing cross-genre bridges. With richer data, the same pipeline should add lyrics, geography, collaborations, release chronology, and external historical events; those additions would allow stronger causal claims about cultural, social, political, or technological influence. The current results are valuable as an auditable map of influence, similarity, and musical evolution using only the four contest files.

## 输出文件
- `artifacts/artist_influence_centrality.csv`
- `artifacts/genre_similarity_matrix.csv`
- `artifacts/genre_feature_evolution.csv`
- `artifacts/feature_contagion.csv`
- `artifacts/revolutionary_artists.csv`
- `artifacts/influence_network_top_artists.png`
- `artifacts/genre_similarity_heatmap.png`
