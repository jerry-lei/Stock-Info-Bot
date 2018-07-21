import requests
import json
from collections import OrderedDict

#returns dictionary of all symbols of query (no particular order)
def findSymbols(query):
    url = "http://autoc.finance.yahoo.com/autoc?query=%s&region=EU&lang=en-GB" % query
    response = requests.get(url)
    if(not response.ok):
        return
    results = json.loads(response.content)
    results = results.get("ResultSet").get("Result")

    return_dict = OrderedDict()

    for result in results:
        return_dict[result.get("symbol")] = result.get("name")

    return return_dict

def getSymbol(query):
    symbols = findSymbols(query)
    if len(symbols) > 0:
        return (symbols.items()[0])[0]
    else:
        return None


if __name__ == "__main__":
    print findSymbols("ED")
    print getSymbol("ED")
