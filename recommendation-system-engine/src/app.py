#!/usr/bin/env python
# coding=utf-8
from flask import Flask, g
from flask_pymongo import PyMongo
import sqlite3

app = Flask('recommendation-system-engine', instance_relative_config=True)
# Load the default configuration
app.config.from_object('config')
mongo = PyMongo(app)

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = make_dicts
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():
    c = get_db().cursor()
    # Create table users
    c.execute('''CREATE TABLE users
                 (firstname text, lastname text, gender text, city text, age int)''')
    c.execute('''CREATE TABLE user_event
                 (user_id int, event_id text, partecipated int)''')
    users = [
        ('Mario', 'Rossi', 'M', 'Milano', 25),
        ('Francesca', 'Trello', 'F', 'Milano', 17),
        ('Andrea', 'Rotin', 'M', 'Milano', 36),
        ('Marta', 'Zaini', 'F', 'Milano', 22),
        ('Annalisa', 'Poteri', 'F', 'Milano', 45),
        ('Alessandro', 'Vaghi', 'M', 'Roma', 19),
        ('Matteo', 'Tundo', 'M', 'Roma', 38),
        ('Alice', 'Perla', 'F', 'Roma', 20),
        ('Milena', 'Gabanello', 'F', 'Roma', 29),
        ('Riccardo', 'Volentis', 'M', 'Roma', 51),
    ]
    c.executemany('INSERT INTO users VALUES (?,?,?,?,?)', users)
    return 'Hello, World!'

@app.route('/users')
def list_users():
    username = ''
    for user in query_db('select * from users'):
        username =  user['firstname']
    return username

if __name__ == '__main__':
    app.run(host='0.0.0.0')
