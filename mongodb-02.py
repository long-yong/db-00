#!/usr/bin/python3
# coding=utf-8

import pymongo

mongo_client = pymongo.MongoClient('localhost', 27017)
db = mongo_client['test']
dbcoll = db['tab2']
print("—"*100)

# delete
dbcoll.drop()

# insert
rcd = {'name': 'Tom', 'age': 18, 'sex': '男', 'hobbies': ['吃饭', '睡觉', '打豆豆']}
print(dbcoll.insert_one(rcd))
rcd = {'name': 'Alice', 'age': 19, 'sex': '女', 'hobbies': ['读书', '跑步', '弹吉他']}
print(dbcoll.insert_one(rcd))

# query
print("—"*100)
for rcd in dbcoll.find():
    print(rcd)

# update
dbcoll.update_many({'name': 'Tom'}, {'$set': {'hobbies': ['不吃饭', '不睡觉', '成天打豆豆']}})

# query
print("—"*100)
for rcd in dbcoll.find():
    print(rcd)





