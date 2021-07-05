# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.greengrassv2

from troposphere.greengrassv2 import (
    ComponentPlatform as _ComponentPlatform,
    LambdaContainerParams as _LambdaContainerParams,
    LambdaDeviceMount as _LambdaDeviceMount,
    LambdaEventSource as _LambdaEventSource,
    LambdaExecutionParameters as _LambdaExecutionParameters,
    LambdaFunctionRecipeSource as _LambdaFunctionRecipeSource,
    LambdaLinuxProcessParams as _LambdaLinuxProcessParams,
    LambdaVolumeMount as _LambdaVolumeMount,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ComponentPlatform(troposphere.greengrassv2.ComponentPlatform, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            **kwargs
        )
        super(ComponentPlatform, self).__init__(**processed_kwargs)


class LambdaEventSource(troposphere.greengrassv2.LambdaEventSource, Mixin):
    def __init__(self,
                 title=None,
                 Topic=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Topic=Topic,
            Type=Type,
            **kwargs
        )
        super(LambdaEventSource, self).__init__(**processed_kwargs)


class LambdaDeviceMount(troposphere.greengrassv2.LambdaDeviceMount, Mixin):
    def __init__(self,
                 title=None,
                 AddGroupOwner=NOTHING, # type: bool
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 Permission=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddGroupOwner=AddGroupOwner,
            Path=Path,
            Permission=Permission,
            **kwargs
        )
        super(LambdaDeviceMount, self).__init__(**processed_kwargs)


class LambdaVolumeMount(troposphere.greengrassv2.LambdaVolumeMount, Mixin):
    def __init__(self,
                 title=None,
                 AddGroupOwner=NOTHING, # type: bool
                 DestinationPath=NOTHING, # type: Union[str, AWSHelperFn]
                 Permission=NOTHING, # type: Union[str, AWSHelperFn]
                 SourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddGroupOwner=AddGroupOwner,
            DestinationPath=DestinationPath,
            Permission=Permission,
            SourcePath=SourcePath,
            **kwargs
        )
        super(LambdaVolumeMount, self).__init__(**processed_kwargs)


class LambdaContainerParams(troposphere.greengrassv2.LambdaContainerParams, Mixin):
    def __init__(self,
                 title=None,
                 Devices=NOTHING, # type: List[_LambdaDeviceMount]
                 MemorySizeInKB=NOTHING, # type: int
                 MountROSysfs=NOTHING, # type: bool
                 Volumes=NOTHING, # type: List[_LambdaVolumeMount]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Devices=Devices,
            MemorySizeInKB=MemorySizeInKB,
            MountROSysfs=MountROSysfs,
            Volumes=Volumes,
            **kwargs
        )
        super(LambdaContainerParams, self).__init__(**processed_kwargs)


class LambdaLinuxProcessParams(troposphere.greengrassv2.LambdaLinuxProcessParams, Mixin):
    def __init__(self,
                 title=None,
                 ContainerParams=NOTHING, # type: _LambdaContainerParams
                 IsolationMode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerParams=ContainerParams,
            IsolationMode=IsolationMode,
            **kwargs
        )
        super(LambdaLinuxProcessParams, self).__init__(**processed_kwargs)


class LambdaExecutionParameters(troposphere.greengrassv2.LambdaExecutionParameters, Mixin):
    def __init__(self,
                 title=None,
                 EnvironmentVariables=NOTHING, # type: dict
                 EventSources=NOTHING, # type: List[_LambdaEventSource]
                 ExecArgs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 InputPayloadEncodingType=NOTHING, # type: Union[str, AWSHelperFn]
                 LinuxProcessParams=NOTHING, # type: _LambdaLinuxProcessParams
                 MaxIdleTimeInSeconds=NOTHING, # type: int
                 MaxInstancesCount=NOTHING, # type: int
                 MaxQueueSize=NOTHING, # type: int
                 Pinned=NOTHING, # type: bool
                 StatusTimeoutInSeconds=NOTHING, # type: int
                 TimeoutInSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EnvironmentVariables=EnvironmentVariables,
            EventSources=EventSources,
            ExecArgs=ExecArgs,
            InputPayloadEncodingType=InputPayloadEncodingType,
            LinuxProcessParams=LinuxProcessParams,
            MaxIdleTimeInSeconds=MaxIdleTimeInSeconds,
            MaxInstancesCount=MaxInstancesCount,
            MaxQueueSize=MaxQueueSize,
            Pinned=Pinned,
            StatusTimeoutInSeconds=StatusTimeoutInSeconds,
            TimeoutInSeconds=TimeoutInSeconds,
            **kwargs
        )
        super(LambdaExecutionParameters, self).__init__(**processed_kwargs)


class LambdaFunctionRecipeSource(troposphere.greengrassv2.LambdaFunctionRecipeSource, Mixin):
    def __init__(self,
                 title=None,
                 ComponentDependencies=NOTHING, # type: dict
                 ComponentLambdaParameters=NOTHING, # type: _LambdaExecutionParameters
                 ComponentName=NOTHING, # type: Union[str, AWSHelperFn]
                 ComponentPlatforms=NOTHING, # type: List[_ComponentPlatform]
                 ComponentVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 LambdaArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComponentDependencies=ComponentDependencies,
            ComponentLambdaParameters=ComponentLambdaParameters,
            ComponentName=ComponentName,
            ComponentPlatforms=ComponentPlatforms,
            ComponentVersion=ComponentVersion,
            LambdaArn=LambdaArn,
            **kwargs
        )
        super(LambdaFunctionRecipeSource, self).__init__(**processed_kwargs)


class ComponentVersion(troposphere.greengrassv2.ComponentVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InlineRecipe=NOTHING, # type: Union[str, AWSHelperFn]
                 LambdaFunction=NOTHING, # type: _LambdaFunctionRecipeSource
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InlineRecipe=InlineRecipe,
            LambdaFunction=LambdaFunction,
            Tags=Tags,
            **kwargs
        )
        super(ComponentVersion, self).__init__(**processed_kwargs)
