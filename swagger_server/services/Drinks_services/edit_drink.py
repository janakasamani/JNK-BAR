from swagger_server.models.edit_drink_request import EditDrinkRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def edit_drink(edit_drink_request: EditDrinkRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["drinks"]

    filter_1 = {"name": edit_drink_request.name}

    edit_request = {"name": edit_drink_request.name,
                "ingredients": edit_drink_request.ingredients,
                "price": edit_drink_request.price,
                "quantity": edit_drink_request.quantity,
                "is_active": edit_drink_request.is_active
                 }


    drink = collection.find_one(filter_1)
    if not drink:
        return {"message": "drink doesnt exist"}, 401
    else:
        updated_drink = collection.update_one(drink, {"$set": edit_request})
        message = "Drink updated Successfully"
        return InlineResponse200(message=message)


