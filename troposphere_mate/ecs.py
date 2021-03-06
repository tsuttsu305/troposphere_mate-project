# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ecs

from troposphere.ecs import (
    AuthorizationConfig as _AuthorizationConfig,
    AutoScalingGroupProvider as _AutoScalingGroupProvider,
    AwsvpcConfiguration as _AwsvpcConfiguration,
    CapacityProviderStrategy as _CapacityProviderStrategy,
    CapacityProviderStrategyItem as _CapacityProviderStrategyItem,
    ClusterConfiguration as _ClusterConfiguration,
    ClusterSetting as _ClusterSetting,
    ContainerDefinition as _ContainerDefinition,
    ContainerDependency as _ContainerDependency,
    DeploymentCircuitBreaker as _DeploymentCircuitBreaker,
    DeploymentConfiguration as _DeploymentConfiguration,
    DeploymentController as _DeploymentController,
    Device as _Device,
    DockerVolumeConfiguration as _DockerVolumeConfiguration,
    EFSVolumeConfiguration as _EFSVolumeConfiguration,
    Environment as _Environment,
    EnvironmentFile as _EnvironmentFile,
    ExecuteCommandConfiguration as _ExecuteCommandConfiguration,
    ExecuteCommandLogConfiguration as _ExecuteCommandLogConfiguration,
    FirelensConfiguration as _FirelensConfiguration,
    HealthCheck as _HealthCheck,
    Host as _Host,
    HostEntry as _HostEntry,
    InferenceAccelerator as _InferenceAccelerator,
    KernelCapabilities as _KernelCapabilities,
    LinuxParameters as _LinuxParameters,
    LoadBalancer as _LoadBalancer,
    LogConfiguration as _LogConfiguration,
    ManagedScaling as _ManagedScaling,
    MountPoint as _MountPoint,
    NetworkConfiguration as _NetworkConfiguration,
    PlacementConstraint as _PlacementConstraint,
    PlacementStrategy as _PlacementStrategy,
    PortMapping as _PortMapping,
    ProxyConfiguration as _ProxyConfiguration,
    RepositoryCredentials as _RepositoryCredentials,
    ResourceRequirement as _ResourceRequirement,
    Scale as _Scale,
    Secret as _Secret,
    ServiceRegistry as _ServiceRegistry,
    SystemControl as _SystemControl,
    Tags as _Tags,
    Tmpfs as _Tmpfs,
    Ulimit as _Ulimit,
    Volume as _Volume,
    VolumesFrom as _VolumesFrom,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ManagedScaling(troposphere.ecs.ManagedScaling, Mixin):
    def __init__(self,
                 title=None,
                 MaximumScalingStepSize=NOTHING, # type: Any
                 MinimumScalingStepSize=NOTHING, # type: Any
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetCapacity=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaximumScalingStepSize=MaximumScalingStepSize,
            MinimumScalingStepSize=MinimumScalingStepSize,
            Status=Status,
            TargetCapacity=TargetCapacity,
            **kwargs
        )
        super(ManagedScaling, self).__init__(**processed_kwargs)


class AutoScalingGroupProvider(troposphere.ecs.AutoScalingGroupProvider, Mixin):
    def __init__(self,
                 title=None,
                 AutoScalingGroupArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ManagedScaling=NOTHING, # type: _ManagedScaling
                 ManagedTerminationProtection=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutoScalingGroupArn=AutoScalingGroupArn,
            ManagedScaling=ManagedScaling,
            ManagedTerminationProtection=ManagedTerminationProtection,
            **kwargs
        )
        super(AutoScalingGroupProvider, self).__init__(**processed_kwargs)


class CapacityProvider(troposphere.ecs.CapacityProvider, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AutoScalingGroupProvider=REQUIRED, # type: _AutoScalingGroupProvider
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AutoScalingGroupProvider=AutoScalingGroupProvider,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(CapacityProvider, self).__init__(**processed_kwargs)


class CapacityProviderStrategyItem(troposphere.ecs.CapacityProviderStrategyItem, Mixin):
    def __init__(self,
                 title=None,
                 Base=NOTHING, # type: int
                 CapacityProvider=NOTHING, # type: Union[str, AWSHelperFn]
                 Weight=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Base=Base,
            CapacityProvider=CapacityProvider,
            Weight=Weight,
            **kwargs
        )
        super(CapacityProviderStrategyItem, self).__init__(**processed_kwargs)


class ExecuteCommandLogConfiguration(troposphere.ecs.ExecuteCommandLogConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchEncryptionEnabled=NOTHING, # type: bool
                 CloudWatchLogGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 S3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 S3EncryptionEnabled=NOTHING, # type: bool
                 S3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchEncryptionEnabled=CloudWatchEncryptionEnabled,
            CloudWatchLogGroupName=CloudWatchLogGroupName,
            S3BucketName=S3BucketName,
            S3EncryptionEnabled=S3EncryptionEnabled,
            S3KeyPrefix=S3KeyPrefix,
            **kwargs
        )
        super(ExecuteCommandLogConfiguration, self).__init__(**processed_kwargs)


class ExecuteCommandConfiguration(troposphere.ecs.ExecuteCommandConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LogConfiguration=NOTHING, # type: _ExecuteCommandLogConfiguration
                 Logging=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KmsKeyId=KmsKeyId,
            LogConfiguration=LogConfiguration,
            Logging=Logging,
            **kwargs
        )
        super(ExecuteCommandConfiguration, self).__init__(**processed_kwargs)


class ClusterConfiguration(troposphere.ecs.ClusterConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ExecuteCommandConfiguration=NOTHING, # type: _ExecuteCommandConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExecuteCommandConfiguration=ExecuteCommandConfiguration,
            **kwargs
        )
        super(ClusterConfiguration, self).__init__(**processed_kwargs)


class ClusterSetting(troposphere.ecs.ClusterSetting, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(ClusterSetting, self).__init__(**processed_kwargs)


class Cluster(troposphere.ecs.Cluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CapacityProviders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ClusterName=NOTHING, # type: Union[str, AWSHelperFn]
                 ClusterSettings=NOTHING, # type: List[_ClusterSetting]
                 Configuration=NOTHING, # type: _ClusterConfiguration
                 DefaultCapacityProviderStrategy=NOTHING, # type: List[_CapacityProviderStrategyItem]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CapacityProviders=CapacityProviders,
            ClusterName=ClusterName,
            ClusterSettings=ClusterSettings,
            Configuration=Configuration,
            DefaultCapacityProviderStrategy=DefaultCapacityProviderStrategy,
            Tags=Tags,
            **kwargs
        )
        super(Cluster, self).__init__(**processed_kwargs)


class CapacityProviderStrategy(troposphere.ecs.CapacityProviderStrategy, Mixin):
    def __init__(self,
                 title=None,
                 CapacityProvider=REQUIRED, # type: Union[str, AWSHelperFn]
                 Base=NOTHING, # type: int
                 Weight=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CapacityProvider=CapacityProvider,
            Base=Base,
            Weight=Weight,
            **kwargs
        )
        super(CapacityProviderStrategy, self).__init__(**processed_kwargs)


class ClusterCapacityProviderAssociations(troposphere.ecs.ClusterCapacityProviderAssociations, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CapacityProviders=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Cluster=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultCapacityProviderStrategy=REQUIRED, # type: List[_CapacityProviderStrategy]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CapacityProviders=CapacityProviders,
            Cluster=Cluster,
            DefaultCapacityProviderStrategy=DefaultCapacityProviderStrategy,
            **kwargs
        )
        super(ClusterCapacityProviderAssociations, self).__init__(**processed_kwargs)


class PrimaryTaskSet(troposphere.ecs.PrimaryTaskSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Cluster=REQUIRED, # type: Union[str, AWSHelperFn]
                 Service=REQUIRED, # type: Union[str, AWSHelperFn]
                 TaskSetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Cluster=Cluster,
            Service=Service,
            TaskSetId=TaskSetId,
            **kwargs
        )
        super(PrimaryTaskSet, self).__init__(**processed_kwargs)


class LoadBalancer(troposphere.ecs.LoadBalancer, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPort=REQUIRED, # type: int
                 ContainerName=NOTHING, # type: Union[str, AWSHelperFn]
                 LoadBalancerName=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPort=ContainerPort,
            ContainerName=ContainerName,
            LoadBalancerName=LoadBalancerName,
            TargetGroupArn=TargetGroupArn,
            **kwargs
        )
        super(LoadBalancer, self).__init__(**processed_kwargs)


class DeploymentCircuitBreaker(troposphere.ecs.DeploymentCircuitBreaker, Mixin):
    def __init__(self,
                 title=None,
                 Enable=REQUIRED, # type: bool
                 Rollback=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enable=Enable,
            Rollback=Rollback,
            **kwargs
        )
        super(DeploymentCircuitBreaker, self).__init__(**processed_kwargs)


class DeploymentConfiguration(troposphere.ecs.DeploymentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DeploymentCircuitBreaker=NOTHING, # type: _DeploymentCircuitBreaker
                 MaximumPercent=NOTHING, # type: int
                 MinimumHealthyPercent=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeploymentCircuitBreaker=DeploymentCircuitBreaker,
            MaximumPercent=MaximumPercent,
            MinimumHealthyPercent=MinimumHealthyPercent,
            **kwargs
        )
        super(DeploymentConfiguration, self).__init__(**processed_kwargs)


class DeploymentController(troposphere.ecs.DeploymentController, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(DeploymentController, self).__init__(**processed_kwargs)


class PlacementConstraint(troposphere.ecs.PlacementConstraint, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 Expression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Expression=Expression,
            **kwargs
        )
        super(PlacementConstraint, self).__init__(**processed_kwargs)


class PlacementStrategy(troposphere.ecs.PlacementStrategy, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 Field=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Field=Field,
            **kwargs
        )
        super(PlacementStrategy, self).__init__(**processed_kwargs)


class AwsvpcConfiguration(troposphere.ecs.AwsvpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Subnets=REQUIRED, # type: list
                 AssignPublicIp=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subnets=Subnets,
            AssignPublicIp=AssignPublicIp,
            SecurityGroups=SecurityGroups,
            **kwargs
        )
        super(AwsvpcConfiguration, self).__init__(**processed_kwargs)


class NetworkConfiguration(troposphere.ecs.NetworkConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AwsvpcConfiguration=NOTHING, # type: _AwsvpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsvpcConfiguration=AwsvpcConfiguration,
            **kwargs
        )
        super(NetworkConfiguration, self).__init__(**processed_kwargs)


class ServiceRegistry(troposphere.ecs.ServiceRegistry, Mixin):
    def __init__(self,
                 title=None,
                 ContainerName=NOTHING, # type: Union[str, AWSHelperFn]
                 ContainerPort=NOTHING, # type: int
                 Port=NOTHING, # type: int
                 RegistryArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerName=ContainerName,
            ContainerPort=ContainerPort,
            Port=Port,
            RegistryArn=RegistryArn,
            **kwargs
        )
        super(ServiceRegistry, self).__init__(**processed_kwargs)


class Service(troposphere.ecs.Service, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TaskDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 CapacityProviderStrategy=NOTHING, # type: List[_CapacityProviderStrategyItem]
                 Cluster=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentConfiguration=NOTHING, # type: _DeploymentConfiguration
                 DeploymentController=NOTHING, # type: _DeploymentController
                 DesiredCount=NOTHING, # type: int
                 EnableECSManagedTags=NOTHING, # type: bool
                 EnableExecuteCommand=NOTHING, # type: bool
                 HealthCheckGracePeriodSeconds=NOTHING, # type: int
                 LaunchType=NOTHING, # type: Any
                 LoadBalancers=NOTHING, # type: List[_LoadBalancer]
                 NetworkConfiguration=NOTHING, # type: _NetworkConfiguration
                 Role=NOTHING, # type: Union[str, AWSHelperFn]
                 PlacementConstraints=NOTHING, # type: List[_PlacementConstraint]
                 PlacementStrategies=NOTHING, # type: List[_PlacementStrategy]
                 PlatformVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 PropagateTags=NOTHING, # type: Union[str, AWSHelperFn]
                 SchedulingStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceRegistries=NOTHING, # type: List[_ServiceRegistry]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TaskDefinition=TaskDefinition,
            CapacityProviderStrategy=CapacityProviderStrategy,
            Cluster=Cluster,
            DeploymentConfiguration=DeploymentConfiguration,
            DeploymentController=DeploymentController,
            DesiredCount=DesiredCount,
            EnableECSManagedTags=EnableECSManagedTags,
            EnableExecuteCommand=EnableExecuteCommand,
            HealthCheckGracePeriodSeconds=HealthCheckGracePeriodSeconds,
            LaunchType=LaunchType,
            LoadBalancers=LoadBalancers,
            NetworkConfiguration=NetworkConfiguration,
            Role=Role,
            PlacementConstraints=PlacementConstraints,
            PlacementStrategies=PlacementStrategies,
            PlatformVersion=PlatformVersion,
            PropagateTags=PropagateTags,
            SchedulingStrategy=SchedulingStrategy,
            ServiceName=ServiceName,
            ServiceRegistries=ServiceRegistries,
            Tags=Tags,
            **kwargs
        )
        super(Service, self).__init__(**processed_kwargs)


class Environment(troposphere.ecs.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class MountPoint(troposphere.ecs.MountPoint, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceVolume=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReadOnly=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            SourceVolume=SourceVolume,
            ReadOnly=ReadOnly,
            **kwargs
        )
        super(MountPoint, self).__init__(**processed_kwargs)


class PortMapping(troposphere.ecs.PortMapping, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPort=REQUIRED, # type: int
                 HostPort=NOTHING, # type: int
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPort=ContainerPort,
            HostPort=HostPort,
            Protocol=Protocol,
            **kwargs
        )
        super(PortMapping, self).__init__(**processed_kwargs)


class VolumesFrom(troposphere.ecs.VolumesFrom, Mixin):
    def __init__(self,
                 title=None,
                 SourceContainer=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReadOnly=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceContainer=SourceContainer,
            ReadOnly=ReadOnly,
            **kwargs
        )
        super(VolumesFrom, self).__init__(**processed_kwargs)


class HostEntry(troposphere.ecs.HostEntry, Mixin):
    def __init__(self,
                 title=None,
                 Hostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Hostname=Hostname,
            IpAddress=IpAddress,
            **kwargs
        )
        super(HostEntry, self).__init__(**processed_kwargs)


class Device(troposphere.ecs.Device, Mixin):
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


class FirelensConfiguration(troposphere.ecs.FirelensConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Options=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Options=Options,
            **kwargs
        )
        super(FirelensConfiguration, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.ecs.HealthCheck, Mixin):
    def __init__(self,
                 title=None,
                 Command=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Interval=NOTHING, # type: int
                 Retries=NOTHING, # type: int
                 StartPeriod=NOTHING, # type: int
                 Timeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Command=Command,
            Interval=Interval,
            Retries=Retries,
            StartPeriod=StartPeriod,
            Timeout=Timeout,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class KernelCapabilities(troposphere.ecs.KernelCapabilities, Mixin):
    def __init__(self,
                 title=None,
                 Add=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Drop=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Add=Add,
            Drop=Drop,
            **kwargs
        )
        super(KernelCapabilities, self).__init__(**processed_kwargs)


class Tmpfs(troposphere.ecs.Tmpfs, Mixin):
    def __init__(self,
                 title=None,
                 ContainerPath=NOTHING, # type: Union[str, AWSHelperFn]
                 MountOptions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Size=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerPath=ContainerPath,
            MountOptions=MountOptions,
            Size=Size,
            **kwargs
        )
        super(Tmpfs, self).__init__(**processed_kwargs)


class LinuxParameters(troposphere.ecs.LinuxParameters, Mixin):
    def __init__(self,
                 title=None,
                 Capabilities=NOTHING, # type: _KernelCapabilities
                 Devices=NOTHING, # type: List[_Device]
                 InitProcessEnabled=NOTHING, # type: bool
                 SharedMemorySize=NOTHING, # type: int
                 Tmpfs=NOTHING, # type: List[_Tmpfs]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Capabilities=Capabilities,
            Devices=Devices,
            InitProcessEnabled=InitProcessEnabled,
            SharedMemorySize=SharedMemorySize,
            Tmpfs=Tmpfs,
            **kwargs
        )
        super(LinuxParameters, self).__init__(**processed_kwargs)


class Secret(troposphere.ecs.Secret, Mixin):
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


class LogConfiguration(troposphere.ecs.LogConfiguration, Mixin):
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


class RepositoryCredentials(troposphere.ecs.RepositoryCredentials, Mixin):
    def __init__(self,
                 title=None,
                 CredentialsParameter=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CredentialsParameter=CredentialsParameter,
            **kwargs
        )
        super(RepositoryCredentials, self).__init__(**processed_kwargs)


class ResourceRequirement(troposphere.ecs.ResourceRequirement, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(ResourceRequirement, self).__init__(**processed_kwargs)


class SystemControl(troposphere.ecs.SystemControl, Mixin):
    def __init__(self,
                 title=None,
                 Namespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Namespace=Namespace,
            Value=Value,
            **kwargs
        )
        super(SystemControl, self).__init__(**processed_kwargs)


class Ulimit(troposphere.ecs.Ulimit, Mixin):
    def __init__(self,
                 title=None,
                 HardLimit=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SoftLimit=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HardLimit=HardLimit,
            Name=Name,
            SoftLimit=SoftLimit,
            **kwargs
        )
        super(Ulimit, self).__init__(**processed_kwargs)


class ContainerDependency(troposphere.ecs.ContainerDependency, Mixin):
    def __init__(self,
                 title=None,
                 Condition=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Condition=Condition,
            ContainerName=ContainerName,
            **kwargs
        )
        super(ContainerDependency, self).__init__(**processed_kwargs)


class EnvironmentFile(troposphere.ecs.EnvironmentFile, Mixin):
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
        super(EnvironmentFile, self).__init__(**processed_kwargs)


class ContainerDefinition(troposphere.ecs.ContainerDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Command=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Cpu=NOTHING, # type: int
                 DependsOn=NOTHING, # type: List[_ContainerDependency]
                 DisableNetworking=NOTHING, # type: bool
                 DnsSearchDomains=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DnsServers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DockerLabels=NOTHING, # type: dict
                 DockerSecurityOptions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EntryPoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: List[_Environment]
                 EnvironmentFiles=NOTHING, # type: List[_EnvironmentFile]
                 Essential=NOTHING, # type: bool
                 ExtraHosts=NOTHING, # type: List[_HostEntry]
                 FirelensConfiguration=NOTHING, # type: _FirelensConfiguration
                 HealthCheck=NOTHING, # type: _HealthCheck
                 Hostname=NOTHING, # type: Union[str, AWSHelperFn]
                 Image=NOTHING, # type: Union[str, AWSHelperFn]
                 Interactive=NOTHING, # type: bool
                 Links=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 LinuxParameters=NOTHING, # type: _LinuxParameters
                 LogConfiguration=NOTHING, # type: _LogConfiguration
                 Memory=NOTHING, # type: int
                 MemoryReservation=NOTHING, # type: int
                 MountPoints=NOTHING, # type: List[_MountPoint]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 PortMappings=NOTHING, # type: List[_PortMapping]
                 Privileged=NOTHING, # type: bool
                 PseudoTerminal=NOTHING, # type: bool
                 ReadonlyRootFilesystem=NOTHING, # type: bool
                 RepositoryCredentials=NOTHING, # type: _RepositoryCredentials
                 ResourceRequirements=NOTHING, # type: List[_ResourceRequirement]
                 Secrets=NOTHING, # type: List[_Secret]
                 StartTimeout=NOTHING, # type: int
                 StopTimeout=NOTHING, # type: int
                 SystemControls=NOTHING, # type: List[_SystemControl]
                 Ulimits=NOTHING, # type: List[_Ulimit]
                 User=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumesFrom=NOTHING, # type: List[_VolumesFrom]
                 WorkingDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Command=Command,
            Cpu=Cpu,
            DependsOn=DependsOn,
            DisableNetworking=DisableNetworking,
            DnsSearchDomains=DnsSearchDomains,
            DnsServers=DnsServers,
            DockerLabels=DockerLabels,
            DockerSecurityOptions=DockerSecurityOptions,
            EntryPoint=EntryPoint,
            Environment=Environment,
            EnvironmentFiles=EnvironmentFiles,
            Essential=Essential,
            ExtraHosts=ExtraHosts,
            FirelensConfiguration=FirelensConfiguration,
            HealthCheck=HealthCheck,
            Hostname=Hostname,
            Image=Image,
            Interactive=Interactive,
            Links=Links,
            LinuxParameters=LinuxParameters,
            LogConfiguration=LogConfiguration,
            Memory=Memory,
            MemoryReservation=MemoryReservation,
            MountPoints=MountPoints,
            Name=Name,
            PortMappings=PortMappings,
            Privileged=Privileged,
            PseudoTerminal=PseudoTerminal,
            ReadonlyRootFilesystem=ReadonlyRootFilesystem,
            RepositoryCredentials=RepositoryCredentials,
            ResourceRequirements=ResourceRequirements,
            Secrets=Secrets,
            StartTimeout=StartTimeout,
            StopTimeout=StopTimeout,
            SystemControls=SystemControls,
            Ulimits=Ulimits,
            User=User,
            VolumesFrom=VolumesFrom,
            WorkingDirectory=WorkingDirectory,
            **kwargs
        )
        super(ContainerDefinition, self).__init__(**processed_kwargs)


class Host(troposphere.ecs.Host, Mixin):
    def __init__(self,
                 title=None,
                 SourcePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourcePath=SourcePath,
            **kwargs
        )
        super(Host, self).__init__(**processed_kwargs)


class DockerVolumeConfiguration(troposphere.ecs.DockerVolumeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Autoprovision=NOTHING, # type: bool
                 Driver=NOTHING, # type: Union[str, AWSHelperFn]
                 DriverOpts=NOTHING, # type: dict
                 Labels=NOTHING, # type: dict
                 Scope=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Autoprovision=Autoprovision,
            Driver=Driver,
            DriverOpts=DriverOpts,
            Labels=Labels,
            Scope=Scope,
            **kwargs
        )
        super(DockerVolumeConfiguration, self).__init__(**processed_kwargs)


class AuthorizationConfig(troposphere.ecs.AuthorizationConfig, Mixin):
    def __init__(self,
                 title=None,
                 AccessPointId=NOTHING, # type: Union[str, AWSHelperFn]
                 IAM=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessPointId=AccessPointId,
            IAM=IAM,
            **kwargs
        )
        super(AuthorizationConfig, self).__init__(**processed_kwargs)


class EFSVolumeConfiguration(troposphere.ecs.EFSVolumeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 FilesystemId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizationConfig=NOTHING, # type: _AuthorizationConfig
                 RootDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 TransitEncryption=NOTHING, # type: Any
                 TransitEncryptionPort=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FilesystemId=FilesystemId,
            AuthorizationConfig=AuthorizationConfig,
            RootDirectory=RootDirectory,
            TransitEncryption=TransitEncryption,
            TransitEncryptionPort=TransitEncryptionPort,
            **kwargs
        )
        super(EFSVolumeConfiguration, self).__init__(**processed_kwargs)


class Volume(troposphere.ecs.Volume, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DockerVolumeConfiguration=NOTHING, # type: _DockerVolumeConfiguration
                 Host=NOTHING, # type: _Host
                 EFSVolumeConfiguration=NOTHING, # type: _EFSVolumeConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            DockerVolumeConfiguration=DockerVolumeConfiguration,
            Host=Host,
            EFSVolumeConfiguration=EFSVolumeConfiguration,
            **kwargs
        )
        super(Volume, self).__init__(**processed_kwargs)


class InferenceAccelerator(troposphere.ecs.InferenceAccelerator, Mixin):
    def __init__(self,
                 title=None,
                 DeviceName=NOTHING, # type: Union[str, AWSHelperFn]
                 DeviceType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceName=DeviceName,
            DeviceType=DeviceType,
            **kwargs
        )
        super(InferenceAccelerator, self).__init__(**processed_kwargs)


class ProxyConfiguration(troposphere.ecs.ProxyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ContainerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProxyConfigurationProperties=NOTHING, # type: list
                 Type=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerName=ContainerName,
            ProxyConfigurationProperties=ProxyConfigurationProperties,
            Type=Type,
            **kwargs
        )
        super(ProxyConfiguration, self).__init__(**processed_kwargs)


class TaskDefinition(troposphere.ecs.TaskDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ContainerDefinitions=NOTHING, # type: List[_ContainerDefinition]
                 Cpu=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Family=NOTHING, # type: Union[str, AWSHelperFn]
                 InferenceAccelerators=NOTHING, # type: List[_InferenceAccelerator]
                 IpcMode=NOTHING, # type: Union[str, AWSHelperFn]
                 Memory=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkMode=NOTHING, # type: Union[str, AWSHelperFn]
                 PidMode=NOTHING, # type: Union[str, AWSHelperFn]
                 PlacementConstraints=NOTHING, # type: List[_PlacementConstraint]
                 ProxyConfiguration=NOTHING, # type: _ProxyConfiguration
                 RequiresCompatibilities=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 TaskRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Volumes=NOTHING, # type: List[_Volume]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ContainerDefinitions=ContainerDefinitions,
            Cpu=Cpu,
            ExecutionRoleArn=ExecutionRoleArn,
            Family=Family,
            InferenceAccelerators=InferenceAccelerators,
            IpcMode=IpcMode,
            Memory=Memory,
            NetworkMode=NetworkMode,
            PidMode=PidMode,
            PlacementConstraints=PlacementConstraints,
            ProxyConfiguration=ProxyConfiguration,
            RequiresCompatibilities=RequiresCompatibilities,
            Tags=Tags,
            TaskRoleArn=TaskRoleArn,
            Volumes=Volumes,
            **kwargs
        )
        super(TaskDefinition, self).__init__(**processed_kwargs)


class Scale(troposphere.ecs.Scale, Mixin):
    def __init__(self,
                 title=None,
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Unit=Unit,
            Value=Value,
            **kwargs
        )
        super(Scale, self).__init__(**processed_kwargs)


class TaskSet(troposphere.ecs.TaskSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Cluster=REQUIRED, # type: Union[str, AWSHelperFn]
                 Service=REQUIRED, # type: Union[str, AWSHelperFn]
                 TaskDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExternalId=NOTHING, # type: Union[str, AWSHelperFn]
                 LaunchType=NOTHING, # type: Union[str, AWSHelperFn]
                 LoadBalancers=NOTHING, # type: List[_LoadBalancer]
                 NetworkConfiguration=NOTHING, # type: _NetworkConfiguration
                 PlatformVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Scale=NOTHING, # type: _Scale
                 ServiceRegistries=NOTHING, # type: List[_ServiceRegistry]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Cluster=Cluster,
            Service=Service,
            TaskDefinition=TaskDefinition,
            ExternalId=ExternalId,
            LaunchType=LaunchType,
            LoadBalancers=LoadBalancers,
            NetworkConfiguration=NetworkConfiguration,
            PlatformVersion=PlatformVersion,
            Scale=Scale,
            ServiceRegistries=ServiceRegistries,
            **kwargs
        )
        super(TaskSet, self).__init__(**processed_kwargs)
