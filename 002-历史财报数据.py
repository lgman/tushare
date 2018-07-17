import tushare

#print(tushare.__version__)

df = tushare.get_report_data(2017,4)
df.to_excel('e:/data/201704.xlsx')
