# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_api_service_status import V1beta1APIServiceStatus


class TestV1beta1APIServiceStatus(unittest.TestCase):
    """ V1beta1APIServiceStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1APIServiceStatus(self):
        """
        Test V1beta1APIServiceStatus
        """
        model = kubernetes.client.models.v1beta1_api_service_status.V1beta1APIServiceStatus()


if __name__ == '__main__':
    unittest.main()
