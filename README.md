# worker — 高考错题权重分析

> 记录做错的题 → 自动计算各**知识点的权重** → 输出**复习优先级排行**，帮你决定「先补哪个考点」。

本地运行的错题分析小站（Flask + SQLite），预置 **数学 / 物理 / 化学 / 生物** 四科的新高考全国卷试卷结构与常见考点，开箱即用。

## 权重算法

每条错题记录的权重 = **客观难度系数 × 主观感受因子 × 分值占比 × 错误频次加成**

| 因子 | 取值 | 含义 |
|---|---|---|
| 客观难度系数 | 基础 5 / 中档 3 / 压轴 1 | 越基础的题做错，越说明基础有漏洞 |
| 主观感受因子 | 6 − 自评难度(1–5) | 你做得越吃力的题，权重越高 |
| 分值占比 | 该题分值 ÷ 该科平均题分 | 大题失分更「贵」 |
| 错误频次加成 | 第 1 次 ×1.0 / 第 2 次 ×1.3 / 第 3 次 ×1.6 / 第 4 次起 ×2.0 | 同一考点反复错，加成递增 |

按考点汇总后，与全科平均权重比较划分 **极高 / 高 / 中 / 低** 四档优先级，并给出累计权重曲线图（Chart.js）。

## 快速开始

```bash
pip install -r requirements.txt
python app.py
# 浏览器打开 http://localhost:5000
```

首次启动自动建库（SQLite：`wrong_questions.db`）并写入种子数据。

## 页面

| 路径 | 功能 |
|---|---|
| `/` | 仪表盘：各科错题总数、高优先级考点数 |
| `/record` | 记录错题：学科 → 题号 → 考点 → 自评难度(1–5) → 备注 |
| `/analysis/<学科id>` | 权重分析与复习顺序（含图表） |
| `/history` | 错题历史 |

## 技术栈

Flask 3.1 · SQLAlchemy 2.0 · SQLite · Chart.js

> 图表库经 jsDelivr CDN 加载，分析页首次打开需联网；离线环境可自行下载 chart.js 替换为本地文件。

## 目录结构

```
app.py            Flask 入口与路由
models.py         Subject / Question / KnowledgePoint / WrongRecord 数据模型
seed_data.py      四科试卷结构与考点种子数据（基于 2024–2025 新高考全国卷）
weight_engine.py  权重计算与优先级划分
templates/        页面模板（base / index / record / analysis / history）
static/style.css  样式
```

## 说明

- 数据完全存储在本地 `wrong_questions.db`，不联网上传。
- 换用其他省市卷时，可直接修改 `seed_data.py` 中的试卷结构与考点。
