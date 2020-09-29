import pandas_datareader.data as web
import pandas as pd
import datetime as dt
#import matplotlib.pyplot as plt
from pandas_datareader import wb
import quandl

##GETTING DATA FROM WEB#####
tickers = "BRJ8"
startDate = '2018-1-1'
endDate = dt.datetime.today()
mgWeb = web.DataReader(tickers, 'moex', startDate, endDate)
mgWeb.to_excel('recData/BRENT_FUTURE_from_web.xlsx')

####GETTING DATA FROM MICROSOFT####
tickers = ['^SPX']
dataSource = 'stooq'
startDate = '2018-1-1'
endDate = dt.datetime.today()
gWeb = web.DataReader(tickers, dataSource, startDate, endDate)
gWeb.to_excel('recData/SP500_from_web.xlsx')

worldBank = wb.download(indicator='NY.GDP.MKTP.CD', country=[
                        'RU'], start=2005, end=2008)
worldBank.to_excel('recData/WB_from_web.xlsx')

keyIndicies = quandl.get('BANKRUSSIA/KEYECIND')
keyIndicies.to_excel('recData/CB_from_web.xlsx')

mgWeb = mgWeb[['VALUE', 'OPEN', 'LOW']]
mgWeb = mgWeb.assign(LowInUSD=mgWeb['LOW']/57)
mgWeb = mgWeb.assign(Numbers=mgWeb['VALUE']/mgWeb['LOW'])
print(mgWeb)
