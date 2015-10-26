import geojson
import os
import sqlite3
import json

_SESSION={}

def init():
    raw_data = open(os.path.join(os.path.dirname(__file__), 'mys_map.geojson')).read()
    
    parsed = geojson.loads(raw_data)
    conn = _SESSION.get('sqlite', None)
    if not conn:
        conn = sqlite3.connect(':memory:')
        _SESSION['sqlite'] = conn
        conn.execute('''
            CREATE TABLE features (
                country text, 
                state text, 
                district text,
                type text,
                data text
            ) ''')
    if _SESSION.get('initialized', False):
        return

    for feature in parsed['features']:
        props = feature['properties']
        conn.execute('''
            INSERT INTO features VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
            )''', (
                props['NAME_0'].upper(), 
                props['NAME_1'].upper(), 
                props['NAME_2'].upper(),
                props['TYPE_2'].upper(),
                json.dumps(feature)
            ))
    conn.commit()
    _SESSION['initialized'] = True

init()

def query(state=None):
    if state is None:
        conn = _SESSION['sqlite']
        res = conn.execute('select data from features')
    else:
        conn = _SESSION['sqlite']
        res = conn.execute('select data from features where state=?',
                (state.upper(),))
    features = []
    for r in res:
        features.append(json.loads(r[0]))
    return {
        'type': 'FeatureCollection',
        'features': features
    }
