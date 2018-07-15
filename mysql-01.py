#!/usr/bin/python3

import pymysql

# db = pymysql.connect("localhost", "root", "", "TEST")
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='TEST', charset='utf8')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("\nDatabase version : %s " % data)

cursor.close()
db.close()
