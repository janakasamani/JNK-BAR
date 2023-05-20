from swagger_server.models.purchase_drink_request import PurchaseDrinkRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo
import connexion

def purchase_drink(drink_request: PurchaseDrinkRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["orders"]
    #token_payload = connexion.context["token_info"]["test_key"]
    #username = token_payload.get("username")
    #print("username", username)
    user =
    ]
    #user = drink_request.to_dict()
    #user["purchased by"] = username
    response = collection.insert_one(user)
    created_id = response.inserted_id

    message = "Drink purchased Successfully "
    return InlineResponse200(message=message + str(created_id))
