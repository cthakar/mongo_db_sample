__author__ = 'chintanthakar'

from pymongo import MongoClient
import pymongo

client = MongoClient("10.10.3.27:27017")
db = client.test

#cursor = db.restaurants.find()
#cursor = db.restaurants.find({"cuisine": "Italian"})
#cursor = db.restaurants.find({"address.zipcode": "10075"})
#cursor = db.restaurants.find({"grades.grade": "B"})
#cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
#cursor = db.restaurants.find({"grades.score": {"$lt": 10}})

#Logical AND with comma
#cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

#Logical OR with $or

#cursor = db.restaurants.find(
#    {"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})

#sorting output

cursor = db.restaurants.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.DESCENDING)
])




for document in cursor:
    print(document)

