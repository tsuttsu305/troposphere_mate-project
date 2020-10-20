# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appflow

from troposphere.appflow import (
    AggregationConfig as _AggregationConfig,
    AmplitudeConnectorProfileCredentials as _AmplitudeConnectorProfileCredentials,
    AmplitudeSourceProperties as _AmplitudeSourceProperties,
    ConnectorOAuthRequest as _ConnectorOAuthRequest,
    ConnectorOperator as _ConnectorOperator,
    ConnectorProfileConfig as _ConnectorProfileConfig,
    ConnectorProfileCredentials as _ConnectorProfileCredentials,
    ConnectorProfileProperties as _ConnectorProfileProperties,
    DatadogConnectorProfileCredentials as _DatadogConnectorProfileCredentials,
    DatadogConnectorProfileProperties as _DatadogConnectorProfileProperties,
    DatadogSourceProperties as _DatadogSourceProperties,
    DestinationConnectorProperties as _DestinationConnectorProperties,
    DestinationFlowConfig as _DestinationFlowConfig,
    DynatraceConnectorProfileCredentials as _DynatraceConnectorProfileCredentials,
    DynatraceConnectorProfileProperties as _DynatraceConnectorProfileProperties,
    DynatraceSourceProperties as _DynatraceSourceProperties,
    ErrorHandlingConfig as _ErrorHandlingConfig,
    EventBridgeDestinationProperties as _EventBridgeDestinationProperties,
    GoogleAnalyticsConnectorProfileCredentials as _GoogleAnalyticsConnectorProfileCredentials,
    GoogleAnalyticsSourceProperties as _GoogleAnalyticsSourceProperties,
    InforNexusConnectorProfileCredentials as _InforNexusConnectorProfileCredentials,
    InforNexusConnectorProfileProperties as _InforNexusConnectorProfileProperties,
    InforNexusSourceProperties as _InforNexusSourceProperties,
    MarketoConnectorProfileCredentials as _MarketoConnectorProfileCredentials,
    MarketoConnectorProfileProperties as _MarketoConnectorProfileProperties,
    MarketoSourceProperties as _MarketoSourceProperties,
    PrefixConfig as _PrefixConfig,
    RedshiftConnectorProfileCredentials as _RedshiftConnectorProfileCredentials,
    RedshiftConnectorProfileProperties as _RedshiftConnectorProfileProperties,
    RedshiftDestinationProperties as _RedshiftDestinationProperties,
    S3DestinationProperties as _S3DestinationProperties,
    S3OutputFormatConfig as _S3OutputFormatConfig,
    S3SourceProperties as _S3SourceProperties,
    SalesforceConnectorProfileCredentials as _SalesforceConnectorProfileCredentials,
    SalesforceConnectorProfileProperties as _SalesforceConnectorProfileProperties,
    SalesforceDestinationProperties as _SalesforceDestinationProperties,
    SalesforceSourceProperties as _SalesforceSourceProperties,
    ScheduledTriggerProperties as _ScheduledTriggerProperties,
    ServiceNowConnectorProfileCredentials as _ServiceNowConnectorProfileCredentials,
    ServiceNowConnectorProfileProperties as _ServiceNowConnectorProfileProperties,
    ServiceNowSourceProperties as _ServiceNowSourceProperties,
    SingularConnectorProfileCredentials as _SingularConnectorProfileCredentials,
    SingularSourceProperties as _SingularSourceProperties,
    SlackConnectorProfileCredentials as _SlackConnectorProfileCredentials,
    SlackConnectorProfileProperties as _SlackConnectorProfileProperties,
    SlackSourceProperties as _SlackSourceProperties,
    SnowflakeConnectorProfileCredentials as _SnowflakeConnectorProfileCredentials,
    SnowflakeConnectorProfileProperties as _SnowflakeConnectorProfileProperties,
    SnowflakeDestinationProperties as _SnowflakeDestinationProperties,
    SourceConnectorProperties as _SourceConnectorProperties,
    SourceFlowConfig as _SourceFlowConfig,
    Tags as _Tags,
    Task as _Task,
    TaskPropertiesObject as _TaskPropertiesObject,
    TrendmicroConnectorProfileCredentials as _TrendmicroConnectorProfileCredentials,
    TrendmicroSourceProperties as _TrendmicroSourceProperties,
    TriggerConfig as _TriggerConfig,
    VeevaConnectorProfileCredentials as _VeevaConnectorProfileCredentials,
    VeevaConnectorProfileProperties as _VeevaConnectorProfileProperties,
    VeevaSourceProperties as _VeevaSourceProperties,
    ZendeskConnectorProfileCredentials as _ZendeskConnectorProfileCredentials,
    ZendeskConnectorProfileProperties as _ZendeskConnectorProfileProperties,
    ZendeskSourceProperties as _ZendeskSourceProperties,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AmplitudeConnectorProfileCredentials(troposphere.appflow.AmplitudeConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ApiKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecretKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiKey=ApiKey,
            SecretKey=SecretKey,
            **kwargs
        )
        super(AmplitudeConnectorProfileCredentials, self).__init__(**processed_kwargs)


class DatadogConnectorProfileCredentials(troposphere.appflow.DatadogConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ApiKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ApplicationKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiKey=ApiKey,
            ApplicationKey=ApplicationKey,
            **kwargs
        )
        super(DatadogConnectorProfileCredentials, self).__init__(**processed_kwargs)


class DynatraceConnectorProfileCredentials(troposphere.appflow.DynatraceConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ApiToken=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiToken=ApiToken,
            **kwargs
        )
        super(DynatraceConnectorProfileCredentials, self).__init__(**processed_kwargs)


class ConnectorOAuthRequest(troposphere.appflow.ConnectorOAuthRequest, Mixin):
    def __init__(self,
                 title=None,
                 AuthCode=NOTHING, # type: Union[str, AWSHelperFn]
                 RedirectUri=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AuthCode=AuthCode,
            RedirectUri=RedirectUri,
            **kwargs
        )
        super(ConnectorOAuthRequest, self).__init__(**processed_kwargs)


class GoogleAnalyticsConnectorProfileCredentials(troposphere.appflow.GoogleAnalyticsConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectorOAuthRequest=NOTHING, # type: _ConnectorOAuthRequest
                 RefreshToken=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            AccessToken=AccessToken,
            ConnectorOAuthRequest=ConnectorOAuthRequest,
            RefreshToken=RefreshToken,
            **kwargs
        )
        super(GoogleAnalyticsConnectorProfileCredentials, self).__init__(**processed_kwargs)


class InforNexusConnectorProfileCredentials(troposphere.appflow.InforNexusConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 AccessKeyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Datakey=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecretAccessKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessKeyId=AccessKeyId,
            Datakey=Datakey,
            SecretAccessKey=SecretAccessKey,
            UserId=UserId,
            **kwargs
        )
        super(InforNexusConnectorProfileCredentials, self).__init__(**processed_kwargs)


class MarketoConnectorProfileCredentials(troposphere.appflow.MarketoConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectorOAuthRequest=NOTHING, # type: _ConnectorOAuthRequest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            AccessToken=AccessToken,
            ConnectorOAuthRequest=ConnectorOAuthRequest,
            **kwargs
        )
        super(MarketoConnectorProfileCredentials, self).__init__(**processed_kwargs)


class RedshiftConnectorProfileCredentials(troposphere.appflow.RedshiftConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            **kwargs
        )
        super(RedshiftConnectorProfileCredentials, self).__init__(**processed_kwargs)


class SalesforceConnectorProfileCredentials(troposphere.appflow.SalesforceConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectorOAuthRequest=NOTHING, # type: _ConnectorOAuthRequest
                 RefreshToken=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessToken=AccessToken,
            ConnectorOAuthRequest=ConnectorOAuthRequest,
            RefreshToken=RefreshToken,
            **kwargs
        )
        super(SalesforceConnectorProfileCredentials, self).__init__(**processed_kwargs)


class ServiceNowConnectorProfileCredentials(troposphere.appflow.ServiceNowConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            **kwargs
        )
        super(ServiceNowConnectorProfileCredentials, self).__init__(**processed_kwargs)


class SingularConnectorProfileCredentials(troposphere.appflow.SingularConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ApiKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiKey=ApiKey,
            **kwargs
        )
        super(SingularConnectorProfileCredentials, self).__init__(**processed_kwargs)


class SlackConnectorProfileCredentials(troposphere.appflow.SlackConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectorOAuthRequest=NOTHING, # type: _ConnectorOAuthRequest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            AccessToken=AccessToken,
            ConnectorOAuthRequest=ConnectorOAuthRequest,
            **kwargs
        )
        super(SlackConnectorProfileCredentials, self).__init__(**processed_kwargs)


class SnowflakeConnectorProfileCredentials(troposphere.appflow.SnowflakeConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            **kwargs
        )
        super(SnowflakeConnectorProfileCredentials, self).__init__(**processed_kwargs)


class TrendmicroConnectorProfileCredentials(troposphere.appflow.TrendmicroConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ApiSecretKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ApiSecretKey=ApiSecretKey,
            **kwargs
        )
        super(TrendmicroConnectorProfileCredentials, self).__init__(**processed_kwargs)


class VeevaConnectorProfileCredentials(troposphere.appflow.VeevaConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 Password=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Password=Password,
            Username=Username,
            **kwargs
        )
        super(VeevaConnectorProfileCredentials, self).__init__(**processed_kwargs)


class ZendeskConnectorProfileCredentials(troposphere.appflow.ZendeskConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 ClientId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessToken=NOTHING, # type: Union[str, AWSHelperFn]
                 ConnectorOAuthRequest=NOTHING, # type: _ConnectorOAuthRequest
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientId=ClientId,
            ClientSecret=ClientSecret,
            AccessToken=AccessToken,
            ConnectorOAuthRequest=ConnectorOAuthRequest,
            **kwargs
        )
        super(ZendeskConnectorProfileCredentials, self).__init__(**processed_kwargs)


class ConnectorProfileCredentials(troposphere.appflow.ConnectorProfileCredentials, Mixin):
    def __init__(self,
                 title=None,
                 Amplitude=NOTHING, # type: _AmplitudeConnectorProfileCredentials
                 Datadog=NOTHING, # type: _DatadogConnectorProfileCredentials
                 Dynatrace=NOTHING, # type: _DynatraceConnectorProfileCredentials
                 GoogleAnalytics=NOTHING, # type: _GoogleAnalyticsConnectorProfileCredentials
                 InforNexus=NOTHING, # type: _InforNexusConnectorProfileCredentials
                 Marketo=NOTHING, # type: _MarketoConnectorProfileCredentials
                 Redshift=NOTHING, # type: _RedshiftConnectorProfileCredentials
                 Salesforce=NOTHING, # type: _SalesforceConnectorProfileCredentials
                 ServiceNow=NOTHING, # type: _ServiceNowConnectorProfileCredentials
                 Singular=NOTHING, # type: _SingularConnectorProfileCredentials
                 Slack=NOTHING, # type: _SlackConnectorProfileCredentials
                 Snowflake=NOTHING, # type: _SnowflakeConnectorProfileCredentials
                 Trendmicro=NOTHING, # type: _TrendmicroConnectorProfileCredentials
                 Veeva=NOTHING, # type: _VeevaConnectorProfileCredentials
                 Zendesk=NOTHING, # type: _ZendeskConnectorProfileCredentials
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Amplitude=Amplitude,
            Datadog=Datadog,
            Dynatrace=Dynatrace,
            GoogleAnalytics=GoogleAnalytics,
            InforNexus=InforNexus,
            Marketo=Marketo,
            Redshift=Redshift,
            Salesforce=Salesforce,
            ServiceNow=ServiceNow,
            Singular=Singular,
            Slack=Slack,
            Snowflake=Snowflake,
            Trendmicro=Trendmicro,
            Veeva=Veeva,
            Zendesk=Zendesk,
            **kwargs
        )
        super(ConnectorProfileCredentials, self).__init__(**processed_kwargs)


class DatadogConnectorProfileProperties(troposphere.appflow.DatadogConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(DatadogConnectorProfileProperties, self).__init__(**processed_kwargs)


class DynatraceConnectorProfileProperties(troposphere.appflow.DynatraceConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(DynatraceConnectorProfileProperties, self).__init__(**processed_kwargs)


class InforNexusConnectorProfileProperties(troposphere.appflow.InforNexusConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(InforNexusConnectorProfileProperties, self).__init__(**processed_kwargs)


class MarketoConnectorProfileProperties(troposphere.appflow.MarketoConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(MarketoConnectorProfileProperties, self).__init__(**processed_kwargs)


class RedshiftConnectorProfileProperties(troposphere.appflow.RedshiftConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            DatabaseUrl=DatabaseUrl,
            RoleArn=RoleArn,
            BucketPrefix=BucketPrefix,
            **kwargs
        )
        super(RedshiftConnectorProfileProperties, self).__init__(**processed_kwargs)


class SalesforceConnectorProfileProperties(troposphere.appflow.SalesforceConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 isSandboxEnvironment=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            isSandboxEnvironment=isSandboxEnvironment,
            **kwargs
        )
        super(SalesforceConnectorProfileProperties, self).__init__(**processed_kwargs)


class ServiceNowConnectorProfileProperties(troposphere.appflow.ServiceNowConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(ServiceNowConnectorProfileProperties, self).__init__(**processed_kwargs)


class SlackConnectorProfileProperties(troposphere.appflow.SlackConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(SlackConnectorProfileProperties, self).__init__(**processed_kwargs)


class SnowflakeConnectorProfileProperties(troposphere.appflow.SnowflakeConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Stage=REQUIRED, # type: Union[str, AWSHelperFn]
                 Warehouse=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccountName=NOTHING, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 PrivateLinkServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 Region=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            Stage=Stage,
            Warehouse=Warehouse,
            AccountName=AccountName,
            BucketPrefix=BucketPrefix,
            PrivateLinkServiceName=PrivateLinkServiceName,
            Region=Region,
            **kwargs
        )
        super(SnowflakeConnectorProfileProperties, self).__init__(**processed_kwargs)


class VeevaConnectorProfileProperties(troposphere.appflow.VeevaConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(VeevaConnectorProfileProperties, self).__init__(**processed_kwargs)


class ZendeskConnectorProfileProperties(troposphere.appflow.ZendeskConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 InstanceUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InstanceUrl=InstanceUrl,
            **kwargs
        )
        super(ZendeskConnectorProfileProperties, self).__init__(**processed_kwargs)


class ConnectorProfileProperties(troposphere.appflow.ConnectorProfileProperties, Mixin):
    def __init__(self,
                 title=None,
                 Datadog=NOTHING, # type: _DatadogConnectorProfileProperties
                 Dynatrace=NOTHING, # type: _DynatraceConnectorProfileProperties
                 InforNexus=NOTHING, # type: _InforNexusConnectorProfileProperties
                 Marketo=NOTHING, # type: _MarketoConnectorProfileProperties
                 Redshift=NOTHING, # type: _RedshiftConnectorProfileProperties
                 Salesforce=NOTHING, # type: _SalesforceConnectorProfileProperties
                 ServiceNow=NOTHING, # type: _ServiceNowConnectorProfileProperties
                 Slack=NOTHING, # type: _SlackConnectorProfileProperties
                 Snowflake=NOTHING, # type: _SnowflakeConnectorProfileProperties
                 Veeva=NOTHING, # type: _VeevaConnectorProfileProperties
                 Zendesk=NOTHING, # type: _ZendeskConnectorProfileProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Datadog=Datadog,
            Dynatrace=Dynatrace,
            InforNexus=InforNexus,
            Marketo=Marketo,
            Redshift=Redshift,
            Salesforce=Salesforce,
            ServiceNow=ServiceNow,
            Slack=Slack,
            Snowflake=Snowflake,
            Veeva=Veeva,
            Zendesk=Zendesk,
            **kwargs
        )
        super(ConnectorProfileProperties, self).__init__(**processed_kwargs)


class ConnectorProfileConfig(troposphere.appflow.ConnectorProfileConfig, Mixin):
    def __init__(self,
                 title=None,
                 ConnectorProfileCredentials=REQUIRED, # type: _ConnectorProfileCredentials
                 ConnectorProfileProperties=NOTHING, # type: _ConnectorProfileProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectorProfileCredentials=ConnectorProfileCredentials,
            ConnectorProfileProperties=ConnectorProfileProperties,
            **kwargs
        )
        super(ConnectorProfileConfig, self).__init__(**processed_kwargs)


class ConnectorProfile(troposphere.appflow.ConnectorProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConnectionMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectorProfileName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectorType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectorProfileConfig=NOTHING, # type: _ConnectorProfileConfig
                 KMSArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConnectionMode=ConnectionMode,
            ConnectorProfileName=ConnectorProfileName,
            ConnectorType=ConnectorType,
            ConnectorProfileConfig=ConnectorProfileConfig,
            KMSArn=KMSArn,
            **kwargs
        )
        super(ConnectorProfile, self).__init__(**processed_kwargs)


class ErrorHandlingConfig(troposphere.appflow.ErrorHandlingConfig, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 FailOnFirstError=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            BucketPrefix=BucketPrefix,
            FailOnFirstError=FailOnFirstError,
            **kwargs
        )
        super(ErrorHandlingConfig, self).__init__(**processed_kwargs)


class EventBridgeDestinationProperties(troposphere.appflow.EventBridgeDestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 ErrorHandlingConfig=NOTHING, # type: _ErrorHandlingConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            ErrorHandlingConfig=ErrorHandlingConfig,
            **kwargs
        )
        super(EventBridgeDestinationProperties, self).__init__(**processed_kwargs)


class RedshiftDestinationProperties(troposphere.appflow.RedshiftDestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 IntermediateBucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 ErrorHandlingConfig=NOTHING, # type: _ErrorHandlingConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IntermediateBucketName=IntermediateBucketName,
            Object=Object,
            BucketPrefix=BucketPrefix,
            ErrorHandlingConfig=ErrorHandlingConfig,
            **kwargs
        )
        super(RedshiftDestinationProperties, self).__init__(**processed_kwargs)


class AggregationConfig(troposphere.appflow.AggregationConfig, Mixin):
    def __init__(self,
                 title=None,
                 AggregationType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregationType=AggregationType,
            **kwargs
        )
        super(AggregationConfig, self).__init__(**processed_kwargs)


class PrefixConfig(troposphere.appflow.PrefixConfig, Mixin):
    def __init__(self,
                 title=None,
                 PrefixFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 PrefixType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PrefixFormat=PrefixFormat,
            PrefixType=PrefixType,
            **kwargs
        )
        super(PrefixConfig, self).__init__(**processed_kwargs)


class S3OutputFormatConfig(troposphere.appflow.S3OutputFormatConfig, Mixin):
    def __init__(self,
                 title=None,
                 AggregationConfig=NOTHING, # type: _AggregationConfig
                 FileType=NOTHING, # type: Union[str, AWSHelperFn]
                 PrefixConfig=NOTHING, # type: _PrefixConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregationConfig=AggregationConfig,
            FileType=FileType,
            PrefixConfig=PrefixConfig,
            **kwargs
        )
        super(S3OutputFormatConfig, self).__init__(**processed_kwargs)


class S3DestinationProperties(troposphere.appflow.S3DestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 S3OutputFormatConfig=NOTHING, # type: _S3OutputFormatConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            BucketPrefix=BucketPrefix,
            S3OutputFormatConfig=S3OutputFormatConfig,
            **kwargs
        )
        super(S3DestinationProperties, self).__init__(**processed_kwargs)


class SalesforceDestinationProperties(troposphere.appflow.SalesforceDestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 ErrorHandlingConfig=NOTHING, # type: _ErrorHandlingConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            ErrorHandlingConfig=ErrorHandlingConfig,
            **kwargs
        )
        super(SalesforceDestinationProperties, self).__init__(**processed_kwargs)


class SnowflakeDestinationProperties(troposphere.appflow.SnowflakeDestinationProperties, Mixin):
    def __init__(self,
                 title=None,
                 IntermediateBucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 ErrorHandlingConfig=NOTHING, # type: _ErrorHandlingConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IntermediateBucketName=IntermediateBucketName,
            Object=Object,
            BucketPrefix=BucketPrefix,
            ErrorHandlingConfig=ErrorHandlingConfig,
            **kwargs
        )
        super(SnowflakeDestinationProperties, self).__init__(**processed_kwargs)


class DestinationConnectorProperties(troposphere.appflow.DestinationConnectorProperties, Mixin):
    def __init__(self,
                 title=None,
                 EventBridge=NOTHING, # type: _EventBridgeDestinationProperties
                 Redshift=NOTHING, # type: _RedshiftDestinationProperties
                 S3=NOTHING, # type: _S3DestinationProperties
                 Salesforce=NOTHING, # type: _SalesforceDestinationProperties
                 Snowflake=NOTHING, # type: _SnowflakeDestinationProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventBridge=EventBridge,
            Redshift=Redshift,
            S3=S3,
            Salesforce=Salesforce,
            Snowflake=Snowflake,
            **kwargs
        )
        super(DestinationConnectorProperties, self).__init__(**processed_kwargs)


class DestinationFlowConfig(troposphere.appflow.DestinationFlowConfig, Mixin):
    def __init__(self,
                 title=None,
                 ConnectorType=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationConnectorProperties=REQUIRED, # type: _DestinationConnectorProperties
                 ConnectorProfileName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectorType=ConnectorType,
            DestinationConnectorProperties=DestinationConnectorProperties,
            ConnectorProfileName=ConnectorProfileName,
            **kwargs
        )
        super(DestinationFlowConfig, self).__init__(**processed_kwargs)


class AmplitudeSourceProperties(troposphere.appflow.AmplitudeSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(AmplitudeSourceProperties, self).__init__(**processed_kwargs)


class DatadogSourceProperties(troposphere.appflow.DatadogSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(DatadogSourceProperties, self).__init__(**processed_kwargs)


class DynatraceSourceProperties(troposphere.appflow.DynatraceSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(DynatraceSourceProperties, self).__init__(**processed_kwargs)


class GoogleAnalyticsSourceProperties(troposphere.appflow.GoogleAnalyticsSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(GoogleAnalyticsSourceProperties, self).__init__(**processed_kwargs)


class InforNexusSourceProperties(troposphere.appflow.InforNexusSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(InforNexusSourceProperties, self).__init__(**processed_kwargs)


class MarketoSourceProperties(troposphere.appflow.MarketoSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(MarketoSourceProperties, self).__init__(**processed_kwargs)


class S3SourceProperties(troposphere.appflow.S3SourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketPrefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            BucketPrefix=BucketPrefix,
            **kwargs
        )
        super(S3SourceProperties, self).__init__(**processed_kwargs)


class SalesforceSourceProperties(troposphere.appflow.SalesforceSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 EnableDynamicFieldUpdate=NOTHING, # type: bool
                 IncludeDeletedRecords=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            EnableDynamicFieldUpdate=EnableDynamicFieldUpdate,
            IncludeDeletedRecords=IncludeDeletedRecords,
            **kwargs
        )
        super(SalesforceSourceProperties, self).__init__(**processed_kwargs)


class ServiceNowSourceProperties(troposphere.appflow.ServiceNowSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(ServiceNowSourceProperties, self).__init__(**processed_kwargs)


class SingularSourceProperties(troposphere.appflow.SingularSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(SingularSourceProperties, self).__init__(**processed_kwargs)


class SlackSourceProperties(troposphere.appflow.SlackSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(SlackSourceProperties, self).__init__(**processed_kwargs)


class TrendmicroSourceProperties(troposphere.appflow.TrendmicroSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(TrendmicroSourceProperties, self).__init__(**processed_kwargs)


class VeevaSourceProperties(troposphere.appflow.VeevaSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(VeevaSourceProperties, self).__init__(**processed_kwargs)


class ZendeskSourceProperties(troposphere.appflow.ZendeskSourceProperties, Mixin):
    def __init__(self,
                 title=None,
                 Object=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Object=Object,
            **kwargs
        )
        super(ZendeskSourceProperties, self).__init__(**processed_kwargs)


class SourceConnectorProperties(troposphere.appflow.SourceConnectorProperties, Mixin):
    def __init__(self,
                 title=None,
                 Amplitude=NOTHING, # type: _AmplitudeSourceProperties
                 Datadog=NOTHING, # type: _DatadogSourceProperties
                 Dynatrace=NOTHING, # type: _DynatraceSourceProperties
                 GoogleAnalytics=NOTHING, # type: _GoogleAnalyticsSourceProperties
                 InforNexus=NOTHING, # type: _InforNexusSourceProperties
                 Marketo=NOTHING, # type: _MarketoSourceProperties
                 S3=NOTHING, # type: _S3SourceProperties
                 Salesforce=NOTHING, # type: _SalesforceSourceProperties
                 ServiceNow=NOTHING, # type: _ServiceNowSourceProperties
                 Singular=NOTHING, # type: _SingularSourceProperties
                 Slack=NOTHING, # type: _SlackSourceProperties
                 Trendmicro=NOTHING, # type: _TrendmicroSourceProperties
                 Veeva=NOTHING, # type: _VeevaSourceProperties
                 Zendesk=NOTHING, # type: _ZendeskSourceProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Amplitude=Amplitude,
            Datadog=Datadog,
            Dynatrace=Dynatrace,
            GoogleAnalytics=GoogleAnalytics,
            InforNexus=InforNexus,
            Marketo=Marketo,
            S3=S3,
            Salesforce=Salesforce,
            ServiceNow=ServiceNow,
            Singular=Singular,
            Slack=Slack,
            Trendmicro=Trendmicro,
            Veeva=Veeva,
            Zendesk=Zendesk,
            **kwargs
        )
        super(SourceConnectorProperties, self).__init__(**processed_kwargs)


class SourceFlowConfig(troposphere.appflow.SourceFlowConfig, Mixin):
    def __init__(self,
                 title=None,
                 ConnectorType=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceConnectorProperties=REQUIRED, # type: _SourceConnectorProperties
                 ConnectorProfileName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConnectorType=ConnectorType,
            SourceConnectorProperties=SourceConnectorProperties,
            ConnectorProfileName=ConnectorProfileName,
            **kwargs
        )
        super(SourceFlowConfig, self).__init__(**processed_kwargs)


class ConnectorOperator(troposphere.appflow.ConnectorOperator, Mixin):
    def __init__(self,
                 title=None,
                 Amplitude=NOTHING, # type: Union[str, AWSHelperFn]
                 Datadog=NOTHING, # type: Union[str, AWSHelperFn]
                 Dynatrace=NOTHING, # type: Union[str, AWSHelperFn]
                 GoogleAnalytics=NOTHING, # type: Union[str, AWSHelperFn]
                 InforNexus=NOTHING, # type: Union[str, AWSHelperFn]
                 Marketo=NOTHING, # type: Union[str, AWSHelperFn]
                 S3=NOTHING, # type: Union[str, AWSHelperFn]
                 Salesforce=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceNow=NOTHING, # type: Union[str, AWSHelperFn]
                 Singular=NOTHING, # type: Union[str, AWSHelperFn]
                 Slack=NOTHING, # type: Union[str, AWSHelperFn]
                 Trendmicro=NOTHING, # type: Union[str, AWSHelperFn]
                 Veeva=NOTHING, # type: Union[str, AWSHelperFn]
                 Zendesk=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Amplitude=Amplitude,
            Datadog=Datadog,
            Dynatrace=Dynatrace,
            GoogleAnalytics=GoogleAnalytics,
            InforNexus=InforNexus,
            Marketo=Marketo,
            S3=S3,
            Salesforce=Salesforce,
            ServiceNow=ServiceNow,
            Singular=Singular,
            Slack=Slack,
            Trendmicro=Trendmicro,
            Veeva=Veeva,
            Zendesk=Zendesk,
            **kwargs
        )
        super(ConnectorOperator, self).__init__(**processed_kwargs)


class TaskPropertiesObject(troposphere.appflow.TaskPropertiesObject, Mixin):
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
        super(TaskPropertiesObject, self).__init__(**processed_kwargs)


class Task(troposphere.appflow.Task, Mixin):
    def __init__(self,
                 title=None,
                 SourceFields=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 TaskType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectorOperator=NOTHING, # type: _ConnectorOperator
                 DestinationField=NOTHING, # type: Union[str, AWSHelperFn]
                 TaskProperties=NOTHING, # type: List[_TaskPropertiesObject]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceFields=SourceFields,
            TaskType=TaskType,
            ConnectorOperator=ConnectorOperator,
            DestinationField=DestinationField,
            TaskProperties=TaskProperties,
            **kwargs
        )
        super(Task, self).__init__(**processed_kwargs)


class ScheduledTriggerProperties(troposphere.appflow.ScheduledTriggerProperties, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataPullMode=NOTHING, # type: Union[str, AWSHelperFn]
                 ScheduleEndTime=NOTHING, # type: float
                 ScheduleStartTime=NOTHING, # type: float
                 TimeZone=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            DataPullMode=DataPullMode,
            ScheduleEndTime=ScheduleEndTime,
            ScheduleStartTime=ScheduleStartTime,
            TimeZone=TimeZone,
            **kwargs
        )
        super(ScheduledTriggerProperties, self).__init__(**processed_kwargs)


class TriggerConfig(troposphere.appflow.TriggerConfig, Mixin):
    def __init__(self,
                 title=None,
                 TriggerType=REQUIRED, # type: Union[str, AWSHelperFn]
                 TriggerProperties=NOTHING, # type: _ScheduledTriggerProperties
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TriggerType=TriggerType,
            TriggerProperties=TriggerProperties,
            **kwargs
        )
        super(TriggerConfig, self).__init__(**processed_kwargs)


class Flow(troposphere.appflow.Flow, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationFlowConfigList=REQUIRED, # type: List[_DestinationFlowConfig]
                 FlowName=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceFlowConfig=REQUIRED, # type: _SourceFlowConfig
                 Tasks=REQUIRED, # type: List[_Task]
                 TriggerConfig=REQUIRED, # type: _TriggerConfig
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 KMSArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationFlowConfigList=DestinationFlowConfigList,
            FlowName=FlowName,
            SourceFlowConfig=SourceFlowConfig,
            Tasks=Tasks,
            TriggerConfig=TriggerConfig,
            Description=Description,
            KMSArn=KMSArn,
            Tags=Tags,
            **kwargs
        )
        super(Flow, self).__init__(**processed_kwargs)
