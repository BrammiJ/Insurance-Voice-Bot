import dbconn1
from sqlite3 import Error
con = dbconn1.conn()
cc=con.cursor()
bu =  False;
sql = "select * FROM insurece"
try:
    cc.execute(sql)
    con.commit()
    all =  cc.fetchall()
    print(len(all))


except Error as e:
     print(e)
     con.rollback()