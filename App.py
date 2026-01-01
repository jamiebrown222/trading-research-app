import streamlit as st
import pandas as pd
from backtester import backtest, add_indicators, analyse
from optimiser import optimise
from probabilities import calculate_probabilities

st.title("FX & Indices Trading Research App")

uploaded_file = st.file_uploader("Upload OHLC CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['time'] = pd.to_datetime(df['time'], utc=True)
    df.set_index('time', inplace=True)
    st.write(df.head())

    params = {
        "ema_fast": 20, "ema_slow": 50, "adx_min": 20,
        "rsi_buy_min": 45, "rsi_buy_max": 65,
        "rsi_sell_min": 35, "rsi_sell_max": 55,
        "atr_sl": 1.5, "rr": 2, "session": "LONDON_NY"
    }

    df = add_indicators(df, params)
    trades, equity = backtest(df, params)
    st.write("Backtest complete")
    st.line_chart(equity)
    stats = analyse(trades, equity)
    st.write(stats)

    if trades:
        last_trade = trades[-1]
        prob = calculate_probabilities(pd.DataFrame(trades), last_trade)
        st.write("Last setup probabilities:", prob)

    if st.button("Run optimisation"):
        st.write("Optimising...")
        ranked = optimise(df)
        st.write(ranked.head(10))
