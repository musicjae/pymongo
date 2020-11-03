from pymongo import MongoClient

client = MongoClient()

mydb = client['mydb']

###  $sum operator calculates and returns the sum of numeric values. ###
###  $group operator groups input documents by a specified identifier expression and applies the accumulator expression(s), if specified, to each group. ###

aggregation = [{'$group':{'_id':1,'all':{'$sum':'$price'}}}]
val = list(mydb.cars.aggregate(aggregation))

print('자동차의 가격은 {} 달러 입니다.'.format(val[0]['all']))