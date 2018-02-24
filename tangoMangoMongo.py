'''
Pokemon GO Dataset: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
Includes basic pokemon information such as pokedex number, name, and type as well as Pokemon GO specific information such as candy name and evolution line.
'''

import json
from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')
db = c.mangoMen
collection = db.pokemon

if collection.count() == 0:
    print 'Adding pokemon to database...'
    with open('pokedex.json', 'rU') as f:
        s = f.read()
        f.close()
    collection.insert_many(json.loads(s)['pokemon'])
else:
    print 'Pokemon are already in database'

def find_pokemon_by_id(num):
    ret = []
    for p in db.pokemon.find({'id' : num}):
        ret.append(p)
    return ret

def find_pokemon_by_name(name):
    ret = []
    for p in db.pokemon.find({'name' : name}):
        ret.append(p)
    return ret

def find_pokemon_by_type(pokemon_type):
    ret = []
    for p in db.pokemon.find({'type' : pokemon_type}):
        ret.append(p)
    return ret
