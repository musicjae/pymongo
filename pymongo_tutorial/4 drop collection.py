from pymongo import MongoClient

client = MongoClient()

mydb=client['mydb']
mydb.cars.drop() # 이것을 수행하면 cars collection 이 drop 된다.