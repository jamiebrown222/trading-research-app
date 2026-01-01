def is_trading_session(ts, session):
    h = ts.hour
    if session == "LONDON": return 7 <= h < 16
    if session == "NEW_YORK": return 12 <= h < 21
    if session == "OVERLAP": return 12 <= h < 16
    if session == "LONDON_NY": return 7 <= h < 21
    return False
