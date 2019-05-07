from pymongo import MongoClient
uri = "mongodb+srv://admin:admin@c4e29-cluster-4yazl.mongodb.net/test?retryWrites=true"
#1. Open connection
client = MongoClient(uri)

#2. get/Create database
bike_app = client.bike_application

#3. get/create collection
Bikes = bike_app["bike_collection"]