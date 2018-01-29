# coding=utf-8
from . import sqlite as sqlite_utils
from . import mongodb as mongodb_utils
from flask import current_app
from random import randint, uniform
import numpy as np

def sample_event(client, events_id_list, category, city):
    events = list(mongodb_utils.get_events_collection(client).find({'category': category, 'city': city}))
    event_index = randint(0, len(events) - 1)
    event_id = events[event_index].get('_id')
    if event_id in events_id_list:
        sample_event(client, events_id_list, category, city)
    else:
        return event_id

def simulate_users_events(client):
    categories = ['Arte', 'Cibo', 'Festa', 'Musica', 'Sport']
    cities = ['Roma', 'Milano']
    users = mongodb_utils.get_users_collection(client).find({})
    events_number = 50
    for user in users:
        events_id_list = list()
        choices = np.random.choice(categories, events_number, replace=True, p=user.get('categories_distribution'))
        user_category_freq = {'Arte': 0, 'Festa': 0, 'Sport': 0, 'Musica': 0, 'Cibo': 0}
        user_city = user.get('city')
        # current_app.logger.info(user.get('categories_distribution'))
        # current_app.logger.info(choices)
        for c in choices:
            user_category_freq[c] += 1
            if uniform(0, 1) > 0.3:
                city = user_city if (cities[0] == user_city) else cities[1]
            else:
                city = cities[1] if (cities[0] == user_city) else user_city
            event_id = sample_event(client, events_id_list, c, city)
            events_id_list.append(event_id)
            sqlite_utils.query_db('INSERT INTO user_event (user_id, event_id, partecipated) VALUES(?, ?, ?)', [str(user.get('_id')), str(event_id), 1,])
        mongodb_utils.get_users_collection(client).update_one(
            {'_id': user.get('_id')},
            {'$set': {'categories_frequency' : user_category_freq}}
        )


        # for i in range(0, events_number):
        #     category_index = randint(0, 4)
        #     category = categories[category_index]
        #     user_category_freq[category] += 1
        #     event_id = sample_event(client, events_id_list, category)
        #     events_id_list.append(event_id)
        #     sqlite_utils.query_db('INSERT INTO user_event (user_id, event_id, partecipated) VALUES(?, ?, ?)', [str(user.get('_id')), str(event_id), 1,])
