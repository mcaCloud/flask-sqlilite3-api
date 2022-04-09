import sqlite3

def get_connect():
    try:
        con = sqlite3.connect('myapi.db')
    except Exception as e:
        print(e)
    else:
        return con
