import tkinter as tk
import requests
import sys
import time
# import yfinance
# import datetime
# from tkhtmlview import HTMLLabel

screened = False
# hours and minutes var
hours = 0
minutes = 0
g = 0
l = 0

def main():
    # vars
    global g
    global l
    global hours
    global minutes
    global screened
    global tckr

    root = tk.Tk()
    root.title("Grass Terminal")
    sys.setrecursionlimit(1500)

    # tckr labels
    tckr = tk.Label(root)


    def timing():
        global hours
        global minutes
        current_time = time.strftime("%H : %M : %S")
        hours = int(time.strftime("%H"))
        minutes = int(time.strftime("%M"))
        clock.config(text=current_time)
        clock.after(200, timing)

    def ticker_price(event):
        stock = stock_var.get()

        # pre-market
        if (hours < 14):
            response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/extended-trading?markettype=pre&assetclass=Stocks&time=0')
            print(response.status_code)
            price = response.json()['data']['tradeDetailTabel']['rows'][0]['price']
            price_label.config(text=price)
            price_label.after(200, ticker_price)

        # real-time
        if (hours > 15 and hours < 22):
            response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/realtime-trades?&limit=5')
            print(response.status_code)
            price = response.json()['data']['rows'][0]['nlsPrice']
            price_label.config(text=price)
            price_label.after(200, ticker_price)

        # after hours
        if (hours > 21) or (hours == 21 and minutes > 0):
            response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/extended-trading?markettype=post&assetclass=stocks&time=0')
            print(response.status_code)
            price = response.json()['data']['tradeDetailTabel']['rows'][0]['price']
            price_label.config(text=price)
            price_label.after(200, ticker_price)

    def submit(tckr):
        if not screened:
            screener()
        if clicked.get() == "$ Gainers":
            for i in range(0,g):
                if (g - i) > 0:
                    root.after(50, lambda: tckr.config(text=gainers[i]))
                    tckr.grid(row=(i+4), column=0)
        if clicked.get() == "$ Losers":
            for i in range(0,l):
                if (l - i) > 0:
                    root.after(50, lambda: tckr.config(text=losers[i]))
                    tckr.grid(row=(i+4), column=0)

    def screener():
        global g
        global l
        response = requests.get('https://api.stockanalysis.com/api/screener/s/bd/premarketChangePercent+premarketPrice+relativeVolume+daysGap.json')
        stocks = response.json()['data']['data']
        for stock in stocks:
            try:
                if (stocks[stock]['daysGap'] > 1) and (stocks[stock]['premarketPrice'] > 10) and (stocks[stock]['relativeVolume'] > 250):
                    gainers.append(stock)
                    g += 1
                    if g == 7:
                        break
                if (stocks[stock]['daysGap'] < -1) and (stocks[stock]['premarketPrice'] > 10) and (stocks[stock]['relativeVolume'] > 250):
                    losers.append(stock)
                    l += 1
                    if l == 7:
                        break
            except KeyError:
                pass

    # clock
    clock = tk.Label(root)
    clock.grid(row=0, column=0)
    timing()

    # ticker search
    stock_var = tk.StringVar()

    price_label = tk.Label(root)
    price_label.grid(row=1, column=1)

    stockSearch_entry = tk.Entry(root, textvariable=stock_var).grid(row=1, column=0)
    root.bind('<Return>', ticker_price)

    gainers = []
    losers = []
    screener_options = [
           "$ Gainers",
           "$ Losers"
           ]
    clicked = tk.StringVar()
    clicked.set("$ Gainers")
    drop = tk.OptionMenu(root, clicked, *screener_options).grid(row=3, column=0)

    button = tk.Button(root, text='Submit', command=lambda: submit(tckr)).grid(row=3, column=1)

    tk.mainloop()

main()
