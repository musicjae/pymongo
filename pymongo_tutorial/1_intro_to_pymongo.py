# https://www.youtube.com/watch?v=YbLzV90dksE
import pymongo

# 클라이언트가 상호작용할 데이터베이스가 필요하다

client = pymongo.MongoClient()

mydb = client["mydb"]

# (1) New collection

mycol = mydb["people"]

# (2) col 내에 datum 넣기

data1 = {'name': 'Jaeyoung', 'age': 29,'type':'man'}  # we can store data into collection through dict type
data2 = {'name':'Cheolsu','age':27,'type':'man'}

mycol.insert_one(data1)  # mycol이라는 collection에 data를 넣는 함수.
mycol.insert_one(data2)

# (3) data를 list로

datalist1 = [{'name':'jane','age':40,'type':'woman'},{'name': 'john','age':32,'type':'man'}]
mycol.insert_many(datalist1)

# (4) clinet에 있는 이름들 출력

print('(4)',client.list_database_names())

# (5) 특정 client 내의 col 이름들 출력

print('(5)',mydb.list_collection_names())

# (6) 특정 col 내의 datum 출력

#for i in mycol.find():
#    print('(6)',i)

# 의문점: 왜 단 한 번씩만 각 id에 상응하는 자료가 출력되지 않고 반복적으로 몇 번씩이나 동일한 자료가 출력되는가?

# (6-2)

for i in mycol.find({"name":{"$gte":29}}): # gte means that its value in question is greater or equal
    print('(6-2)',i)

