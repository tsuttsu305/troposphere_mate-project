# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.gamelift

from troposphere.gamelift import (
    AutoScalingPolicy as _AutoScalingPolicy,
    CertificateConfiguration as _CertificateConfiguration,
    Destination as _Destination,
    GameProperty as _GameProperty,
    InstanceDefinition as _InstanceDefinition,
    InstanceDefinitions as _InstanceDefinitions,
    IpPermission as _IpPermission,
    LaunchTemplate as _LaunchTemplate,
    PlayerLatencyPolicy as _PlayerLatencyPolicy,
    ResourceCreationLimitPolicy as _ResourceCreationLimitPolicy,
    RoutingStrategy as _RoutingStrategy,
    RuntimeConfiguration as _RuntimeConfiguration,
    S3Location as _S3Location,
    ServerProcess as _ServerProcess,
    Tags as _Tags,
    TargetTrackingConfiguration as _TargetTrackingConfiguration,
    VpcSubnets as _VpcSubnets,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class RoutingStrategy(troposphere.gamelift.RoutingStrategy, Mixin):
    def __init__(self,
                 title=None,
                 FleetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Message=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FleetId=FleetId,
            Message=Message,
            Type=Type,
            **kwargs
        )
        super(RoutingStrategy, self).__init__(**processed_kwargs)


class Alias(troposphere.gamelift.Alias, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoutingStrategy=REQUIRED, # type: _RoutingStrategy
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RoutingStrategy=RoutingStrategy,
            Description=Description,
            **kwargs
        )
        super(Alias, self).__init__(**processed_kwargs)


class S3Location(troposphere.gamelift.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            RoleArn=RoleArn,
            ObjectVersion=ObjectVersion,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class Build(troposphere.gamelift.Build, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 OperatingSystem=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageLocation=NOTHING, # type: _S3Location
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            OperatingSystem=OperatingSystem,
            StorageLocation=StorageLocation,
            Version=Version,
            **kwargs
        )
        super(Build, self).__init__(**processed_kwargs)


class CertificateConfiguration(troposphere.gamelift.CertificateConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CertificateType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateType=CertificateType,
            **kwargs
        )
        super(CertificateConfiguration, self).__init__(**processed_kwargs)


class IpPermission(troposphere.gamelift.IpPermission, Mixin):
    def __init__(self,
                 title=None,
                 FromPort=REQUIRED, # type: int
                 IpRange=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 ToPort=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FromPort=FromPort,
            IpRange=IpRange,
            Protocol=Protocol,
            ToPort=ToPort,
            **kwargs
        )
        super(IpPermission, self).__init__(**processed_kwargs)


class ResourceCreationLimitPolicy(troposphere.gamelift.ResourceCreationLimitPolicy, Mixin):
    def __init__(self,
                 title=None,
                 NewGameSessionsPerCreator=NOTHING, # type: int
                 PolicyPeriodInMinutes=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NewGameSessionsPerCreator=NewGameSessionsPerCreator,
            PolicyPeriodInMinutes=PolicyPeriodInMinutes,
            **kwargs
        )
        super(ResourceCreationLimitPolicy, self).__init__(**processed_kwargs)


class ServerProcess(troposphere.gamelift.ServerProcess, Mixin):
    def __init__(self,
                 title=None,
                 ConcurrentExecutions=REQUIRED, # type: int
                 LaunchPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConcurrentExecutions=ConcurrentExecutions,
            LaunchPath=LaunchPath,
            Parameters=Parameters,
            **kwargs
        )
        super(ServerProcess, self).__init__(**processed_kwargs)


class RuntimeConfiguration(troposphere.gamelift.RuntimeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 GameSessionActivationTimeoutSeconds=NOTHING, # type: int
                 MaxConcurrentGameSessionActivations=NOTHING, # type: int
                 ServerProcesses=NOTHING, # type: List[_ServerProcess]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GameSessionActivationTimeoutSeconds=GameSessionActivationTimeoutSeconds,
            MaxConcurrentGameSessionActivations=MaxConcurrentGameSessionActivations,
            ServerProcesses=ServerProcesses,
            **kwargs
        )
        super(RuntimeConfiguration, self).__init__(**processed_kwargs)


class Fleet(troposphere.gamelift.Fleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EC2InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 BuildId=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateConfiguration=NOTHING, # type: _CertificateConfiguration
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DesiredEC2Instances=NOTHING, # type: int
                 EC2InboundPermissions=NOTHING, # type: List[_IpPermission]
                 FleetType=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceRoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 LogPaths=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaxSize=NOTHING, # type: int
                 MetricGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MinSize=NOTHING, # type: int
                 NewGameSessionProtectionPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerVpcAwsAccountId=NOTHING, # type: Union[str, AWSHelperFn]
                 PeerVpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceCreationLimitPolicy=NOTHING, # type: _ResourceCreationLimitPolicy
                 RuntimeConfiguration=NOTHING, # type: _RuntimeConfiguration
                 ScriptId=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerLaunchParameters=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerLaunchPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EC2InstanceType=EC2InstanceType,
            Name=Name,
            BuildId=BuildId,
            CertificateConfiguration=CertificateConfiguration,
            Description=Description,
            DesiredEC2Instances=DesiredEC2Instances,
            EC2InboundPermissions=EC2InboundPermissions,
            FleetType=FleetType,
            InstanceRoleARN=InstanceRoleARN,
            LogPaths=LogPaths,
            MaxSize=MaxSize,
            MetricGroups=MetricGroups,
            MinSize=MinSize,
            NewGameSessionProtectionPolicy=NewGameSessionProtectionPolicy,
            PeerVpcAwsAccountId=PeerVpcAwsAccountId,
            PeerVpcId=PeerVpcId,
            ResourceCreationLimitPolicy=ResourceCreationLimitPolicy,
            RuntimeConfiguration=RuntimeConfiguration,
            ScriptId=ScriptId,
            ServerLaunchParameters=ServerLaunchParameters,
            ServerLaunchPath=ServerLaunchPath,
            **kwargs
        )
        super(Fleet, self).__init__(**processed_kwargs)


class TargetTrackingConfiguration(troposphere.gamelift.TargetTrackingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 TargetValue=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetValue=TargetValue,
            **kwargs
        )
        super(TargetTrackingConfiguration, self).__init__(**processed_kwargs)


class AutoScalingPolicy(troposphere.gamelift.AutoScalingPolicy, Mixin):
    def __init__(self,
                 title=None,
                 TargetTrackingConfiguration=REQUIRED, # type: _TargetTrackingConfiguration
                 EstimatedInstanceWarmup=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetTrackingConfiguration=TargetTrackingConfiguration,
            EstimatedInstanceWarmup=EstimatedInstanceWarmup,
            **kwargs
        )
        super(AutoScalingPolicy, self).__init__(**processed_kwargs)


class InstanceDefinition(troposphere.gamelift.InstanceDefinition, Mixin):
    def __init__(self,
                 title=None,
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 WeightedCapacity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceType=InstanceType,
            WeightedCapacity=WeightedCapacity,
            **kwargs
        )
        super(InstanceDefinition, self).__init__(**processed_kwargs)


class InstanceDefinitions(troposphere.gamelift.InstanceDefinitions, Mixin):
    def __init__(self,
                 title=None,
                 InstanceDefinitions=NOTHING, # type: List[_InstanceDefinition]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceDefinitions=InstanceDefinitions,
            **kwargs
        )
        super(InstanceDefinitions, self).__init__(**processed_kwargs)


class LaunchTemplate(troposphere.gamelift.LaunchTemplate, Mixin):
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
        super(LaunchTemplate, self).__init__(**processed_kwargs)


class VpcSubnets(troposphere.gamelift.VpcSubnets, Mixin):
    def __init__(self,
                 title=None,
                 VpcSubnets=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VpcSubnets=VpcSubnets,
            **kwargs
        )
        super(VpcSubnets, self).__init__(**processed_kwargs)


class GameServerGroup(troposphere.gamelift.GameServerGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GameServerGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 InstanceDefinitions=REQUIRED, # type: _InstanceDefinitions
                 LaunchTemplate=REQUIRED, # type: _LaunchTemplate
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoScalingPolicy=NOTHING, # type: _AutoScalingPolicy
                 BalancingStrategy=NOTHING, # type: Union[str, AWSHelperFn]
                 DeleteOption=NOTHING, # type: Union[str, AWSHelperFn]
                 GameServerProtectionPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxSize=NOTHING, # type: float
                 MinSize=NOTHING, # type: float
                 Tags=NOTHING, # type: _Tags
                 VpcSubnets=NOTHING, # type: _VpcSubnets
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GameServerGroupName=GameServerGroupName,
            InstanceDefinitions=InstanceDefinitions,
            LaunchTemplate=LaunchTemplate,
            RoleArn=RoleArn,
            AutoScalingPolicy=AutoScalingPolicy,
            BalancingStrategy=BalancingStrategy,
            DeleteOption=DeleteOption,
            GameServerProtectionPolicy=GameServerProtectionPolicy,
            MaxSize=MaxSize,
            MinSize=MinSize,
            Tags=Tags,
            VpcSubnets=VpcSubnets,
            **kwargs
        )
        super(GameServerGroup, self).__init__(**processed_kwargs)


class Destination(troposphere.gamelift.Destination, Mixin):
    def __init__(self,
                 title=None,
                 DestinationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationArn=DestinationArn,
            **kwargs
        )
        super(Destination, self).__init__(**processed_kwargs)


class PlayerLatencyPolicy(troposphere.gamelift.PlayerLatencyPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MaximumIndividualPlayerLatencyMilliseconds=NOTHING, # type: int
                 PolicyDurationSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaximumIndividualPlayerLatencyMilliseconds=MaximumIndividualPlayerLatencyMilliseconds,
            PolicyDurationSeconds=PolicyDurationSeconds,
            **kwargs
        )
        super(PlayerLatencyPolicy, self).__init__(**processed_kwargs)


class GameSessionQueue(troposphere.gamelift.GameSessionQueue, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Destinations=NOTHING, # type: List[_Destination]
                 PlayerLatencyPolicies=NOTHING, # type: List[_PlayerLatencyPolicy]
                 TimeoutInSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Destinations=Destinations,
            PlayerLatencyPolicies=PlayerLatencyPolicies,
            TimeoutInSeconds=TimeoutInSeconds,
            **kwargs
        )
        super(GameSessionQueue, self).__init__(**processed_kwargs)


class GameProperty(troposphere.gamelift.GameProperty, Mixin):
    def __init__(self,
                 title=None,
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(GameProperty, self).__init__(**processed_kwargs)


class MatchmakingConfiguration(troposphere.gamelift.MatchmakingConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AcceptanceRequired=REQUIRED, # type: bool
                 GameSessionQueueArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RequestTimeoutSeconds=REQUIRED, # type: int
                 RuleSetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceptanceTimeoutSeconds=NOTHING, # type: int
                 AdditionalPlayerCount=NOTHING, # type: int
                 BackfillMode=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomEventData=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GameProperties=NOTHING, # type: List[_GameProperty]
                 GameSessionData=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationTarget=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AcceptanceRequired=AcceptanceRequired,
            GameSessionQueueArns=GameSessionQueueArns,
            Name=Name,
            RequestTimeoutSeconds=RequestTimeoutSeconds,
            RuleSetName=RuleSetName,
            AcceptanceTimeoutSeconds=AcceptanceTimeoutSeconds,
            AdditionalPlayerCount=AdditionalPlayerCount,
            BackfillMode=BackfillMode,
            CustomEventData=CustomEventData,
            Description=Description,
            GameProperties=GameProperties,
            GameSessionData=GameSessionData,
            NotificationTarget=NotificationTarget,
            **kwargs
        )
        super(MatchmakingConfiguration, self).__init__(**processed_kwargs)


class MatchmakingRuleSet(troposphere.gamelift.MatchmakingRuleSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleSetBody=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RuleSetBody=RuleSetBody,
            **kwargs
        )
        super(MatchmakingRuleSet, self).__init__(**processed_kwargs)


class Script(troposphere.gamelift.Script, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StorageLocation=REQUIRED, # type: _S3Location
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StorageLocation=StorageLocation,
            Name=Name,
            Version=Version,
            **kwargs
        )
        super(Script, self).__init__(**processed_kwargs)
