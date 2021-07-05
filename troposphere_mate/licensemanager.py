# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.licensemanager

from troposphere.licensemanager import (
    BorrowConfiguration as _BorrowConfiguration,
    ConsumptionConfiguration as _ConsumptionConfiguration,
    Entitlement as _Entitlement,
    IssuerData as _IssuerData,
    Metadata as _Metadata,
    ProvisionalConfiguration as _ProvisionalConfiguration,
    ValidityDateFormat as _ValidityDateFormat,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Grant(troposphere.licensemanager.Grant, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AllowedOperations=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 GrantName=NOTHING, # type: Union[str, AWSHelperFn]
                 HomeRegion=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Principals=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AllowedOperations=AllowedOperations,
            GrantName=GrantName,
            HomeRegion=HomeRegion,
            LicenseArn=LicenseArn,
            Principals=Principals,
            Status=Status,
            **kwargs
        )
        super(Grant, self).__init__(**processed_kwargs)


class BorrowConfiguration(troposphere.licensemanager.BorrowConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AllowEarlyCheckIn=REQUIRED, # type: bool
                 MaxTimeToLiveInMinutes=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowEarlyCheckIn=AllowEarlyCheckIn,
            MaxTimeToLiveInMinutes=MaxTimeToLiveInMinutes,
            **kwargs
        )
        super(BorrowConfiguration, self).__init__(**processed_kwargs)


class ProvisionalConfiguration(troposphere.licensemanager.ProvisionalConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 MaxTimeToLiveInMinutes=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            MaxTimeToLiveInMinutes=MaxTimeToLiveInMinutes,
            **kwargs
        )
        super(ProvisionalConfiguration, self).__init__(**processed_kwargs)


class ConsumptionConfiguration(troposphere.licensemanager.ConsumptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BorrowConfiguration=NOTHING, # type: _BorrowConfiguration
                 ProvisionalConfiguration=NOTHING, # type: _ProvisionalConfiguration
                 RenewType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BorrowConfiguration=BorrowConfiguration,
            ProvisionalConfiguration=ProvisionalConfiguration,
            RenewType=RenewType,
            **kwargs
        )
        super(ConsumptionConfiguration, self).__init__(**processed_kwargs)


class Entitlement(troposphere.licensemanager.Entitlement, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Unit=REQUIRED, # type: Union[str, AWSHelperFn]
                 AllowCheckIn=NOTHING, # type: bool
                 MaxCount=NOTHING, # type: int
                 Overage=NOTHING, # type: bool
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Unit=Unit,
            AllowCheckIn=AllowCheckIn,
            MaxCount=MaxCount,
            Overage=Overage,
            Value=Value,
            **kwargs
        )
        super(Entitlement, self).__init__(**processed_kwargs)


class IssuerData(troposphere.licensemanager.IssuerData, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 SignKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            SignKey=SignKey,
            **kwargs
        )
        super(IssuerData, self).__init__(**processed_kwargs)


class Metadata(troposphere.licensemanager.Metadata, Mixin):
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
        super(Metadata, self).__init__(**processed_kwargs)


class ValidityDateFormat(troposphere.licensemanager.ValidityDateFormat, Mixin):
    def __init__(self,
                 title=None,
                 Begin=REQUIRED, # type: Union[str, AWSHelperFn]
                 End=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Begin=Begin,
            End=End,
            **kwargs
        )
        super(ValidityDateFormat, self).__init__(**processed_kwargs)


class License(troposphere.licensemanager.License, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ConsumptionConfiguration=REQUIRED, # type: _ConsumptionConfiguration
                 Entitlements=REQUIRED, # type: List[_Entitlement]
                 HomeRegion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Issuer=REQUIRED, # type: _IssuerData
                 LicenseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProductName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Validity=REQUIRED, # type: _ValidityDateFormat
                 Beneficiary=NOTHING, # type: Union[str, AWSHelperFn]
                 LicenseMetadata=NOTHING, # type: List[_Metadata]
                 ProductSKU=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ConsumptionConfiguration=ConsumptionConfiguration,
            Entitlements=Entitlements,
            HomeRegion=HomeRegion,
            Issuer=Issuer,
            LicenseName=LicenseName,
            ProductName=ProductName,
            Validity=Validity,
            Beneficiary=Beneficiary,
            LicenseMetadata=LicenseMetadata,
            ProductSKU=ProductSKU,
            Status=Status,
            **kwargs
        )
        super(License, self).__init__(**processed_kwargs)
