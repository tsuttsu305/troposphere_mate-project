# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.transfer

from troposphere.transfer import (
    EndpointDetails as _EndpointDetails,
    HomeDirectoryMapEntry as _HomeDirectoryMapEntry,
    IdentityProviderDetails as _IdentityProviderDetails,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EndpointDetails(troposphere.transfer.EndpointDetails, Mixin):
    def __init__(self,
                 title=None,
                 AddressAllocationIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VpcEndpointId=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddressAllocationIds=AddressAllocationIds,
            SubnetIds=SubnetIds,
            VpcEndpointId=VpcEndpointId,
            VpcId=VpcId,
            **kwargs
        )
        super(EndpointDetails, self).__init__(**processed_kwargs)


class IdentityProviderDetails(troposphere.transfer.IdentityProviderDetails, Mixin):
    def __init__(self,
                 title=None,
                 InvocationRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 Url=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InvocationRole=InvocationRole,
            Url=Url,
            **kwargs
        )
        super(IdentityProviderDetails, self).__init__(**processed_kwargs)


class Server(troposphere.transfer.Server, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointDetails=NOTHING, # type: _EndpointDetails
                 EndpointType=NOTHING, # type: Union[str, AWSHelperFn]
                 IdentityProviderDetails=NOTHING, # type: _IdentityProviderDetails
                 IdentityProviderType=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingRole=NOTHING, # type: Union[str, AWSHelperFn]
                 Protocols=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Certificate=Certificate,
            EndpointDetails=EndpointDetails,
            EndpointType=EndpointType,
            IdentityProviderDetails=IdentityProviderDetails,
            IdentityProviderType=IdentityProviderType,
            LoggingRole=LoggingRole,
            Protocols=Protocols,
            Tags=Tags,
            **kwargs
        )
        super(Server, self).__init__(**processed_kwargs)


class HomeDirectoryMapEntry(troposphere.transfer.HomeDirectoryMapEntry, Mixin):
    def __init__(self,
                 title=None,
                 Entry=REQUIRED, # type: Union[str, AWSHelperFn]
                 Target=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Entry=Entry,
            Target=Target,
            **kwargs
        )
        super(HomeDirectoryMapEntry, self).__init__(**processed_kwargs)


class User(troposphere.transfer.User, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HomeDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 HomeDirectoryMappings=NOTHING, # type: List[_HomeDirectoryMapEntry]
                 HomeDirectoryType=NOTHING, # type: Any
                 Policy=NOTHING, # type: Union[str, AWSHelperFn]
                 SshPublicKeys=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Role=Role,
            ServerId=ServerId,
            UserName=UserName,
            HomeDirectory=HomeDirectory,
            HomeDirectoryMappings=HomeDirectoryMappings,
            HomeDirectoryType=HomeDirectoryType,
            Policy=Policy,
            SshPublicKeys=SshPublicKeys,
            Tags=Tags,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)
