import connexion
import six

from swagger_server.models.add_user_request import AddUserRequest  # noqa: E501
from swagger_server.models.edit_balance_request import EditBalanceRequest  # noqa: E501
from swagger_server.models.edit_user_request import EditUserRequest  # noqa: E501
from swagger_server.models.get_user_response import GetUserResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.signup_request import SignupRequest  # noqa: E501
from swagger_server import util
from swagger_server.services.user_services.add_user import add_user as add_user_services
from swagger_server.services.user_services.get_user import get_user as get_user_services
from swagger_server.services.user_services.login_user import login_user as login_user_services
from swagger_server.services.user_services.signup_user import signup_user as signup_user_services
from swagger_server.services.user_services.edit_user import edit_user as edit_user_services
from swagger_server.services.user_services.balance_user import balance_user as balance_user_services

def add_user(body=None):  # noqa: E501
    """add the user

    add the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = AddUserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return add_user_services(user_request=body)


def edit_balance(body=None):  # noqa: E501
    """edit user balance

    edit balance # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = EditBalanceRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return balance_user_services(balance_request=body)


def edit_user(body=None):  # noqa: E501
    """edit user

    edit user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = EditUserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return edit_user_services(edit_request=body)


def get_user(username=None):  # noqa: E501
    """get the user

    get user # noqa: E501

    :param username: 
    :type username: str

    :rtype: GetUserResponse
    """
    return get_user_services(username=username)


def login_user(body=None):  # noqa: E501
    """login user

    login user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: LoginResponse
    """
    if connexion.request.is_json:
        body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return login_user_services(login_request=body)


def signup_user(body=None):  # noqa: E501
    """Sign up user

    Sign up user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    if connexion.request.is_json:
        body = SignupRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return signup_user_services(signup_request=body)
