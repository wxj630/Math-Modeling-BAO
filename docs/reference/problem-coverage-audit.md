# Problem Coverage Audit

这份报告对比本地归档材料、教程索引和本地题面 Markdown，用来回答“本地已有材料但没有进入教程”的缺口。

## 结论

- CUMCM 本地归档题面：63 题；教程索引：63 题；当前缺口：0 题。
- MCM/ICM 本地规范索引：66 题；教程索引：66 题；当前唯一题目缺口：0 题。
- CUMCM 2025 的根因是官方压缩包已经进入 `cumcm/source_materials/raw_downloads/archives/`，但中文文件名没有正确解压成 A-E 题面 PDF，因此旧清洗阶段只看到了 `format2025.doc`。
- MCM 2015 只显示 C/D 的根因是本地早期归档只下载了 ICM C/D PDF；MCM A/B 在 COMAP 2015 官方网页中以 HTML 题面出现，没有独立 PDF 文件。

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
| 2019-P06 | 2019-F |
| 2022-P01 | 2022-D |
| 2023-C-Boats | 2023-Y |
| 2023-C-Wordle | 2023-C |
| 2023-F-GreenGDP | 2023-F |

这些重复别名来自早期抽取或命名方式，不代表新的独立赛题；教程只保留规范题号，避免同一题出现两套入口。

## 机器可读摘要

```json
{
  "cumcm": {
    "expected": 63,
    "indexed": 63,
    "missing_from_index": [],
    "extra_indexed": []
  },
  "mcm": {
    "expected": 66,
    "indexed": 66,
    "missing_from_index": [],
    "extra_indexed": [],
    "duplicate_aliases": {
      "2015-P01": "2015-D",
      "2015-P02": "2015-C",
      "2019-P06": "2019-F",
      "2022-P01": "2022-D",
      "2023-C-Boats": "2023-Y",
      "2023-C-Wordle": "2023-C",
      "2023-F-GreenGDP": "2023-F"
    }
  }
}
```
