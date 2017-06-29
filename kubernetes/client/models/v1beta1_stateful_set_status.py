# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1StatefulSetStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_replicas=None, current_revision=None, observed_generation=None, ready_replicas=None, replicas=None, update_revision=None, updated_replicas=None):
        """
        V1beta1StatefulSetStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_replicas': 'int',
            'current_revision': 'str',
            'observed_generation': 'int',
            'ready_replicas': 'int',
            'replicas': 'int',
            'update_revision': 'str',
            'updated_replicas': 'int'
        }

        self.attribute_map = {
            'current_replicas': 'currentReplicas',
            'current_revision': 'currentRevision',
            'observed_generation': 'observedGeneration',
            'ready_replicas': 'readyReplicas',
            'replicas': 'replicas',
            'update_revision': 'updateRevision',
            'updated_replicas': 'updatedReplicas'
        }

        self._current_replicas = current_replicas
        self._current_revision = current_revision
        self._observed_generation = observed_generation
        self._ready_replicas = ready_replicas
        self._replicas = replicas
        self._update_revision = update_revision
        self._updated_replicas = updated_replicas

    @property
    def current_replicas(self):
        """
        Gets the current_replicas of this V1beta1StatefulSetStatus.
        currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.

        :return: The current_replicas of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """
        Sets the current_replicas of this V1beta1StatefulSetStatus.
        currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.

        :param current_replicas: The current_replicas of this V1beta1StatefulSetStatus.
        :type: int
        """

        self._current_replicas = current_replicas

    @property
    def current_revision(self):
        """
        Gets the current_revision of this V1beta1StatefulSetStatus.
        currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).

        :return: The current_revision of this V1beta1StatefulSetStatus.
        :rtype: str
        """
        return self._current_revision

    @current_revision.setter
    def current_revision(self, current_revision):
        """
        Sets the current_revision of this V1beta1StatefulSetStatus.
        currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).

        :param current_revision: The current_revision of this V1beta1StatefulSetStatus.
        :type: str
        """

        self._current_revision = current_revision

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1beta1StatefulSetStatus.
        observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.

        :return: The observed_generation of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1beta1StatefulSetStatus.
        observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.

        :param observed_generation: The observed_generation of this V1beta1StatefulSetStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """
        Gets the ready_replicas of this V1beta1StatefulSetStatus.
        readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition.

        :return: The ready_replicas of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """
        Sets the ready_replicas of this V1beta1StatefulSetStatus.
        readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition.

        :param ready_replicas: The ready_replicas of this V1beta1StatefulSetStatus.
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """
        Gets the replicas of this V1beta1StatefulSetStatus.
        replicas is the number of Pods created by the StatefulSet controller.

        :return: The replicas of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1beta1StatefulSetStatus.
        replicas is the number of Pods created by the StatefulSet controller.

        :param replicas: The replicas of this V1beta1StatefulSetStatus.
        :type: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")

        self._replicas = replicas

    @property
    def update_revision(self):
        """
        Gets the update_revision of this V1beta1StatefulSetStatus.
        updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)

        :return: The update_revision of this V1beta1StatefulSetStatus.
        :rtype: str
        """
        return self._update_revision

    @update_revision.setter
    def update_revision(self, update_revision):
        """
        Sets the update_revision of this V1beta1StatefulSetStatus.
        updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)

        :param update_revision: The update_revision of this V1beta1StatefulSetStatus.
        :type: str
        """

        self._update_revision = update_revision

    @property
    def updated_replicas(self):
        """
        Gets the updated_replicas of this V1beta1StatefulSetStatus.
        updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.

        :return: The updated_replicas of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """
        Sets the updated_replicas of this V1beta1StatefulSetStatus.
        updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.

        :param updated_replicas: The updated_replicas of this V1beta1StatefulSetStatus.
        :type: int
        """

        self._updated_replicas = updated_replicas

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1StatefulSetStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
