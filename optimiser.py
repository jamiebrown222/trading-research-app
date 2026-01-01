import itertools
from backtester import backtest, add_indicators, analyse

def optimise(df):
    grid = {
        "ema_fast": [10, 20],
        "ema_slow": [50, 100],
        "adx_min": [20, 25],
        "rsi_buy_min": [45, 50],
        "rsi_buy_max": [65, 70],
        "rsi_sell_min": [30, 35],
        "rsi_sell_max": [50, 55],
        "atr_sl": [1.2, 1.5],
        "rr": [2, 3],
        "session": ["LONDON", "LONDON_NY"]
    }

    keys = grid.keys()
    results = []

    for combo in itertools.product(*grid.values()):
        p = dict(zip(keys, combo))
        data = add_indicators(df.copy(), p)
        trades, equity = backtest(data, p)
        stats = analyse(trades, equity)
        if stats and stats['trades'] >= 50 and stats['expectancy'] > 0:
            results.append({**p, **stats})

    return pd.DataFrame(results).sort_values(by=['expectancy', 'win_rate'], ascending=False)
