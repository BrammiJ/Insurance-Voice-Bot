import dbconn
from sqlite3 import Error
import win32com.client
from collections import Counter
import operator
import itertools
class Alldata:
    def __init__(self):
        pass
    def all(self):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT * FROM userdata"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()
            for a in all:
                speaker = win32com.client.Dispatch("SAPI.SpVoice")

                speaker.Speak(a[1]+a[2])
            print(all)
        except Error as e:
            print(e)
            con.rollback()
    def allreturn(self):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT * FROM userdata"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()


        except Error as e:
            print(e)
            con.rollback()
        return  all
    def alldatareturn(self):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT * FROM datadata"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()


        except Error as e:
            print(e)
            con.rollback()
        return  all
    def allpolicyreturn(self):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT num,policy,keys FROM insurence"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()


        except Error as e:
            print(e)
            con.rollback()
        return  all
    def insertpolicy(self,number,policy,keys):
        con = dbconn.conn()
        cc = con.cursor()
        sql = "INSERT INTO insurence(num,policy,keys)values('"+number+"','"+policy+"','"+keys+"')"
        try:
            cc.execute(sql)
            con.commit()
            print ('inserted')


        except Error as e:
            print(e)
            con.rollback()
        return all
    def updatepolicy(self,a,b):
        self.data = False
        con = dbconn.conn()
        cc = con.cursor()
        sql = "UPDATE insurence SET policy ='"+b+"' WHERE num = '" + a + "'"
        try:
            cc.execute(sql)
            con.commit()

            self.data = True

        except Error as e:
            self.data = False

            con.rollback()
        return self.data
    def deletepolicy(self,a):
        self.data = False
        con = dbconn.conn()
        cc = con.cursor()
        sql = "DELETE FROM insurence WHERE num = '"+a+"'"
        try:
            cc.execute(sql)
            con.commit()

            self.data=True

        except Error as e:
            self.data =False

            con.rollback()
        return  self.data
    def singlepolicyreturn(self,quest):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT num,policy,keys FROM insurence WHERE num='"+quest+"' or policy='"+quest+"'or keys='"+quest+"'"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()


        except Error as e:
            print(e)
            con.rollback()
        return  all
    def singledatareturn(self,quest):
        con = dbconn.conn()
        cc=con.cursor()
        sql = "SELECT answer FROM datadata WHERE question='"+quest+"'"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()
            for x in all:
                all1 =x[0]


        except Error as e:
            print(e)
            con.rollback()
        return  all1
    def singlelikedatareturn(self,a):
        con = dbconn.conn()
        cc=con.cursor()
        all1 = "no value"

        sql = "SELECT answer FROM datadata WHERE question LIKE '%"+a+"%'"
        try:
            cc.execute(sql)
            con.commit()
            all =  cc.fetchall()
            for x in all:
                all1=  x[0]


        except Error as e:
            print(e)
            con.rollback()
        return all1
    def suggestdata(self,a):
        con = dbconn.conn()
        cc=con.cursor()
        list = a

        all = []
        aa = []
        for x in list:
            sql = "SELECT num FROM insurence WHERE keys LIKE'%" + str(x) + "%'"
            try:
                cc.execute(sql)
                con.commit()
                all = cc.fetchall()

                for i in all:

                    aa.append(i[0])
            except Error as e:
                print(e)
        try:

            c = Counter(aa)
            print(c)

            d = {}
            d = {x: aa.count(x) for x in aa}
            print(d)
            alls = []
            groups = itertools.groupby(d.values())

            # Consume one group if there is one, then see if there's another.
            next(groups, None)
            if next(groups, None) is None:
                # All values are equal.
                print("all values equal")
                for i,j in d.items():
                    sql = "SELECT policy FROM insurence WHERE num ='" + str(i) + "'"

                    try:
                        cc.execute(sql)
                        con.commit()
                        new = cc.fetchall()
                        for i in new:
                            alls.append(i)
                    except Error as e:
                        print(e)

            else:
                # Unequal values detected.
                print("all values not equal")
                data = max(d.items(), key=operator.itemgetter(1))[0]
                print(data)

                sql = "SELECT policy FROM insurence WHERE num ='" + str(data) + "'"

                try:
                    cc.execute(sql)
                    con.commit()
                    new = cc.fetchall()
                    for i  in new:

                        alls.append(i)
                except Error as e:
                    print(e)
        except Error as e:
            print(e)
        return alls

a=  Alldata()
data = ["above45","married"]
print(a.suggestdata(data))
