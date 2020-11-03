from pymongo import MongoClient, DESCENDING, ASCENDING # 아래로 내려가는 내림차순(또는 필요시 오름차순) 정렬 기능을 추가해준다.

client = MongoClient()
mydb=client['mydb']

cars = mydb.cars.find().sort("price",DESCENDING)

for car in cars:
    print(car['name'],car['price'])

cars_asc = mydb.cars.find().sort("price",ASCENDING)

print('\n')
for car in cars_asc:
    print(car['name'], car['price'])