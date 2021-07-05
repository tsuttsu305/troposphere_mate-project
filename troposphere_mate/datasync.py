# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.datasync

from troposphere.datasync import (
    Ec2Config as _Ec2Config,
    FilterRule as _FilterRule,
    MountOptions as _MountOptions,
    OnPremConfig as _OnPremConfig,
    Options as _Options,
    S3Config as _S3Config,
    Tags as _Tags,
    TaskSchedule as _TaskSchedule,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Agent(troposphere.datasync.Agent, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ActivationKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 AgentName=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 VpcEndpointId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ActivationKey=ActivationKey,
            AgentName=AgentName,
            SecurityGroupArns=SecurityGroupArns,
            SubnetArns=SubnetArns,
            Tags=Tags,
            VpcEndpointId=VpcEndpointId,
            **kwargs
        )
        super(Agent, self).__init__(**processed_kwargs)


class Ec2Config(troposphere.datasync.Ec2Config, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupArns=SecurityGroupArns,
            SubnetArn=SubnetArn,
            **kwargs
        )
        super(Ec2Config, self).__init__(**processed_kwargs)


class LocationEFS(troposphere.datasync.LocationEFS, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Ec2Config=REQUIRED, # type: _Ec2Config
                 EfsFilesystemArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Subdirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Ec2Config=Ec2Config,
            EfsFilesystemArn=EfsFilesystemArn,
            Subdirectory=Subdirectory,
            Tags=Tags,
            **kwargs
        )
        super(LocationEFS, self).__init__(**processed_kwargs)


class LocationFSxWindows(troposphere.datasync.LocationFSxWindows, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FsxFilesystemArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecurityGroupArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 User=REQUIRED, # type: Union[str, AWSHelperFn]
                 Domain=NOTHING, # type: Union[str, AWSHelperFn]
                 Subdirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FsxFilesystemArn=FsxFilesystemArn,
            Password=Password,
            SecurityGroupArns=SecurityGroupArns,
            User=User,
            Domain=Domain,
            Subdirectory=Subdirectory,
            Tags=Tags,
            **kwargs
        )
        super(LocationFSxWindows, self).__init__(**processed_kwargs)


class MountOptions(troposphere.datasync.MountOptions, Mixin):
    def __init__(self,
                 title=None,
                 Version=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Version=Version,
            **kwargs
        )
        super(MountOptions, self).__init__(**processed_kwargs)


class OnPremConfig(troposphere.datasync.OnPremConfig, Mixin):
    def __init__(self,
                 title=None,
                 AgentArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AgentArns=AgentArns,
            **kwargs
        )
        super(OnPremConfig, self).__init__(**processed_kwargs)


class LocationNFS(troposphere.datasync.LocationNFS, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 OnPremConfig=REQUIRED, # type: _OnPremConfig
                 ServerHostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 Subdirectory=REQUIRED, # type: Union[str, AWSHelperFn]
                 MountOptions=NOTHING, # type: _MountOptions
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            OnPremConfig=OnPremConfig,
            ServerHostname=ServerHostname,
            Subdirectory=Subdirectory,
            MountOptions=MountOptions,
            Tags=Tags,
            **kwargs
        )
        super(LocationNFS, self).__init__(**processed_kwargs)


class LocationObjectStorage(troposphere.datasync.LocationObjectStorage, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AgentArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerHostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessKey=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretKey=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerPort=NOTHING, # type: int
                 ServerProtocol=NOTHING, # type: Union[str, AWSHelperFn]
                 Subdirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AgentArns=AgentArns,
            BucketName=BucketName,
            ServerHostname=ServerHostname,
            AccessKey=AccessKey,
            SecretKey=SecretKey,
            ServerPort=ServerPort,
            ServerProtocol=ServerProtocol,
            Subdirectory=Subdirectory,
            Tags=Tags,
            **kwargs
        )
        super(LocationObjectStorage, self).__init__(**processed_kwargs)


class S3Config(troposphere.datasync.S3Config, Mixin):
    def __init__(self,
                 title=None,
                 BucketAccessRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketAccessRoleArn=BucketAccessRoleArn,
            **kwargs
        )
        super(S3Config, self).__init__(**processed_kwargs)


class LocationS3(troposphere.datasync.LocationS3, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 S3BucketArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Config=REQUIRED, # type: _S3Config
                 S3StorageClass=NOTHING, # type: Union[str, AWSHelperFn]
                 Subdirectory=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            S3BucketArn=S3BucketArn,
            S3Config=S3Config,
            S3StorageClass=S3StorageClass,
            Subdirectory=Subdirectory,
            Tags=Tags,
            **kwargs
        )
        super(LocationS3, self).__init__(**processed_kwargs)


class LocationSMB(troposphere.datasync.LocationSMB, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AgentArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerHostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 Subdirectory=REQUIRED, # type: Union[str, AWSHelperFn]
                 User=REQUIRED, # type: Union[str, AWSHelperFn]
                 Domain=NOTHING, # type: Union[str, AWSHelperFn]
                 MountOptions=NOTHING, # type: _MountOptions
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AgentArns=AgentArns,
            Password=Password,
            ServerHostname=ServerHostname,
            Subdirectory=Subdirectory,
            User=User,
            Domain=Domain,
            MountOptions=MountOptions,
            Tags=Tags,
            **kwargs
        )
        super(LocationSMB, self).__init__(**processed_kwargs)


class FilterRule(troposphere.datasync.FilterRule, Mixin):
    def __init__(self,
                 title=None,
                 FilterType=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FilterType=FilterType,
            Value=Value,
            **kwargs
        )
        super(FilterRule, self).__init__(**processed_kwargs)


class Options(troposphere.datasync.Options, Mixin):
    def __init__(self,
                 title=None,
                 Atime=NOTHING, # type: Union[str, AWSHelperFn]
                 BytesPerSecond=NOTHING, # type: int
                 Gid=NOTHING, # type: Union[str, AWSHelperFn]
                 LogLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 Mtime=NOTHING, # type: Union[str, AWSHelperFn]
                 OverwriteMode=NOTHING, # type: Union[str, AWSHelperFn]
                 PosixPermissions=NOTHING, # type: Union[str, AWSHelperFn]
                 PreserveDeletedFiles=NOTHING, # type: Union[str, AWSHelperFn]
                 PreserveDevices=NOTHING, # type: Union[str, AWSHelperFn]
                 TaskQueueing=NOTHING, # type: Union[str, AWSHelperFn]
                 TransferMode=NOTHING, # type: Union[str, AWSHelperFn]
                 Uid=NOTHING, # type: Union[str, AWSHelperFn]
                 VerifyMode=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Atime=Atime,
            BytesPerSecond=BytesPerSecond,
            Gid=Gid,
            LogLevel=LogLevel,
            Mtime=Mtime,
            OverwriteMode=OverwriteMode,
            PosixPermissions=PosixPermissions,
            PreserveDeletedFiles=PreserveDeletedFiles,
            PreserveDevices=PreserveDevices,
            TaskQueueing=TaskQueueing,
            TransferMode=TransferMode,
            Uid=Uid,
            VerifyMode=VerifyMode,
            **kwargs
        )
        super(Options, self).__init__(**processed_kwargs)


class TaskSchedule(troposphere.datasync.TaskSchedule, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(TaskSchedule, self).__init__(**processed_kwargs)


class Task(troposphere.datasync.Task, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationLocationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceLocationArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CloudWatchLogGroupArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Excludes=NOTHING, # type: List[_FilterRule]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Options=NOTHING, # type: _Options
                 Schedule=NOTHING, # type: _TaskSchedule
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationLocationArn=DestinationLocationArn,
            SourceLocationArn=SourceLocationArn,
            CloudWatchLogGroupArn=CloudWatchLogGroupArn,
            Excludes=Excludes,
            Name=Name,
            Options=Options,
            Schedule=Schedule,
            Tags=Tags,
            **kwargs
        )
        super(Task, self).__init__(**processed_kwargs)
