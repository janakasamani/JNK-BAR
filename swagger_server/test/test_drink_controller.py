# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.add_drink_request import AddDrinkRequest  # noqa: E501
from swagger_server.models.edit_drink_request import EditDrinkRequest  # noqa: E501
from swagger_server.models.get_drink_response import GetDrinkResponse  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.purchase_drink_request_inner import PurchaseDrinkRequestInner  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDrinkController(BaseTestCase):
    """DrinkController integration test stubs"""

    def test_add_drink(self):
        """Test case for add_drink

        add drink
        """
        body = AddDrinkRequest()
        response = self.client.open(
            '/api/v3/drink',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_drink(self):
        """Test case for edit_drink

        edit drink
        """
        body = EditDrinkRequest()
        response = self.client.open(
            '/api/v3/drink',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_drink(self):
        """Test case for get_drink

        get the drink
        """
        query_string = [('name', 'name_example'),
                        ('ingredients', 'ingredients_example')]
        response = self.client.open(
            '/api/v3/drink',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_purchase_drink(self):
        """Test case for purchase_drink

        Purchasee Drink
        """
        body = [PurchaseDrinkRequestInner()]
        response = self.client.open(
            '/api/v3/drink/purchase',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
