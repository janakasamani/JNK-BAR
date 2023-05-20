from swagger_server.models.login_request import LoginRequest
from swagger_server.models.login_response import LoginResponse
import pymongo
from helpers.token_helpers import get_token
def login_user(login_request: LoginRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    filt = {"username": login_request.username,
            "password": login_request.password,
    }
    login_response = collection.find_one(filt)
    if not login_response:
        return {"message": "invalid username or password"}, 401
    else:
        token = get_token(login_response)
        return LoginResponse(message="login successful", token=token)




