from jose import jwt, JWTError
from dotenv import load_dotenv
from pathlib import Path
import os
import datetime
from connexion.exceptions import ProblemException

def get_token(dictionary):
    dotenv_path = Path('./env')
    load_dotenv(dotenv_path=dotenv_path)

    JWT_SECRET = os.getenv("TOKEN_SECURITY_KEY")
    JWT_LIFETIME_SECONDS = 3600
    JWT_ALGORITHM = 'HS256'

    user_id = str(dictionary.get("_id", ""))
    user_username = dictionary.get("username", "")
    user_role = dictionary.get("role", "")

    payload = { "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_LIFETIME_SECONDS),
                "username": user_username,
                "id": user_id,
                "role": user_role
                }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decode_token(token):
    JWT_SECRET = os.getenv("TOKEN_SECURITY_KEY")
    JWT_ALGORITHM = 'HS256'
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded_token
    except JWTError as e:
        return ProblemException(status=401,title="Unauthorized",detail="Token Invalid Or Expired.")

