import requests

response = requests.get('https://api.nasdaq.com/api/quote/{stock}/extended-trading?markettype=pre&assetclass=Stocks&time=0')
print(response.status_code)
