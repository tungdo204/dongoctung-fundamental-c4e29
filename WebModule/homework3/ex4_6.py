from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)

db = client.c4e

river = db.river

first_river = river.find({'continent': 'Africa'})
for item in first_river:
    print(item['name'])

second_river = river.find({'$and':[{'continent':'S. America'},{'length':{'$lt':1000}}]})
for item in second_river:
    print(item['name'])
