# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.acmpca

from troposphere.acmpca import (
    ApiPassthrough as _ApiPassthrough,
    CertificatePolicyList as _CertificatePolicyList,
    CrlConfiguration as _CrlConfiguration,
    EdiPartyName as _EdiPartyName,
    ExtendedKeyUsage as _ExtendedKeyUsage,
    ExtendedKeyUsageList as _ExtendedKeyUsageList,
    Extensions as _Extensions,
    GeneralName as _GeneralName,
    GeneralNameList as _GeneralNameList,
    KeyUsage as _KeyUsage,
    OtherName as _OtherName,
    PolicyInformation as _PolicyInformation,
    PolicyQualifierInfo as _PolicyQualifierInfo,
    PolicyQualifierInfoList as _PolicyQualifierInfoList,
    Qualifier as _Qualifier,
    RevocationConfiguration as _RevocationConfiguration,
    Subject as _Subject,
    Tags as _Tags,
    Validity as _Validity,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Qualifier(troposphere.acmpca.Qualifier, Mixin):
    def __init__(self,
                 title=None,
                 CpsUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CpsUri=CpsUri,
            **kwargs
        )
        super(Qualifier, self).__init__(**processed_kwargs)


class PolicyQualifierInfo(troposphere.acmpca.PolicyQualifierInfo, Mixin):
    def __init__(self,
                 title=None,
                 PolicyQualifierId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Qualifier=REQUIRED, # type: _Qualifier
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PolicyQualifierId=PolicyQualifierId,
            Qualifier=Qualifier,
            **kwargs
        )
        super(PolicyQualifierInfo, self).__init__(**processed_kwargs)


class PolicyQualifierInfoList(troposphere.acmpca.PolicyQualifierInfoList, Mixin):
    def __init__(self,
                 title=None,
                 PolicyQualifierInfoList=NOTHING, # type: List[_PolicyQualifierInfo]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PolicyQualifierInfoList=PolicyQualifierInfoList,
            **kwargs
        )
        super(PolicyQualifierInfoList, self).__init__(**processed_kwargs)


class PolicyInformation(troposphere.acmpca.PolicyInformation, Mixin):
    def __init__(self,
                 title=None,
                 CertPolicyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyQualifiers=NOTHING, # type: _PolicyQualifierInfoList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertPolicyId=CertPolicyId,
            PolicyQualifiers=PolicyQualifiers,
            **kwargs
        )
        super(PolicyInformation, self).__init__(**processed_kwargs)


class CertificatePolicyList(troposphere.acmpca.CertificatePolicyList, Mixin):
    def __init__(self,
                 title=None,
                 CertificatePolicyList=NOTHING, # type: List[_PolicyInformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificatePolicyList=CertificatePolicyList,
            **kwargs
        )
        super(CertificatePolicyList, self).__init__(**processed_kwargs)


class ExtendedKeyUsage(troposphere.acmpca.ExtendedKeyUsage, Mixin):
    def __init__(self,
                 title=None,
                 ExtendedKeyUsageObjectIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 ExtendedKeyUsageType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExtendedKeyUsageObjectIdentifier=ExtendedKeyUsageObjectIdentifier,
            ExtendedKeyUsageType=ExtendedKeyUsageType,
            **kwargs
        )
        super(ExtendedKeyUsage, self).__init__(**processed_kwargs)


class ExtendedKeyUsageList(troposphere.acmpca.ExtendedKeyUsageList, Mixin):
    def __init__(self,
                 title=None,
                 ExtendedKeyUsageList=NOTHING, # type: List[_ExtendedKeyUsage]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExtendedKeyUsageList=ExtendedKeyUsageList,
            **kwargs
        )
        super(ExtendedKeyUsageList, self).__init__(**processed_kwargs)


class EdiPartyName(troposphere.acmpca.EdiPartyName, Mixin):
    def __init__(self,
                 title=None,
                 NameAssigner=REQUIRED, # type: Union[str, AWSHelperFn]
                 PartyName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            NameAssigner=NameAssigner,
            PartyName=PartyName,
            **kwargs
        )
        super(EdiPartyName, self).__init__(**processed_kwargs)


class OtherName(troposphere.acmpca.OtherName, Mixin):
    def __init__(self,
                 title=None,
                 TypeId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TypeId=TypeId,
            Value=Value,
            **kwargs
        )
        super(OtherName, self).__init__(**processed_kwargs)


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


class GeneralName(troposphere.acmpca.GeneralName, Mixin):
    def __init__(self,
                 title=None,
                 DirectoryName=NOTHING, # type: _Subject
                 DnsName=NOTHING, # type: Union[str, AWSHelperFn]
                 EdiPartyName=NOTHING, # type: _EdiPartyName
                 IpAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 OtherName=NOTHING, # type: _OtherName
                 RegisteredId=NOTHING, # type: Union[str, AWSHelperFn]
                 Rfc822Name=NOTHING, # type: Union[str, AWSHelperFn]
                 UniformResourceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DirectoryName=DirectoryName,
            DnsName=DnsName,
            EdiPartyName=EdiPartyName,
            IpAddress=IpAddress,
            OtherName=OtherName,
            RegisteredId=RegisteredId,
            Rfc822Name=Rfc822Name,
            UniformResourceIdentifier=UniformResourceIdentifier,
            **kwargs
        )
        super(GeneralName, self).__init__(**processed_kwargs)


class GeneralNameList(troposphere.acmpca.GeneralNameList, Mixin):
    def __init__(self,
                 title=None,
                 GeneralNameList=NOTHING, # type: List[_GeneralName]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GeneralNameList=GeneralNameList,
            **kwargs
        )
        super(GeneralNameList, self).__init__(**processed_kwargs)


class KeyUsage(troposphere.acmpca.KeyUsage, Mixin):
    def __init__(self,
                 title=None,
                 CRLSign=NOTHING, # type: bool
                 DataEncipherment=NOTHING, # type: bool
                 DecipherOnly=NOTHING, # type: bool
                 DigitalSignature=NOTHING, # type: bool
                 EncipherOnly=NOTHING, # type: bool
                 KeyAgreement=NOTHING, # type: bool
                 KeyCertSign=NOTHING, # type: bool
                 KeyEncipherment=NOTHING, # type: bool
                 NonRepudiation=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CRLSign=CRLSign,
            DataEncipherment=DataEncipherment,
            DecipherOnly=DecipherOnly,
            DigitalSignature=DigitalSignature,
            EncipherOnly=EncipherOnly,
            KeyAgreement=KeyAgreement,
            KeyCertSign=KeyCertSign,
            KeyEncipherment=KeyEncipherment,
            NonRepudiation=NonRepudiation,
            **kwargs
        )
        super(KeyUsage, self).__init__(**processed_kwargs)


class Extensions(troposphere.acmpca.Extensions, Mixin):
    def __init__(self,
                 title=None,
                 CertificatePolicies=NOTHING, # type: _CertificatePolicyList
                 ExtendedKeyUsage=NOTHING, # type: _ExtendedKeyUsageList
                 KeyUsage=NOTHING, # type: _KeyUsage
                 SubjectAlternativeNames=NOTHING, # type: _GeneralNameList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CertificatePolicies=CertificatePolicies,
            ExtendedKeyUsage=ExtendedKeyUsage,
            KeyUsage=KeyUsage,
            SubjectAlternativeNames=SubjectAlternativeNames,
            **kwargs
        )
        super(Extensions, self).__init__(**processed_kwargs)


class ApiPassthrough(troposphere.acmpca.ApiPassthrough, Mixin):
    def __init__(self,
                 title=None,
                 Extensions=NOTHING, # type: _Extensions
                 Subject=NOTHING, # type: _Subject
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Extensions=Extensions,
            Subject=Subject,
            **kwargs
        )
        super(ApiPassthrough, self).__init__(**processed_kwargs)


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
                 ApiPassthrough=NOTHING, # type: _ApiPassthrough
                 TemplateArn=NOTHING, # type: Union[str, AWSHelperFn]
                 ValidityNotBefore=NOTHING, # type: _Validity
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CertificateAuthorityArn=CertificateAuthorityArn,
            CertificateSigningRequest=CertificateSigningRequest,
            SigningAlgorithm=SigningAlgorithm,
            Validity=Validity,
            ApiPassthrough=ApiPassthrough,
            TemplateArn=TemplateArn,
            ValidityNotBefore=ValidityNotBefore,
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
