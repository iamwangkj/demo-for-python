import tushare as ts
from datetime import date, datetime

TOKEN = '1e5f37fe89fe4c360b7980be64e5211167156c2e1f4913c0a91e4e78'
ts.set_token(TOKEN)
pro = ts.pro_api()

def getRealTime():
  df = ts.get_realtime_quotes()
  # df[['code','name','price','bid','ask','volume','amount','time']]
  print(df)


# 获取当天所有数据，需要在今天的收盘收才能获取到数据
def getTodayAll():
  today = datetime.now().strftime('%Y%m%d')
  df = pro.daily(trade_date=today)
  print(df)
  

getRealTime()