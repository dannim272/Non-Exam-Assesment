import requests
import yfinance as yf
import numpy as np

stock = yf.Ticker("pcg")
data = stock.history(period="1d", interval="1m", prepost=True)
pre_market_data = data.between_time("9:00","9:30")
x = [540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570]
x = np.array(x)
y = pre_market_data.reset_index()
y = y["Close"]

n = np.size(x)
sumX = np.sum(x)
sumY = np.sum(y)
ssq = np.sum(x**2)
multXY = np.sum(x*y)
ssm = sumX**2

a = (sumY(ssq)-sumX(multXY))/(n(ssq)-ssm)
print(a)
