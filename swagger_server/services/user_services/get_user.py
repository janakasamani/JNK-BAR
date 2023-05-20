from swagger_server.models.get_user_response import GetUserResponse
import pymongo

def get_user(username = None):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    filter = {}
    if username:
        filter["username"] = username

    user = collection.find_one(filter)

    return GetUserResponse.from_dict(user)
