import pandas as pd
from tushare.stock import cons as ct
from urllib.request import urlopen, Request
import tushare
import urllib

request = urllib.request.Request(ct.ALL_STOCK_BASICS_FILE%('201807/', '20180704'))


#print(request)
print(request.full_url)
#print(request.data)


#url = ct.ALL_STOCK_BASICS_FILE%('201807/', '20180704')
text = urllib.request.urlopen(request, timeout=10).read()

#text = text.decode('GBK')
#text = text.replace('--', '')
#df = pd.read_csv(StringIO(text), dtype={'code':'object'})
#df = df.set_index('code')

#print(df)


#print(tushare.get_stock_basics())

