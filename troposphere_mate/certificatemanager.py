# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.certificatemanager

from troposphere.certificatemanager import (
    DomainValidationOption as _DomainValidationOption,
    ExpiryEventsConfiguration as _ExpiryEventsConfiguration,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ExpiryEventsConfiguration(troposphere.certificatemanager.ExpiryEventsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DaysBeforeExpiry=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DaysBeforeExpiry=DaysBeforeExpiry,
            **kwargs
        )
        super(ExpiryEventsConfiguration, self).__init__(**processed_kwargs)


class Account(troposphere.certificatemanager.Account, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExpiryEventsConfiguration=REQUIRED, # type: _ExpiryEventsConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ExpiryEventsConfiguration=ExpiryEventsConfiguration,
            **kwargs
        )
        super(Account, self).__init__(**processed_kwargs)


class DomainValidationOption(troposphere.certificatemanager.DomainValidationOption, Mixin):
    def __init__(self,
                 title=None,
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 HostedZoneId=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidationDomain=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DomainName=DomainName,
            HostedZoneId=HostedZoneId,
            ValidationDomain=ValidationDomain,
            **kwargs
        )
        super(DomainValidationOption, self).__init__(**processed_kwargs)


class Certificate(troposphere.certificatemanager.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateAuthorityArn=NOTHING, # type: Union[str, AWSHelperFn]
                 CertificateTransparencyLoggingPreference=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainValidationOptions=NOTHING, # type: List[_DomainValidationOption]
                 SubjectAlternativeNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 ValidationMethod=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            CertificateAuthorityArn=CertificateAuthorityArn,
            CertificateTransparencyLoggingPreference=CertificateTransparencyLoggingPreference,
            DomainValidationOptions=DomainValidationOptions,
            SubjectAlternativeNames=SubjectAlternativeNames,
            Tags=Tags,
            ValidationMethod=ValidationMethod,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)
