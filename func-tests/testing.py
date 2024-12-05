import requests
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stock = yf.Ticker("td")
levels = stock.history(period="1mo")
levels = levels.reset_index()
levels = np.array(levels["Close"])

data = stock.history(period="1d", interval="1m", prepost=True)
pre_market_data = data.between_time("8:00","9:30")
y = pre_market_data.reset_index()
y = np.array(y["Close"])

b = 0
o = 1
s = 2
p = 3
r = 4
u = 5

while True:
    if levels[o] < levels[b] and levels[b] < levels[s] and levels[s] > levels[p] and levels[p] > levels[r] and levels[r] > levels[u]:
        print(f'{levels[o]} - {levels[b]} - {levels[s]}')
    b += 1
    o += 1
    s += 1
    p += 1
    r += 1
    u += 1

x = []
a = 9
for i in y:
    x.append(a)
    a += 0.5

#-plt.plot(x,y)
# plt.show()
