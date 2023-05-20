import connexion
import six

from swagger_server.models.get_orders_response import GetOrdersResponse  # noqa: E501
from swagger_server import util


def get_order(customer_name=None, date_from=None, date_to=None):  # noqa: E501
    """get the customer orders

    get customer orders # noqa: E501

    :param customer_name: 
    :type customer_name: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str

    :rtype: GetOrdersResponse
    """
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    return 'do some magic!'
