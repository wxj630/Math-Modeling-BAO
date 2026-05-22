# 2021 MCM-A Fungi

## 数据真实性
- 官方来源：`docs/mcm-2015-2025/official_assets/2021/Fungi`。
- 本题无 COMAP 数值附件；脚本只使用官方题面中的 growth rate、moisture tolerance、环境类型和显式确定性 trait 情景。

## 分解模型
- 方法：trait-based multi-species litter decomposition model using growth rate, moisture tolerance, competition rank, and moisture niche width。
- 机制：fast opportunists dominate early when moisture matches their narrow niche; slower tolerant strains persist through long-run fluctuations.

## 环境波动
- 解释：Increasing variability shifts advantage from fast narrow-niche fungi to slower broad-tolerance fungi and can reduce total decomposition in arid and semi-arid settings.

## 生物多样性
- 作用：Diversity improves system efficiency by keeping at least one active decomposer close to its moisture niche during rapid environmental changes.

## 教材文章摘录
Introductory college level biology textbook article: Fungi are not interchangeable decomposers. A fast-growing fungus can remove woody litter quickly when moisture is favorable, but it may lose dominance when moisture and temperature fluctuate. Slow-growing, moisture-tolerant fungi act like ecological insurance: they keep decomposition active through dry or rapidly changing periods. The model shows why biodiversity matters for the carbon cycle. A mixed fungal community contains species with different growth rates and moisture niches, so the community can continue breaking down wood across arid, temperate, arboreal, and tropical settings. Recent trait-based thinking therefore changes the textbook picture from a single decay rate to a dynamic competition among decomposers.

## 输出产物
- `fungal_trait_table.csv`：五类真菌 trait 与分解率。
- `decomposition_environment_results.csv`：五种环境下的分解与优势种。
- `environmental_variability_sensitivity.csv`：快速环境波动敏感性。
- `biodiversity_sensitivity.csv`：多样性与分解效率。
- `fungi_decomposition_frontier.png`：多样性-分解效率图。
