from flask import Flask,render_template,request, url_for, flash, redirect,session
import yfinance as yf
import analysis_functions.calculations as StockCalc
from analysis_functions.determine_trend import BBAND_Indicator,SMA_Indicator,RSI_Indicator
import os
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/output/<ticker>',methods=["GET"])
def output(ticker):
    yfdata = yf.download(ticker, start="2020-01-01", end="2022-04-30")
    current_price = yfdata['Close'].iloc[-1]
    StockOutput = StockCalc.StockProperties(ticker=ticker,yfdata=yfdata)
    BBANDS = StockOutput.BBANDS()
    BBANDS_lower = BBANDS[0]
    BBANDS_higher = BBANDS[1]
    SMA_Shorter = StockOutput.SMA_Shorter()
    SMA_Longer = StockOutput.SMA_Longer()
    RSI = StockOutput.RSI()

    BBAND_condition = BBAND_Indicator(BBANDS_lower=BBANDS_lower,BBANDS_higher=BBANDS_higher, current_price=current_price)
    SMA_condition = SMA_Indicator(SMA_Shorter=SMA_Shorter,SMA_Longer=SMA_Longer)
    RSI_condition = RSI_Indicator(rsi=RSI)

    outputDict = {"ticker":ticker,"BBAND":{"BBAND_lower":BBANDS_lower,"BBAND_higher":BBANDS_higher,"BBAND_condition":BBAND_condition},"SMA":{"SMA_Shorter":SMA_Shorter,"SMA_Longer":SMA_Longer,"SMA_condition":SMA_condition},"RSI":{"RSI":RSI,"RSI_condition":RSI_condition}}
    return render_template('/output.html',outputDict=outputDict)

@app.route('/',methods=("POST","GET"))
def index():
    if request.method == "POST":
        ticker = request.form['ticker']
        if ticker is "":
            flash("No ticker input","error")
            return redirect(url_for("index"))
        else:
            today = (datetime.datetime.now()).strftime('%Y-%m-%d')
            yfdata = yf.download(ticker, start="2020-01-01", end=today)

            if yfdata.empty:
                flash("Invalid ticker","error")
                return redirect(url_for("index"))
            else:
                session["yfdata"] = yfdata.to_json()
                return redirect(url_for("output",ticker=ticker))

    return render_template('/index.html')

if __name__ == "__main__":
    app.run()

