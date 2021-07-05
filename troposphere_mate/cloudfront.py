# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloudfront

from troposphere.cloudfront import (
    CacheBehavior as _CacheBehavior,
    CacheCookiesConfig as _CacheCookiesConfig,
    CacheHeadersConfig as _CacheHeadersConfig,
    CachePolicyConfig as _CachePolicyConfig,
    CacheQueryStringsConfig as _CacheQueryStringsConfig,
    CloudFrontOriginAccessIdentityConfig as _CloudFrontOriginAccessIdentityConfig,
    Cookies as _Cookies,
    CustomErrorResponse as _CustomErrorResponse,
    CustomOriginConfig as _CustomOriginConfig,
    DefaultCacheBehavior as _DefaultCacheBehavior,
    DistributionConfig as _DistributionConfig,
    EndPoint as _EndPoint,
    ForwardedValues as _ForwardedValues,
    GeoRestriction as _GeoRestriction,
    KeyGroupConfig as _KeyGroupConfig,
    KinesisStreamConfig as _KinesisStreamConfig,
    LambdaFunctionAssociation as _LambdaFunctionAssociation,
    Logging as _Logging,
    Origin as _Origin,
    OriginCustomHeader as _OriginCustomHeader,
    OriginGroup as _OriginGroup,
    OriginGroupFailoverCriteria as _OriginGroupFailoverCriteria,
    OriginGroupMember as _OriginGroupMember,
    OriginGroupMembers as _OriginGroupMembers,
    OriginGroups as _OriginGroups,
    OriginRequestCookiesConfig as _OriginRequestCookiesConfig,
    OriginRequestHeadersConfig as _OriginRequestHeadersConfig,
    OriginRequestPolicyConfig as _OriginRequestPolicyConfig,
    OriginRequestQueryStringsConfig as _OriginRequestQueryStringsConfig,
    OriginShield as _OriginShield,
    ParametersInCacheKeyAndForwardedToOrigin as _ParametersInCacheKeyAndForwardedToOrigin,
    PublicKeyConfig as _PublicKeyConfig,
    Restrictions as _Restrictions,
    S3Origin as _S3Origin,
    S3OriginConfig as _S3OriginConfig,
    StatusCodes as _StatusCodes,
    StreamingDistributionConfig as _StreamingDistributionConfig,
    Tags as _Tags,
    TrustedSigners as _TrustedSigners,
    ViewerCertificate as _ViewerCertificate,
    integer as _integer,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Cookies(troposphere.cloudfront.Cookies, Mixin):
    def __init__(self,
                 title=None,
                 Forward=REQUIRED, # type: str
                 WhitelistedNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Forward=Forward,
            WhitelistedNames=WhitelistedNames,
            **kwargs
        )
        super(Cookies, self).__init__(**processed_kwargs)


class ForwardedValues(troposphere.cloudfront.ForwardedValues, Mixin):
    def __init__(self,
                 title=None,
                 QueryString=REQUIRED, # type: bool
                 Cookies=NOTHING, # type: _Cookies
                 Headers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 QueryStringCacheKeys=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryString=QueryString,
            Cookies=Cookies,
            Headers=Headers,
            QueryStringCacheKeys=QueryStringCacheKeys,
            **kwargs
        )
        super(ForwardedValues, self).__init__(**processed_kwargs)


class LambdaFunctionAssociation(troposphere.cloudfront.LambdaFunctionAssociation, Mixin):
    def __init__(self,
                 title=None,
                 EventType=NOTHING, # type: str
                 IncludeBody=NOTHING, # type: bool
                 LambdaFunctionARN=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventType=EventType,
            IncludeBody=IncludeBody,
            LambdaFunctionARN=LambdaFunctionARN,
            **kwargs
        )
        super(LambdaFunctionAssociation, self).__init__(**processed_kwargs)


class CacheBehavior(troposphere.cloudfront.CacheBehavior, Mixin):
    def __init__(self,
                 title=None,
                 PathPattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetOriginId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ViewerProtocolPolicy=REQUIRED, # type: str
                 AllowedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CachePolicyId=NOTHING, # type: Union[str, AWSHelperFn]
                 CachedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Compress=NOTHING, # type: bool
                 DefaultTTL=NOTHING, # type: int
                 FieldLevelEncryptionId=NOTHING, # type: Union[str, AWSHelperFn]
                 ForwardedValues=NOTHING, # type: _ForwardedValues
                 LambdaFunctionAssociations=NOTHING, # type: List[_LambdaFunctionAssociation]
                 MaxTTL=NOTHING, # type: int
                 MinTTL=NOTHING, # type: int
                 OriginRequestPolicyId=NOTHING, # type: Union[str, AWSHelperFn]
                 RealtimeLogConfigArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SmoothStreaming=NOTHING, # type: bool
                 TrustedKeyGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TrustedSigners=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PathPattern=PathPattern,
            TargetOriginId=TargetOriginId,
            ViewerProtocolPolicy=ViewerProtocolPolicy,
            AllowedMethods=AllowedMethods,
            CachePolicyId=CachePolicyId,
            CachedMethods=CachedMethods,
            Compress=Compress,
            DefaultTTL=DefaultTTL,
            FieldLevelEncryptionId=FieldLevelEncryptionId,
            ForwardedValues=ForwardedValues,
            LambdaFunctionAssociations=LambdaFunctionAssociations,
            MaxTTL=MaxTTL,
            MinTTL=MinTTL,
            OriginRequestPolicyId=OriginRequestPolicyId,
            RealtimeLogConfigArn=RealtimeLogConfigArn,
            SmoothStreaming=SmoothStreaming,
            TrustedKeyGroups=TrustedKeyGroups,
            TrustedSigners=TrustedSigners,
            **kwargs
        )
        super(CacheBehavior, self).__init__(**processed_kwargs)


class DefaultCacheBehavior(troposphere.cloudfront.DefaultCacheBehavior, Mixin):
    def __init__(self,
                 title=None,
                 TargetOriginId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ViewerProtocolPolicy=REQUIRED, # type: str
                 AllowedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CachePolicyId=NOTHING, # type: Union[str, AWSHelperFn]
                 CachedMethods=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Compress=NOTHING, # type: bool
                 DefaultTTL=NOTHING, # type: int
                 FieldLevelEncryptionId=NOTHING, # type: Union[str, AWSHelperFn]
                 ForwardedValues=NOTHING, # type: _ForwardedValues
                 LambdaFunctionAssociations=NOTHING, # type: List[_LambdaFunctionAssociation]
                 MaxTTL=NOTHING, # type: int
                 MinTTL=NOTHING, # type: int
                 OriginRequestPolicyId=NOTHING, # type: Union[str, AWSHelperFn]
                 RealtimeLogConfigArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SmoothStreaming=NOTHING, # type: bool
                 TrustedKeyGroups=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TrustedSigners=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TargetOriginId=TargetOriginId,
            ViewerProtocolPolicy=ViewerProtocolPolicy,
            AllowedMethods=AllowedMethods,
            CachePolicyId=CachePolicyId,
            CachedMethods=CachedMethods,
            Compress=Compress,
            DefaultTTL=DefaultTTL,
            FieldLevelEncryptionId=FieldLevelEncryptionId,
            ForwardedValues=ForwardedValues,
            LambdaFunctionAssociations=LambdaFunctionAssociations,
            MaxTTL=MaxTTL,
            MinTTL=MinTTL,
            OriginRequestPolicyId=OriginRequestPolicyId,
            RealtimeLogConfigArn=RealtimeLogConfigArn,
            SmoothStreaming=SmoothStreaming,
            TrustedKeyGroups=TrustedKeyGroups,
            TrustedSigners=TrustedSigners,
            **kwargs
        )
        super(DefaultCacheBehavior, self).__init__(**processed_kwargs)


class S3Origin(troposphere.cloudfront.S3Origin, Mixin):
    def __init__(self,
                 title=None,
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 OriginAccessIdentity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DomainName=DomainName,
            OriginAccessIdentity=OriginAccessIdentity,
            **kwargs
        )
        super(S3Origin, self).__init__(**processed_kwargs)


class CustomOriginConfig(troposphere.cloudfront.CustomOriginConfig, Mixin):
    def __init__(self,
                 title=None,
                 OriginProtocolPolicy=REQUIRED, # type: Union[str, AWSHelperFn]
                 HTTPPort=NOTHING, # type: int
                 HTTPSPort=NOTHING, # type: int
                 OriginKeepaliveTimeout=NOTHING, # type: int
                 OriginReadTimeout=NOTHING, # type: int
                 OriginSSLProtocols=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OriginProtocolPolicy=OriginProtocolPolicy,
            HTTPPort=HTTPPort,
            HTTPSPort=HTTPSPort,
            OriginKeepaliveTimeout=OriginKeepaliveTimeout,
            OriginReadTimeout=OriginReadTimeout,
            OriginSSLProtocols=OriginSSLProtocols,
            **kwargs
        )
        super(CustomOriginConfig, self).__init__(**processed_kwargs)


class OriginCustomHeader(troposphere.cloudfront.OriginCustomHeader, Mixin):
    def __init__(self,
                 title=None,
                 HeaderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HeaderValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderName=HeaderName,
            HeaderValue=HeaderValue,
            **kwargs
        )
        super(OriginCustomHeader, self).__init__(**processed_kwargs)


class S3OriginConfig(troposphere.cloudfront.S3OriginConfig, Mixin):
    def __init__(self,
                 title=None,
                 OriginAccessIdentity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OriginAccessIdentity=OriginAccessIdentity,
            **kwargs
        )
        super(S3OriginConfig, self).__init__(**processed_kwargs)


class OriginShield(troposphere.cloudfront.OriginShield, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 OriginShieldRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            OriginShieldRegion=OriginShieldRegion,
            **kwargs
        )
        super(OriginShield, self).__init__(**processed_kwargs)


class Origin(troposphere.cloudfront.Origin, Mixin):
    def __init__(self,
                 title=None,
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConnectionAttempts=NOTHING, # type: int
                 ConnectionTimeout=NOTHING, # type: int
                 CustomOriginConfig=NOTHING, # type: _CustomOriginConfig
                 OriginCustomHeaders=NOTHING, # type: List[_OriginCustomHeader]
                 OriginPath=NOTHING, # type: Union[str, AWSHelperFn]
                 OriginShield=NOTHING, # type: _OriginShield
                 S3OriginConfig=NOTHING, # type: _S3OriginConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DomainName=DomainName,
            Id=Id,
            ConnectionAttempts=ConnectionAttempts,
            ConnectionTimeout=ConnectionTimeout,
            CustomOriginConfig=CustomOriginConfig,
            OriginCustomHeaders=OriginCustomHeaders,
            OriginPath=OriginPath,
            OriginShield=OriginShield,
            S3OriginConfig=S3OriginConfig,
            **kwargs
        )
        super(Origin, self).__init__(**processed_kwargs)


class Logging(troposphere.cloudfront.Logging, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 IncludeCookies=NOTHING, # type: bool
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            IncludeCookies=IncludeCookies,
            Prefix=Prefix,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class CustomErrorResponse(troposphere.cloudfront.CustomErrorResponse, Mixin):
    def __init__(self,
                 title=None,
                 ErrorCode=REQUIRED, # type: int
                 ErrorCachingMinTTL=NOTHING, # type: int
                 ResponseCode=NOTHING, # type: int
                 ResponsePagePath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ErrorCode=ErrorCode,
            ErrorCachingMinTTL=ErrorCachingMinTTL,
            ResponseCode=ResponseCode,
            ResponsePagePath=ResponsePagePath,
            **kwargs
        )
        super(CustomErrorResponse, self).__init__(**processed_kwargs)


class GeoRestriction(troposphere.cloudfront.GeoRestriction, Mixin):
    def __init__(self,
                 title=None,
                 RestrictionType=REQUIRED, # type: str
                 Locations=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RestrictionType=RestrictionType,
            Locations=Locations,
            **kwargs
        )
        super(GeoRestriction, self).__init__(**processed_kwargs)


class Restrictions(troposphere.cloudfront.Restrictions, Mixin):
    def __init__(self,
                 title=None,
                 GeoRestriction=REQUIRED, # type: _GeoRestriction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GeoRestriction=GeoRestriction,
            **kwargs
        )
        super(Restrictions, self).__init__(**processed_kwargs)


class ViewerCertificate(troposphere.cloudfront.ViewerCertificate, Mixin):
    def __init__(self,
                 title=None,
                 AcmCertificateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CloudFrontDefaultCertificate=NOTHING, # type: bool
                 IamCertificateId=NOTHING, # type: Union[str, AWSHelperFn]
                 MinimumProtocolVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 SslSupportMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AcmCertificateArn=AcmCertificateArn,
            CloudFrontDefaultCertificate=CloudFrontDefaultCertificate,
            IamCertificateId=IamCertificateId,
            MinimumProtocolVersion=MinimumProtocolVersion,
            SslSupportMethod=SslSupportMethod,
            **kwargs
        )
        super(ViewerCertificate, self).__init__(**processed_kwargs)


class StatusCodes(troposphere.cloudfront.StatusCodes, Mixin):
    def __init__(self,
                 title=None,
                 Items=REQUIRED, # type: List[_integer]
                 Quantity=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Items=Items,
            Quantity=Quantity,
            **kwargs
        )
        super(StatusCodes, self).__init__(**processed_kwargs)


class OriginGroupFailoverCriteria(troposphere.cloudfront.OriginGroupFailoverCriteria, Mixin):
    def __init__(self,
                 title=None,
                 StatusCodes=REQUIRED, # type: _StatusCodes
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StatusCodes=StatusCodes,
            **kwargs
        )
        super(OriginGroupFailoverCriteria, self).__init__(**processed_kwargs)


class OriginGroupMember(troposphere.cloudfront.OriginGroupMember, Mixin):
    def __init__(self,
                 title=None,
                 OriginId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OriginId=OriginId,
            **kwargs
        )
        super(OriginGroupMember, self).__init__(**processed_kwargs)


class OriginGroupMembers(troposphere.cloudfront.OriginGroupMembers, Mixin):
    def __init__(self,
                 title=None,
                 Items=NOTHING, # type: List[_OriginGroupMember]
                 Quantity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Items=Items,
            Quantity=Quantity,
            **kwargs
        )
        super(OriginGroupMembers, self).__init__(**processed_kwargs)


class OriginGroup(troposphere.cloudfront.OriginGroup, Mixin):
    def __init__(self,
                 title=None,
                 FailoverCriteria=REQUIRED, # type: _OriginGroupFailoverCriteria
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Members=REQUIRED, # type: _OriginGroupMembers
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FailoverCriteria=FailoverCriteria,
            Id=Id,
            Members=Members,
            **kwargs
        )
        super(OriginGroup, self).__init__(**processed_kwargs)


class OriginGroups(troposphere.cloudfront.OriginGroups, Mixin):
    def __init__(self,
                 title=None,
                 Items=NOTHING, # type: List[_OriginGroup]
                 Quantity=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Items=Items,
            Quantity=Quantity,
            **kwargs
        )
        super(OriginGroups, self).__init__(**processed_kwargs)


class DistributionConfig(troposphere.cloudfront.DistributionConfig, Mixin):
    def __init__(self,
                 title=None,
                 DefaultCacheBehavior=REQUIRED, # type: _DefaultCacheBehavior
                 Enabled=REQUIRED, # type: bool
                 Origins=REQUIRED, # type: List[_Origin]
                 Aliases=NOTHING, # type: list
                 CacheBehaviors=NOTHING, # type: List[_CacheBehavior]
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomErrorResponses=NOTHING, # type: List[_CustomErrorResponse]
                 DefaultRootObject=NOTHING, # type: Union[str, AWSHelperFn]
                 HttpVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 IPV6Enabled=NOTHING, # type: bool
                 Logging=NOTHING, # type: _Logging
                 OriginGroups=NOTHING, # type: _OriginGroups
                 PriceClass=NOTHING, # type: str
                 Restrictions=NOTHING, # type: _Restrictions
                 ViewerCertificate=NOTHING, # type: _ViewerCertificate
                 WebACLId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultCacheBehavior=DefaultCacheBehavior,
            Enabled=Enabled,
            Origins=Origins,
            Aliases=Aliases,
            CacheBehaviors=CacheBehaviors,
            Comment=Comment,
            CustomErrorResponses=CustomErrorResponses,
            DefaultRootObject=DefaultRootObject,
            HttpVersion=HttpVersion,
            IPV6Enabled=IPV6Enabled,
            Logging=Logging,
            OriginGroups=OriginGroups,
            PriceClass=PriceClass,
            Restrictions=Restrictions,
            ViewerCertificate=ViewerCertificate,
            WebACLId=WebACLId,
            **kwargs
        )
        super(DistributionConfig, self).__init__(**processed_kwargs)


class Distribution(troposphere.cloudfront.Distribution, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DistributionConfig=REQUIRED, # type: _DistributionConfig
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DistributionConfig=DistributionConfig,
            Tags=Tags,
            **kwargs
        )
        super(Distribution, self).__init__(**processed_kwargs)


class CloudFrontOriginAccessIdentityConfig(troposphere.cloudfront.CloudFrontOriginAccessIdentityConfig, Mixin):
    def __init__(self,
                 title=None,
                 Comment=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            **kwargs
        )
        super(CloudFrontOriginAccessIdentityConfig, self).__init__(**processed_kwargs)


class CloudFrontOriginAccessIdentity(troposphere.cloudfront.CloudFrontOriginAccessIdentity, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CloudFrontOriginAccessIdentityConfig=REQUIRED, # type: _CloudFrontOriginAccessIdentityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig,
            **kwargs
        )
        super(CloudFrontOriginAccessIdentity, self).__init__(**processed_kwargs)


class TrustedSigners(troposphere.cloudfront.TrustedSigners, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=REQUIRED, # type: bool
                 AwsAccountNumbers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            AwsAccountNumbers=AwsAccountNumbers,
            **kwargs
        )
        super(TrustedSigners, self).__init__(**processed_kwargs)


class StreamingDistributionConfig(troposphere.cloudfront.StreamingDistributionConfig, Mixin):
    def __init__(self,
                 title=None,
                 Comment=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 S3Origin=REQUIRED, # type: _S3Origin
                 TrustedSigners=REQUIRED, # type: _TrustedSigners
                 Aliases=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Logging=NOTHING, # type: _Logging
                 PriceClass=NOTHING, # type: str
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Comment=Comment,
            Enabled=Enabled,
            S3Origin=S3Origin,
            TrustedSigners=TrustedSigners,
            Aliases=Aliases,
            Logging=Logging,
            PriceClass=PriceClass,
            **kwargs
        )
        super(StreamingDistributionConfig, self).__init__(**processed_kwargs)


class StreamingDistribution(troposphere.cloudfront.StreamingDistribution, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 StreamingDistributionConfig=REQUIRED, # type: _StreamingDistributionConfig
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            StreamingDistributionConfig=StreamingDistributionConfig,
            Tags=Tags,
            **kwargs
        )
        super(StreamingDistribution, self).__init__(**processed_kwargs)


class CacheCookiesConfig(troposphere.cloudfront.CacheCookiesConfig, Mixin):
    def __init__(self,
                 title=None,
                 CookieBehavior=REQUIRED, # type: Any
                 Cookies=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookieBehavior=CookieBehavior,
            Cookies=Cookies,
            **kwargs
        )
        super(CacheCookiesConfig, self).__init__(**processed_kwargs)


class CacheHeadersConfig(troposphere.cloudfront.CacheHeadersConfig, Mixin):
    def __init__(self,
                 title=None,
                 HeaderBehavior=REQUIRED, # type: Any
                 Headers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderBehavior=HeaderBehavior,
            Headers=Headers,
            **kwargs
        )
        super(CacheHeadersConfig, self).__init__(**processed_kwargs)


class CacheQueryStringsConfig(troposphere.cloudfront.CacheQueryStringsConfig, Mixin):
    def __init__(self,
                 title=None,
                 QueryStringBehavior=REQUIRED, # type: Any
                 QueryStrings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryStringBehavior=QueryStringBehavior,
            QueryStrings=QueryStrings,
            **kwargs
        )
        super(CacheQueryStringsConfig, self).__init__(**processed_kwargs)


class ParametersInCacheKeyAndForwardedToOrigin(troposphere.cloudfront.ParametersInCacheKeyAndForwardedToOrigin, Mixin):
    def __init__(self,
                 title=None,
                 CookiesConfig=REQUIRED, # type: _CacheCookiesConfig
                 EnableAcceptEncodingGzip=REQUIRED, # type: bool
                 HeadersConfig=REQUIRED, # type: _CacheHeadersConfig
                 QueryStringsConfig=REQUIRED, # type: _CacheQueryStringsConfig
                 EnableAcceptEncodingBrotli=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookiesConfig=CookiesConfig,
            EnableAcceptEncodingGzip=EnableAcceptEncodingGzip,
            HeadersConfig=HeadersConfig,
            QueryStringsConfig=QueryStringsConfig,
            EnableAcceptEncodingBrotli=EnableAcceptEncodingBrotli,
            **kwargs
        )
        super(ParametersInCacheKeyAndForwardedToOrigin, self).__init__(**processed_kwargs)


class CachePolicyConfig(troposphere.cloudfront.CachePolicyConfig, Mixin):
    def __init__(self,
                 title=None,
                 DefaultTTL=REQUIRED, # type: int
                 MaxTTL=REQUIRED, # type: int
                 MinTTL=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParametersInCacheKeyAndForwardedToOrigin=REQUIRED, # type: _ParametersInCacheKeyAndForwardedToOrigin
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultTTL=DefaultTTL,
            MaxTTL=MaxTTL,
            MinTTL=MinTTL,
            Name=Name,
            ParametersInCacheKeyAndForwardedToOrigin=ParametersInCacheKeyAndForwardedToOrigin,
            Comment=Comment,
            **kwargs
        )
        super(CachePolicyConfig, self).__init__(**processed_kwargs)


class CachePolicy(troposphere.cloudfront.CachePolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CachePolicyConfig=REQUIRED, # type: _CachePolicyConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CachePolicyConfig=CachePolicyConfig,
            **kwargs
        )
        super(CachePolicy, self).__init__(**processed_kwargs)


class OriginRequestCookiesConfig(troposphere.cloudfront.OriginRequestCookiesConfig, Mixin):
    def __init__(self,
                 title=None,
                 CookieBehavior=REQUIRED, # type: Any
                 Cookies=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookieBehavior=CookieBehavior,
            Cookies=Cookies,
            **kwargs
        )
        super(OriginRequestCookiesConfig, self).__init__(**processed_kwargs)


class OriginRequestHeadersConfig(troposphere.cloudfront.OriginRequestHeadersConfig, Mixin):
    def __init__(self,
                 title=None,
                 HeaderBehavior=REQUIRED, # type: Any
                 Headers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HeaderBehavior=HeaderBehavior,
            Headers=Headers,
            **kwargs
        )
        super(OriginRequestHeadersConfig, self).__init__(**processed_kwargs)


class OriginRequestQueryStringsConfig(troposphere.cloudfront.OriginRequestQueryStringsConfig, Mixin):
    def __init__(self,
                 title=None,
                 QueryStringBehavior=REQUIRED, # type: Any
                 QueryStrings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryStringBehavior=QueryStringBehavior,
            QueryStrings=QueryStrings,
            **kwargs
        )
        super(OriginRequestQueryStringsConfig, self).__init__(**processed_kwargs)


class OriginRequestPolicyConfig(troposphere.cloudfront.OriginRequestPolicyConfig, Mixin):
    def __init__(self,
                 title=None,
                 CookiesConfig=REQUIRED, # type: _OriginRequestCookiesConfig
                 HeadersConfig=REQUIRED, # type: _OriginRequestHeadersConfig
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 QueryStringsConfig=REQUIRED, # type: _OriginRequestQueryStringsConfig
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CookiesConfig=CookiesConfig,
            HeadersConfig=HeadersConfig,
            Name=Name,
            QueryStringsConfig=QueryStringsConfig,
            Comment=Comment,
            **kwargs
        )
        super(OriginRequestPolicyConfig, self).__init__(**processed_kwargs)


class OriginRequestPolicy(troposphere.cloudfront.OriginRequestPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 OriginRequestPolicyConfig=REQUIRED, # type: _OriginRequestPolicyConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            OriginRequestPolicyConfig=OriginRequestPolicyConfig,
            **kwargs
        )
        super(OriginRequestPolicy, self).__init__(**processed_kwargs)


class KeyGroupConfig(troposphere.cloudfront.KeyGroupConfig, Mixin):
    def __init__(self,
                 title=None,
                 Items=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Items=Items,
            Name=Name,
            Comment=Comment,
            **kwargs
        )
        super(KeyGroupConfig, self).__init__(**processed_kwargs)


class KeyGroup(troposphere.cloudfront.KeyGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyGroupConfig=REQUIRED, # type: _KeyGroupConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyGroupConfig=KeyGroupConfig,
            **kwargs
        )
        super(KeyGroup, self).__init__(**processed_kwargs)


class PublicKeyConfig(troposphere.cloudfront.PublicKeyConfig, Mixin):
    def __init__(self,
                 title=None,
                 CallerReference=REQUIRED, # type: Union[str, AWSHelperFn]
                 EncodedKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Comment=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CallerReference=CallerReference,
            EncodedKey=EncodedKey,
            Name=Name,
            Comment=Comment,
            **kwargs
        )
        super(PublicKeyConfig, self).__init__(**processed_kwargs)


class PublicKey(troposphere.cloudfront.PublicKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PublicKeyConfig=REQUIRED, # type: _PublicKeyConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PublicKeyConfig=PublicKeyConfig,
            **kwargs
        )
        super(PublicKey, self).__init__(**processed_kwargs)


class KinesisStreamConfig(troposphere.cloudfront.KinesisStreamConfig, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StreamArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            StreamArn=StreamArn,
            **kwargs
        )
        super(KinesisStreamConfig, self).__init__(**processed_kwargs)


class EndPoint(troposphere.cloudfront.EndPoint, Mixin):
    def __init__(self,
                 title=None,
                 KinesisStreamConfig=REQUIRED, # type: _KinesisStreamConfig
                 StreamType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KinesisStreamConfig=KinesisStreamConfig,
            StreamType=StreamType,
            **kwargs
        )
        super(EndPoint, self).__init__(**processed_kwargs)


class RealtimeLogConfig(troposphere.cloudfront.RealtimeLogConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndPoints=REQUIRED, # type: List[_EndPoint]
                 Fields=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SamplingRate=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndPoints=EndPoints,
            Fields=Fields,
            Name=Name,
            SamplingRate=SamplingRate,
            **kwargs
        )
        super(RealtimeLogConfig, self).__init__(**processed_kwargs)
