# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.batch

from troposphere.batch import (
    ComputeEnvironmentOrder as _ComputeEnvironmentOrder,
    ComputeResources as _ComputeResources,
    ContainerProperties as _ContainerProperties,
    Device as _Device,
    Ec2ConfigurationObject as _Ec2ConfigurationObject,
    Environment as _Environment,
    EvaluateOnExit as _EvaluateOnExit,
    LaunchTemplateSpecification as _LaunchTemplateSpecification,
    LinuxParameters as _LinuxParameters,
    LogConfiguration as _LogConfiguration,
    MountPoints as _MountPoints,
    NodeProperties as _NodeProperties,
    NodeRangeProperty as _NodeRangeProperty,
    ResourceRequirement as _ResourceRequirement,
    RetryStrategy as _RetryStrategy,
    Secret as _Secret,
    Timeout as _Timeout,
    Tmpfs as _Tmpfs,
    Ulimit as _Ulimit,
    Volumes as _Volumes,
    VolumesHost as _VolumesHost,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Ec2ConfigurationObject(troposphere.batch.Ec2ConfigurationObject, Mixin):
    def __init__(self,
                 title=None,
                 ImageType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageIdOverride=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageType=ImageType,
            ImageIdOverride=ImageIdOverride,
            **kwargs
        )
        super(Ec2ConfigurationObject, self).__init__(**processed_kwargs)


class LaunchTemplateSpecification(troposphere.batch.LaunchTemplateSpecification, Mixin):
    def __init__(self,
                 title=None,
                 LaunchTemplateId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchTemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LaunchTemplateId=LaunchTemplateId,
            LaunchTemplateName=LaunchTemplateName,
            Version=Version,
            **kwargs
        )
        super(LaunchTemplateSpecification, self).__init__(**processed_kwargs)


class ComputeResources(troposphere.batch.ComputeResources, Mixin):
    def __init__(self,
                 title=None,
                 MaxvCpus=REQUIRED, # type: int
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllocationStrategy=NOTHING, # type: Any
                 BidPercentage=NOTHING, # type: int
                 DesiredvCpus=NOTHING, # type: int
                 Ec2Configuration=NOTHING, # type: List[_Ec2ConfigurationObject]
                 Ec2KeyPair=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageId=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceRole=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 LaunchTemplate=NOTHING, # type: _LaunchTemplateSpecification
                 MinvCpus=NOTHING, # type: int
                 PlacementGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SpotIamFleetRole=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxvCpus=MaxvCpus,
            Subnets=Subnets,
            Type=Type,
            AllocationStrategy=AllocationStrategy,
            BidPercentage=BidPercentage,
            DesiredvCpus=DesiredvCpus,
            Ec2Configuration=Ec2Configuration,
            Ec2KeyPair=Ec2KeyPair,
            ImageId=ImageId,
            InstanceRole=InstanceRole,
            InstanceTypes=InstanceTypes,
            LaunchTemplate=LaunchTemplate,
            MinvCpus=MinvCpus,
            PlacementGroup=PlacementGroup,
            SecurityGroupIds=SecurityGroupIds,
            SpotIamFleetRole=SpotIamFleetRole,
            Tags=Tags,
            **kwargs
        )
        super(ComputeResources, self).__init__(**processed_kwargs)


class Device(troposphere.batch.Device, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 HostPath=NOTHING, # type: Union[str, AWSHelperFn]
                 Permissions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            HostPath=HostPath,
            Permissions=Permissions,
            **kwargs
        )
        super(Device, self).__init__(**processed_kwargs)


class Tmpfs(troposphere.batch.Tmpfs, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 Size=REQUIRED, # type: int
                 MountOptions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            Size=Size,
            MountOptions=MountOptions,
            **kwargs
        )
        super(Tmpfs, self).__init__(**processed_kwargs)


class LinuxParameters(troposphere.batch.LinuxParameters, Mixin):
    def __init__(self,
                 title=None,
                 Devices=NOTHING, # type: List[_Device]
                 InitProcessEnabled=NOTHING, # type: bool
                 MaxSwap=NOTHING, # type: int
                 SharedMemorySize=NOTHING, # type: int
                 Swappiness=NOTHING, # type: int
                 Tmpfs=NOTHING, # type: List[_Tmpfs]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Devices=Devices,
            InitProcessEnabled=InitProcessEnabled,
            MaxSwap=MaxSwap,
            SharedMemorySize=SharedMemorySize,
            Swappiness=Swappiness,
            Tmpfs=Tmpfs,
            **kwargs
        )
        super(LinuxParameters, self).__init__(**processed_kwargs)


class Secret(troposphere.batch.Secret, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ValueFrom=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            ValueFrom=ValueFrom,
            **kwargs
        )
        super(Secret, self).__init__(**processed_kwargs)


class LogConfiguration(troposphere.batch.LogConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 LogDriver=REQUIRED, # type: Union[str, AWSHelperFn]
                 Options=NOTHING, # type: dict
                 SecretOptions=NOTHING, # type: List[_Secret]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogDriver=LogDriver,
            Options=Options,
            SecretOptions=SecretOptions,
            **kwargs
        )
        super(LogConfiguration, self).__init__(**processed_kwargs)


class MountPoints(troposphere.batch.MountPoints, Mixin):
    def __init__(self,
                 title=None,
                 ReadOnly=NOTHING, # type: bool
                 SourceVolume=NOTHING, # type: Union[str, AWSHelperFn]
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReadOnly=ReadOnly,
            SourceVolume=SourceVolume,
            ContainerPath=ContainerPath,
            **kwargs
        )
        super(MountPoints, self).__init__(**processed_kwargs)


class VolumesHost(troposphere.batch.VolumesHost, Mixin):
    def __init__(self,
                 title=None,
                 SourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourcePath=SourcePath,
            **kwargs
        )
        super(VolumesHost, self).__init__(**processed_kwargs)


class Volumes(troposphere.batch.Volumes, Mixin):
    def __init__(self,
                 title=None,
                 Host=NOTHING, # type: _VolumesHost
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Host=Host,
            Name=Name,
            **kwargs
        )
        super(Volumes, self).__init__(**processed_kwargs)


class Environment(troposphere.batch.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            Name=Name,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class ResourceRequirement(troposphere.batch.ResourceRequirement, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(ResourceRequirement, self).__init__(**processed_kwargs)


class Ulimit(troposphere.batch.Ulimit, Mixin):
    def __init__(self,
                 title=None,
                 SoftLimit=REQUIRED, # type: int
                 HardLimit=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SoftLimit=SoftLimit,
            HardLimit=HardLimit,
            Name=Name,
            **kwargs
        )
        super(Ulimit, self).__init__(**processed_kwargs)


class ContainerProperties(troposphere.batch.ContainerProperties, Mixin):
    def __init__(self,
                 title=None,
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 Memory=REQUIRED, # type: int
                 Vcpus=REQUIRED, # type: int
                 Command=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: List[_Environment]
                 ExecutionRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 JobRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 LinuxParameters=NOTHING, # type: _LinuxParameters
                 LogConfiguration=NOTHING, # type: _LogConfiguration
                 MountPoints=NOTHING, # type: List[_MountPoints]
                 Privileged=NOTHING, # type: bool
                 ReadonlyRootFilesystem=NOTHING, # type: bool
                 ResourceRequirements=NOTHING, # type: List[_ResourceRequirement]
                 Secrets=NOTHING, # type: List[_Secret]
                 Ulimits=NOTHING, # type: List[_Ulimit]
                 User=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: List[_Volumes]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Image=Image,
            Memory=Memory,
            Vcpus=Vcpus,
            Command=Command,
            Environment=Environment,
            ExecutionRoleArn=ExecutionRoleArn,
            InstanceType=InstanceType,
            JobRoleArn=JobRoleArn,
            LinuxParameters=LinuxParameters,
            LogConfiguration=LogConfiguration,
            MountPoints=MountPoints,
            Privileged=Privileged,
            ReadonlyRootFilesystem=ReadonlyRootFilesystem,
            ResourceRequirements=ResourceRequirements,
            Secrets=Secrets,
            Ulimits=Ulimits,
            User=User,
            Volumes=Volumes,
            **kwargs
        )
        super(ContainerProperties, self).__init__(**processed_kwargs)


class NodeRangeProperty(troposphere.batch.NodeRangeProperty, Mixin):
    def __init__(self,
                 title=None,
                 TargetNodes=REQUIRED, # type: Union[str, AWSHelperFn]
                 Container=NOTHING, # type: _ContainerProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetNodes=TargetNodes,
            Container=Container,
            **kwargs
        )
        super(NodeRangeProperty, self).__init__(**processed_kwargs)


class NodeProperties(troposphere.batch.NodeProperties, Mixin):
    def __init__(self,
                 title=None,
                 MainNode=REQUIRED, # type: int
                 NodeRangeProperties=REQUIRED, # type: List[_NodeRangeProperty]
                 NumNodes=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MainNode=MainNode,
            NodeRangeProperties=NodeRangeProperties,
            NumNodes=NumNodes,
            **kwargs
        )
        super(NodeProperties, self).__init__(**processed_kwargs)


class EvaluateOnExit(troposphere.batch.EvaluateOnExit, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 OnExitCode=NOTHING, # type: Union[str, AWSHelperFn]
                 OnReason=NOTHING, # type: Union[str, AWSHelperFn]
                 OnStatusReason=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            OnExitCode=OnExitCode,
            OnReason=OnReason,
            OnStatusReason=OnStatusReason,
            **kwargs
        )
        super(EvaluateOnExit, self).__init__(**processed_kwargs)


class RetryStrategy(troposphere.batch.RetryStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Attempts=NOTHING, # type: int
                 EvaluateOnExit=NOTHING, # type: List[_EvaluateOnExit]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attempts=Attempts,
            EvaluateOnExit=EvaluateOnExit,
            **kwargs
        )
        super(RetryStrategy, self).__init__(**processed_kwargs)


class Timeout(troposphere.batch.Timeout, Mixin):
    def __init__(self,
                 title=None,
                 AttemptDurationSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttemptDurationSeconds=AttemptDurationSeconds,
            **kwargs
        )
        super(Timeout, self).__init__(**processed_kwargs)


class JobDefinition(troposphere.batch.JobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerProperties=NOTHING, # type: _ContainerProperties
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 NodeProperties=NOTHING, # type: _NodeProperties
                 Parameters=NOTHING, # type: dict
                 PlatformCapabilities=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PropagateTags=NOTHING, # type: bool
                 RetryStrategy=NOTHING, # type: _RetryStrategy
                 Tags=NOTHING, # type: dict
                 Timeout=NOTHING, # type: _Timeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            ContainerProperties=ContainerProperties,
            JobDefinitionName=JobDefinitionName,
            NodeProperties=NodeProperties,
            Parameters=Parameters,
            PlatformCapabilities=PlatformCapabilities,
            PropagateTags=PropagateTags,
            RetryStrategy=RetryStrategy,
            Tags=Tags,
            Timeout=Timeout,
            **kwargs
        )
        super(JobDefinition, self).__init__(**processed_kwargs)


class ComputeEnvironment(troposphere.batch.ComputeEnvironment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 ComputeResources=REQUIRED, # type: _ComputeResources
                 ComputeEnvironmentName=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Any
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Type=Type,
            ServiceRole=ServiceRole,
            ComputeResources=ComputeResources,
            ComputeEnvironmentName=ComputeEnvironmentName,
            State=State,
            Tags=Tags,
            **kwargs
        )
        super(ComputeEnvironment, self).__init__(**processed_kwargs)


class ComputeEnvironmentOrder(troposphere.batch.ComputeEnvironmentOrder, Mixin):
    def __init__(self,
                 title=None,
                 ComputeEnvironment=REQUIRED, # type: Union[str, AWSHelperFn]
                 Order=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeEnvironment=ComputeEnvironment,
            Order=Order,
            **kwargs
        )
        super(ComputeEnvironmentOrder, self).__init__(**processed_kwargs)


class JobQueue(troposphere.batch.JobQueue, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ComputeEnvironmentOrder=REQUIRED, # type: List[_ComputeEnvironmentOrder]
                 Priority=REQUIRED, # type: int
                 State=NOTHING, # type: Any
                 JobQueueName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ComputeEnvironmentOrder=ComputeEnvironmentOrder,
            Priority=Priority,
            State=State,
            JobQueueName=JobQueueName,
            Tags=Tags,
            **kwargs
        )
        super(JobQueue, self).__init__(**processed_kwargs)
