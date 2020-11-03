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

if "vocab" in dbs:
    print("Database Exist")

else:
    print("Non")

