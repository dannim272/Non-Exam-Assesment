import requests
import yfinance as yf

tck = input("Enter Ticker you would like to search up: ")
stock = yf.Ticker(tck)
data = stock.history(period="6mo")
price = data['Close']
volume = data['Volume']

print(f'{tck} price is {price[0]} and volume is {volume[0]}')
