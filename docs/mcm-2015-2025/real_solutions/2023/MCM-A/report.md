# 2023 MCM-A Drought-Stricken Plant Communities

## Official Statement Basis
- Source: `Drought-Stricken Plant Communities.pdf`.
- The official prompt states that one-species communities may adapt poorly, while communities with four or more species can benefit from localized biodiversity.
- No COMAP numeric data attachment is provided; this workflow uses deterministic scenario assumptions and labels them as assumptions.

## Model
- State variable: species biomass by year.
- Core mechanism: logistic biomass growth, drought penalty moderated by species traits, biodiversity facilitation after four or more persistent species, pollution penalty, and habitat carrying capacity.
- Typical tutorial models: differential/difference equations, sensitivity analysis, comprehensive evaluation, and policy optimization from `/Users/wuxiaojun/code/My-Agent/intro-mathmodel`.

## Results
- Estimated minimum species for benefit: 4.
- Recommended minimum species: 4.
- Single-species viability score: 0.761.
- Output artifacts: biodiversity threshold table, community trajectories, drought sensitivity table, stressor table, and viability frontier plot.

## Management Interpretation
- Maintain at least four functional plant species and prefer six or more when future drought frequency increases.
- Mix drought-tolerant deep-rooted species with faster-recovering grasses and forbs instead of maximizing species count alone.
- Reduce pollution load before drought years because stressor stacking sharply lowers carrying capacity.
- Preserve habitat corridors and seed banks so post-drought recovery can occur over successive generations.

## Memo
For a drought-stricken plant community, the model recommends preserving at least four functional species and preferably six or more under future drought intensification. The practical focus should be functional diversity, habitat continuity, and pollution reduction, because these raise post-drought biomass persistence and protect the larger environment from erosion and forage collapse.
