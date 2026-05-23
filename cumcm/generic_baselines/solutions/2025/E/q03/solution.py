# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question_generic_baseline

PAYLOAD = {
  "problem_id": "2025-E",
  "question_index": 3,
  "title": "2025年 CUMCM E题：AI 辅助智能体测",
  "problem_path": "cumcm/problems/2025/E.md",
  "question": {
    "label": "问题3",
    "statement": "基于问题1 和问题2 的模型和结果，结合附件5 中运动者11 的跳远视频和位 置信息以及个人体质信息（见附件4），预测该运动者的实际跳远成绩。",
    "tasks": [
      "基于问题1 和问题2 的模型和结果，结合附件5 中运动者11 的跳远视频和位 置信息以及个人体质信息（见附件4），预测该运动者的实际跳远成绩"
    ],
    "models": [
      {
        "key": "fitting",
        "name": "数据处理与拟合",
        "chapter": "CH6",
        "keywords": [
          "预测"
        ]
      },
      {
        "key": "time_series",
        "name": "时间序列模型",
        "chapter": "CH8",
        "keywords": [
          "预测"
        ]
      },
      {
        "key": "signal_text",
        "name": "图像文本与信号",
        "chapter": "CH10",
        "keywords": [
          "视频"
        ]
      }
    ]
  },
  "attachments": [
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/E题.pdf",
      "name": "E题.pdf",
      "suffix": ".pdf",
      "kind": "document",
      "size_bytes": 226037,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者1和运动者2的跳远成绩.txt",
      "name": "运动者1和运动者2的跳远成绩.txt",
      "suffix": ".txt",
      "kind": "media_or_archive",
      "size_bytes": 62,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者1的跳远位置信息.xlsx",
      "name": "运动者1的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 149479,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者1的跳远视频.mp4",
      "name": "运动者1的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1735906,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者2的跳远位置信息.xlsx",
      "name": "运动者2的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 150036,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件1/运动者2的跳远视频.mp4",
      "name": "运动者2的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1544422,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件2.jpg",
      "name": "附件2.jpg",
      "suffix": ".jpg",
      "kind": "media_or_archive",
      "size_bytes": 50761,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者10第1次的跳远位置信息.xlsx",
      "name": "运动者10第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 150998,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者10第1次的跳远视频.mp4",
      "name": "运动者10第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1632122,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者10第2次的跳远位置信息.xlsx",
      "name": "运动者10第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152220,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者10第2次的跳远视频.mp4",
      "name": "运动者10第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1762389,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第1次的跳远位置信息.xlsx",
      "name": "运动者3第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 151889,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第1次的跳远视频.mp4",
      "name": "运动者3第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1652453,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第2次的跳远位置信息.xlsx",
      "name": "运动者3第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 151815,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第2次的跳远视频.mp4",
      "name": "运动者3第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1666930,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第3次的跳远位置信息.xlsx",
      "name": "运动者3第3次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 153607,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第3次的跳远视频.mp4",
      "name": "运动者3第3次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1924889,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第4次的跳远位置信息.xlsx",
      "name": "运动者3第4次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 151928,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第4次的跳远视频.mp4",
      "name": "运动者3第4次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1640156,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第5次的跳远位置信息.xlsx",
      "name": "运动者3第5次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 150803,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者3第5次的跳远视频.mp4",
      "name": "运动者3第5次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1525587,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者4第1次的跳远位置信息.xlsx",
      "name": "运动者4第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 124140,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者4第1次的跳远视频.mp4",
      "name": "运动者4第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1383507,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者5第1次的跳远位置信息.xlsx",
      "name": "运动者5第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 153783,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者5第1次的跳远视频.mp4",
      "name": "运动者5第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1851497,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者5第2次的跳远位置信息.xlsx",
      "name": "运动者5第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 108872,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者5第2次的跳远视频.mp4",
      "name": "运动者5第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1165506,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者6第1次的跳远位置信息.xlsx",
      "name": "运动者6第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152195,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者6第1次的跳远视频.mp4",
      "name": "运动者6第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1643103,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者6第2次的跳远位置信息.xlsx",
      "name": "运动者6第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152285,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者6第2次的跳远视频.mp4",
      "name": "运动者6第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1709862,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者7第1次的跳远位置信息.xlsx",
      "name": "运动者7第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152543,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者7第1次的跳远视频.mp4",
      "name": "运动者7第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1812867,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者7第2次的跳远位置信息.xlsx",
      "name": "运动者7第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 145385,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者7第2次的跳远视频.mp4",
      "name": "运动者7第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1554685,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者8第1次的跳远位置信息.xlsx",
      "name": "运动者8第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152328,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者8第1次的跳远视频.mp4",
      "name": "运动者8第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1769581,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者8第2次的跳远位置信息.xlsx",
      "name": "运动者8第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 139663,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者8第2次的跳远视频.mp4",
      "name": "运动者8第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1541497,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者9第1次的跳远位置信息.xlsx",
      "name": "运动者9第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 151176,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者9第1次的跳远视频.mp4",
      "name": "运动者9第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1527056,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整前/运动者姿势调整前的跳远成绩.txt",
      "name": "运动者姿势调整前的跳远成绩.txt",
      "suffix": ".txt",
      "kind": "media_or_archive",
      "size_bytes": 434,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者10调整后第1次的跳远位置信息.xlsx",
      "name": "运动者10调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152027,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者10调整后第1次的跳远视频.mp4",
      "name": "运动者10调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1589713,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者10调整后第2次的跳远位置信息.xlsx",
      "name": "运动者10调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152554,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者10调整后第2次的跳远视频.mp4",
      "name": "运动者10调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1661656,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者3调整后第1次的跳远位置信息.xlsx",
      "name": "运动者3调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 151965,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者3调整后第1次的跳远视频.mp4",
      "name": "运动者3调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1735906,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者3调整后第2次的跳远位置信息.xlsx",
      "name": "运动者3调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 147860,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者3调整后第2次的跳远视频.mp4",
      "name": "运动者3调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1828980,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者4调整后第1次的跳远位置信息.xlsx",
      "name": "运动者4调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 153849,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者4调整后第1次的跳远视频.mp4",
      "name": "运动者4调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1921148,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者4调整后第2次的跳远位置信息.xlsx",
      "name": "运动者4调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 153076,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者4调整后第2次的跳远视频.mp4",
      "name": "运动者4调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1918943,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者5调整后第1次的跳远位置信息.xlsx",
      "name": "运动者5调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 137312,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者5调整后第1次的跳远视频.mp4",
      "name": "运动者5调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1758878,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者5调整后第2次的跳远位置信息.xlsx",
      "name": "运动者5调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 120653,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者5调整后第2次的跳远视频.mp4",
      "name": "运动者5调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1311877,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者6调整后第1次的跳远位置信息.xlsx",
      "name": "运动者6调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152214,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者6调整后第1次的跳远视频.mp4",
      "name": "运动者6调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1674195,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者6调整后第2次的跳远位置信息.xlsx",
      "name": "运动者6调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 149739,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者6调整后第2次的跳远视频.mp4",
      "name": "运动者6调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1511521,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者7调整后第1次的跳远位置信息.xlsx",
      "name": "运动者7调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152834,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者7调整后第1次的跳远视频.mp4",
      "name": "运动者7调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1779805,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者7调整后第2次的跳远位置信息.xlsx",
      "name": "运动者7调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152443,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者7调整后第2次的跳远视频.mp4",
      "name": "运动者7调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1699539,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者8调整后第1次的跳远位置信息.xlsx",
      "name": "运动者8调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152405,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者8调整后第1次的跳远视频.mp4",
      "name": "运动者8调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1767956,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者9调整后第1次的跳远位置信息.xlsx",
      "name": "运动者9调整后第1次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 149026,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者9调整后第1次的跳远视频.mp4",
      "name": "运动者9调整后第1次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1588206,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者9调整后第2次的跳远位置信息.xlsx",
      "name": "运动者9调整后第2次的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 152065,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者9调整后第2次的跳远视频.mp4",
      "name": "运动者9调整后第2次的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1694324,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件3/姿势调整后/运动者姿势调整后的跳远成绩.txt",
      "name": "运动者姿势调整后的跳远成绩.txt",
      "suffix": ".txt",
      "kind": "media_or_archive",
      "size_bytes": 477,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件4.xlsx",
      "name": "附件4.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 11313,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件5/运动者11的跳远位置信息.xlsx",
      "name": "运动者11的跳远位置信息.xlsx",
      "suffix": ".xlsx",
      "kind": "data",
      "size_bytes": 150492,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    },
    {
      "path": "../../Documents/Playground/cumcm_unzipped/2025_SvpohSGacdffe718bcaa3b6e835c03ae3461cab1/E题/附件/附件5/运动者11的跳远视频.mp4",
      "name": "运动者11的跳远视频.mp4",
      "suffix": ".mp4",
      "kind": "media_or_archive",
      "size_bytes": 1446162,
      "source_root": "../../Documents/Playground/cumcm_unzipped"
    }
  ]
}
RESULT_PATH = ROOT / "generic_baselines" / "results" / "2025" / "E" / "q03" / "result.json"
REPORT_PATH = ROOT / "generic_baselines" / "reports" / "2025" / "E" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "generic_baselines" / "artifacts" / "2025" / "E" / "q03"


def write_generic_report(result: dict, solution_path: Path) -> None:
    def repo_rel(path: Path | str) -> str:
        path = Path(path)
        try:
            return str(path.resolve().relative_to(ROOT.parent.resolve()))
        except ValueError:
            return str(path)

    f = result["formulation"]
    lines = [
        f"# {result['problem_id']} {result['question_label']} 通用基线报告",
        "",
        "> 这是题目专用化之前的第一版通用模型。它用于保留建模进步过程，不代表最终竞赛级解法。",
        "",
        "## 题目与任务",
        "",
        f"- 题目：{result['title']}",
        f"- 问题：{result['question_label']}",
        f"- 原问：{result['statement']}",
        "",
        "## 通用模型选择",
        "",
        f"- 模型：{result['selected_model']['name']}（{result['selected_model']['chapter']}：{result['selected_model']['chapter_title']}）",
        f"- 教程参考：{result['selected_model']['doc']}",
        f"- 通用方法：`{result['experiment_result'].get('method', 'generic_model')}`",
        "",
        "## 变量、约束与公式",
        "",
        "### 变量定义",
    ]
    lines.extend(f"- {item}" for item in f.get("decision_variables", []))
    lines += ["", "### 约束条件"]
    lines.extend(f"- {item}" for item in f.get("constraints", []))
    lines += ["", "### 模型公式 / 目标函数"]
    lines.extend(f"- `{item}`" for item in f.get("objective_or_equations", []))
    lines += ["", "## 运行与产物", ""]
    lines.append(f"- 通用代码：{repo_rel(solution_path)}")
    lines.append(f"- 单问运行：`.venv/bin/python {repo_rel(solution_path)}`")
    lines.append(f"- 结果 JSON：{repo_rel(RESULT_PATH)}")
    lines.append(f"- 实验报告：{repo_rel(REPORT_PATH)}")
    for artifact in result.get("artifact_paths", []):
        lines.append(f"- 实验产物：{repo_rel(ROOT / artifact)}")
    lines += ["", "## 数据来源", ""]
    ds = result.get("data_source", {})
    lines.append(f"- 类型：{ds.get('source_type', 'unknown')}")
    if ds.get("path"):
        lines.append(f"- 路径：{ds['path']}")
    lines.append(f"- 说明：{ds.get('note', '')}")
    lines += ["", "## 核心结果", "", "```json", json.dumps(result["experiment_result"], ensure_ascii=False, indent=2), "```", ""]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    result = solve_question_generic_baseline(PAYLOAD, ARTIFACT_DIR)
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_generic_report(result, Path(__file__).resolve())
    print(f"wrote {RESULT_PATH}")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote artifacts under {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
