# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_orders_response import GetOrdersResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_get_order(self):
        """Test case for get_order

        get the customer orders
        """
        query_string = [('customer_name', 'customer_name_example'),
                        ('date_from', '2013-10-20T19:20:30+01:00'),
                        ('date_to', '2013-10-20T19:20:30+01:00')]
        response = self.client.open(
            '/api/v3/orders',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
