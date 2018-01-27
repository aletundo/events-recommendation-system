#!/usr/bin/env python
# coding=utf-8
from flask import Flask, g, current_app
from flask_pymongo import PyMongo
from utils import sqlite as sqlite_utils
from utils import mongodb as mongodb_utils
from utils import matrix_sim as simulation_utils
from bson.json_util import dumps
from bson.objectid import ObjectId
from scipy import spatial

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

@app.route('/users/<string:user_id>/recommendations')
def recommendations(user_id):
    results = compute_recommendations(user_id)
    events = list()
    for event_id in results['events']:
        events.append(mongodb_utils.get_events_collection(mongo).find_one({'_id': ObjectId(event_id)}))
    results['events'] = events
    return dumps(results)

def compute_recommendations(target_user_id):
    target_user = mongodb_utils.get_users_collection(mongo).find_one({'_id': ObjectId(target_user_id)})
    users_list = list(mongodb_utils.get_users_collection(mongo).find({'_id': {'$ne': ObjectId(target_user_id)}}))
    similar_users_list = list()
    events_id_to_suggest = set()
    threshold = 0.05
    for user in users_list:
        target_user_events = [e['event_id'] for e in sqlite_utils.query_db('SELECT event_id FROM user_event WHERE user_id = ?', (target_user_id,)) if 'event_id' in e and e['event_id'] != 'None']
        user_events =  [e['event_id'] for e in sqlite_utils.query_db('SELECT event_id FROM user_event WHERE user_id = ?', (str(user.get('_id')),)) if 'event_id' in e and e['event_id'] != 'None']
        similarity = users_similarity(target_user, user, target_user_events, user_events)
        if similarity >= threshold:
            similar_users_list.append(user)
            events_id_to_suggest = events_id_to_suggest.union(set(user_events).difference(set(target_user_events)))
    return {'events': events_id_to_suggest, 'users': similar_users_list}

def category_normalization(user_category_freq):
    freq_sum = 0
    for key, value in user_category_freq.items():
        freq_sum += value
    for key,value in user_category_freq.items():
        user_category_freq[key] = value/freq_sum
    return user_category_freq

def users_similarity(target_user, other_user, target_user_events, other_user_events):
    target_user_norm_freq = category_normalization(target_user['categories_frequency'])
    other_user_norm_freq = category_normalization(other_user.get('categories_frequency'))

    target_user_events_set = set(target_user_events)
    other_user_events_set = set(other_user_events)
    common_events = target_user_events_set.intersection(other_user_events_set)

    target_user_vect = []
    other_user_vect = []
    for event in common_events:
        event_category = mongodb_utils.get_events_collection(mongo).find_one({'_id': ObjectId(event)}).get('category')
        target_user_category_weight = target_user_norm_freq[event_category]
        other_user_category_weight = other_user_norm_freq[event_category]
        target_user_vect.append((1 * target_user_category_weight))
        other_user_vect.append((1 * other_user_category_weight))

    return spatial.distance.cosine(target_user_vect, other_user_vect)

@app.before_first_request
def init_data():
    sqlite_utils.init_db()
    mongodb_utils.init_users_collection(mongo)
    mongodb_utils.init_events_collection(mongo)
    simulation_utils.simulate_users_events(mongo)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
