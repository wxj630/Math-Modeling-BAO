# 2023 ICM-D Prioritizing the UN Sustainability Goals

## Official Statement Basis
- Source: `Prioritizing the UN Sustainability Goals.pdf`.
- Official statement lists 17 Sustainable Development Goals and asks for a relationship network, priorities, 10-year achievability, achieved-goal network changes, crisis impacts, and transfer to other organizations.
- No COMAP numeric attachment is provided; edge weights and crisis multipliers are deterministic scenario assumptions.

## Model
- Directed weighted network over the 17 official SDGs.
- Priority score combines PageRank, betweenness, outgoing influence, incoming support, and direct need.
- Tutorial model references: complex networks/graph theory, comprehensive evaluation, and scenario sensitivity from `/Users/wuxiaojun/code/My-Agent/intro-mathmodel`.

## Top Priorities
- SDG 1 No Poverty: priority score 0.5962.
- SDG 17 Partnerships to achieve the Goal: priority score 0.5429.
- SDG 10 Reduced Inequality: priority score 0.5346.
- SDG 15 Life on Land: priority score 0.525.
- SDG 13 Climate Action: priority score 0.5219.

## Crisis Interpretation
Crises matter most when they hit bridge goals such as health, education, institutions, partnerships, climate, and inequality at the same time.

## Organization Transfer
- list organizational goals as nodes and define positive or negative dependencies as weighted edges
- score each goal using centrality, direct mission need, feasibility, and risk exposure
- fund a small first-wave portfolio of bridge goals instead of isolated high-visibility goals
- rerun the network after a goal is achieved or after a crisis changes edge weights
- publish tradeoff edges so stakeholders can see where progress on one objective may slow another
