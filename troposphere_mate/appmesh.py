# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appmesh

from troposphere.appmesh import (
    AccessLog as _AccessLog,
    AwsCloudMapInstanceAttribute as _AwsCloudMapInstanceAttribute,
    AwsCloudMapServiceDiscovery as _AwsCloudMapServiceDiscovery,
    Backend as _Backend,
    BackendDefaults as _BackendDefaults,
    ClientPolicy as _ClientPolicy,
    ClientPolicyTls as _ClientPolicyTls,
    ClientTlsCertificate as _ClientTlsCertificate,
    DnsServiceDiscovery as _DnsServiceDiscovery,
    Duration as _Duration,
    EgressFilter as _EgressFilter,
    FileAccessLog as _FileAccessLog,
    GatewayRouteSpec as _GatewayRouteSpec,
    GatewayRouteTarget as _GatewayRouteTarget,
    GatewayRouteVirtualService as _GatewayRouteVirtualService,
    GrpcGatewayRoute as _GrpcGatewayRoute,
    GrpcGatewayRouteAction as _GrpcGatewayRouteAction,
    GrpcGatewayRouteMatch as _GrpcGatewayRouteMatch,
    GrpcRetryPolicy as _GrpcRetryPolicy,
    GrpcRoute as _GrpcRoute,
    GrpcRouteAction as _GrpcRouteAction,
    GrpcRouteMatch as _GrpcRouteMatch,
    GrpcRouteMetadata as _GrpcRouteMetadata,
    GrpcRouteMetadataMatchMethod as _GrpcRouteMetadataMatchMethod,
    GrpcTimeout as _GrpcTimeout,
    HeaderMatchMethod as _HeaderMatchMethod,
    HealthCheck as _HealthCheck,
    HttpGatewayRoute as _HttpGatewayRoute,
    HttpGatewayRouteAction as _HttpGatewayRouteAction,
    HttpGatewayRouteMatch as _HttpGatewayRouteMatch,
    HttpRetryPolicy as _HttpRetryPolicy,
    HttpRoute as _HttpRoute,
    HttpRouteAction as _HttpRouteAction,
    HttpRouteHeader as _HttpRouteHeader,
    HttpRouteMatch as _HttpRouteMatch,
    HttpTimeout as _HttpTimeout,
    Listener as _Listener,
    ListenerTimeout as _ListenerTimeout,
    ListenerTls as _ListenerTls,
    ListenerTlsAcmCertificate as _ListenerTlsAcmCertificate,
    ListenerTlsCertificate as _ListenerTlsCertificate,
    ListenerTlsFileCertificate as _ListenerTlsFileCertificate,
    ListenerTlsSdsCertificate as _ListenerTlsSdsCertificate,
    ListenerTlsValidationContext as _ListenerTlsValidationContext,
    ListenerTlsValidationContextTrust as _ListenerTlsValidationContextTrust,
    Logging as _Logging,
    MatchRange as _MatchRange,
    MeshSpec as _MeshSpec,
    OutlierDetection as _OutlierDetection,
    PortMapping as _PortMapping,
    RouteSpec as _RouteSpec,
    ServiceDiscovery as _ServiceDiscovery,
    SubjectAlternativeNameMatchers as _SubjectAlternativeNameMatchers,
    SubjectAlternativeNames as _SubjectAlternativeNames,
    Tags as _Tags,
    TcpRoute as _TcpRoute,
    TcpRouteAction as _TcpRouteAction,
    TcpTimeout as _TcpTimeout,
    TlsValidationContext as _TlsValidationContext,
    TlsValidationContextAcmTrust as _TlsValidationContextAcmTrust,
    TlsValidationContextFileTrust as _TlsValidationContextFileTrust,
    TlsValidationContextSdsTrust as _TlsValidationContextSdsTrust,
    TlsValidationContextTrust as _TlsValidationContextTrust,
    VirtualGatewayAccessLog as _VirtualGatewayAccessLog,
    VirtualGatewayBackendDefaults as _VirtualGatewayBackendDefaults,
    VirtualGatewayClientPolicy as _VirtualGatewayClientPolicy,
    VirtualGatewayClientPolicyTls as _VirtualGatewayClientPolicyTls,
    VirtualGatewayClientTlsCertificate as _VirtualGatewayClientTlsCertificate,
    VirtualGatewayConnectionPool as _VirtualGatewayConnectionPool,
    VirtualGatewayFileAccessLog as _VirtualGatewayFileAccessLog,
    VirtualGatewayGrpcConnectionPool as _VirtualGatewayGrpcConnectionPool,
    VirtualGatewayHealthCheckPolicy as _VirtualGatewayHealthCheckPolicy,
    VirtualGatewayHttp2ConnectionPool as _VirtualGatewayHttp2ConnectionPool,
    VirtualGatewayHttpConnectionPool as _VirtualGatewayHttpConnectionPool,
    VirtualGatewayListener as _VirtualGatewayListener,
    VirtualGatewayListenerTls as _VirtualGatewayListenerTls,
    VirtualGatewayListenerTlsAcmCertificate as _VirtualGatewayListenerTlsAcmCertificate,
    VirtualGatewayListenerTlsCertificate as _VirtualGatewayListenerTlsCertificate,
    VirtualGatewayListenerTlsFileCertificate as _VirtualGatewayListenerTlsFileCertificate,
    VirtualGatewayListenerTlsSdsCertificate as _VirtualGatewayListenerTlsSdsCertificate,
    VirtualGatewayListenerTlsValidationContext as _VirtualGatewayListenerTlsValidationContext,
    VirtualGatewayListenerTlsValidationContextTrust as _VirtualGatewayListenerTlsValidationContextTrust,
    VirtualGatewayLogging as _VirtualGatewayLogging,
    VirtualGatewayPortMapping as _VirtualGatewayPortMapping,
    VirtualGatewaySpec as _VirtualGatewaySpec,
    VirtualGatewayTlsValidationContext as _VirtualGatewayTlsValidationContext,
    VirtualGatewayTlsValidationContextAcmTrust as _VirtualGatewayTlsValidationContextAcmTrust,
    VirtualGatewayTlsValidationContextFileTrust as _VirtualGatewayTlsValidationContextFileTrust,
    VirtualGatewayTlsValidationContextSdsTrust as _VirtualGatewayTlsValidationContextSdsTrust,
    VirtualGatewayTlsValidationContextTrust as _VirtualGatewayTlsValidationContextTrust,
    VirtualNodeConnectionPool as _VirtualNodeConnectionPool,
    VirtualNodeGrpcConnectionPool as _VirtualNodeGrpcConnectionPool,
    VirtualNodeHttp2ConnectionPool as _VirtualNodeHttp2ConnectionPool,
    VirtualNodeHttpConnectionPool as _VirtualNodeHttpConnectionPool,
    VirtualNodeServiceProvider as _VirtualNodeServiceProvider,
    VirtualNodeSpec as _VirtualNodeSpec,
    VirtualNodeTcpConnectionPool as _VirtualNodeTcpConnectionPool,
    VirtualRouterListener as _VirtualRouterListener,
    VirtualRouterServiceProvider as _VirtualRouterServiceProvider,
    VirtualRouterSpec as _VirtualRouterSpec,
    VirtualServiceBackend as _VirtualServiceBackend,
    VirtualServiceProvider as _VirtualServiceProvider,
    VirtualServiceSpec as _VirtualServiceSpec,
    WeightedTarget as _WeightedTarget,
    integer as _integer,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class GatewayRouteVirtualService(troposphere.appmesh.GatewayRouteVirtualService, Mixin):
    def __init__(self,
                 title=None,
                 VirtualServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualServiceName=VirtualServiceName,
            **kwargs
        )
        super(GatewayRouteVirtualService, self).__init__(**processed_kwargs)


class GatewayRouteTarget(troposphere.appmesh.GatewayRouteTarget, Mixin):
    def __init__(self,
                 title=None,
                 VirtualService=REQUIRED, # type: _GatewayRouteVirtualService
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualService=VirtualService,
            **kwargs
        )
        super(GatewayRouteTarget, self).__init__(**processed_kwargs)


class GrpcGatewayRouteAction(troposphere.appmesh.GrpcGatewayRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 Target=REQUIRED, # type: _GatewayRouteTarget
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Target=Target,
            **kwargs
        )
        super(GrpcGatewayRouteAction, self).__init__(**processed_kwargs)


class GrpcGatewayRouteMatch(troposphere.appmesh.GrpcGatewayRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceName=ServiceName,
            **kwargs
        )
        super(GrpcGatewayRouteMatch, self).__init__(**processed_kwargs)


class GrpcGatewayRoute(troposphere.appmesh.GrpcGatewayRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _GrpcGatewayRouteAction
                 Match=REQUIRED, # type: _GrpcGatewayRouteMatch
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            **kwargs
        )
        super(GrpcGatewayRoute, self).__init__(**processed_kwargs)


class HttpGatewayRouteAction(troposphere.appmesh.HttpGatewayRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 Target=REQUIRED, # type: _GatewayRouteTarget
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Target=Target,
            **kwargs
        )
        super(HttpGatewayRouteAction, self).__init__(**processed_kwargs)


class HttpGatewayRouteMatch(troposphere.appmesh.HttpGatewayRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prefix=Prefix,
            **kwargs
        )
        super(HttpGatewayRouteMatch, self).__init__(**processed_kwargs)


class HttpGatewayRoute(troposphere.appmesh.HttpGatewayRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _HttpGatewayRouteAction
                 Match=REQUIRED, # type: _HttpGatewayRouteMatch
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            **kwargs
        )
        super(HttpGatewayRoute, self).__init__(**processed_kwargs)


class GatewayRouteSpec(troposphere.appmesh.GatewayRouteSpec, Mixin):
    def __init__(self,
                 title=None,
                 GrpcRoute=NOTHING, # type: _GrpcGatewayRoute
                 Http2Route=NOTHING, # type: _HttpGatewayRoute
                 HttpRoute=NOTHING, # type: _HttpGatewayRoute
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GrpcRoute=GrpcRoute,
            Http2Route=Http2Route,
            HttpRoute=HttpRoute,
            **kwargs
        )
        super(GatewayRouteSpec, self).__init__(**processed_kwargs)


class GatewayRoute(troposphere.appmesh.GatewayRoute, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _GatewayRouteSpec
                 VirtualGatewayName=REQUIRED, # type: Union[str, AWSHelperFn]
                 GatewayRouteName=NOTHING, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualGatewayName=VirtualGatewayName,
            GatewayRouteName=GatewayRouteName,
            MeshOwner=MeshOwner,
            Tags=Tags,
            **kwargs
        )
        super(GatewayRoute, self).__init__(**processed_kwargs)


class EgressFilter(troposphere.appmesh.EgressFilter, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            **kwargs
        )
        super(EgressFilter, self).__init__(**processed_kwargs)


class MeshSpec(troposphere.appmesh.MeshSpec, Mixin):
    def __init__(self,
                 title=None,
                 EgressFilter=NOTHING, # type: _EgressFilter
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EgressFilter=EgressFilter,
            **kwargs
        )
        super(MeshSpec, self).__init__(**processed_kwargs)


class Mesh(troposphere.appmesh.Mesh, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=NOTHING, # type: Union[str, AWSHelperFn]
                 Spec=NOTHING, # type: _MeshSpec
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            Tags=Tags,
            **kwargs
        )
        super(Mesh, self).__init__(**processed_kwargs)


class Duration(troposphere.appmesh.Duration, Mixin):
    def __init__(self,
                 title=None,
                 Unit=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Unit=Unit,
            Value=Value,
            **kwargs
        )
        super(Duration, self).__init__(**processed_kwargs)


class GrpcRetryPolicy(troposphere.appmesh.GrpcRetryPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MaxRetries=REQUIRED, # type: int
                 PerRetryTimeout=REQUIRED, # type: _Duration
                 GrpcRetryEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 HttpRetryEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TcpRetryEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRetries=MaxRetries,
            PerRetryTimeout=PerRetryTimeout,
            GrpcRetryEvents=GrpcRetryEvents,
            HttpRetryEvents=HttpRetryEvents,
            TcpRetryEvents=TcpRetryEvents,
            **kwargs
        )
        super(GrpcRetryPolicy, self).__init__(**processed_kwargs)


class WeightedTarget(troposphere.appmesh.WeightedTarget, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNode=REQUIRED, # type: Union[str, AWSHelperFn]
                 Weight=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNode=VirtualNode,
            Weight=Weight,
            **kwargs
        )
        super(WeightedTarget, self).__init__(**processed_kwargs)


class GrpcRouteAction(troposphere.appmesh.GrpcRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: List[_WeightedTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(GrpcRouteAction, self).__init__(**processed_kwargs)


class MatchRange(troposphere.appmesh.MatchRange, Mixin):
    def __init__(self,
                 title=None,
                 End=REQUIRED, # type: int
                 Start=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            End=End,
            Start=Start,
            **kwargs
        )
        super(MatchRange, self).__init__(**processed_kwargs)


class GrpcRouteMetadataMatchMethod(troposphere.appmesh.GrpcRouteMetadataMatchMethod, Mixin):
    def __init__(self,
                 title=None,
                 Exact=NOTHING, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 Range=NOTHING, # type: _MatchRange
                 Regex=NOTHING, # type: Union[str, AWSHelperFn]
                 Suffix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Exact=Exact,
            Prefix=Prefix,
            Range=Range,
            Regex=Regex,
            Suffix=Suffix,
            **kwargs
        )
        super(GrpcRouteMetadataMatchMethod, self).__init__(**processed_kwargs)


class GrpcRouteMetadata(troposphere.appmesh.GrpcRouteMetadata, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Invert=NOTHING, # type: bool
                 Match=NOTHING, # type: _GrpcRouteMetadataMatchMethod
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Invert=Invert,
            Match=Match,
            **kwargs
        )
        super(GrpcRouteMetadata, self).__init__(**processed_kwargs)


class GrpcRouteMatch(troposphere.appmesh.GrpcRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 Metadata=NOTHING, # type: List[_GrpcRouteMetadata]
                 MethodName=NOTHING, # type: Union[str, AWSHelperFn]
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Metadata=Metadata,
            MethodName=MethodName,
            ServiceName=ServiceName,
            **kwargs
        )
        super(GrpcRouteMatch, self).__init__(**processed_kwargs)


class GrpcTimeout(troposphere.appmesh.GrpcTimeout, Mixin):
    def __init__(self,
                 title=None,
                 Idle=NOTHING, # type: _Duration
                 PerRequest=NOTHING, # type: _Duration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Idle=Idle,
            PerRequest=PerRequest,
            **kwargs
        )
        super(GrpcTimeout, self).__init__(**processed_kwargs)


class GrpcRoute(troposphere.appmesh.GrpcRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _GrpcRouteAction
                 Match=REQUIRED, # type: _GrpcRouteMatch
                 RetryPolicy=NOTHING, # type: _GrpcRetryPolicy
                 Timeout=NOTHING, # type: _GrpcTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            RetryPolicy=RetryPolicy,
            Timeout=Timeout,
            **kwargs
        )
        super(GrpcRoute, self).__init__(**processed_kwargs)


class HttpRetryPolicy(troposphere.appmesh.HttpRetryPolicy, Mixin):
    def __init__(self,
                 title=None,
                 MaxRetries=REQUIRED, # type: int
                 PerRetryTimeout=REQUIRED, # type: _Duration
                 HttpRetryEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 TcpRetryEvents=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRetries=MaxRetries,
            PerRetryTimeout=PerRetryTimeout,
            HttpRetryEvents=HttpRetryEvents,
            TcpRetryEvents=TcpRetryEvents,
            **kwargs
        )
        super(HttpRetryPolicy, self).__init__(**processed_kwargs)


class HttpRouteAction(troposphere.appmesh.HttpRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: List[_WeightedTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(HttpRouteAction, self).__init__(**processed_kwargs)


class HeaderMatchMethod(troposphere.appmesh.HeaderMatchMethod, Mixin):
    def __init__(self,
                 title=None,
                 Exact=NOTHING, # type: Union[str, AWSHelperFn]
                 Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 Range=NOTHING, # type: _MatchRange
                 Regex=NOTHING, # type: Union[str, AWSHelperFn]
                 Suffix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Exact=Exact,
            Prefix=Prefix,
            Range=Range,
            Regex=Regex,
            Suffix=Suffix,
            **kwargs
        )
        super(HeaderMatchMethod, self).__init__(**processed_kwargs)


class HttpRouteHeader(troposphere.appmesh.HttpRouteHeader, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Invert=NOTHING, # type: bool
                 Match=NOTHING, # type: _HeaderMatchMethod
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Invert=Invert,
            Match=Match,
            **kwargs
        )
        super(HttpRouteHeader, self).__init__(**processed_kwargs)


class HttpRouteMatch(troposphere.appmesh.HttpRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 Headers=NOTHING, # type: List[_HttpRouteHeader]
                 Method=NOTHING, # type: Union[str, AWSHelperFn]
                 Scheme=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prefix=Prefix,
            Headers=Headers,
            Method=Method,
            Scheme=Scheme,
            **kwargs
        )
        super(HttpRouteMatch, self).__init__(**processed_kwargs)


class HttpTimeout(troposphere.appmesh.HttpTimeout, Mixin):
    def __init__(self,
                 title=None,
                 Idle=NOTHING, # type: _Duration
                 PerRequest=NOTHING, # type: _Duration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Idle=Idle,
            PerRequest=PerRequest,
            **kwargs
        )
        super(HttpTimeout, self).__init__(**processed_kwargs)


class HttpRoute(troposphere.appmesh.HttpRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _HttpRouteAction
                 Match=REQUIRED, # type: _HttpRouteMatch
                 RetryPolicy=NOTHING, # type: _HttpRetryPolicy
                 Timeout=NOTHING, # type: _HttpTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            RetryPolicy=RetryPolicy,
            Timeout=Timeout,
            **kwargs
        )
        super(HttpRoute, self).__init__(**processed_kwargs)


class TcpRouteAction(troposphere.appmesh.TcpRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: List[_WeightedTarget]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(TcpRouteAction, self).__init__(**processed_kwargs)


class TcpTimeout(troposphere.appmesh.TcpTimeout, Mixin):
    def __init__(self,
                 title=None,
                 Idle=NOTHING, # type: _Duration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Idle=Idle,
            **kwargs
        )
        super(TcpTimeout, self).__init__(**processed_kwargs)


class TcpRoute(troposphere.appmesh.TcpRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _TcpRouteAction
                 Timeout=NOTHING, # type: _TcpTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Timeout=Timeout,
            **kwargs
        )
        super(TcpRoute, self).__init__(**processed_kwargs)


class RouteSpec(troposphere.appmesh.RouteSpec, Mixin):
    def __init__(self,
                 title=None,
                 GrpcRoute=NOTHING, # type: _GrpcRoute
                 Http2Route=NOTHING, # type: _HttpRoute
                 HttpRoute=NOTHING, # type: _HttpRoute
                 Priority=NOTHING, # type: int
                 TcpRoute=NOTHING, # type: _TcpRoute
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GrpcRoute=GrpcRoute,
            Http2Route=Http2Route,
            HttpRoute=HttpRoute,
            Priority=Priority,
            TcpRoute=TcpRoute,
            **kwargs
        )
        super(RouteSpec, self).__init__(**processed_kwargs)


class Route(troposphere.appmesh.Route, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _RouteSpec
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 RouteName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualRouterName=VirtualRouterName,
            MeshOwner=MeshOwner,
            RouteName=RouteName,
            Tags=Tags,
            **kwargs
        )
        super(Route, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsFileCertificate(troposphere.appmesh.VirtualGatewayListenerTlsFileCertificate, Mixin):
    def __init__(self,
                 title=None,
                 CertificateChain=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrivateKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateChain=CertificateChain,
            PrivateKey=PrivateKey,
            **kwargs
        )
        super(VirtualGatewayListenerTlsFileCertificate, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsSdsCertificate(troposphere.appmesh.VirtualGatewayListenerTlsSdsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 SecretName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretName=SecretName,
            **kwargs
        )
        super(VirtualGatewayListenerTlsSdsCertificate, self).__init__(**processed_kwargs)


class VirtualGatewayClientTlsCertificate(troposphere.appmesh.VirtualGatewayClientTlsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _VirtualGatewayListenerTlsFileCertificate
                 SDS=NOTHING, # type: _VirtualGatewayListenerTlsSdsCertificate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(VirtualGatewayClientTlsCertificate, self).__init__(**processed_kwargs)


class SubjectAlternativeNameMatchers(troposphere.appmesh.SubjectAlternativeNameMatchers, Mixin):
    def __init__(self,
                 title=None,
                 Exact=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Exact=Exact,
            **kwargs
        )
        super(SubjectAlternativeNameMatchers, self).__init__(**processed_kwargs)


class SubjectAlternativeNames(troposphere.appmesh.SubjectAlternativeNames, Mixin):
    def __init__(self,
                 title=None,
                 Match=REQUIRED, # type: _SubjectAlternativeNameMatchers
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Match=Match,
            **kwargs
        )
        super(SubjectAlternativeNames, self).__init__(**processed_kwargs)


class VirtualGatewayTlsValidationContextAcmTrust(troposphere.appmesh.VirtualGatewayTlsValidationContextAcmTrust, Mixin):
    def __init__(self,
                 title=None,
                 CertificateAuthorityArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateAuthorityArns=CertificateAuthorityArns,
            **kwargs
        )
        super(VirtualGatewayTlsValidationContextAcmTrust, self).__init__(**processed_kwargs)


class VirtualGatewayTlsValidationContextFileTrust(troposphere.appmesh.VirtualGatewayTlsValidationContextFileTrust, Mixin):
    def __init__(self,
                 title=None,
                 CertificateChain=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateChain=CertificateChain,
            **kwargs
        )
        super(VirtualGatewayTlsValidationContextFileTrust, self).__init__(**processed_kwargs)


class VirtualGatewayTlsValidationContextSdsTrust(troposphere.appmesh.VirtualGatewayTlsValidationContextSdsTrust, Mixin):
    def __init__(self,
                 title=None,
                 SecretName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretName=SecretName,
            **kwargs
        )
        super(VirtualGatewayTlsValidationContextSdsTrust, self).__init__(**processed_kwargs)


class VirtualGatewayTlsValidationContextTrust(troposphere.appmesh.VirtualGatewayTlsValidationContextTrust, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _VirtualGatewayTlsValidationContextAcmTrust
                 File=NOTHING, # type: _VirtualGatewayTlsValidationContextFileTrust
                 SDS=NOTHING, # type: _VirtualGatewayTlsValidationContextSdsTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(VirtualGatewayTlsValidationContextTrust, self).__init__(**processed_kwargs)


class VirtualGatewayTlsValidationContext(troposphere.appmesh.VirtualGatewayTlsValidationContext, Mixin):
    def __init__(self,
                 title=None,
                 Trust=REQUIRED, # type: _VirtualGatewayTlsValidationContextTrust
                 SubjectAlternativeNames=NOTHING, # type: _SubjectAlternativeNames
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Trust=Trust,
            SubjectAlternativeNames=SubjectAlternativeNames,
            **kwargs
        )
        super(VirtualGatewayTlsValidationContext, self).__init__(**processed_kwargs)


class VirtualGatewayClientPolicyTls(troposphere.appmesh.VirtualGatewayClientPolicyTls, Mixin):
    def __init__(self,
                 title=None,
                 Validation=REQUIRED, # type: _VirtualGatewayTlsValidationContext
                 Certificate=NOTHING, # type: _VirtualGatewayClientTlsCertificate
                 Enforce=NOTHING, # type: bool
                 Ports=NOTHING, # type: List[_integer]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Validation=Validation,
            Certificate=Certificate,
            Enforce=Enforce,
            Ports=Ports,
            **kwargs
        )
        super(VirtualGatewayClientPolicyTls, self).__init__(**processed_kwargs)


class VirtualGatewayClientPolicy(troposphere.appmesh.VirtualGatewayClientPolicy, Mixin):
    def __init__(self,
                 title=None,
                 TLS=NOTHING, # type: _VirtualGatewayClientPolicyTls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TLS=TLS,
            **kwargs
        )
        super(VirtualGatewayClientPolicy, self).__init__(**processed_kwargs)


class VirtualGatewayBackendDefaults(troposphere.appmesh.VirtualGatewayBackendDefaults, Mixin):
    def __init__(self,
                 title=None,
                 ClientPolicy=NOTHING, # type: _VirtualGatewayClientPolicy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientPolicy=ClientPolicy,
            **kwargs
        )
        super(VirtualGatewayBackendDefaults, self).__init__(**processed_kwargs)


class VirtualGatewayGrpcConnectionPool(troposphere.appmesh.VirtualGatewayGrpcConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxRequests=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRequests=MaxRequests,
            **kwargs
        )
        super(VirtualGatewayGrpcConnectionPool, self).__init__(**processed_kwargs)


class VirtualGatewayHttp2ConnectionPool(troposphere.appmesh.VirtualGatewayHttp2ConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxRequests=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRequests=MaxRequests,
            **kwargs
        )
        super(VirtualGatewayHttp2ConnectionPool, self).__init__(**processed_kwargs)


class VirtualGatewayHttpConnectionPool(troposphere.appmesh.VirtualGatewayHttpConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxConnections=REQUIRED, # type: int
                 MaxPendingRequests=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxConnections=MaxConnections,
            MaxPendingRequests=MaxPendingRequests,
            **kwargs
        )
        super(VirtualGatewayHttpConnectionPool, self).__init__(**processed_kwargs)


class VirtualGatewayConnectionPool(troposphere.appmesh.VirtualGatewayConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 GRPC=NOTHING, # type: _VirtualGatewayGrpcConnectionPool
                 HTTP=NOTHING, # type: _VirtualGatewayHttpConnectionPool
                 HTTP2=NOTHING, # type: _VirtualGatewayHttp2ConnectionPool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GRPC=GRPC,
            HTTP=HTTP,
            HTTP2=HTTP2,
            **kwargs
        )
        super(VirtualGatewayConnectionPool, self).__init__(**processed_kwargs)


class VirtualGatewayHealthCheckPolicy(troposphere.appmesh.VirtualGatewayHealthCheckPolicy, Mixin):
    def __init__(self,
                 title=None,
                 HealthyThreshold=REQUIRED, # type: int
                 IntervalMillis=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeoutMillis=REQUIRED, # type: int
                 UnhealthyThreshold=REQUIRED, # type: int
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HealthyThreshold=HealthyThreshold,
            IntervalMillis=IntervalMillis,
            Protocol=Protocol,
            TimeoutMillis=TimeoutMillis,
            UnhealthyThreshold=UnhealthyThreshold,
            Path=Path,
            Port=Port,
            **kwargs
        )
        super(VirtualGatewayHealthCheckPolicy, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsAcmCertificate(troposphere.appmesh.VirtualGatewayListenerTlsAcmCertificate, Mixin):
    def __init__(self,
                 title=None,
                 CertificateArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateArn=CertificateArn,
            **kwargs
        )
        super(VirtualGatewayListenerTlsAcmCertificate, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsCertificate(troposphere.appmesh.VirtualGatewayListenerTlsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _VirtualGatewayListenerTlsAcmCertificate
                 File=NOTHING, # type: _VirtualGatewayListenerTlsFileCertificate
                 SDS=NOTHING, # type: _VirtualGatewayListenerTlsSdsCertificate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(VirtualGatewayListenerTlsCertificate, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsValidationContextTrust(troposphere.appmesh.VirtualGatewayListenerTlsValidationContextTrust, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _VirtualGatewayTlsValidationContextFileTrust
                 SDS=NOTHING, # type: _VirtualGatewayTlsValidationContextSdsTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(VirtualGatewayListenerTlsValidationContextTrust, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTlsValidationContext(troposphere.appmesh.VirtualGatewayListenerTlsValidationContext, Mixin):
    def __init__(self,
                 title=None,
                 Trust=REQUIRED, # type: _VirtualGatewayListenerTlsValidationContextTrust
                 SubjectAlternativeNames=NOTHING, # type: _SubjectAlternativeNames
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Trust=Trust,
            SubjectAlternativeNames=SubjectAlternativeNames,
            **kwargs
        )
        super(VirtualGatewayListenerTlsValidationContext, self).__init__(**processed_kwargs)


class VirtualGatewayListenerTls(troposphere.appmesh.VirtualGatewayListenerTls, Mixin):
    def __init__(self,
                 title=None,
                 Certificate=REQUIRED, # type: _VirtualGatewayListenerTlsCertificate
                 Mode=REQUIRED, # type: Union[str, AWSHelperFn]
                 Validation=NOTHING, # type: _VirtualGatewayListenerTlsValidationContext
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Certificate=Certificate,
            Mode=Mode,
            Validation=Validation,
            **kwargs
        )
        super(VirtualGatewayListenerTls, self).__init__(**processed_kwargs)


class VirtualGatewayPortMapping(troposphere.appmesh.VirtualGatewayPortMapping, Mixin):
    def __init__(self,
                 title=None,
                 Port=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Port=Port,
            Protocol=Protocol,
            **kwargs
        )
        super(VirtualGatewayPortMapping, self).__init__(**processed_kwargs)


class VirtualGatewayListener(troposphere.appmesh.VirtualGatewayListener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _VirtualGatewayPortMapping
                 ConnectionPool=NOTHING, # type: _VirtualGatewayConnectionPool
                 HealthCheck=NOTHING, # type: _VirtualGatewayHealthCheckPolicy
                 TLS=NOTHING, # type: _VirtualGatewayListenerTls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            ConnectionPool=ConnectionPool,
            HealthCheck=HealthCheck,
            TLS=TLS,
            **kwargs
        )
        super(VirtualGatewayListener, self).__init__(**processed_kwargs)


class VirtualGatewayFileAccessLog(troposphere.appmesh.VirtualGatewayFileAccessLog, Mixin):
    def __init__(self,
                 title=None,
                 Path=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Path=Path,
            **kwargs
        )
        super(VirtualGatewayFileAccessLog, self).__init__(**processed_kwargs)


class VirtualGatewayAccessLog(troposphere.appmesh.VirtualGatewayAccessLog, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _VirtualGatewayFileAccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            **kwargs
        )
        super(VirtualGatewayAccessLog, self).__init__(**processed_kwargs)


class VirtualGatewayLogging(troposphere.appmesh.VirtualGatewayLogging, Mixin):
    def __init__(self,
                 title=None,
                 AccessLog=NOTHING, # type: _VirtualGatewayAccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessLog=AccessLog,
            **kwargs
        )
        super(VirtualGatewayLogging, self).__init__(**processed_kwargs)


class VirtualGatewaySpec(troposphere.appmesh.VirtualGatewaySpec, Mixin):
    def __init__(self,
                 title=None,
                 Listeners=REQUIRED, # type: List[_VirtualGatewayListener]
                 BackendDefaults=NOTHING, # type: _VirtualGatewayBackendDefaults
                 Logging=NOTHING, # type: _VirtualGatewayLogging
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Listeners=Listeners,
            BackendDefaults=BackendDefaults,
            Logging=Logging,
            **kwargs
        )
        super(VirtualGatewaySpec, self).__init__(**processed_kwargs)


class VirtualGateway(troposphere.appmesh.VirtualGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualGatewaySpec
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VirtualGatewayName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            MeshOwner=MeshOwner,
            Tags=Tags,
            VirtualGatewayName=VirtualGatewayName,
            **kwargs
        )
        super(VirtualGateway, self).__init__(**processed_kwargs)


class ListenerTlsFileCertificate(troposphere.appmesh.ListenerTlsFileCertificate, Mixin):
    def __init__(self,
                 title=None,
                 CertificateChain=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrivateKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateChain=CertificateChain,
            PrivateKey=PrivateKey,
            **kwargs
        )
        super(ListenerTlsFileCertificate, self).__init__(**processed_kwargs)


class ListenerTlsSdsCertificate(troposphere.appmesh.ListenerTlsSdsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 SecretName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretName=SecretName,
            **kwargs
        )
        super(ListenerTlsSdsCertificate, self).__init__(**processed_kwargs)


class ClientTlsCertificate(troposphere.appmesh.ClientTlsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _ListenerTlsFileCertificate
                 SDS=NOTHING, # type: _ListenerTlsSdsCertificate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(ClientTlsCertificate, self).__init__(**processed_kwargs)


class TlsValidationContextAcmTrust(troposphere.appmesh.TlsValidationContextAcmTrust, Mixin):
    def __init__(self,
                 title=None,
                 CertificateAuthorityArns=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateAuthorityArns=CertificateAuthorityArns,
            **kwargs
        )
        super(TlsValidationContextAcmTrust, self).__init__(**processed_kwargs)


class TlsValidationContextFileTrust(troposphere.appmesh.TlsValidationContextFileTrust, Mixin):
    def __init__(self,
                 title=None,
                 CertificateChain=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateChain=CertificateChain,
            **kwargs
        )
        super(TlsValidationContextFileTrust, self).__init__(**processed_kwargs)


class TlsValidationContextSdsTrust(troposphere.appmesh.TlsValidationContextSdsTrust, Mixin):
    def __init__(self,
                 title=None,
                 SecretName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretName=SecretName,
            **kwargs
        )
        super(TlsValidationContextSdsTrust, self).__init__(**processed_kwargs)


class TlsValidationContextTrust(troposphere.appmesh.TlsValidationContextTrust, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _TlsValidationContextAcmTrust
                 File=NOTHING, # type: _TlsValidationContextFileTrust
                 SDS=NOTHING, # type: _TlsValidationContextSdsTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(TlsValidationContextTrust, self).__init__(**processed_kwargs)


class TlsValidationContext(troposphere.appmesh.TlsValidationContext, Mixin):
    def __init__(self,
                 title=None,
                 Trust=REQUIRED, # type: _TlsValidationContextTrust
                 SubjectAlternativeNames=NOTHING, # type: _SubjectAlternativeNames
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Trust=Trust,
            SubjectAlternativeNames=SubjectAlternativeNames,
            **kwargs
        )
        super(TlsValidationContext, self).__init__(**processed_kwargs)


class ClientPolicyTls(troposphere.appmesh.ClientPolicyTls, Mixin):
    def __init__(self,
                 title=None,
                 Validation=REQUIRED, # type: _TlsValidationContext
                 Certificate=NOTHING, # type: _ClientTlsCertificate
                 Enforce=NOTHING, # type: bool
                 Ports=NOTHING, # type: List[_integer]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Validation=Validation,
            Certificate=Certificate,
            Enforce=Enforce,
            Ports=Ports,
            **kwargs
        )
        super(ClientPolicyTls, self).__init__(**processed_kwargs)


class ClientPolicy(troposphere.appmesh.ClientPolicy, Mixin):
    def __init__(self,
                 title=None,
                 TLS=NOTHING, # type: _ClientPolicyTls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TLS=TLS,
            **kwargs
        )
        super(ClientPolicy, self).__init__(**processed_kwargs)


class VirtualServiceBackend(troposphere.appmesh.VirtualServiceBackend, Mixin):
    def __init__(self,
                 title=None,
                 VirtualServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClientPolicy=NOTHING, # type: _ClientPolicy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualServiceName=VirtualServiceName,
            ClientPolicy=ClientPolicy,
            **kwargs
        )
        super(VirtualServiceBackend, self).__init__(**processed_kwargs)


class Backend(troposphere.appmesh.Backend, Mixin):
    def __init__(self,
                 title=None,
                 VirtualService=NOTHING, # type: _VirtualServiceBackend
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualService=VirtualService,
            **kwargs
        )
        super(Backend, self).__init__(**processed_kwargs)


class BackendDefaults(troposphere.appmesh.BackendDefaults, Mixin):
    def __init__(self,
                 title=None,
                 ClientPolicy=NOTHING, # type: _ClientPolicy
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClientPolicy=ClientPolicy,
            **kwargs
        )
        super(BackendDefaults, self).__init__(**processed_kwargs)


class HealthCheck(troposphere.appmesh.HealthCheck, Mixin):
    def __init__(self,
                 title=None,
                 HealthyThreshold=REQUIRED, # type: int
                 IntervalMillis=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 TimeoutMillis=REQUIRED, # type: int
                 UnhealthyThreshold=REQUIRED, # type: int
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HealthyThreshold=HealthyThreshold,
            IntervalMillis=IntervalMillis,
            Protocol=Protocol,
            TimeoutMillis=TimeoutMillis,
            UnhealthyThreshold=UnhealthyThreshold,
            Path=Path,
            Port=Port,
            **kwargs
        )
        super(HealthCheck, self).__init__(**processed_kwargs)


class ListenerTimeout(troposphere.appmesh.ListenerTimeout, Mixin):
    def __init__(self,
                 title=None,
                 GRPC=NOTHING, # type: _GrpcTimeout
                 HTTP=NOTHING, # type: _HttpTimeout
                 HTTP2=NOTHING, # type: _HttpTimeout
                 TCP=NOTHING, # type: _TcpTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GRPC=GRPC,
            HTTP=HTTP,
            HTTP2=HTTP2,
            TCP=TCP,
            **kwargs
        )
        super(ListenerTimeout, self).__init__(**processed_kwargs)


class ListenerTlsAcmCertificate(troposphere.appmesh.ListenerTlsAcmCertificate, Mixin):
    def __init__(self,
                 title=None,
                 CertificateArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificateArn=CertificateArn,
            **kwargs
        )
        super(ListenerTlsAcmCertificate, self).__init__(**processed_kwargs)


class ListenerTlsCertificate(troposphere.appmesh.ListenerTlsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _ListenerTlsAcmCertificate
                 File=NOTHING, # type: _ListenerTlsFileCertificate
                 SDS=NOTHING, # type: _ListenerTlsSdsCertificate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(ListenerTlsCertificate, self).__init__(**processed_kwargs)


class ListenerTlsValidationContextTrust(troposphere.appmesh.ListenerTlsValidationContextTrust, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _TlsValidationContextFileTrust
                 SDS=NOTHING, # type: _TlsValidationContextSdsTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            SDS=SDS,
            **kwargs
        )
        super(ListenerTlsValidationContextTrust, self).__init__(**processed_kwargs)


class ListenerTlsValidationContext(troposphere.appmesh.ListenerTlsValidationContext, Mixin):
    def __init__(self,
                 title=None,
                 Trust=REQUIRED, # type: _ListenerTlsValidationContextTrust
                 SubjectAlternativeNames=NOTHING, # type: _SubjectAlternativeNames
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Trust=Trust,
            SubjectAlternativeNames=SubjectAlternativeNames,
            **kwargs
        )
        super(ListenerTlsValidationContext, self).__init__(**processed_kwargs)


class ListenerTls(troposphere.appmesh.ListenerTls, Mixin):
    def __init__(self,
                 title=None,
                 Certificate=REQUIRED, # type: _ListenerTlsCertificate
                 Mode=REQUIRED, # type: Any
                 Validation=NOTHING, # type: _ListenerTlsValidationContext
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Certificate=Certificate,
            Mode=Mode,
            Validation=Validation,
            **kwargs
        )
        super(ListenerTls, self).__init__(**processed_kwargs)


class OutlierDetection(troposphere.appmesh.OutlierDetection, Mixin):
    def __init__(self,
                 title=None,
                 BaseEjectionDuration=REQUIRED, # type: _Duration
                 Interval=REQUIRED, # type: _Duration
                 MaxEjectionPercent=REQUIRED, # type: int
                 MaxServerErrors=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BaseEjectionDuration=BaseEjectionDuration,
            Interval=Interval,
            MaxEjectionPercent=MaxEjectionPercent,
            MaxServerErrors=MaxServerErrors,
            **kwargs
        )
        super(OutlierDetection, self).__init__(**processed_kwargs)


class PortMapping(troposphere.appmesh.PortMapping, Mixin):
    def __init__(self,
                 title=None,
                 Port=REQUIRED, # type: int
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Port=Port,
            Protocol=Protocol,
            **kwargs
        )
        super(PortMapping, self).__init__(**processed_kwargs)


class VirtualNodeGrpcConnectionPool(troposphere.appmesh.VirtualNodeGrpcConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxRequests=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRequests=MaxRequests,
            **kwargs
        )
        super(VirtualNodeGrpcConnectionPool, self).__init__(**processed_kwargs)


class VirtualNodeHttp2ConnectionPool(troposphere.appmesh.VirtualNodeHttp2ConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxRequests=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxRequests=MaxRequests,
            **kwargs
        )
        super(VirtualNodeHttp2ConnectionPool, self).__init__(**processed_kwargs)


class VirtualNodeHttpConnectionPool(troposphere.appmesh.VirtualNodeHttpConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxConnections=REQUIRED, # type: int
                 MaxPendingRequests=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxConnections=MaxConnections,
            MaxPendingRequests=MaxPendingRequests,
            **kwargs
        )
        super(VirtualNodeHttpConnectionPool, self).__init__(**processed_kwargs)


class VirtualNodeTcpConnectionPool(troposphere.appmesh.VirtualNodeTcpConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 MaxConnections=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxConnections=MaxConnections,
            **kwargs
        )
        super(VirtualNodeTcpConnectionPool, self).__init__(**processed_kwargs)


class VirtualNodeConnectionPool(troposphere.appmesh.VirtualNodeConnectionPool, Mixin):
    def __init__(self,
                 title=None,
                 GRPC=NOTHING, # type: _VirtualNodeGrpcConnectionPool
                 HTTP=NOTHING, # type: _VirtualNodeHttpConnectionPool
                 HTTP2=NOTHING, # type: _VirtualNodeHttp2ConnectionPool
                 TCP=NOTHING, # type: _VirtualNodeTcpConnectionPool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GRPC=GRPC,
            HTTP=HTTP,
            HTTP2=HTTP2,
            TCP=TCP,
            **kwargs
        )
        super(VirtualNodeConnectionPool, self).__init__(**processed_kwargs)


class Listener(troposphere.appmesh.Listener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 ConnectionPool=NOTHING, # type: _VirtualNodeConnectionPool
                 HealthCheck=NOTHING, # type: _HealthCheck
                 OutlierDetection=NOTHING, # type: _OutlierDetection
                 TLS=NOTHING, # type: _ListenerTls
                 Timeout=NOTHING, # type: _ListenerTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            ConnectionPool=ConnectionPool,
            HealthCheck=HealthCheck,
            OutlierDetection=OutlierDetection,
            TLS=TLS,
            Timeout=Timeout,
            **kwargs
        )
        super(Listener, self).__init__(**processed_kwargs)


class FileAccessLog(troposphere.appmesh.FileAccessLog, Mixin):
    def __init__(self,
                 title=None,
                 Path=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Path=Path,
            **kwargs
        )
        super(FileAccessLog, self).__init__(**processed_kwargs)


class AccessLog(troposphere.appmesh.AccessLog, Mixin):
    def __init__(self,
                 title=None,
                 File=NOTHING, # type: _FileAccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            File=File,
            **kwargs
        )
        super(AccessLog, self).__init__(**processed_kwargs)


class Logging(troposphere.appmesh.Logging, Mixin):
    def __init__(self,
                 title=None,
                 AccessLog=NOTHING, # type: _AccessLog
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AccessLog=AccessLog,
            **kwargs
        )
        super(Logging, self).__init__(**processed_kwargs)


class AwsCloudMapInstanceAttribute(troposphere.appmesh.AwsCloudMapInstanceAttribute, Mixin):
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
        super(AwsCloudMapInstanceAttribute, self).__init__(**processed_kwargs)


class AwsCloudMapServiceDiscovery(troposphere.appmesh.AwsCloudMapServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 NamespaceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Attributes=NOTHING, # type: List[_AwsCloudMapInstanceAttribute]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NamespaceName=NamespaceName,
            ServiceName=ServiceName,
            Attributes=Attributes,
            **kwargs
        )
        super(AwsCloudMapServiceDiscovery, self).__init__(**processed_kwargs)


class DnsServiceDiscovery(troposphere.appmesh.DnsServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 Hostname=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Hostname=Hostname,
            **kwargs
        )
        super(DnsServiceDiscovery, self).__init__(**processed_kwargs)


class ServiceDiscovery(troposphere.appmesh.ServiceDiscovery, Mixin):
    def __init__(self,
                 title=None,
                 AWSCloudMap=NOTHING, # type: _AwsCloudMapServiceDiscovery
                 DNS=NOTHING, # type: _DnsServiceDiscovery
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AWSCloudMap=AWSCloudMap,
            DNS=DNS,
            **kwargs
        )
        super(ServiceDiscovery, self).__init__(**processed_kwargs)


class VirtualNodeSpec(troposphere.appmesh.VirtualNodeSpec, Mixin):
    def __init__(self,
                 title=None,
                 BackendDefaults=NOTHING, # type: _BackendDefaults
                 Backends=NOTHING, # type: List[_Backend]
                 Listeners=NOTHING, # type: List[_Listener]
                 Logging=NOTHING, # type: _Logging
                 ServiceDiscovery=NOTHING, # type: _ServiceDiscovery
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BackendDefaults=BackendDefaults,
            Backends=Backends,
            Listeners=Listeners,
            Logging=Logging,
            ServiceDiscovery=ServiceDiscovery,
            **kwargs
        )
        super(VirtualNodeSpec, self).__init__(**processed_kwargs)


class VirtualNode(troposphere.appmesh.VirtualNode, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualNodeSpec
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VirtualNodeName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            MeshOwner=MeshOwner,
            Tags=Tags,
            VirtualNodeName=VirtualNodeName,
            **kwargs
        )
        super(VirtualNode, self).__init__(**processed_kwargs)


class VirtualRouterListener(troposphere.appmesh.VirtualRouterListener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            **kwargs
        )
        super(VirtualRouterListener, self).__init__(**processed_kwargs)


class VirtualRouterSpec(troposphere.appmesh.VirtualRouterSpec, Mixin):
    def __init__(self,
                 title=None,
                 Listeners=REQUIRED, # type: List[_VirtualRouterListener]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Listeners=Listeners,
            **kwargs
        )
        super(VirtualRouterSpec, self).__init__(**processed_kwargs)


class VirtualRouter(troposphere.appmesh.VirtualRouter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualRouterSpec
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VirtualRouterName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            MeshOwner=MeshOwner,
            Tags=Tags,
            VirtualRouterName=VirtualRouterName,
            **kwargs
        )
        super(VirtualRouter, self).__init__(**processed_kwargs)


class VirtualNodeServiceProvider(troposphere.appmesh.VirtualNodeServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNodeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNodeName=VirtualNodeName,
            **kwargs
        )
        super(VirtualNodeServiceProvider, self).__init__(**processed_kwargs)


class VirtualRouterServiceProvider(troposphere.appmesh.VirtualRouterServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualRouterName=VirtualRouterName,
            **kwargs
        )
        super(VirtualRouterServiceProvider, self).__init__(**processed_kwargs)


class VirtualServiceProvider(troposphere.appmesh.VirtualServiceProvider, Mixin):
    def __init__(self,
                 title=None,
                 VirtualNode=NOTHING, # type: _VirtualNodeServiceProvider
                 VirtualRouter=NOTHING, # type: _VirtualRouterServiceProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VirtualNode=VirtualNode,
            VirtualRouter=VirtualRouter,
            **kwargs
        )
        super(VirtualServiceProvider, self).__init__(**processed_kwargs)


class VirtualServiceSpec(troposphere.appmesh.VirtualServiceSpec, Mixin):
    def __init__(self,
                 title=None,
                 Provider=NOTHING, # type: _VirtualServiceProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Provider=Provider,
            **kwargs
        )
        super(VirtualServiceSpec, self).__init__(**processed_kwargs)


class VirtualService(troposphere.appmesh.VirtualService, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _VirtualServiceSpec
                 VirtualServiceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualServiceName=VirtualServiceName,
            MeshOwner=MeshOwner,
            Tags=Tags,
            **kwargs
        )
        super(VirtualService, self).__init__(**processed_kwargs)
