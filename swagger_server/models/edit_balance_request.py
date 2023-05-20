# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EditBalanceRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, user_balance: float=None):  # noqa: E501
        """EditBalanceRequest - a model defined in Swagger

        :param username: The username of this EditBalanceRequest.  # noqa: E501
        :type username: str
        :param user_balance: The user_balance of this EditBalanceRequest.  # noqa: E501
        :type user_balance: float
        """
        self.swagger_types = {
            'username': str,
            'user_balance': float
        }

        self.attribute_map = {
            'username': 'username',
            'user_balance': 'user balance'
        }
        self._username = username
        self._user_balance = user_balance

    @classmethod
    def from_dict(cls, dikt) -> 'EditBalanceRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EditBalanceRequest of this EditBalanceRequest.  # noqa: E501
        :rtype: EditBalanceRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this EditBalanceRequest.


        :return: The username of this EditBalanceRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this EditBalanceRequest.


        :param username: The username of this EditBalanceRequest.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def user_balance(self) -> float:
        """Gets the user_balance of this EditBalanceRequest.


        :return: The user_balance of this EditBalanceRequest.
        :rtype: float
        """
        return self._user_balance

    @user_balance.setter
    def user_balance(self, user_balance: float):
        """Sets the user_balance of this EditBalanceRequest.


        :param user_balance: The user_balance of this EditBalanceRequest.
        :type user_balance: float
        """
        if user_balance is None:
            raise ValueError("Invalid value for `user_balance`, must not be `None`")  # noqa: E501

        self._user_balance = user_balance
