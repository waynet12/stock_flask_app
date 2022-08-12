# stock_flask_app

A simple web app developed with the Flask framework. 

The purpose of this application is to input a stock symbol and retrieve an analysis of whether to buy a stock based on technical indicators. **This application is for demo purposes only and should not be used for finanical advice**


## Running the app in local development
The Docker Compose file allows you to run the app locally in development. To start the container, run: 
```
$ docker-compose up
```
Once the stack is launched, try testing the application by navigating to:
- http://localhost:50000/ to access the "stock_flask_app" application. 

Type in a stock ticker to get the technical indicators. 

## Technical Indicators

The following are the technical indicators used:
- [Bollinger Bands](https://www.investopedia.com/terms/b/bollingerbands.asp) - Use three trendlines (upper, middle, and lower bands) to determine whether an asset is overbought or oversold.
    - **Overbought condition** - If the current price is greater than the higher band
    - **Oversold condition** - If the current price is less than the lower band
- [Simple Moving Average](https://www.investopedia.com/terms/s/sma.asp#:~:text=A%20simple%20moving%20average%20(SMA)%20is%20an%20arithmetic%20moving%20average,periods%20in%20the%20calculation%20average.) Compare the calculation of average range of closing prices in various time ranges to determine a bullish or bearish trend. 
    - **Bullish condition** - If the shorter time period of the SMA is greater than the longer time period of the SMA
    - **Bearish condition** - If the shorter time period of the SMA is less than the longer time period of the SMA
- [Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp) - Momementum indicator that measures the magnitude and speed of a price change to indicate whether a security is oversold or overbought. 
    - **Overbought condition** - RSI is greater than 70
    - **Oversold condition** - RSI is less than 30