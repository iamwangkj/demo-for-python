from sqlalchemy import create_engine
import tushare as ts
import pymysql

def setDataToDB(tableName):
  df = ts.get_today_all()
  engine = create_engine('mysql+pymysql://qdm142902383:password_here@qdm142902383.my3w.com/qdm142902383_db?charset=utf8')
  #存入数据库
  # if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
  df.to_sql(tableName, engine, if_exists='replace')
  #追加数据到现有表
  #df.to_sql('tick_data',engine,if_exists='append')

def getDataFromDB():
  # 打开数据库连接
  db = pymysql.connect('qdm142902383.my3w.com', 'qdm142902383', 'password_here', 'qdm142902383_db', charset='utf8')
  # 使用 cursor() 方法创建一个游标对象 cursor
  cursor = db.cursor()
  # 使用 execute()  方法执行 SQL 查询 
  cursor.execute('SELECT * FROM tushare_1400')
  # 获取数据.
  data1400 = cursor.fetchall()
  cursor.execute('SELECT * FROM tushare_1430')
  data1430 = cursor.fetchall()
  itemRiseTuple = ()
  for item1430 in data1430:
    for item1400 in data1400:
      # 确保同一股
      if item1430[1] == item1400[1]:
        # 在14点30时上涨多少
        changepercent = (item1430[4] - item1400[4]) / item1400[4]
        # 筛选出在14点30时上涨1%的股
        if changepercent > 0.01:
          itemRiseTuple = itemRiseTuple + item1430
        break
  print(type(data1430[0]))
  print(data1430[0])
  # 关闭数据库连接
  db.close()