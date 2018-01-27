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
            'avatar': 'https://tinyfac.es/data/avatars/BA0CB1F2-8C79-4376-B13B-DD5FB8772537-200w.jpeg',
        },
        {
            'firstname': 'Francesca',
            'lastname' : 'Trello',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 17,
            'avatar': 'https://tinyfac.es/data/avatars/03F55412-DE8A-4F83-AAA6-D67EE5CE48DA-200w.jpeg',
        },
        {
            'firstname': 'Andrea',
            'lastname' : 'Rotin',
            'gender' : 'M',
            'city' : 'Milano',
            'age' : 36,
            'avatar': 'https://tinyfac.es/data/avatars/B3CF5288-34B0-4A5E-9877-5965522529D6-200w.jpeg',
        },
        {
            'firstname': 'Marta',
            'lastname' : 'Zaini',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 22,
            'avatar': 'https://tinyfac.es/data/avatars/A7299C8E-CEFC-47D9-939A-3C8CA0EA4D13-200w.jpeg',
        },
        {
            'firstname': 'Annalisa',
            'lastname' : 'Poteri',
            'gender' : 'F',
            'city' : 'Milano',
            'age' : 45,
            'avatar': 'https://tinyfac.es/data/avatars/A7299C8E-CEFC-47D9-939A-3C8CA0EA4D13-200w.jpeg',
        },
        {
            'firstname': 'Alessandro',
            'lastname' : 'Vaghi',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 19,
            'avatar': 'https://tinyfac.es/data/avatars/2DDDE973-40EC-4004-ABC0-73FD4CD6D042-200w.jpeg',
        },
        {
            'firstname': 'Matteo',
            'lastname' : 'Tundo',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 38,
            'avatar': 'https://tinyfac.es/data/avatars/344CFC24-61FB-426C-B3D1-CAD5BCBD3209-200w.jpeg',
        },
        {
            'firstname': 'Alice',
            'lastname' : 'Perla',
            'gender' : 'F',
            'city' : 'Roma',
            'age' : 20,
            'avatar': 'https://tinyfac.es/data/avatars/03F55412-DE8A-4F83-AAA6-D67EE5CE48DA-200w.jpeg',
        },
        {
            'firstname': 'Milena',
            'lastname' : 'Gabanelli',
            'gender' : 'F',
            'city' : 'Roma',
            'age' : 29,
            'avatar': 'https://tinyfac.es/data/avatars/A7299C8E-CEFC-47D9-939A-3C8CA0EA4D13-200w.jpeg',
        },
        {
            'firstname': 'Riccardo',
            'lastname' : 'Volentis',
            'gender' : 'M',
            'city' : 'Roma',
            'age' : 51,
            'avatar': 'https://tinyfac.es/data/avatars/BA0CB1F2-8C79-4376-B13B-DD5FB8772537-200w.jpeg',
        },
    ])
