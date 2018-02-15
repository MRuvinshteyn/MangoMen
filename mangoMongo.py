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

def findRestaurantsByZipcodeAndGrade(zipcode,grade):
    restaurants = collection.find({"address.zipcode":zipcode})
    ret = []
    for i in restaurants:
        if len(i['grades']) > 0:
            for c in i['grades']:
                #print c['grade'] == grade
                if (c['grade'] == grade):
                    ret.append(i)
                    break
    if (print_results):
        for i in ret:
            print i
    else:
        print ret
        return ret
            
#findRestaurantsByZipcodeAndGrade("11377","B")

def findRestaurantsByZipcodeAndScore(zipcode,score):
    restaurants = collection.find({"address.zipcode":zipcode})
    ret = []
    intScore = int(score)
    for i in restaurants:
        if len(i['grades']) > 0:
            for c in i['grades']:
                print int(c['score']) < intScore
                if (int(c['score']) < intScore):
                    ret.append(i)
                    break
    if (print_results):
        for i in ret:
            print i
    else:
        print ret
        return ret
  
#findRestaurantsByZipcodeAndScore("11377","1")
