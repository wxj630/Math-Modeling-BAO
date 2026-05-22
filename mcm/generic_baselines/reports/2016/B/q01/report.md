# 2016-B q01 MCM 通用基线报告

> 这是题目专用化之前的最低可运行通用基线，用于保留第一版建模脚手架；它不代表最终竞赛级解法。

## 题目与任务

- 题目：2016-B
- 小问：q01 时间相关商业机会模型
- 原问：Develop a time-dependent model to determine the best alternative or combination of alternatives that a private firm could adopt as a commercial opportunity to address the space debris problem.

## 通用模型选择

- 模型：线性加权评分基线
- 方法键：`linear_weighted_score_baseline`
- 章节提示：CH7
- 命中关键词：指标

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

- 通用代码：mcm/generic_baselines/solutions/2016/B/q01/solution.py
- 结果 JSON：mcm/generic_baselines/results/2016/B/q01/result.json
- 实验报告：mcm/generic_baselines/reports/2016/B/q01/report.md
- 实验产物：mcm/generic_baselines/artifacts/2016/B/q01/experiment_table.csv

## 数据来源

- 类型：mcm_question_index
- 真实工作流：question_solutions/2016/B/q01/solution.py
- 真实产物：question_artifacts/2016/B/q01/alternative_scores.csv

## 核心结果

```json
{
  "method": "linear_weighted_score_baseline",
  "baseline_score": 0.567886,
  "component_rows": [
    {
      "component": "statement_specificity",
      "raw_value": 192,
      "normalized_score": 0.457143,
      "audit_note": "Longer problem statements usually expose more constraints for a first-pass model."
    },
    {
      "component": "numeric_anchor_count",
      "raw_value": 4,
      "normalized_score": 0.5,
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
      "raw_value": "official_statement_parameters",
      "normalized_score": 0.72,
      "audit_note": "Rewards official attachments and explicit official statement parameters."
    },
    {
      "component": "artifact_readiness",
      "raw_value": "question_artifacts/2016/B/q01/alternative_scores.csv",
      "normalized_score": 1.0,
      "audit_note": "Rewards table-like artifacts that a baseline can inspect directly."
    }
  ],
  "extracted_numeric_tokens": [
    500.0,
    0.0,
    2009.0,
    10.0
  ],
  "numeric_token_count": 4,
  "outline": [
    "Read the official question and any indexed real-data workflow before adding domain assumptions.",
    "Use this baseline only as the first scaffold for variables, constraints, and sanity checks.",
    "Replace the generic score with a problem-specific model and cite official assets in the final solution."
  ],
  "method_confidence": 0.6384
}
```

## 限制

- This is the intentionally minimal baseline layer, not the contest-grade real solution.
- It does not introduce new empirical observations beyond the indexed official workflow metadata.
- It is useful for a quick modeling starting point and for regression-checking archive coverage.
