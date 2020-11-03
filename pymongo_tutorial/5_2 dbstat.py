from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client['mydb']
print(mydb.collection_names())

status = mydb.command("dbstats")
pprint(status)