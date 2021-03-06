# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.awslambda

from troposphere.awslambda import (
    AliasRoutingConfiguration as _AliasRoutingConfiguration,
    AllowedPublishers as _AllowedPublishers,
    Code as _Code,
    CodeSigningPolicies as _CodeSigningPolicies,
    Content as _Content,
    DeadLetterConfig as _DeadLetterConfig,
    DestinationConfig as _DestinationConfig,
    Endpoints as _Endpoints,
    Environment as _Environment,
    FileSystemConfig as _FileSystemConfig,
    ImageConfig as _ImageConfig,
    OnFailure as _OnFailure,
    OnSuccess as _OnSuccess,
    ProvisionedConcurrencyConfiguration as _ProvisionedConcurrencyConfiguration,
    SelfManagedEventSource as _SelfManagedEventSource,
    SourceAccessConfiguration as _SourceAccessConfiguration,
    Tags as _Tags,
    TracingConfig as _TracingConfig,
    VPCConfig as _VPCConfig,
    VersionWeight as _VersionWeight,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Code(troposphere.awslambda.Code, Mixin):
    def __init__(self,
                 title=None,
                 ImageUri=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Bucket=NOTHING, # type: Union[str, AWSHelperFn]
                 S3Key=NOTHING, # type: Union[str, AWSHelperFn]
                 S3ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 ZipFile=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageUri=ImageUri,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            S3ObjectVersion=S3ObjectVersion,
            ZipFile=ZipFile,
            **kwargs
        )
        super(Code, self).__init__(**processed_kwargs)


class ImageConfig(troposphere.awslambda.ImageConfig, Mixin):
    def __init__(self,
                 title=None,
                 Command=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EntryPoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 WorkingDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Command=Command,
            EntryPoint=EntryPoint,
            WorkingDirectory=WorkingDirectory,
            **kwargs
        )
        super(ImageConfig, self).__init__(**processed_kwargs)


class VPCConfig(troposphere.awslambda.VPCConfig, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=REQUIRED, # type: list
                 SubnetIds=REQUIRED, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(VPCConfig, self).__init__(**processed_kwargs)


class OnFailure(troposphere.awslambda.OnFailure, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            **kwargs
        )
        super(OnFailure, self).__init__(**processed_kwargs)


class OnSuccess(troposphere.awslambda.OnSuccess, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            **kwargs
        )
        super(OnSuccess, self).__init__(**processed_kwargs)


class DestinationConfig(troposphere.awslambda.DestinationConfig, Mixin):
    def __init__(self,
                 title=None,
                 OnFailure=NOTHING, # type: _OnFailure
                 OnSuccess=NOTHING, # type: _OnSuccess
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OnFailure=OnFailure,
            OnSuccess=OnSuccess,
            **kwargs
        )
        super(DestinationConfig, self).__init__(**processed_kwargs)


class EventInvokeConfig(troposphere.awslambda.EventInvokeConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Qualifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationConfig=NOTHING, # type: _DestinationConfig
                 MaximumEventAgeInSeconds=NOTHING, # type: int
                 MaximumRetryAttempts=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            Qualifier=Qualifier,
            DestinationConfig=DestinationConfig,
            MaximumEventAgeInSeconds=MaximumEventAgeInSeconds,
            MaximumRetryAttempts=MaximumRetryAttempts,
            **kwargs
        )
        super(EventInvokeConfig, self).__init__(**processed_kwargs)


class Endpoints(troposphere.awslambda.Endpoints, Mixin):
    def __init__(self,
                 title=None,
                 KafkaBootstrapServers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KafkaBootstrapServers=KafkaBootstrapServers,
            **kwargs
        )
        super(Endpoints, self).__init__(**processed_kwargs)


class SelfManagedEventSource(troposphere.awslambda.SelfManagedEventSource, Mixin):
    def __init__(self,
                 title=None,
                 Endpoints=NOTHING, # type: _Endpoints
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Endpoints=Endpoints,
            **kwargs
        )
        super(SelfManagedEventSource, self).__init__(**processed_kwargs)


class SourceAccessConfiguration(troposphere.awslambda.SourceAccessConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 URI=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            URI=URI,
            **kwargs
        )
        super(SourceAccessConfiguration, self).__init__(**processed_kwargs)


class EventSourceMapping(troposphere.awslambda.EventSourceMapping, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BatchSize=NOTHING, # type: int
                 BisectBatchOnFunctionError=NOTHING, # type: bool
                 DestinationConfig=NOTHING, # type: _DestinationConfig
                 Enabled=NOTHING, # type: bool
                 EventSourceArn=NOTHING, # type: Union[str, AWSHelperFn]
                 FunctionResponseTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaximumBatchingWindowInSeconds=NOTHING, # type: int
                 MaximumRecordAgeInSeconds=NOTHING, # type: int
                 MaximumRetryAttempts=NOTHING, # type: int
                 ParallelizationFactor=NOTHING, # type: int
                 PartialBatchResponse=NOTHING, # type: bool
                 Queues=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SelfManagedEventSource=NOTHING, # type: _SelfManagedEventSource
                 SourceAccessConfigurations=NOTHING, # type: List[_SourceAccessConfiguration]
                 StartingPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 Topics=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TumblingWindowInSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            BatchSize=BatchSize,
            BisectBatchOnFunctionError=BisectBatchOnFunctionError,
            DestinationConfig=DestinationConfig,
            Enabled=Enabled,
            EventSourceArn=EventSourceArn,
            FunctionResponseTypes=FunctionResponseTypes,
            MaximumBatchingWindowInSeconds=MaximumBatchingWindowInSeconds,
            MaximumRecordAgeInSeconds=MaximumRecordAgeInSeconds,
            MaximumRetryAttempts=MaximumRetryAttempts,
            ParallelizationFactor=ParallelizationFactor,
            PartialBatchResponse=PartialBatchResponse,
            Queues=Queues,
            SelfManagedEventSource=SelfManagedEventSource,
            SourceAccessConfigurations=SourceAccessConfigurations,
            StartingPosition=StartingPosition,
            Topics=Topics,
            TumblingWindowInSeconds=TumblingWindowInSeconds,
            **kwargs
        )
        super(EventSourceMapping, self).__init__(**processed_kwargs)


class DeadLetterConfig(troposphere.awslambda.DeadLetterConfig, Mixin):
    def __init__(self,
                 title=None,
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetArn=TargetArn,
            **kwargs
        )
        super(DeadLetterConfig, self).__init__(**processed_kwargs)


class Environment(troposphere.awslambda.Environment, Mixin):
    def __init__(self,
                 title=None,
                 Variables=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Variables=Variables,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class FileSystemConfig(troposphere.awslambda.FileSystemConfig, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 LocalMountPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            LocalMountPath=LocalMountPath,
            **kwargs
        )
        super(FileSystemConfig, self).__init__(**processed_kwargs)


class TracingConfig(troposphere.awslambda.TracingConfig, Mixin):
    def __init__(self,
                 title=None,
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Mode=Mode,
            **kwargs
        )
        super(TracingConfig, self).__init__(**processed_kwargs)


class Function(troposphere.awslambda.Function, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Code=REQUIRED, # type: _Code
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DeadLetterConfig=NOTHING, # type: _DeadLetterConfig
                 Environment=NOTHING, # type: _Environment
                 FileSystemConfigs=NOTHING, # type: List[_FileSystemConfig]
                 FunctionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Handler=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageConfig=NOTHING, # type: _ImageConfig
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MemorySize=NOTHING, # type: Any
                 Layers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PackageType=NOTHING, # type: Any
                 ReservedConcurrentExecutions=NOTHING, # type: int
                 Runtime=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Timeout=NOTHING, # type: int
                 TracingConfig=NOTHING, # type: _TracingConfig
                 VpcConfig=NOTHING, # type: _VPCConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Code=Code,
            Role=Role,
            Description=Description,
            DeadLetterConfig=DeadLetterConfig,
            Environment=Environment,
            FileSystemConfigs=FileSystemConfigs,
            FunctionName=FunctionName,
            Handler=Handler,
            ImageConfig=ImageConfig,
            KmsKeyArn=KmsKeyArn,
            MemorySize=MemorySize,
            Layers=Layers,
            PackageType=PackageType,
            ReservedConcurrentExecutions=ReservedConcurrentExecutions,
            Runtime=Runtime,
            Tags=Tags,
            Timeout=Timeout,
            TracingConfig=TracingConfig,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Function, self).__init__(**processed_kwargs)


class Permission(troposphere.awslambda.Permission, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventSourceToken=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceAccount=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            FunctionName=FunctionName,
            Principal=Principal,
            EventSourceToken=EventSourceToken,
            SourceAccount=SourceAccount,
            SourceArn=SourceArn,
            **kwargs
        )
        super(Permission, self).__init__(**processed_kwargs)


class VersionWeight(troposphere.awslambda.VersionWeight, Mixin):
    def __init__(self,
                 title=None,
                 FunctionVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionWeight=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionVersion=FunctionVersion,
            FunctionWeight=FunctionWeight,
            **kwargs
        )
        super(VersionWeight, self).__init__(**processed_kwargs)


class AliasRoutingConfiguration(troposphere.awslambda.AliasRoutingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AdditionalVersionWeights=REQUIRED, # type: List[_VersionWeight]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdditionalVersionWeights=AdditionalVersionWeights,
            **kwargs
        )
        super(AliasRoutingConfiguration, self).__init__(**processed_kwargs)


class ProvisionedConcurrencyConfiguration(troposphere.awslambda.ProvisionedConcurrencyConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ProvisionedConcurrentExecutions=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ProvisionedConcurrentExecutions=ProvisionedConcurrentExecutions,
            **kwargs
        )
        super(ProvisionedConcurrencyConfiguration, self).__init__(**processed_kwargs)


class Alias(troposphere.awslambda.Alias, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FunctionVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisionedConcurrencyConfig=NOTHING, # type: _ProvisionedConcurrencyConfiguration
                 RoutingConfig=NOTHING, # type: _AliasRoutingConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            FunctionVersion=FunctionVersion,
            Name=Name,
            Description=Description,
            ProvisionedConcurrencyConfig=ProvisionedConcurrencyConfig,
            RoutingConfig=RoutingConfig,
            **kwargs
        )
        super(Alias, self).__init__(**processed_kwargs)


class AllowedPublishers(troposphere.awslambda.AllowedPublishers, Mixin):
    def __init__(self,
                 title=None,
                 SigningProfileVersionArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SigningProfileVersionArns=SigningProfileVersionArns,
            **kwargs
        )
        super(AllowedPublishers, self).__init__(**processed_kwargs)


class CodeSigningPolicies(troposphere.awslambda.CodeSigningPolicies, Mixin):
    def __init__(self,
                 title=None,
                 UntrustedArtifactOnDeployment=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            UntrustedArtifactOnDeployment=UntrustedArtifactOnDeployment,
            **kwargs
        )
        super(CodeSigningPolicies, self).__init__(**processed_kwargs)


class CodeSigningConfig(troposphere.awslambda.CodeSigningConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllowedPublishers=REQUIRED, # type: _AllowedPublishers
                 CodeSigningPolicies=NOTHING, # type: _CodeSigningPolicies
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllowedPublishers=AllowedPublishers,
            CodeSigningPolicies=CodeSigningPolicies,
            Description=Description,
            **kwargs
        )
        super(CodeSigningConfig, self).__init__(**processed_kwargs)


class Version(troposphere.awslambda.Version, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FunctionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CodeSha256=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisionedConcurrencyConfig=NOTHING, # type: _ProvisionedConcurrencyConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FunctionName=FunctionName,
            CodeSha256=CodeSha256,
            Description=Description,
            ProvisionedConcurrencyConfig=ProvisionedConcurrencyConfig,
            **kwargs
        )
        super(Version, self).__init__(**processed_kwargs)


class Content(troposphere.awslambda.Content, Mixin):
    def __init__(self,
                 title=None,
                 S3Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3ObjectVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Bucket=S3Bucket,
            S3Key=S3Key,
            S3ObjectVersion=S3ObjectVersion,
            **kwargs
        )
        super(Content, self).__init__(**processed_kwargs)


class LayerVersion(troposphere.awslambda.LayerVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Content=REQUIRED, # type: _Content
                 CompatibleRuntimes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LayerName=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseInfo=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Content=Content,
            CompatibleRuntimes=CompatibleRuntimes,
            Description=Description,
            LayerName=LayerName,
            LicenseInfo=LicenseInfo,
            **kwargs
        )
        super(LayerVersion, self).__init__(**processed_kwargs)


class LayerVersionPermission(troposphere.awslambda.LayerVersionPermission, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 LayerVersionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 OrganizationId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            LayerVersionArn=LayerVersionArn,
            Principal=Principal,
            OrganizationId=OrganizationId,
            **kwargs
        )
        super(LayerVersionPermission, self).__init__(**processed_kwargs)
