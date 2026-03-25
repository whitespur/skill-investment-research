# Investment Research

A public `investment-research` skill for structured, one-off investment analysis.

## What It Does

This skill helps generate research on a single company, ticker, sector, or theme using a **20-dimension investment scorecard**. It is designed for:

- stock deep dives
- AI company analysis
- sector or theme mapping
- valuation discussion
- thesis, bear case, and risk review

This skill focuses on **analysis only**. It does **not** handle automated monitoring, portfolio tracking, or document export workflows.

## Core Framework

The default scoring system is a **20-dimension scorecard** covering:

- moat and technical edge
- business model and growth quality
- profitability and cash flow
- valuation and valuation history
- industry cycle and market position
- management, customer structure, and shareholder quality
- geopolitics, policy, and supply chain risk

The final rating uses these thresholds by default:

- `Strong Buy`: `>= 8.0`
- `Buy`: `>= 6.5`
- `Hold`: `>= 4.5`
- `Sell`: `< 4.5`

## Included Files

- `SKILL.md` — main skill definition and workflow
- `scripts/quick_analysis.py` — lightweight structured analysis scaffold
- `scripts/generate_radar_chart.py` — 20-dimension radar chart generator
- `templates/20_dimension_scorecard_template.md` — report template
- `examples/` — sample report and chart outputs

## Usage Notes

Use this skill when the task is a **one-off research request**.

Good examples:

- "Analyze AAOI as an investment."
- "Give me a deep-dive investment memo on LITE."
- "Compare several names in AI optical networking."
- "Score this company with a structured investment framework."

Do **not** use this skill as a substitute for:

- daily or weekly monitoring
- portfolio-wide change detection
- watchlist automation

## Dependencies

Install the minimal Python dependencies with:

```bash
pip install -r requirements.txt
```

Notes:

- `quick_analysis.py` uses only the Python standard library
- `generate_radar_chart.py` requires `matplotlib` and `numpy`

## Dependencies

Install the minimal Python dependencies with:

```bash
pip install -r requirements.txt
```

Notes:

- `quick_analysis.py` uses only the Python standard library
- `generate_radar_chart.py` requires `matplotlib` and `numpy`

## Scripts

### `quick_analysis.py`

Generate a lightweight analysis scaffold:

```bash
python3 scripts/quick_analysis.py --symbol AAOI --name "Applied Optoelectronics"
```

### `generate_radar_chart.py`

Generate a 20-dimension radar chart:

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

The radar chart output is English-first for public portability.

## Output Expectations

A typical report should include:

- executive summary
- 20-dimension scorecard
- valuation snapshot
- bull case / bear case
- risks and catalysts
- final rating with timing judgment

## Public Positioning

This skill is intentionally packaged as a **portable public research skill**.
It avoids private machine paths and private project-specific coupling, so it can be shared more easily.
