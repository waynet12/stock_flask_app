def BBAND_Indicator(BBANDS_lower,BBANDS_higher,current_price):
    if current_price < float(BBANDS_lower):
        condition = "Oversold"
    elif current_price > float(BBANDS_higher):
        condition = "Overbought"
    else:
        condition = "Neutral"
    return condition

def SMA_Indicator(SMA_Shorter,SMA_Longer):
    if float(SMA_Shorter) > float(SMA_Longer):
        condition = "Buy"
    else:
        condition = "Sell"
    return condition

def RSI_Indicator(rsi):
    if float(rsi) > 70:
        condition = "Overbought"
    elif float(rsi) < 30:
        condition = "Oversold"
    else:
        condition = "Neutral"
    return condition