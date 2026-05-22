# 2025-A q03 MCM 通用基线报告

> 这是题目专用化之前的最低可运行通用基线，用于保留第一版建模脚手架；它不代表最终竞赛级解法。

## 题目与任务

- 题目：2025-A
- 小问：q03 并排或单列使用模式
- 原问：How many people used the stairs simultaneously? For example, did pairs of people climb the stairs side-by-side or did they travel single file?

## 通用模型选择

- 模型：证据表基线
- 方法键：`evidence_table_baseline`
- 章节提示：CH6
- 命中关键词：generic

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

- 通用代码：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/solutions/2025/A/q03/solution.py
- 结果 JSON：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/results/2025/A/q03/result.json
- 实验报告：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/reports/2025/A/q03/report.md
- 实验产物：/Users/wuxiaojun/code/Math-Modeling-World/mcm/generic_baselines/artifacts/2025/A/q03/experiment_table.csv

## 数据来源

- 类型：mcm_question_index
- 真实工作流：question_solutions/2025/A/q03/solution.py
- 真实产物：question_artifacts/2025/A/q03/wear_cross_section.png

## 核心结果

```json
{
  "method": "evidence_table_baseline",
  "baseline_score": 0.415257,
  "component_rows": [
    {
      "component": "statement_specificity",
      "raw_value": 142,
      "normalized_score": 0.338095,
      "audit_note": "Longer problem statements usually expose more constraints for a first-pass model."
    },
    {
      "component": "numeric_anchor_count",
      "raw_value": 0,
      "normalized_score": 0.0,
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
      "raw_value": "question_artifacts/2025/A/q03/wear_cross_section.png",
      "normalized_score": 0.68,
      "audit_note": "Rewards table-like artifacts that a baseline can inspect directly."
    }
  ],
  "extracted_numeric_tokens": [],
  "numeric_token_count": 0,
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
