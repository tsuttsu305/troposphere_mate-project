# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.dms

from troposphere.dms import (
    DocDbSettings as _DocDbSettings,
    DynamoDbSettings as _DynamoDbSettings,
    ElasticsearchSettings as _ElasticsearchSettings,
    IbmDb2Settings as _IbmDb2Settings,
    KafkaSettings as _KafkaSettings,
    KinesisSettings as _KinesisSettings,
    MicrosoftSqlServerSettings as _MicrosoftSqlServerSettings,
    MongoDbSettings as _MongoDbSettings,
    MySqlSettings as _MySqlSettings,
    NeptuneSettings as _NeptuneSettings,
    OracleSettings as _OracleSettings,
    PostgreSqlSettings as _PostgreSqlSettings,
    RedshiftSettings as _RedshiftSettings,
    S3Settings as _S3Settings,
    SybaseSettings as _SybaseSettings,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Certificate(troposphere.dms.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CertificateIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificatePem=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateWallet=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateIdentifier=CertificateIdentifier,
            CertificatePem=CertificatePem,
            CertificateWallet=CertificateWallet,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)


class DocDbSettings(troposphere.dms.DocDbSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(DocDbSettings, self).__init__(**processed_kwargs)


class DynamoDbSettings(troposphere.dms.DynamoDbSettings, Mixin):
    def __init__(self,
                 title=None,
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(DynamoDbSettings, self).__init__(**processed_kwargs)


class ElasticsearchSettings(troposphere.dms.ElasticsearchSettings, Mixin):
    def __init__(self,
                 title=None,
                 EndpointUri=NOTHING, # type: Union[str, AWSHelperFn]
                 ErrorRetryDuration=NOTHING, # type: int
                 FullLoadErrorPercentage=NOTHING, # type: int
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EndpointUri=EndpointUri,
            ErrorRetryDuration=ErrorRetryDuration,
            FullLoadErrorPercentage=FullLoadErrorPercentage,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(ElasticsearchSettings, self).__init__(**processed_kwargs)


class IbmDb2Settings(troposphere.dms.IbmDb2Settings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(IbmDb2Settings, self).__init__(**processed_kwargs)


class KafkaSettings(troposphere.dms.KafkaSettings, Mixin):
    def __init__(self,
                 title=None,
                 Broker=NOTHING, # type: Union[str, AWSHelperFn]
                 Topic=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Broker=Broker,
            Topic=Topic,
            **kwargs
        )
        super(KafkaSettings, self).__init__(**processed_kwargs)


class KinesisSettings(troposphere.dms.KinesisSettings, Mixin):
    def __init__(self,
                 title=None,
                 MessageFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MessageFormat=MessageFormat,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            StreamArn=StreamArn,
            **kwargs
        )
        super(KinesisSettings, self).__init__(**processed_kwargs)


class MicrosoftSqlServerSettings(troposphere.dms.MicrosoftSqlServerSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(MicrosoftSqlServerSettings, self).__init__(**processed_kwargs)


class MongoDbSettings(troposphere.dms.MongoDbSettings, Mixin):
    def __init__(self,
                 title=None,
                 AuthMechanism=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthSource=NOTHING, # type: Union[str, AWSHelperFn]
                 AuthType=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 DocsToInvestigate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtractDocId=NOTHING, # type: Union[str, AWSHelperFn]
                 NestingLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerName=NOTHING, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthMechanism=AuthMechanism,
            AuthSource=AuthSource,
            AuthType=AuthType,
            DatabaseName=DatabaseName,
            DocsToInvestigate=DocsToInvestigate,
            ExtractDocId=ExtractDocId,
            NestingLevel=NestingLevel,
            Password=Password,
            Port=Port,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            ServerName=ServerName,
            Username=Username,
            **kwargs
        )
        super(MongoDbSettings, self).__init__(**processed_kwargs)


class MySqlSettings(troposphere.dms.MySqlSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(MySqlSettings, self).__init__(**processed_kwargs)


class NeptuneSettings(troposphere.dms.NeptuneSettings, Mixin):
    def __init__(self,
                 title=None,
                 ErrorRetryDuration=NOTHING, # type: int
                 IamAuthEnabled=NOTHING, # type: bool
                 MaxFileSize=NOTHING, # type: int
                 MaxRetryCount=NOTHING, # type: int
                 S3BucketFolder=NOTHING, # type: Union[str, AWSHelperFn]
                 S3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ErrorRetryDuration=ErrorRetryDuration,
            IamAuthEnabled=IamAuthEnabled,
            MaxFileSize=MaxFileSize,
            MaxRetryCount=MaxRetryCount,
            S3BucketFolder=S3BucketFolder,
            S3BucketName=S3BucketName,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(NeptuneSettings, self).__init__(**processed_kwargs)


class OracleSettings(troposphere.dms.OracleSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerOracleAsmAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerOracleAsmSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerOracleAsmAccessRoleArn=SecretsManagerOracleAsmAccessRoleArn,
            SecretsManagerOracleAsmSecretId=SecretsManagerOracleAsmSecretId,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(OracleSettings, self).__init__(**processed_kwargs)


class PostgreSqlSettings(troposphere.dms.PostgreSqlSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(PostgreSqlSettings, self).__init__(**processed_kwargs)


class RedshiftSettings(troposphere.dms.RedshiftSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(RedshiftSettings, self).__init__(**processed_kwargs)


class S3Settings(troposphere.dms.S3Settings, Mixin):
    def __init__(self,
                 title=None,
                 BucketFolder=NOTHING, # type: Union[str, AWSHelperFn]
                 BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 CompressionType=NOTHING, # type: Union[str, AWSHelperFn]
                 CsvDelimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 CsvRowDelimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 ExternalTableDefinition=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketFolder=BucketFolder,
            BucketName=BucketName,
            CompressionType=CompressionType,
            CsvDelimiter=CsvDelimiter,
            CsvRowDelimiter=CsvRowDelimiter,
            ExternalTableDefinition=ExternalTableDefinition,
            ServiceAccessRoleArn=ServiceAccessRoleArn,
            **kwargs
        )
        super(S3Settings, self).__init__(**processed_kwargs)


class SybaseSettings(troposphere.dms.SybaseSettings, Mixin):
    def __init__(self,
                 title=None,
                 SecretsManagerAccessRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretsManagerSecretId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretsManagerAccessRoleArn=SecretsManagerAccessRoleArn,
            SecretsManagerSecretId=SecretsManagerSecretId,
            **kwargs
        )
        super(SybaseSettings, self).__init__(**processed_kwargs)


class Endpoint(troposphere.dms.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointType=REQUIRED, # type: Union[str, AWSHelperFn]
                 EngineName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 DocDbSettings=NOTHING, # type: _DocDbSettings
                 DynamoDbSettings=NOTHING, # type: _DynamoDbSettings
                 ElasticsearchSettings=NOTHING, # type: _ElasticsearchSettings
                 EndpointIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtraConnectionAttributes=NOTHING, # type: Union[str, AWSHelperFn]
                 IbmDb2Settings=NOTHING, # type: _IbmDb2Settings
                 KafkaSettings=NOTHING, # type: _KafkaSettings
                 KinesisSettings=NOTHING, # type: _KinesisSettings
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 MicrosoftSqlServerSettings=NOTHING, # type: _MicrosoftSqlServerSettings
                 MongoDbSettings=NOTHING, # type: _MongoDbSettings
                 MySqlSettings=NOTHING, # type: _MySqlSettings
                 NeptuneSettings=NOTHING, # type: _NeptuneSettings
                 OracleSettings=NOTHING, # type: _OracleSettings
                 Password=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 PostgreSqlSettings=NOTHING, # type: _PostgreSqlSettings
                 RedshiftSettings=NOTHING, # type: _RedshiftSettings
                 S3Settings=NOTHING, # type: _S3Settings
                 ServerName=NOTHING, # type: Union[str, AWSHelperFn]
                 SslMode=NOTHING, # type: Union[str, AWSHelperFn]
                 SybaseSettings=NOTHING, # type: _SybaseSettings
                 Tags=NOTHING, # type: _Tags
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointType=EndpointType,
            EngineName=EngineName,
            CertificateArn=CertificateArn,
            DatabaseName=DatabaseName,
            DocDbSettings=DocDbSettings,
            DynamoDbSettings=DynamoDbSettings,
            ElasticsearchSettings=ElasticsearchSettings,
            EndpointIdentifier=EndpointIdentifier,
            ExtraConnectionAttributes=ExtraConnectionAttributes,
            IbmDb2Settings=IbmDb2Settings,
            KafkaSettings=KafkaSettings,
            KinesisSettings=KinesisSettings,
            KmsKeyId=KmsKeyId,
            MicrosoftSqlServerSettings=MicrosoftSqlServerSettings,
            MongoDbSettings=MongoDbSettings,
            MySqlSettings=MySqlSettings,
            NeptuneSettings=NeptuneSettings,
            OracleSettings=OracleSettings,
            Password=Password,
            Port=Port,
            PostgreSqlSettings=PostgreSqlSettings,
            RedshiftSettings=RedshiftSettings,
            S3Settings=S3Settings,
            ServerName=ServerName,
            SslMode=SslMode,
            SybaseSettings=SybaseSettings,
            Tags=Tags,
            Username=Username,
            **kwargs
        )
        super(Endpoint, self).__init__(**processed_kwargs)


class EventSubscription(troposphere.dms.EventSubscription, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SnsTopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 EventCategories=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceType=NOTHING, # type: Union[str, AWSHelperFn]
                 SubscriptionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
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
            SubscriptionName=SubscriptionName,
            Tags=Tags,
            **kwargs
        )
        super(EventSubscription, self).__init__(**processed_kwargs)


class ReplicationInstance(troposphere.dms.ReplicationInstance, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationInstanceClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllocatedStorage=NOTHING, # type: int
                 AllowMajorVersionUpgrade=NOTHING, # type: bool
                 AutoMinorVersionUpgrade=NOTHING, # type: bool
                 AvailabilityZone=NOTHING, # type: Union[str, AWSHelperFn]
                 EngineVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 MultiAZ=NOTHING, # type: bool
                 PreferredMaintenanceWindow=NOTHING, # type: Union[str, AWSHelperFn]
                 PubliclyAccessible=NOTHING, # type: bool
                 ReplicationInstanceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationSubnetGroupIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VpcSecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationInstanceClass=ReplicationInstanceClass,
            AllocatedStorage=AllocatedStorage,
            AllowMajorVersionUpgrade=AllowMajorVersionUpgrade,
            AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
            AvailabilityZone=AvailabilityZone,
            EngineVersion=EngineVersion,
            KmsKeyId=KmsKeyId,
            MultiAZ=MultiAZ,
            PreferredMaintenanceWindow=PreferredMaintenanceWindow,
            PubliclyAccessible=PubliclyAccessible,
            ReplicationInstanceIdentifier=ReplicationInstanceIdentifier,
            ReplicationSubnetGroupIdentifier=ReplicationSubnetGroupIdentifier,
            Tags=Tags,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            **kwargs
        )
        super(ReplicationInstance, self).__init__(**processed_kwargs)


class ReplicationSubnetGroup(troposphere.dms.ReplicationSubnetGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ReplicationSubnetGroupDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ReplicationSubnetGroupIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ReplicationSubnetGroupDescription=ReplicationSubnetGroupDescription,
            SubnetIds=SubnetIds,
            ReplicationSubnetGroupIdentifier=ReplicationSubnetGroupIdentifier,
            Tags=Tags,
            **kwargs
        )
        super(ReplicationSubnetGroup, self).__init__(**processed_kwargs)


class ReplicationTask(troposphere.dms.ReplicationTask, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MigrationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReplicationInstanceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceEndpointArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableMappings=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetEndpointArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CdcStartPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 CdcStartTime=NOTHING, # type: int
                 CdcStopPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationTaskIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicationTaskSettings=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TaskData=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MigrationType=MigrationType,
            ReplicationInstanceArn=ReplicationInstanceArn,
            SourceEndpointArn=SourceEndpointArn,
            TableMappings=TableMappings,
            TargetEndpointArn=TargetEndpointArn,
            CdcStartPosition=CdcStartPosition,
            CdcStartTime=CdcStartTime,
            CdcStopPosition=CdcStopPosition,
            ReplicationTaskIdentifier=ReplicationTaskIdentifier,
            ReplicationTaskSettings=ReplicationTaskSettings,
            Tags=Tags,
            TaskData=TaskData,
            **kwargs
        )
        super(ReplicationTask, self).__init__(**processed_kwargs)
