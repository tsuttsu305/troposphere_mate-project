# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.devopsguru

from troposphere.devopsguru import (
    CloudFormationCollectionFilter as _CloudFormationCollectionFilter,
    NotificationChannelConfig as _NotificationChannelConfig,
    ResourceCollectionFilter as _ResourceCollectionFilter,
    SnsChannelConfig as _SnsChannelConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class SnsChannelConfig(troposphere.devopsguru.SnsChannelConfig, Mixin):
    def __init__(self,
                 title=None,
                 TopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TopicArn=TopicArn,
            **kwargs
        )
        super(SnsChannelConfig, self).__init__(**processed_kwargs)


class NotificationChannelConfig(troposphere.devopsguru.NotificationChannelConfig, Mixin):
    def __init__(self,
                 title=None,
                 Sns=NOTHING, # type: _SnsChannelConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Sns=Sns,
            **kwargs
        )
        super(NotificationChannelConfig, self).__init__(**processed_kwargs)


class NotificationChannel(troposphere.devopsguru.NotificationChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Config=REQUIRED, # type: _NotificationChannelConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Config=Config,
            **kwargs
        )
        super(NotificationChannel, self).__init__(**processed_kwargs)


class CloudFormationCollectionFilter(troposphere.devopsguru.CloudFormationCollectionFilter, Mixin):
    def __init__(self,
                 title=None,
                 StackNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StackNames=StackNames,
            **kwargs
        )
        super(CloudFormationCollectionFilter, self).__init__(**processed_kwargs)


class ResourceCollectionFilter(troposphere.devopsguru.ResourceCollectionFilter, Mixin):
    def __init__(self,
                 title=None,
                 CloudFormation=NOTHING, # type: _CloudFormationCollectionFilter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudFormation=CloudFormation,
            **kwargs
        )
        super(ResourceCollectionFilter, self).__init__(**processed_kwargs)


class ResourceCollection(troposphere.devopsguru.ResourceCollection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceCollectionFilter=REQUIRED, # type: _ResourceCollectionFilter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceCollectionFilter=ResourceCollectionFilter,
            **kwargs
        )
        super(ResourceCollection, self).__init__(**processed_kwargs)
