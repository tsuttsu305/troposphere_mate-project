# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iotwireless

from troposphere.iotwireless import (
    AbpV10x as _AbpV10x,
    AbpV11 as _AbpV11,
    LoRaWANDevice as _LoRaWANDevice,
    LoRaWANDeviceProfile as _LoRaWANDeviceProfile,
    LoRaWANGateway as _LoRaWANGateway,
    LoRaWANServiceProfile as _LoRaWANServiceProfile,
    OtaaV10x as _OtaaV10x,
    OtaaV11 as _OtaaV11,
    SessionKeysAbpV10x as _SessionKeysAbpV10x,
    SessionKeysAbpV11 as _SessionKeysAbpV11,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Destination(troposphere.iotwireless.Destination, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Expression=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExpressionType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Expression=Expression,
            ExpressionType=ExpressionType,
            Name=Name,
            RoleArn=RoleArn,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Destination, self).__init__(**processed_kwargs)


class LoRaWANDeviceProfile(troposphere.iotwireless.LoRaWANDeviceProfile, Mixin):
    def __init__(self,
                 title=None,
                 ClassBTimeout=NOTHING, # type: int
                 ClassCTimeout=NOTHING, # type: int
                 MacVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxDutyCycle=NOTHING, # type: int
                 MaxEirp=NOTHING, # type: int
                 PingSlotDr=NOTHING, # type: int
                 PingSlotFreq=NOTHING, # type: int
                 PingSlotPeriod=NOTHING, # type: int
                 RegParamsRevision=NOTHING, # type: Union[str, AWSHelperFn]
                 RfRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 Supports32BitFCnt=NOTHING, # type: bool
                 SupportsClassB=NOTHING, # type: bool
                 SupportsClassC=NOTHING, # type: bool
                 SupportsJoin=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ClassBTimeout=ClassBTimeout,
            ClassCTimeout=ClassCTimeout,
            MacVersion=MacVersion,
            MaxDutyCycle=MaxDutyCycle,
            MaxEirp=MaxEirp,
            PingSlotDr=PingSlotDr,
            PingSlotFreq=PingSlotFreq,
            PingSlotPeriod=PingSlotPeriod,
            RegParamsRevision=RegParamsRevision,
            RfRegion=RfRegion,
            Supports32BitFCnt=Supports32BitFCnt,
            SupportsClassB=SupportsClassB,
            SupportsClassC=SupportsClassC,
            SupportsJoin=SupportsJoin,
            **kwargs
        )
        super(LoRaWANDeviceProfile, self).__init__(**processed_kwargs)


class DeviceProfile(troposphere.iotwireless.DeviceProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LoRaWAN=NOTHING, # type: _LoRaWANDeviceProfile
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LoRaWAN=LoRaWAN,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(DeviceProfile, self).__init__(**processed_kwargs)


class LoRaWANServiceProfile(troposphere.iotwireless.LoRaWANServiceProfile, Mixin):
    def __init__(self,
                 title=None,
                 AddGwMetadata=NOTHING, # type: bool
                 ChannelMask=NOTHING, # type: Union[str, AWSHelperFn]
                 DevStatusReqFreq=NOTHING, # type: int
                 DlBucketSize=NOTHING, # type: int
                 DlRate=NOTHING, # type: int
                 DlRatePolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 DrMax=NOTHING, # type: int
                 DrMin=NOTHING, # type: int
                 HrAllowed=NOTHING, # type: bool
                 MinGwDiversity=NOTHING, # type: int
                 NwkGeoLoc=NOTHING, # type: bool
                 PrAllowed=NOTHING, # type: bool
                 RaAllowed=NOTHING, # type: bool
                 ReportDevStatusBattery=NOTHING, # type: bool
                 ReportDevStatusMargin=NOTHING, # type: bool
                 TargetPer=NOTHING, # type: int
                 UlBucketSize=NOTHING, # type: int
                 UlRate=NOTHING, # type: int
                 UlRatePolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddGwMetadata=AddGwMetadata,
            ChannelMask=ChannelMask,
            DevStatusReqFreq=DevStatusReqFreq,
            DlBucketSize=DlBucketSize,
            DlRate=DlRate,
            DlRatePolicy=DlRatePolicy,
            DrMax=DrMax,
            DrMin=DrMin,
            HrAllowed=HrAllowed,
            MinGwDiversity=MinGwDiversity,
            NwkGeoLoc=NwkGeoLoc,
            PrAllowed=PrAllowed,
            RaAllowed=RaAllowed,
            ReportDevStatusBattery=ReportDevStatusBattery,
            ReportDevStatusMargin=ReportDevStatusMargin,
            TargetPer=TargetPer,
            UlBucketSize=UlBucketSize,
            UlRate=UlRate,
            UlRatePolicy=UlRatePolicy,
            **kwargs
        )
        super(LoRaWANServiceProfile, self).__init__(**processed_kwargs)


class ServiceProfile(troposphere.iotwireless.ServiceProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LoRaWAN=NOTHING, # type: _LoRaWANServiceProfile
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LoRaWAN=LoRaWAN,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(ServiceProfile, self).__init__(**processed_kwargs)


class SessionKeysAbpV10x(troposphere.iotwireless.SessionKeysAbpV10x, Mixin):
    def __init__(self,
                 title=None,
                 AppSKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 NwkSKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppSKey=AppSKey,
            NwkSKey=NwkSKey,
            **kwargs
        )
        super(SessionKeysAbpV10x, self).__init__(**processed_kwargs)


class AbpV10x(troposphere.iotwireless.AbpV10x, Mixin):
    def __init__(self,
                 title=None,
                 DevAddr=REQUIRED, # type: Union[str, AWSHelperFn]
                 SessionKeys=REQUIRED, # type: _SessionKeysAbpV10x
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DevAddr=DevAddr,
            SessionKeys=SessionKeys,
            **kwargs
        )
        super(AbpV10x, self).__init__(**processed_kwargs)


class SessionKeysAbpV11(troposphere.iotwireless.SessionKeysAbpV11, Mixin):
    def __init__(self,
                 title=None,
                 AppSKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 FNwkSIntKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 NwkSEncKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 SNwkSIntKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppSKey=AppSKey,
            FNwkSIntKey=FNwkSIntKey,
            NwkSEncKey=NwkSEncKey,
            SNwkSIntKey=SNwkSIntKey,
            **kwargs
        )
        super(SessionKeysAbpV11, self).__init__(**processed_kwargs)


class AbpV11(troposphere.iotwireless.AbpV11, Mixin):
    def __init__(self,
                 title=None,
                 DevAddr=REQUIRED, # type: Union[str, AWSHelperFn]
                 SessionKeys=REQUIRED, # type: _SessionKeysAbpV11
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DevAddr=DevAddr,
            SessionKeys=SessionKeys,
            **kwargs
        )
        super(AbpV11, self).__init__(**processed_kwargs)


class OtaaV10x(troposphere.iotwireless.OtaaV10x, Mixin):
    def __init__(self,
                 title=None,
                 AppEui=REQUIRED, # type: Union[str, AWSHelperFn]
                 AppKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppEui=AppEui,
            AppKey=AppKey,
            **kwargs
        )
        super(OtaaV10x, self).__init__(**processed_kwargs)


class OtaaV11(troposphere.iotwireless.OtaaV11, Mixin):
    def __init__(self,
                 title=None,
                 AppKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 JoinEui=REQUIRED, # type: Union[str, AWSHelperFn]
                 NwkKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AppKey=AppKey,
            JoinEui=JoinEui,
            NwkKey=NwkKey,
            **kwargs
        )
        super(OtaaV11, self).__init__(**processed_kwargs)


class LoRaWANDevice(troposphere.iotwireless.LoRaWANDevice, Mixin):
    def __init__(self,
                 title=None,
                 AbpV10x=NOTHING, # type: _AbpV10x
                 AbpV11=NOTHING, # type: _AbpV11
                 DevEui=NOTHING, # type: Union[str, AWSHelperFn]
                 DeviceProfileId=NOTHING, # type: Union[str, AWSHelperFn]
                 OtaaV10x=NOTHING, # type: _OtaaV10x
                 OtaaV11=NOTHING, # type: _OtaaV11
                 ServiceProfileId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AbpV10x=AbpV10x,
            AbpV11=AbpV11,
            DevEui=DevEui,
            DeviceProfileId=DeviceProfileId,
            OtaaV10x=OtaaV10x,
            OtaaV11=OtaaV11,
            ServiceProfileId=ServiceProfileId,
            **kwargs
        )
        super(LoRaWANDevice, self).__init__(**processed_kwargs)


class WirelessDevice(troposphere.iotwireless.WirelessDevice, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DestinationName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LastUplinkReceivedAt=NOTHING, # type: Union[str, AWSHelperFn]
                 LoRaWAN=NOTHING, # type: _LoRaWANDevice
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 ThingArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DestinationName=DestinationName,
            Type=Type,
            Description=Description,
            LastUplinkReceivedAt=LastUplinkReceivedAt,
            LoRaWAN=LoRaWAN,
            Name=Name,
            Tags=Tags,
            ThingArn=ThingArn,
            **kwargs
        )
        super(WirelessDevice, self).__init__(**processed_kwargs)


class LoRaWANGateway(troposphere.iotwireless.LoRaWANGateway, Mixin):
    def __init__(self,
                 title=None,
                 GatewayEui=REQUIRED, # type: Union[str, AWSHelperFn]
                 RfRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GatewayEui=GatewayEui,
            RfRegion=RfRegion,
            **kwargs
        )
        super(LoRaWANGateway, self).__init__(**processed_kwargs)


class WirelessGateway(troposphere.iotwireless.WirelessGateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 LoRaWAN=REQUIRED, # type: _LoRaWANGateway
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 LastUplinkReceivedAt=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 ThingArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            LoRaWAN=LoRaWAN,
            Description=Description,
            LastUplinkReceivedAt=LastUplinkReceivedAt,
            Name=Name,
            Tags=Tags,
            ThingArn=ThingArn,
            **kwargs
        )
        super(WirelessGateway, self).__init__(**processed_kwargs)
