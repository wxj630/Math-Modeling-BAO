# 2020 MCM-C A Wealth of Data

## Data Source
- Official PDF asset: `docs/mcm-2015-2025/official_assets/2020/A Wealth of Data`.
- Official ZIP asset: `docs/mcm-2015-2025/official_assets/2020/Problem Data- A Wealth of Data`.
- Rows: {'hair_dryer.tsv': 11470, 'microwave.tsv': 1615, 'pacifier.tsv': 18939}.

## Recommendation
Letter to the Marketing Director of Sunshine Company: track low-star share, helpfulness-weighted review length, and disappointed/enthusiastic descriptor lift from launch week onward. The official Amazon review files show that the most useful early warning is not the mean rating alone; it is the combination of rating trend, low-rating share, and negative descriptors that other customers find helpful. Sunshine should compare microwave, pacifier, and hair dryer launches against these baselines and investigate product design features whenever low-rating share and broken/disappointed language rise together.

## Output Files
- `product_review_measures.csv`: rating, helpfulness, and review-length measures.
- `monthly_reputation_trends.csv`: monthly reputation time patterns.
- `text_descriptor_rating_lift.csv`: descriptor and rating association.
- `success_failure_signals.csv`: product success/failure signal scores.
- `product_reputation_frontier.png`: product reputation frontier.
