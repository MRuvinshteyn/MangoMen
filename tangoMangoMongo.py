'''
Pokemon GO Dataset: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
Includes basic pokemon information such as pokedex number, name, and type as well as Pokemon GO specific information such as candy name and evolution line.

This script checks if the collection already exists before inserting data and doesn't do so if the data is already loaded into the database. 
'''

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
