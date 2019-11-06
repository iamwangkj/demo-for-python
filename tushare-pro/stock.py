import tushare as ts
from datetime import date, datetime

TOKEN = '1e5f37fe89fe4c360b7980be64e5211167156c2e1f4913c0a91e4e78'
ts.set_token(TOKEN)
pro = ts.pro_api()

def getTodayString():
  return datetime.now().strftime('%Y%m%d')

def getStockCalendar():
  today = getTodayString()
  df = pro.trade_cal(exchange='', start_date=today, end_date=today)
  print(df)
  # print(df.is_open)


# 获取当天所有数据，更新时间：交易日每天15点～16点之间，需要在今天的收盘收才能获取到数据
def getTodayAll():
  today = getTodayString()
  df = pro.daily(trade_date=today)
  # df[['code','name','price','bid','ask','volume','amount','time']]
  print(df)
  

# getStockCalendar()
getStockCalendar()
