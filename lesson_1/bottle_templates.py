# coding: utf-8
from pymongo import MongoClient
from bottle import get, post, run, template, request


@get('/')
def index():
    connection = MongoClient('localhost')
    db = connection.test

    name = db.names
    item = name.find_one()

    return template('hello_world', username = item['name'], things = item['cosas'])


@post('/favourite_thing')
def favourite_thing():
    thing = request.forms.get('thing')

    if thing:
        return template('selected_thing', thing = thing)
    else:
        return 'No thing selected!'


run(reloader = True)
