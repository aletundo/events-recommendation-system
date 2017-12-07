#!/usr/bin/env python3
# coding=utf-8

import facebook_bot, json
import os, glob, sys, argparse, time
from os.path import basename

TODAY = time.strftime("%Y-%m-%d")
EVENT_FIELDS = [
    'id',
    'name',
    'start_time',
    'end_time',
    'description',
    'place',
    'type',
    'category',
    'ticket_uri',
    'cover.fields(id,source)',
    'picture.type(large)',
    'attending_count',
    'declined_count',
    'maybe_count',
    'noreply_count'
]

def crawl(lat=45.464211, lng=9.191383, place_type='*', distance=500, scan_radius=500, base_time=TODAY, fields=EVENT_FIELDS):

    # Change directory to the script directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Create data directory if it not exists
    data_dir_path = "../data/"
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)

    print("Starting Facebook events crawaler...")

    # Getting events from Facebook API
    results = facebook_bot.get_events_by_location(lat, lng, place_type, distance, scan_radius, base_time, fields)

    # Create events JSON object
    events_files = dict()
    events = list()
    events_file_counter = 1

    for result in results:
        print(result)
        events += result
        if len(events) >= 50:
            events_dict = {'events':events}
            events_json = json.dumps(events_dict)
            events_files[str(events_file_counter)] = events_json
            events = list()
            events_file_counter += 1
    # Get remaining events if they exist
    if len(events) > 0:
        events_dict = {'events':events}
        events_json = json.dumps(events_dict)
        events_files[str(events_file_counter)] = events_json

    print("Crawling completed!")

    # Write JSON to files
    for key, events in events_files.items():
        events_file_path = "{}events-{}.json".format(data_dir_path, key)
        events_file = open(events_file_path, 'w')
        events_file.write(events)
        events_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get all Facebook events from given location circle.')

    parser.add_argument('-lat','--latitude', help='Latitude of location\'s center', type=float, required=True)
    parser.add_argument('-lng','--longitude', help='Latitude of location\'s center', type=float, required=True)
    parser.add_argument('-pt','--place_type', help='Type of Page you want to get events from. \'*\' mean all.', default='*')
    parser.add_argument('-d','--distance', help='Radius of location\'s circle in meters. Limit it for better performances.', type=int, default=500)
    parser.add_argument('-bt', '--base_time', help='Limit started day to crawl events. Format: YYYY-MM-DD', default=TODAY)
    parser.add_argument('-f', '--fields', help='The fields list. It accepts a list [] to specificy a list of strings. See See more at \
    https://developers.facebook.com/docs/graph-api/reference/event.', nargs='+', default=EVENT_FIELDS)
    args = parser.parse_args()

    crawl(lat=args.latitude, lng=args.longitude, place_type=args.place_type, distance=args.distance, base_time=args.base_time, fields=args.fields)
