import pandas as pd

class StockProperties:
    def __init__(self,ticker,yfdata):
        self.ticker = ticker
        self.yfdata = yfdata

    def SMA_Shorter(self):
        yfdata = self.yfdata
        SMA = pd.Series(yfdata['Close'].rolling(50).mean(), name='SMA')
        yfdata = yfdata.join(SMA)
        SMA = yfdata.dropna()
        SMA = str(round(SMA['SMA'][0],2))

        return SMA
    def SMA_Longer(self):
        yfdata = self.yfdata
        SMA = pd.Series(yfdata['Close'].rolling(200).mean(), name='SMA')
        yfdata = yfdata.join(SMA)
        SMA = yfdata.dropna()
        SMA = str(round(SMA['SMA'][0], 2))
        return SMA
    def BBANDS(self):
        yfdata = self.yfdata
        MA = yfdata.Close.rolling(window=50).mean()
        SD = yfdata.Close.rolling(window=50).std()
        upperBand = MA + (2 * SD)
        lowerBand = MA - (2 * SD)
        BBANDSArray = [str(round(lowerBand[-1],2)),str(round(upperBand[-1],2))]
        return BBANDSArray

    def RSI(self):
        yfdata = self.yfdata
        time_window = 14
        diff = yfdata.diff(1).dropna()
        up_chg = 0 * diff
        down_chg = 0 * diff
        up_chg[diff > 0] = diff[diff > 0]
        down_chg[diff < 0] = diff[diff < 0]
        up_chg_avg = up_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
        down_chg_avg = down_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
        rs = abs(up_chg_avg / down_chg_avg)
        rsi = round(100 - 100 / (1 + rs),2)
        rsi = str(rsi['Adj Close'].iat[-1])
        return rsi


