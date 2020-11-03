from pymongo import MongoClient
from pprint import pprint

client=MongoClient()

mydb = client['mydb']

status = mydb.command("serverStatus")
pprint(status)

# The example prints a lengthy servers status.