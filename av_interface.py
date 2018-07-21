## Interface for Alpha Vantage:
### List of functions:
### -- TIME_SERIES_INTRADAY
### --

import config
import requests
import json

# params = {
#     "symbol": "F",
#     "interval": 1,
#     ...
# }

class av_interface(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def returnJsonContent(self, url):
        response = requests.get(url)
        if(response.ok):
            return json.loads(response.content)

    # -- TIME SERIES INTRADAY --
    #   This API returns intraday time series (timestamp, open, high, low, close, volume) of the equity specified, updated realtime.
    #requires:
    ## symbol: "F" -- symbol is case insensitive
    ## interval (1,5,15,30,60 mins): 1,5,15,30,60
    ## output size(compact--100 pts/full): "compact", "full"
    #default interval = 1min
    def intraday(self, parameters):
        symbol = parameters.get("symbol")
        if symbol == None:
            return
        interval = str(parameters.get("interval", 1)) + "min"
        outputsize = parameters.get("outputsize", "compact")
        query_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
        query_url_params = "&symbol=%s&interval=%s&outputsize=%s&apikey=%s" % (symbol, interval, outputsize, self.api_key)

        return self.returnJsonContent(query_url_base + query_url_params)

    # -- TIME SERIES DAILY --
    #   This API returns daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering up to 20 years of historical data.
    #requires:
    ## symbol, outputsize
    def daily(self, parameters):
        symbol = parameters.get("symbol")
        if symbol == None:
            return
        outputsize = parameters.get("outputsize", "compact")
        query_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
        query_url_params = "&symbol=%s&outputsize=%s&apikey=%s" % (symbol, outputsize, self.api_key)
        print self.returnJsonContent(query_url_base + query_url_params)

    # -- TIME SERIES WEEKLY --
    #   This API returns weekly time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly volume) of the global equity specified, covering up to 20 years of historical data.
    #requires:
    ## symbol
    def weekly(self, parameters):
        symbol = parameters.get("symbol")
        if symbol == None:
            return
        query_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY"
        query_url_params = "&symbol=%s&apikey=%s" % (symbol, , self.api_key)

        print self.returnJsonContent(query_url_base + query_url_params)

    # -- TIME SERIES MONTHLY --
    #   This API returns weekly time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly volume) of the global equity specified, covering up to 20 years of historical data.
    #requires:
    ## symbol
    def monthly(self, parameters):
        symbol = parameters.get("symbol")
        if symbol == None:
            return
        query_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY"
        query_url_params = "&symbol=%s&apikey=%s" % (symbol, , self.api_key)

        print self.returnJsonContent(query_url_base + query_url_params)



if __name__ == '__main__':
    av = av_interface(config.ALPHA_VANTAGE_API_KEY)

    parameters = {
        "symbol": "ED",
        "interval": 60,
        "outputsize": "compact"
    }

    av.daily(parameters)
