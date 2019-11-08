import pymysql
 
# 打开数据库连接
db = pymysql.connect('qdm142902383.my3w.com', 'qdm142902383', 'wq29635973', 'qdm142902383_db', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute('SELECT * FROM tushare_1400')
# 获取数据.
data1400 = cursor.fetchall()

cursor.execute('SELECT * FROM tushare_1430')
data1430 = cursor.fetchall()

print(data1430)

# 初始化容器
riseTuple = ()
for item1430 in data1430:
  for item1400 in data1400:
    # 确保同一股
    if item1430[1] == item1400[1] and item1400[4] != 0:
      # 在14点30时上涨多少
      changepercent = (item1430[4] - item1400[4]) / item1400[4]
      # 筛选出在14点30时上涨1%的股
      if changepercent > 0.01:
        riseTuple = riseTuple + item1430
      break

print(riseTuple)

# 关闭数据库连接
db.close()