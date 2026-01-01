import pandas as pd

def calculate_probabilities(trades_df, current_setup, tolerance=0.1):
    similar = trades_df[
        (trades_df['dir'] == current_setup['dir']) &
        (abs(trades_df['rsi'] - current_setup['rsi']) <= tolerance * 100) &
        (abs(trades_df['adx'] - current_setup['adx']) <= tolerance * 50) &
        (trades_df['session'] == current_setup['session'])
    ]
    if len(similar) < 30:
        return {"probability": None, "sample_size": len(similar), "expectancy": None}
    win_rate = (similar['result'] > 0).mean()
    expectancy = similar['result'].mean()
    return {"probability": round(win_rate*100,2), "sample_size": len(similar), "expectancy": round(expectancy,2)}
