# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.s3outposts

from troposphere.s3outposts import (
    AbortIncompleteMultipartUpload as _AbortIncompleteMultipartUpload,
    LifecycleConfiguration as _LifecycleConfiguration,
    Rule as _Rule,
    Tags as _Tags,
    VpcConfiguration as _VpcConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class VpcConfiguration(troposphere.s3outposts.VpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 VpcId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VpcId=VpcId,
            **kwargs
        )
        super(VpcConfiguration, self).__init__(**processed_kwargs)


class AccessPoint(troposphere.s3outposts.AccessPoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 VpcConfiguration=REQUIRED, # type: _VpcConfiguration
                 Policy=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bucket=Bucket,
            Name=Name,
            VpcConfiguration=VpcConfiguration,
            Policy=Policy,
            **kwargs
        )
        super(AccessPoint, self).__init__(**processed_kwargs)


class AbortIncompleteMultipartUpload(troposphere.s3outposts.AbortIncompleteMultipartUpload, Mixin):
    def __init__(self,
                 title=None,
                 DaysAfterInitiation=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DaysAfterInitiation=DaysAfterInitiation,
            **kwargs
        )
        super(AbortIncompleteMultipartUpload, self).__init__(**processed_kwargs)


class Rule(troposphere.s3outposts.Rule, Mixin):
    def __init__(self,
                 title=None,
                 AbortIncompleteMultipartUpload=NOTHING, # type: _AbortIncompleteMultipartUpload
                 ExpirationDate=NOTHING, # type: Union[str, AWSHelperFn]
                 ExpirationInDays=NOTHING, # type: int
                 Filter=NOTHING, # type: dict
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AbortIncompleteMultipartUpload=AbortIncompleteMultipartUpload,
            ExpirationDate=ExpirationDate,
            ExpirationInDays=ExpirationInDays,
            Filter=Filter,
            Id=Id,
            Status=Status,
            **kwargs
        )
        super(Rule, self).__init__(**processed_kwargs)


class LifecycleConfiguration(troposphere.s3outposts.LifecycleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Rules=REQUIRED, # type: List[_Rule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Rules=Rules,
            **kwargs
        )
        super(LifecycleConfiguration, self).__init__(**processed_kwargs)


class Bucket(troposphere.s3outposts.Bucket, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 OutpostId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LifecycleConfiguration=NOTHING, # type: _LifecycleConfiguration
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            BucketName=BucketName,
            OutpostId=OutpostId,
            LifecycleConfiguration=LifecycleConfiguration,
            Tags=Tags,
            **kwargs
        )
        super(Bucket, self).__init__(**processed_kwargs)


class BucketPolicy(troposphere.s3outposts.BucketPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyDocument=REQUIRED, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Bucket=Bucket,
            PolicyDocument=PolicyDocument,
            **kwargs
        )
        super(BucketPolicy, self).__init__(**processed_kwargs)


class Endpoint(troposphere.s3outposts.Endpoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 OutpostId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecurityGroupId=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            OutpostId=OutpostId,
            SecurityGroupId=SecurityGroupId,
            SubnetId=SubnetId,
            **kwargs
        )
        super(Endpoint, self).__init__(**processed_kwargs)
