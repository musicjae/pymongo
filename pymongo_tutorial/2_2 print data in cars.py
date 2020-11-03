
import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]

mycol = mydb["cars"]

for i in mycol.find():
    print(i)