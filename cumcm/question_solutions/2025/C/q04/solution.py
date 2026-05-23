# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2025-C",
  "title": "2025年 CUMCM C题：NIPT 的时点选择与胎儿的异常判定",
  "problem_path": "cumcm/problems/2025/C.md",
  "question_index": 4,
  "question": {
    "label": "问题4",
    "statement": "由于孕妇和女胎都不携带Y 染色体，重要的是如何判定女胎是否异常。试以女胎孕妇的21 号、18 号和13 号染色体非整倍体（AB 列）为判定结果，综合考虑X 染色体及上述染色体的Z 值、GC 含量、读段数及相关比例、BMI 等因素，给出女胎异常的判定方法。 附录1 附件中各列数据的说明 附录2 Z 值（Z-score） Z 值（Z-score）的计算公式： 𝑍= 𝑋−𝜇 𝜎 其中X 为待检测样本中目标染色体的相对计数比例，𝜇 为正常对照群体中该染色体计数比例的均值，𝜎 为正常群体中该比例的标准差。在NIPT 中，对于常见染色体非整倍体检测，通常采用Z 值分析方法进 行统计判定。已知染色体非整倍体通常定义为该染色体存在一个或三个拷贝，正常为两个拷贝，且每条 染色体所采集到的读段数量与该染色体长度成正比。 列 说明 列 说明 A 样本序号 Q 13 号染色体的Z 值 B 孕妇代码 R 18 号染色体的Z 值 C 孕妇年龄 S 21 号染色体的Z 值 D 孕妇身高 T X 染色体的Z 值 E 孕妇体重 U Y 染色体的Z 值（女胎数据此列为空白） F 末次月经时间 V Y 染色体浓度，即Y 染色体游离DNA 片 段的比例（女胎数据此列为空白） G IVF 妊娠方式 W X 染色体浓度（其数值是通过生物信息学在 一定假设下通过数据分析估计得出，可能出 现负值） H 检测时间 X 13 号染色体的GC 含量 I 检测抽血次数 Y 18 号染色体的GC 含量 J 孕妇本次检测时的孕周（周数+天数） Z 21 号染色体的GC 含量 K 孕妇BMI 指标 AA 被过滤掉的读段数占总读段数的比例 L 原始测序数据的总读段数（个） AB 检测出的13 号，18 号，21 号染色体非整 倍体，即数量异常，空白即为无异常 M 总读段数中在参考基因组上比对的比例 AC 孕妇的怀孕次数 N 总读段数中重复读段的比例 AD 孕妇的生产次数 O 总读段数中唯一比对的读段数（个） AE 胎儿是否健康（婴儿出生后的结果） P GC 含量，序列中碱基 G（鸟嘌呤）和 C （胞嘧啶）所占的比例，是测序数据质量 评估中的一个重要指标，正常 GC 含量范 围为40% ~ 60%，GC 含量过高、过低、 或分布异常可能意味着测序质量存在问题",
    "tasks": [
      "试以女胎孕妇的21 号、18 号和13 号染色体非整倍体（AB 列）为判定结果，综合考虑X 染色体及上述染色体的Z 值、GC 含量、读段数及相关比例、BMI 等因素，给出女胎异常的判定方法",
      "附录1 附件中各列数据的说明 附录2 Z 值（Z-score） Z 值（Z-score）的计算公式： 𝑍= 𝑋−𝜇 𝜎 其中X 为待检测样本中目标染色体的相对计数比例，𝜇 为正常对照群体中该染色体计数比例的均值，𝜎 为正常群体中该比例的标准差",
      "在NIPT 中，对于常见染色体非整倍体检测，通常采用Z 值分析方法进 行统计判定",
      "列 说明 列 说明 A 样本序号 Q 13 号染色体的Z 值 B 孕妇代码 R 18 号染色体的Z 值 C 孕妇年龄 S 21 号染色体的Z 值 D 孕妇身高 T X 染色体的Z 值 E 孕妇体重 U Y 染色体的Z 值（女胎数据此列为空白） F 末次月经时间 V Y 染色体浓度，即Y 染色体游离DNA 片 段的比例（女胎数据此列为空白） G IVF 妊娠方式 W X 染色体浓度（其数值是通过生物信息学在 一定假设下通过数据分析估计得出，可能出 现负值） H 检测时间 X 13 号染色体的GC 含量 I 检测抽血次数 Y 18 号染色体的GC 含量 J 孕妇本次检测时的孕周（周数+天数） Z 21 号染色体的GC 含量 K 孕妇BMI 指标 AA 被过滤掉的读段数占总读段数的比例 L 原始测序数据的总读段数（个） AB 检测出的13 号，18 号，21 号染色体非整 倍体，即数量异常，空白即为无异常 M 总读段数中在参考基因组上比对的比例 AC 孕妇的怀孕次数 N 总读段数中重复读段的比例 AD 孕妇的生产次数 O 总读段数中唯一比对的读段数（个） AE 胎儿是否健康（婴儿出生后的结果） P GC 含量，序列中碱基 G（鸟嘌呤）和 C （胞嘧啶）所占的比例，是测序数据质量 评估中的一个重要指标，正常 GC 含量范 围为40% ~ 60%，GC 含量过高、过低、 或分布异常可能意味着测序质量存在问题"
    ],
    "models": [
      {
        "key": "evaluation",
        "name": "评价与决策模型",
        "chapter": "CH7",
        "keywords": [
          "综合",
          "指标",
          "评估"
        ]
      },
      {
        "key": "ml_statistics",
        "name": "机器学习与统计",
        "chapter": "CH9",
        "keywords": [
          "检测",
          "统计"
        ]
      },
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "数据"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/C题.pdf",
      "name": "C题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 357653,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/C题/附件.xlsx",
      "name": "附件.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 481734,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "question_results" / "2025" / "C" / "q04" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "C" / "q04" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "C" / "q04"


def main() -> None:
    result = solve_question(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_question_report(result, REPORT_PATH)
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
