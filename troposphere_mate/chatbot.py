# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.chatbot


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class SlackChannelConfiguration(troposphere.chatbot.SlackChannelConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigurationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IamRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SlackChannelId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SlackWorkspaceId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 LoggingLevel=NOTHING, # type: Any
                 SnsTopicArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigurationName=ConfigurationName,
            IamRoleArn=IamRoleArn,
            SlackChannelId=SlackChannelId,
            SlackWorkspaceId=SlackWorkspaceId,
            Arn=Arn,
            LoggingLevel=LoggingLevel,
            SnsTopicArns=SnsTopicArns,
            **kwargs
        )
        super(SlackChannelConfiguration, self).__init__(**processed_kwargs)
