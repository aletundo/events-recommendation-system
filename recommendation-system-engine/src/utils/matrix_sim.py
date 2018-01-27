# coding=utf-8
from . import sqlite as sqlite_utils
from . import mongodb as mongodb_utils
from flask import current_app
from random import randint

def sample_event(client, events_id_list, category):
    events = list(mongodb_utils.get_events_collection(client).find({'category': category}))
    event_index = randint(0, len(events) - 1)
    event_id = events[event_index].get('_id')
    if event_id in events_id_list:
        sample_event(client, events_id_list, category)
    else:
        return event_id

def simulate_users_events(client):
    categories = ['Arte', 'Festa', 'Sport', 'Musica', 'Cibo']
    users = mongodb_utils.get_users_collection(client).find({})
    events_number = 50
    for user in users:
        events_id_list = list()
        user_category_freq = {'Arte': 0, 'Festa': 0, 'Sport': 0, 'Musica': 0, 'Cibo': 0}
        for i in range(0, events_number):
            category_index = randint(0, 4)
            category = categories[category_index]
            user_category_freq[category] += 1
            event_id = sample_event(client, events_id_list, category)
            events_id_list.append(event_id)
            sqlite_utils.query_db('INSERT INTO user_event (user_id, event_id, partecipated) VALUES(?, ?, ?)', [str(user.get('_id')), str(event_id), 1,])
        mongodb_utils.get_users_collection(client).update_one(
            {'_id': user.get('_id')},
            {'$set': {'categories_frequency' : user_category_freq}}
        )
