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
from kubernetes.client.models.v1_pod_anti_affinity import V1PodAntiAffinity


class TestV1PodAntiAffinity(unittest.TestCase):
    """ V1PodAntiAffinity unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1PodAntiAffinity(self):
        """
        Test V1PodAntiAffinity
        """
        model = kubernetes.client.models.v1_pod_anti_affinity.V1PodAntiAffinity()


if __name__ == '__main__':
    unittest.main()
