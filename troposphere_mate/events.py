# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.events

from troposphere.events import (
    AwsVpcConfiguration as _AwsVpcConfiguration,
    BatchArrayProperties as _BatchArrayProperties,
    BatchParameters as _BatchParameters,
    BatchRetryStrategy as _BatchRetryStrategy,
    Condition as _Condition,
    DeadLetterConfig as _DeadLetterConfig,
    EcsParameters as _EcsParameters,
    HttpParameters as _HttpParameters,
    InputTransformer as _InputTransformer,
    KinesisParameters as _KinesisParameters,
    NetworkConfiguration as _NetworkConfiguration,
    RedshiftDataParameters as _RedshiftDataParameters,
    RetryPolicy as _RetryPolicy,
    RunCommandParameters as _RunCommandParameters,
    RunCommandTarget as _RunCommandTarget,
    SqsParameters as _SqsParameters,
    Target as _Target,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ApiDestination(troposphere.events.ApiDestination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConnectionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 HttpMethod=REQUIRED, # type: Union[str, AWSHelperFn]
                 InvocationEndpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 InvocationRateLimitPerSecond=NOTHING, # type: int
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConnectionArn=ConnectionArn,
            HttpMethod=HttpMethod,
            InvocationEndpoint=InvocationEndpoint,
            Description=Description,
            InvocationRateLimitPerSecond=InvocationRateLimitPerSecond,
            Name=Name,
            **kwargs
        )
        super(ApiDestination, self).__init__(**processed_kwargs)


class Archive(troposphere.events.Archive, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ArchiveName=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EventPattern=NOTHING, # type: dict
                 RetentionDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SourceArn=SourceArn,
            ArchiveName=ArchiveName,
            Description=Description,
            EventPattern=EventPattern,
            RetentionDays=RetentionDays,
            **kwargs
        )
        super(Archive, self).__init__(**processed_kwargs)


class Connection(troposphere.events.Connection, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthParameters=REQUIRED, # type: dict
                 AuthorizationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthParameters=AuthParameters,
            AuthorizationType=AuthorizationType,
            Description=Description,
            Name=Name,
            **kwargs
        )
        super(Connection, self).__init__(**processed_kwargs)


class EventBus(troposphere.events.EventBus, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventSourceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            EventSourceName=EventSourceName,
            **kwargs
        )
        super(EventBus, self).__init__(**processed_kwargs)


class Condition(troposphere.events.Condition, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(Condition, self).__init__(**processed_kwargs)


class EventBusPolicy(troposphere.events.EventBusPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StatementId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Action=NOTHING, # type: Union[str, AWSHelperFn]
                 Condition=NOTHING, # type: _Condition
                 EventBusName=NOTHING, # type: Union[str, AWSHelperFn]
                 Principal=NOTHING, # type: Union[str, AWSHelperFn]
                 Statement=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StatementId=StatementId,
            Action=Action,
            Condition=Condition,
            EventBusName=EventBusName,
            Principal=Principal,
            Statement=Statement,
            **kwargs
        )
        super(EventBusPolicy, self).__init__(**processed_kwargs)


class BatchArrayProperties(troposphere.events.BatchArrayProperties, Mixin):
    def __init__(self,
                 title=None,
                 Size=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Size=Size,
            **kwargs
        )
        super(BatchArrayProperties, self).__init__(**processed_kwargs)


class BatchRetryStrategy(troposphere.events.BatchRetryStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Attempts=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attempts=Attempts,
            **kwargs
        )
        super(BatchRetryStrategy, self).__init__(**processed_kwargs)


class BatchParameters(troposphere.events.BatchParameters, Mixin):
    def __init__(self,
                 title=None,
                 JobDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ArrayProperties=NOTHING, # type: _BatchArrayProperties
                 RetryStrategy=NOTHING, # type: _BatchRetryStrategy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JobDefinition=JobDefinition,
            JobName=JobName,
            ArrayProperties=ArrayProperties,
            RetryStrategy=RetryStrategy,
            **kwargs
        )
        super(BatchParameters, self).__init__(**processed_kwargs)


class DeadLetterConfig(troposphere.events.DeadLetterConfig, Mixin):
    def __init__(self,
                 title=None,
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            **kwargs
        )
        super(DeadLetterConfig, self).__init__(**processed_kwargs)


class AwsVpcConfiguration(troposphere.events.AwsVpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AssignPublicIp=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subnets=Subnets,
            AssignPublicIp=AssignPublicIp,
            SecurityGroups=SecurityGroups,
            **kwargs
        )
        super(AwsVpcConfiguration, self).__init__(**processed_kwargs)


class NetworkConfiguration(troposphere.events.NetworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AwsVpcConfiguration=NOTHING, # type: _AwsVpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsVpcConfiguration=AwsVpcConfiguration,
            **kwargs
        )
        super(NetworkConfiguration, self).__init__(**processed_kwargs)


class EcsParameters(troposphere.events.EcsParameters, Mixin):
    def __init__(self,
                 title=None,
                 TaskDefinitionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Group=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchType=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkConfiguration=NOTHING, # type: _NetworkConfiguration
                 PlatformVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 TaskCount=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TaskDefinitionArn=TaskDefinitionArn,
            Group=Group,
            LaunchType=LaunchType,
            NetworkConfiguration=NetworkConfiguration,
            PlatformVersion=PlatformVersion,
            TaskCount=TaskCount,
            **kwargs
        )
        super(EcsParameters, self).__init__(**processed_kwargs)


class HttpParameters(troposphere.events.HttpParameters, Mixin):
    def __init__(self,
                 title=None,
                 HeaderParameters=NOTHING, # type: dict
                 PathParameterValues=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 QueryStringParameters=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderParameters=HeaderParameters,
            PathParameterValues=PathParameterValues,
            QueryStringParameters=QueryStringParameters,
            **kwargs
        )
        super(HttpParameters, self).__init__(**processed_kwargs)


class InputTransformer(troposphere.events.InputTransformer, Mixin):
    def __init__(self,
                 title=None,
                 InputTemplate=REQUIRED, # type: Union[str, AWSHelperFn]
                 InputPathsMap=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputTemplate=InputTemplate,
            InputPathsMap=InputPathsMap,
            **kwargs
        )
        super(InputTransformer, self).__init__(**processed_kwargs)


class KinesisParameters(troposphere.events.KinesisParameters, Mixin):
    def __init__(self,
                 title=None,
                 PartitionKeyPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PartitionKeyPath=PartitionKeyPath,
            **kwargs
        )
        super(KinesisParameters, self).__init__(**processed_kwargs)


class RedshiftDataParameters(troposphere.events.RedshiftDataParameters, Mixin):
    def __init__(self,
                 title=None,
                 Database=REQUIRED, # type: Union[str, AWSHelperFn]
                 Sql=REQUIRED, # type: Union[str, AWSHelperFn]
                 DbUser=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretManagerArn=NOTHING, # type: Union[str, AWSHelperFn]
                 StatementName=NOTHING, # type: Union[str, AWSHelperFn]
                 WithEvent=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Database=Database,
            Sql=Sql,
            DbUser=DbUser,
            SecretManagerArn=SecretManagerArn,
            StatementName=StatementName,
            WithEvent=WithEvent,
            **kwargs
        )
        super(RedshiftDataParameters, self).__init__(**processed_kwargs)


class RetryPolicy(troposphere.events.RetryPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MaximumEventAgeInSeconds=NOTHING, # type: int
                 MaximumRetryAttempts=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaximumEventAgeInSeconds=MaximumEventAgeInSeconds,
            MaximumRetryAttempts=MaximumRetryAttempts,
            **kwargs
        )
        super(RetryPolicy, self).__init__(**processed_kwargs)


class RunCommandTarget(troposphere.events.RunCommandTarget, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(RunCommandTarget, self).__init__(**processed_kwargs)


class RunCommandParameters(troposphere.events.RunCommandParameters, Mixin):
    def __init__(self,
                 title=None,
                 RunCommandTargets=REQUIRED, # type: List[_RunCommandTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RunCommandTargets=RunCommandTargets,
            **kwargs
        )
        super(RunCommandParameters, self).__init__(**processed_kwargs)


class SqsParameters(troposphere.events.SqsParameters, Mixin):
    def __init__(self,
                 title=None,
                 MessageGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MessageGroupId=MessageGroupId,
            **kwargs
        )
        super(SqsParameters, self).__init__(**processed_kwargs)


class Target(troposphere.events.Target, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 BatchParameters=NOTHING, # type: _BatchParameters
                 DeadLetterConfig=NOTHING, # type: _DeadLetterConfig
                 EcsParameters=NOTHING, # type: _EcsParameters
                 HttpParameters=NOTHING, # type: _HttpParameters
                 Input=NOTHING, # type: Union[str, AWSHelperFn]
                 InputPath=NOTHING, # type: Union[str, AWSHelperFn]
                 InputTransformer=NOTHING, # type: _InputTransformer
                 KinesisParameters=NOTHING, # type: _KinesisParameters
                 RedshiftDataParameters=NOTHING, # type: _RedshiftDataParameters
                 RetryPolicy=NOTHING, # type: _RetryPolicy
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RunCommandParameters=NOTHING, # type: _RunCommandParameters
                 SqsParameters=NOTHING, # type: _SqsParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            Id=Id,
            BatchParameters=BatchParameters,
            DeadLetterConfig=DeadLetterConfig,
            EcsParameters=EcsParameters,
            HttpParameters=HttpParameters,
            Input=Input,
            InputPath=InputPath,
            InputTransformer=InputTransformer,
            KinesisParameters=KinesisParameters,
            RedshiftDataParameters=RedshiftDataParameters,
            RetryPolicy=RetryPolicy,
            RoleArn=RoleArn,
            RunCommandParameters=RunCommandParameters,
            SqsParameters=SqsParameters,
            **kwargs
        )
        super(Target, self).__init__(**processed_kwargs)


class Rule(troposphere.events.Rule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EventBusName=NOTHING, # type: Union[str, AWSHelperFn]
                 EventPattern=NOTHING, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Union[str, AWSHelperFn]
                 Targets=NOTHING, # type: List[_Target]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            EventBusName=EventBusName,
            EventPattern=EventPattern,
            Name=Name,
            RoleArn=RoleArn,
            ScheduleExpression=ScheduleExpression,
            State=State,
            Targets=Targets,
            **kwargs
        )
        super(Rule, self).__init__(**processed_kwargs)
