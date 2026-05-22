# 2019-C q02 MCM 通用基线报告

> 这是题目专用化之前的最低可运行通用基线，用于保留第一版建模脚手架；它不代表最终竞赛级解法。

## 题目与任务

- 题目：2019-C
- 小问：q02 ACS 社会经济因素关联与模型修正
- 原问：Using the U.S. Census socio-economic data provided, determine whether use or trends-in-use are associated with any of the provided Census data, and modify the model from Part 1 to include important factors.

## 通用模型选择

- 模型：线性趋势预测基线
- 方法键：`linear_trend_forecast_baseline`
- 章节提示：CH8
- 命中关键词：trend

## 变量、约束与公式

### 变量定义
- x_i: normalized evidence component score for baseline component i
- w_i: fixed transparent weight assigned to component i
- S: first-pass baseline readiness score

### 约束条件
- 0 <= x_i <= 1 for every component
- sum_i w_i = 1
- The baseline must not replace the real-data workflow or invent hidden observations.

### 模型公式 / 目标函数
- `S = sum_i w_i x_i`
- `method = argmax keyword_overlap(question, model_family)`

## 运行与产物

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/solutions/2019/C/q02/solution.py
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/results/2019/C/q02/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/reports/2019/C/q02/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/artifacts/2019/C/q02/experiment_table.csv

## 数据来源

- 类型：mcm_question_index
- 真实工作流：question_solutions/2019/C/q02/solution.py
- 真实产物：question_artifacts/2019/C/q02/socioeconomic_correlations.csv

## 核心结果

```json
{
  "method": "linear_trend_forecast_baseline",
  "baseline_score": 0.672286,
  "component_rows": [
    {
      "component": "statement_specificity",
      "raw_value": 206,
      "normalized_score": 0.490476,
      "audit_note": "Longer problem statements usually expose more constraints for a first-pass model."
    },
    {
      "component": "numeric_anchor_count",
      "raw_value": 5,
      "normalized_score": 0.625,
      "audit_note": "Counts numeric anchors visible in the question statement and method hint."
    },
    {
      "component": "model_keyword_match",
      "raw_value": 1,
      "normalized_score": 0.2,
      "audit_note": "Measures how clearly the question maps to a classical modeling family."
    },
    {
      "component": "source_strength",
      "raw_value": "official_comap_xlsx_csv",
      "normalized_score": 1.0,
      "audit_note": "Rewards official attachments and explicit official statement parameters."
    },
    {
      "component": "artifact_readiness",
      "raw_value": "question_artifacts/2019/C/q02/socioeconomic_correlations.csv",
      "normalized_score": 1.0,
      "audit_note": "Rewards table-like artifacts that a baseline can inspect directly."
    }
  ],
  "extracted_numeric_tokens": [
    1.0,
    2010.0,
    -2016.0,
    2.0,
    1000.0
  ],
  "numeric_token_count": 5,
  "outline": [
    "Read the official question and any indexed real-data workflow before adding domain assumptions.",
    "Use this baseline only as the first scaffold for variables, constraints, and sanity checks.",
    "Replace the generic score with a problem-specific model and cite official assets in the final solution."
  ],
  "method_confidence": 0.7
}
```

## 限制

- This is the intentionally minimal baseline layer, not the contest-grade real solution.
- It does not introduce new empirical observations beyond the indexed official workflow metadata.
- It is useful for a quick modeling starting point and for regression-checking archive coverage.
