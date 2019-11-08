from sqlalchemy import create_engine
import tushare as ts

df = ts.get_today_all()
# df = ts.get_realtime_quotes('000002')
engine = create_engine('mysql+pymysql://qdm142902383:wq29635973@qdm142902383.my3w.com/qdm142902383_db?charset=utf8')

print(df)
#存入数据库
# if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
df.to_sql('tushare_1400', engine, if_exists='replace')

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')