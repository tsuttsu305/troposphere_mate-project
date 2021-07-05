# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.efs

from troposphere.efs import (
    BackupPolicy as _BackupPolicy,
    CreationInfo as _CreationInfo,
    LifecyclePolicy as _LifecyclePolicy,
    PosixUser as _PosixUser,
    RootDirectory as _RootDirectory,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class PosixUser(troposphere.efs.PosixUser, Mixin):
    def __init__(self,
                 title=None,
                 Gid=REQUIRED, # type: Union[str, AWSHelperFn]
                 Uid=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecondaryGids=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Gid=Gid,
            Uid=Uid,
            SecondaryGids=SecondaryGids,
            **kwargs
        )
        super(PosixUser, self).__init__(**processed_kwargs)


class CreationInfo(troposphere.efs.CreationInfo, Mixin):
    def __init__(self,
                 title=None,
                 OwnerGid=REQUIRED, # type: Union[str, AWSHelperFn]
                 OwnerUid=REQUIRED, # type: Union[str, AWSHelperFn]
                 Permissions=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OwnerGid=OwnerGid,
            OwnerUid=OwnerUid,
            Permissions=Permissions,
            **kwargs
        )
        super(CreationInfo, self).__init__(**processed_kwargs)


class RootDirectory(troposphere.efs.RootDirectory, Mixin):
    def __init__(self,
                 title=None,
                 CreationInfo=NOTHING, # type: _CreationInfo
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CreationInfo=CreationInfo,
            Path=Path,
            **kwargs
        )
        super(RootDirectory, self).__init__(**processed_kwargs)


class AccessPoint(troposphere.efs.AccessPoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FileSystemId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessPointTags=NOTHING, # type: _Tags
                 ClientToken=NOTHING, # type: Union[str, AWSHelperFn]
                 PosixUser=NOTHING, # type: _PosixUser
                 RootDirectory=NOTHING, # type: _RootDirectory
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FileSystemId=FileSystemId,
            AccessPointTags=AccessPointTags,
            ClientToken=ClientToken,
            PosixUser=PosixUser,
            RootDirectory=RootDirectory,
            **kwargs
        )
        super(AccessPoint, self).__init__(**processed_kwargs)


class LifecyclePolicy(troposphere.efs.LifecyclePolicy, Mixin):
    def __init__(self,
                 title=None,
                 TransitionToIA=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TransitionToIA=TransitionToIA,
            **kwargs
        )
        super(LifecyclePolicy, self).__init__(**processed_kwargs)


class BackupPolicy(troposphere.efs.BackupPolicy, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            **kwargs
        )
        super(BackupPolicy, self).__init__(**processed_kwargs)


class FileSystem(troposphere.efs.FileSystem, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AvailabilityZoneName=NOTHING, # type: Union[str, AWSHelperFn]
                 BackupPolicy=NOTHING, # type: _BackupPolicy
                 Encrypted=NOTHING, # type: bool
                 FileSystemPolicy=NOTHING, # type: dict
                 FileSystemTags=NOTHING, # type: _Tags
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LifecyclePolicies=NOTHING, # type: List[_LifecyclePolicy]
                 PerformanceMode=NOTHING, # type: Union[str, AWSHelperFn]
                 ProvisionedThroughputInMibps=NOTHING, # type: float
                 ThroughputMode=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AvailabilityZoneName=AvailabilityZoneName,
            BackupPolicy=BackupPolicy,
            Encrypted=Encrypted,
            FileSystemPolicy=FileSystemPolicy,
            FileSystemTags=FileSystemTags,
            KmsKeyId=KmsKeyId,
            LifecyclePolicies=LifecyclePolicies,
            PerformanceMode=PerformanceMode,
            ProvisionedThroughputInMibps=ProvisionedThroughputInMibps,
            ThroughputMode=ThroughputMode,
            **kwargs
        )
        super(FileSystem, self).__init__(**processed_kwargs)


class MountTarget(troposphere.efs.MountTarget, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FileSystemId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecurityGroups=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 IpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FileSystemId=FileSystemId,
            SecurityGroups=SecurityGroups,
            SubnetId=SubnetId,
            IpAddress=IpAddress,
            **kwargs
        )
        super(MountTarget, self).__init__(**processed_kwargs)
