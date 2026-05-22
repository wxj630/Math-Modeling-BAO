# 2020 MCM-B The Longest Lasting Sandcastle(s)

## Data Source
- Official PDF asset: `docs/mcm-2015-2025/official_assets/2020/The Longest Lasting Sandcastle(s)`.
- No COMAP numeric attachment is supplied; this workflow uses official statement constraints and explicit deterministic modeling inputs.

## Recommendation
- Shape: low circular mound with expected lifetime 22.854 hours.
- Water fraction: 0.12 with expected lifetime 22.854 hours.

## Article
Fun in the Sun article: The most durable castle starts with a low, rounded foundation, not a tall tower. Our model gives each shape the same sand, beach distance, and water mix, then estimates how much surface and corner exposure waves can attack during a tide. A compact truncated cone or low circular mound lasts longer because waves climb over it gradually instead of cutting steep walls. The best water fraction is moist enough for capillary bridges but not so wet that the mound slumps. Rain lowers every lifetime, but broad low foundations remain safest because they shed runoff and avoid sharp corners.

## Output Files
- `sandcastle_shape_scores.csv`: shape erosion scores.
- `sand_water_mixture_scores.csv`: water fraction scan.
- `rain_sensitivity.csv`: rain case outcomes.
- `longevity_strategies.csv`: practical strategies.
- `sandcastle_longevity_frontier.png`: shape and mixture frontier.
