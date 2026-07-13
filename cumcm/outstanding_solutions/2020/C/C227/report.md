# CUMCM 2020-C Outstanding Reproduction: C227

This reproduction reads the official three Excel attachments and rebuilds the ensemble credit-risk workflow.
- Unknown high-risk firms: 34, paper target 34.
- Eligible unknown firms: 268, paper target 268.
- Rating counts among eligible firms: {'A': 63, 'B': 103, 'C': 102}, paper target A/B/C = 63/103/102.
- XGBoost is not in the project requirements, so GradientBoostingClassifier is used as the tree-boosting proxy.
