# coding=utf-8
from flask import current_app
from bson.json_util import loads
import glob, json, os

def get_users_collection(client):
    return client.db.users

def get_events_collection(client):
    return client.db.events

def init_events_collection(client):
    collection = get_events_collection(client)
    collection.delete_many({})
    data_dir = current_app.config['DATA_DIR']
    for json_file in glob.glob(os.path.join(data_dir, '*.json')):
        events = json.load(open(json_file))
        collection.insert_many(events)

def init_users_collection(client):
    collection = get_users_collection(client)
    collection.delete_many({})
    collection.insert_many([
        {
            'firstname': 'Mario',
            'lastname' : 'Rossi',
            'gender' : 'M',
            'city' : 'Milano',
            'age' : 25,
        },
        {
            'firstname': 'Francesca',
            'lastname' : 'Trello',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 17,
        },
        {
            'firstname': 'Andrea',
            'lastname' : 'Rotin',
            'gender' : 'M',
            'city' : 'Milano',
            'age' : 36,
        },
        {
            'firstname': 'Marta',
            'lastname' : 'Zaini',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 22,
        },
        {
            'firstname': 'Annalisa',
            'lastname' : 'Poteri',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 45,
        },
        {
            'firstname': 'Alessandro',
            'lastname' : 'Vaghi',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 19,
        },
        {
            'firstname': 'Matteo',
            'lastname' : 'Tundo',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 38,
        },
        {
            'firstname': 'Alice',
            'lastname' : 'Perla',
            'gender' : 'F',
            'city' : 'Roma',
            'age' : 20,
        },
        {
            'firstname': 'Milena',
            'lastname' : 'Gabanelli',
            'gender' : 'F',
            'city' : 'Roma',
            'age' : 29,
        },
        {
            'firstname': 'Riccardo',
            'lastname' : 'Volentis',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 51,
        },
    ])
