# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.fms

from troposphere.fms import (
    IEMap as _IEMap,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class IEMap(troposphere.fms.IEMap, Mixin):
    def __init__(self,
                 title=None,
                 ACCOUNT=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ORGUNIT=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACCOUNT=ACCOUNT,
            ORGUNIT=ORGUNIT,
            **kwargs
        )
        super(IEMap, self).__init__(**processed_kwargs)


class Policy(troposphere.fms.Policy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExcludeResourceTags=REQUIRED, # type: bool
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RemediationEnabled=REQUIRED, # type: bool
                 ResourceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceTypeList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SecurityServicePolicyData=REQUIRED, # type: json_checker
                 DeleteAllPolicyResources=NOTHING, # type: bool
                 ExcludeMap=NOTHING, # type: _IEMap
                 IncludeMap=NOTHING, # type: _IEMap
                 ResourceTags=NOTHING, # type: _Tags
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ExcludeResourceTags=ExcludeResourceTags,
            PolicyName=PolicyName,
            RemediationEnabled=RemediationEnabled,
            ResourceType=ResourceType,
            ResourceTypeList=ResourceTypeList,
            SecurityServicePolicyData=SecurityServicePolicyData,
            DeleteAllPolicyResources=DeleteAllPolicyResources,
            ExcludeMap=ExcludeMap,
            IncludeMap=IncludeMap,
            ResourceTags=ResourceTags,
            Tags=Tags,
            **kwargs
        )
        super(Policy, self).__init__(**processed_kwargs)


class NotificationChannel(troposphere.fms.NotificationChannel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SnsRoleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SnsTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SnsRoleName=SnsRoleName,
            SnsTopicArn=SnsTopicArn,
            **kwargs
        )
        super(NotificationChannel, self).__init__(**processed_kwargs)
