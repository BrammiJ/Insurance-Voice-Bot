from sqlite3 import Error
import  dbconn
con =  dbconn.conn()
cc=  con.cursor()
def usertable():
    sql = "CREATE TABLE userdata (id INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT,lname TEXT,email TEXT,mobile TEXT,password TEXT)"
    try:
        cc.execute(sql)
        con.commit()
        print('table created');
    except Error as e:
        print(e)
        con.rollback()
def datatable():
    sql = "CREATE TABLE datadata (id INTEGER PRIMARY KEY AUTOINCREMENT,question TEXT,answer TEXT)"
    try:
        cc.execute(sql)
        con.commit()
        print('table created');
    except Error as e:
        print(e)
        con.rollback()
def table():

    sql = "CREATE TABLE insurence (id INTEGER PRIMARY KEY  AUTOINCREMENT,num INTEGER (9),policy TEXT,keys TEXT)"
    try:
        con.execute(sql)
        con.commit()
        print("table created")
    except Error as e:
        print(e)

datatable()
usertable()
table()