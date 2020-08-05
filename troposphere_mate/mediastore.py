# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.mediastore

from troposphere.mediastore import (
    CorsRule as _CorsRule,
    MetricPolicy as _MetricPolicy,
    MetricPolicyRule as _MetricPolicyRule,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class CorsRule(troposphere.mediastore.CorsRule, Mixin):
    def __init__(self,
                 title=None,
                 AllowedHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AllowedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AllowedOrigins=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ExposeHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaxAgeSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowedHeaders=AllowedHeaders,
            AllowedMethods=AllowedMethods,
            AllowedOrigins=AllowedOrigins,
            ExposeHeaders=ExposeHeaders,
            MaxAgeSeconds=MaxAgeSeconds,
            **kwargs
        )
        super(CorsRule, self).__init__(**processed_kwargs)


class MetricPolicyRule(troposphere.mediastore.MetricPolicyRule, Mixin):
    def __init__(self,
                 title=None,
                 ObjectGroup=REQUIRED, # type: Union[str, AWSHelperFn]
                 ObjectGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ObjectGroup=ObjectGroup,
            ObjectGroupName=ObjectGroupName,
            **kwargs
        )
        super(MetricPolicyRule, self).__init__(**processed_kwargs)


class MetricPolicy(troposphere.mediastore.MetricPolicy, Mixin):
    def __init__(self,
                 title=None,
                 ContainerLevelMetrics=REQUIRED, # type: Any
                 MetricPolicyRules=NOTHING, # type: List[_MetricPolicyRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerLevelMetrics=ContainerLevelMetrics,
            MetricPolicyRules=MetricPolicyRules,
            **kwargs
        )
        super(MetricPolicy, self).__init__(**processed_kwargs)


class Container(troposphere.mediastore.Container, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContainerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessLoggingEnabled=NOTHING, # type: bool
                 CorsPolicy=NOTHING, # type: List[_CorsRule]
                 LifecyclePolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 MetricPolicy=NOTHING, # type: _MetricPolicy
                 Policy=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContainerName=ContainerName,
            AccessLoggingEnabled=AccessLoggingEnabled,
            CorsPolicy=CorsPolicy,
            LifecyclePolicy=LifecyclePolicy,
            MetricPolicy=MetricPolicy,
            Policy=Policy,
            Tags=Tags,
            **kwargs
        )
        super(Container, self).__init__(**processed_kwargs)
