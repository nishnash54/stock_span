from env import val
import requests
import json

def return_data(sym):

    parameters = {'function': 'TIME_SERIES_INTRADAY', 'interval': '1min', 'symbol': sym, 'apikey': val.apikey}
    r = requests.get(url = val.link, params = parameters)

    # print r.content
    data = json.loads(r.content)
    # print data
    # print data['Time Series (1min)']["2018-03-15 14:50:00"]

    plot_data = {}
    for each in data['Time Series (1min)']:
        # print data['Time Series (1min)'][each]
        plot_data[each] = float(data['Time Series (1min)'][each]['1. open'])

    print plot_data
    x = plot_data.keys()
    y = plot_data.values()
    print x
    print y

return_data('MSFT')
