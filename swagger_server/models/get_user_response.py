# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class GetUserResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, email: str=None, username: str=None, password: str=None, date_of_birth: datetime=None, role: str=None, user_balance: float=None):  # noqa: E501
        """GetUserResponse - a model defined in Swagger

        :param name: The name of this GetUserResponse.  # noqa: E501
        :type name: str
        :param email: The email of this GetUserResponse.  # noqa: E501
        :type email: str
        :param username: The username of this GetUserResponse.  # noqa: E501
        :type username: str
        :param password: The password of this GetUserResponse.  # noqa: E501
        :type password: str
        :param date_of_birth: The date_of_birth of this GetUserResponse.  # noqa: E501
        :type date_of_birth: datetime
        :param role: The role of this GetUserResponse.  # noqa: E501
        :type role: str
        :param user_balance: The user_balance of this GetUserResponse.  # noqa: E501
        :type user_balance: float
        """
        self.swagger_types = {
            'name': str,
            'email': str,
            'username': str,
            'password': str,
            'date_of_birth': datetime,
            'role': str,
            'user_balance': float
        }

        self.attribute_map = {
            'name': 'name',
            'email': 'email',
            'username': 'username',
            'password': 'password',
            'date_of_birth': 'date of birth',
            'role': 'role',
            'user_balance': 'user balance'
        }
        self._name = name
        self._email = email
        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth
        self._role = role
        self._user_balance = user_balance

    @classmethod
    def from_dict(cls, dikt) -> 'GetUserResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetUserResponse of this GetUserResponse.  # noqa: E501
        :rtype: GetUserResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this GetUserResponse.


        :return: The name of this GetUserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GetUserResponse.


        :param name: The name of this GetUserResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this GetUserResponse.


        :return: The email of this GetUserResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this GetUserResponse.


        :param email: The email of this GetUserResponse.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def username(self) -> str:
        """Gets the username of this GetUserResponse.


        :return: The username of this GetUserResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this GetUserResponse.


        :param username: The username of this GetUserResponse.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this GetUserResponse.


        :return: The password of this GetUserResponse.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this GetUserResponse.


        :param password: The password of this GetUserResponse.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def date_of_birth(self) -> datetime:
        """Gets the date_of_birth of this GetUserResponse.


        :return: The date_of_birth of this GetUserResponse.
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: datetime):
        """Sets the date_of_birth of this GetUserResponse.


        :param date_of_birth: The date_of_birth of this GetUserResponse.
        :type date_of_birth: datetime
        """
        if date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def role(self) -> str:
        """Gets the role of this GetUserResponse.


        :return: The role of this GetUserResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this GetUserResponse.


        :param role: The role of this GetUserResponse.
        :type role: str
        """
        allowed_values = ["customer", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def user_balance(self) -> float:
        """Gets the user_balance of this GetUserResponse.


        :return: The user_balance of this GetUserResponse.
        :rtype: float
        """
        return self._user_balance

    @user_balance.setter
    def user_balance(self, user_balance: float):
        """Sets the user_balance of this GetUserResponse.


        :param user_balance: The user_balance of this GetUserResponse.
        :type user_balance: float
        """
        if user_balance is None:
            raise ValueError("Invalid value for `user_balance`, must not be `None`")  # noqa: E501

        self._user_balance = user_balance