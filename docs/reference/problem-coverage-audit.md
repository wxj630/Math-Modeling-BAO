# Problem Coverage Audit

这份报告对比本地归档材料、教程索引和本地题面 Markdown，用来回答“本地已有材料但没有进入教程”的缺口。

## 结论

- CUMCM 本地归档题面：58 题；教程索引：58 题；当前缺口：0 题。
- MCM/ICM 本地规范索引：64 题；教程索引：64 题；当前唯一题目缺口：0 题。
- CUMCM 这次的根因是 2022/2023 年 A-E 已经解压到 `cumcm/source_materials/extracted/`，但旧清洗阶段只转出了 2022-B、2022-D、2023-D 三个 markdown，因此后续 `cumcm/problems`、逐问索引和教程页都只看到了这些题。

## CUMCM 缺口

| 年份 | 题号 |
| --- | --- |
| 无 | 无 |

## MCM/ICM 缺口

| 年份 | 题号 |
| --- | --- |
| 无 | 无 |

## MCM/ICM 本地重复别名

| 本地文件题号 | 教程采用的规范题号 |
| --- | --- |
| 2015-P01 | 2015-D |
| 2015-P02 | 2015-C |
| 2023-C | 2023-C-Boats |

这些重复别名来自早期抽取或命名方式，不代表新的独立赛题；教程只保留规范题号，避免同一题出现两套入口。

## 机器可读摘要

```json
{
  "cumcm": {
    "expected": 58,
    "indexed": 58,
    "missing_from_index": [],
    "extra_indexed": []
  },
  "mcm": {
    "expected": 64,
    "indexed": 64,
    "missing_from_index": [],
    "extra_indexed": [],
    "duplicate_aliases": {
      "2015-P01": "2015-D",
      "2015-P02": "2015-C",
      "2023-C": "2023-C-Boats"
    }
  }
}
```
