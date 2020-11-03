from pymongo import MongoClient, DESCENDING, ASCENDING # 아래로 내려가는 내림차순(또는 필요시 오름차순) 정렬 기능을 추가해준다.

client = MongoClient()
mydb=client['mydb']

### $match operator to select specific cars to aggregate. ###

aggregation = [{ '$match': {'$or': [ { 'name': "Audi" }, { 'name': "Volvo" }] }},
        { '$group': {'_id': 1, 'sum2cars': { '$sum': "$price" } }}]

val = list(mydb.cars.aggregate(aggregation))

print('두 자동차 가격의 합은 {} 입니다.'.format(val[0]['sum2cars']))