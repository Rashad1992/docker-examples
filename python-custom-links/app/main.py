from http import client
from pymongo import MongoClient 
from pprint import pprint

Mongo_URL = "mongodb://mongo:27017"
client=MongoClient(Mongo_URL)
db=client.records
col=db.links
col.insert_one({"link":"Furqanist.com"})
links=col.find({})
for link in links:
    pprint(link)
