# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.fsx

from troposphere.fsx import (
    LustreConfiguration as _LustreConfiguration,
    SelfManagedActiveDirectoryConfiguration as _SelfManagedActiveDirectoryConfiguration,
    Tags as _Tags,
    WindowsConfiguration as _WindowsConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class LustreConfiguration(troposphere.fsx.LustreConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AutoImportPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 AutomaticBackupRetentionDays=NOTHING, # type: int
                 CopyTagsToBackups=NOTHING, # type: bool
                 DailyAutomaticBackupStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentType=NOTHING, # type: Any
                 DriveCacheType=NOTHING, # type: Union[str, AWSHelperFn]
                 ExportPath=NOTHING, # type: Union[str, AWSHelperFn]
                 ImportedFileChunkSize=NOTHING, # type: int
                 ImportPath=NOTHING, # type: Union[str, AWSHelperFn]
                 PerUnitStorageThroughput=NOTHING, # type: Any
                 WeeklyMaintenanceStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutoImportPolicy=AutoImportPolicy,
            AutomaticBackupRetentionDays=AutomaticBackupRetentionDays,
            CopyTagsToBackups=CopyTagsToBackups,
            DailyAutomaticBackupStartTime=DailyAutomaticBackupStartTime,
            DeploymentType=DeploymentType,
            DriveCacheType=DriveCacheType,
            ExportPath=ExportPath,
            ImportedFileChunkSize=ImportedFileChunkSize,
            ImportPath=ImportPath,
            PerUnitStorageThroughput=PerUnitStorageThroughput,
            WeeklyMaintenanceStartTime=WeeklyMaintenanceStartTime,
            **kwargs
        )
        super(LustreConfiguration, self).__init__(**processed_kwargs)


class SelfManagedActiveDirectoryConfiguration(troposphere.fsx.SelfManagedActiveDirectoryConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DnsIps=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DomainName=NOTHING, # type: Union[str, AWSHelperFn]
                 FileSystemAdministratorsGroup=NOTHING, # type: Union[str, AWSHelperFn]
                 OrganizationalUnitDistinguishedName=NOTHING, # type: Union[str, AWSHelperFn]
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 UserName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DnsIps=DnsIps,
            DomainName=DomainName,
            FileSystemAdministratorsGroup=FileSystemAdministratorsGroup,
            OrganizationalUnitDistinguishedName=OrganizationalUnitDistinguishedName,
            Password=Password,
            UserName=UserName,
            **kwargs
        )
        super(SelfManagedActiveDirectoryConfiguration, self).__init__(**processed_kwargs)


class WindowsConfiguration(troposphere.fsx.WindowsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ThroughputCapacity=REQUIRED, # type: int
                 ActiveDirectoryId=NOTHING, # type: Union[str, AWSHelperFn]
                 Aliases=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 AutomaticBackupRetentionDays=NOTHING, # type: int
                 CopyTagsToBackups=NOTHING, # type: bool
                 DailyAutomaticBackupStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 DeploymentType=NOTHING, # type: Union[str, AWSHelperFn]
                 PreferredSubnetId=NOTHING, # type: Union[str, AWSHelperFn]
                 SelfManagedActiveDirectoryConfiguration=NOTHING, # type: _SelfManagedActiveDirectoryConfiguration
                 WeeklyMaintenanceStartTime=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ThroughputCapacity=ThroughputCapacity,
            ActiveDirectoryId=ActiveDirectoryId,
            Aliases=Aliases,
            AutomaticBackupRetentionDays=AutomaticBackupRetentionDays,
            CopyTagsToBackups=CopyTagsToBackups,
            DailyAutomaticBackupStartTime=DailyAutomaticBackupStartTime,
            DeploymentType=DeploymentType,
            PreferredSubnetId=PreferredSubnetId,
            SelfManagedActiveDirectoryConfiguration=SelfManagedActiveDirectoryConfiguration,
            WeeklyMaintenanceStartTime=WeeklyMaintenanceStartTime,
            **kwargs
        )
        super(WindowsConfiguration, self).__init__(**processed_kwargs)


class FileSystem(troposphere.fsx.FileSystem, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BackupId=NOTHING, # type: Union[str, AWSHelperFn]
                 FileSystemType=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LustreConfiguration=NOTHING, # type: _LustreConfiguration
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StorageCapacity=NOTHING, # type: int
                 StorageType=NOTHING, # type: Any
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 WindowsConfiguration=NOTHING, # type: _WindowsConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BackupId=BackupId,
            FileSystemType=FileSystemType,
            KmsKeyId=KmsKeyId,
            LustreConfiguration=LustreConfiguration,
            SecurityGroupIds=SecurityGroupIds,
            StorageCapacity=StorageCapacity,
            StorageType=StorageType,
            SubnetIds=SubnetIds,
            Tags=Tags,
            WindowsConfiguration=WindowsConfiguration,
            **kwargs
        )
        super(FileSystem, self).__init__(**processed_kwargs)
