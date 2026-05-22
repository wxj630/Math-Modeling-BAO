# 2015-C q01 MCM 通用基线报告

> 这是题目专用化之前的最低可运行通用基线，用于保留第一版建模脚手架；它不代表最终竞赛级解法。

## 题目与任务

- 题目：2015-C
- 小问：q01 ICM 组织人力资本网络模型
- 原问：Build a human capital network model of the personnel situation at ICM using the provided data. You may have to make bold assumptions to build the model; be sure to describe the model and your assumptions.

## 通用模型选择

- 模型：网络路径基线
- 方法键：`network_path_baseline`
- 章节提示：CH4
- 命中关键词：network, 网络

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/solutions/2015/C/q01/solution.py
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/results/2015/C/q01/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/reports/2015/C/q01/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/artifacts/2015/C/q01/experiment_table.csv

## 数据来源

- 类型：mcm_question_index
- 真实工作流：question_solutions/2015/C/q01/solution.py
- 真实产物：question_artifacts/2015/C/q01/workforce_level_table.csv

## 核心结果

```json
{
  "method": "network_path_baseline",
  "baseline_score": 0.697029,
  "component_rows": [
    {
      "component": "statement_specificity",
      "raw_value": 204,
      "normalized_score": 0.485714,
      "audit_note": "Longer problem statements usually expose more constraints for a first-pass model."
    },
    {
      "component": "numeric_anchor_count",
      "raw_value": 8,
      "normalized_score": 1.0,
      "audit_note": "Counts numeric anchors visible in the question statement and method hint."
    },
    {
      "component": "model_keyword_match",
      "raw_value": 2,
      "normalized_score": 0.4,
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
      "raw_value": "question_artifacts/2015/C/q01/workforce_level_table.csv",
      "normalized_score": 1.0,
      "audit_note": "Rewards table-like artifacts that a baseline can inspect directly."
    }
  ],
  "extracted_numeric_tokens": [
    370.0,
    46.0,
    7.0,
    12.0,
    4.0,
    85.0,
    8.0,
    -10.0
  ],
  "numeric_token_count": 8,
  "outline": [
    "Read the official question and any indexed real-data workflow before adding domain assumptions.",
    "Use this baseline only as the first scaffold for variables, constraints, and sanity checks.",
    "Replace the generic score with a problem-specific model and cite official assets in the final solution."
  ],
  "method_confidence": 0.7684
}
```

## 限制

- This is the intentionally minimal baseline layer, not the contest-grade real solution.
- It does not introduce new empirical observations beyond the indexed official workflow metadata.
- It is useful for a quick modeling starting point and for regression-checking archive coverage.
