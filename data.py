import requests

response = requests.get('https://api.stockanalysis.com/api/screener/s/bd/premarketChangePercent+premarketPrice+relativeVolume+daysGap.json')
print(response.status_code)
stocks = response.json()['data']['data']

a = 0
for i in stocks:
    try:
        if (stocks[i]['daysGap'] < -1) and (stocks[i]['premarketPrice'] > 10) and (stocks[i]['relativeVolume'] > 250):
            a += 1
            print(i,': gap - ',stocks[i]['daysGap'],',price - ',stocks[i]['premarketPrice'],' and rV - ',stocks[i]['relativeVolume'] > 250)
            print(a)
    except KeyError:
        pass
