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
    AssetPropertyTimestamp as _AssetPropertyTimestamp,
    AssetPropertyValue as _AssetPropertyValue,
    AssetPropertyVariant as _AssetPropertyVariant,
    CloudwatchAlarmAction as _CloudwatchAlarmAction,
    CloudwatchMetricAction as _CloudwatchMetricAction,
    DynamoDBAction as _DynamoDBAction,
    DynamoDBv2Action as _DynamoDBv2Action,
    ElasticsearchAction as _ElasticsearchAction,
    FirehoseAction as _FirehoseAction,
    HttpAction as _HttpAction,
    HttpActionHeader as _HttpActionHeader,
    HttpAuthorization as _HttpAuthorization,
    IotAnalyticsAction as _IotAnalyticsAction,
    IotEventsAction as _IotEventsAction,
    IotSiteWiseAction as _IotSiteWiseAction,
    KinesisAction as _KinesisAction,
    LambdaAction as _LambdaAction,
    ProvisioningHook as _ProvisioningHook,
    PutAssetPropertyValueEntry as _PutAssetPropertyValueEntry,
    PutItemInput as _PutItemInput,
    RepublishAction as _RepublishAction,
    S3Action as _S3Action,
    SigV4Authorization as _SigV4Authorization,
    SnsAction as _SnsAction,
    SqsAction as _SqsAction,
    StepFunctionsAction as _StepFunctionsAction,
    TopicRulePayload as _TopicRulePayload,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



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


class Certificate(troposphere.iot.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CertificateSigningRequest=REQUIRED, # type: Union[str, AWSHelperFn]
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateSigningRequest=CertificateSigningRequest,
            Status=Status,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)


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
