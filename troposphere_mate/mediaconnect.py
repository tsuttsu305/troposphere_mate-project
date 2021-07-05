# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.mediaconnect

from troposphere.mediaconnect import (
    Encryption as _Encryption,
    FailoverConfig as _FailoverConfig,
    Source as _Source,
    VpcInterfaceAttachment as _VpcInterfaceAttachment,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class FailoverConfig(troposphere.mediaconnect.FailoverConfig, Mixin):
    def __init__(self,
                 title=None,
                 RecoveryWindow=NOTHING, # type: int
                 State=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RecoveryWindow=RecoveryWindow,
            State=State,
            **kwargs
        )
        super(FailoverConfig, self).__init__(**processed_kwargs)


class Encryption(troposphere.mediaconnect.Encryption, Mixin):
    def __init__(self,
                 title=None,
                 Algorithm=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConstantInitializationVector=NOTHING, # type: Union[str, AWSHelperFn]
                 DeviceId=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 Region=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Url=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Algorithm=Algorithm,
            RoleArn=RoleArn,
            ConstantInitializationVector=ConstantInitializationVector,
            DeviceId=DeviceId,
            KeyType=KeyType,
            Region=Region,
            ResourceId=ResourceId,
            SecretArn=SecretArn,
            Url=Url,
            **kwargs
        )
        super(Encryption, self).__init__(**processed_kwargs)


class Source(troposphere.mediaconnect.Source, Mixin):
    def __init__(self,
                 title=None,
                 Decryption=NOTHING, # type: _Encryption
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EntitlementArn=NOTHING, # type: Union[str, AWSHelperFn]
                 IngestIp=NOTHING, # type: Union[str, AWSHelperFn]
                 IngestPort=NOTHING, # type: int
                 MaxBitrate=NOTHING, # type: int
                 MaxLatency=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceArn=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcInterfaceName=NOTHING, # type: Union[str, AWSHelperFn]
                 WhitelistCidr=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Decryption=Decryption,
            Description=Description,
            EntitlementArn=EntitlementArn,
            IngestIp=IngestIp,
            IngestPort=IngestPort,
            MaxBitrate=MaxBitrate,
            MaxLatency=MaxLatency,
            Name=Name,
            Protocol=Protocol,
            SourceArn=SourceArn,
            StreamId=StreamId,
            VpcInterfaceName=VpcInterfaceName,
            WhitelistCidr=WhitelistCidr,
            **kwargs
        )
        super(Source, self).__init__(**processed_kwargs)


class Flow(troposphere.mediaconnect.Flow, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Source=REQUIRED, # type: _Source
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceFailoverConfig=NOTHING, # type: _FailoverConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Source=Source,
            AvailabilityZone=AvailabilityZone,
            SourceFailoverConfig=SourceFailoverConfig,
            **kwargs
        )
        super(Flow, self).__init__(**processed_kwargs)


class FlowEntitlement(troposphere.mediaconnect.FlowEntitlement, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 FlowArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Subscribers=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 DataTransferSubscriberFeePercent=NOTHING, # type: int
                 Encryption=NOTHING, # type: _Encryption
                 EntitlementStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            FlowArn=FlowArn,
            Name=Name,
            Subscribers=Subscribers,
            DataTransferSubscriberFeePercent=DataTransferSubscriberFeePercent,
            Encryption=Encryption,
            EntitlementStatus=EntitlementStatus,
            **kwargs
        )
        super(FlowEntitlement, self).__init__(**processed_kwargs)


class VpcInterfaceAttachment(troposphere.mediaconnect.VpcInterfaceAttachment, Mixin):
    def __init__(self,
                 title=None,
                 VpcInterfaceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VpcInterfaceName=VpcInterfaceName,
            **kwargs
        )
        super(VpcInterfaceAttachment, self).__init__(**processed_kwargs)


class FlowOutput(troposphere.mediaconnect.FlowOutput, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FlowArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 CidrAllowList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Destination=NOTHING, # type: Union[str, AWSHelperFn]
                 Encryption=NOTHING, # type: _Encryption
                 MaxLatency=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 RemoteId=NOTHING, # type: Union[str, AWSHelperFn]
                 SmoothingLatency=NOTHING, # type: int
                 StreamId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcInterfaceAttachment=NOTHING, # type: _VpcInterfaceAttachment
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FlowArn=FlowArn,
            Protocol=Protocol,
            CidrAllowList=CidrAllowList,
            Description=Description,
            Destination=Destination,
            Encryption=Encryption,
            MaxLatency=MaxLatency,
            Name=Name,
            Port=Port,
            RemoteId=RemoteId,
            SmoothingLatency=SmoothingLatency,
            StreamId=StreamId,
            VpcInterfaceAttachment=VpcInterfaceAttachment,
            **kwargs
        )
        super(FlowOutput, self).__init__(**processed_kwargs)


class FlowSource(troposphere.mediaconnect.FlowSource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Decryption=NOTHING, # type: _Encryption
                 EntitlementArn=NOTHING, # type: Union[str, AWSHelperFn]
                 FlowArn=NOTHING, # type: Union[str, AWSHelperFn]
                 IngestPort=NOTHING, # type: int
                 MaxBitrate=NOTHING, # type: int
                 MaxLatency=NOTHING, # type: int
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcInterfaceName=NOTHING, # type: Union[str, AWSHelperFn]
                 WhitelistCidr=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Name=Name,
            Decryption=Decryption,
            EntitlementArn=EntitlementArn,
            FlowArn=FlowArn,
            IngestPort=IngestPort,
            MaxBitrate=MaxBitrate,
            MaxLatency=MaxLatency,
            Protocol=Protocol,
            StreamId=StreamId,
            VpcInterfaceName=VpcInterfaceName,
            WhitelistCidr=WhitelistCidr,
            **kwargs
        )
        super(FlowSource, self).__init__(**processed_kwargs)


class FlowVpcInterface(troposphere.mediaconnect.FlowVpcInterface, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FlowArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FlowArn=FlowArn,
            Name=Name,
            RoleArn=RoleArn,
            SecurityGroupIds=SecurityGroupIds,
            SubnetId=SubnetId,
            **kwargs
        )
        super(FlowVpcInterface, self).__init__(**processed_kwargs)
