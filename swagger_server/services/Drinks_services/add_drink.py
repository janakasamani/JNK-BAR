from swagger_server.models.add_drink_request import AddDrinkRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo
import connexion

def add_drink(drink_request: AddDrinkRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["drinks"]
    token_payload = connexion.context["token_info"]["test_key"]
    username = token_payload.get("username")
    print("username", username)

    user = drink_request.to_dict()
    user["added_by_username"] = username
    response = collection.insert_one(user)
    created_id = response.inserted_id

    message = "Drink added Successfully "
    return InlineResponse200(message=message + str(created_id))
