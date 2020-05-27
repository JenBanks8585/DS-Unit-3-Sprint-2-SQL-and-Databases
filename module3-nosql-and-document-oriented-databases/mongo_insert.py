


#client = pymongo.MongoClient("mongodb+srv://jenniferbanks8585:rover12345@cluster0-70sz6.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test

import pymongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient

#load_dotenv()
#db = client.test

MONGO_USER="jenniferbanks8585"
MONGO_PASSWORD = "rover12345"
MONGO_CLUSTER_NAME="cluster0-70sz6"

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)


client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
breakpoint()
db = client.inclass_db # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.inclass_pokemon # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))