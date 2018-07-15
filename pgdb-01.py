#!/usr/bin/python3
# coding=utf-8

import psycopg2

db = psycopg2.connect(database='test', user='postgres', password='10b10b', host='127.0.0.1', port='5432')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("\nversion: %s" % data)

cursor.close()
db.close()