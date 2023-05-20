from swagger_server.models.add_user_request import AddUserRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def add_user(user_request: AddUserRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    user_request_dict = user_request.to_dict()
    try:
        response = collection.insert_one(user_request_dict)
        created_id = response.inserted_id
    except pymongo.errors.DuplicateKeyError:
        return {"error": "Username already exists"}
    message = "User Created Successfully"
    return InlineResponse200(message=message)

