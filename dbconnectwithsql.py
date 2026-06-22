
"""
Connection MySQL With Python
pip install mysql.connector
pip install mysql.connector.python

"""

import mysql.connector

# Building a connection with mysql server
conn = mysql.connector.connect(
    host = "127.0.0.1" ,
    port = 3306,
    user = 'root',
    password = '12345',
    database = 'school')


# Creating a cursor to execute queries
cur = conn.cursor()

'''
sql = "CREATE DATABASE school"
cur.execute(sql)

sql = 'USE school'
cur.execute(sql)

sql = 'CREATE TABLE student(sid INT, sname TEXT, sadd TEXT, scource TEXT)'
cur.execute(sql)

sql = 'INSERT INTO student VALUE(101, "Raman", "Noida", "Data Science")'
cur.execute(sql)
conn.commit()
'''


sid =input("Enter student ID:")
sname = input("Enter student name:")
sadd = input("Enter student address:")
scource = input("Enter student course:")

sql = f'INSERT INTO student VALUES({sid}, "{sname}", "{sadd}", "{scource}")'
cur.execute(sql)
conn.commit()


sid =input("Enter student ID:")
sname = input("Enter student name:")
sadd = input("Enter student address:")
scource = input("Enter student course:")

sql = f'INSERT INTO student VALUE(%s, %s, %s, %s)'
data = (sid, sname, sadd, scource)
cur.execute(sql, data)
conn.commit()
print("Data stored successfully")


sql = 'SELECT * FROM student'
cur.execute(sql)
data = cur.fetchall()
for stu in data:
    print("\nStudent ID :", stu[0])
    print("Student Name :", stu[1])
    print("Student Address :", stu[2])
    print("Student Course :", stu[3])



