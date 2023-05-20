from swagger_server.models.signup_request import SignupRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def signup_user(signup_request: SignupRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:a2hrElcoiW3vu6HQ@cluster0.8arxn8v.mongodb.net/test")
    database = myclient["JnKs_bartending"]
    collection = database["users"]

    user_dictionary = {
        "name": signup_request.name,
        "username": signup_request.username,
        "email": signup_request.email,
        "password": signup_request.password,
        "date of birth": signup_request.date_of_birth,
        "role": "costumer"
    }
    try:
        signup_response = collection.insert_one(user_dictionary)
        created_id = signup_response.inserted_id

    except pymongo.errors.DuplicateKeyError:
        return {"error": "Username already exists"}
    message = "User Created Successfully"
    return InlineResponse200(message=message)

