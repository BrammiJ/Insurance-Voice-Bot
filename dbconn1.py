from sqlite3 import Error
import sqlite3


def conn():
    try:
        ss=  sqlite3.connect('ins.db')
        print('db created')
    except Error as e:
        print(e)
    return ss
