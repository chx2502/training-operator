# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0rc0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_elastic_policy import KubeflowOrgV1ElasticPolicy  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1ElasticPolicy(unittest.TestCase):
    """KubeflowOrgV1ElasticPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1ElasticPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_elastic_policy.KubeflowOrgV1ElasticPolicy()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1ElasticPolicy(
                max_replicas = 56, 
                max_restarts = 56, 
                metrics = [
                    None
                    ], 
                min_replicas = 56, 
                n_proc_per_node = 56, 
                rdzv_backend = '0', 
                rdzv_conf = [
                    kubeflow_org_v1_rdzv_conf.KubeflowOrgV1RDZVConf(
                        key = '0', 
                        value = '0', )
                    ], 
                rdzv_host = '0', 
                rdzv_id = '0', 
                rdzv_port = 56, 
                standalone = True
            )
        else :
            return KubeflowOrgV1ElasticPolicy(
        )

    def testKubeflowOrgV1ElasticPolicy(self):
        """Test KubeflowOrgV1ElasticPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
