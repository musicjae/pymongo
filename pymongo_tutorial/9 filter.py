# The first parameter of find() and find_one() is a filter. The filter is a condition that all documents must match.

from pymongo import MongoClient

client = MongoClient()
mydb=client['mydb']

expensive_cars = mydb.cars.find({'price':{'$gt':50000}}) # 50000 보다 크거나 같은 것을 탐색

for ecar in expensive_cars:
    print(ecar)
    print(ecar['name'])
