from flask import Flask, render_template, request

app = Flask(__name__)

import json
from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')
db = c.mangoMen
collection = db.pokemon

#add all pokemon from API into database, unless the database already exists
if collection.count() == 0:
    print 'Adding pokemon to database...'
    with open('pokedex.json', 'rU') as f:
        s = f.read()
        f.close()
    collection.insert_many(json.loads(s)['pokemon'])
else:
    print 'Pokemon are already in database'

#returns list of pokemon based on id
def find_pokemon_by_id(num):
    ret = []
    for p in db.pokemon.find({'id' : num}):
        ret.append(p)
    return ret

#returns list of pokemon based on name
def find_pokemon_by_name(name):
    ret = []
    for p in db.pokemon.find({'name' : name}):
        ret.append(p)
    return ret

#returns list of pokemon based on type
def find_pokemon_by_type(pokemon_type):
    ret = []
    for p in db.pokemon.find({'type' : pokemon_type}):
        ret.append(p)
    return ret

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def query():
    search_query = request.args.get('query').strip()
    full_list = []
    if search_query.isdigit():
        full_list += find_pokemon_by_id(int(search_query))
    full_list += find_pokemon_by_name(search_query)
    full_list += find_pokemon_by_type(search_query)
    ret = ''
    for pokemon in full_list:
        entry = {}
        entry['id'] = pokemon['id']
        entry['name'] = pokemon['name'].encode('ascii', 'ignore')
        entry['type'] = pokemon['type'][0].encode('ascii', 'ignore')
        entry['img'] = pokemon['img'].encode('ascii', 'ignore')
        ret += 'Pokemon #%d: %s with type %s,' % (entry['id'], entry['name'], entry['type'])
    return ret[:-1]

if __name__ == '__main__':
    app.run(debug=True)
