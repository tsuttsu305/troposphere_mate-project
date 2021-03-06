# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.rds

from troposphere.rds import (
    AuthFormat as _AuthFormat,
    ConnectionPoolConfigurationInfoFormat as _ConnectionPoolConfigurationInfoFormat,
    DBClusterRole as _DBClusterRole,
    DBInstanceRole as _DBInstanceRole,
    OptionConfiguration as _OptionConfiguration,
    OptionSetting as _OptionSetting,
    ProcessorFeature as _ProcessorFeature,
    ScalingConfiguration as _ScalingConfiguration,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DBInstanceRole(troposphere.rds.DBInstanceRole, Mixin):
    def __init__(self,
                 title=None,
                 FeatureName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FeatureName=FeatureName,
            RoleArn=RoleArn,
            Status=Status,
            **kwargs
        )
        super(DBInstanceRole, self).__init__(**processed_kwargs)


class ProcessorFeature(troposphere.rds.ProcessorFeature, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(ProcessorFeature, self).__init__(**processed_kwargs)


class DBInstance(troposphere.rds.DBInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBInstanceClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllocatedStorage=NOTHING, # type: int
                 AllowMajorVersionUpgrade=NOTHING, # type: bool
                 AssociatedRoles=NOTHING, # type: List[_DBInstanceRole]
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 BackupRetentionPeriod=NOTHING, # type: Any
                 CACertificateIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 CharacterSetName=NOTHING, # type: Union[str, AWSHelperFn]
                 CopyTagsToSnapshot=NOTHING, # type: bool
                 DBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBInstanceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSecurityGroups=NOTHING, # type: list
                 DBSnapshotIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DeleteAutomatedBackups=NOTHING, # type: bool
                 DeletionProtection=NOTHING, # type: bool
                 Domain=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainIAMRoleName=NOTHING, # type: Union[str, AWSHelperFn]
                 EnableCloudwatchLogsExports=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EnableIAMDatabaseAuthentication=NOTHING, # type: bool
                 EnablePerformanceInsights=NOTHING, # type: bool
                 Engine=NOTHING, # type: Any
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Iops=NOTHING, # type: Any
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseModel=NOTHING, # type: Any
                 MasterUsername=NOTHING, # type: Union[str, AWSHelperFn]
                 MasterUserPassword=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxAllocatedStorage=NOTHING, # type: int
                 MonitoringInterval=NOTHING, # type: int
                 MonitoringRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MultiAZ=NOTHING, # type: bool
                 OptionGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 PerformanceInsightsKMSKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 PerformanceInsightsRetentionPeriod=NOTHING, # type: int
                 Port=NOTHING, # type: int
                 PreferredBackupWindow=NOTHING, # type: Any
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 ProcessorFeatures=NOTHING, # type: List[_ProcessorFeature]
                 PromotionTier=NOTHING, # type: int
                 PubliclyAccessible=NOTHING, # type: bool
                 SourceDBInstanceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageEncrypted=NOTHING, # type: bool
                 StorageType=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 UseDefaultProcessorFeatures=NOTHING, # type: bool
                 Timezone=NOTHING, # type: Union[str, AWSHelperFn]
                 VPCSecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBInstanceClass=DBInstanceClass,
            AllocatedStorage=AllocatedStorage,
            AllowMajorVersionUpgrade=AllowMajorVersionUpgrade,
            AssociatedRoles=AssociatedRoles,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AvailabilityZone=AvailabilityZone,
            BackupRetentionPeriod=BackupRetentionPeriod,
            CACertificateIdentifier=CACertificateIdentifier,
            CharacterSetName=CharacterSetName,
            CopyTagsToSnapshot=CopyTagsToSnapshot,
            DBClusterIdentifier=DBClusterIdentifier,
            DBInstanceIdentifier=DBInstanceIdentifier,
            DBName=DBName,
            DBParameterGroupName=DBParameterGroupName,
            DBSecurityGroups=DBSecurityGroups,
            DBSnapshotIdentifier=DBSnapshotIdentifier,
            DBSubnetGroupName=DBSubnetGroupName,
            DeleteAutomatedBackups=DeleteAutomatedBackups,
            DeletionProtection=DeletionProtection,
            Domain=Domain,
            DomainIAMRoleName=DomainIAMRoleName,
            EnableCloudwatchLogsExports=EnableCloudwatchLogsExports,
            EnableIAMDatabaseAuthentication=EnableIAMDatabaseAuthentication,
            EnablePerformanceInsights=EnablePerformanceInsights,
            Engine=Engine,
            EngineVersion=EngineVersion,
            Iops=Iops,
            KmsKeyId=KmsKeyId,
            LicenseModel=LicenseModel,
            MasterUsername=MasterUsername,
            MasterUserPassword=MasterUserPassword,
            MaxAllocatedStorage=MaxAllocatedStorage,
            MonitoringInterval=MonitoringInterval,
            MonitoringRoleArn=MonitoringRoleArn,
            MultiAZ=MultiAZ,
            OptionGroupName=OptionGroupName,
            PerformanceInsightsKMSKeyId=PerformanceInsightsKMSKeyId,
            PerformanceInsightsRetentionPeriod=PerformanceInsightsRetentionPeriod,
            Port=Port,
            PreferredBackupWindow=PreferredBackupWindow,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            ProcessorFeatures=ProcessorFeatures,
            PromotionTier=PromotionTier,
            PubliclyAccessible=PubliclyAccessible,
            SourceDBInstanceIdentifier=SourceDBInstanceIdentifier,
            SourceRegion=SourceRegion,
            StorageEncrypted=StorageEncrypted,
            StorageType=StorageType,
            Tags=Tags,
            UseDefaultProcessorFeatures=UseDefaultProcessorFeatures,
            Timezone=Timezone,
            VPCSecurityGroups=VPCSecurityGroups,
            **kwargs
        )
        super(DBInstance, self).__init__(**processed_kwargs)


class DBParameterGroup(troposphere.rds.DBParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Family=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Family=Family,
            Parameters=Parameters,
            Tags=Tags,
            **kwargs
        )
        super(DBParameterGroup, self).__init__(**processed_kwargs)


class AuthFormat(troposphere.rds.AuthFormat, Mixin):
    def __init__(self,
                 title=None,
                 AuthScheme=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 IAMAuth=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretArn=NOTHING, # type: Union[str, AWSHelperFn]
                 UserName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthScheme=AuthScheme,
            Description=Description,
            IAMAuth=IAMAuth,
            SecretArn=SecretArn,
            UserName=UserName,
            **kwargs
        )
        super(AuthFormat, self).__init__(**processed_kwargs)


class DBProxy(troposphere.rds.DBProxy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Auth=REQUIRED, # type: List[_AuthFormat]
                 DBProxyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineFamily=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcSubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 DebugLogging=NOTHING, # type: bool
                 IdleClientTimeout=NOTHING, # type: int
                 RequireTLS=NOTHING, # type: bool
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Auth=Auth,
            DBProxyName=DBProxyName,
            EngineFamily=EngineFamily,
            RoleArn=RoleArn,
            VpcSubnetIds=VpcSubnetIds,
            DebugLogging=DebugLogging,
            IdleClientTimeout=IdleClientTimeout,
            RequireTLS=RequireTLS,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(DBProxy, self).__init__(**processed_kwargs)


class DBProxyEndpoint(troposphere.rds.DBProxyEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBProxyEndpointName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DBProxyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcSubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 TargetRole=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBProxyEndpointName=DBProxyEndpointName,
            DBProxyName=DBProxyName,
            VpcSubnetIds=VpcSubnetIds,
            Tags=Tags,
            TargetRole=TargetRole,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(DBProxyEndpoint, self).__init__(**processed_kwargs)


class ConnectionPoolConfigurationInfoFormat(troposphere.rds.ConnectionPoolConfigurationInfoFormat, Mixin):
    def __init__(self,
                 title=None,
                 ConnectionBorrowTimeout=NOTHING, # type: int
                 InitQuery=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxConnectionsPercent=NOTHING, # type: int
                 MaxIdleConnectionsPercent=NOTHING, # type: int
                 SessionPinningFilters=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectionBorrowTimeout=ConnectionBorrowTimeout,
            InitQuery=InitQuery,
            MaxConnectionsPercent=MaxConnectionsPercent,
            MaxIdleConnectionsPercent=MaxIdleConnectionsPercent,
            SessionPinningFilters=SessionPinningFilters,
            **kwargs
        )
        super(ConnectionPoolConfigurationInfoFormat, self).__init__(**processed_kwargs)


class DBProxyTargetGroup(troposphere.rds.DBProxyTargetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBProxyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectionPoolConfigurationInfo=NOTHING, # type: _ConnectionPoolConfigurationInfoFormat
                 DBClusterIdentifiers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 DBInstanceIdentifiers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBProxyName=DBProxyName,
            TargetGroupName=TargetGroupName,
            ConnectionPoolConfigurationInfo=ConnectionPoolConfigurationInfo,
            DBClusterIdentifiers=DBClusterIdentifiers,
            DBInstanceIdentifiers=DBInstanceIdentifiers,
            **kwargs
        )
        super(DBProxyTargetGroup, self).__init__(**processed_kwargs)


class DBSubnetGroup(troposphere.rds.DBSubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBSubnetGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: list
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBSubnetGroupDescription=DBSubnetGroupDescription,
            SubnetIds=SubnetIds,
            DBSubnetGroupName=DBSubnetGroupName,
            Tags=Tags,
            **kwargs
        )
        super(DBSubnetGroup, self).__init__(**processed_kwargs)


class RDSSecurityGroup(troposphere.rds.RDSSecurityGroup, Mixin):
    def __init__(self,
                 title=None,
                 CIDRIP=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CIDRIP=CIDRIP,
            EC2SecurityGroupId=EC2SecurityGroupId,
            EC2SecurityGroupName=EC2SecurityGroupName,
            EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId,
            **kwargs
        )
        super(RDSSecurityGroup, self).__init__(**processed_kwargs)


class DBSecurityGroup(troposphere.rds.DBSecurityGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBSecurityGroupIngress=REQUIRED, # type: list
                 GroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 EC2VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBSecurityGroupIngress=DBSecurityGroupIngress,
            GroupDescription=GroupDescription,
            EC2VpcId=EC2VpcId,
            Tags=Tags,
            **kwargs
        )
        super(DBSecurityGroup, self).__init__(**processed_kwargs)


class DBSecurityGroupIngress(troposphere.rds.DBSecurityGroupIngress, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DBSecurityGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CIDRIP=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupId=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 EC2SecurityGroupOwnerId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DBSecurityGroupName=DBSecurityGroupName,
            CIDRIP=CIDRIP,
            EC2SecurityGroupId=EC2SecurityGroupId,
            EC2SecurityGroupName=EC2SecurityGroupName,
            EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId,
            **kwargs
        )
        super(DBSecurityGroupIngress, self).__init__(**processed_kwargs)


class EventSubscription(troposphere.rds.EventSubscription, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SnsTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 EventCategories=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SnsTopicArn=SnsTopicArn,
            Enabled=Enabled,
            EventCategories=EventCategories,
            SourceIds=SourceIds,
            SourceType=SourceType,
            **kwargs
        )
        super(EventSubscription, self).__init__(**processed_kwargs)


class GlobalCluster(troposphere.rds.GlobalCluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeletionProtection=NOTHING, # type: bool
                 Engine=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 GlobalClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceDBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageEncrypted=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeletionProtection=DeletionProtection,
            Engine=Engine,
            EngineVersion=EngineVersion,
            GlobalClusterIdentifier=GlobalClusterIdentifier,
            SourceDBClusterIdentifier=SourceDBClusterIdentifier,
            StorageEncrypted=StorageEncrypted,
            **kwargs
        )
        super(GlobalCluster, self).__init__(**processed_kwargs)


class OptionSetting(troposphere.rds.OptionSetting, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(OptionSetting, self).__init__(**processed_kwargs)


class OptionConfiguration(troposphere.rds.OptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 OptionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DBSecurityGroupMemberships=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 OptionSettings=NOTHING, # type: List[_OptionSetting]
                 OptionVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 VpcSecurityGroupMemberships=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OptionName=OptionName,
            DBSecurityGroupMemberships=DBSecurityGroupMemberships,
            OptionSettings=OptionSettings,
            OptionVersion=OptionVersion,
            Port=Port,
            VpcSecurityGroupMemberships=VpcSecurityGroupMemberships,
            **kwargs
        )
        super(OptionConfiguration, self).__init__(**processed_kwargs)


class OptionGroup(troposphere.rds.OptionGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EngineName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MajorEngineVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 OptionGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 OptionConfigurations=REQUIRED, # type: List[_OptionConfiguration]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EngineName=EngineName,
            MajorEngineVersion=MajorEngineVersion,
            OptionGroupDescription=OptionGroupDescription,
            OptionConfigurations=OptionConfigurations,
            Tags=Tags,
            **kwargs
        )
        super(OptionGroup, self).__init__(**processed_kwargs)


class DBClusterParameterGroup(troposphere.rds.DBClusterParameterGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 Family=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            Family=Family,
            Parameters=Parameters,
            Tags=Tags,
            **kwargs
        )
        super(DBClusterParameterGroup, self).__init__(**processed_kwargs)


class DBClusterRole(troposphere.rds.DBClusterRole, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 FeatureName=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            FeatureName=FeatureName,
            Status=Status,
            **kwargs
        )
        super(DBClusterRole, self).__init__(**processed_kwargs)


class ScalingConfiguration(troposphere.rds.ScalingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AutoPause=NOTHING, # type: bool
                 MaxCapacity=NOTHING, # type: Any
                 MinCapacity=NOTHING, # type: Any
                 SecondsUntilAutoPause=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutoPause=AutoPause,
            MaxCapacity=MaxCapacity,
            MinCapacity=MinCapacity,
            SecondsUntilAutoPause=SecondsUntilAutoPause,
            **kwargs
        )
        super(ScalingConfiguration, self).__init__(**processed_kwargs)


class DBCluster(troposphere.rds.DBCluster, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Engine=REQUIRED, # type: Any
                 AssociatedRoles=NOTHING, # type: List[_DBClusterRole]
                 AvailabilityZones=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 BacktrackWindow=NOTHING, # type: Any
                 BackupRetentionPeriod=NOTHING, # type: Any
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 DBClusterParameterGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DBSubnetGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 DeletionProtection=NOTHING, # type: bool
                 EnableCloudwatchLogsExports=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EnableHttpEndpoint=NOTHING, # type: bool
                 EnableIAMDatabaseAuthentication=NOTHING, # type: bool
                 EngineMode=NOTHING, # type: Any
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 MasterUsername=NOTHING, # type: Union[str, AWSHelperFn]
                 MasterUserPassword=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 PreferredBackupWindow=NOTHING, # type: Any
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationSourceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 RestoreType=NOTHING, # type: Union[str, AWSHelperFn]
                 ScalingConfiguration=NOTHING, # type: _ScalingConfiguration
                 SnapshotIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceDBClusterIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 StorageEncrypted=NOTHING, # type: bool
                 Tags=NOTHING, # type: Union[_Tags, list]
                 UseLatestRestorableTime=NOTHING, # type: bool
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Engine=Engine,
            AssociatedRoles=AssociatedRoles,
            AvailabilityZones=AvailabilityZones,
            BacktrackWindow=BacktrackWindow,
            BackupRetentionPeriod=BackupRetentionPeriod,
            DatabaseName=DatabaseName,
            DBClusterIdentifier=DBClusterIdentifier,
            DBClusterParameterGroupName=DBClusterParameterGroupName,
            DBSubnetGroupName=DBSubnetGroupName,
            DeletionProtection=DeletionProtection,
            EnableCloudwatchLogsExports=EnableCloudwatchLogsExports,
            EnableHttpEndpoint=EnableHttpEndpoint,
            EnableIAMDatabaseAuthentication=EnableIAMDatabaseAuthentication,
            EngineMode=EngineMode,
            EngineVersion=EngineVersion,
            KmsKeyId=KmsKeyId,
            MasterUsername=MasterUsername,
            MasterUserPassword=MasterUserPassword,
            Port=Port,
            PreferredBackupWindow=PreferredBackupWindow,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            ReplicationSourceIdentifier=ReplicationSourceIdentifier,
            RestoreType=RestoreType,
            ScalingConfiguration=ScalingConfiguration,
            SnapshotIdentifier=SnapshotIdentifier,
            SourceDBClusterIdentifier=SourceDBClusterIdentifier,
            SourceRegion=SourceRegion,
            StorageEncrypted=StorageEncrypted,
            Tags=Tags,
            UseLatestRestorableTime=UseLatestRestorableTime,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(DBCluster, self).__init__(**processed_kwargs)
