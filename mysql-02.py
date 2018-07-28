#!/usr/bin/python3
# coding=utf-8

import pymysql

# db = pymysql.connect("localhost", "root", "", "TEST")
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone();  print ("\nversion: %s" % data)

data = cursor.executemany("insert into tab1(name,age)values(%s,%s)", [("ly", "50")])
print("\ninsert returned: %s\n" % data)

cursor.execute("select * from tab1")
rows = cursor.fetchall()
print(rows)

db.commit()
cursor.close()
db.close()
