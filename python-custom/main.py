from http import client
from pymongo import MongoClient 
from pprint import pprint

Mongo_URL = "mongodb://mongo:27017"
client=MongoClient(Mongo_URL)
db=client.admin
dbs_list=db.command("listDatabases")
pprint(dbs_list)