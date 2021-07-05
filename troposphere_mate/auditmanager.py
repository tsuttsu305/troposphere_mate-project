# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.auditmanager

from troposphere.auditmanager import (
    AWSAccount as _AWSAccount,
    AWSService as _AWSService,
    AssessmentReportsDestination as _AssessmentReportsDestination,
    Role as _Role,
    Scope as _Scope,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AWSAccount(troposphere.auditmanager.AWSAccount, Mixin):
    def __init__(self,
                 title=None,
                 EmailAddress=NOTHING, # type: Union[str, AWSHelperFn]
                 Id=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EmailAddress=EmailAddress,
            Id=Id,
            Name=Name,
            **kwargs
        )
        super(AWSAccount, self).__init__(**processed_kwargs)


class AssessmentReportsDestination(troposphere.auditmanager.AssessmentReportsDestination, Mixin):
    def __init__(self,
                 title=None,
                 Destination=NOTHING, # type: Union[str, AWSHelperFn]
                 DestinationType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            DestinationType=DestinationType,
            **kwargs
        )
        super(AssessmentReportsDestination, self).__init__(**processed_kwargs)


class Role(troposphere.auditmanager.Role, Mixin):
    def __init__(self,
                 title=None,
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleType=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RoleArn=RoleArn,
            RoleType=RoleType,
            **kwargs
        )
        super(Role, self).__init__(**processed_kwargs)


class AWSService(troposphere.auditmanager.AWSService, Mixin):
    def __init__(self,
                 title=None,
                 ServiceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ServiceName=ServiceName,
            **kwargs
        )
        super(AWSService, self).__init__(**processed_kwargs)


class Scope(troposphere.auditmanager.Scope, Mixin):
    def __init__(self,
                 title=None,
                 AwsAccounts=NOTHING, # type: List[_AWSAccount]
                 AwsServices=NOTHING, # type: List[_AWSService]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AwsAccounts=AwsAccounts,
            AwsServices=AwsServices,
            **kwargs
        )
        super(Scope, self).__init__(**processed_kwargs)


class Assessment(troposphere.auditmanager.Assessment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssessmentReportsDestination=NOTHING, # type: _AssessmentReportsDestination
                 AwsAccount=NOTHING, # type: _AWSAccount
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FrameworkId=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Roles=NOTHING, # type: List[_Role]
                 Scope=NOTHING, # type: _Scope
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssessmentReportsDestination=AssessmentReportsDestination,
            AwsAccount=AwsAccount,
            Description=Description,
            FrameworkId=FrameworkId,
            Name=Name,
            Roles=Roles,
            Scope=Scope,
            Status=Status,
            Tags=Tags,
            **kwargs
        )
        super(Assessment, self).__init__(**processed_kwargs)
