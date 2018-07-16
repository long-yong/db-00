#!/usr/bin/python3
# coding=utf-8

import pymongo

mongo_client = pymongo.MongoClient('localhost', 27017)
db = mongo_client['test']
dbcoll = db['tab1']

print("\ntab1:\n")
for rcd in dbcoll.find():
    print(rcd)
