# The find methods return a PyMongo cursor, which is a reference to the result set of a query.

from pymongo import MongoClient

client = MongoClient()

mydb=client['mydb']

mycol_car= mydb['cars']

cars_find= mycol_car.find()


print(cars_find.next())
print(cars_find.next())
print(cars_find.next())

cars_find.rewind() # The rewind() method rewinds the cursor to its unevaluated state.

print(cars_find.next())
print(cars_find.next())
print(cars_find.next())

print(list(cars_find))

