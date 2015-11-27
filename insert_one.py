__author__ = 'chintanthakar'

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("10.10.3.27:27017")
db = client.test

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "3 Avenue",
            "zipcode": "10076",
            "building": "1481",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

print(result.inserted_id)


#print('hello')


