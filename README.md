# Investment Research

一个面向公开分发的 `investment-research` skill，用于进行**结构化、一次性**投研分析。

## 这个技能做什么

这个 skill 用一套**20维投资评分卡**，帮助你对单个公司、单个股票代码、单个行业或单个主题做结构化研究。适用场景包括：

- 个股深度分析
- AI 公司分析
- 行业 / 主题对比
- 估值讨论
- 投资逻辑、风险与反方观点梳理

这个 skill **只做分析**，不负责：

- 自动化监控
- 组合跟踪
- watchlist 自动化
- 文档导出流程

## 核心框架

默认使用一套**20维投资评分卡**，覆盖：

- 技术护城河与竞争优势
- 商业模式与增长质量
- 盈利能力与现金流
- 当前估值与历史估值位置
- 行业周期与市场地位
- 管理层、客户结构、股东结构
- 地缘政治、政策、供应链风险

默认评级阈值：

- `Strong Buy`: `>= 8.0`
- `Buy`: `>= 6.5`
- `Hold`: `>= 4.5`
- `Sell`: `< 4.5`

## 包含文件

- `SKILL.md` — 技能定义与工作流说明
- `scripts/quick_analysis.py` — 轻量分析脚手架
- `scripts/generate_radar_chart.py` — 20维雷达图生成脚本
- `templates/20_dimension_scorecard_template.md` — 报告模板
- `examples/` — 示例报告与示例图
- `requirements.txt` — 脚本所需的最小 Python 依赖

## 依赖

安装最小依赖：

```bash
pip install -r requirements.txt
```

说明：

- `quick_analysis.py` 只依赖 Python 标准库
- `generate_radar_chart.py` 依赖 `matplotlib` 和 `numpy`

## 使用建议

这个 skill 适合**一次性投研请求**。

典型示例：

- “分析一下 AAOI 这家公司值不值得投。”
- “给我做一份 LITE 的深度投研 memo。”
- “比较一下 AI 光通信板块几个核心标的。”
- “用结构化投资框架给这家公司打分。”

不建议把这个 skill 当成以下任务的替代品：

- 每日 / 每周自动监控
- 全组合变化检测
- watchlist 自动化追踪

## 脚本

### `quick_analysis.py`

生成一个轻量分析框架：

```bash
python3 scripts/quick_analysis.py --symbol AAOI --name "Applied Optoelectronics"
```

### `generate_radar_chart.py`

生成 20 维投资雷达图：

```bash
python3 scripts/generate_radar_chart.py \
  --scores "7,6,8,6,5,7,4,8,6,7,6,5,6,4,6,5,6,5,4,5" \
  --ticker AAOI \
  --total 6.35 \
  --rating Buy \
  --price 113.9 \
  --pe 18 \
  --output-dir ./out
```

雷达图输出默认是 **English-first**，方便公开分发时避免中文字体兼容问题。

## 输出预期

一份标准报告通常应包括：

- executive summary
- 20维评分卡
- 估值快照
- bull case / bear case
- 风险与催化剂
- 最终评级与时点判断

## 对外定位

这个 skill 被刻意整理成一个**可公开分发、可移植**的投研技能。

它避免绑定私有机器路径和私有项目流程，因此更适合公开展示、共享和复用。
