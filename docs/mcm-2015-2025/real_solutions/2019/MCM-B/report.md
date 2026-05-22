# 2019 MCM-B Send in the Drones

## Data Source
- Official PDF asset: `/Users/wuxiaojun/code/Math-Modeling-World/docs/mcm-2015-2025/official_assets/2019/Send in the Drones- Developing an Aerial Disaster Relief Response System`.
- Uses official attachment tables embedded in the PDF: drone dimensions/capabilities, cargo-bay dimensions, MED package dimensions, and Puerto Rico demand rows.

## Recommended System
- Container rows: 3.
- Delivery route rows: 10.

## Memo
Memo to HELP, Inc.: deploy DroneGo as three containerized regional cells rather than one central cache. The recommended mix emphasizes type C and G drones for payload and video flexibility, type B for fast small-package runs, type F for heavy medical-only supply, and tethered units for local overwatch. This meets the attachment demand table with clearer tradeoffs when road closures stretch sortie times.

## Output Files
- `drone_fleet_plan.csv`
- `container_packing_plan.csv`
- `container_location_scores.csv`
- `delivery_route_schedule.csv`
- `video_recon_flight_plan.csv`
- `dronego_response_frontier.png`
