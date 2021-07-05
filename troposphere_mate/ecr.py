# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ecr

from troposphere.ecr import (
    LifecyclePolicy as _LifecyclePolicy,
    ReplicationConfigurationProperty as _ReplicationConfigurationProperty,
    ReplicationDestination as _ReplicationDestination,
    ReplicationRule as _ReplicationRule,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class PublicRepository(troposphere.ecr.PublicRepository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RepositoryCatalogData=NOTHING, # type: dict
                 RepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 RepositoryPolicyText=NOTHING, # type: Union[dict]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RepositoryCatalogData=RepositoryCatalogData,
            RepositoryName=RepositoryName,
            RepositoryPolicyText=RepositoryPolicyText,
            Tags=Tags,
            **kwargs
        )
        super(PublicRepository, self).__init__(**processed_kwargs)


class RegistryPolicy(troposphere.ecr.RegistryPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyText=REQUIRED, # type: Union[dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyText=PolicyText,
            **kwargs
        )
        super(RegistryPolicy, self).__init__(**processed_kwargs)


class ReplicationDestination(troposphere.ecr.ReplicationDestination, Mixin):
    def __init__(self,
                 title=None,
                 Region=REQUIRED, # type: Union[str, AWSHelperFn]
                 RegistryId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Region=Region,
            RegistryId=RegistryId,
            **kwargs
        )
        super(ReplicationDestination, self).__init__(**processed_kwargs)


class ReplicationRule(troposphere.ecr.ReplicationRule, Mixin):
    def __init__(self,
                 title=None,
                 Destinations=REQUIRED, # type: List[_ReplicationDestination]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destinations=Destinations,
            **kwargs
        )
        super(ReplicationRule, self).__init__(**processed_kwargs)


class ReplicationConfigurationProperty(troposphere.ecr.ReplicationConfigurationProperty, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_ReplicationRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(ReplicationConfigurationProperty, self).__init__(**processed_kwargs)


class ReplicationConfiguration(troposphere.ecr.ReplicationConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationConfigurationProperty=REQUIRED, # type: _ReplicationConfigurationProperty
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationConfigurationProperty=ReplicationConfigurationProperty,
            **kwargs
        )
        super(ReplicationConfiguration, self).__init__(**processed_kwargs)


class LifecyclePolicy(troposphere.ecr.LifecyclePolicy, Mixin):
    def __init__(self,
                 title=None,
                 LifecyclePolicyText=NOTHING, # type: Union[str, AWSHelperFn]
                 RegistryId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LifecyclePolicyText=LifecyclePolicyText,
            RegistryId=RegistryId,
            **kwargs
        )
        super(LifecyclePolicy, self).__init__(**processed_kwargs)


class Repository(troposphere.ecr.Repository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ImageScanningConfiguration=NOTHING, # type: dict
                 ImageTagMutability=NOTHING, # type: Union[str, AWSHelperFn]
                 LifecyclePolicy=NOTHING, # type: _LifecyclePolicy
                 RepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 RepositoryPolicyText=NOTHING, # type: Union[dict]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ImageScanningConfiguration=ImageScanningConfiguration,
            ImageTagMutability=ImageTagMutability,
            LifecyclePolicy=LifecyclePolicy,
            RepositoryName=RepositoryName,
            RepositoryPolicyText=RepositoryPolicyText,
            Tags=Tags,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)
