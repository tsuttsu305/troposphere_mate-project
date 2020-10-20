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
    DnsServiceDiscovery as _DnsServiceDiscovery,
    Duration as _Duration,
    EgressFilter as _EgressFilter,
    FileAccessLog as _FileAccessLog,
    GatewayGrpcRoute as _GatewayGrpcRoute,
    GatewayGrpcRouteAction as _GatewayGrpcRouteAction,
    GatewayGrpcRouteMatch as _GatewayGrpcRouteMatch,
    GatewayHttpRoute as _GatewayHttpRoute,
    GatewayHttpRouteAction as _GatewayHttpRouteAction,
    GatewayHttpRouteMatch as _GatewayHttpRouteMatch,
    GatewayRouteSpec as _GatewayRouteSpec,
    GatewayRouteTarget as _GatewayRouteTarget,
    GatewayRouteVirtualService as _GatewayRouteVirtualService,
    GrpcRetryPolicy as _GrpcRetryPolicy,
    GrpcRoute as _GrpcRoute,
    GrpcRouteAction as _GrpcRouteAction,
    GrpcRouteMatch as _GrpcRouteMatch,
    GrpcRouteMetadata as _GrpcRouteMetadata,
    GrpcRouteMetadataMatchMethod as _GrpcRouteMetadataMatchMethod,
    GrpcTimeout as _GrpcTimeout,
    HeaderMatchMethod as _HeaderMatchMethod,
    HealthCheck as _HealthCheck,
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
    Logging as _Logging,
    MatchRange as _MatchRange,
    MeshSpec as _MeshSpec,
    PortMapping as _PortMapping,
    RouteSpec as _RouteSpec,
    ServiceDiscovery as _ServiceDiscovery,
    Tags as _Tags,
    TcpRoute as _TcpRoute,
    TcpRouteAction as _TcpRouteAction,
    TcpTimeout as _TcpTimeout,
    TlsValidationContext as _TlsValidationContext,
    TlsValidationContextAcmTrust as _TlsValidationContextAcmTrust,
    TlsValidationContextFileTrust as _TlsValidationContextFileTrust,
    TlsValidationContextTrust as _TlsValidationContextTrust,
    VirtualGatewayListener as _VirtualGatewayListener,
    VirtualGatewaySpec as _VirtualGatewaySpec,
    VirtualNodeServiceProvider as _VirtualNodeServiceProvider,
    VirtualNodeSpec as _VirtualNodeSpec,
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
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
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
                 RouteName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _RouteSpec
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            RouteName=RouteName,
            Spec=Spec,
            VirtualRouterName=VirtualRouterName,
            MeshOwner=MeshOwner,
            Tags=Tags,
            **kwargs
        )
        super(Route, self).__init__(**processed_kwargs)


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


class TlsValidationContextTrust(troposphere.appmesh.TlsValidationContextTrust, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _TlsValidationContextAcmTrust
                 File=NOTHING, # type: _TlsValidationContextFileTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            **kwargs
        )
        super(TlsValidationContextTrust, self).__init__(**processed_kwargs)


class TlsValidationContext(troposphere.appmesh.TlsValidationContext, Mixin):
    def __init__(self,
                 title=None,
                 Trust=REQUIRED, # type: _TlsValidationContextTrust
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Trust=Trust,
            **kwargs
        )
        super(TlsValidationContext, self).__init__(**processed_kwargs)


class ClientPolicyTls(troposphere.appmesh.ClientPolicyTls, Mixin):
    def __init__(self,
                 title=None,
                 Validation=REQUIRED, # type: _TlsValidationContext
                 Enforce=NOTHING, # type: bool
                 Ports=NOTHING, # type: List[_integer]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Validation=Validation,
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


class ListenerTlsCertificate(troposphere.appmesh.ListenerTlsCertificate, Mixin):
    def __init__(self,
                 title=None,
                 ACM=NOTHING, # type: _ListenerTlsAcmCertificate
                 File=NOTHING, # type: _ListenerTlsFileCertificate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ACM=ACM,
            File=File,
            **kwargs
        )
        super(ListenerTlsCertificate, self).__init__(**processed_kwargs)


class ListenerTls(troposphere.appmesh.ListenerTls, Mixin):
    def __init__(self,
                 title=None,
                 Certificate=REQUIRED, # type: _ListenerTlsCertificate
                 Mode=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Certificate=Certificate,
            Mode=Mode,
            **kwargs
        )
        super(ListenerTls, self).__init__(**processed_kwargs)


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


class Listener(troposphere.appmesh.Listener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 HealthCheck=NOTHING, # type: _HealthCheck
                 TLS=NOTHING, # type: _ListenerTls
                 Timeout=NOTHING, # type: _ListenerTimeout
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            HealthCheck=HealthCheck,
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
                 VirtualNodeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualNodeName=VirtualNodeName,
            MeshOwner=MeshOwner,
            Tags=Tags,
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
                 VirtualRouterName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
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
            Tags=Tags,
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


class VirtualGatewayListener(troposphere.appmesh.VirtualGatewayListener, Mixin):
    def __init__(self,
                 title=None,
                 PortMapping=REQUIRED, # type: _PortMapping
                 HealthCheck=NOTHING, # type: _HealthCheck
                 TLS=NOTHING, # type: _ListenerTls
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PortMapping=PortMapping,
            HealthCheck=HealthCheck,
            TLS=TLS,
            **kwargs
        )
        super(VirtualGatewayListener, self).__init__(**processed_kwargs)


class VirtualGatewaySpec(troposphere.appmesh.VirtualGatewaySpec, Mixin):
    def __init__(self,
                 title=None,
                 Listeners=REQUIRED, # type: List[_VirtualGatewayListener]
                 BackendDefaults=NOTHING, # type: _BackendDefaults
                 Logging=NOTHING, # type: _Logging
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
                 VirtualGatewayName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: List[_Tags]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MeshName=MeshName,
            Spec=Spec,
            VirtualGatewayName=VirtualGatewayName,
            MeshOwner=MeshOwner,
            Tags=Tags,
            **kwargs
        )
        super(VirtualGateway, self).__init__(**processed_kwargs)


class GatewayHttpRouteMatch(troposphere.appmesh.GatewayHttpRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 Prefix=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Prefix=Prefix,
            **kwargs
        )
        super(GatewayHttpRouteMatch, self).__init__(**processed_kwargs)


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


class GatewayHttpRouteAction(troposphere.appmesh.GatewayHttpRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 Target=REQUIRED, # type: _GatewayRouteTarget
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Target=Target,
            **kwargs
        )
        super(GatewayHttpRouteAction, self).__init__(**processed_kwargs)


class GatewayHttpRoute(troposphere.appmesh.GatewayHttpRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _GatewayHttpRouteAction
                 Match=REQUIRED, # type: _GatewayHttpRouteMatch
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            **kwargs
        )
        super(GatewayHttpRoute, self).__init__(**processed_kwargs)


class GatewayGrpcRouteMatch(troposphere.appmesh.GatewayGrpcRouteMatch, Mixin):
    def __init__(self,
                 title=None,
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceName=ServiceName,
            **kwargs
        )
        super(GatewayGrpcRouteMatch, self).__init__(**processed_kwargs)


class GatewayGrpcRouteAction(troposphere.appmesh.GatewayGrpcRouteAction, Mixin):
    def __init__(self,
                 title=None,
                 WeightedTargets=REQUIRED, # type: _GatewayRouteTarget
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            WeightedTargets=WeightedTargets,
            **kwargs
        )
        super(GatewayGrpcRouteAction, self).__init__(**processed_kwargs)


class GatewayGrpcRoute(troposphere.appmesh.GatewayGrpcRoute, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _GatewayGrpcRouteAction
                 Match=REQUIRED, # type: _GatewayGrpcRouteMatch
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Match=Match,
            **kwargs
        )
        super(GatewayGrpcRoute, self).__init__(**processed_kwargs)


class GatewayRouteSpec(troposphere.appmesh.GatewayRouteSpec, Mixin):
    def __init__(self,
                 title=None,
                 GrpcRoute=NOTHING, # type: _GatewayGrpcRoute
                 Http2Route=NOTHING, # type: _GatewayHttpRoute
                 HttpRoute=NOTHING, # type: _GatewayHttpRoute
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
                 GatewayRouteName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Spec=REQUIRED, # type: _GatewayRouteSpec
                 VirtualGatewayName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MeshOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: List[_Tags]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GatewayRouteName=GatewayRouteName,
            MeshName=MeshName,
            Spec=Spec,
            VirtualGatewayName=VirtualGatewayName,
            MeshOwner=MeshOwner,
            Tags=Tags,
            **kwargs
        )
        super(GatewayRoute, self).__init__(**processed_kwargs)
