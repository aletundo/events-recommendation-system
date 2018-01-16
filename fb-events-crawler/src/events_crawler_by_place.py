#!/usr/bin/env python3
# coding=utf-8
import facebook, os, sys, json, pprint, copy

CATEGORIES = ['Arte', 'Musica', 'Festa', 'Sport', 'Cibo']
CITIES = ['Milano', 'Roma']

milan_places = {
    'Arte': [
        {
            'name': 'MUDEC - Museo delle Culture'
        },
        {
            'name': 'Castello Sforzesco di Milano'
        },
        {
            'name': 'Palazzo Reale Milano'
        },
        {
            'name': 'Pirelli HangarBicocca'
        },
        {
            'name': 'Museo Archeologico di Milano'
        },
        {
            'name': 'Museo del Novecento'
        },
        {
            'name': 'Statuto13'
        },
        {
            'name': 'Museo Poldi Pezzoli'
        },
        {
            'name': 'GAM Manzoni'
        }
    ],
    'Festa': [
        {
            'name': 'Alcatraz'
        },
        {
            'name': 'AMNESIA milano'
        },
        {
            'name': 'Fabrique Milano'
        },
        {
            'name': 'Quantic'
        },
        {
            'name': 'The Club Milano'
        },
        {
            'name': 'Hollywood - Milano'
        },
        {
            'name': 'Gate Milano'
        },
        {
            'name': 'MAGAZZINI GENERALI'
        },
        {
            'name': 'VIBE Room'
        }
    ],
    'Sport': [
        {
            'name': 'Milano Marathon'
        },
        {
            'name': 'MTB Milano Trail Bike'
        },
        {
            'name': 'Befly - Flying Trapeze Milano'
        },
        {
            'name': 'Stadio San Siro'
        },
        {
            'name': 'Club della Vela Mareaperto'
        },
        {
            'name': 'Ape Milano'
        },
        {
            'name': 'Centro Sportivo Crespi'
        },
        {
            'name': 'Gonzaga SPORT CLUB'
        },
        {
            'name': 'Il tempio dello sport asd'
        },
        {
            'name': 'CrossFit Bicocca'
        }
    ],
    'Musica': [
        {
            'name': 'La salumeria della musica'
        },
        {
            'name': 'Santeria Social Club'
        },
        {
            'name': 'Kraken Pub'
        },
        {
            'name': 'NAM MILANO'
        },
        {
            'name': 'Macao'
        },
        {
            'name': 'Legend Club Milano'
        },
        {
            'name': 'Blueshouse'
        },
        {
            'name': 'Blue Note Milano'
        }
    ],
    'Cibo': [
        {
            'name': 'Eataly'
        },
        {
            'name': 'Vineria di Via Stradella'
        },
        {
            'name': 'Enoteca Da Gatto'
        },
        {
            'name': 'Mr. Jangì'
        },
        {
            'name': 'La Scighera'
        },
        {
            'name': 'Italiancakedesign School'
        },
        {
            'name': 'Farm-65'
        },
        {
            'name': 'Ristorante Officina 12'
        },
        {
            'name': 'Ross & Bianch'
        },
        {
            'name': 'Ca\'Lore'
        }
    ],
}

def get_graph_instance():
    if os.environ.get('CLIENT_ID') == None or os.environ.get('CLIENT_SECRET') == None:
        raise ValueError("CLIENT_ID and/or CLIENT_SECRET not set")
    access_token = os.environ.get('CLIENT_ID') + '|' + os.environ.get('CLIENT_SECRET')
    graph = facebook.GraphAPI(access_token=access_token, version="2.11")
    return graph

def collect_places_id(graph, places):
    for place in places:
        places_response = graph.search(type='place', q=place['name'], fields='id,name')
        results = places_response['data']
        if not results:
            raise ValueError('Place not found! Remove: ' + place['name'])
        else:
            for r in results:
                if r['name'] == place['name']:
                    place['id'] = r['id']
                    break

        if not 'id' in place:
            raise ValueError('Place not found! Remove: ' + place['name'])
    return places

def collect_events_by_place_id(graph, place_id, after=None, results=list()):
    if after == None:
        events_response = graph.get_object(id=place_id+'/events', fields='name,description,start_time,end_time,id,picture{url}')
    else:
        events_response = graph.get_object(id=place_id+'/events', fields='name,description,start_time,end_time,id,picture{url}', after=after)

    if events_response['data']:
        results.extend(events_response['data'])

    if 'paging' in events_response.keys():
        collect_events_by_place_id(graph, place_id, events_response['paging']['cursors']['after'], results)

    return results

def collect_events(graph, places, category, city):
    for place in places:
        events = collect_events_by_place_id(graph, place['id'])
        for event in events:
            event['category'] = category
            event['city'] = city
        place['events'] = events
    return places

graph = get_graph_instance()
for category in milan_places.keys():
    milan_places[category] = collect_places_id(graph, milan_places[category])
    milan_places[category] = collect_events(graph, milan_places[category], category, 'Milano')

for category in rome_places.keys():
    rome_places[category] = collect_places_id(graph, rome_places[category])
    rome_places[category] = collect_events(graph, rome_places[category], category, 'Roma')
