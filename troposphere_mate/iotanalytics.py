# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iotanalytics

from troposphere.iotanalytics import (
    Action as _Action,
    Activity as _Activity,
    ActivityChannel as _ActivityChannel,
    ActivityDatastore as _ActivityDatastore,
    AddAttributes as _AddAttributes,
    ChannelStorage as _ChannelStorage,
    Column as _Column,
    ContainerAction as _ContainerAction,
    CustomerManagedS3 as _CustomerManagedS3,
    DatasetContentDeliveryRule as _DatasetContentDeliveryRule,
    DatasetContentDeliveryRuleDestination as _DatasetContentDeliveryRuleDestination,
    DatasetContentVersionValue as _DatasetContentVersionValue,
    DatastoreStorage as _DatastoreStorage,
    DeltaTime as _DeltaTime,
    DeltaTimeSessionWindowConfiguration as _DeltaTimeSessionWindowConfiguration,
    DeviceRegistryEnrich as _DeviceRegistryEnrich,
    DeviceShadowEnrich as _DeviceShadowEnrich,
    FileFormatConfiguration as _FileFormatConfiguration,
    Filter as _Filter,
    GlueConfiguration as _GlueConfiguration,
    IotEventsDestinationConfiguration as _IotEventsDestinationConfiguration,
    Lambda as _Lambda,
    LateDataRule as _LateDataRule,
    LateDataRuleConfiguration as _LateDataRuleConfiguration,
    Math as _Math,
    OutputFileUriValue as _OutputFileUriValue,
    ParquetConfiguration as _ParquetConfiguration,
    QueryAction as _QueryAction,
    QueryActionFilter as _QueryActionFilter,
    RemoveAttributes as _RemoveAttributes,
    ResourceConfiguration as _ResourceConfiguration,
    RetentionPeriod as _RetentionPeriod,
    S3DestinationConfiguration as _S3DestinationConfiguration,
    Schedule as _Schedule,
    SchemaDefinition as _SchemaDefinition,
    SelectAttributes as _SelectAttributes,
    ServiceManagedS3 as _ServiceManagedS3,
    Tags as _Tags,
    Trigger as _Trigger,
    TriggeringDataset as _TriggeringDataset,
    Variable as _Variable,
    VersioningConfiguration as _VersioningConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class RetentionPeriod(troposphere.iotanalytics.RetentionPeriod, Mixin):
    def __init__(self,
                 title=None,
                 NumberOfDays=NOTHING, # type: int
                 Unlimited=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NumberOfDays=NumberOfDays,
            Unlimited=Unlimited,
            **kwargs
        )
        super(RetentionPeriod, self).__init__(**processed_kwargs)


class CustomerManagedS3(troposphere.iotanalytics.CustomerManagedS3, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 KeyPrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            RoleArn=RoleArn,
            KeyPrefix=KeyPrefix,
            **kwargs
        )
        super(CustomerManagedS3, self).__init__(**processed_kwargs)


class ServiceManagedS3(troposphere.iotanalytics.ServiceManagedS3, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(ServiceManagedS3, self).__init__(**processed_kwargs)


class ChannelStorage(troposphere.iotanalytics.ChannelStorage, Mixin):
    def __init__(self,
                 title=None,
                 CustomerManagedS3=NOTHING, # type: _CustomerManagedS3
                 ServiceManagedS3=NOTHING, # type: _ServiceManagedS3
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CustomerManagedS3=CustomerManagedS3,
            ServiceManagedS3=ServiceManagedS3,
            **kwargs
        )
        super(ChannelStorage, self).__init__(**processed_kwargs)


class Channel(troposphere.iotanalytics.Channel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ChannelName=NOTHING, # type: Union[str, AWSHelperFn]
                 ChannelStorage=NOTHING, # type: _ChannelStorage
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ChannelName=ChannelName,
            ChannelStorage=ChannelStorage,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class AddAttributes(troposphere.iotanalytics.AddAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: dict
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(AddAttributes, self).__init__(**processed_kwargs)


class ActivityChannel(troposphere.iotanalytics.ActivityChannel, Mixin):
    def __init__(self,
                 title=None,
                 ChannelName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChannelName=ChannelName,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(ActivityChannel, self).__init__(**processed_kwargs)


class ActivityDatastore(troposphere.iotanalytics.ActivityDatastore, Mixin):
    def __init__(self,
                 title=None,
                 DatastoreName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatastoreName=DatastoreName,
            Name=Name,
            **kwargs
        )
        super(ActivityDatastore, self).__init__(**processed_kwargs)


class DeviceRegistryEnrich(troposphere.iotanalytics.DeviceRegistryEnrich, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Name=Name,
            Next=Next,
            RoleArn=RoleArn,
            ThingName=ThingName,
            **kwargs
        )
        super(DeviceRegistryEnrich, self).__init__(**processed_kwargs)


class DeviceShadowEnrich(troposphere.iotanalytics.DeviceShadowEnrich, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ThingName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Name=Name,
            Next=Next,
            RoleArn=RoleArn,
            ThingName=ThingName,
            **kwargs
        )
        super(DeviceShadowEnrich, self).__init__(**processed_kwargs)


class Filter(troposphere.iotanalytics.Filter, Mixin):
    def __init__(self,
                 title=None,
                 Filter=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Filter=Filter,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Filter, self).__init__(**processed_kwargs)


class Lambda(troposphere.iotanalytics.Lambda, Mixin):
    def __init__(self,
                 title=None,
                 BatchSize=NOTHING, # type: int
                 LambdaName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BatchSize=BatchSize,
            LambdaName=LambdaName,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Lambda, self).__init__(**processed_kwargs)


class Math(troposphere.iotanalytics.Math, Mixin):
    def __init__(self,
                 title=None,
                 Attribute=NOTHING, # type: Union[str, AWSHelperFn]
                 Math=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attribute=Attribute,
            Math=Math,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(Math, self).__init__(**processed_kwargs)


class RemoveAttributes(troposphere.iotanalytics.RemoveAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(RemoveAttributes, self).__init__(**processed_kwargs)


class SelectAttributes(troposphere.iotanalytics.SelectAttributes, Mixin):
    def __init__(self,
                 title=None,
                 Attributes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Next=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Attributes=Attributes,
            Name=Name,
            Next=Next,
            **kwargs
        )
        super(SelectAttributes, self).__init__(**processed_kwargs)


class Activity(troposphere.iotanalytics.Activity, Mixin):
    def __init__(self,
                 title=None,
                 AddAttributes=NOTHING, # type: _AddAttributes
                 Channel=NOTHING, # type: _ActivityChannel
                 Datastore=NOTHING, # type: _ActivityDatastore
                 DeviceRegistryEnrich=NOTHING, # type: _DeviceRegistryEnrich
                 DeviceShadowEnrich=NOTHING, # type: _DeviceShadowEnrich
                 Filter=NOTHING, # type: _Filter
                 Lambda=NOTHING, # type: _Lambda
                 Math=NOTHING, # type: _Math
                 RemoveAttributes=NOTHING, # type: _RemoveAttributes
                 SelectAttributes=NOTHING, # type: _SelectAttributes
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddAttributes=AddAttributes,
            Channel=Channel,
            Datastore=Datastore,
            DeviceRegistryEnrich=DeviceRegistryEnrich,
            DeviceShadowEnrich=DeviceShadowEnrich,
            Filter=Filter,
            Lambda=Lambda,
            Math=Math,
            RemoveAttributes=RemoveAttributes,
            SelectAttributes=SelectAttributes,
            **kwargs
        )
        super(Activity, self).__init__(**processed_kwargs)


class Pipeline(troposphere.iotanalytics.Pipeline, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PipelineActivities=REQUIRED, # type: List[_Activity]
                 PipelineName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PipelineActivities=PipelineActivities,
            PipelineName=PipelineName,
            Tags=Tags,
            **kwargs
        )
        super(Pipeline, self).__init__(**processed_kwargs)


class ResourceConfiguration(troposphere.iotanalytics.ResourceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ComputeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 VolumeSizeInGB=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeType=ComputeType,
            VolumeSizeInGB=VolumeSizeInGB,
            **kwargs
        )
        super(ResourceConfiguration, self).__init__(**processed_kwargs)


class DatasetContentVersionValue(troposphere.iotanalytics.DatasetContentVersionValue, Mixin):
    def __init__(self,
                 title=None,
                 DatasetName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetName=DatasetName,
            **kwargs
        )
        super(DatasetContentVersionValue, self).__init__(**processed_kwargs)


class OutputFileUriValue(troposphere.iotanalytics.OutputFileUriValue, Mixin):
    def __init__(self,
                 title=None,
                 FileName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FileName=FileName,
            **kwargs
        )
        super(OutputFileUriValue, self).__init__(**processed_kwargs)


class Variable(troposphere.iotanalytics.Variable, Mixin):
    def __init__(self,
                 title=None,
                 DatasetContentVersionValue=NOTHING, # type: _DatasetContentVersionValue
                 DoubleValue=NOTHING, # type: float
                 OutputFileUriValue=NOTHING, # type: _OutputFileUriValue
                 StringValue=NOTHING, # type: Union[str, AWSHelperFn]
                 VariableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetContentVersionValue=DatasetContentVersionValue,
            DoubleValue=DoubleValue,
            OutputFileUriValue=OutputFileUriValue,
            StringValue=StringValue,
            VariableName=VariableName,
            **kwargs
        )
        super(Variable, self).__init__(**processed_kwargs)


class ContainerAction(troposphere.iotanalytics.ContainerAction, Mixin):
    def __init__(self,
                 title=None,
                 ExecutionRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceConfiguration=NOTHING, # type: _ResourceConfiguration
                 Variables=NOTHING, # type: List[_Variable]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExecutionRoleArn=ExecutionRoleArn,
            Image=Image,
            ResourceConfiguration=ResourceConfiguration,
            Variables=Variables,
            **kwargs
        )
        super(ContainerAction, self).__init__(**processed_kwargs)


class DeltaTime(troposphere.iotanalytics.DeltaTime, Mixin):
    def __init__(self,
                 title=None,
                 TimeExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 OffsetSeconds=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeExpression=TimeExpression,
            OffsetSeconds=OffsetSeconds,
            **kwargs
        )
        super(DeltaTime, self).__init__(**processed_kwargs)


class QueryActionFilter(troposphere.iotanalytics.QueryActionFilter, Mixin):
    def __init__(self,
                 title=None,
                 DeltaTime=NOTHING, # type: _DeltaTime
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeltaTime=DeltaTime,
            **kwargs
        )
        super(QueryActionFilter, self).__init__(**processed_kwargs)


class QueryAction(troposphere.iotanalytics.QueryAction, Mixin):
    def __init__(self,
                 title=None,
                 Filters=NOTHING, # type: List[_QueryActionFilter]
                 SqlQuery=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Filters=Filters,
            SqlQuery=SqlQuery,
            **kwargs
        )
        super(QueryAction, self).__init__(**processed_kwargs)


class Action(troposphere.iotanalytics.Action, Mixin):
    def __init__(self,
                 title=None,
                 ActionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContainerAction=NOTHING, # type: _ContainerAction
                 QueryAction=NOTHING, # type: _QueryAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActionName=ActionName,
            ContainerAction=ContainerAction,
            QueryAction=QueryAction,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class IotEventsDestinationConfiguration(troposphere.iotanalytics.IotEventsDestinationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 InputName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            InputName=InputName,
            RoleArn=RoleArn,
            **kwargs
        )
        super(IotEventsDestinationConfiguration, self).__init__(**processed_kwargs)


class GlueConfiguration(troposphere.iotanalytics.GlueConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseName=DatabaseName,
            TableName=TableName,
            **kwargs
        )
        super(GlueConfiguration, self).__init__(**processed_kwargs)


class S3DestinationConfiguration(troposphere.iotanalytics.S3DestinationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 GlueConfiguration=NOTHING, # type: _GlueConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            RoleArn=RoleArn,
            GlueConfiguration=GlueConfiguration,
            **kwargs
        )
        super(S3DestinationConfiguration, self).__init__(**processed_kwargs)


class DatasetContentDeliveryRuleDestination(troposphere.iotanalytics.DatasetContentDeliveryRuleDestination, Mixin):
    def __init__(self,
                 title=None,
                 IotEventsDestinationConfiguration=NOTHING, # type: _IotEventsDestinationConfiguration
                 S3DestinationConfiguration=NOTHING, # type: _S3DestinationConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IotEventsDestinationConfiguration=IotEventsDestinationConfiguration,
            S3DestinationConfiguration=S3DestinationConfiguration,
            **kwargs
        )
        super(DatasetContentDeliveryRuleDestination, self).__init__(**processed_kwargs)


class DatasetContentDeliveryRule(troposphere.iotanalytics.DatasetContentDeliveryRule, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: _DatasetContentDeliveryRuleDestination
                 EntryName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            EntryName=EntryName,
            **kwargs
        )
        super(DatasetContentDeliveryRule, self).__init__(**processed_kwargs)


class DeltaTimeSessionWindowConfiguration(troposphere.iotanalytics.DeltaTimeSessionWindowConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 TimeoutInMinutes=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TimeoutInMinutes=TimeoutInMinutes,
            **kwargs
        )
        super(DeltaTimeSessionWindowConfiguration, self).__init__(**processed_kwargs)


class LateDataRuleConfiguration(troposphere.iotanalytics.LateDataRuleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DeltaTimeSessionWindowConfiguration=NOTHING, # type: _DeltaTimeSessionWindowConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeltaTimeSessionWindowConfiguration=DeltaTimeSessionWindowConfiguration,
            **kwargs
        )
        super(LateDataRuleConfiguration, self).__init__(**processed_kwargs)


class LateDataRule(troposphere.iotanalytics.LateDataRule, Mixin):
    def __init__(self,
                 title=None,
                 RuleConfiguration=REQUIRED, # type: _LateDataRuleConfiguration
                 RuleName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RuleConfiguration=RuleConfiguration,
            RuleName=RuleName,
            **kwargs
        )
        super(LateDataRule, self).__init__(**processed_kwargs)


class Schedule(troposphere.iotanalytics.Schedule, Mixin):
    def __init__(self,
                 title=None,
                 ScheduleExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ScheduleExpression=ScheduleExpression,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)


class TriggeringDataset(troposphere.iotanalytics.TriggeringDataset, Mixin):
    def __init__(self,
                 title=None,
                 DatasetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatasetName=DatasetName,
            **kwargs
        )
        super(TriggeringDataset, self).__init__(**processed_kwargs)


class Trigger(troposphere.iotanalytics.Trigger, Mixin):
    def __init__(self,
                 title=None,
                 Schedule=NOTHING, # type: _Schedule
                 TriggeringDataset=NOTHING, # type: _TriggeringDataset
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Schedule=Schedule,
            TriggeringDataset=TriggeringDataset,
            **kwargs
        )
        super(Trigger, self).__init__(**processed_kwargs)


class VersioningConfiguration(troposphere.iotanalytics.VersioningConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MaxVersions=NOTHING, # type: int
                 Unlimited=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxVersions=MaxVersions,
            Unlimited=Unlimited,
            **kwargs
        )
        super(VersioningConfiguration, self).__init__(**processed_kwargs)


class Dataset(troposphere.iotanalytics.Dataset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Actions=REQUIRED, # type: List[_Action]
                 ContentDeliveryRules=NOTHING, # type: List[_DatasetContentDeliveryRule]
                 DatasetName=NOTHING, # type: Union[str, AWSHelperFn]
                 LateDataRules=NOTHING, # type: List[_LateDataRule]
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: _Tags
                 Triggers=NOTHING, # type: List[_Trigger]
                 VersioningConfiguration=NOTHING, # type: _VersioningConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Actions=Actions,
            ContentDeliveryRules=ContentDeliveryRules,
            DatasetName=DatasetName,
            LateDataRules=LateDataRules,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            Triggers=Triggers,
            VersioningConfiguration=VersioningConfiguration,
            **kwargs
        )
        super(Dataset, self).__init__(**processed_kwargs)


class DatastoreStorage(troposphere.iotanalytics.DatastoreStorage, Mixin):
    def __init__(self,
                 title=None,
                 CustomerManagedS3=NOTHING, # type: _CustomerManagedS3
                 ServiceManagedS3=NOTHING, # type: _ServiceManagedS3
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CustomerManagedS3=CustomerManagedS3,
            ServiceManagedS3=ServiceManagedS3,
            **kwargs
        )
        super(DatastoreStorage, self).__init__(**processed_kwargs)


class Column(troposphere.iotanalytics.Column, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            **kwargs
        )
        super(Column, self).__init__(**processed_kwargs)


class SchemaDefinition(troposphere.iotanalytics.SchemaDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Columns=NOTHING, # type: List[_Column]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Columns=Columns,
            **kwargs
        )
        super(SchemaDefinition, self).__init__(**processed_kwargs)


class ParquetConfiguration(troposphere.iotanalytics.ParquetConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SchemaDefinition=NOTHING, # type: _SchemaDefinition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SchemaDefinition=SchemaDefinition,
            **kwargs
        )
        super(ParquetConfiguration, self).__init__(**processed_kwargs)


class FileFormatConfiguration(troposphere.iotanalytics.FileFormatConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 JsonConfiguration=NOTHING, # type: dict
                 ParquetConfiguration=NOTHING, # type: _ParquetConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JsonConfiguration=JsonConfiguration,
            ParquetConfiguration=ParquetConfiguration,
            **kwargs
        )
        super(FileFormatConfiguration, self).__init__(**processed_kwargs)


class Datastore(troposphere.iotanalytics.Datastore, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatastoreName=NOTHING, # type: Union[str, AWSHelperFn]
                 DatastoreStorage=NOTHING, # type: _DatastoreStorage
                 FileFormatConfiguration=NOTHING, # type: _FileFormatConfiguration
                 RetentionPeriod=NOTHING, # type: _RetentionPeriod
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatastoreName=DatastoreName,
            DatastoreStorage=DatastoreStorage,
            FileFormatConfiguration=FileFormatConfiguration,
            RetentionPeriod=RetentionPeriod,
            Tags=Tags,
            **kwargs
        )
        super(Datastore, self).__init__(**processed_kwargs)
