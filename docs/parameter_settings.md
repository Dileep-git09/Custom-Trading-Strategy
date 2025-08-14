# Parameter Settings for Pine Script Daily Trading Strategy

This document explains the adjustable parameters in `strategy.pine` and how they affect trading performance.

## 1. ATR Multiplier
- **Purpose:** Adjusts the trailing stop loss level.
- **Default:** 1.5
- **Effect:** Lower values tighten stop loss; higher values give trades more room.

## 2. Moving Average Lengths
- **Purpose:** Defines the periods for the short-term and long-term moving averages.
- **Default:** Short = 9, Long = 21
- **Effect:** Shorter lengths increase sensitivity; longer lengths smoothen signals.

## 3. Stop Loss & Take Profit
- **Purpose:** Defines fixed exit levels (in percentage).
- **Default:** SL = 1.5%, TP = 3%
- **Effect:** Affects risk-reward ratio and win rate.

## 4. Alert Conditions
- **Purpose:** Determines when buy/sell alerts are triggered.
- **Default:** On signal candle close.
- **Effect:** Can trigger alerts on candle open or intrabar.

---

**Tip:** Always backtest after changing parameters to evaluate the impact on performance.
