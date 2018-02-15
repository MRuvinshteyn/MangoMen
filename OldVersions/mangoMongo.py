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
        ret = []
        for i in restaurants:
            ret.append(i)
        print ret
        return ret

#findRestaurantsByBorough("Queens")

def findRestaurantsByZipcode(zipcode):
    restaurants = collection.find({"address.zipcode":zipcode})
    if (print_results):
        for i in restaurants:
            print i
    else:
        ret = []
        for i in restaurants:
            ret.append(i)
        print ret
        return ret

#findRestaurantsByZipcode("11377")

def findRestaurantsByZipcodeAndGrade(zipcode, grade):
    restaurants = collection.find({"address.zipcode":zipcode, "grades.grade":grade})
    if (print_results):
        for i in restaurants:
            print i
    else:
        print restaurants
        return restaurants

#findRestaurantsByZipcodeAndGrade("11377", "A")

def findRestaurantsByZipcodeWithMaxScore(zipcode, score):
    restaurants = collection.find({"address.zipcode":zipcode, "grades.score": {"$lt": score}})
    if (print_results):
        for i in restaurants:
            print i
    else:
        print restaurants
        return restaurants

#findRestaurantsByZipcodeWithMaxScore("11377", 15)

def findRestaurantsBy(key, value):
    restaurants = collection.find({key:value})
    if (print_results):
        for i in restaurants:
            print i
    else:
        print restaurants
        return restaurants

findRestaurantsBy("grades.score", 11)
