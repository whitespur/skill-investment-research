---
name: investment-research
description: 面向股票、AI 公司与部分加密资产的结构化投研 skill，基于 20 维投资评分卡输出研究报告、估值分析、投资逻辑、风险拆解与深度 memo。Use when the user wants a structured research report, scorecard-based analysis, valuation discussion, thesis/risk breakdown, or deep-dive investment memo on a specific company, ticker, sector, or theme.
---

# Investment Research Skill v2.4

## 说明

使用本 skill 内定义的**20维投资评分框架**，完成结构化投研分析。

这个 skill 适用于**单标的**或**单主题**研究工作，例如：
- 个股深度分析
- AI 公司研究
- 行业 / 主题映射
- 估值讨论
- 多空逻辑 / 风险复盘

这个 skill **只负责分析**。
文档导出、自动化监控、组合级追踪不属于它的职责范围。

如果任务是**跨组合、连续、自动化**的监控型工作，应使用专门的监控工作流，而不是这个一次性分析 skill。

---

## 核心规则

默认以本 skill 中定义的 **20维评分框架** 作为分析基准。

如果当前工作区明确提供了同一框架下的评分配置，则优先使用工作区配置。
否则，以本 skill 中记录的权重、阈值和结构作为事实标准。

---

## 工作流

### 1. 快速分析

适用于快速研究单个公司 / ticker。

要做：
- 获取近期新闻和关键事件
- 获取当前价格和估值快照
- 用 20 维框架评分
- 提炼投资逻辑、核心风险、当前阶段判断

### 2. 深度分析

适用于完整投资 memo。

要做：
- 构建事件时间线
- 分析商业模式与护城河
- 评估行业地位与周期位置
- 评估估值与历史估值位置
- 映射风险、催化剂与状态跃迁
- 生成结构化评分卡与最终评级

### 3. 主题 / 行业映射

适用于用户要求行业对比、产业链梳理或主题映射时。

要做：
- 明确主题与子主题
- 区分龙头与弹性标的
- 解释相对强弱由哪些维度驱动
- 不要把这种一次性分析伪装成实时监控或 watchlist 自动化系统

---

## 核心分析框架（20维评分卡）

严肃的权益类研究，默认都应使用以下 20 个维度与权重。

| # | 维度 | 权重 | 核心判断 |
|---|------|------|----------|
| 1 | `technical_moat` | 10% | 技术优势、架构领先性、防御性 |
| 2 | `business_model` | 7% | 收入逻辑、变现质量、价值捕获 |
| 3 | `revenue_growth` | 7% | 增长速度、增长质量、持续性 |
| 4 | `profitability` | 7% | 利润结构、盈利路径、单位经济性 |
| 5 | `cash_flow` | 7% | 现金创造能力、资本开支、跑道 |
| 6 | `valuation_history` | 7% | 当前估值相对自身历史区间 |
| 7 | `geopolitics` | 7% | 地缘政治、制裁、战争、跨境风险 |
| 8 | `state_transition` | 6% | 是否处于概念 → 基建 / 核心资产跃迁 |
| 9 | `valuation` | 6% | 绝对估值与同业比较 |
| 10 | `industry_cycle` | 6% | 行业所处阶段：底部 / 上行 / 成熟 / 下行 |
| 11 | `market_position` | 6% | 竞争地位、份额、议价能力 |
| 12 | `investment_phase` | 5% | 当前投资阶段位置 |
| 13 | `moat_depth` | 5% | 护城河深度与持续性 |
| 14 | `customer_structure` | 3% | 客户质量、集中度、粘性 |
| 15 | `management` | 3% | 创始人 / 管理层质量与执行力 |
| 16 | `policy` | 2% | 监管与政策支持 / 拖累 |
| 17 | `product_iteration` | 2% | 产品节奏、迭代速度、路线图兑现 |
| 18 | `supply_chain` | 2% | 供应链韧性、上下游控制力 |
| 19 | `shareholder` | 1% | 股东结构与利益一致性 |
| 20 | `analyst_consensus` | 1% | 卖方一致预期与市场共识背景 |

### 分类分组

#### Quantitative
- `valuation`
- `valuation_history`
- `cash_flow`
- `revenue_growth`
- `profitability`
- `industry_cycle`

#### Qualitative
- `technical_moat`
- `moat_depth`
- `business_model`
- `market_position`
- `state_transition`
- `investment_phase`
- `management`
- `customer_structure`
- `shareholder`
- `analyst_consensus`
- `product_iteration`
- `supply_chain`

#### Macro
- `geopolitics`
- `policy`

---

## 评级阈值

除非用户明确要求自定义标准，否则默认使用：

- `Strong Buy`: `>= 8.0`
- `Buy`: `>= 6.5`
- `Hold`: `>= 4.5`
- `Sell`: `< 4.5`

默认缺失维度分数：
- `5.0`

---

## 报告要求

每份研究报告默认应包括：

### 1. Executive Summary
- 一段话结论
- 最终得分与评级
- 核心 bull case
- 核心 bear case
- 什么条件会改变判断

### 2. Scorecard Table
每个维度至少展示：
- score
- weight
- brief evidence
- source / basis
- confidence label: `✅ Verified / ⚠️ Unverified / ❓ Unknown`

### 3. Valuation Section
必须包含：
- current price
- market cap
- core valuation multiple(s)
- valuation vs history（若可得）
- valuation vs peers（若相关）

### 4. Thesis Section
必须包含：
- bull case
- bear case
- key risk factors
- catalysts
- current investment phase

### 5. Final Judgment
必须使用以下之一：
- `Strong Buy`
- `Buy`
- `Hold`
- `Sell`

并明确解释 **why now** 或 **why not now**。

---

## 数据规则

### 优先新数据
对于股票 / 上市公司，尽量拿到：
- 当前价格
- 估值指标
- 最新季度 / 最新年报参考
- 近期重大新闻

### 事实与推断必须分开
统一使用：
- `✅ Verified`
- `⚠️ Unverified`
- `❓ Unknown`

### 不要伪装精确度
如果数据质量一般，必须直接说清楚。

---

## 推荐输出结构

```markdown
# [Company / Ticker] Investment Research

## Executive Summary
- Final rating: [Rating]
- Total score: X.XX / 10
- Core essence: ...
- Why now / why not now: ...

## 20-Dimension Scorecard
| Dimension | Score | Weight | Evidence | Confidence |
|-----------|------:|-------:|----------|------------|

## Valuation
- Current price:
- Market cap:
- Core multiple(s):
- Historical valuation position:
- Peer comparison:

## Thesis
### Bull Case
- ...

### Bear Case
- ...

### Key Risks
- ...

### Catalysts
- ...

## Final Judgment
- Rating:
- What would upgrade the name:
- What would downgrade the name:
```

---

## Scope Boundary

适合使用本 skill 的场景：
- 用户要一份 one-off 研究报告
- 用户要单一公司 / 单一主题的深度分析
- 用户要结构化 memo

不适合用本 skill 代替的场景：
- 每日 / 每周自动监控
- 全组合变化检测
- watchlist 自动化

---

## 实操建议

### AI / infrastructure 类标的
重点关注：
- `technical_moat`
- `state_transition`
- `market_position`
- `industry_cycle`
- `geopolitics`
- `supply_chain`

### 周期 / 制造类标的
重点关注：
- `industry_cycle`
- `valuation_history`
- `cash_flow`
- `market_position`
- `policy`

### 早期 / 高波动标的
要更严格地看：
- `business_model`
- `cash_flow`
- `investment_phase`
- `state_transition`

---

## Maintenance Note

This skill reflects the public 20-dimension framework as of `2026-03-25`.
If the framework changes, update the weights, thresholds, and examples here to match.
