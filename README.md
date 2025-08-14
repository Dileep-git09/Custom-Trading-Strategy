# Custom-Trading-Strategy
# 📊 Custom Pine Script Strategy for Daily Trading

This repository contains my **custom Pine Script strategy** for intraday trading in **NIFTY index options** using TradingView.  
The strategy integrates multiple technical indicators and custom logic to produce high-probability buy/sell signals with automated alerts.

---

## 🚀 Features
- **ATR-based Trailing Stop Loss** – Protects profits and limits drawdowns dynamically.
- **Crossover Signals** – Detects market entry and exit points.
- **Heikin Ashi Integration** – Reduces noise and improves trend identification.
- **Custom Alerts** – Sends trade notifications in real-time.
- **Backtesting Support** – Evaluate performance on historical market data.

---

## 🛠 Tech Stack
- **Language:** Pine Script (TradingView)
- **Tools:** TradingView Charting Platform
- **Domain:** Algorithmic Trading, Technical Analysis

---

## 📈 Trading Logic
1. Detects market trends via moving average crossovers.
2. Confirms signals with Heikin Ashi candle patterns.
3. Applies ATR-based trailing stop loss.
4. Generates automated alerts for execution.

---

## 📊 Backtest Results
![Backtest Results](backtest_results.png)

---

## 🔧 Parameter Settings
Adjust parameters in `strategy.pine`:
- ATR Multiplier
- Moving Average Lengths
- Stop Loss Levels
- Alert Conditions

---

## 📂 Repository Structure
