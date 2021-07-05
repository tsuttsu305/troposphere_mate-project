# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.emrcontainers

from troposphere.emrcontainers import (
    ContainerInfo as _ContainerInfo,
    ContainerProvider as _ContainerProvider,
    EksInfo as _EksInfo,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EksInfo(troposphere.emrcontainers.EksInfo, Mixin):
    def __init__(self,
                 title=None,
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Namespace=Namespace,
            **kwargs
        )
        super(EksInfo, self).__init__(**processed_kwargs)


class ContainerInfo(troposphere.emrcontainers.ContainerInfo, Mixin):
    def __init__(self,
                 title=None,
                 EksInfo=REQUIRED, # type: _EksInfo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EksInfo=EksInfo,
            **kwargs
        )
        super(ContainerInfo, self).__init__(**processed_kwargs)


class ContainerProvider(troposphere.emrcontainers.ContainerProvider, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Info=REQUIRED, # type: _ContainerInfo
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Info=Info,
            Type=Type,
            **kwargs
        )
        super(ContainerProvider, self).__init__(**processed_kwargs)


class VirtualCluster(troposphere.emrcontainers.VirtualCluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContainerProvider=REQUIRED, # type: _ContainerProvider
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContainerProvider=ContainerProvider,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(VirtualCluster, self).__init__(**processed_kwargs)
