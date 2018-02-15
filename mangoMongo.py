from pymongo import MongoClient

print_results = True #print items individually or return them as a list?

c = MongoClient("lisa.stuy.edu")
db = c.test
collection = db.restaurants

#for i in collection.find():
    #print len(i['grades'])

    
def findRestaurantsByBorough(borough):
    restaurants = collection.find({"borough":borough})
    if (print_results):
        for i in restaurants:
            print i
    else:
        #print restaurants
        return restaurants

#findRestaurantsByBorough("Queens")

def findRestaurantsByZipcode(zipcode):
    restaurants = collection.find({"address.zipcode":zipcode})
    if (print_results):
        for i in restaurants:
            print i
    else:
        print restaurants
        return restaurants

#findRestaurantsByZipcode("11377")
