
import connexion
import six

from swagger_server.models.add_drink_request import AddDrinkRequest  # noqa: E501
from swagger_server.models.edit_drink_request import EditDrinkRequest  # noqa: E501
from swagger_server.models.get_drink_response import GetDrinkResponse  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.purchase_drink_request_inner import PurchaseDrinkRequestInner  # noqa: E501

from swagger_server import util
from swagger_server.services.Drinks_services.add_drink import add_drink as add_drink_service
from swagger_server.services.Drinks_services.purchase_drink import purchase_drink as purchase_drink_service
from swagger_server.services.Drinks_services.get_drink import get_drink as get_drink_service
from swagger_server.services.Drinks_services.edit_drink import edit_drink as edit_drink_service
def add_drink(body=None):  # noqa: E501
    """add drink

    add the drink # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """
    if connexion.request.is_json:
        body = AddDrinkRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return add_drink_service(drink_request=body)


def edit_drink(body=None):  # noqa: E501
    """edit drink

    edit drink # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2004
    """
    if connexion.request.is_json:
        body = EditDrinkRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return edit_drink_service(edit_drink_request=body)


def get_drink(name=None, ingredients=None):  # noqa: E501
    """get the drink

    get drink # noqa: E501

    :param name: 
    :type name: str
    :param ingredients: 
    :type ingredients: List[str]

    :rtype: GetDrinkResponse
    """
    return get_drink_service(name=name, ingredients=ingredients)

def purchase_drink(body=None):  # noqa: E501
    """Purchasee Drink

    Purchase drink # noqa: E501

    :param body:
    :type body: list | bytes

    :rtype: InlineResponse2006
    """
    if connexion.request.is_json:
        body = [PurchaseDrinkRequestInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return purchase_drink_service(drink_request=body)