# coding=utf-8
import sqlite3
from flask import current_app, g

def init_db():
    with current_app.app_context():
        result = query_db('SELECT name FROM sqlite_master WHERE type=? AND name=?', ('table', 'user_event'), True)
        if result is None:
            query_db('CREATE TABLE user_event (user_id int, event_id text, partecipated int)')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE'])
    db.row_factory = make_dicts
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    get_db().commit()
    return (rv[0] if rv else None) if one else rv

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
