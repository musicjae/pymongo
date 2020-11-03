from pymongo import MongoClient


client = MongoClient()
mydb=client['mydb']

cars_col = mydb.cars.find()

list_cars=[]
list_prices=[]

for car in cars_col:
    print('{0} {1}'.format(car['name'],car['price']))
    list_cars.append(car['name'])
    list_prices.append(car['price'])

print(list_cars)
print(list_prices)





