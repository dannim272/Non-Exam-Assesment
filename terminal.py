import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import requests, time, sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

hours = 0
minutes = 0
g = 0
l = 0
# gainers = []
# losers = []

def main():
    # vars
    # global gainers
    # global losers 
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
    tckr.grid(row=(4), column=1)
    tckr1 = tk.Label(root)
    tckr1.grid(row=(5), column=1)
    tckr2 = tk.Label(root)
    tckr2.grid(row=(6), column=1)
    tckr3 = tk.Label(root)
    tckr3.grid(row=(7), column=1)
    tckr4 = tk.Label(root)
    tckr4.grid(row=(8), column=1)

    # tckr button
    tckrButton = False
    tckr_button = tk.Button(root, text='Graph', command=lambda: plot(tckrButton, tckr2Button))
    tckr_button.grid(row=4, column=0)
    tckr2Button = False
    tckr2_button = tk.Button(root, text='Graph', command=lambda: plot(tckrButton, tckr2Button))
    tckr2_button.grid(row=5, column=0)

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
        if (hours < 14) or (hours == 14):
            response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/extended-trading?markettype=pre&assetclass=Stocks&time=0')
            price = response.json()['data']['tradeDetailTabel']['rows'][0]['price']
            price_label.config(text=price)
            price_label.after(200, ticker_price)

        # real-time
        if (hours > 15 and hours < 22):
            response = requests.get(f'https://api.stockanalysis.com/api/quotes/s/{stock}')
            price = response.json()['data']['p']
            price_label.config(text=price)

        # after hours
        if (hours > 21) or (hours == 21 and minutes > 0):
            response = requests.get(f'https://api.nasdaq.com/api/quote/{stock}/extended-trading?markettype=post&assetclass=stocks&time=0')
            price = response.json()['data']['tradeDetailTabel']['rows'][0]['price']
            price_label.config(text=price)
            price_label.after(200, ticker_price)

    def plot(tckrButton, tckr2Button):
        if clicked.get() == "$ Gainers":
            if tckrButton == True:
                stock = yf.Ticker(gainers[0])
            if tckr2Button == True:
                stock = yf.Ticker(gainers[2])
        if clicked.get() == "$ Losers":
            if tckrButton == True:
                stock = yf.Ticker(losers[0])
            if tckr2Button == True:
                stock = yf.Ticker(losers[2])
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

        sp_fig = Figure(figsize=(5, 4), dpi=100)
        ax = sp_fig.add_subplot(111)
        ax.plot(x, y)
        canvas = FigureCanvasTkAgg(sp_fig, root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9,column=2)


    def submit(tckr,tckr1,tckr2,tckr3,tckr4):
        screener()
        root.after(50, lambda: tckr.config(text=''))
        root.after(50, lambda: tckr1.config(text=''))
        root.after(50, lambda: tckr2.config(text=''))
        root.after(50, lambda: tckr3.config(text=''))
        root.after(50, lambda: tckr4.config(text=''))
        if clicked.get() == "$ Gainers":
            root.after(50, lambda: tckr.config(text=f'{gainers[0]}: ${gainers[1]}'))
            root.after(50, lambda: tckr1.config(text=f'{gainers[2]}: ${gainers[3]}'))
            root.after(50, lambda: tckr2.config(text=f'{gainers[4]}: ${gainers[5]}'))
            root.after(50, lambda: tckr3.config(text=f'{gainers[6]}: ${gainers[7]}'))
            root.after(50, lambda: tckr4.config(text=f'{gainers[8]}: ${gainers[9]}'))
        if clicked.get() == "$ Losers":
            root.after(50, lambda: tckr.config(text=f'{losers[0]}: ${losers[1]}'))
            root.after(50, lambda: tckr1.config(text=f'{losers[2]}: ${losers[3]}'))
            root.after(50, lambda: tckr2.config(text=f'{losers[4]}: ${losers[5]}'))
            root.after(50, lambda: tckr3.config(text=f'{losers[6]}: ${losers[7]}'))
            root.after(50, lambda: tckr4.config(text=f'{losers[8]}: ${losers[9]}'))

    def screener():
        global g
        global l
        response = requests.get('https://api.stockanalysis.com/api/screener/s/bd/premarketChangePercent+premarketPrice+relativeVolume+daysGap.json')
        stocks = response.json()['data']['data']
        for stock in stocks:
            try:
                if (stocks[stock]['daysGap'] > 1) and (stocks[stock]['premarketPrice'] > 10) and (stocks[stock]['relativeVolume'] > 250):
                    if stock in gainers:
                        pass
                    else:
                        gainers.append(stock)
                        gainers.append(stocks[stock]['premarketPrice'])
                        g += 1
                    if g > 4:
                        break
                if (stocks[stock]['daysGap'] < -1) and (stocks[stock]['premarketPrice'] > 10) and (stocks[stock]['relativeVolume'] > 250):
                    if stock in losers:
                        pass
                    else:
                        losers.append(stock)
                        losers.append(stocks[stock]['premarketPrice'])
                        l += 1
                    if l > 4:
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
    button = tk.Button(root, text='Submit', command=lambda: submit(tckr,tckr1,tckr2,tckr3,tckr4)).grid(row=3, column=1)

    tk.mainloop()

main()
