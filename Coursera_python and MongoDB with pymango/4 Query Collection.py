from pymongo import MongoClient
from pprint import pprint

fh = open("./Vocabulary_set.csv", "r")
wd_list = fh.readlines()

wd_list.pop(0) # delete First word

vocab_list =[]

for rawstring in wd_list:
    word, definition = rawstring.split(',',1) # maxsplit=1
    definition = definition.rstrip()
    vocab_list.append({'word':word,'definition':definition})

# mongdb와의 연결을 위해서는 uri이 요구된다.

client = MongoClient("mongodb://localhost:27017/")
db=client['vocab']

#(1) db 리스트 이름 확인

dbs = client.list_database_names()
vocab_col = db["vocab_list"]

# (2) doc을 col 안으로 넣어보자.

vocab_dict = {'word':'cryptic','definition':'secret with hidden meaning'}

# (2-1) 한번에 하나 넣기
res = vocab_col.insert_one(vocab_dict)
#print('inserted id: ',res.inserted_id)
#if "vocab" in dbs:
#   print('exist')

#(2-2) 한번에 많이 넣기

res2 = vocab_col.insert_many(vocab_list)

# (3) query col

#(3-1) only one

data=vocab_col.find_one()
#print(data)

#(3-2) many
j=0
"""
for data in vocab_col.find({}):
    print(data)
    j+=1
print('len: ',j+1)
"""
#for data in vocab_col.find({},{"_id":0,"definition":0}): # id와 definition이 제외된다.
    #print(data)

#(3-3) many & select
data = vocab_col.find_one({'word':'boisterous'},{"_id":0,"definition":0})
print(data)