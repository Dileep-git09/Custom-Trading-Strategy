# Strategy Logic – Pine Script Daily Trading Bot

## Indicators Used
- Moving Average Crossovers
- ATR (Average True Range)
- Heikin Ashi Candles

## Entry Rules
- Bullish crossover detected.
- Heikin Ashi candle turns green.
- ATR value confirms volatility conditions.

## Exit Rules
- Bearish crossover detected.
- ATR trailing stop is hit.
- Time-based exit if position is open past defined session.

---

## Alert System
Alerts are triggered when:
- Buy signal is generated.
- Sell signal is generated.
- Stop loss or take profit is hit.

---
