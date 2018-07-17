# -*- coding:utf-8 -*- 
"""
基本面数据接口 
Created on 2015/01/18
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""
import pandas as pd
import lxml.html
from lxml import etree
from pandas.compat import StringIO
from urllib.request import urlopen, Request
    
def get_basicdata_hexin(code):
    try:
        url = 'http://basic.10jqka.com.cn/%s/finance.html'%code
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request = Request(url,headers=headers)
        #request = Request('http://www.runoob.com/mongodb/mongodb-window-install.html')
        text = urlopen(request, timeout=10).read()

        #with open(code+".html", "wb") as f:
            #   写文件用bytes而不是str，所以要转码
        #    f.write(text)

    
        text = text.decode('GBK')
        text = text.replace('--', '')
        
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//p[@id=\"main\"]")
        sarr = [etree.tostring(node).decode('utf-8') for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr

        with open(code+"__.html", "wb") as f:
            #   写文件用bytes而不是str，所以要转码
            f.write(sarr.encode('GBK'))
        
        #df = pd.read_html(sarr)[0]
        #df.columns = ct.CASHFLOW_COLS
        #dataArr = dataArr.append(df, ignore_index=True)
        #return dataArr
        #return df
    except Exception as e:
        print(e)


get_basicdata_hexin('000917')
