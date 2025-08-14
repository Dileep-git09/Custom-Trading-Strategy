# Strategy Logic – Pine Script Daily Trading Bot

## 1. Overview
This strategy is designed for **intraday trading** on **NIFTY index options**.  
It combines trend-following and volatility-based exit logic to maximize returns while controlling risk.

---

## 2. Indicators Used
1. **Moving Average Crossovers**
   - Two moving averages: Short-term and Long-term.
   - Bullish signal: Short MA crosses above Long MA.
   - Bearish signal: Short MA crosses below Long MA.

2. **ATR (Average True Range)**
   - Measures market volatility.
   - Used to calculate a **dynamic trailing stop loss**.
   - Higher ATR = wider stops; lower ATR = tighter stops.

3. **Heikin Ashi Candles**
   - Smooths price action to filter out market noise.
   - Confirms trend direction before entering trades.

---

## 3. Entry Rules
**Long Entry (Buy)**
- Short MA crosses above Long MA.
- Current Heikin Ashi candle is bullish (green).
- ATR confirms acceptable volatility conditions.

**Short Entry (Sell)**
- Short MA crosses below Long MA.
- Current Heikin Ashi candle is bearish (red).
- ATR confirms acceptable volatility conditions.

---

## 4. Exit Rules
**Stop Loss (SL)**
- ATR-based trailing stop loss adjusts dynamically as trade moves in favor.

**Take Profit (TP)**
- Fixed percentage target (default: 3%).
- Can be modified in the parameter settings.

**Time Exit**
- Positions automatically closed at session end to avoid overnight risk.

---

## 5. Alerts
Alerts are generated when:
- Buy or Sell entry conditions are met.
- Stop loss or take profit is hit.
- Time-based exit is triggered.

These alerts can be connected to a broker or bot via webhooks for automated execution.

---

## 6. Backtesting
- Strategy tested on historical **NIFTY intraday data**.
- Metrics reviewed:
  - **Win Rate (%)**
  - **Return on Investment (ROI%)**
  - **Max Drawdown (%)**
  - **Risk-Reward Ratio**

---

## 7. Advantages
- Combines trend detection (MA crossovers) with noise reduction (Heikin Ashi).
- Dynamic stop loss adapts to market conditions.
- Works well in volatile intraday markets like NIFTY options.

---

## 8. Limitations
- Performance can vary in low-volatility sideways markets.
- Requires parameter optimization for different instruments/timeframes.

---

## 9. Usage Tips
- Always re-optimize parameters before applying in live markets.
- Combine with broader market analysis for better decision-making.
- Test on paper trading before going live.

---
