#%%
import pandas as pd
import yahooquery as yq
import plotly.express as px

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
funds.sort_values(by = "premium", inplace = True)

#%%
funds.to_csv("NAV.csv", index = False)

#%%
plt = px.bar(funds, x = 'symbol', y = 'premium', labels = {'premium': 'discount/premium'}, height = 800)
plt.update_layout(title_text = 'Discount or Premium to NAV', title_x = 0.5).update_yaxes(dtick = 5).show()
# %%
