# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sagemaker

from troposphere.sagemaker import (
    BaselineConfig as _BaselineConfig,
    CaptureContentTypeHeader as _CaptureContentTypeHeader,
    CaptureOption as _CaptureOption,
    ClusterConfig as _ClusterConfig,
    CognitoMemberDefinition as _CognitoMemberDefinition,
    ConstraintsResource as _ConstraintsResource,
    ContainerDefinition as _ContainerDefinition,
    DataCaptureConfig as _DataCaptureConfig,
    EndpointInput as _EndpointInput,
    GitConfig as _GitConfig,
    MemberDefinition as _MemberDefinition,
    MonitoringAppSpecification as _MonitoringAppSpecification,
    MonitoringExecutionSummary as _MonitoringExecutionSummary,
    MonitoringInput as _MonitoringInput,
    MonitoringInputs as _MonitoringInputs,
    MonitoringJobDefinition as _MonitoringJobDefinition,
    MonitoringOutput as _MonitoringOutput,
    MonitoringOutputConfig as _MonitoringOutputConfig,
    MonitoringResources as _MonitoringResources,
    MonitoringScheduleConfig as _MonitoringScheduleConfig,
    NetworkConfig as _NetworkConfig,
    NotebookInstanceLifecycleHook as _NotebookInstanceLifecycleHook,
    NotificationConfiguration as _NotificationConfiguration,
    ProductionVariant as _ProductionVariant,
    S3Output as _S3Output,
    ScheduleConfig as _ScheduleConfig,
    StatisticsResource as _StatisticsResource,
    StoppingCondition as _StoppingCondition,
    Tags as _Tags,
    VpcConfig as _VpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



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


class Endpoint(troposphere.sagemaker.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointConfigName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EndpointName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointConfigName=EndpointConfigName,
            EndpointName=EndpointName,
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


class ContainerDefinition(troposphere.sagemaker.ContainerDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerHostname=NOTHING, # type: Union[str, AWSHelperFn]
                 Environment=NOTHING, # type: dict
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 ModelDataUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Image=Image,
            ContainerHostname=ContainerHostname,
            Environment=Environment,
            Mode=Mode,
            ModelDataUrl=ModelDataUrl,
            **kwargs
        )
        super(ContainerDefinition, self).__init__(**processed_kwargs)


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


class Model(troposphere.sagemaker.Model, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Containers=NOTHING, # type: List[_ContainerDefinition]
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
            ModelName=ModelName,
            PrimaryContainer=PrimaryContainer,
            Tags=Tags,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Model, self).__init__(**processed_kwargs)


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
