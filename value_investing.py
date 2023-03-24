#%%

"""Tests to see if i can get data imported and into dataframe"""
import pandas as pd
import numpy as np 
import yfinance as yf 
from yahoofinancials import YahooFinancials



yahoo_financials = YahooFinancials('AAPL')
data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
                                                  end_date='2019-12-31', 
                                                  time_interval='weekly')
aapl_df = pd.DataFrame(data['AAPL']['prices'])
aapl_df = aapl_df.drop('date', axis=1).set_index('formatted_date')
aapl_df.head()


yahoo_financials = YahooFinancials('AAPL')
data = yahoo_financials.get_financial_stmts('annual', 'income')
# print(data)

# df = pd.DataFrame(data['incomeStatementHistory']['AAPL'])
# df
dict_list = data['incomeStatementHistory']['AAPL']
df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
df = df.rename_axis('name').reset_index()
# df.insert(0, 'ticker', 'AAPL')
df

print(data)
# %%
"""Try to get qurterly reports into dataframe"""
import pandas as pd
import numpy as np 
import yfinance as yf 
from yahoofinancials import YahooFinancials
