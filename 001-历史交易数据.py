import tushare

#print(tushare.__version__)

'''
df = tushare.get_stock_basics()
date = df.ix['000917']['timeToMarket']
print(date)
print(df)
'''

#获取历史复权数据
#df = tushare.get_h_data('000917',start='2018-01-01',end='2018-07-01')
#print(df)


#一次性获取当前交易所有股票的行情数据
#df = tushare.get_today_all()
#print(df)

#大盘指数行情列表-----------
#df = tushare.get_index()
#print(df)

#取近三年全部日K线数据
#df = tushare.get_hist_data('000917')
#print(df)

#取指定日期段的月历史数据
#df = tushare.get_k_data('000917',ktype='M',start='2000-01-01',end='20180701')
#print(df)

#取指定日期段的周历史数据
#df = tushare.get_k_data('000917',ktype='W',start='2000-01-01',end='20180701')
#print(df)

#取指定日期段的日历史数据
df = tushare.get_k_data('000917',ktype='D',start='2000-01-01',end='20180701')
print(df)


