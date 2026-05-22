# MCM 2015-2025 真实性审计

这份审计用于区分“真实赛题/真实附件驱动的实验”和“随机生成数据的烟雾测试”。

## 当前结论

- 未发现随机生成数据工作流。
- 当前可审计解法集中在 `real_solutions/` 与 `mcm/question_solutions/`，并由官方附件或明确题面参数驱动。
- 如果新增旧年份题目，必须先接入官方 PDF/附件或显式题面参数，再生成实验结果和报告。

## 命中统计

```json
{
  "finding_count": 0,
  "solution.py": 0,
  "solution_template.py": 0,
  "report_or_note_md": 0,
  "library_py": 0
}
```

## 审计明细

- CSV：`synthetic_usage_audit.csv`

## 前 30 个命中示例

| 文件 | 标记 | 示例 |
|---|---|---|
