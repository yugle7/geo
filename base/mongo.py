import pymongo

client = pymongo.MongoClient('localhost', 27017)

# ----------------------------------

# cd C:\Program Files\MongoDB\Server\3.0\bin
# mongod.exe --dbpath C:\data

# ----------------------------------

temp_collection = client.data['temp']  # для точек в процессе получения трека
position_collection = client.data['position']  # позиции людей

square_collection = client.data['square']  # данные для поиска

active_collection = client.data['active']  # вероятность активности
attract_collection = client.data['attract']  # точки притяжения
