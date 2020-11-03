# The limit query option specifies the number of documents to be returned and the skip() option some documents.

from pymongo import MongoClient

client = MongoClient()

mydb = client['mydb']



### (1) 모든 값을 출력하는 경우 ###

cars_1 = mydb.cars.find()
for car in cars_1:

    print( car['name'],car['price'])

### (2) skip, limit 기능이 추가된 경우 ###
print('\n')
cars = mydb.cars.find().skip(2).limit(3) # 앞에서 두 개의 doc을 스킵한 뒤 남은 것들 중 차례로 3 개의 doc만을 출력

for car in cars:
    print(car['name'],car['price'])