# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.imagebuilder

from troposphere.imagebuilder import (
    ComponentConfiguration as _ComponentConfiguration,
    Distribution as _Distribution,
    EbsInstanceBlockDeviceSpecification as _EbsInstanceBlockDeviceSpecification,
    ImageTestsConfiguration as _ImageTestsConfiguration,
    InstanceBlockDeviceMapping as _InstanceBlockDeviceMapping,
    Logging as _Logging,
    S3Logs as _S3Logs,
    Schedule as _Schedule,
    Tags as _Tags,
    TargetContainerRepository as _TargetContainerRepository,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Component(troposphere.imagebuilder.Component, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Platform=REQUIRED, # type: Any
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 ChangeDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 Data=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 Uri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Platform=Platform,
            Version=Version,
            ChangeDescription=ChangeDescription,
            Data=Data,
            Description=Description,
            KmsKeyId=KmsKeyId,
            Tags=Tags,
            Uri=Uri,
            **kwargs
        )
        super(Component, self).__init__(**processed_kwargs)


class ComponentConfiguration(troposphere.imagebuilder.ComponentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ComponentArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComponentArn=ComponentArn,
            **kwargs
        )
        super(ComponentConfiguration, self).__init__(**processed_kwargs)


class TargetContainerRepository(troposphere.imagebuilder.TargetContainerRepository, Mixin):
    def __init__(self,
                 title=None,
                 RepositoryName=NOTHING, # type: Union[str, AWSHelperFn]
                 Service=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RepositoryName=RepositoryName,
            Service=Service,
            **kwargs
        )
        super(TargetContainerRepository, self).__init__(**processed_kwargs)


class ContainerRecipe(troposphere.imagebuilder.ContainerRecipe, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Components=REQUIRED, # type: List[_ComponentConfiguration]
                 ContainerType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParentImage=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetRepository=REQUIRED, # type: _TargetContainerRepository
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DockerfileTemplateData=NOTHING, # type: Union[str, AWSHelperFn]
                 DockerfileTemplateUri=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageOsVersionOverride=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 PlatformOverride=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 WorkingDirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Components=Components,
            ContainerType=ContainerType,
            Name=Name,
            ParentImage=ParentImage,
            TargetRepository=TargetRepository,
            Version=Version,
            Description=Description,
            DockerfileTemplateData=DockerfileTemplateData,
            DockerfileTemplateUri=DockerfileTemplateUri,
            ImageOsVersionOverride=ImageOsVersionOverride,
            KmsKeyId=KmsKeyId,
            PlatformOverride=PlatformOverride,
            Tags=Tags,
            WorkingDirectory=WorkingDirectory,
            **kwargs
        )
        super(ContainerRecipe, self).__init__(**processed_kwargs)


class Distribution(troposphere.imagebuilder.Distribution, Mixin):
    def __init__(self,
                 title=None,
                 AmiDistributionConfiguration=NOTHING, # type: dict
                 LicenseConfigurationArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Region=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AmiDistributionConfiguration=AmiDistributionConfiguration,
            LicenseConfigurationArns=LicenseConfigurationArns,
            Region=Region,
            **kwargs
        )
        super(Distribution, self).__init__(**processed_kwargs)


class DistributionConfiguration(troposphere.imagebuilder.DistributionConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Distributions=REQUIRED, # type: List[_Distribution]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Distributions=Distributions,
            Name=Name,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(DistributionConfiguration, self).__init__(**processed_kwargs)


class ImageTestsConfiguration(troposphere.imagebuilder.ImageTestsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ImageTestsEnabled=NOTHING, # type: bool
                 TimeoutMinutes=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ImageTestsEnabled=ImageTestsEnabled,
            TimeoutMinutes=TimeoutMinutes,
            **kwargs
        )
        super(ImageTestsConfiguration, self).__init__(**processed_kwargs)


class Image(troposphere.imagebuilder.Image, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ImageRecipeArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ImageTestsConfiguration=REQUIRED, # type: _ImageTestsConfiguration
                 InfrastructureConfigurationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DistributionConfigurationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ImageRecipeArn=ImageRecipeArn,
            ImageTestsConfiguration=ImageTestsConfiguration,
            InfrastructureConfigurationArn=InfrastructureConfigurationArn,
            DistributionConfigurationArn=DistributionConfigurationArn,
            Tags=Tags,
            **kwargs
        )
        super(Image, self).__init__(**processed_kwargs)


class S3Logs(troposphere.imagebuilder.S3Logs, Mixin):
    def __init__(self,
                 title=None,
                 S3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 S3KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3BucketName=S3BucketName,
            S3KeyPrefix=S3KeyPrefix,
            **kwargs
        )
        super(S3Logs, self).__init__(**processed_kwargs)


class Logging(troposphere.imagebuilder.Logging, Mixin):
    def __init__(self,
                 title=None,
                 S3Logs=NOTHING, # type: _S3Logs
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Logs=S3Logs,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class InfrastructureConfiguration(troposphere.imagebuilder.InfrastructureConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceProfileName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 InstanceTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 KeyPair=NOTHING, # type: Union[str, AWSHelperFn]
                 Logging=NOTHING, # type: _Logging
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SnsTopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 TerminateInstanceOnFailure=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceProfileName=InstanceProfileName,
            Name=Name,
            Description=Description,
            InstanceTypes=InstanceTypes,
            KeyPair=KeyPair,
            Logging=Logging,
            SecurityGroupIds=SecurityGroupIds,
            SnsTopicArn=SnsTopicArn,
            SubnetId=SubnetId,
            Tags=Tags,
            TerminateInstanceOnFailure=TerminateInstanceOnFailure,
            **kwargs
        )
        super(InfrastructureConfiguration, self).__init__(**processed_kwargs)


class EbsInstanceBlockDeviceSpecification(troposphere.imagebuilder.EbsInstanceBlockDeviceSpecification, Mixin):
    def __init__(self,
                 title=None,
                 DeleteOnTermination=NOTHING, # type: bool
                 Encrypted=NOTHING, # type: bool
                 Iops=NOTHING, # type: int
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 SnapshotId=NOTHING, # type: Union[str, AWSHelperFn]
                 VolumeSize=NOTHING, # type: int
                 VolumeType=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeleteOnTermination=DeleteOnTermination,
            Encrypted=Encrypted,
            Iops=Iops,
            KmsKeyId=KmsKeyId,
            SnapshotId=SnapshotId,
            VolumeSize=VolumeSize,
            VolumeType=VolumeType,
            **kwargs
        )
        super(EbsInstanceBlockDeviceSpecification, self).__init__(**processed_kwargs)


class InstanceBlockDeviceMapping(troposphere.imagebuilder.InstanceBlockDeviceMapping, Mixin):
    def __init__(self,
                 title=None,
                 DeviceName=NOTHING, # type: Union[str, AWSHelperFn]
                 Ebs=NOTHING, # type: _EbsInstanceBlockDeviceSpecification
                 NoDevice=NOTHING, # type: Union[str, AWSHelperFn]
                 VirtualName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeviceName=DeviceName,
            Ebs=Ebs,
            NoDevice=NoDevice,
            VirtualName=VirtualName,
            **kwargs
        )
        super(InstanceBlockDeviceMapping, self).__init__(**processed_kwargs)


class ComponentConfiguration(troposphere.imagebuilder.ComponentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ComponentArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComponentArn=ComponentArn,
            **kwargs
        )
        super(ComponentConfiguration, self).__init__(**processed_kwargs)


class ImageRecipe(troposphere.imagebuilder.ImageRecipe, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Components=REQUIRED, # type: List[_ComponentConfiguration]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParentImage=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 BlockDeviceMappings=NOTHING, # type: List[_InstanceBlockDeviceMapping]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Components=Components,
            Name=Name,
            ParentImage=ParentImage,
            Version=Version,
            BlockDeviceMappings=BlockDeviceMappings,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(ImageRecipe, self).__init__(**processed_kwargs)


class Schedule(troposphere.imagebuilder.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 PipelineExecutionStartCondition=NOTHING, # type: Any
                 ScheduleExpression=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PipelineExecutionStartCondition=PipelineExecutionStartCondition,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class ImagePipeline(troposphere.imagebuilder.ImagePipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ImageRecipeArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 InfrastructureConfigurationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DistributionConfigurationArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ImageTestsConfiguration=NOTHING, # type: _ImageTestsConfiguration
                 Schedule=NOTHING, # type: _Schedule
                 Status=NOTHING, # type: Any
                 Tags=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ImageRecipeArn=ImageRecipeArn,
            InfrastructureConfigurationArn=InfrastructureConfigurationArn,
            Name=Name,
            Description=Description,
            DistributionConfigurationArn=DistributionConfigurationArn,
            ImageTestsConfiguration=ImageTestsConfiguration,
            Schedule=Schedule,
            Status=Status,
            Tags=Tags,
            **kwargs
        )
        super(ImagePipeline, self).__init__(**processed_kwargs)
