from pymongo import MongoClient

# projection으로 우리는 반환된 document에서 특정 필드를 선택할 수 있다. 이 projections은 find() 메서드의 두번째 argument를 지나간다.

client = MongoClient()
mydb=client['mydb']

cars = mydb.cars.find({},{'_id':1,'name':1})
test_list=[]
for car in cars:
    print(car['name'])
    print(car['_id'])
    test_list.append(car['name'])

print('리스트 테스트: ',test_list[0])

# We can specify either including or excluding projections, not both at the same time.

