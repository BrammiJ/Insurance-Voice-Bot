import dbconn
from sqlite3 import Error
class UserRegister:
    def __init__(self):
        pass
    def insert(self,fname,lname,email,mobile,password):
        con = dbconn.conn()
        cc=con.cursor()

        sql = "INSERT INTO userdata(fname,lname,email,mobile,password) values('"+fname+"','"+lname+"','"+email+"','"+mobile+"','"+password+"')"
        try:
            cc.execute(sql)
            con.commit()
            result = "inserted  Success"
        except Error as e:
            print(e)
            result = " Not inserted  Success"
            con.rollback()
        return result
    def insertpolicy(self,ques,answer):
        con = dbconn.conn()
        cc=con.cursor()

        sql = "INSERT INTO datadata(question,answer) values('"+ques+"','"+answer+"')"
        try:
            cc.execute(sql)
            con.commit()
            print('inserted success')
        except Error as e:
            print(e)
            con.rollback()
    def loginuser(self,username,password):
        con = dbconn.conn()
        cc=con.cursor()
        bu =  False;
        sql = "SELECT * from userdata WHERE email='"+username+"' AND password='"+password+"'"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()
            print(len(all))
            if len(all)>0:
                bu = True
            else:
                bu=False

        except Error as e:
            print(e)

            con.rollback()
        return  bu

