data_stream = [{'data': {'open': 35,'close':40}}, {}, {}, {'data': {'open': 12,'close':13}},{'data': {'open': 35,'close':40}},{'data': {'open': 35,'close':40}},{'data': {'open': 35,'close':40}},{},{}]

for market_day in data_stream:

    if 'data' in market_day:
        print(market_day['data']['open'])


for market_day in data_stream:
    price = market_day.get('data', 0)
    print(price)