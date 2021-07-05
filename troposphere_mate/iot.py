# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iot

from troposphere.iot import (
    Action as _Action,
    ActionParams as _ActionParams,
    AddThingsToThingGroupParams as _AddThingsToThingGroupParams,
    AssetPropertyTimestamp as _AssetPropertyTimestamp,
    AssetPropertyValue as _AssetPropertyValue,
    AssetPropertyVariant as _AssetPropertyVariant,
    AuditCheckConfiguration as _AuditCheckConfiguration,
    AuditCheckConfigurations as _AuditCheckConfigurations,
    AuditNotificationTarget as _AuditNotificationTarget,
    AuditNotificationTargetConfigurations as _AuditNotificationTargetConfigurations,
    AuthorizerConfig as _AuthorizerConfig,
    Behavior as _Behavior,
    BehaviorCriteria as _BehaviorCriteria,
    CloudwatchAlarmAction as _CloudwatchAlarmAction,
    CloudwatchMetricAction as _CloudwatchMetricAction,
    DynamoDBAction as _DynamoDBAction,
    DynamoDBv2Action as _DynamoDBv2Action,
    ElasticsearchAction as _ElasticsearchAction,
    EnableIoTLoggingParams as _EnableIoTLoggingParams,
    FirehoseAction as _FirehoseAction,
    HttpAction as _HttpAction,
    HttpActionHeader as _HttpActionHeader,
    HttpAuthorization as _HttpAuthorization,
    HttpUrlDestinationSummary as _HttpUrlDestinationSummary,
    IotAnalyticsAction as _IotAnalyticsAction,
    IotEventsAction as _IotEventsAction,
    IotSiteWiseAction as _IotSiteWiseAction,
    KinesisAction as _KinesisAction,
    LambdaAction as _LambdaAction,
    MachineLearningDetectionConfig as _MachineLearningDetectionConfig,
    MetricDimension as _MetricDimension,
    MetricToRetain as _MetricToRetain,
    MetricValue as _MetricValue,
    ProvisioningHook as _ProvisioningHook,
    PublishFindingToSnsParams as _PublishFindingToSnsParams,
    PutAssetPropertyValueEntry as _PutAssetPropertyValueEntry,
    PutItemInput as _PutItemInput,
    ReplaceDefaultPolicyVersionParams as _ReplaceDefaultPolicyVersionParams,
    RepublishAction as _RepublishAction,
    S3Action as _S3Action,
    SigV4Authorization as _SigV4Authorization,
    SnsAction as _SnsAction,
    SqsAction as _SqsAction,
    StatisticalThreshold as _StatisticalThreshold,
    StepFunctionsAction as _StepFunctionsAction,
    Tags as _Tags,
    TopicRulePayload as _TopicRulePayload,
    UpdateCACertificateParams as _UpdateCACertificateParams,
    UpdateDeviceCertificateParams as _UpdateDeviceCertificateParams,
    VpcDestinationProperties as _VpcDestinationProperties,
    double as _double,
    integer as _integer,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AuditCheckConfiguration(troposphere.iot.AuditCheckConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            **kwargs
        )
        super(AuditCheckConfiguration, self).__init__(**processed_kwargs)


class AuditCheckConfigurations(troposphere.iot.AuditCheckConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 AuthenticatedCognitoRoleOverlyPermissiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 CaCertificateExpiringCheck=NOTHING, # type: _AuditCheckConfiguration
                 CaCertificateKeyQualityCheck=NOTHING, # type: _AuditCheckConfiguration
                 ConflictingClientIdsCheck=NOTHING, # type: _AuditCheckConfiguration
                 DeviceCertificateExpiringCheck=NOTHING, # type: _AuditCheckConfiguration
                 DeviceCertificateKeyQualityCheck=NOTHING, # type: _AuditCheckConfiguration
                 DeviceCertificateSharedCheck=NOTHING, # type: _AuditCheckConfiguration
                 IotPolicyOverlyPermissiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 IotRoleAliasAllowsAccessToUnusedServicesCheck=NOTHING, # type: _AuditCheckConfiguration
                 IotRoleAliasOverlyPermissiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 LoggingDisabledCheck=NOTHING, # type: _AuditCheckConfiguration
                 RevokedCaCertificateStillActiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 RevokedDeviceCertificateStillActiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 UnauthenticatedCognitoRoleOverlyPermissiveCheck=NOTHING, # type: _AuditCheckConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthenticatedCognitoRoleOverlyPermissiveCheck=AuthenticatedCognitoRoleOverlyPermissiveCheck,
            CaCertificateExpiringCheck=CaCertificateExpiringCheck,
            CaCertificateKeyQualityCheck=CaCertificateKeyQualityCheck,
            ConflictingClientIdsCheck=ConflictingClientIdsCheck,
            DeviceCertificateExpiringCheck=DeviceCertificateExpiringCheck,
            DeviceCertificateKeyQualityCheck=DeviceCertificateKeyQualityCheck,
            DeviceCertificateSharedCheck=DeviceCertificateSharedCheck,
            IotPolicyOverlyPermissiveCheck=IotPolicyOverlyPermissiveCheck,
            IotRoleAliasAllowsAccessToUnusedServicesCheck=IotRoleAliasAllowsAccessToUnusedServicesCheck,
            IotRoleAliasOverlyPermissiveCheck=IotRoleAliasOverlyPermissiveCheck,
            LoggingDisabledCheck=LoggingDisabledCheck,
            RevokedCaCertificateStillActiveCheck=RevokedCaCertificateStillActiveCheck,
            RevokedDeviceCertificateStillActiveCheck=RevokedDeviceCertificateStillActiveCheck,
            UnauthenticatedCognitoRoleOverlyPermissiveCheck=UnauthenticatedCognitoRoleOverlyPermissiveCheck,
            **kwargs
        )
        super(AuditCheckConfigurations, self).__init__(**processed_kwargs)


class AuditNotificationTarget(troposphere.iot.AuditNotificationTarget, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            RoleArn=RoleArn,
            TargetArn=TargetArn,
            **kwargs
        )
        super(AuditNotificationTarget, self).__init__(**processed_kwargs)


class AuditNotificationTargetConfigurations(troposphere.iot.AuditNotificationTargetConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 Sns=NOTHING, # type: _AuditNotificationTarget
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Sns=Sns,
            **kwargs
        )
        super(AuditNotificationTargetConfigurations, self).__init__(**processed_kwargs)


class AccountAuditConfiguration(troposphere.iot.AccountAuditConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuditCheckConfigurations=REQUIRED, # type: _AuditCheckConfigurations
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuditNotificationTargetConfigurations=NOTHING, # type: _AuditNotificationTargetConfigurations
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccountId=AccountId,
            AuditCheckConfigurations=AuditCheckConfigurations,
            RoleArn=RoleArn,
            AuditNotificationTargetConfigurations=AuditNotificationTargetConfigurations,
            **kwargs
        )
        super(AccountAuditConfiguration, self).__init__(**processed_kwargs)


class Authorizer(troposphere.iot.Authorizer, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthorizerFunctionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 AuthorizerName=NOTHING, # type: Union[str, AWSHelperFn]
                 SigningDisabled=NOTHING, # type: bool
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: dict
                 TokenKeyName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthorizerFunctionArn=AuthorizerFunctionArn,
            AuthorizerName=AuthorizerName,
            SigningDisabled=SigningDisabled,
            Status=Status,
            Tags=Tags,
            TokenKeyName=TokenKeyName,
            **kwargs
        )
        super(Authorizer, self).__init__(**processed_kwargs)


class Certificate(troposphere.iot.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 CACertificatePem=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateMode=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificatePem=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateSigningRequest=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Status=Status,
            CACertificatePem=CACertificatePem,
            CertificateMode=CertificateMode,
            CertificatePem=CertificatePem,
            CertificateSigningRequest=CertificateSigningRequest,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)


class CustomMetric(troposphere.iot.CustomMetric, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MetricType=REQUIRED, # type: Union[str, AWSHelperFn]
                 DisplayName=NOTHING, # type: Union[str, AWSHelperFn]
                 MetricName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MetricType=MetricType,
            DisplayName=DisplayName,
            MetricName=MetricName,
            Tags=Tags,
            **kwargs
        )
        super(CustomMetric, self).__init__(**processed_kwargs)


class Dimension(troposphere.iot.Dimension, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StringValues=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StringValues=StringValues,
            Type=Type,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Dimension, self).__init__(**processed_kwargs)


class AuthorizerConfig(troposphere.iot.AuthorizerConfig, Mixin):
    def __init__(self,
                 title=None,
                 AllowAuthorizerOverride=NOTHING, # type: bool
                 DefaultAuthorizerName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowAuthorizerOverride=AllowAuthorizerOverride,
            DefaultAuthorizerName=DefaultAuthorizerName,
            **kwargs
        )
        super(AuthorizerConfig, self).__init__(**processed_kwargs)


class DomainConfiguration(troposphere.iot.DomainConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthorizerConfig=NOTHING, # type: _AuthorizerConfig
                 DomainConfigurationName=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainConfigurationStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServerCertificateArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ServiceType=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 ValidationCertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthorizerConfig=AuthorizerConfig,
            DomainConfigurationName=DomainConfigurationName,
            DomainConfigurationStatus=DomainConfigurationStatus,
            DomainName=DomainName,
            ServerCertificateArns=ServerCertificateArns,
            ServiceType=ServiceType,
            Tags=Tags,
            ValidationCertificateArn=ValidationCertificateArn,
            **kwargs
        )
        super(DomainConfiguration, self).__init__(**processed_kwargs)


class AddThingsToThingGroupParams(troposphere.iot.AddThingsToThingGroupParams, Mixin):
    def __init__(self,
                 title=None,
                 ThingGroupNames=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 OverrideDynamicGroups=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ThingGroupNames=ThingGroupNames,
            OverrideDynamicGroups=OverrideDynamicGroups,
            **kwargs
        )
        super(AddThingsToThingGroupParams, self).__init__(**processed_kwargs)


class EnableIoTLoggingParams(troposphere.iot.EnableIoTLoggingParams, Mixin):
    def __init__(self,
                 title=None,
                 LogLevel=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArnForLogging=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogLevel=LogLevel,
            RoleArnForLogging=RoleArnForLogging,
            **kwargs
        )
        super(EnableIoTLoggingParams, self).__init__(**processed_kwargs)


class PublishFindingToSnsParams(troposphere.iot.PublishFindingToSnsParams, Mixin):
    def __init__(self,
                 title=None,
                 TopicArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TopicArn=TopicArn,
            **kwargs
        )
        super(PublishFindingToSnsParams, self).__init__(**processed_kwargs)


class ReplaceDefaultPolicyVersionParams(troposphere.iot.ReplaceDefaultPolicyVersionParams, Mixin):
    def __init__(self,
                 title=None,
                 TemplateName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TemplateName=TemplateName,
            **kwargs
        )
        super(ReplaceDefaultPolicyVersionParams, self).__init__(**processed_kwargs)


class UpdateCACertificateParams(troposphere.iot.UpdateCACertificateParams, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            **kwargs
        )
        super(UpdateCACertificateParams, self).__init__(**processed_kwargs)


class UpdateDeviceCertificateParams(troposphere.iot.UpdateDeviceCertificateParams, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            **kwargs
        )
        super(UpdateDeviceCertificateParams, self).__init__(**processed_kwargs)


class ActionParams(troposphere.iot.ActionParams, Mixin):
    def __init__(self,
                 title=None,
                 AddThingsToThingGroupParams=NOTHING, # type: _AddThingsToThingGroupParams
                 EnableIoTLoggingParams=NOTHING, # type: _EnableIoTLoggingParams
                 PublishFindingToSnsParams=NOTHING, # type: _PublishFindingToSnsParams
                 ReplaceDefaultPolicyVersionParams=NOTHING, # type: _ReplaceDefaultPolicyVersionParams
                 UpdateCACertificateParams=NOTHING, # type: _UpdateCACertificateParams
                 UpdateDeviceCertificateParams=NOTHING, # type: _UpdateDeviceCertificateParams
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddThingsToThingGroupParams=AddThingsToThingGroupParams,
            EnableIoTLoggingParams=EnableIoTLoggingParams,
            PublishFindingToSnsParams=PublishFindingToSnsParams,
            ReplaceDefaultPolicyVersionParams=ReplaceDefaultPolicyVersionParams,
            UpdateCACertificateParams=UpdateCACertificateParams,
            UpdateDeviceCertificateParams=UpdateDeviceCertificateParams,
            **kwargs
        )
        super(ActionParams, self).__init__(**processed_kwargs)


class MitigationAction(troposphere.iot.MitigationAction, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ActionParams=REQUIRED, # type: _ActionParams
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ActionName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ActionParams=ActionParams,
            RoleArn=RoleArn,
            ActionName=ActionName,
            Tags=Tags,
            **kwargs
        )
        super(MitigationAction, self).__init__(**processed_kwargs)


class CloudwatchAlarmAction(troposphere.iot.CloudwatchAlarmAction, Mixin):
    def __init__(self,
                 title=None,
                 AlarmName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StateReason=REQUIRED, # type: Union[str, AWSHelperFn]
                 StateValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmName=AlarmName,
            RoleArn=RoleArn,
            StateReason=StateReason,
            StateValue=StateValue,
            **kwargs
        )
        super(CloudwatchAlarmAction, self).__init__(**processed_kwargs)


class CloudwatchMetricAction(troposphere.iot.CloudwatchMetricAction, Mixin):
    def __init__(self,
                 title=None,
                 MetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricNamespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricUnit=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricTimestamp=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MetricName=MetricName,
            MetricNamespace=MetricNamespace,
            MetricUnit=MetricUnit,
            MetricValue=MetricValue,
            RoleArn=RoleArn,
            MetricTimestamp=MetricTimestamp,
            **kwargs
        )
        super(CloudwatchMetricAction, self).__init__(**processed_kwargs)


class DynamoDBAction(troposphere.iot.DynamoDBAction, Mixin):
    def __init__(self,
                 title=None,
                 HashKeyField=REQUIRED, # type: Union[str, AWSHelperFn]
                 HashKeyValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HashKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 PayloadField=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyField=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 RangeKeyValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HashKeyField=HashKeyField,
            HashKeyValue=HashKeyValue,
            RoleArn=RoleArn,
            TableName=TableName,
            HashKeyType=HashKeyType,
            PayloadField=PayloadField,
            RangeKeyField=RangeKeyField,
            RangeKeyType=RangeKeyType,
            RangeKeyValue=RangeKeyValue,
            **kwargs
        )
        super(DynamoDBAction, self).__init__(**processed_kwargs)


class PutItemInput(troposphere.iot.PutItemInput, Mixin):
    def __init__(self,
                 title=None,
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TableName=TableName,
            **kwargs
        )
        super(PutItemInput, self).__init__(**processed_kwargs)


class DynamoDBv2Action(troposphere.iot.DynamoDBv2Action, Mixin):
    def __init__(self,
                 title=None,
                 PutItem=NOTHING, # type: _PutItemInput
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PutItem=PutItem,
            RoleArn=RoleArn,
            **kwargs
        )
        super(DynamoDBv2Action, self).__init__(**processed_kwargs)


class ElasticsearchAction(troposphere.iot.ElasticsearchAction, Mixin):
    def __init__(self,
                 title=None,
                 Endpoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Index=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Endpoint=Endpoint,
            Id=Id,
            Index=Index,
            RoleArn=RoleArn,
            Type=Type,
            **kwargs
        )
        super(ElasticsearchAction, self).__init__(**processed_kwargs)


class FirehoseAction(troposphere.iot.FirehoseAction, Mixin):
    def __init__(self,
                 title=None,
                 DeliveryStreamName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Separator=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeliveryStreamName=DeliveryStreamName,
            RoleArn=RoleArn,
            Separator=Separator,
            **kwargs
        )
        super(FirehoseAction, self).__init__(**processed_kwargs)


class IotAnalyticsAction(troposphere.iot.IotAnalyticsAction, Mixin):
    def __init__(self,
                 title=None,
                 ChannelName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChannelName=ChannelName,
            RoleArn=RoleArn,
            **kwargs
        )
        super(IotAnalyticsAction, self).__init__(**processed_kwargs)


class KinesisAction(troposphere.iot.KinesisAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StreamName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PartitionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            StreamName=StreamName,
            PartitionKey=PartitionKey,
            **kwargs
        )
        super(KinesisAction, self).__init__(**processed_kwargs)


class LambdaAction(troposphere.iot.LambdaAction, Mixin):
    def __init__(self,
                 title=None,
                 FunctionArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FunctionArn=FunctionArn,
            **kwargs
        )
        super(LambdaAction, self).__init__(**processed_kwargs)


class RepublishAction(troposphere.iot.RepublishAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Topic=REQUIRED, # type: Union[str, AWSHelperFn]
                 Qos=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            Topic=Topic,
            Qos=Qos,
            **kwargs
        )
        super(RepublishAction, self).__init__(**processed_kwargs)


class S3Action(troposphere.iot.S3Action, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            Key=Key,
            RoleArn=RoleArn,
            **kwargs
        )
        super(S3Action, self).__init__(**processed_kwargs)


class SnsAction(troposphere.iot.SnsAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MessageFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            TargetArn=TargetArn,
            MessageFormat=MessageFormat,
            **kwargs
        )
        super(SnsAction, self).__init__(**processed_kwargs)


class SqsAction(troposphere.iot.SqsAction, Mixin):
    def __init__(self,
                 title=None,
                 QueueUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 UseBase64=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueueUrl=QueueUrl,
            RoleArn=RoleArn,
            UseBase64=UseBase64,
            **kwargs
        )
        super(SqsAction, self).__init__(**processed_kwargs)


class SigV4Authorization(troposphere.iot.SigV4Authorization, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SigningRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            ServiceName=ServiceName,
            SigningRegion=SigningRegion,
            **kwargs
        )
        super(SigV4Authorization, self).__init__(**processed_kwargs)


class HttpActionHeader(troposphere.iot.HttpActionHeader, Mixin):
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
        super(HttpActionHeader, self).__init__(**processed_kwargs)


class HttpAuthorization(troposphere.iot.HttpAuthorization, Mixin):
    def __init__(self,
                 title=None,
                 Sigv4=NOTHING, # type: _SigV4Authorization
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Sigv4=Sigv4,
            **kwargs
        )
        super(HttpAuthorization, self).__init__(**processed_kwargs)


class HttpAction(troposphere.iot.HttpAction, Mixin):
    def __init__(self,
                 title=None,
                 Url=REQUIRED, # type: Union[str, AWSHelperFn]
                 Auth=NOTHING, # type: _HttpAuthorization
                 ConfirmationUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 Headers=NOTHING, # type: List[_HttpActionHeader]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Url=Url,
            Auth=Auth,
            ConfirmationUrl=ConfirmationUrl,
            Headers=Headers,
            **kwargs
        )
        super(HttpAction, self).__init__(**processed_kwargs)


class IotEventsAction(troposphere.iot.IotEventsAction, Mixin):
    def __init__(self,
                 title=None,
                 InputName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MessageId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputName=InputName,
            RoleArn=RoleArn,
            MessageId=MessageId,
            **kwargs
        )
        super(IotEventsAction, self).__init__(**processed_kwargs)


class AssetPropertyVariant(troposphere.iot.AssetPropertyVariant, Mixin):
    def __init__(self,
                 title=None,
                 BooleanValue=NOTHING, # type: Union[str, AWSHelperFn]
                 DoubleValue=NOTHING, # type: Union[str, AWSHelperFn]
                 IntegerValue=NOTHING, # type: Union[str, AWSHelperFn]
                 StringValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BooleanValue=BooleanValue,
            DoubleValue=DoubleValue,
            IntegerValue=IntegerValue,
            StringValue=StringValue,
            **kwargs
        )
        super(AssetPropertyVariant, self).__init__(**processed_kwargs)


class AssetPropertyTimestamp(troposphere.iot.AssetPropertyTimestamp, Mixin):
    def __init__(self,
                 title=None,
                 TimeInSeconds=REQUIRED, # type: Union[str, AWSHelperFn]
                 OffsetInNanos=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeInSeconds=TimeInSeconds,
            OffsetInNanos=OffsetInNanos,
            **kwargs
        )
        super(AssetPropertyTimestamp, self).__init__(**processed_kwargs)


class AssetPropertyValue(troposphere.iot.AssetPropertyValue, Mixin):
    def __init__(self,
                 title=None,
                 Timestamp=REQUIRED, # type: _AssetPropertyTimestamp
                 Value=REQUIRED, # type: _AssetPropertyVariant
                 Quality=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Timestamp=Timestamp,
            Value=Value,
            Quality=Quality,
            **kwargs
        )
        super(AssetPropertyValue, self).__init__(**processed_kwargs)


class PutAssetPropertyValueEntry(troposphere.iot.PutAssetPropertyValueEntry, Mixin):
    def __init__(self,
                 title=None,
                 PropertyValues=REQUIRED, # type: List[_AssetPropertyValue]
                 AssetId=NOTHING, # type: Union[str, AWSHelperFn]
                 EntryId=NOTHING, # type: Union[str, AWSHelperFn]
                 PropertyAlias=NOTHING, # type: Union[str, AWSHelperFn]
                 PropertyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PropertyValues=PropertyValues,
            AssetId=AssetId,
            EntryId=EntryId,
            PropertyAlias=PropertyAlias,
            PropertyId=PropertyId,
            **kwargs
        )
        super(PutAssetPropertyValueEntry, self).__init__(**processed_kwargs)


class IotSiteWiseAction(troposphere.iot.IotSiteWiseAction, Mixin):
    def __init__(self,
                 title=None,
                 PutAssetPropertyValueEntries=REQUIRED, # type: List[_PutAssetPropertyValueEntry]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PutAssetPropertyValueEntries=PutAssetPropertyValueEntries,
            RoleArn=RoleArn,
            **kwargs
        )
        super(IotSiteWiseAction, self).__init__(**processed_kwargs)


class StepFunctionsAction(troposphere.iot.StepFunctionsAction, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StateMachineName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExecutionNamePrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            StateMachineName=StateMachineName,
            ExecutionNamePrefix=ExecutionNamePrefix,
            **kwargs
        )
        super(StepFunctionsAction, self).__init__(**processed_kwargs)


class Action(troposphere.iot.Action, Mixin):
    def __init__(self,
                 title=None,
                 CloudwatchAlarm=NOTHING, # type: _CloudwatchAlarmAction
                 CloudwatchMetric=NOTHING, # type: _CloudwatchMetricAction
                 DynamoDB=NOTHING, # type: _DynamoDBAction
                 DynamoDBv2=NOTHING, # type: _DynamoDBv2Action
                 Elasticsearch=NOTHING, # type: _ElasticsearchAction
                 Firehose=NOTHING, # type: _FirehoseAction
                 Http=NOTHING, # type: _HttpAction
                 IotAnalytics=NOTHING, # type: _IotAnalyticsAction
                 IotEvents=NOTHING, # type: _IotEventsAction
                 IotSiteWise=NOTHING, # type: _IotSiteWiseAction
                 Kinesis=NOTHING, # type: _KinesisAction
                 Lambda=NOTHING, # type: _LambdaAction
                 Republish=NOTHING, # type: _RepublishAction
                 S3=NOTHING, # type: _S3Action
                 Sns=NOTHING, # type: _SnsAction
                 Sqs=NOTHING, # type: _SqsAction
                 StepFunctions=NOTHING, # type: _StepFunctionsAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudwatchAlarm=CloudwatchAlarm,
            CloudwatchMetric=CloudwatchMetric,
            DynamoDB=DynamoDB,
            DynamoDBv2=DynamoDBv2,
            Elasticsearch=Elasticsearch,
            Firehose=Firehose,
            Http=Http,
            IotAnalytics=IotAnalytics,
            IotEvents=IotEvents,
            IotSiteWise=IotSiteWise,
            Kinesis=Kinesis,
            Lambda=Lambda,
            Republish=Republish,
            S3=S3,
            Sns=Sns,
            Sqs=Sqs,
            StepFunctions=StepFunctions,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class TopicRulePayload(troposphere.iot.TopicRulePayload, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: List[_Action]
                 RuleDisabled=REQUIRED, # type: bool
                 Sql=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsIotSqlVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            RuleDisabled=RuleDisabled,
            Sql=Sql,
            AwsIotSqlVersion=AwsIotSqlVersion,
            Description=Description,
            **kwargs
        )
        super(TopicRulePayload, self).__init__(**processed_kwargs)


class TopicRule(troposphere.iot.TopicRule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TopicRulePayload=REQUIRED, # type: _TopicRulePayload
                 RuleName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TopicRulePayload=TopicRulePayload,
            RuleName=RuleName,
            **kwargs
        )
        super(TopicRule, self).__init__(**processed_kwargs)


class ThingPrincipalAttachment(troposphere.iot.ThingPrincipalAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 ThingName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Principal=Principal,
            ThingName=ThingName,
            **kwargs
        )
        super(ThingPrincipalAttachment, self).__init__(**processed_kwargs)


class Thing(troposphere.iot.Thing, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AttributePayload=NOTHING, # type: dict
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AttributePayload=AttributePayload,
            ThingName=ThingName,
            **kwargs
        )
        super(Thing, self).__init__(**processed_kwargs)


class PolicyPrincipalAttachment(troposphere.iot.PolicyPrincipalAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyName=PolicyName,
            Principal=Principal,
            **kwargs
        )
        super(PolicyPrincipalAttachment, self).__init__(**processed_kwargs)


class Policy(troposphere.iot.Policy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 PolicyName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PolicyDocument=PolicyDocument,
            PolicyName=PolicyName,
            **kwargs
        )
        super(Policy, self).__init__(**processed_kwargs)


class ProvisioningHook(troposphere.iot.ProvisioningHook, Mixin):
    def __init__(self,
                 title=None,
                 PayloadVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PayloadVersion=PayloadVersion,
            TargetArn=TargetArn,
            **kwargs
        )
        super(ProvisioningHook, self).__init__(**processed_kwargs)


class ProvisioningTemplate(troposphere.iot.ProvisioningTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ProvisioningRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TemplateBody=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 PreProvisioningHook=NOTHING, # type: _ProvisioningHook
                 Tags=NOTHING, # type: dict
                 TemplateName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ProvisioningRoleArn=ProvisioningRoleArn,
            TemplateBody=TemplateBody,
            Description=Description,
            Enabled=Enabled,
            PreProvisioningHook=PreProvisioningHook,
            Tags=Tags,
            TemplateName=TemplateName,
            **kwargs
        )
        super(ProvisioningTemplate, self).__init__(**processed_kwargs)


class ScheduledAudit(troposphere.iot.ScheduledAudit, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Frequency=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetCheckNames=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 DayOfMonth=NOTHING, # type: Union[str, AWSHelperFn]
                 DayOfWeek=NOTHING, # type: Union[str, AWSHelperFn]
                 ScheduledAuditName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Frequency=Frequency,
            TargetCheckNames=TargetCheckNames,
            DayOfMonth=DayOfMonth,
            DayOfWeek=DayOfWeek,
            ScheduledAuditName=ScheduledAuditName,
            Tags=Tags,
            **kwargs
        )
        super(ScheduledAudit, self).__init__(**processed_kwargs)


class MachineLearningDetectionConfig(troposphere.iot.MachineLearningDetectionConfig, Mixin):
    def __init__(self,
                 title=None,
                 ConfidenceLevel=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfidenceLevel=ConfidenceLevel,
            **kwargs
        )
        super(MachineLearningDetectionConfig, self).__init__(**processed_kwargs)


class MetricValue(troposphere.iot.MetricValue, Mixin):
    def __init__(self,
                 title=None,
                 Cidrs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Count=NOTHING, # type: Union[str, AWSHelperFn]
                 Number=NOTHING, # type: float
                 Numbers=NOTHING, # type: List[_double]
                 Ports=NOTHING, # type: List[_integer]
                 Strings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Cidrs=Cidrs,
            Count=Count,
            Number=Number,
            Numbers=Numbers,
            Ports=Ports,
            Strings=Strings,
            **kwargs
        )
        super(MetricValue, self).__init__(**processed_kwargs)


class StatisticalThreshold(troposphere.iot.StatisticalThreshold, Mixin):
    def __init__(self,
                 title=None,
                 Statistic=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statistic=Statistic,
            **kwargs
        )
        super(StatisticalThreshold, self).__init__(**processed_kwargs)


class BehaviorCriteria(troposphere.iot.BehaviorCriteria, Mixin):
    def __init__(self,
                 title=None,
                 ComparisonOperator=NOTHING, # type: Union[str, AWSHelperFn]
                 ConsecutiveDatapointsToAlarm=NOTHING, # type: int
                 ConsecutiveDatapointsToClear=NOTHING, # type: int
                 DurationSeconds=NOTHING, # type: int
                 MlDetectionConfig=NOTHING, # type: _MachineLearningDetectionConfig
                 StatisticalThreshold=NOTHING, # type: _StatisticalThreshold
                 Value=NOTHING, # type: _MetricValue
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComparisonOperator=ComparisonOperator,
            ConsecutiveDatapointsToAlarm=ConsecutiveDatapointsToAlarm,
            ConsecutiveDatapointsToClear=ConsecutiveDatapointsToClear,
            DurationSeconds=DurationSeconds,
            MlDetectionConfig=MlDetectionConfig,
            StatisticalThreshold=StatisticalThreshold,
            Value=Value,
            **kwargs
        )
        super(BehaviorCriteria, self).__init__(**processed_kwargs)


class MetricDimension(troposphere.iot.MetricDimension, Mixin):
    def __init__(self,
                 title=None,
                 DimensionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Operator=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DimensionName=DimensionName,
            Operator=Operator,
            **kwargs
        )
        super(MetricDimension, self).__init__(**processed_kwargs)


class Behavior(troposphere.iot.Behavior, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Criteria=NOTHING, # type: _BehaviorCriteria
                 Metric=NOTHING, # type: Union[str, AWSHelperFn]
                 MetricDimension=NOTHING, # type: _MetricDimension
                 SuppressAlerts=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Criteria=Criteria,
            Metric=Metric,
            MetricDimension=MetricDimension,
            SuppressAlerts=SuppressAlerts,
            **kwargs
        )
        super(Behavior, self).__init__(**processed_kwargs)


class MetricToRetain(troposphere.iot.MetricToRetain, Mixin):
    def __init__(self,
                 title=None,
                 Metric=REQUIRED, # type: Union[str, AWSHelperFn]
                 MetricDimension=NOTHING, # type: _MetricDimension
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Metric=Metric,
            MetricDimension=MetricDimension,
            **kwargs
        )
        super(MetricToRetain, self).__init__(**processed_kwargs)


class SecurityProfile(troposphere.iot.SecurityProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AdditionalMetricsToRetainV2=NOTHING, # type: List[_MetricToRetain]
                 AlertTargets=NOTHING, # type: dict
                 Behaviors=NOTHING, # type: List[_Behavior]
                 SecurityProfileDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityProfileName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TargetArns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AdditionalMetricsToRetainV2=AdditionalMetricsToRetainV2,
            AlertTargets=AlertTargets,
            Behaviors=Behaviors,
            SecurityProfileDescription=SecurityProfileDescription,
            SecurityProfileName=SecurityProfileName,
            Tags=Tags,
            TargetArns=TargetArns,
            **kwargs
        )
        super(SecurityProfile, self).__init__(**processed_kwargs)


class HttpUrlDestinationSummary(troposphere.iot.HttpUrlDestinationSummary, Mixin):
    def __init__(self,
                 title=None,
                 ConfirmationUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfirmationUrl=ConfirmationUrl,
            **kwargs
        )
        super(HttpUrlDestinationSummary, self).__init__(**processed_kwargs)


class VpcDestinationProperties(troposphere.iot.VpcDestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            SecurityGroups=SecurityGroups,
            SubnetIds=SubnetIds,
            VpcId=VpcId,
            **kwargs
        )
        super(VpcDestinationProperties, self).__init__(**processed_kwargs)


class TopicRuleDestination(troposphere.iot.TopicRuleDestination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 HttpUrlProperties=NOTHING, # type: _HttpUrlDestinationSummary
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcProperties=NOTHING, # type: _VpcDestinationProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            HttpUrlProperties=HttpUrlProperties,
            Status=Status,
            VpcProperties=VpcProperties,
            **kwargs
        )
        super(TopicRuleDestination, self).__init__(**processed_kwargs)
