# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class SignupRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, email: str=None, username: str=None, password: str=None, date_of_birth: datetime=None):  # noqa: E501
        """SignupRequest - a model defined in Swagger

        :param name: The name of this SignupRequest.  # noqa: E501
        :type name: str
        :param email: The email of this SignupRequest.  # noqa: E501
        :type email: str
        :param username: The username of this SignupRequest.  # noqa: E501
        :type username: str
        :param password: The password of this SignupRequest.  # noqa: E501
        :type password: str
        :param date_of_birth: The date_of_birth of this SignupRequest.  # noqa: E501
        :type date_of_birth: datetime
        """
        self.swagger_types = {
            'name': str,
            'email': str,
            'username': str,
            'password': str,
            'date_of_birth': datetime
        }

        self.attribute_map = {
            'name': 'name',
            'email': 'email',
            'username': 'username',
            'password': 'password',
            'date_of_birth': 'date of birth'
        }
        self._name = name
        self._email = email
        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth

    @classmethod
    def from_dict(cls, dikt) -> 'SignupRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SignupRequest of this SignupRequest.  # noqa: E501
        :rtype: SignupRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this SignupRequest.


        :return: The name of this SignupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SignupRequest.


        :param name: The name of this SignupRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this SignupRequest.


        :return: The email of this SignupRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SignupRequest.


        :param email: The email of this SignupRequest.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def username(self) -> str:
        """Gets the username of this SignupRequest.


        :return: The username of this SignupRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this SignupRequest.


        :param username: The username of this SignupRequest.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this SignupRequest.


        :return: The password of this SignupRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this SignupRequest.


        :param password: The password of this SignupRequest.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def date_of_birth(self) -> datetime:
        """Gets the date_of_birth of this SignupRequest.


        :return: The date_of_birth of this SignupRequest.
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: datetime):
        """Sets the date_of_birth of this SignupRequest.


        :param date_of_birth: The date_of_birth of this SignupRequest.
        :type date_of_birth: datetime
        """
        if date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth
