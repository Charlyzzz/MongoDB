# coding: utf-8
# coding: utf-8
from pymongo import MongoClient
from bottle import route, run


@route('/')
def index():
    connection = MongoClient('localhost')
    db = connection.test

    name = db.names
    item = name.find_one()

    return "<b> Hello %s! </b>" % item['name']


run(reloader = True)