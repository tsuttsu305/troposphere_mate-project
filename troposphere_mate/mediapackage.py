# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.mediapackage

from troposphere.mediapackage import (
    Authorization as _Authorization,
    CmafEncryption as _CmafEncryption,
    CmafPackage as _CmafPackage,
    DashEncryption as _DashEncryption,
    DashManifest as _DashManifest,
    DashPackage as _DashPackage,
    EgressEndpoint as _EgressEndpoint,
    HlsEncryption as _HlsEncryption,
    HlsManifest as _HlsManifest,
    HlsPackage as _HlsPackage,
    MssEncryption as _MssEncryption,
    MssManifest as _MssManifest,
    MssPackage as _MssPackage,
    SpekeKeyProvider as _SpekeKeyProvider,
    StreamSelection as _StreamSelection,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class EgressEndpoint(troposphere.mediapackage.EgressEndpoint, Mixin):
    def __init__(self,
                 title=None,
                 PackagingConfigurationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Url=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PackagingConfigurationId=PackagingConfigurationId,
            Url=Url,
            **kwargs
        )
        super(EgressEndpoint, self).__init__(**processed_kwargs)


class Asset(troposphere.mediapackage.Asset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 PackagingGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 EgressEndpoints=NOTHING, # type: List[_EgressEndpoint]
                 ResourceId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Id=Id,
            PackagingGroupId=PackagingGroupId,
            SourceArn=SourceArn,
            SourceRoleArn=SourceRoleArn,
            EgressEndpoints=EgressEndpoints,
            ResourceId=ResourceId,
            Tags=Tags,
            **kwargs
        )
        super(Asset, self).__init__(**processed_kwargs)


class Channel(troposphere.mediapackage.Channel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Id=Id,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class Authorization(troposphere.mediapackage.Authorization, Mixin):
    def __init__(self,
                 title=None,
                 CdnIdentifierSecret=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecretsRoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CdnIdentifierSecret=CdnIdentifierSecret,
            SecretsRoleArn=SecretsRoleArn,
            **kwargs
        )
        super(Authorization, self).__init__(**processed_kwargs)


class SpekeKeyProvider(troposphere.mediapackage.SpekeKeyProvider, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SystemIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Url=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            SystemIds=SystemIds,
            Url=Url,
            **kwargs
        )
        super(SpekeKeyProvider, self).__init__(**processed_kwargs)


class CmafEncryption(troposphere.mediapackage.CmafEncryption, Mixin):
    def __init__(self,
                 title=None,
                 SpekeKeyProvider=REQUIRED, # type: _SpekeKeyProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpekeKeyProvider=SpekeKeyProvider,
            **kwargs
        )
        super(CmafEncryption, self).__init__(**processed_kwargs)


class StreamSelection(troposphere.mediapackage.StreamSelection, Mixin):
    def __init__(self,
                 title=None,
                 MaxVideoBitsPerSecond=NOTHING, # type: int
                 MinVideoBitsPerSecond=NOTHING, # type: int
                 StreamOrder=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxVideoBitsPerSecond=MaxVideoBitsPerSecond,
            MinVideoBitsPerSecond=MinVideoBitsPerSecond,
            StreamOrder=StreamOrder,
            **kwargs
        )
        super(StreamSelection, self).__init__(**processed_kwargs)


class HlsManifest(troposphere.mediapackage.HlsManifest, Mixin):
    def __init__(self,
                 title=None,
                 AdMarkers=NOTHING, # type: Union[str, AWSHelperFn]
                 IncludeIframeOnlyStream=NOTHING, # type: bool
                 ManifestName=NOTHING, # type: Union[str, AWSHelperFn]
                 ProgramDateTimeIntervalSeconds=NOTHING, # type: int
                 RepeatExtXKey=NOTHING, # type: bool
                 StreamSelection=NOTHING, # type: _StreamSelection
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdMarkers=AdMarkers,
            IncludeIframeOnlyStream=IncludeIframeOnlyStream,
            ManifestName=ManifestName,
            ProgramDateTimeIntervalSeconds=ProgramDateTimeIntervalSeconds,
            RepeatExtXKey=RepeatExtXKey,
            StreamSelection=StreamSelection,
            **kwargs
        )
        super(HlsManifest, self).__init__(**processed_kwargs)


class CmafPackage(troposphere.mediapackage.CmafPackage, Mixin):
    def __init__(self,
                 title=None,
                 HlsManifests=REQUIRED, # type: List[_HlsManifest]
                 Encryption=NOTHING, # type: _CmafEncryption
                 SegmentDurationSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HlsManifests=HlsManifests,
            Encryption=Encryption,
            SegmentDurationSeconds=SegmentDurationSeconds,
            **kwargs
        )
        super(CmafPackage, self).__init__(**processed_kwargs)


class DashEncryption(troposphere.mediapackage.DashEncryption, Mixin):
    def __init__(self,
                 title=None,
                 SpekeKeyProvider=REQUIRED, # type: _SpekeKeyProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpekeKeyProvider=SpekeKeyProvider,
            **kwargs
        )
        super(DashEncryption, self).__init__(**processed_kwargs)


class DashManifest(troposphere.mediapackage.DashManifest, Mixin):
    def __init__(self,
                 title=None,
                 ManifestLayout=NOTHING, # type: Union[str, AWSHelperFn]
                 ManifestName=NOTHING, # type: Union[str, AWSHelperFn]
                 MinBufferTimeSeconds=NOTHING, # type: int
                 Profile=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamSelection=NOTHING, # type: _StreamSelection
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ManifestLayout=ManifestLayout,
            ManifestName=ManifestName,
            MinBufferTimeSeconds=MinBufferTimeSeconds,
            Profile=Profile,
            StreamSelection=StreamSelection,
            **kwargs
        )
        super(DashManifest, self).__init__(**processed_kwargs)


class DashPackage(troposphere.mediapackage.DashPackage, Mixin):
    def __init__(self,
                 title=None,
                 DashManifests=REQUIRED, # type: List[_DashManifest]
                 Encryption=NOTHING, # type: _DashEncryption
                 PeriodTriggers=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SegmentDurationSeconds=NOTHING, # type: int
                 SegmentTemplateFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DashManifests=DashManifests,
            Encryption=Encryption,
            PeriodTriggers=PeriodTriggers,
            SegmentDurationSeconds=SegmentDurationSeconds,
            SegmentTemplateFormat=SegmentTemplateFormat,
            **kwargs
        )
        super(DashPackage, self).__init__(**processed_kwargs)


class HlsEncryption(troposphere.mediapackage.HlsEncryption, Mixin):
    def __init__(self,
                 title=None,
                 SpekeKeyProvider=REQUIRED, # type: _SpekeKeyProvider
                 ConstantInitializationVector=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpekeKeyProvider=SpekeKeyProvider,
            ConstantInitializationVector=ConstantInitializationVector,
            EncryptionMethod=EncryptionMethod,
            **kwargs
        )
        super(HlsEncryption, self).__init__(**processed_kwargs)


class HlsPackage(troposphere.mediapackage.HlsPackage, Mixin):
    def __init__(self,
                 title=None,
                 HlsManifests=REQUIRED, # type: List[_HlsManifest]
                 Encryption=NOTHING, # type: _HlsEncryption
                 SegmentDurationSeconds=NOTHING, # type: int
                 UseAudioRenditionGroup=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HlsManifests=HlsManifests,
            Encryption=Encryption,
            SegmentDurationSeconds=SegmentDurationSeconds,
            UseAudioRenditionGroup=UseAudioRenditionGroup,
            **kwargs
        )
        super(HlsPackage, self).__init__(**processed_kwargs)


class MssEncryption(troposphere.mediapackage.MssEncryption, Mixin):
    def __init__(self,
                 title=None,
                 SpekeKeyProvider=REQUIRED, # type: _SpekeKeyProvider
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpekeKeyProvider=SpekeKeyProvider,
            **kwargs
        )
        super(MssEncryption, self).__init__(**processed_kwargs)


class MssManifest(troposphere.mediapackage.MssManifest, Mixin):
    def __init__(self,
                 title=None,
                 ManifestName=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamSelection=NOTHING, # type: _StreamSelection
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ManifestName=ManifestName,
            StreamSelection=StreamSelection,
            **kwargs
        )
        super(MssManifest, self).__init__(**processed_kwargs)


class MssPackage(troposphere.mediapackage.MssPackage, Mixin):
    def __init__(self,
                 title=None,
                 MssManifests=REQUIRED, # type: List[_MssManifest]
                 Encryption=NOTHING, # type: _MssEncryption
                 SegmentDurationSeconds=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MssManifests=MssManifests,
            Encryption=Encryption,
            SegmentDurationSeconds=SegmentDurationSeconds,
            **kwargs
        )
        super(MssPackage, self).__init__(**processed_kwargs)


class OriginEndpoint(troposphere.mediapackage.OriginEndpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ChannelId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Authorization=NOTHING, # type: _Authorization
                 CmafPackage=NOTHING, # type: _CmafPackage
                 DashPackage=NOTHING, # type: _DashPackage
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 HlsPackage=NOTHING, # type: _HlsPackage
                 ManifestName=NOTHING, # type: Union[str, AWSHelperFn]
                 MssPackage=NOTHING, # type: _MssPackage
                 Origination=NOTHING, # type: Union[str, AWSHelperFn]
                 StartoverWindowSeconds=NOTHING, # type: int
                 Tags=NOTHING, # type: _Tags
                 TimeDelaySeconds=NOTHING, # type: int
                 Whitelist=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ChannelId=ChannelId,
            Id=Id,
            Authorization=Authorization,
            CmafPackage=CmafPackage,
            DashPackage=DashPackage,
            Description=Description,
            HlsPackage=HlsPackage,
            ManifestName=ManifestName,
            MssPackage=MssPackage,
            Origination=Origination,
            StartoverWindowSeconds=StartoverWindowSeconds,
            Tags=Tags,
            TimeDelaySeconds=TimeDelaySeconds,
            Whitelist=Whitelist,
            **kwargs
        )
        super(OriginEndpoint, self).__init__(**processed_kwargs)


class PackagingConfiguration(troposphere.mediapackage.PackagingConfiguration, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 PackagingGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 CmafPackage=NOTHING, # type: _CmafPackage
                 DashPackage=NOTHING, # type: _DashPackage
                 HlsPackage=NOTHING, # type: _HlsPackage
                 MssPackage=NOTHING, # type: _MssPackage
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Id=Id,
            PackagingGroupId=PackagingGroupId,
            CmafPackage=CmafPackage,
            DashPackage=DashPackage,
            HlsPackage=HlsPackage,
            MssPackage=MssPackage,
            Tags=Tags,
            **kwargs
        )
        super(PackagingConfiguration, self).__init__(**processed_kwargs)


class PackagingGroup(troposphere.mediapackage.PackagingGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Id=REQUIRED, # type: Union[str, AWSHelperFn]
                 Authorization=NOTHING, # type: _Authorization
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Id=Id,
            Authorization=Authorization,
            Tags=Tags,
            **kwargs
        )
        super(PackagingGroup, self).__init__(**processed_kwargs)
