import urllib2,json
from pymongo import MongoClient

url = urllib2.urlopen("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json")
#print jsonMango
jsonMango = json.load(url)

c = MongoClient("lisa.stuy.edu")
db = c.mangoMen

collection = db.pokemon

collection.insert(jsonMango)
