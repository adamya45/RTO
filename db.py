import mysql.connector as m
from mysql.connector import Error

def connect_db():
    try:
        conn = m.connect(user='root',password='root',host='localhost',database='rto_management')
        # print('connected to DB successfully!')
        return conn
    
    except Error as e:
            print(f"Error connecting to DB: {e}")
   