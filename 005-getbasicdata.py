'''
from datetime import *

def getLastWeekDay(day=date.today):
    now=day
    if now.isoweekday()==1:
        dayStep=3
    else:
        dayStep=1
    lastWorkDay = now - timedelta(days=dayStep)
    return lastWorkDay

print(getLastWeekDay(date(2018,6,29)))
print(getLastWeekDay(date(2018,6,30)))
print(getLastWeekDay(date(2018,7,1)))
print(getLastWeekDay(date(2018,7,2)))
print(getLastWeekDay(date(2018,7,3)))
print(getLastWeekDay(date(2018,7,4)))
print(getLastWeekDay(date(2018,7,5)))
'''


from tushare.util import dateu
import datetime

#print(dateu.last_tddate())


def get_stock_basics(date=None):

    
#get_stock_basics()
get_stock_basics('2018-07-09')
