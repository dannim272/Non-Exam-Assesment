import requests
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

ticker = input("Enter ticker: ")
response = requests.get(f'https://api.nasdaq.com/api/quote/{ticker}/extended-trading?markettype=pre&assetclass=stocks&time=0')
prices = response.json()['data']['tradeDetailTable']['rows']

data = []
i = 0
for price in prices:
    price = prices[i]['price']
    price = float(price[1:-1])
    data.append(price)
    time = prices[i]['time']
    data.append(time)
    i += 1
print(data)

