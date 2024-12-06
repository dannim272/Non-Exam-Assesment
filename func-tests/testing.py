import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stock = yf.Ticker("^gspc")
levels = stock.history(period="1mo")
levels = levels.reset_index()
levels = np.array(levels["Close"])

data = stock.history(period="1d", interval="1m", prepost=True)
pre_market_data = data.between_time("8:00","9:30")
y = pre_market_data.reset_index()
y = np.array(y["Close"])

x = []
a = 9
for i in y:
    x.append(a)
    a += 0.5

plt.plot(x,y)
plt.show()
