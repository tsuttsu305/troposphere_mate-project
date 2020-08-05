# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.synthetics

from troposphere.synthetics import (
    Code as _Code,
    RunConfig as _RunConfig,
    Schedule as _Schedule,
    Tags as _Tags,
    VPCConfig as _VPCConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class VPCConfig(troposphere.synthetics.VPCConfig, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            VpcId=VpcId,
            **kwargs
        )
        super(VPCConfig, self).__init__(**processed_kwargs)


class Schedule(troposphere.synthetics.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 Expression=REQUIRED, # type: Union[str, AWSHelperFn]
                 DurationInSeconds=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Expression=Expression,
            DurationInSeconds=DurationInSeconds,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class RunConfig(troposphere.synthetics.RunConfig, Mixin):
    def __init__(self,
                 title=None,
                 TimeoutInSeconds=REQUIRED, # type: int
                 MemoryInMB=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeoutInSeconds=TimeoutInSeconds,
            MemoryInMB=MemoryInMB,
            **kwargs
        )
        super(RunConfig, self).__init__(**processed_kwargs)


class Code(troposphere.synthetics.Code, Mixin):
    def __init__(self,
                 title=None,
                 Handler=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Key=NOTHING, # type: Union[str, AWSHelperFn]
                 S3ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Script=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Handler=Handler,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            S3ObjectVersion=S3ObjectVersion,
            Script=Script,
            **kwargs
        )
        super(Code, self).__init__(**processed_kwargs)


class Canary(troposphere.synthetics.Canary, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ArtifactS3Location=REQUIRED, # type: Union[str, AWSHelperFn]
                 Code=REQUIRED, # type: _Code
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuntimeVersion=REQUIRED, # type: Any
                 Schedule=REQUIRED, # type: _Schedule
                 StartCanaryAfterCreation=REQUIRED, # type: bool
                 FailureRetentionPeriod=NOTHING, # type: int
                 RunConfig=NOTHING, # type: _RunConfig
                 SuccessRetentionPeriod=NOTHING, # type: int
                 Tags=NOTHING, # type: _Tags
                 VPCConfig=NOTHING, # type: _VPCConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ArtifactS3Location=ArtifactS3Location,
            Code=Code,
            ExecutionRoleArn=ExecutionRoleArn,
            Name=Name,
            RuntimeVersion=RuntimeVersion,
            Schedule=Schedule,
            StartCanaryAfterCreation=StartCanaryAfterCreation,
            FailureRetentionPeriod=FailureRetentionPeriod,
            RunConfig=RunConfig,
            SuccessRetentionPeriod=SuccessRetentionPeriod,
            Tags=Tags,
            VPCConfig=VPCConfig,
            **kwargs
        )
        super(Canary, self).__init__(**processed_kwargs)
