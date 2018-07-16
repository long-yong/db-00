#!/usr/bin/python3
# coding=utf-8

import pymongo

mongo_client = pymongo.MongoClient('localhost', 27017)
db = mongo_client['test']
dbcoll = db['tab1']
print("—"*100)

'''
for rcd in dbcoll.find():
    print(rcd)
'''

# insert
rcd = {'name': 'Tom', 'age': 18, 'sex': '男', 'hobbies': ['吃饭', '睡觉', '打豆豆']}
id = dbcoll.insert_one(rcd)
print(id)
rcd = {'name': 'Alice', 'age': 19, 'sex': '女', 'hobbies': ['读书', '跑步', '弹吉他']}
id = dbcoll.insert_one(rcd)
print(id)

# query
print("—"*100)
for rcd in dbcoll.find():
    print(rcd)

# update
print("—"*100)
dbcoll.update_many({'name': 'Tom'}, {'$set': {'hobbies': ['不吃饭', '不睡觉', '成天打豆豆']}})
for rcd in dbcoll.find():
    print(rcd)

# delete
print("—"*100)
dbcoll.drop()
for rcd in dbcoll.find():
    print(rcd)


