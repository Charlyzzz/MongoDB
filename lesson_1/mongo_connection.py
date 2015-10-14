# coding: utf-8
from pymongo import MongoClient

connection = MongoClient('localhost')
db = connection.test

name = db.names
item = name.find_one()

print item['name']
