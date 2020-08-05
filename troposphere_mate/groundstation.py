# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.groundstation

from troposphere.groundstation import (
    AntennaDownlinkConfig as _AntennaDownlinkConfig,
    AntennaDownlinkDemodDecodeConfig as _AntennaDownlinkDemodDecodeConfig,
    AntennaUplinkConfig as _AntennaUplinkConfig,
    Bandwidth as _Bandwidth,
    ConfigData as _ConfigData,
    DataflowEdge as _DataflowEdge,
    DataflowEndpoint as _DataflowEndpoint,
    DataflowEndpointConfig as _DataflowEndpointConfig,
    DecodeConfig as _DecodeConfig,
    DemodulationConfig as _DemodulationConfig,
    Eirp as _Eirp,
    EndpointDetails as _EndpointDetails,
    Frequency as _Frequency,
    SecurityDetails as _SecurityDetails,
    SocketAddress as _SocketAddress,
    SpectrumConfig as _SpectrumConfig,
    Tags as _Tags,
    TrackingConfig as _TrackingConfig,
    UplinkEchoConfig as _UplinkEchoConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DataflowEdge(troposphere.groundstation.DataflowEdge, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: Union[str, AWSHelperFn]
                 Source=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            Source=Source,
            **kwargs
        )
        super(DataflowEdge, self).__init__(**processed_kwargs)


class MissionProfile(troposphere.groundstation.MissionProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DataflowEdges=REQUIRED, # type: List[_DataflowEdge]
                 MinimumViableContactDurationSeconds=REQUIRED, # type: int
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 TrackingConfigArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ContactPostPassDurationSeconds=NOTHING, # type: int
                 ContactPrePassDurationSeconds=NOTHING, # type: int
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DataflowEdges=DataflowEdges,
            MinimumViableContactDurationSeconds=MinimumViableContactDurationSeconds,
            Name=Name,
            TrackingConfigArn=TrackingConfigArn,
            ContactPostPassDurationSeconds=ContactPostPassDurationSeconds,
            ContactPrePassDurationSeconds=ContactPrePassDurationSeconds,
            Tags=Tags,
            **kwargs
        )
        super(MissionProfile, self).__init__(**processed_kwargs)


class SocketAddress(troposphere.groundstation.SocketAddress, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Port=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Port=Port,
            **kwargs
        )
        super(SocketAddress, self).__init__(**processed_kwargs)


class DataflowEndpoint(troposphere.groundstation.DataflowEndpoint, Mixin):
    def __init__(self,
                 title=None,
                 Address=NOTHING, # type: _SocketAddress
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Address=Address,
            Name=Name,
            **kwargs
        )
        super(DataflowEndpoint, self).__init__(**processed_kwargs)


class SecurityDetails(troposphere.groundstation.SecurityDetails, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 SecurityGroupIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(SecurityDetails, self).__init__(**processed_kwargs)


class EndpointDetails(troposphere.groundstation.EndpointDetails, Mixin):
    def __init__(self,
                 title=None,
                 DataflowEndpoint=NOTHING, # type: _DataflowEndpoint
                 SecurityDetails=NOTHING, # type: _SecurityDetails
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataflowEndpoint=DataflowEndpoint,
            SecurityDetails=SecurityDetails,
            **kwargs
        )
        super(EndpointDetails, self).__init__(**processed_kwargs)


class DecodeConfig(troposphere.groundstation.DecodeConfig, Mixin):
    def __init__(self,
                 title=None,
                 UnvalidatedJSON=REQUIRED, # type: json_checker
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            UnvalidatedJSON=UnvalidatedJSON,
            **kwargs
        )
        super(DecodeConfig, self).__init__(**processed_kwargs)


class DemodulationConfig(troposphere.groundstation.DemodulationConfig, Mixin):
    def __init__(self,
                 title=None,
                 UnvalidatedJSON=REQUIRED, # type: json_checker
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            UnvalidatedJSON=UnvalidatedJSON,
            **kwargs
        )
        super(DemodulationConfig, self).__init__(**processed_kwargs)


class Bandwidth(troposphere.groundstation.Bandwidth, Mixin):
    def __init__(self,
                 title=None,
                 Units=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Units=Units,
            Value=Value,
            **kwargs
        )
        super(Bandwidth, self).__init__(**processed_kwargs)


class Frequency(troposphere.groundstation.Frequency, Mixin):
    def __init__(self,
                 title=None,
                 Units=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Units=Units,
            Value=Value,
            **kwargs
        )
        super(Frequency, self).__init__(**processed_kwargs)


class SpectrumConfig(troposphere.groundstation.SpectrumConfig, Mixin):
    def __init__(self,
                 title=None,
                 Bandwidth=REQUIRED, # type: _Bandwidth
                 CenterFrequency=REQUIRED, # type: _Frequency
                 Polarization=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bandwidth=Bandwidth,
            CenterFrequency=CenterFrequency,
            Polarization=Polarization,
            **kwargs
        )
        super(SpectrumConfig, self).__init__(**processed_kwargs)


class AntennaDownlinkConfig(troposphere.groundstation.AntennaDownlinkConfig, Mixin):
    def __init__(self,
                 title=None,
                 SpectrumConfig=REQUIRED, # type: _SpectrumConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SpectrumConfig=SpectrumConfig,
            **kwargs
        )
        super(AntennaDownlinkConfig, self).__init__(**processed_kwargs)


class AntennaDownlinkDemodDecodeConfig(troposphere.groundstation.AntennaDownlinkDemodDecodeConfig, Mixin):
    def __init__(self,
                 title=None,
                 DecodeConfig=REQUIRED, # type: _DecodeConfig
                 DemodulationConfig=REQUIRED, # type: _DemodulationConfig
                 SpectrumConfig=REQUIRED, # type: _SpectrumConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DecodeConfig=DecodeConfig,
            DemodulationConfig=DemodulationConfig,
            SpectrumConfig=SpectrumConfig,
            **kwargs
        )
        super(AntennaDownlinkDemodDecodeConfig, self).__init__(**processed_kwargs)


class SpectrumConfig(troposphere.groundstation.SpectrumConfig, Mixin):
    def __init__(self,
                 title=None,
                 Bandwidth=REQUIRED, # type: _Bandwidth
                 CenterFrequency=REQUIRED, # type: _Frequency
                 Polarization=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bandwidth=Bandwidth,
            CenterFrequency=CenterFrequency,
            Polarization=Polarization,
            **kwargs
        )
        super(SpectrumConfig, self).__init__(**processed_kwargs)


class DataflowEndpointGroup(troposphere.groundstation.DataflowEndpointGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 EndpointDetailsList=REQUIRED, # type: List[_EndpointDetails]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            EndpointDetailsList=EndpointDetailsList,
            Tags=Tags,
            **kwargs
        )
        super(DataflowEndpointGroup, self).__init__(**processed_kwargs)


class Eirp(troposphere.groundstation.Eirp, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Units=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Units=Units,
            Value=Value,
            **kwargs
        )
        super(Eirp, self).__init__(**processed_kwargs)


class AntennaUplinkConfig(troposphere.groundstation.AntennaUplinkConfig, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SpectrumConfig=REQUIRED, # type: _SpectrumConfig
                 TargetEirp=REQUIRED, # type: _Eirp
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SpectrumConfig=SpectrumConfig,
            TargetEirp=TargetEirp,
            **kwargs
        )
        super(AntennaUplinkConfig, self).__init__(**processed_kwargs)


class DataflowEndpointConfig(troposphere.groundstation.DataflowEndpointConfig, Mixin):
    def __init__(self,
                 title=None,
                 DataflowEndpointName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataflowEndpointRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataflowEndpointName=DataflowEndpointName,
            DataflowEndpointRegion=DataflowEndpointRegion,
            **kwargs
        )
        super(DataflowEndpointConfig, self).__init__(**processed_kwargs)


class TrackingConfig(troposphere.groundstation.TrackingConfig, Mixin):
    def __init__(self,
                 title=None,
                 AutoTrack=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutoTrack=AutoTrack,
            **kwargs
        )
        super(TrackingConfig, self).__init__(**processed_kwargs)


class UplinkEchoConfig(troposphere.groundstation.UplinkEchoConfig, Mixin):
    def __init__(self,
                 title=None,
                 AntennaUplinkConfigArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Enabled=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AntennaUplinkConfigArn=AntennaUplinkConfigArn,
            Enabled=Enabled,
            **kwargs
        )
        super(UplinkEchoConfig, self).__init__(**processed_kwargs)


class ConfigData(troposphere.groundstation.ConfigData, Mixin):
    def __init__(self,
                 title=None,
                 AntennaDownlinkConfig=NOTHING, # type: _AntennaDownlinkConfig
                 AntennaDownlinkDemodDecodeConfig=NOTHING, # type: _AntennaDownlinkDemodDecodeConfig
                 AntennaUplinkConfig=NOTHING, # type: _AntennaUplinkConfig
                 DataflowEndpointConfig=NOTHING, # type: _DataflowEndpointConfig
                 TrackingConfig=NOTHING, # type: _TrackingConfig
                 UplinkEchoConfig=NOTHING, # type: _UplinkEchoConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AntennaDownlinkConfig=AntennaDownlinkConfig,
            AntennaDownlinkDemodDecodeConfig=AntennaDownlinkDemodDecodeConfig,
            AntennaUplinkConfig=AntennaUplinkConfig,
            DataflowEndpointConfig=DataflowEndpointConfig,
            TrackingConfig=TrackingConfig,
            UplinkEchoConfig=UplinkEchoConfig,
            **kwargs
        )
        super(ConfigData, self).__init__(**processed_kwargs)


class Config(troposphere.groundstation.Config, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConfigData=REQUIRED, # type: _ConfigData
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConfigData=ConfigData,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Config, self).__init__(**processed_kwargs)
