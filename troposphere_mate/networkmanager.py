# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.networkmanager

from troposphere.networkmanager import (
    Bandwidth as _Bandwidth,
    Location as _Location,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class TransitGatewayRegistration(troposphere.networkmanager.TransitGatewayRegistration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransitGatewayArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GlobalNetworkId=GlobalNetworkId,
            TransitGatewayArn=TransitGatewayArn,
            **kwargs
        )
        super(TransitGatewayRegistration, self).__init__(**processed_kwargs)


class Location(troposphere.networkmanager.Location, Mixin):
    def __init__(self,
                 title=None,
                 Address=NOTHING, # type: Union[str, AWSHelperFn]
                 Latitude=NOTHING, # type: Union[str, AWSHelperFn]
                 Longitude=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Address=Address,
            Latitude=Latitude,
            Longitude=Longitude,
            **kwargs
        )
        super(Location, self).__init__(**processed_kwargs)


class Site(troposphere.networkmanager.Site, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Location=NOTHING, # type: _Location
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GlobalNetworkId=GlobalNetworkId,
            Description=Description,
            Location=Location,
            Tags=Tags,
            **kwargs
        )
        super(Site, self).__init__(**processed_kwargs)


class LinkAssociation(troposphere.networkmanager.LinkAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeviceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LinkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeviceId=DeviceId,
            GlobalNetworkId=GlobalNetworkId,
            LinkId=LinkId,
            **kwargs
        )
        super(LinkAssociation, self).__init__(**processed_kwargs)


class Bandwidth(troposphere.networkmanager.Bandwidth, Mixin):
    def __init__(self,
                 title=None,
                 DownloadSpeed=NOTHING, # type: Union[str, AWSHelperFn]
                 UploadSpeed=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DownloadSpeed=DownloadSpeed,
            UploadSpeed=UploadSpeed,
            **kwargs
        )
        super(Bandwidth, self).__init__(**processed_kwargs)


class Link(troposphere.networkmanager.Link, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bandwidth=REQUIRED, # type: _Bandwidth
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SiteId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Provider=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bandwidth=Bandwidth,
            GlobalNetworkId=GlobalNetworkId,
            SiteId=SiteId,
            Description=Description,
            Provider=Provider,
            Tags=Tags,
            Type=Type,
            **kwargs
        )
        super(Link, self).__init__(**processed_kwargs)


class GlobalNetwork(troposphere.networkmanager.GlobalNetwork, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(GlobalNetwork, self).__init__(**processed_kwargs)


class Device(troposphere.networkmanager.Device, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 Model=NOTHING, # type: Union[str, AWSHelperFn]
                 SerialNumber=NOTHING, # type: Union[str, AWSHelperFn]
                 SiteId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Vendor=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GlobalNetworkId=GlobalNetworkId,
            Description=Description,
            Location=Location,
            Model=Model,
            SerialNumber=SerialNumber,
            SiteId=SiteId,
            Tags=Tags,
            Type=Type,
            Vendor=Vendor,
            **kwargs
        )
        super(Device, self).__init__(**processed_kwargs)


class CustomerGatewayAssociation(troposphere.networkmanager.CustomerGatewayAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CustomerGatewayArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeviceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 GlobalNetworkId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LinkId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CustomerGatewayArn=CustomerGatewayArn,
            DeviceId=DeviceId,
            GlobalNetworkId=GlobalNetworkId,
            LinkId=LinkId,
            **kwargs
        )
        super(CustomerGatewayAssociation, self).__init__(**processed_kwargs)
