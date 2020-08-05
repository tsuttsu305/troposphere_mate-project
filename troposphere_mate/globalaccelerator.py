# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.globalaccelerator

from troposphere.globalaccelerator import (
    EndpointConfiguration as _EndpointConfiguration,
    PortRange as _PortRange,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Accelerator(troposphere.globalaccelerator.Accelerator, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 IpAddresses=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 IpAddressType=NOTHING, # type: Any
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Enabled=Enabled,
            IpAddresses=IpAddresses,
            IpAddressType=IpAddressType,
            Tags=Tags,
            **kwargs
        )
        super(Accelerator, self).__init__(**processed_kwargs)


class PortRange(troposphere.globalaccelerator.PortRange, Mixin):
    def __init__(self,
                 title=None,
                 FromPort=REQUIRED, # type: int
                 ToPort=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FromPort=FromPort,
            ToPort=ToPort,
            **kwargs
        )
        super(PortRange, self).__init__(**processed_kwargs)


class Listener(troposphere.globalaccelerator.Listener, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AcceleratorArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PortRanges=REQUIRED, # type: List[_PortRange]
                 ClientAffinity=NOTHING, # type: Any
                 Protocol=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AcceleratorArn=AcceleratorArn,
            PortRanges=PortRanges,
            ClientAffinity=ClientAffinity,
            Protocol=Protocol,
            **kwargs
        )
        super(Listener, self).__init__(**processed_kwargs)


class EndpointConfiguration(troposphere.globalaccelerator.EndpointConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 EndpointId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientIPPreservationEnabled=NOTHING, # type: bool
                 Weight=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointId=EndpointId,
            ClientIPPreservationEnabled=ClientIPPreservationEnabled,
            Weight=Weight,
            **kwargs
        )
        super(EndpointConfiguration, self).__init__(**processed_kwargs)


class EndpointGroup(troposphere.globalaccelerator.EndpointGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointGroupRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 ListenerArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 EndpointConfigurations=NOTHING, # type: List[_EndpointConfiguration]
                 HealthCheckIntervalSeconds=NOTHING, # type: int
                 HealthCheckPath=NOTHING, # type: Union[str, AWSHelperFn]
                 HealthCheckPort=NOTHING, # type: int
                 HealthCheckProtocol=NOTHING, # type: Any
                 ThresholdCount=NOTHING, # type: int
                 TrafficDialPercentage=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointGroupRegion=EndpointGroupRegion,
            ListenerArn=ListenerArn,
            EndpointConfigurations=EndpointConfigurations,
            HealthCheckIntervalSeconds=HealthCheckIntervalSeconds,
            HealthCheckPath=HealthCheckPath,
            HealthCheckPort=HealthCheckPort,
            HealthCheckProtocol=HealthCheckProtocol,
            ThresholdCount=ThresholdCount,
            TrafficDialPercentage=TrafficDialPercentage,
            **kwargs
        )
        super(EndpointGroup, self).__init__(**processed_kwargs)
