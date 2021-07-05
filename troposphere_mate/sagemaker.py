# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sagemaker

from troposphere.sagemaker import (
    Alarm as _Alarm,
    AutoRollbackConfig as _AutoRollbackConfig,
    BaselineConfig as _BaselineConfig,
    BlueGreenUpdatePolicy as _BlueGreenUpdatePolicy,
    CapacitySize as _CapacitySize,
    CaptureContentTypeHeader as _CaptureContentTypeHeader,
    CaptureOption as _CaptureOption,
    ClusterConfig as _ClusterConfig,
    CognitoMemberDefinition as _CognitoMemberDefinition,
    ConstraintsResource as _ConstraintsResource,
    ContainerDefinition as _ContainerDefinition,
    CustomImage as _CustomImage,
    DataCaptureConfig as _DataCaptureConfig,
    DataQualityAppSpecification as _DataQualityAppSpecification,
    DataQualityBaselineConfig as _DataQualityBaselineConfig,
    DataQualityJobInput as _DataQualityJobInput,
    DeploymentConfig as _DeploymentConfig,
    EdgeOutputConfig as _EdgeOutputConfig,
    EndpointInput as _EndpointInput,
    FeatureDefinition as _FeatureDefinition,
    FileSystemConfig as _FileSystemConfig,
    GitConfig as _GitConfig,
    ImageConfig as _ImageConfig,
    InferenceExecutionConfig as _InferenceExecutionConfig,
    JupyterServerAppSettings as _JupyterServerAppSettings,
    KernelGatewayAppSettings as _KernelGatewayAppSettings,
    KernelGatewayImageConfig as _KernelGatewayImageConfig,
    KernelSpec as _KernelSpec,
    MemberDefinition as _MemberDefinition,
    ModelBiasAppSpecification as _ModelBiasAppSpecification,
    ModelBiasBaselineConfig as _ModelBiasBaselineConfig,
    ModelBiasJobInput as _ModelBiasJobInput,
    ModelExplainabilityAppSpecification as _ModelExplainabilityAppSpecification,
    ModelExplainabilityBaselineConfig as _ModelExplainabilityBaselineConfig,
    ModelExplainabilityJobInput as _ModelExplainabilityJobInput,
    ModelQualityAppSpecification as _ModelQualityAppSpecification,
    ModelQualityBaselineConfig as _ModelQualityBaselineConfig,
    ModelQualityJobInput as _ModelQualityJobInput,
    MonitoringAppSpecification as _MonitoringAppSpecification,
    MonitoringExecutionSummary as _MonitoringExecutionSummary,
    MonitoringGroundTruthS3Input as _MonitoringGroundTruthS3Input,
    MonitoringInput as _MonitoringInput,
    MonitoringInputs as _MonitoringInputs,
    MonitoringJobDefinition as _MonitoringJobDefinition,
    MonitoringOutput as _MonitoringOutput,
    MonitoringOutputConfig as _MonitoringOutputConfig,
    MonitoringResources as _MonitoringResources,
    MonitoringScheduleConfig as _MonitoringScheduleConfig,
    MultiModelConfig as _MultiModelConfig,
    NetworkConfig as _NetworkConfig,
    NotebookInstanceLifecycleHook as _NotebookInstanceLifecycleHook,
    NotificationConfiguration as _NotificationConfiguration,
    ProductionVariant as _ProductionVariant,
    ResourceSpec as _ResourceSpec,
    S3Output as _S3Output,
    ScheduleConfig as _ScheduleConfig,
    SharingSettings as _SharingSettings,
    StatisticsResource as _StatisticsResource,
    StoppingCondition as _StoppingCondition,
    Tags as _Tags,
    TrafficRoutingConfig as _TrafficRoutingConfig,
    UserSettings as _UserSettings,
    VariantProperty as _VariantProperty,
    VpcConfig as _VpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ResourceSpec(troposphere.sagemaker.ResourceSpec, Mixin):
    def __init__(self,
                 title=None,
                 InstanceType=NOTHING, # type: Union[str, AWSHelperFn]
                 SageMakerImageArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SageMakerImageVersionArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceType=InstanceType,
            SageMakerImageArn=SageMakerImageArn,
            SageMakerImageVersionArn=SageMakerImageVersionArn,
            **kwargs
        )
        super(ResourceSpec, self).__init__(**processed_kwargs)


class App(troposphere.sagemaker.App, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AppName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AppType=REQUIRED, # type: Union[str, AWSHelperFn]
                 DomainId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserProfileName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceSpec=NOTHING, # type: _ResourceSpec
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AppName=AppName,
            AppType=AppType,
            DomainId=DomainId,
            UserProfileName=UserProfileName,
            ResourceSpec=ResourceSpec,
            Tags=Tags,
            **kwargs
        )
        super(App, self).__init__(**processed_kwargs)


class FileSystemConfig(troposphere.sagemaker.FileSystemConfig, Mixin):
    def __init__(self,
                 title=None,
                 DefaultGid=NOTHING, # type: int
                 DefaultUid=NOTHING, # type: int
                 MountPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultGid=DefaultGid,
            DefaultUid=DefaultUid,
            MountPath=MountPath,
            **kwargs
        )
        super(FileSystemConfig, self).__init__(**processed_kwargs)


class KernelSpec(troposphere.sagemaker.KernelSpec, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            DisplayName=DisplayName,
            **kwargs
        )
        super(KernelSpec, self).__init__(**processed_kwargs)


class KernelGatewayImageConfig(troposphere.sagemaker.KernelGatewayImageConfig, Mixin):
    def __init__(self,
                 title=None,
                 KernelSpecs=REQUIRED, # type: List[_KernelSpec]
                 FileSystemConfig=NOTHING, # type: _FileSystemConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KernelSpecs=KernelSpecs,
            FileSystemConfig=FileSystemConfig,
            **kwargs
        )
        super(KernelGatewayImageConfig, self).__init__(**processed_kwargs)


class AppImageConfig(troposphere.sagemaker.AppImageConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AppImageConfigName=REQUIRED, # type: Union[str, AWSHelperFn]
                 KernelGatewayImageConfig=NOTHING, # type: _KernelGatewayImageConfig
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AppImageConfigName=AppImageConfigName,
            KernelGatewayImageConfig=KernelGatewayImageConfig,
            Tags=Tags,
            **kwargs
        )
        super(AppImageConfig, self).__init__(**processed_kwargs)


class GitConfig(troposphere.sagemaker.GitConfig, Mixin):
    def __init__(self,
                 title=None,
                 RepositoryUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 Branch=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RepositoryUrl=RepositoryUrl,
            Branch=Branch,
            SecretArn=SecretArn,
            **kwargs
        )
        super(GitConfig, self).__init__(**processed_kwargs)


class CodeRepository(troposphere.sagemaker.CodeRepository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GitConfig=REQUIRED, # type: _GitConfig
                 CodeRepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GitConfig=GitConfig,
            CodeRepositoryName=CodeRepositoryName,
            **kwargs
        )
        super(CodeRepository, self).__init__(**processed_kwargs)


class DataQualityAppSpecification(troposphere.sagemaker.DataQualityAppSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ImageUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerArguments=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ContainerEntrypoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: dict
                 PostAnalyticsProcessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 RecordPreprocessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageUri=ImageUri,
            ContainerArguments=ContainerArguments,
            ContainerEntrypoint=ContainerEntrypoint,
            Environment=Environment,
            PostAnalyticsProcessorSourceUri=PostAnalyticsProcessorSourceUri,
            RecordPreprocessorSourceUri=RecordPreprocessorSourceUri,
            **kwargs
        )
        super(DataQualityAppSpecification, self).__init__(**processed_kwargs)


class ConstraintsResource(troposphere.sagemaker.ConstraintsResource, Mixin):
    def __init__(self,
                 title=None,
                 S3Uri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Uri=S3Uri,
            **kwargs
        )
        super(ConstraintsResource, self).__init__(**processed_kwargs)


class StatisticsResource(troposphere.sagemaker.StatisticsResource, Mixin):
    def __init__(self,
                 title=None,
                 S3Uri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Uri=S3Uri,
            **kwargs
        )
        super(StatisticsResource, self).__init__(**processed_kwargs)


class DataQualityBaselineConfig(troposphere.sagemaker.DataQualityBaselineConfig, Mixin):
    def __init__(self,
                 title=None,
                 BaseliningJobName=NOTHING, # type: Union[str, AWSHelperFn]
                 ConstraintsResource=NOTHING, # type: _ConstraintsResource
                 StatisticsResource=NOTHING, # type: _StatisticsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BaseliningJobName=BaseliningJobName,
            ConstraintsResource=ConstraintsResource,
            StatisticsResource=StatisticsResource,
            **kwargs
        )
        super(DataQualityBaselineConfig, self).__init__(**processed_kwargs)


class EndpointInput(troposphere.sagemaker.EndpointInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LocalPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3DataDistributionType=NOTHING, # type: Union[str, AWSHelperFn]
                 S3InputMode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointName=EndpointName,
            LocalPath=LocalPath,
            S3DataDistributionType=S3DataDistributionType,
            S3InputMode=S3InputMode,
            **kwargs
        )
        super(EndpointInput, self).__init__(**processed_kwargs)


class DataQualityJobInput(troposphere.sagemaker.DataQualityJobInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointInput=REQUIRED, # type: _EndpointInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointInput=EndpointInput,
            **kwargs
        )
        super(DataQualityJobInput, self).__init__(**processed_kwargs)


class S3Output(troposphere.sagemaker.S3Output, Mixin):
    def __init__(self,
                 title=None,
                 LocalPath=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Uri=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3UploadMode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LocalPath=LocalPath,
            S3Uri=S3Uri,
            S3UploadMode=S3UploadMode,
            **kwargs
        )
        super(S3Output, self).__init__(**processed_kwargs)


class MonitoringOutput(troposphere.sagemaker.MonitoringOutput, Mixin):
    def __init__(self,
                 title=None,
                 S3Output=REQUIRED, # type: _S3Output
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Output=S3Output,
            **kwargs
        )
        super(MonitoringOutput, self).__init__(**processed_kwargs)


class MonitoringOutputConfig(troposphere.sagemaker.MonitoringOutputConfig, Mixin):
    def __init__(self,
                 title=None,
                 MonitoringOutputs=REQUIRED, # type: List[_MonitoringOutput]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MonitoringOutputs=MonitoringOutputs,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(MonitoringOutputConfig, self).__init__(**processed_kwargs)


class ClusterConfig(troposphere.sagemaker.ClusterConfig, Mixin):
    def __init__(self,
                 title=None,
                 InstanceCount=REQUIRED, # type: int
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 VolumeSizeInGB=REQUIRED, # type: int
                 VolumeKmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceCount=InstanceCount,
            InstanceType=InstanceType,
            VolumeSizeInGB=VolumeSizeInGB,
            VolumeKmsKeyId=VolumeKmsKeyId,
            **kwargs
        )
        super(ClusterConfig, self).__init__(**processed_kwargs)


class MonitoringResources(troposphere.sagemaker.MonitoringResources, Mixin):
    def __init__(self,
                 title=None,
                 ClusterConfig=REQUIRED, # type: _ClusterConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClusterConfig=ClusterConfig,
            **kwargs
        )
        super(MonitoringResources, self).__init__(**processed_kwargs)


class VpcConfig(troposphere.sagemaker.VpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Subnets=Subnets,
            SecurityGroupIds=SecurityGroupIds,
            **kwargs
        )
        super(VpcConfig, self).__init__(**processed_kwargs)


class NetworkConfig(troposphere.sagemaker.NetworkConfig, Mixin):
    def __init__(self,
                 title=None,
                 EnableInterContainerTrafficEncryption=NOTHING, # type: bool
                 EnableNetworkIsolation=NOTHING, # type: bool
                 VpcConfig=NOTHING, # type: _VpcConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EnableInterContainerTrafficEncryption=EnableInterContainerTrafficEncryption,
            EnableNetworkIsolation=EnableNetworkIsolation,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(NetworkConfig, self).__init__(**processed_kwargs)


class StoppingCondition(troposphere.sagemaker.StoppingCondition, Mixin):
    def __init__(self,
                 title=None,
                 MaxRuntimeInSeconds=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRuntimeInSeconds=MaxRuntimeInSeconds,
            **kwargs
        )
        super(StoppingCondition, self).__init__(**processed_kwargs)


class DataQualityJobDefinition(troposphere.sagemaker.DataQualityJobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DataQualityAppSpecification=REQUIRED, # type: _DataQualityAppSpecification
                 DataQualityJobInput=REQUIRED, # type: _DataQualityJobInput
                 DataQualityJobOutputConfig=REQUIRED, # type: _MonitoringOutputConfig
                 JobResources=REQUIRED, # type: _MonitoringResources
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataQualityBaselineConfig=NOTHING, # type: _DataQualityBaselineConfig
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkConfig=NOTHING, # type: _NetworkConfig
                 StoppingCondition=NOTHING, # type: _StoppingCondition
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DataQualityAppSpecification=DataQualityAppSpecification,
            DataQualityJobInput=DataQualityJobInput,
            DataQualityJobOutputConfig=DataQualityJobOutputConfig,
            JobResources=JobResources,
            RoleArn=RoleArn,
            DataQualityBaselineConfig=DataQualityBaselineConfig,
            JobDefinitionName=JobDefinitionName,
            NetworkConfig=NetworkConfig,
            StoppingCondition=StoppingCondition,
            Tags=Tags,
            **kwargs
        )
        super(DataQualityJobDefinition, self).__init__(**processed_kwargs)


class Device(troposphere.sagemaker.Device, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeviceFleetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Device=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeviceFleetName=DeviceFleetName,
            Device=Device,
            Tags=Tags,
            **kwargs
        )
        super(Device, self).__init__(**processed_kwargs)


class EdgeOutputConfig(troposphere.sagemaker.EdgeOutputConfig, Mixin):
    def __init__(self,
                 title=None,
                 S3OutputLocation=REQUIRED, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3OutputLocation=S3OutputLocation,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(EdgeOutputConfig, self).__init__(**processed_kwargs)


class DeviceFleet(troposphere.sagemaker.DeviceFleet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeviceFleetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 OutputConfig=REQUIRED, # type: _EdgeOutputConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeviceFleetName=DeviceFleetName,
            OutputConfig=OutputConfig,
            RoleArn=RoleArn,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(DeviceFleet, self).__init__(**processed_kwargs)


class JupyterServerAppSettings(troposphere.sagemaker.JupyterServerAppSettings, Mixin):
    def __init__(self,
                 title=None,
                 DefaultResourceSpec=NOTHING, # type: _ResourceSpec
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultResourceSpec=DefaultResourceSpec,
            **kwargs
        )
        super(JupyterServerAppSettings, self).__init__(**processed_kwargs)


class CustomImage(troposphere.sagemaker.CustomImage, Mixin):
    def __init__(self,
                 title=None,
                 AppImageConfigName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageVersionNumber=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppImageConfigName=AppImageConfigName,
            ImageName=ImageName,
            ImageVersionNumber=ImageVersionNumber,
            **kwargs
        )
        super(CustomImage, self).__init__(**processed_kwargs)


class KernelGatewayAppSettings(troposphere.sagemaker.KernelGatewayAppSettings, Mixin):
    def __init__(self,
                 title=None,
                 CustomImages=NOTHING, # type: List[_CustomImage]
                 DefaultResourceSpec=NOTHING, # type: _ResourceSpec
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CustomImages=CustomImages,
            DefaultResourceSpec=DefaultResourceSpec,
            **kwargs
        )
        super(KernelGatewayAppSettings, self).__init__(**processed_kwargs)


class SharingSettings(troposphere.sagemaker.SharingSettings, Mixin):
    def __init__(self,
                 title=None,
                 NotebookOutputOption=NOTHING, # type: Union[str, AWSHelperFn]
                 S3KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 S3OutputPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NotebookOutputOption=NotebookOutputOption,
            S3KmsKeyId=S3KmsKeyId,
            S3OutputPath=S3OutputPath,
            **kwargs
        )
        super(SharingSettings, self).__init__(**processed_kwargs)


class UserSettings(troposphere.sagemaker.UserSettings, Mixin):
    def __init__(self,
                 title=None,
                 ExecutionRole=NOTHING, # type: Union[str, AWSHelperFn]
                 JupyterServerAppSettings=NOTHING, # type: _JupyterServerAppSettings
                 KernelGatewayAppSettings=NOTHING, # type: _KernelGatewayAppSettings
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SharingSettings=NOTHING, # type: _SharingSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExecutionRole=ExecutionRole,
            JupyterServerAppSettings=JupyterServerAppSettings,
            KernelGatewayAppSettings=KernelGatewayAppSettings,
            SecurityGroups=SecurityGroups,
            SharingSettings=SharingSettings,
            **kwargs
        )
        super(UserSettings, self).__init__(**processed_kwargs)


class Domain(troposphere.sagemaker.Domain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultUserSettings=REQUIRED, # type: _UserSettings
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AppNetworkAccessType=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthMode=AuthMode,
            DefaultUserSettings=DefaultUserSettings,
            DomainName=DomainName,
            SubnetIds=SubnetIds,
            VpcId=VpcId,
            AppNetworkAccessType=AppNetworkAccessType,
            KmsKeyId=KmsKeyId,
            Tags=Tags,
            **kwargs
        )
        super(Domain, self).__init__(**processed_kwargs)


class Alarm(troposphere.sagemaker.Alarm, Mixin):
    def __init__(self,
                 title=None,
                 AlarmName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmName=AlarmName,
            **kwargs
        )
        super(Alarm, self).__init__(**processed_kwargs)


class AutoRollbackConfig(troposphere.sagemaker.AutoRollbackConfig, Mixin):
    def __init__(self,
                 title=None,
                 Alarms=REQUIRED, # type: List[_Alarm]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Alarms=Alarms,
            **kwargs
        )
        super(AutoRollbackConfig, self).__init__(**processed_kwargs)


class CapacitySize(troposphere.sagemaker.CapacitySize, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(CapacitySize, self).__init__(**processed_kwargs)


class TrafficRoutingConfig(troposphere.sagemaker.TrafficRoutingConfig, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 CanarySize=NOTHING, # type: _CapacitySize
                 WaitIntervalInSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            CanarySize=CanarySize,
            WaitIntervalInSeconds=WaitIntervalInSeconds,
            **kwargs
        )
        super(TrafficRoutingConfig, self).__init__(**processed_kwargs)


class BlueGreenUpdatePolicy(troposphere.sagemaker.BlueGreenUpdatePolicy, Mixin):
    def __init__(self,
                 title=None,
                 TrafficRoutingConfiguration=REQUIRED, # type: _TrafficRoutingConfig
                 MaximumExecutionTimeoutInSeconds=NOTHING, # type: int
                 TerminationWaitInSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TrafficRoutingConfiguration=TrafficRoutingConfiguration,
            MaximumExecutionTimeoutInSeconds=MaximumExecutionTimeoutInSeconds,
            TerminationWaitInSeconds=TerminationWaitInSeconds,
            **kwargs
        )
        super(BlueGreenUpdatePolicy, self).__init__(**processed_kwargs)


class DeploymentConfig(troposphere.sagemaker.DeploymentConfig, Mixin):
    def __init__(self,
                 title=None,
                 BlueGreenUpdatePolicy=REQUIRED, # type: _BlueGreenUpdatePolicy
                 AutoRollbackConfiguration=NOTHING, # type: _AutoRollbackConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BlueGreenUpdatePolicy=BlueGreenUpdatePolicy,
            AutoRollbackConfiguration=AutoRollbackConfiguration,
            **kwargs
        )
        super(DeploymentConfig, self).__init__(**processed_kwargs)


class VariantProperty(troposphere.sagemaker.VariantProperty, Mixin):
    def __init__(self,
                 title=None,
                 VariantPropertyType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VariantPropertyType=VariantPropertyType,
            **kwargs
        )
        super(VariantProperty, self).__init__(**processed_kwargs)


class Endpoint(troposphere.sagemaker.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointConfigName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeploymentConfig=NOTHING, # type: _DeploymentConfig
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludeRetainedVariantProperties=NOTHING, # type: List[_VariantProperty]
                 RetainAllVariantProperties=NOTHING, # type: bool
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointConfigName=EndpointConfigName,
            DeploymentConfig=DeploymentConfig,
            EndpointName=EndpointName,
            ExcludeRetainedVariantProperties=ExcludeRetainedVariantProperties,
            RetainAllVariantProperties=RetainAllVariantProperties,
            Tags=Tags,
            **kwargs
        )
        super(Endpoint, self).__init__(**processed_kwargs)


class CaptureContentTypeHeader(troposphere.sagemaker.CaptureContentTypeHeader, Mixin):
    def __init__(self,
                 title=None,
                 CsvContentTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 JsonContentTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CsvContentTypes=CsvContentTypes,
            JsonContentTypes=JsonContentTypes,
            **kwargs
        )
        super(CaptureContentTypeHeader, self).__init__(**processed_kwargs)


class CaptureOption(troposphere.sagemaker.CaptureOption, Mixin):
    def __init__(self,
                 title=None,
                 CaptureMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CaptureMode=CaptureMode,
            **kwargs
        )
        super(CaptureOption, self).__init__(**processed_kwargs)


class DataCaptureConfig(troposphere.sagemaker.DataCaptureConfig, Mixin):
    def __init__(self,
                 title=None,
                 CaptureOptions=REQUIRED, # type: List[_CaptureOption]
                 DestinationS3Uri=REQUIRED, # type: Union[str, AWSHelperFn]
                 InitialSamplingPercentage=REQUIRED, # type: int
                 CaptureContentTypeHeader=NOTHING, # type: _CaptureContentTypeHeader
                 EnableCapture=NOTHING, # type: bool
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CaptureOptions=CaptureOptions,
            DestinationS3Uri=DestinationS3Uri,
            InitialSamplingPercentage=InitialSamplingPercentage,
            CaptureContentTypeHeader=CaptureContentTypeHeader,
            EnableCapture=EnableCapture,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(DataCaptureConfig, self).__init__(**processed_kwargs)


class ProductionVariant(troposphere.sagemaker.ProductionVariant, Mixin):
    def __init__(self,
                 title=None,
                 ModelName=REQUIRED, # type: Union[str, AWSHelperFn]
                 VariantName=REQUIRED, # type: Union[str, AWSHelperFn]
                 InitialInstanceCount=REQUIRED, # type: int
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 InitialVariantWeight=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ModelName=ModelName,
            VariantName=VariantName,
            InitialInstanceCount=InitialInstanceCount,
            InstanceType=InstanceType,
            InitialVariantWeight=InitialVariantWeight,
            **kwargs
        )
        super(ProductionVariant, self).__init__(**processed_kwargs)


class EndpointConfig(troposphere.sagemaker.EndpointConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProductionVariants=REQUIRED, # type: List[_ProductionVariant]
                 DataCaptureConfig=NOTHING, # type: _DataCaptureConfig
                 EndpointConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProductionVariants=ProductionVariants,
            DataCaptureConfig=DataCaptureConfig,
            EndpointConfigName=EndpointConfigName,
            KmsKeyId=KmsKeyId,
            Tags=Tags,
            **kwargs
        )
        super(EndpointConfig, self).__init__(**processed_kwargs)


class FeatureDefinition(troposphere.sagemaker.FeatureDefinition, Mixin):
    def __init__(self,
                 title=None,
                 FeatureName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FeatureType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FeatureName=FeatureName,
            FeatureType=FeatureType,
            **kwargs
        )
        super(FeatureDefinition, self).__init__(**processed_kwargs)


class FeatureGroup(troposphere.sagemaker.FeatureGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EventTimeFeatureName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FeatureDefinitions=REQUIRED, # type: List[_FeatureDefinition]
                 FeatureGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RecordIdentifierFeatureName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 OfflineStoreConfig=NOTHING, # type: dict
                 OnlineStoreConfig=NOTHING, # type: dict
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EventTimeFeatureName=EventTimeFeatureName,
            FeatureDefinitions=FeatureDefinitions,
            FeatureGroupName=FeatureGroupName,
            RecordIdentifierFeatureName=RecordIdentifierFeatureName,
            Description=Description,
            OfflineStoreConfig=OfflineStoreConfig,
            OnlineStoreConfig=OnlineStoreConfig,
            RoleArn=RoleArn,
            Tags=Tags,
            **kwargs
        )
        super(FeatureGroup, self).__init__(**processed_kwargs)


class Image(troposphere.sagemaker.Image, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ImageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageDisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ImageName=ImageName,
            ImageRoleArn=ImageRoleArn,
            ImageDescription=ImageDescription,
            ImageDisplayName=ImageDisplayName,
            Tags=Tags,
            **kwargs
        )
        super(Image, self).__init__(**processed_kwargs)


class ImageVersion(troposphere.sagemaker.ImageVersion, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BaseImage=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BaseImage=BaseImage,
            ImageName=ImageName,
            **kwargs
        )
        super(ImageVersion, self).__init__(**processed_kwargs)


class ImageConfig(troposphere.sagemaker.ImageConfig, Mixin):
    def __init__(self,
                 title=None,
                 RepositoryAccessMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RepositoryAccessMode=RepositoryAccessMode,
            **kwargs
        )
        super(ImageConfig, self).__init__(**processed_kwargs)


class MultiModelConfig(troposphere.sagemaker.MultiModelConfig, Mixin):
    def __init__(self,
                 title=None,
                 ModelCacheSetting=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ModelCacheSetting=ModelCacheSetting,
            **kwargs
        )
        super(MultiModelConfig, self).__init__(**processed_kwargs)


class ContainerDefinition(troposphere.sagemaker.ContainerDefinition, Mixin):
    def __init__(self,
                 title=None,
                 ContainerHostname=NOTHING, # type: Union[str, AWSHelperFn]
                 Environment=NOTHING, # type: dict
                 Image=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageConfig=NOTHING, # type: _ImageConfig
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelDataUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelPackageName=NOTHING, # type: Union[str, AWSHelperFn]
                 MultiModelConfig=NOTHING, # type: _MultiModelConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ContainerHostname=ContainerHostname,
            Environment=Environment,
            Image=Image,
            ImageConfig=ImageConfig,
            Mode=Mode,
            ModelDataUrl=ModelDataUrl,
            ModelPackageName=ModelPackageName,
            MultiModelConfig=MultiModelConfig,
            **kwargs
        )
        super(ContainerDefinition, self).__init__(**processed_kwargs)


class InferenceExecutionConfig(troposphere.sagemaker.InferenceExecutionConfig, Mixin):
    def __init__(self,
                 title=None,
                 Mode=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Mode=Mode,
            **kwargs
        )
        super(InferenceExecutionConfig, self).__init__(**processed_kwargs)


class Model(troposphere.sagemaker.Model, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Containers=NOTHING, # type: List[_ContainerDefinition]
                 EnableNetworkIsolation=NOTHING, # type: bool
                 InferenceExecutionConfig=NOTHING, # type: _InferenceExecutionConfig
                 ModelName=NOTHING, # type: Union[str, AWSHelperFn]
                 PrimaryContainer=NOTHING, # type: _ContainerDefinition
                 Tags=NOTHING, # type: _Tags
                 VpcConfig=NOTHING, # type: _VpcConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ExecutionRoleArn=ExecutionRoleArn,
            Containers=Containers,
            EnableNetworkIsolation=EnableNetworkIsolation,
            InferenceExecutionConfig=InferenceExecutionConfig,
            ModelName=ModelName,
            PrimaryContainer=PrimaryContainer,
            Tags=Tags,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Model, self).__init__(**processed_kwargs)


class ModelBiasAppSpecification(troposphere.sagemaker.ModelBiasAppSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ConfigUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 Environment=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigUri=ConfigUri,
            ImageUri=ImageUri,
            Environment=Environment,
            **kwargs
        )
        super(ModelBiasAppSpecification, self).__init__(**processed_kwargs)


class ModelBiasBaselineConfig(troposphere.sagemaker.ModelBiasBaselineConfig, Mixin):
    def __init__(self,
                 title=None,
                 BaseliningJobName=NOTHING, # type: Union[str, AWSHelperFn]
                 ConstraintsResource=NOTHING, # type: _ConstraintsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BaseliningJobName=BaseliningJobName,
            ConstraintsResource=ConstraintsResource,
            **kwargs
        )
        super(ModelBiasBaselineConfig, self).__init__(**processed_kwargs)


class MonitoringGroundTruthS3Input(troposphere.sagemaker.MonitoringGroundTruthS3Input, Mixin):
    def __init__(self,
                 title=None,
                 S3Uri=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Uri=S3Uri,
            **kwargs
        )
        super(MonitoringGroundTruthS3Input, self).__init__(**processed_kwargs)


class ModelBiasJobInput(troposphere.sagemaker.ModelBiasJobInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointInput=REQUIRED, # type: _EndpointInput
                 GroundTruthS3Input=REQUIRED, # type: _MonitoringGroundTruthS3Input
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointInput=EndpointInput,
            GroundTruthS3Input=GroundTruthS3Input,
            **kwargs
        )
        super(ModelBiasJobInput, self).__init__(**processed_kwargs)


class ModelBiasJobDefinition(troposphere.sagemaker.ModelBiasJobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 JobResources=REQUIRED, # type: _MonitoringResources
                 ModelBiasAppSpecification=REQUIRED, # type: _ModelBiasAppSpecification
                 ModelBiasJobInput=REQUIRED, # type: _ModelBiasJobInput
                 ModelBiasJobOutputConfig=REQUIRED, # type: _MonitoringOutputConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelBiasBaselineConfig=NOTHING, # type: _ModelBiasBaselineConfig
                 NetworkConfig=NOTHING, # type: _NetworkConfig
                 StoppingCondition=NOTHING, # type: _StoppingCondition
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            JobResources=JobResources,
            ModelBiasAppSpecification=ModelBiasAppSpecification,
            ModelBiasJobInput=ModelBiasJobInput,
            ModelBiasJobOutputConfig=ModelBiasJobOutputConfig,
            RoleArn=RoleArn,
            JobDefinitionName=JobDefinitionName,
            ModelBiasBaselineConfig=ModelBiasBaselineConfig,
            NetworkConfig=NetworkConfig,
            StoppingCondition=StoppingCondition,
            Tags=Tags,
            **kwargs
        )
        super(ModelBiasJobDefinition, self).__init__(**processed_kwargs)


class ModelExplainabilityAppSpecification(troposphere.sagemaker.ModelExplainabilityAppSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ConfigUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 Environment=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigUri=ConfigUri,
            ImageUri=ImageUri,
            Environment=Environment,
            **kwargs
        )
        super(ModelExplainabilityAppSpecification, self).__init__(**processed_kwargs)


class ModelExplainabilityBaselineConfig(troposphere.sagemaker.ModelExplainabilityBaselineConfig, Mixin):
    def __init__(self,
                 title=None,
                 BaseliningJobName=NOTHING, # type: Union[str, AWSHelperFn]
                 ConstraintsResource=NOTHING, # type: _ConstraintsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BaseliningJobName=BaseliningJobName,
            ConstraintsResource=ConstraintsResource,
            **kwargs
        )
        super(ModelExplainabilityBaselineConfig, self).__init__(**processed_kwargs)


class ModelExplainabilityJobInput(troposphere.sagemaker.ModelExplainabilityJobInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointInput=REQUIRED, # type: _EndpointInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointInput=EndpointInput,
            **kwargs
        )
        super(ModelExplainabilityJobInput, self).__init__(**processed_kwargs)


class ModelExplainabilityJobDefinition(troposphere.sagemaker.ModelExplainabilityJobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 JobResources=REQUIRED, # type: _MonitoringResources
                 ModelExplainabilityAppSpecification=REQUIRED, # type: _ModelExplainabilityAppSpecification
                 ModelExplainabilityJobInput=REQUIRED, # type: _ModelExplainabilityJobInput
                 ModelExplainabilityJobOutputConfig=REQUIRED, # type: _MonitoringOutputConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelExplainabilityBaselineConfig=NOTHING, # type: _ModelExplainabilityBaselineConfig
                 NetworkConfig=NOTHING, # type: _NetworkConfig
                 StoppingCondition=NOTHING, # type: _StoppingCondition
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            JobResources=JobResources,
            ModelExplainabilityAppSpecification=ModelExplainabilityAppSpecification,
            ModelExplainabilityJobInput=ModelExplainabilityJobInput,
            ModelExplainabilityJobOutputConfig=ModelExplainabilityJobOutputConfig,
            RoleArn=RoleArn,
            JobDefinitionName=JobDefinitionName,
            ModelExplainabilityBaselineConfig=ModelExplainabilityBaselineConfig,
            NetworkConfig=NetworkConfig,
            StoppingCondition=StoppingCondition,
            Tags=Tags,
            **kwargs
        )
        super(ModelExplainabilityJobDefinition, self).__init__(**processed_kwargs)


class ModelPackageGroup(troposphere.sagemaker.ModelPackageGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ModelPackageGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ModelPackageGroupDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelPackageGroupPolicy=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ModelPackageGroupName=ModelPackageGroupName,
            ModelPackageGroupDescription=ModelPackageGroupDescription,
            ModelPackageGroupPolicy=ModelPackageGroupPolicy,
            Tags=Tags,
            **kwargs
        )
        super(ModelPackageGroup, self).__init__(**processed_kwargs)


class ModelQualityAppSpecification(troposphere.sagemaker.ModelQualityAppSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ImageUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProblemType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerArguments=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ContainerEntrypoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Environment=NOTHING, # type: dict
                 PostAnalyticsProcessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 RecordPreprocessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageUri=ImageUri,
            ProblemType=ProblemType,
            ContainerArguments=ContainerArguments,
            ContainerEntrypoint=ContainerEntrypoint,
            Environment=Environment,
            PostAnalyticsProcessorSourceUri=PostAnalyticsProcessorSourceUri,
            RecordPreprocessorSourceUri=RecordPreprocessorSourceUri,
            **kwargs
        )
        super(ModelQualityAppSpecification, self).__init__(**processed_kwargs)


class ModelQualityBaselineConfig(troposphere.sagemaker.ModelQualityBaselineConfig, Mixin):
    def __init__(self,
                 title=None,
                 BaseliningJobName=NOTHING, # type: Union[str, AWSHelperFn]
                 ConstraintsResource=NOTHING, # type: _ConstraintsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BaseliningJobName=BaseliningJobName,
            ConstraintsResource=ConstraintsResource,
            **kwargs
        )
        super(ModelQualityBaselineConfig, self).__init__(**processed_kwargs)


class ModelQualityJobInput(troposphere.sagemaker.ModelQualityJobInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointInput=REQUIRED, # type: _EndpointInput
                 GroundTruthS3Input=REQUIRED, # type: _MonitoringGroundTruthS3Input
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointInput=EndpointInput,
            GroundTruthS3Input=GroundTruthS3Input,
            **kwargs
        )
        super(ModelQualityJobInput, self).__init__(**processed_kwargs)


class ModelQualityJobDefinition(troposphere.sagemaker.ModelQualityJobDefinition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 JobResources=REQUIRED, # type: _MonitoringResources
                 ModelQualityAppSpecification=REQUIRED, # type: _ModelQualityAppSpecification
                 ModelQualityJobInput=REQUIRED, # type: _ModelQualityJobInput
                 ModelQualityJobOutputConfig=REQUIRED, # type: _MonitoringOutputConfig
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobDefinitionName=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelQualityBaselineConfig=NOTHING, # type: _ModelQualityBaselineConfig
                 NetworkConfig=NOTHING, # type: _NetworkConfig
                 StoppingCondition=NOTHING, # type: _StoppingCondition
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            JobResources=JobResources,
            ModelQualityAppSpecification=ModelQualityAppSpecification,
            ModelQualityJobInput=ModelQualityJobInput,
            ModelQualityJobOutputConfig=ModelQualityJobOutputConfig,
            RoleArn=RoleArn,
            JobDefinitionName=JobDefinitionName,
            ModelQualityBaselineConfig=ModelQualityBaselineConfig,
            NetworkConfig=NetworkConfig,
            StoppingCondition=StoppingCondition,
            Tags=Tags,
            **kwargs
        )
        super(ModelQualityJobDefinition, self).__init__(**processed_kwargs)


class MonitoringExecutionSummary(troposphere.sagemaker.MonitoringExecutionSummary, Mixin):
    def __init__(self,
                 title=None,
                 CreationTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 LastModifiedTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 MonitoringExecutionStatus=REQUIRED, # type: Union[str, AWSHelperFn]
                 MonitoringScheduleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ScheduledTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 FailureReason=NOTHING, # type: Union[str, AWSHelperFn]
                 ProcessingJobArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CreationTime=CreationTime,
            LastModifiedTime=LastModifiedTime,
            MonitoringExecutionStatus=MonitoringExecutionStatus,
            MonitoringScheduleName=MonitoringScheduleName,
            ScheduledTime=ScheduledTime,
            EndpointName=EndpointName,
            FailureReason=FailureReason,
            ProcessingJobArn=ProcessingJobArn,
            **kwargs
        )
        super(MonitoringExecutionSummary, self).__init__(**processed_kwargs)


class BaselineConfig(troposphere.sagemaker.BaselineConfig, Mixin):
    def __init__(self,
                 title=None,
                 ConstraintsResource=NOTHING, # type: _ConstraintsResource
                 StatisticsResource=NOTHING, # type: _StatisticsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConstraintsResource=ConstraintsResource,
            StatisticsResource=StatisticsResource,
            **kwargs
        )
        super(BaselineConfig, self).__init__(**processed_kwargs)


class MonitoringAppSpecification(troposphere.sagemaker.MonitoringAppSpecification, Mixin):
    def __init__(self,
                 title=None,
                 ImageUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerArguments=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ContainerEntrypoint=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PostAnalyticsProcessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 RecordPreprocessorSourceUri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageUri=ImageUri,
            ContainerArguments=ContainerArguments,
            ContainerEntrypoint=ContainerEntrypoint,
            PostAnalyticsProcessorSourceUri=PostAnalyticsProcessorSourceUri,
            RecordPreprocessorSourceUri=RecordPreprocessorSourceUri,
            **kwargs
        )
        super(MonitoringAppSpecification, self).__init__(**processed_kwargs)


class MonitoringInput(troposphere.sagemaker.MonitoringInput, Mixin):
    def __init__(self,
                 title=None,
                 EndpointInput=REQUIRED, # type: _EndpointInput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointInput=EndpointInput,
            **kwargs
        )
        super(MonitoringInput, self).__init__(**processed_kwargs)


class MonitoringInputs(troposphere.sagemaker.MonitoringInputs, Mixin):
    def __init__(self,
                 title=None,
                 MonitoringInputs=NOTHING, # type: List[_MonitoringInput]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MonitoringInputs=MonitoringInputs,
            **kwargs
        )
        super(MonitoringInputs, self).__init__(**processed_kwargs)


class MonitoringJobDefinition(troposphere.sagemaker.MonitoringJobDefinition, Mixin):
    def __init__(self,
                 title=None,
                 MonitoringAppSpecification=REQUIRED, # type: _MonitoringAppSpecification
                 MonitoringInputs=REQUIRED, # type: _MonitoringInputs
                 MonitoringOutputConfig=REQUIRED, # type: _MonitoringOutputConfig
                 MonitoringResources=REQUIRED, # type: _MonitoringResources
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 BaselineConfig=NOTHING, # type: _BaselineConfig
                 Environment=NOTHING, # type: dict
                 NetworkConfig=NOTHING, # type: _NetworkConfig
                 StoppingCondition=NOTHING, # type: _StoppingCondition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MonitoringAppSpecification=MonitoringAppSpecification,
            MonitoringInputs=MonitoringInputs,
            MonitoringOutputConfig=MonitoringOutputConfig,
            MonitoringResources=MonitoringResources,
            RoleArn=RoleArn,
            BaselineConfig=BaselineConfig,
            Environment=Environment,
            NetworkConfig=NetworkConfig,
            StoppingCondition=StoppingCondition,
            **kwargs
        )
        super(MonitoringJobDefinition, self).__init__(**processed_kwargs)


class ScheduleConfig(troposphere.sagemaker.ScheduleConfig, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(ScheduleConfig, self).__init__(**processed_kwargs)


class MonitoringScheduleConfig(troposphere.sagemaker.MonitoringScheduleConfig, Mixin):
    def __init__(self,
                 title=None,
                 MonitoringJobDefinition=REQUIRED, # type: _MonitoringJobDefinition
                 ScheduleConfig=NOTHING, # type: _ScheduleConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MonitoringJobDefinition=MonitoringJobDefinition,
            ScheduleConfig=ScheduleConfig,
            **kwargs
        )
        super(MonitoringScheduleConfig, self).__init__(**processed_kwargs)


class MonitoringSchedule(troposphere.sagemaker.MonitoringSchedule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MonitoringScheduleConfig=REQUIRED, # type: _MonitoringScheduleConfig
                 MonitoringScheduleName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CreationTime=NOTHING, # type: Union[str, AWSHelperFn]
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 FailureReason=NOTHING, # type: Union[str, AWSHelperFn]
                 LastModifiedTime=NOTHING, # type: Union[str, AWSHelperFn]
                 LastMonitoringExecutionSummary=NOTHING, # type: _MonitoringExecutionSummary
                 MonitoringScheduleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MonitoringScheduleStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MonitoringScheduleConfig=MonitoringScheduleConfig,
            MonitoringScheduleName=MonitoringScheduleName,
            CreationTime=CreationTime,
            EndpointName=EndpointName,
            FailureReason=FailureReason,
            LastModifiedTime=LastModifiedTime,
            LastMonitoringExecutionSummary=LastMonitoringExecutionSummary,
            MonitoringScheduleArn=MonitoringScheduleArn,
            MonitoringScheduleStatus=MonitoringScheduleStatus,
            Tags=Tags,
            **kwargs
        )
        super(MonitoringSchedule, self).__init__(**processed_kwargs)


class NotebookInstance(troposphere.sagemaker.NotebookInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AcceleratorTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AdditionalCodeRepositories=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DefaultCodeRepository=NOTHING, # type: Union[str, AWSHelperFn]
                 DirectInternetAccess=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LifecycleConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 NotebookInstanceName=NOTHING, # type: Union[str, AWSHelperFn]
                 RootAccess=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VolumeSizeInGB=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceType=InstanceType,
            RoleArn=RoleArn,
            AcceleratorTypes=AcceleratorTypes,
            AdditionalCodeRepositories=AdditionalCodeRepositories,
            DefaultCodeRepository=DefaultCodeRepository,
            DirectInternetAccess=DirectInternetAccess,
            KmsKeyId=KmsKeyId,
            LifecycleConfigName=LifecycleConfigName,
            NotebookInstanceName=NotebookInstanceName,
            RootAccess=RootAccess,
            SecurityGroupIds=SecurityGroupIds,
            SubnetId=SubnetId,
            Tags=Tags,
            VolumeSizeInGB=VolumeSizeInGB,
            **kwargs
        )
        super(NotebookInstance, self).__init__(**processed_kwargs)


class NotebookInstanceLifecycleHook(troposphere.sagemaker.NotebookInstanceLifecycleHook, Mixin):
    def __init__(self,
                 title=None,
                 Content=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Content=Content,
            **kwargs
        )
        super(NotebookInstanceLifecycleHook, self).__init__(**processed_kwargs)


class NotebookInstanceLifecycleConfig(troposphere.sagemaker.NotebookInstanceLifecycleConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 NotebookInstanceLifecycleConfigName=NOTHING, # type: Union[str, AWSHelperFn]
                 OnCreate=NOTHING, # type: List[_NotebookInstanceLifecycleHook]
                 OnStart=NOTHING, # type: List[_NotebookInstanceLifecycleHook]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            NotebookInstanceLifecycleConfigName=NotebookInstanceLifecycleConfigName,
            OnCreate=OnCreate,
            OnStart=OnStart,
            **kwargs
        )
        super(NotebookInstanceLifecycleConfig, self).__init__(**processed_kwargs)


class Pipeline(troposphere.sagemaker.Pipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PipelineDefinition=REQUIRED, # type: dict
                 PipelineName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PipelineDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 PipelineDisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PipelineDefinition=PipelineDefinition,
            PipelineName=PipelineName,
            RoleArn=RoleArn,
            PipelineDescription=PipelineDescription,
            PipelineDisplayName=PipelineDisplayName,
            Tags=Tags,
            **kwargs
        )
        super(Pipeline, self).__init__(**processed_kwargs)


class Project(troposphere.sagemaker.Project, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProjectName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceCatalogProvisioningDetails=REQUIRED, # type: dict
                 ProjectDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProjectName=ProjectName,
            ServiceCatalogProvisioningDetails=ServiceCatalogProvisioningDetails,
            ProjectDescription=ProjectDescription,
            Tags=Tags,
            **kwargs
        )
        super(Project, self).__init__(**processed_kwargs)


class UserProfile(troposphere.sagemaker.UserProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainId=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserProfileName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SingleSignOnUserIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SingleSignOnUserValue=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 UserSettings=NOTHING, # type: _UserSettings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainId=DomainId,
            UserProfileName=UserProfileName,
            SingleSignOnUserIdentifier=SingleSignOnUserIdentifier,
            SingleSignOnUserValue=SingleSignOnUserValue,
            Tags=Tags,
            UserSettings=UserSettings,
            **kwargs
        )
        super(UserProfile, self).__init__(**processed_kwargs)


class CognitoMemberDefinition(troposphere.sagemaker.CognitoMemberDefinition, Mixin):
    def __init__(self,
                 title=None,
                 CognitoClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 CognitoUserGroup=REQUIRED, # type: Union[str, AWSHelperFn]
                 CognitoUserPool=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CognitoClientId=CognitoClientId,
            CognitoUserGroup=CognitoUserGroup,
            CognitoUserPool=CognitoUserPool,
            **kwargs
        )
        super(CognitoMemberDefinition, self).__init__(**processed_kwargs)


class MemberDefinition(troposphere.sagemaker.MemberDefinition, Mixin):
    def __init__(self,
                 title=None,
                 CognitoMemberDefinition=REQUIRED, # type: _CognitoMemberDefinition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CognitoMemberDefinition=CognitoMemberDefinition,
            **kwargs
        )
        super(MemberDefinition, self).__init__(**processed_kwargs)


class NotificationConfiguration(troposphere.sagemaker.NotificationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 NotificationTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NotificationTopicArn=NotificationTopicArn,
            **kwargs
        )
        super(NotificationConfiguration, self).__init__(**processed_kwargs)


class Workteam(troposphere.sagemaker.Workteam, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 MemberDefinitions=NOTHING, # type: List[_MemberDefinition]
                 NotificationConfiguration=NOTHING, # type: _NotificationConfiguration
                 Tags=NOTHING, # type: _Tags
                 WorkteamName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            MemberDefinitions=MemberDefinitions,
            NotificationConfiguration=NotificationConfiguration,
            Tags=Tags,
            WorkteamName=WorkteamName,
            **kwargs
        )
        super(Workteam, self).__init__(**processed_kwargs)
