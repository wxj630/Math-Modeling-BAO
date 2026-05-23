# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "lib"))
from question_models import solve_question, write_question_report

PAYLOAD = {
  "problem_id": "2025-E",
  "title": "2025年 CUMCM E题：AI 辅助智能体测",
  "problem_path": "cumcm/problems/2025/E.md",
  "question_index": 3,
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
RESULT_PATH = ROOT / "question_results" / "2025" / "E" / "q03" / "result.json"
REPORT_PATH = ROOT / "question_reports" / "2025" / "E" / "q03" / "report.md"
ARTIFACT_DIR = ROOT / "question_artifacts" / "2025" / "E" / "q03"


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
