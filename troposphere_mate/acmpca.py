# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.acmpca

from troposphere.acmpca import (
    CrlConfiguration as _CrlConfiguration,
    RevocationConfiguration as _RevocationConfiguration,
    Subject as _Subject,
    Tags as _Tags,
    Validity as _Validity,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Validity(troposphere.acmpca.Validity, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Any
                 Value=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Value=Value,
            **kwargs
        )
        super(Validity, self).__init__(**processed_kwargs)


class Certificate(troposphere.acmpca.Certificate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CertificateAuthorityArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateSigningRequest=REQUIRED, # type: Union[str, AWSHelperFn]
                 SigningAlgorithm=REQUIRED, # type: Any
                 Validity=REQUIRED, # type: _Validity
                 TemplateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateAuthorityArn=CertificateAuthorityArn,
            CertificateSigningRequest=CertificateSigningRequest,
            SigningAlgorithm=SigningAlgorithm,
            Validity=Validity,
            TemplateArn=TemplateArn,
            **kwargs
        )
        super(Certificate, self).__init__(**processed_kwargs)


class CertificateAuthorityActivation(troposphere.acmpca.CertificateAuthorityActivation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Certificate=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateAuthorityArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CertificateChain=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Certificate=Certificate,
            CertificateAuthorityArn=CertificateAuthorityArn,
            CertificateChain=CertificateChain,
            Status=Status,
            **kwargs
        )
        super(CertificateAuthorityActivation, self).__init__(**processed_kwargs)


class CrlConfiguration(troposphere.acmpca.CrlConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CustomCname=NOTHING, # type: Union[str, AWSHelperFn]
                 Enabled=NOTHING, # type: bool
                 ExpirationInDays=NOTHING, # type: int
                 S3BucketName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CustomCname=CustomCname,
            Enabled=Enabled,
            ExpirationInDays=ExpirationInDays,
            S3BucketName=S3BucketName,
            **kwargs
        )
        super(CrlConfiguration, self).__init__(**processed_kwargs)


class RevocationConfiguration(troposphere.acmpca.RevocationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CrlConfiguration=NOTHING, # type: _CrlConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CrlConfiguration=CrlConfiguration,
            **kwargs
        )
        super(RevocationConfiguration, self).__init__(**processed_kwargs)


class Subject(troposphere.acmpca.Subject, Mixin):
    def __init__(self,
                 title=None,
                 CommonName=NOTHING, # type: Union[str, AWSHelperFn]
                 Country=NOTHING, # type: Union[str, AWSHelperFn]
                 DistinguishedNameQualifier=NOTHING, # type: Union[str, AWSHelperFn]
                 GenerationQualifier=NOTHING, # type: Union[str, AWSHelperFn]
                 GivenName=NOTHING, # type: Union[str, AWSHelperFn]
                 Initials=NOTHING, # type: Union[str, AWSHelperFn]
                 Locality=NOTHING, # type: Union[str, AWSHelperFn]
                 Organization=NOTHING, # type: Union[str, AWSHelperFn]
                 OrganizationalUnit=NOTHING, # type: Union[str, AWSHelperFn]
                 Pseudonym=NOTHING, # type: Union[str, AWSHelperFn]
                 SerialNumber=NOTHING, # type: Union[str, AWSHelperFn]
                 State=NOTHING, # type: Union[str, AWSHelperFn]
                 Surname=NOTHING, # type: Union[str, AWSHelperFn]
                 Title=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CommonName=CommonName,
            Country=Country,
            DistinguishedNameQualifier=DistinguishedNameQualifier,
            GenerationQualifier=GenerationQualifier,
            GivenName=GivenName,
            Initials=Initials,
            Locality=Locality,
            Organization=Organization,
            OrganizationalUnit=OrganizationalUnit,
            Pseudonym=Pseudonym,
            SerialNumber=SerialNumber,
            State=State,
            Surname=Surname,
            Title=Title,
            **kwargs
        )
        super(Subject, self).__init__(**processed_kwargs)


class CertificateAuthority(troposphere.acmpca.CertificateAuthority, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyAlgorithm=REQUIRED, # type: Any
                 SigningAlgorithm=REQUIRED, # type: Any
                 Subject=REQUIRED, # type: _Subject
                 Type=REQUIRED, # type: Any
                 RevocationConfiguration=NOTHING, # type: _RevocationConfiguration
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyAlgorithm=KeyAlgorithm,
            SigningAlgorithm=SigningAlgorithm,
            Subject=Subject,
            Type=Type,
            RevocationConfiguration=RevocationConfiguration,
            Tags=Tags,
            **kwargs
        )
        super(CertificateAuthority, self).__init__(**processed_kwargs)
