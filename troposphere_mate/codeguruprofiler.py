# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codeguruprofiler

from troposphere.codeguruprofiler import (
    Channel as _Channel,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Channel(troposphere.codeguruprofiler.Channel, Mixin):
    def __init__(self,
                 title=None,
                 channelUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 channelId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            channelUri=channelUri,
            channelId=channelId,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class ProfilingGroup(troposphere.codeguruprofiler.ProfilingGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProfilingGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AgentPermissions=NOTHING, # type: dict
                 AnomalyDetectionNotificationConfiguration=NOTHING, # type: List[_Channel]
                 ComputePlatform=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProfilingGroupName=ProfilingGroupName,
            AgentPermissions=AgentPermissions,
            AnomalyDetectionNotificationConfiguration=AnomalyDetectionNotificationConfiguration,
            ComputePlatform=ComputePlatform,
            Tags=Tags,
            **kwargs
        )
        super(ProfilingGroup, self).__init__(**processed_kwargs)
