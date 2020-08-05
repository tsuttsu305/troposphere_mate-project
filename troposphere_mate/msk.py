# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.msk

from troposphere.msk import (
    BrokerLogs as _BrokerLogs,
    BrokerNodeGroupInfo as _BrokerNodeGroupInfo,
    ClientAuthentication as _ClientAuthentication,
    CloudWatchLogs as _CloudWatchLogs,
    ConfigurationInfo as _ConfigurationInfo,
    EBSStorageInfo as _EBSStorageInfo,
    EncryptionAtRest as _EncryptionAtRest,
    EncryptionInTransit as _EncryptionInTransit,
    EncryptionInfo as _EncryptionInfo,
    Firehose as _Firehose,
    JmxExporter as _JmxExporter,
    LoggingInfo as _LoggingInfo,
    NodeExporter as _NodeExporter,
    OpenMonitoring as _OpenMonitoring,
    Prometheus as _Prometheus,
    S3 as _S3,
    StorageInfo as _StorageInfo,
    Tls as _Tls,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EBSStorageInfo(troposphere.msk.EBSStorageInfo, Mixin):
    def __init__(self,
                 title=None,
                 VolumeSize=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VolumeSize=VolumeSize,
            **kwargs
        )
        super(EBSStorageInfo, self).__init__(**processed_kwargs)


class StorageInfo(troposphere.msk.StorageInfo, Mixin):
    def __init__(self,
                 title=None,
                 EBSStorageInfo=NOTHING, # type: _EBSStorageInfo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EBSStorageInfo=EBSStorageInfo,
            **kwargs
        )
        super(StorageInfo, self).__init__(**processed_kwargs)


class BrokerNodeGroupInfo(troposphere.msk.BrokerNodeGroupInfo, Mixin):
    def __init__(self,
                 title=None,
                 ClientSubnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 BrokerAZDistribution=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StorageInfo=NOTHING, # type: _StorageInfo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientSubnets=ClientSubnets,
            InstanceType=InstanceType,
            BrokerAZDistribution=BrokerAZDistribution,
            SecurityGroups=SecurityGroups,
            StorageInfo=StorageInfo,
            **kwargs
        )
        super(BrokerNodeGroupInfo, self).__init__(**processed_kwargs)


class Tls(troposphere.msk.Tls, Mixin):
    def __init__(self,
                 title=None,
                 CertificateAuthorityArnList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateAuthorityArnList=CertificateAuthorityArnList,
            **kwargs
        )
        super(Tls, self).__init__(**processed_kwargs)


class ClientAuthentication(troposphere.msk.ClientAuthentication, Mixin):
    def __init__(self,
                 title=None,
                 Tls=NOTHING, # type: _Tls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Tls=Tls,
            **kwargs
        )
        super(ClientAuthentication, self).__init__(**processed_kwargs)


class ConfigurationInfo(troposphere.msk.ConfigurationInfo, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Revision=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            Revision=Revision,
            **kwargs
        )
        super(ConfigurationInfo, self).__init__(**processed_kwargs)


class EncryptionAtRest(troposphere.msk.EncryptionAtRest, Mixin):
    def __init__(self,
                 title=None,
                 DataVolumeKMSKeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataVolumeKMSKeyId=DataVolumeKMSKeyId,
            **kwargs
        )
        super(EncryptionAtRest, self).__init__(**processed_kwargs)


class EncryptionInTransit(troposphere.msk.EncryptionInTransit, Mixin):
    def __init__(self,
                 title=None,
                 ClientBroker=NOTHING, # type: Union[str, AWSHelperFn]
                 InCluster=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientBroker=ClientBroker,
            InCluster=InCluster,
            **kwargs
        )
        super(EncryptionInTransit, self).__init__(**processed_kwargs)


class EncryptionInfo(troposphere.msk.EncryptionInfo, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionAtRest=NOTHING, # type: _EncryptionAtRest
                 EncryptionInTransit=NOTHING, # type: _EncryptionInTransit
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionAtRest=EncryptionAtRest,
            EncryptionInTransit=EncryptionInTransit,
            **kwargs
        )
        super(EncryptionInfo, self).__init__(**processed_kwargs)


class JmxExporter(troposphere.msk.JmxExporter, Mixin):
    def __init__(self,
                 title=None,
                 EnabledInBroker=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EnabledInBroker=EnabledInBroker,
            **kwargs
        )
        super(JmxExporter, self).__init__(**processed_kwargs)


class NodeExporter(troposphere.msk.NodeExporter, Mixin):
    def __init__(self,
                 title=None,
                 EnabledInBroker=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EnabledInBroker=EnabledInBroker,
            **kwargs
        )
        super(NodeExporter, self).__init__(**processed_kwargs)


class Prometheus(troposphere.msk.Prometheus, Mixin):
    def __init__(self,
                 title=None,
                 JmxExporter=NOTHING, # type: _JmxExporter
                 NodeExporter=NOTHING, # type: _NodeExporter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JmxExporter=JmxExporter,
            NodeExporter=NodeExporter,
            **kwargs
        )
        super(Prometheus, self).__init__(**processed_kwargs)


class OpenMonitoring(troposphere.msk.OpenMonitoring, Mixin):
    def __init__(self,
                 title=None,
                 Prometheus=REQUIRED, # type: _Prometheus
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prometheus=Prometheus,
            **kwargs
        )
        super(OpenMonitoring, self).__init__(**processed_kwargs)


class Firehose(troposphere.msk.Firehose, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStream=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStream=DeliveryStream,
            Enabled=Enabled,
            **kwargs
        )
        super(Firehose, self).__init__(**processed_kwargs)


class CloudWatchLogs(troposphere.msk.CloudWatchLogs, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 LogGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            LogGroup=LogGroup,
            **kwargs
        )
        super(CloudWatchLogs, self).__init__(**processed_kwargs)


class S3(troposphere.msk.S3, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            Bucket=Bucket,
            Prefix=Prefix,
            **kwargs
        )
        super(S3, self).__init__(**processed_kwargs)


class BrokerLogs(troposphere.msk.BrokerLogs, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchLogs=NOTHING, # type: _CloudWatchLogs
                 Firehose=NOTHING, # type: _Firehose
                 S3=NOTHING, # type: _S3
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchLogs=CloudWatchLogs,
            Firehose=Firehose,
            S3=S3,
            **kwargs
        )
        super(BrokerLogs, self).__init__(**processed_kwargs)


class LoggingInfo(troposphere.msk.LoggingInfo, Mixin):
    def __init__(self,
                 title=None,
                 BrokerLogs=REQUIRED, # type: _BrokerLogs
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BrokerLogs=BrokerLogs,
            **kwargs
        )
        super(LoggingInfo, self).__init__(**processed_kwargs)


class Cluster(troposphere.msk.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BrokerNodeGroupInfo=REQUIRED, # type: _BrokerNodeGroupInfo
                 ClusterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KafkaVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 NumberOfBrokerNodes=REQUIRED, # type: int
                 ClientAuthentication=NOTHING, # type: _ClientAuthentication
                 ConfigurationInfo=NOTHING, # type: _ConfigurationInfo
                 EncryptionInfo=NOTHING, # type: _EncryptionInfo
                 EnhancedMonitoring=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingInfo=NOTHING, # type: _LoggingInfo
                 OpenMonitoring=NOTHING, # type: _OpenMonitoring
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BrokerNodeGroupInfo=BrokerNodeGroupInfo,
            ClusterName=ClusterName,
            KafkaVersion=KafkaVersion,
            NumberOfBrokerNodes=NumberOfBrokerNodes,
            ClientAuthentication=ClientAuthentication,
            ConfigurationInfo=ConfigurationInfo,
            EncryptionInfo=EncryptionInfo,
            EnhancedMonitoring=EnhancedMonitoring,
            LoggingInfo=LoggingInfo,
            OpenMonitoring=OpenMonitoring,
            Tags=Tags,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)
