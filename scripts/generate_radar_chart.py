#!/usr/bin/env python3
"""
Investment Research Radar Chart Generator
Generates 20-dimension investment scorecard visualization
"""

import argparse
import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np


RATING_EN_MAP = {
    'strong buy': 'Strong Buy',
    'buy': 'Buy',
    'hold': 'Hold',
    'sell': 'Sell',
    '强烈买入': 'Strong Buy',
    '强力买入': 'Strong Buy',
    '买入': 'Buy',
    '持有': 'Hold',
    '观望': 'Hold',
    '卖出': 'Sell',
}


def english_only_text(value, fallback='N/A'):
    if value is None:
        return fallback
    text = str(value).strip()
    if not text:
        return fallback
    mapped = RATING_EN_MAP.get(text.lower())
    if mapped:
        return mapped
    ascii_text = text.encode('ascii', 'ignore').decode('ascii').strip()
    return ascii_text or fallback


LABELS_20 = [
    'Tech Moat\n(10%)',
    'Business\nModel (7%)',
    'Revenue\nGrowth (7%)',
    'Profitability\n(7%)',
    'Cash\nFlow (7%)',
    'Valuation\nHistory (7%)',
    'Geopolitics\n(7%)',
    'State\nTransition (6%)',
    'Valuation\n(6%)',
    'Industry\nCycle (6%)',
    'Market\nPosition (6%)',
    'Investment\nPhase (5%)',
    'Moat\nDepth (5%)',
    'Customer\nStructure (3%)',
    'Management\n(3%)',
    'Policy\n(2%)',
    'Product\nIteration (2%)',
    'Supply\nChain (2%)',
    'Shareholder\n(1%)',
    'Analyst\nConsensus (1%)',
]


def parse_scores(scores_str):
    return [float(item.strip()) for item in scores_str.split(',')]


def validate_scores(scores):
    if len(scores) != 20:
        raise ValueError(f"Expected 20 scores, got {len(scores)}")
    if not all(0 <= score <= 10 for score in scores):
        raise ValueError("All scores must be between 0 and 10")
    return scores


def format_score_label(score):
    if float(score).is_integer():
        return str(int(score))
    return f"{score:.1f}"


def format_pe_label(pe_ratio):
    if pe_ratio is None or pe_ratio <= 0:
        return "N/A"
    if float(pe_ratio).is_integer():
        return f"{int(pe_ratio)}x"
    return f"{pe_ratio:.1f}x"


def get_score_color(score):
    if score >= 7:
        return '#28a745'
    if score <= 4:
        return '#dc3545'
    return '#ffc107'


def generate_radar_chart(scores, ticker, total_score, rating, price, pe_ratio, output_dir='.', warning_msg=None):
    scores = validate_scores(scores)
    rating_label = english_only_text(rating, fallback='Unrated')
    warning_label = english_only_text(warning_msg, fallback='See report notes for risk flags') if warning_msg else None
    ticker_label = english_only_text(ticker, fallback='TICKER')
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    scores_plot = scores + scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(14, 14), subplot_kw=dict(projection='polar'))
    ax.plot(angles, scores_plot, 'o-', linewidth=3, color='#2E86AB', markersize=8)
    ax.fill(angles, scores_plot, alpha=0.25, color='#2E86AB')

    ax.plot(angles, [6] * len(angles), '--', linewidth=1.5, color='orange', alpha=0.8, label='Pass Line (6)')
    ax.plot(angles, [10] * len(angles), '--', linewidth=1, color='gray', alpha=0.4, label='Max (10)')

    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10, fontweight='bold')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(LABELS_20, fontsize=9)

    title = (
        f'{ticker_label} 20-Dimension Investment Scorecard\n'
        f'Total: {total_score}/10 | Rating: {rating_label} | Price: ${price} | P/E: {pe_ratio}x'
    )
    plt.title(title, fontsize=15, fontweight='bold', pad=30, color='#1a1a2e')

    for angle, score in zip(angles[:-1], scores):
        color = get_score_color(score)
        ax.annotate(
            format_score_label(score),
            xy=(angle, score),
            xytext=(angle, score + 0.6),
            fontsize=10,
            ha='center',
            fontweight='bold',
            color=color,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.8),
        )

    ax.legend(loc='upper right', bbox_to_anchor=(1.28, 1.12), fontsize=10)

    if warning_label:
        fig.text(
            0.5,
            0.02,
            f'⚠️ WARNING: {warning_label}',
            ha='center',
            fontsize=11,
            color='#dc3545',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3cd', edgecolor='#dc3545'),
        )
        plt.subplots_adjust(bottom=0.08)

    plt.tight_layout()
    timestamp = datetime.now().strftime('%Y%m%d')
    filename = f'{ticker}-radar-chart-{timestamp}.png'
    filepath = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Radar chart saved: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description='Generate 20-dimension investment scorecard radar chart')
    parser.add_argument('--scores', required=True, help='Comma-separated 20 dimension scores (0-10)')
    parser.add_argument('--ticker', required=True, help='Stock ticker symbol')
    parser.add_argument('--total', type=float, required=True, help='Weighted total score')
    parser.add_argument('--rating', required=True, help='Investment rating')
    parser.add_argument('--price', type=float, required=True, help='Current stock price')
    parser.add_argument('--pe', type=float, required=True, help='P/E ratio')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--warning', default=None, help='Optional warning message')
    args = parser.parse_args()

    scores = parse_scores(args.scores)
    generate_radar_chart(
        scores=scores,
        ticker=args.ticker,
        total_score=args.total,
        rating=args.rating,
        price=args.price,
        pe_ratio=args.pe,
        output_dir=args.output_dir,
        warning_msg=args.warning,
    )


if __name__ == '__main__':
    main()
