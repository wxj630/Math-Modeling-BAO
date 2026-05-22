# 2019 ICM-D Time to leave the Louvre

## Data Source
- Official PDF asset: `/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets/2019/Time to leave the Louvre`.
- No numeric COMAP attachment is supplied; this workflow uses official statement facts and explicit deterministic evacuation inputs.

## Model Summary
- Estimated peak occupancy: 8361.
- Main exit capacity: 1040 persons/min.
- Threat scenarios: 4.

## Technology Plan
Use Affluences wait-time logic as an evacuation routing layer: multilingual push messages, exit status, responder corridor reservations, and floor-specific crowd metering.

## Output Files
- `louvre_evacuation_baseline.csv`
- `louvre_bottlenecks.csv`
- `louvre_threat_scenarios.csv`
- `louvre_evacuation_frontier.png`
