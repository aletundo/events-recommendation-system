#!/usr/bin/env python
# coding=utf-8
from flask import Flask, g, current_app
from flask_pymongo import PyMongo
from utils import sqlite as sqlite_utils
from utils import mongodb as mongodb_utils
from bson.json_util import dumps
import json
from random import randint

app = Flask('recommendation-system-engine', instance_relative_config=True)
app.config.from_object('config')
mongo = PyMongo(app)

@app.route('/users')
def list_users():
    collection = mongodb_utils.get_users_collection(mongo)
    users = dumps(collection.find())
    return users

@app.route('/events')
def list_events():
    collection = mongodb_utils.get_events_collection(mongo)
    events = dumps(collection.find())
    return events

@app.before_first_request
def init_data():
    sqlite_utils.init_db()
    mongodb_utils.init_users_collection(mongo)
    mongodb_utils.init_events_collection(mongo)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
