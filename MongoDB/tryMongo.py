from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client.test1 #Database
#db = client['test']

coll = db.restaurants  #Collection
#coll = db['restaurants']

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
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

print result.inserted_id

print "Finish add value"
print "Start find value"

cursor = db.restaurants.find()
for document in cursor:
	print(document)

cursorField = db.restaurants.find({"address.zipcode": "10075"})
for document in cursorField:
	print(document)

cursorArray = db.restaurants.find({"grades.grade": "B"})
for document in cursorArray:
	print(document)