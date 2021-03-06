# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.s3

from troposphere.s3 import (
    AbortIncompleteMultipartUpload as _AbortIncompleteMultipartUpload,
    AccelerateConfiguration as _AccelerateConfiguration,
    AccessControlTranslation as _AccessControlTranslation,
    AccountLevel as _AccountLevel,
    ActivityMetrics as _ActivityMetrics,
    AnalyticsConfiguration as _AnalyticsConfiguration,
    AwsOrg as _AwsOrg,
    BucketEncryption as _BucketEncryption,
    BucketLevel as _BucketLevel,
    BucketsAndRegions as _BucketsAndRegions,
    CorsConfiguration as _CorsConfiguration,
    CorsRules as _CorsRules,
    DataExport as _DataExport,
    DefaultRetention as _DefaultRetention,
    DeleteMarkerReplication as _DeleteMarkerReplication,
    Destination as _Destination,
    EncryptionConfiguration as _EncryptionConfiguration,
    Filter as _Filter,
    InventoryConfiguration as _InventoryConfiguration,
    LambdaConfigurations as _LambdaConfigurations,
    LifecycleConfiguration as _LifecycleConfiguration,
    LifecycleRule as _LifecycleRule,
    LifecycleRuleTransition as _LifecycleRuleTransition,
    LoggingConfiguration as _LoggingConfiguration,
    Metrics as _Metrics,
    MetricsConfiguration as _MetricsConfiguration,
    NoncurrentVersionTransition as _NoncurrentVersionTransition,
    NotificationConfiguration as _NotificationConfiguration,
    ObjectLockConfiguration as _ObjectLockConfiguration,
    ObjectLockRule as _ObjectLockRule,
    OwnershipControls as _OwnershipControls,
    OwnershipControlsRule as _OwnershipControlsRule,
    PrefixLevel as _PrefixLevel,
    PrefixLevelStorageMetrics as _PrefixLevelStorageMetrics,
    PublicAccessBlockConfiguration as _PublicAccessBlockConfiguration,
    QueueConfigurations as _QueueConfigurations,
    RedirectAllRequestsTo as _RedirectAllRequestsTo,
    RedirectRule as _RedirectRule,
    ReplicaModifications as _ReplicaModifications,
    ReplicationConfiguration as _ReplicationConfiguration,
    ReplicationConfigurationRules as _ReplicationConfigurationRules,
    ReplicationConfigurationRulesDestination as _ReplicationConfigurationRulesDestination,
    ReplicationRuleAndOperator as _ReplicationRuleAndOperator,
    ReplicationRuleFilter as _ReplicationRuleFilter,
    ReplicationTime as _ReplicationTime,
    ReplicationTimeValue as _ReplicationTimeValue,
    RoutingRule as _RoutingRule,
    RoutingRuleCondition as _RoutingRuleCondition,
    Rules as _Rules,
    S3Key as _S3Key,
    SelectionCriteria as _SelectionCriteria,
    ServerSideEncryptionByDefault as _ServerSideEncryptionByDefault,
    ServerSideEncryptionRule as _ServerSideEncryptionRule,
    SourceSelectionCriteria as _SourceSelectionCriteria,
    SseKmsEncryptedObjects as _SseKmsEncryptedObjects,
    StorageClassAnalysis as _StorageClassAnalysis,
    StorageLensConfiguration as _StorageLensConfiguration,
    TagFilter as _TagFilter,
    Tags as _Tags,
    TopicConfigurations as _TopicConfigurations,
    VersioningConfiguration as _VersioningConfiguration,
    VpcConfiguration as _VpcConfiguration,
    WebsiteConfiguration as _WebsiteConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class PublicAccessBlockConfiguration(troposphere.s3.PublicAccessBlockConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BlockPublicAcls=NOTHING, # type: bool
                 BlockPublicPolicy=NOTHING, # type: bool
                 IgnorePublicAcls=NOTHING, # type: bool
                 RestrictPublicBuckets=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BlockPublicAcls=BlockPublicAcls,
            BlockPublicPolicy=BlockPublicPolicy,
            IgnorePublicAcls=IgnorePublicAcls,
            RestrictPublicBuckets=RestrictPublicBuckets,
            **kwargs
        )
        super(PublicAccessBlockConfiguration, self).__init__(**processed_kwargs)


class VpcConfiguration(troposphere.s3.VpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VpcId=VpcId,
            **kwargs
        )
        super(VpcConfiguration, self).__init__(**processed_kwargs)


class AccessPoint(troposphere.s3.AccessPoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 CreationDate=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NetworkOrigin=NOTHING, # type: Union[str, AWSHelperFn]
                 Policy=NOTHING, # type: dict
                 PolicyStatus=NOTHING, # type: dict
                 PublicAccessBlockConfiguration=NOTHING, # type: _PublicAccessBlockConfiguration
                 VpcConfiguration=NOTHING, # type: _VpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bucket=Bucket,
            CreationDate=CreationDate,
            Name=Name,
            NetworkOrigin=NetworkOrigin,
            Policy=Policy,
            PolicyStatus=PolicyStatus,
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration,
            VpcConfiguration=VpcConfiguration,
            **kwargs
        )
        super(AccessPoint, self).__init__(**processed_kwargs)


class CorsRules(troposphere.s3.CorsRules, Mixin):
    def __init__(self,
                 title=None,
                 AllowedMethods=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AllowedOrigins=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 AllowedHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ExposedHeaders=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxAge=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowedMethods=AllowedMethods,
            AllowedOrigins=AllowedOrigins,
            AllowedHeaders=AllowedHeaders,
            ExposedHeaders=ExposedHeaders,
            Id=Id,
            MaxAge=MaxAge,
            **kwargs
        )
        super(CorsRules, self).__init__(**processed_kwargs)


class CorsConfiguration(troposphere.s3.CorsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CorsRules=REQUIRED, # type: List[_CorsRules]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CorsRules=CorsRules,
            **kwargs
        )
        super(CorsConfiguration, self).__init__(**processed_kwargs)


class VersioningConfiguration(troposphere.s3.VersioningConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            **kwargs
        )
        super(VersioningConfiguration, self).__init__(**processed_kwargs)


class AccelerateConfiguration(troposphere.s3.AccelerateConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AccelerationStatus=REQUIRED, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccelerationStatus=AccelerationStatus,
            **kwargs
        )
        super(AccelerateConfiguration, self).__init__(**processed_kwargs)


class RedirectAllRequestsTo(troposphere.s3.RedirectAllRequestsTo, Mixin):
    def __init__(self,
                 title=None,
                 HostName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HostName=HostName,
            Protocol=Protocol,
            **kwargs
        )
        super(RedirectAllRequestsTo, self).__init__(**processed_kwargs)


class RedirectRule(troposphere.s3.RedirectRule, Mixin):
    def __init__(self,
                 title=None,
                 HostName=NOTHING, # type: Union[str, AWSHelperFn]
                 HttpRedirectCode=NOTHING, # type: Union[str, AWSHelperFn]
                 Protocol=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplaceKeyPrefixWith=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplaceKeyWith=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HostName=HostName,
            HttpRedirectCode=HttpRedirectCode,
            Protocol=Protocol,
            ReplaceKeyPrefixWith=ReplaceKeyPrefixWith,
            ReplaceKeyWith=ReplaceKeyWith,
            **kwargs
        )
        super(RedirectRule, self).__init__(**processed_kwargs)


class RoutingRuleCondition(troposphere.s3.RoutingRuleCondition, Mixin):
    def __init__(self,
                 title=None,
                 HttpErrorCodeReturnedEquals=NOTHING, # type: Union[str, AWSHelperFn]
                 KeyPrefixEquals=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HttpErrorCodeReturnedEquals=HttpErrorCodeReturnedEquals,
            KeyPrefixEquals=KeyPrefixEquals,
            **kwargs
        )
        super(RoutingRuleCondition, self).__init__(**processed_kwargs)


class RoutingRule(troposphere.s3.RoutingRule, Mixin):
    def __init__(self,
                 title=None,
                 RedirectRule=REQUIRED, # type: _RedirectRule
                 RoutingRuleCondition=NOTHING, # type: _RoutingRuleCondition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RedirectRule=RedirectRule,
            RoutingRuleCondition=RoutingRuleCondition,
            **kwargs
        )
        super(RoutingRule, self).__init__(**processed_kwargs)


class WebsiteConfiguration(troposphere.s3.WebsiteConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 IndexDocument=NOTHING, # type: Union[str, AWSHelperFn]
                 ErrorDocument=NOTHING, # type: Union[str, AWSHelperFn]
                 RedirectAllRequestsTo=NOTHING, # type: _RedirectAllRequestsTo
                 RoutingRules=NOTHING, # type: List[_RoutingRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IndexDocument=IndexDocument,
            ErrorDocument=ErrorDocument,
            RedirectAllRequestsTo=RedirectAllRequestsTo,
            RoutingRules=RoutingRules,
            **kwargs
        )
        super(WebsiteConfiguration, self).__init__(**processed_kwargs)


class LifecycleRuleTransition(troposphere.s3.LifecycleRuleTransition, Mixin):
    def __init__(self,
                 title=None,
                 StorageClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransitionDate=NOTHING, # type: Union[str, AWSHelperFn]
                 TransitionInDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StorageClass=StorageClass,
            TransitionDate=TransitionDate,
            TransitionInDays=TransitionInDays,
            **kwargs
        )
        super(LifecycleRuleTransition, self).__init__(**processed_kwargs)


class AbortIncompleteMultipartUpload(troposphere.s3.AbortIncompleteMultipartUpload, Mixin):
    def __init__(self,
                 title=None,
                 DaysAfterInitiation=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DaysAfterInitiation=DaysAfterInitiation,
            **kwargs
        )
        super(AbortIncompleteMultipartUpload, self).__init__(**processed_kwargs)


class NoncurrentVersionTransition(troposphere.s3.NoncurrentVersionTransition, Mixin):
    def __init__(self,
                 title=None,
                 StorageClass=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransitionInDays=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StorageClass=StorageClass,
            TransitionInDays=TransitionInDays,
            **kwargs
        )
        super(NoncurrentVersionTransition, self).__init__(**processed_kwargs)


class TagFilter(troposphere.s3.TagFilter, Mixin):
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
        super(TagFilter, self).__init__(**processed_kwargs)


class LifecycleRule(troposphere.s3.LifecycleRule, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 AbortIncompleteMultipartUpload=NOTHING, # type: _AbortIncompleteMultipartUpload
                 ExpirationDate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExpirationInDays=NOTHING, # type: int
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 NoncurrentVersionExpirationInDays=NOTHING, # type: int
                 NoncurrentVersionTransition=NOTHING, # type: _NoncurrentVersionTransition
                 NoncurrentVersionTransitions=NOTHING, # type: List[_NoncurrentVersionTransition]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 Transition=NOTHING, # type: _LifecycleRuleTransition
                 Transitions=NOTHING, # type: List[_LifecycleRuleTransition]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            AbortIncompleteMultipartUpload=AbortIncompleteMultipartUpload,
            ExpirationDate=ExpirationDate,
            ExpirationInDays=ExpirationInDays,
            Id=Id,
            NoncurrentVersionExpirationInDays=NoncurrentVersionExpirationInDays,
            NoncurrentVersionTransition=NoncurrentVersionTransition,
            NoncurrentVersionTransitions=NoncurrentVersionTransitions,
            Prefix=Prefix,
            TagFilters=TagFilters,
            Transition=Transition,
            Transitions=Transitions,
            **kwargs
        )
        super(LifecycleRule, self).__init__(**processed_kwargs)


class LifecycleConfiguration(troposphere.s3.LifecycleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_LifecycleRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(LifecycleConfiguration, self).__init__(**processed_kwargs)


class LoggingConfiguration(troposphere.s3.LoggingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DestinationBucketName=NOTHING, # type: str
                 LogFilePrefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationBucketName=DestinationBucketName,
            LogFilePrefix=LogFilePrefix,
            **kwargs
        )
        super(LoggingConfiguration, self).__init__(**processed_kwargs)


class Rules(troposphere.s3.Rules, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(Rules, self).__init__(**processed_kwargs)


class S3Key(troposphere.s3.S3Key, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_Rules]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(S3Key, self).__init__(**processed_kwargs)


class Filter(troposphere.s3.Filter, Mixin):
    def __init__(self,
                 title=None,
                 S3Key=REQUIRED, # type: _S3Key
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Key=S3Key,
            **kwargs
        )
        super(Filter, self).__init__(**processed_kwargs)


class LambdaConfigurations(troposphere.s3.LambdaConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 Event=REQUIRED, # type: Union[str, AWSHelperFn]
                 Function=REQUIRED, # type: Union[str, AWSHelperFn]
                 Filter=NOTHING, # type: _Filter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Event=Event,
            Function=Function,
            Filter=Filter,
            **kwargs
        )
        super(LambdaConfigurations, self).__init__(**processed_kwargs)


class QueueConfigurations(troposphere.s3.QueueConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 Event=REQUIRED, # type: Union[str, AWSHelperFn]
                 Queue=REQUIRED, # type: Union[str, AWSHelperFn]
                 Filter=NOTHING, # type: _Filter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Event=Event,
            Queue=Queue,
            Filter=Filter,
            **kwargs
        )
        super(QueueConfigurations, self).__init__(**processed_kwargs)


class TopicConfigurations(troposphere.s3.TopicConfigurations, Mixin):
    def __init__(self,
                 title=None,
                 Event=REQUIRED, # type: Union[str, AWSHelperFn]
                 Topic=REQUIRED, # type: Union[str, AWSHelperFn]
                 Filter=NOTHING, # type: _Filter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Event=Event,
            Topic=Topic,
            Filter=Filter,
            **kwargs
        )
        super(TopicConfigurations, self).__init__(**processed_kwargs)


class MetricsConfiguration(troposphere.s3.MetricsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            Prefix=Prefix,
            TagFilters=TagFilters,
            **kwargs
        )
        super(MetricsConfiguration, self).__init__(**processed_kwargs)


class NotificationConfiguration(troposphere.s3.NotificationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 LambdaConfigurations=NOTHING, # type: List[_LambdaConfigurations]
                 QueueConfigurations=NOTHING, # type: List[_QueueConfigurations]
                 TopicConfigurations=NOTHING, # type: List[_TopicConfigurations]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LambdaConfigurations=LambdaConfigurations,
            QueueConfigurations=QueueConfigurations,
            TopicConfigurations=TopicConfigurations,
            **kwargs
        )
        super(NotificationConfiguration, self).__init__(**processed_kwargs)


class OwnershipControlsRule(troposphere.s3.OwnershipControlsRule, Mixin):
    def __init__(self,
                 title=None,
                 ObjectOwnership=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ObjectOwnership=ObjectOwnership,
            **kwargs
        )
        super(OwnershipControlsRule, self).__init__(**processed_kwargs)


class OwnershipControls(troposphere.s3.OwnershipControls, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_OwnershipControlsRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(OwnershipControls, self).__init__(**processed_kwargs)


class DeleteMarkerReplication(troposphere.s3.DeleteMarkerReplication, Mixin):
    def __init__(self,
                 title=None,
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            **kwargs
        )
        super(DeleteMarkerReplication, self).__init__(**processed_kwargs)


class AccessControlTranslation(troposphere.s3.AccessControlTranslation, Mixin):
    def __init__(self,
                 title=None,
                 Owner=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Owner=Owner,
            **kwargs
        )
        super(AccessControlTranslation, self).__init__(**processed_kwargs)


class EncryptionConfiguration(troposphere.s3.EncryptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ReplicaKmsKeyID=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReplicaKmsKeyID=ReplicaKmsKeyID,
            **kwargs
        )
        super(EncryptionConfiguration, self).__init__(**processed_kwargs)


class ReplicationTimeValue(troposphere.s3.ReplicationTimeValue, Mixin):
    def __init__(self,
                 title=None,
                 Minutes=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Minutes=Minutes,
            **kwargs
        )
        super(ReplicationTimeValue, self).__init__(**processed_kwargs)


class Metrics(troposphere.s3.Metrics, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 EventThreshold=NOTHING, # type: _ReplicationTimeValue
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            EventThreshold=EventThreshold,
            **kwargs
        )
        super(Metrics, self).__init__(**processed_kwargs)


class ReplicationTime(troposphere.s3.ReplicationTime, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 Time=REQUIRED, # type: _ReplicationTimeValue
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            Time=Time,
            **kwargs
        )
        super(ReplicationTime, self).__init__(**processed_kwargs)


class ReplicationConfigurationRulesDestination(troposphere.s3.ReplicationConfigurationRulesDestination, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessControlTranslation=NOTHING, # type: _AccessControlTranslation
                 Account=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionConfiguration=NOTHING, # type: _EncryptionConfiguration
                 Metrics=NOTHING, # type: _Metrics
                 ReplicationTime=NOTHING, # type: _ReplicationTime
                 StorageClass=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            AccessControlTranslation=AccessControlTranslation,
            Account=Account,
            EncryptionConfiguration=EncryptionConfiguration,
            Metrics=Metrics,
            ReplicationTime=ReplicationTime,
            StorageClass=StorageClass,
            **kwargs
        )
        super(ReplicationConfigurationRulesDestination, self).__init__(**processed_kwargs)


class ReplicationRuleAndOperator(troposphere.s3.ReplicationRuleAndOperator, Mixin):
    def __init__(self,
                 title=None,
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prefix=Prefix,
            TagFilters=TagFilters,
            **kwargs
        )
        super(ReplicationRuleAndOperator, self).__init__(**processed_kwargs)


class ReplicationRuleFilter(troposphere.s3.ReplicationRuleFilter, Mixin):
    def __init__(self,
                 title=None,
                 And=NOTHING, # type: _ReplicationRuleAndOperator
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilter=NOTHING, # type: _TagFilter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            And=And,
            Prefix=Prefix,
            TagFilter=TagFilter,
            **kwargs
        )
        super(ReplicationRuleFilter, self).__init__(**processed_kwargs)


class ReplicaModifications(troposphere.s3.ReplicaModifications, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            **kwargs
        )
        super(ReplicaModifications, self).__init__(**processed_kwargs)


class SseKmsEncryptedObjects(troposphere.s3.SseKmsEncryptedObjects, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            **kwargs
        )
        super(SseKmsEncryptedObjects, self).__init__(**processed_kwargs)


class SourceSelectionCriteria(troposphere.s3.SourceSelectionCriteria, Mixin):
    def __init__(self,
                 title=None,
                 ReplicaModifications=NOTHING, # type: _ReplicaModifications
                 SseKmsEncryptedObjects=NOTHING, # type: _SseKmsEncryptedObjects
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReplicaModifications=ReplicaModifications,
            SseKmsEncryptedObjects=SseKmsEncryptedObjects,
            **kwargs
        )
        super(SourceSelectionCriteria, self).__init__(**processed_kwargs)


class ReplicationConfigurationRules(troposphere.s3.ReplicationConfigurationRules, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: _ReplicationConfigurationRulesDestination
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 Status=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeleteMarkerReplication=NOTHING, # type: _DeleteMarkerReplication
                 Filter=NOTHING, # type: _ReplicationRuleFilter
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 Priority=NOTHING, # type: int
                 SourceSelectionCriteria=NOTHING, # type: _SourceSelectionCriteria
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            Prefix=Prefix,
            Status=Status,
            DeleteMarkerReplication=DeleteMarkerReplication,
            Filter=Filter,
            Id=Id,
            Priority=Priority,
            SourceSelectionCriteria=SourceSelectionCriteria,
            **kwargs
        )
        super(ReplicationConfigurationRules, self).__init__(**processed_kwargs)


class ReplicationConfiguration(troposphere.s3.ReplicationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Role=REQUIRED, # type: Union[str, AWSHelperFn]
                 Rules=REQUIRED, # type: List[_ReplicationConfigurationRules]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Role=Role,
            Rules=Rules,
            **kwargs
        )
        super(ReplicationConfiguration, self).__init__(**processed_kwargs)


class Destination(troposphere.s3.Destination, Mixin):
    def __init__(self,
                 title=None,
                 BucketArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Format=REQUIRED, # type: Union[str, AWSHelperFn]
                 BucketAccountId=NOTHING, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketArn=BucketArn,
            Format=Format,
            BucketAccountId=BucketAccountId,
            Prefix=Prefix,
            **kwargs
        )
        super(Destination, self).__init__(**processed_kwargs)


class DataExport(troposphere.s3.DataExport, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: _Destination
                 OutputSchemaVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            OutputSchemaVersion=OutputSchemaVersion,
            **kwargs
        )
        super(DataExport, self).__init__(**processed_kwargs)


class StorageClassAnalysis(troposphere.s3.StorageClassAnalysis, Mixin):
    def __init__(self,
                 title=None,
                 DataExport=NOTHING, # type: _DataExport
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataExport=DataExport,
            **kwargs
        )
        super(StorageClassAnalysis, self).__init__(**processed_kwargs)


class AnalyticsConfiguration(troposphere.s3.AnalyticsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 StorageClassAnalysis=REQUIRED, # type: _StorageClassAnalysis
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Id=Id,
            StorageClassAnalysis=StorageClassAnalysis,
            Prefix=Prefix,
            TagFilters=TagFilters,
            **kwargs
        )
        super(AnalyticsConfiguration, self).__init__(**processed_kwargs)


class ServerSideEncryptionByDefault(troposphere.s3.ServerSideEncryptionByDefault, Mixin):
    def __init__(self,
                 title=None,
                 SSEAlgorithm=REQUIRED, # type: Union[str, AWSHelperFn]
                 KMSMasterKeyID=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SSEAlgorithm=SSEAlgorithm,
            KMSMasterKeyID=KMSMasterKeyID,
            **kwargs
        )
        super(ServerSideEncryptionByDefault, self).__init__(**processed_kwargs)


class ServerSideEncryptionRule(troposphere.s3.ServerSideEncryptionRule, Mixin):
    def __init__(self,
                 title=None,
                 BucketKeyEnabled=NOTHING, # type: bool
                 ServerSideEncryptionByDefault=NOTHING, # type: _ServerSideEncryptionByDefault
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketKeyEnabled=BucketKeyEnabled,
            ServerSideEncryptionByDefault=ServerSideEncryptionByDefault,
            **kwargs
        )
        super(ServerSideEncryptionRule, self).__init__(**processed_kwargs)


class BucketEncryption(troposphere.s3.BucketEncryption, Mixin):
    def __init__(self,
                 title=None,
                 ServerSideEncryptionConfiguration=REQUIRED, # type: List[_ServerSideEncryptionRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServerSideEncryptionConfiguration=ServerSideEncryptionConfiguration,
            **kwargs
        )
        super(BucketEncryption, self).__init__(**processed_kwargs)


class InventoryConfiguration(troposphere.s3.InventoryConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: _Destination
                 Enabled=REQUIRED, # type: bool
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 IncludedObjectVersions=REQUIRED, # type: Union[str, AWSHelperFn]
                 OptionalFields=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ScheduleFrequency=REQUIRED, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            Enabled=Enabled,
            Id=Id,
            IncludedObjectVersions=IncludedObjectVersions,
            OptionalFields=OptionalFields,
            ScheduleFrequency=ScheduleFrequency,
            Prefix=Prefix,
            **kwargs
        )
        super(InventoryConfiguration, self).__init__(**processed_kwargs)


class DefaultRetention(troposphere.s3.DefaultRetention, Mixin):
    def __init__(self,
                 title=None,
                 Days=NOTHING, # type: int
                 Mode=NOTHING, # type: Union[str, AWSHelperFn]
                 Years=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Days=Days,
            Mode=Mode,
            Years=Years,
            **kwargs
        )
        super(DefaultRetention, self).__init__(**processed_kwargs)


class ObjectLockRule(troposphere.s3.ObjectLockRule, Mixin):
    def __init__(self,
                 title=None,
                 DefaultRetention=NOTHING, # type: _DefaultRetention
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultRetention=DefaultRetention,
            **kwargs
        )
        super(ObjectLockRule, self).__init__(**processed_kwargs)


class ObjectLockConfiguration(troposphere.s3.ObjectLockConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ObjectLockEnabled=NOTHING, # type: Union[str, AWSHelperFn]
                 Rule=NOTHING, # type: _ObjectLockRule
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ObjectLockEnabled=ObjectLockEnabled,
            Rule=Rule,
            **kwargs
        )
        super(ObjectLockConfiguration, self).__init__(**processed_kwargs)


class Bucket(troposphere.s3.Bucket, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccelerateConfiguration=NOTHING, # type: _AccelerateConfiguration
                 AccessControl=NOTHING, # type: Union[str, AWSHelperFn]
                 AnalyticsConfigurations=NOTHING, # type: List[_AnalyticsConfiguration]
                 BucketEncryption=NOTHING, # type: _BucketEncryption
                 BucketName=NOTHING, # type: str
                 CorsConfiguration=NOTHING, # type: _CorsConfiguration
                 InventoryConfigurations=NOTHING, # type: List[_InventoryConfiguration]
                 LifecycleConfiguration=NOTHING, # type: _LifecycleConfiguration
                 LoggingConfiguration=NOTHING, # type: _LoggingConfiguration
                 MetricsConfigurations=NOTHING, # type: List[_MetricsConfiguration]
                 NotificationConfiguration=NOTHING, # type: _NotificationConfiguration
                 ObjectLockConfiguration=NOTHING, # type: _ObjectLockConfiguration
                 ObjectLockEnabled=NOTHING, # type: bool
                 OwnershipControls=NOTHING, # type: _OwnershipControls
                 PublicAccessBlockConfiguration=NOTHING, # type: _PublicAccessBlockConfiguration
                 ReplicationConfiguration=NOTHING, # type: _ReplicationConfiguration
                 Tags=NOTHING, # type: _Tags
                 VersioningConfiguration=NOTHING, # type: _VersioningConfiguration
                 WebsiteConfiguration=NOTHING, # type: _WebsiteConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccelerateConfiguration=AccelerateConfiguration,
            AccessControl=AccessControl,
            AnalyticsConfigurations=AnalyticsConfigurations,
            BucketEncryption=BucketEncryption,
            BucketName=BucketName,
            CorsConfiguration=CorsConfiguration,
            InventoryConfigurations=InventoryConfigurations,
            LifecycleConfiguration=LifecycleConfiguration,
            LoggingConfiguration=LoggingConfiguration,
            MetricsConfigurations=MetricsConfigurations,
            NotificationConfiguration=NotificationConfiguration,
            ObjectLockConfiguration=ObjectLockConfiguration,
            ObjectLockEnabled=ObjectLockEnabled,
            OwnershipControls=OwnershipControls,
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration,
            ReplicationConfiguration=ReplicationConfiguration,
            Tags=Tags,
            VersioningConfiguration=VersioningConfiguration,
            WebsiteConfiguration=WebsiteConfiguration,
            **kwargs
        )
        super(Bucket, self).__init__(**processed_kwargs)


class BucketPolicy(troposphere.s3.BucketPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyDocument=REQUIRED, # type: Union[dict]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bucket=Bucket,
            PolicyDocument=PolicyDocument,
            **kwargs
        )
        super(BucketPolicy, self).__init__(**processed_kwargs)


class ActivityMetrics(troposphere.s3.ActivityMetrics, Mixin):
    def __init__(self,
                 title=None,
                 IsEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IsEnabled=IsEnabled,
            **kwargs
        )
        super(ActivityMetrics, self).__init__(**processed_kwargs)


class SelectionCriteria(troposphere.s3.SelectionCriteria, Mixin):
    def __init__(self,
                 title=None,
                 Delimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxDepth=NOTHING, # type: int
                 MinStorageBytesPercentage=NOTHING, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Delimiter=Delimiter,
            MaxDepth=MaxDepth,
            MinStorageBytesPercentage=MinStorageBytesPercentage,
            **kwargs
        )
        super(SelectionCriteria, self).__init__(**processed_kwargs)


class PrefixLevelStorageMetrics(troposphere.s3.PrefixLevelStorageMetrics, Mixin):
    def __init__(self,
                 title=None,
                 IsEnabled=NOTHING, # type: bool
                 SelectionCriteria=NOTHING, # type: _SelectionCriteria
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IsEnabled=IsEnabled,
            SelectionCriteria=SelectionCriteria,
            **kwargs
        )
        super(PrefixLevelStorageMetrics, self).__init__(**processed_kwargs)


class PrefixLevel(troposphere.s3.PrefixLevel, Mixin):
    def __init__(self,
                 title=None,
                 StorageMetrics=REQUIRED, # type: _PrefixLevelStorageMetrics
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StorageMetrics=StorageMetrics,
            **kwargs
        )
        super(PrefixLevel, self).__init__(**processed_kwargs)


class BucketLevel(troposphere.s3.BucketLevel, Mixin):
    def __init__(self,
                 title=None,
                 ActivityMetrics=NOTHING, # type: _ActivityMetrics
                 PrefixLevel=NOTHING, # type: _PrefixLevel
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActivityMetrics=ActivityMetrics,
            PrefixLevel=PrefixLevel,
            **kwargs
        )
        super(BucketLevel, self).__init__(**processed_kwargs)


class AccountLevel(troposphere.s3.AccountLevel, Mixin):
    def __init__(self,
                 title=None,
                 BucketLevel=REQUIRED, # type: _BucketLevel
                 ActivityMetrics=NOTHING, # type: _ActivityMetrics
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketLevel=BucketLevel,
            ActivityMetrics=ActivityMetrics,
            **kwargs
        )
        super(AccountLevel, self).__init__(**processed_kwargs)


class AwsOrg(troposphere.s3.AwsOrg, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            **kwargs
        )
        super(AwsOrg, self).__init__(**processed_kwargs)


class BucketsAndRegions(troposphere.s3.BucketsAndRegions, Mixin):
    def __init__(self,
                 title=None,
                 Buckets=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Regions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Buckets=Buckets,
            Regions=Regions,
            **kwargs
        )
        super(BucketsAndRegions, self).__init__(**processed_kwargs)


class StorageLensConfiguration(troposphere.s3.StorageLensConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AccountLevel=REQUIRED, # type: _AccountLevel
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 IsEnabled=REQUIRED, # type: bool
                 AwsOrg=NOTHING, # type: _AwsOrg
                 DataExport=NOTHING, # type: _DataExport
                 Exclude=NOTHING, # type: _BucketsAndRegions
                 Include=NOTHING, # type: _BucketsAndRegions
                 StorageLensArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccountLevel=AccountLevel,
            Id=Id,
            IsEnabled=IsEnabled,
            AwsOrg=AwsOrg,
            DataExport=DataExport,
            Exclude=Exclude,
            Include=Include,
            StorageLensArn=StorageLensArn,
            **kwargs
        )
        super(StorageLensConfiguration, self).__init__(**processed_kwargs)


class StorageLens(troposphere.s3.StorageLens, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StorageLensConfiguration=REQUIRED, # type: _StorageLensConfiguration
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StorageLensConfiguration=StorageLensConfiguration,
            Tags=Tags,
            **kwargs
        )
        super(StorageLens, self).__init__(**processed_kwargs)
