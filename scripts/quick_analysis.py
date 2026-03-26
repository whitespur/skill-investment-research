#!/usr/bin/env python3
"""
投资研究快速分析脚本
执行单标的快速分析流程（20维框架轻量版）
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

LATEST_20D = [
    ("technical_moat", 10.0),
    ("business_model", 7.0),
    ("revenue_growth", 7.0),
    ("profitability", 7.0),
    ("cash_flow", 7.0),
    ("valuation_history", 7.0),
    ("geopolitics", 7.0),
    ("state_transition", 6.0),
    ("valuation", 6.0),
    ("industry_cycle", 6.0),
    ("market_position", 6.0),
    ("investment_phase", 5.0),
    ("moat_depth", 5.0),
    ("customer_structure", 3.0),
    ("management", 3.0),
    ("policy", 2.0),
    ("product_iteration", 2.0),
    ("supply_chain", 2.0),
    ("shareholder", 1.0),
    ("analyst_consensus", 1.0),
]


def quick_analysis(symbol: str, name: str, sector: str = "") -> Dict[str, Any]:
    return {
        "metadata": {
            "symbol": symbol,
            "name": name,
            "sector": sector,
            "analysis_type": "quick",
            "framework": "latest-20-dimension-scorecard",
            "generated_at": datetime.now().isoformat(),
            "estimated_duration": "15 minutes",
        },
        "workflow": {
            "step_1_news_and_events": {
                "status": "pending",
                "queries": [
                    f"{name} {symbol} latest news",
                    f"{name} earnings guidance",
                    f"{name} industry cycle catalyst",
                ],
            },
            "step_2_market_snapshot": {
                "status": "pending",
                "metrics": ["current_price", "market_cap", "pe_or_ps", "52_week_range", "analyst_targets"],
            },
            "step_3_20d_scorecard": {
                "status": "pending",
                "dimensions": [{"name": name, "weight": weight} for name, weight in LATEST_20D],
            },
            "step_4_thesis_and_risks": {
                "status": "pending",
                "sections": ["bull_case", "bear_case", "catalysts", "why_now_or_not_now"],
            },
        },
        "output_template": {
            "executive_summary": {
                "rating": "Strong Buy / Buy / Hold / Sell",
                "total_score": "X.XX / 10",
                "confidence": "HIGH / MEDIUM / LOW",
            },
            "valuation_snapshot": {
                "current_price": None,
                "market_cap": None,
                "valuation_metric": None,
                "valuation_history": None,
            },
            "scorecard": [{"dimension": name, "weight": weight, "score": None} for name, weight in LATEST_20D],
            "bull_case": [],
            "bear_case": [],
            "catalysts": [],
            "final_judgment": {
                "why_now": "",
                "what_upgrades": "",
                "what_downgrades": "",
            },
        },
    }


def default_output_path(symbol: str) -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    return Path("reports") / today / f"{symbol.upper()}-quick-analysis.json"


def main():
    parser = argparse.ArgumentParser(description="投资研究快速分析 - 最新20维框架")
    parser.add_argument("--symbol", "-s", required=True, help="股票代码或代币符号")
    parser.add_argument("--name", "-n", required=True, help="公司名称")
    parser.add_argument("--sector", default="", help="行业/板块")
    parser.add_argument("--output", "-o", help="输出文件路径 (JSON格式)，默认保存到 reports/YYYY-MM-DD/")
    args = parser.parse_args()

    report = quick_analysis(args.symbol, args.name, args.sector)
    output_path = Path(args.output) if args.output else default_output_path(args.symbol)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
    print(f"✅ 分析框架已保存: {output_path}")


if __name__ == "__main__":
    main()
