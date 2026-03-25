---
name: investment-research
description: Comprehensive investment research for stocks, AI companies, and selected crypto assets using a structured 20-dimension scorecard. Use when the user wants a structured research report, scorecard-based analysis, valuation discussion, thesis/risk breakdown, or deep-dive investment memo on a specific company, ticker, sector, or theme.
---

# Investment Research Skill v2.4

## Description

Perform structured investment research using the **20-dimension scoring framework defined in this skill** as the default source of truth.

This skill is for **single-name** or **single-theme** research work:
- stock deep dives
- AI company analysis
- sector/theme mapping
- valuation discussion
- thesis / bear-case / risk review

This skill focuses on **investment analysis only**.
Document conversion/export tasks are out of scope.

If the task is **continuous daily monitoring across a portfolio**, use a dedicated monitoring workflow rather than this one-off analysis skill.

---

## Core Rule

The canonical scoring framework is the 20-dimension framework documented in this skill.

If the current workspace provides an explicit scoring config for the same framework, follow that config.
Otherwise, use the weights and thresholds documented here as the source of truth.

---

## Workflows

### 1. Quick Analysis

Use for fast research on one company/ticker.

Do:
- get recent news and key events
- get current price / valuation snapshot
- score the company with the 20-dimension framework
- summarize thesis, risks, and current stage

### 2. Deep Dive Analysis

Use for a full investment memo.

Do:
- build event timeline
- analyze business model and moat
- evaluate industry position and cycle
- evaluate valuation and historical valuation position
- map risks, catalysts, and state transition
- generate structured scorecard and final rating

### 3. Theme / Sector Mapping

Use when the user asks for sector comparison or industry-chain mapping.

Do:
- identify the theme and sub-themes
- map leaders vs elastic names
- explain which dimension(s) drive relative strength
- avoid pretending this is equivalent to a live monitoring or watchlist automation system

---

## Core Analysis Framework (Latest 20-Dimension Scorecard)

Every serious equity-style report should use these 20 dimensions and weights.

| # | Dimension | Weight | What to judge |
|---|-----------|--------|---------------|
| 1 | `technical_moat` | 10% | Technical edge, architectural advantage, defensibility |
| 2 | `business_model` | 7% | Revenue logic, monetization quality, customer value capture |
| 3 | `revenue_growth` | 7% | Growth rate, growth quality, sustainability |
| 4 | `profitability` | 7% | Margin structure, path to profit, unit economics |
| 5 | `cash_flow` | 7% | Cash generation, runway, capital intensity |
| 6 | `valuation_history` | 7% | Current valuation vs own history / historical percentile |
| 7 | `geopolitics` | 7% | Geopolitical sensitivity, sanctions, war, cross-border risk |
| 8 | `state_transition` | 6% | Whether the asset is moving from concept → infrastructure / core asset |
| 9 | `valuation` | 6% | Absolute valuation vs peers / quality |
| 10 | `industry_cycle` | 6% | Industry phase: bottom / upcycle / mature / downcycle |
| 11 | `market_position` | 6% | Competitive position, share, bargaining power |
| 12 | `investment_phase` | 5% | Which investment phase the company is in |
| 13 | `moat_depth` | 5% | How deep and durable the moat really is |
| 14 | `customer_structure` | 3% | Customer quality, concentration, stickiness |
| 15 | `management` | 3% | Founder / management quality, execution credibility |
| 16 | `policy` | 2% | Regulatory and policy support / drag |
| 17 | `product_iteration` | 2% | Product cadence, iteration speed, roadmap execution |
| 18 | `supply_chain` | 2% | Supply resilience, upstream/downstream control |
| 19 | `shareholder` | 1% | Shareholder quality and alignment |
| 20 | `analyst_consensus` | 1% | Sell-side positioning / consensus backdrop |

### Category Grouping

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

## Rating Thresholds

Use these thresholds unless the user explicitly asks for a custom rubric.

- `Strong Buy`: `>= 8.0`
- `Buy`: `>= 6.5`
- `Hold`: `>= 4.5`
- `Sell`: `< 4.5`

Default missing dimension score:
- `5.0`

---

## Reporting Requirements

For each research report, include:

### 1. Executive Summary
- one-paragraph conclusion
- final score and rating
- key bull case
- key bear case
- what would change your mind

### 2. Scorecard Table
For each dimension, show:
- score
- weight
- brief evidence
- source / basis
- confidence label: `✅ Verified / ⚠️ Unverified / ❓ Unknown`

### 3. Valuation Section
Must include:
- current price
- market cap
- core valuation multiple(s)
- valuation vs history if available
- valuation vs peers if relevant

### 4. Thesis Section
Must include:
- bull case
- bear case
- key risk factors
- catalysts
- current investment phase

### 5. Final Judgment
Use one of:
- `Strong Buy`
- `Buy`
- `Hold`
- `Sell`

And explain **why now** or **why not now**.

---

## Data Rules

### Always prefer fresh data
For stocks / public equities, try to obtain:
- current price
- valuation metrics
- latest quarter / latest annual reference
- recent major news

### Always separate fact from inference
Use these labels consistently:
- `✅ Verified`
- `⚠️ Unverified`
- `❓ Unknown`

### Do not overstate precision
If data quality is weak, say so clearly.

---

## Recommended Output Shape

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

Use this skill when:
- the user wants a one-off report
- the user asks for a deep dive on a single ticker/company/theme
- the user wants a structured memo

Do not use this skill as a substitute for:
- daily/weekly automated monitoring
- portfolio-wide change detection
- watchlist automation

---

## Practical Guidance

### For AI / infrastructure names
Bias attention toward:
- `technical_moat`
- `state_transition`
- `market_position`
- `industry_cycle`
- `geopolitics`
- `supply_chain`

### For cyclical / manufacturing names
Bias attention toward:
- `industry_cycle`
- `valuation_history`
- `cash_flow`
- `market_position`
- `policy`

### For early-stage or speculative names
Be stricter on:
- `business_model`
- `cash_flow`
- `investment_phase`
- `state_transition`

---

## Maintenance Note

This skill reflects the public 20-dimension framework as of `2026-03-25`.
If the framework changes, update the weights, thresholds, and examples here to match.
