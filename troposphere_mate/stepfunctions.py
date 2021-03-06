# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.stepfunctions

from troposphere.stepfunctions import (
    CloudWatchLogsLogGroup as _CloudWatchLogsLogGroup,
    LogDestination as _LogDestination,
    LoggingConfiguration as _LoggingConfiguration,
    S3Location as _S3Location,
    Tags as _Tags,
    TracingConfiguration as _TracingConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Activity(troposphere.stepfunctions.Activity, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Activity, self).__init__(**processed_kwargs)


class CloudWatchLogsLogGroup(troposphere.stepfunctions.CloudWatchLogsLogGroup, Mixin):
    def __init__(self,
                 title=None,
                 LogGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogGroupArn=LogGroupArn,
            **kwargs
        )
        super(CloudWatchLogsLogGroup, self).__init__(**processed_kwargs)


class LogDestination(troposphere.stepfunctions.LogDestination, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchLogsLogGroup=NOTHING, # type: _CloudWatchLogsLogGroup
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchLogsLogGroup=CloudWatchLogsLogGroup,
            **kwargs
        )
        super(LogDestination, self).__init__(**processed_kwargs)


class LoggingConfiguration(troposphere.stepfunctions.LoggingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Destinations=NOTHING, # type: List[_LogDestination]
                 IncludeExecutionData=NOTHING, # type: bool
                 Level=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destinations=Destinations,
            IncludeExecutionData=IncludeExecutionData,
            Level=Level,
            **kwargs
        )
        super(LoggingConfiguration, self).__init__(**processed_kwargs)


class S3Location(troposphere.stepfunctions.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            Version=Version,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class TracingConfiguration(troposphere.stepfunctions.TracingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            **kwargs
        )
        super(TracingConfiguration, self).__init__(**processed_kwargs)


class StateMachine(troposphere.stepfunctions.StateMachine, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Definition=NOTHING, # type: dict
                 DefinitionS3Location=NOTHING, # type: _S3Location
                 DefinitionString=NOTHING, # type: Union[str, AWSHelperFn]
                 DefinitionSubstitutions=NOTHING, # type: dict
                 LoggingConfiguration=NOTHING, # type: _LoggingConfiguration
                 StateMachineName=NOTHING, # type: Union[str, AWSHelperFn]
                 StateMachineType=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TracingConfiguration=NOTHING, # type: _TracingConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RoleArn=RoleArn,
            Definition=Definition,
            DefinitionS3Location=DefinitionS3Location,
            DefinitionString=DefinitionString,
            DefinitionSubstitutions=DefinitionSubstitutions,
            LoggingConfiguration=LoggingConfiguration,
            StateMachineName=StateMachineName,
            StateMachineType=StateMachineType,
            Tags=Tags,
            TracingConfiguration=TracingConfiguration,
            **kwargs
        )
        super(StateMachine, self).__init__(**processed_kwargs)
