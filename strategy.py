//@version=5
strategy("Advanced NIFTY Scalping Strategy v3", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// === USER INPUTS === //
sensitivity     = input.float(1.0, "UTBot Sensitivity", step=0.1)
atrPeriod       = input.int(10, "ATR Period")
rsiPeriod       = input.int(14, "RSI Period")
rsiOverbought   = input.int(70, "RSI Overbought Level")
rsiOversold     = input.int(30, "RSI Oversold Level")
fastEMA         = input.int(50, "Fast EMA")
slowEMA         = input.int(200, "Slow EMA")
useMACD         = input.bool(true, "Enable MACD Confirmation")
useHeikinAshi   = input.bool(false, "Use Heikin Ashi Candles")

tpPerc          = input.float(0.5, "Take Profit (%)", step=0.1)
tslPerc         = input.float(0.3, "Trailing Stop Loss (%)", step=0.1)

// === PRICE SOURCE === //
haTicker = ticker.heikinashi(syminfo.tickerid)
haClose  = request.security(haTicker, timeframe.period, close)
src      = useHeikinAshi ? haClose : close

// === INDICATORS === //
emaFast         = ta.ema(close, fastEMA)
emaSlow         = ta.ema(close, slowEMA)
rsi             = ta.rsi(close, rsiPeriod)
[macdLine, signalLine, _] = ta.macd(close, 12, 26, 9)
macdBullish     = macdLine > signalLine
macdBearish     = macdLine < signalLine

// === UT BOT ATR TRAILING STOP === //
atr = ta.atr(atrPeriod)
nLoss = sensitivity * atr

var float trailingStop = na
trailingStop := src > nz(trailingStop[1]) and src[1] > nz(trailingStop[1]) ? math.max(nz(trailingStop[1]), src - nLoss) :
                 src < nz(trailingStop[1]) and src[1] < nz(trailingStop[1]) ? math.min(nz(trailingStop[1]), src + nLoss) :
                 src > nz(trailingStop[1]) ? src - nLoss : src + nLoss

var int trend = 0
trend := src > trailingStop ? 1 : src < trailingStop ? -1 : nz(trend[1])

// === CONDITIONS === //
trendUp     = trend == 1
trendDown   = trend == -1
bullFilter  = emaFast > emaSlow and rsi < rsiOverbought and (macdBullish or not useMACD)
bearFilter  = emaFast < emaSlow and rsi > rsiOversold and (macdBearish or not useMACD)

buySignal   = trendUp and bullFilter
sellSignal  = trendDown and bearFilter

// === STRATEGY ENTRIES === //
strategy.entry("Buy", strategy.long, when=buySignal)
strategy.entry("Sell", strategy.short, when=sellSignal)

// === STRATEGY EXITS === //
strategy.close("Buy", when=sellSignal)
strategy.close("Sell", when=buySignal)

// === TAKE PROFIT & TRAILING STOP LOGIC === //
longTakeProfit   = strategy.position_avg_price * (1 + tpPerc / 100)
longStopLoss     = strategy.position_avg_price * (1 - tslPerc / 100)
shortTakeProfit  = strategy.position_avg_price * (1 - tpPerc / 100)
shortStopLoss    = strategy.position_avg_price * (1 + tslPerc / 100)

if (strategy.position_size > 0)
    strategy.exit("TP/SL Long", from_entry="Buy", limit=longTakeProfit, stop=longStopLoss)

if (strategy.position_size < 0)
    strategy.exit("TP/SL Short", from_entry="Sell", limit=shortTakeProfit, stop=shortStopLoss)

// === PLOTS === //
plot(trailingStop, title="ATR Trailing Stop", color=color.orange, linewidth=2)
plot(emaFast, title="EMA 50", color=color.blue)
plot(emaSlow, title="EMA 200", color=color.red)

plotshape(buySignal, title="Buy Signal", style=shape.labelup, location=location.belowbar, color=color.green, text="BUY", textcolor=color.white)
plotshape(sellSignal, title="Sell Signal", style=shape.labeldown, location=location.abovebar, color=color.red, text="SELL", textcolor=color.white)

// === ALERTS === //
alertcondition(buySignal, title="Buy Alert", message="NIFTY Buy Signal Triggered!")
alertcondition(sellSignal, title="Sell Alert", message="NIFTY Sell Signal Triggered!")
