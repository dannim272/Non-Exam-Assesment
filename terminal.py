import tkinter as tk
import requests
import sys
import time
# import yfinance
# import datetime
# from tkhtmlview import HTMLLabel
from login import log

# log()

root = tk.Tk()
root.title("Grass Terminal")

sys.setrecursionlimit(1500)


# clock
def timing():
    current_time = time.strftime("%H : %M : %S")
    hours = int(time.strftime("%H"))
    if hours > 21 or hours < 9:
        root.after(50, lambda: root.destroy())
    clock.config(text=current_time)
    clock.after(200, timing)


clock = tk.Label(root)
clock.grid(row=0, column=0)
timing()


def sp500_p():
    response_sp = requests.get('https://api.nasdaq.com/api/quote/watchlist?symbol=spx%7cindex&symbol=aapl%7cstocks&symbol=sp%7cfutures&symbol=indu%7cindex&symbol=tsla%7cstocks&type=Rv')
    sp500 = response_sp.json()['data']['rows'][0]['lastSale']
    sp500_label.config(text=f'S&P 500: ${sp500}')
    sp500_label.after(100, sp500_p)


sp500_label = tk.Label(root)
sp500_label.grid(row=0, column=1, columnspan=2)
sp500_p()

# ticker search
stock_var = tk.StringVar()


def ticker_price():
    stock = stock_var.get()
    response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/realtime-trades?&limit=5')
    price = response.json()['data']['rows'][0]['nlsPrice']
    price_label.config(text=price)
    price_label.after(200, ticker_price)


price_label = tk.Label(root)
price_label.grid(row=1, column=1)

stockSearch_entry = tk.Entry(root, textvariable=stock_var).grid(row=1, column=0)
root.bind('<Return>', ticker_price)


tk.mainloop()
