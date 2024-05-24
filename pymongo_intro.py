import pymongo
import pprint

# Connecting to MongoDB
client = pymongo.MongoClient()  # This automatically calls the default address of our connection
db = client["starwars"]
#
# # Retrieve a document from the database
# luke = db.characters.find_one({"name": "Luke Skywalker"})
# print(luke)
#
# # Getting only certain fields
# luke_short = db.characters.find_one({"name": "Luke Skywalker"}, {"name": 1, "eye_color": 1, "_id": 0})
# print(luke_short)
#
# # Iterating through multiple records/documents
# droids = db.characters.find({"species.name": "Droid"}, {"name": 1, "species.name": 1})
# print(droids)

# Basics
# Exercise 1 - Find the height of Darth Vader, only return results for the name and the height.
darth_vader = db.characters.find_one({"name": "Darth Vader"}, {"_id": 0, "name": 1, "height": 1})
print(darth_vader)

# Exercise 2 - Find all characters with yellow eyes, only return results for the names of the characters.
yellow_eyes = db.characters.find({"eye_color": "yellow"}, {"_id": 0, "name": 1, "species.name": 1})
print([char for char in yellow_eyes])

# Exercise 3 - Find male characters. Limit your results to only show the first 3.
males = db.characters.find({"gender": "male"}, {"_id": 0, "name": 1})
print([char for char in males][:3])

# Exercise 4 -Find the names of all the humans whose homeworld is Alderaan.
alderaan_humans = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"}, {"_id": 0, "name": 1})
print([char for char in alderaan_humans])

# Pymongo Aggregation

# Exercise 1 - What is the avaerage height of female characters?
pipeline = [
    {"$match": {"gender": "female"}},
    {"$group": {"_id": "$gender", "avgHeight": {"$avg": "$height"}}},
]

pprint.pprint(list(db.characters.aggregate(pipeline)))

# Exercise 2 - Which character is the tallest?
pipeline = [
    {"$match": {"name": {"$nin": [None]}}},
    {"$group": {"_id": ["$name", "$height"] }}, #, "maxHeight": {"$max": "$height"}}},
    {"$sort": {"_id[""$height""]": -1}},
    {"$limit": 1}
]

pprint.pprint(list(db.characters.aggregate(pipeline)))
