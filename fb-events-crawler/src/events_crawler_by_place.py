#!/usr/bin/env python3
# coding=utf-8
import facebook, os, pytz
from dateutil import parser
from datetime import datetime
import json

rome_places = {
    'Arte': [
        {
            'name': 'Vatican Museums - Musei Vaticani'
        },
        {
            'name': 'Mercati di Traiano - Museo dei Fori Imperiali'
        },
        {
            'name': 'Musei Capitolini'
        },
        {
            'name': 'TAG - Tevere Art Gallery'
        },
        {
            'name': 'Fusolab 2.0'
        },
        {
            'name': 'Museo Del Vittoriano'
        },
        {
            'name': 'Fori Imperiali'
        },
        {
            'name': 'Scuderie del Quirinale'
        },
        {
            'name': 'Vatican Museums - Musei Vaticani'
        },
        {
            'name': 'Museo dell\'Ara Pacis'
        },
        {
            'name': 'Villa Farnesina'
        }
    ],
    'Festa': [
        {
            'name': 'Art Cafè'
        },
        {
            'name': 'Ex Magazzini'
        },
        {
            'name': 'Circolo Degli Illuminati'
        },
        {
            'name': 'BARRIO LATINO'
        },
        {
            'name': 'Room 26'
        },
        {
            'name': 'La Suite'
        },
        {
            'name': 'Spazio Novecento Ufficiale'
        },
        {
            'name': 'Shari Vari'
        },
        {
            'name': 'Piper Club Roma - Official'
        }
    ],
    'Sport' : [
        {
            'name': 'LUNGOTEVERE FITNESS'
        },
        {
            'name': 'Italiana Fitness®'
        },
        {
            'name': 'Heaven Fight Arena'
        },
        {
            'name': 'Otzuka Club - Arti Marziali'
        },
        {
            'name': 'Le Palme Sporting Club'
        },
        {
            'name': 'Asc Danza'
        },
        {
            'name': 'SSD Bracelli Club'
        },
        {
            'name': 'Karting Roma'
        }
    ],
    'Musica' : [
        {
            'name': 'Auditorium Parco della Musica - Roma'
        },
        {
            'name': 'Accademia Nazionale di Santa Cecilia'
        },
        {
            'name': 'Roma Atlantico Live'
        },
        {
            'name': 'Largo venue'
        },
        {
            'name': 'CrossRoads Live Club'
        },
        {
            'name': 'Wishlist Club'
        },
        {
            'name': 'Lanificio159'
        },
        {
            'name': 'ORION'
        }
    ],
    'Cibo' : [
        {
            'name': 'Mozzico'
        },
        {
            'name': 'Porto Fluviale'
        },
        {
            'name': 'Sweet King'
        },
        {
            'name': 'Haus Garten'
        },
        {
            'name': 'Bancovino'
        },
        {
            'name': 'FAD Burger and Bistrot - Centocelle'
        },
        {
            'name': 'Eataly'
        },
        {
            'name': 'Tavernacolo Roma Aurelio'
        }
    ]
}
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
            'name': 'Alcatraz - Milano'
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
        # {
        #     'name': 'Befly - Flying Trapeze Milano'
        # },
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

def collect_places_id(graph, places, category, city):
    for place in places:
        places_response = graph.search(type='place', q=place['name'], fields='id,name,location{city}')
        results = places_response['data']
        if not results:
            raise ValueError('Place not found! Remove: ' + place['name'])
        else:
            for r in results:
                if r['name'] == place['name'] and (r['location']['city'] == city[0] or r['location']['city'] == city[1]):
                    place['id'] = r['id']
                    break

        if not 'id' in place:
            raise ValueError('Place not found! Remove: ' + place['name'])
    print('Collected {} places id for {}'.format(category, city[1]))
    return places

def collect_events_by_place_id(graph, place_id, city, after=None, results=list()):
    if after == None:
        events_response = graph.get_object(id=place_id+'/events', fields='name,description,place{name,location{city}},start_time,end_time,id,picture{url}')
    else:
        events_response = graph.get_object(id=place_id+'/events', fields='name,description,place{name,location{city}},start_time,end_time,id,picture{url}', after=after)

    if events_response['data']:
        results.extend(events_response['data'])

    if 'paging' in events_response.keys():
        collect_events_by_place_id(graph, place_id, city, events_response['paging']['cursors']['after'], results)
    filtered_results = [
        x for x in results
        if parser.parse(x['start_time']) >= datetime(2017, 12, 1, 0, 0, 0, tzinfo=pytz.UTC)
        and 'place' in x.keys()
        and isinstance(x['place'], dict)
        and 'location' in x['place'].keys()
        and isinstance(x['place']['location'], dict)
        and 'city' in x['place']['location'].keys()
        and (x['place']['location']['city'] == city[0] or x['place']['location']['city'] == city[1])
    ]
    return filtered_results

def collect_events(graph, places, category, city):
    all_events = list()
    for place in places:
        events = collect_events_by_place_id(graph, place['id'], city)
        for event in events:
            event['category'] = category
            event['place'] = event['place']['name']
            event['city'] = city[0]
        print(events)
        all_events.extend(events)
        print('Collected events for {}'.format(place['name']))
    return all_events

os.chdir(os.path.dirname(os.path.realpath(__file__)))
data_dir = '../../recommendation-system-engine/data'
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)
    print('Data directory created')

graph = get_graph_instance()
milan_events = list()
for category in milan_places.keys():
    milan_places[category] = collect_places_id(graph, milan_places[category], category, ['Milano', 'Milan'])
    milan_events.extend(collect_events(graph, milan_places[category], category, ['Milano', 'Milan']))

with open(data_dir + '/Milan_events.json', 'w') as outfile:
    json.dump(milan_events, outfile, ensure_ascii=False)
    print('Created Milan events JSON file')

rome_events = list()
for category in rome_places.keys():
    rome_places[category] = collect_places_id(graph, rome_places[category], category, ['Roma', 'Rome'])
    rome_events = collect_events(graph, rome_places[category], category, ['Roma', 'Rome'])

with open(data_dir + '/Rome_events.json', 'w') as outfile:
    json.dump(rome_events, outfile, ensure_ascii=False)
    print('Created Rome events JSON file')
