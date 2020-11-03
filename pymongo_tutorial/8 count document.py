from pymongo import MongoClient

client = MongoClient()
mydb=client['mydb']

n_cars =mydb.cars.find().count()

print(f'차가 {n_cars}개 있다.')