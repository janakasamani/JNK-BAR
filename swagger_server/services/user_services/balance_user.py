from swagger_server.models.edit_balance_request import EditBalanceRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def balance_user(balance_request: EditBalanceRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    request_balance = balance_request.user_balance

    username = {
        "username": balance_request.username
            }

    user = collection.find_one(username)

    if not user:
        return {"message": "invalid username"}, 401
    else:
        top_up_balance = collection.update_one(user, {"$inc": {"user_balance": request_balance}})
        return InlineResponse200(message="done")


