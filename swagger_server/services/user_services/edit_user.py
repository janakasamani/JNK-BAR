from swagger_server.models.edit_user_request import EditUserRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def edit_user(edit_request: EditUserRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    filter = {
        "name": edit_request.name,
        "username": edit_request.username,
        "email": edit_request.email,
        "password": edit_request.password,
        "date of birth": edit_request.date_of_birth,
        "role": edit_request.role,
        "user_balance": edit_request.user_balance,
            }
    filter_2 = {"username": edit_request.username}
    user = collection.find_one(filter_2)
    if not user:
        return {"message": "invalid username"}, 401
    else:
        response = collection.update_one(user, {"$set": filter})
        return InlineResponse200(message="done")


