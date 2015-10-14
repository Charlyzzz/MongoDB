# coding: utf-8
from pymongo import MongoClient

from bottle import get, route, post, run, template, request, response, redirect


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

    if not thing:
        thing = "No fruit selected"

    response.set_cookie('thing', thing)
    redirect('/favourite_cookie_thing')


@route('/favourite_cookie_thing')
def show_thing():
    cookie = request.get_cookie('thing')

    return template('selected_thing', thing = cookie)


run(reloader = True)
