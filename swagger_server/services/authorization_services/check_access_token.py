from helpers.token_helpers import decode_token
import connexion
from connexion.exceptions import ProblemException

def check_access_token(token,required_scopes):
    payload = decode_token(token)
    user_role = payload.get("role")
    allowed_apis = []
    if user_role == "admin":
        allowed_apis = ["add_drink","edit_drink","get_drink","add_user","get_user","edit_user","edit_balance", "purchase_drink"]
    elif user_role == "customer":
        allowed_apis = ["get_drink"]

    api_endpoint = connexion.request.endpoint.split("controller_")[1]
    if api_endpoint in allowed_apis:
        return {'sub': payload.get("id"), 'test_key': payload}
    else:
        raise ProblemException(status=401, title="Unauthorized", detail="You are not allowed to use this API.")

