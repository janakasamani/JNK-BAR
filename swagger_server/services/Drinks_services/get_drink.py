from swagger_server.models.get_drink_response import GetDrinkResponse
import pymongo

def get_drink(name=None, ingredients=None):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["drinks"]

    filter= {}

    if name:
        filter["name"] = name
    if ingredients:
        filter["ingredients"] = ingredients
    response = collection.find_one(filter)
    return GetDrinkResponse.from_dict(response)


