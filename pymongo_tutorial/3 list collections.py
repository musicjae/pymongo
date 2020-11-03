from pymongo import MongoClient

client = MongoClient()

mydb =client['mydb']
print(mydb.list_collection_names())