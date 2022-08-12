#%%
import pandas as pd
import yahooquery as yq

#%%
def getPrice(symbol):
    try:
        price = yq.Ticker(symbol).price[symbol]['regularMarketPrice']
    except:
        price = None
    return price

#%%
funds = pd.read_json("funds.json")

#%%
funds['price'] = funds['symbol'].apply(getPrice)
funds['nav'] = funds['nav'].apply(getPrice)
funds['premium'] = 100 * (funds['price'] - funds['nav']) / funds['nav']

#%%
funds.to_csv("NAV.csv", index = False)