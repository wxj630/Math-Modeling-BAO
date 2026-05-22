# 2023 ICM-F Green GDP Official PDF + World Bank Workflow

## Data Source
- Official PDF: `docs/mcm-2015-2025/official_assets_extracted/2023/Green GDP.pdf`.
- Public data: World Bank WDI latest available GDP, adjusted-savings CO2 damage, resource depletion, forest depletion, forest area, and resource-rent indicators.
- Cache: `artifacts/cache/world_bank_green_gdp_panel.csv`.

## Selected GGDP Method
- Method: adjusted_savings_green_gdp.
- Formula: GGDP = GDP * (1 - observed adjusted-savings environmental penalty percent / 100).

## Global Assessment
- World penalty: 3.1402% of GNI.
- Recommendation: support_switch.
- Net benefit score: 17.381.

## Brazil Case
- Green GDP penalty: 5.0118% of GNI.
- Green gap: $109,549,016,371.

## One-page Report
One-page report to Brazil's economic and environmental leaders

Recommendation: Brazil should support a phased switch to GGDP. Conventional GDP rewards current production even when natural capital is depleted. Using the selected adjusted-savings GGDP method, Brazil's observed environmental penalty is 5.0118% of GNI, leaving a green-GDP ratio of 0.9499. This gap is large enough to make forest protection, cleaner energy, and resource-rent reinvestment visible in the headline economic metric.

Expected changes: projects that raise GDP by drawing down forests, minerals, or climate stability would face an explicit deduction. Projects that preserve forest capital, reduce CO2 damage, and reinvest resource rents would become more attractive because they protect the income base available to future generations.

Risk and implementation: the switch will be politically difficult, so Brazil should support a phased international standard with audited WDI/SEEA-style accounts, publish both GDP and GGDP during a transition period, and use the GGDP gap to guide investment rather than as a punitive ranking alone.

## Output Files
- `result.json`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/result.json
- `ggdp_formula_components.csv`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/artifacts/ggdp_formula_components.csv
- `world_bank_green_gdp_panel.csv`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/artifacts/world_bank_green_gdp_panel.csv
- `global_impact_scenarios.csv`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/artifacts/global_impact_scenarios.csv
- `brazil_country_analysis.csv`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/artifacts/brazil_country_analysis.csv
- `green_gdp_policy_frontier.png`: docs/mcm-2015-2025/real_solutions/2023/ICM-F-GreenGDP/artifacts/green_gdp_policy_frontier.png
