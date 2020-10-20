# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.sso

from troposphere.sso import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Assignment(troposphere.sso.Assignment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PermissionSetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrincipalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 PrincipalType=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceArn=InstanceArn,
            PermissionSetArn=PermissionSetArn,
            PrincipalId=PrincipalId,
            PrincipalType=PrincipalType,
            TargetId=TargetId,
            TargetType=TargetType,
            **kwargs
        )
        super(Assignment, self).__init__(**processed_kwargs)


class PermissionSet(troposphere.sso.PermissionSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InstanceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 InlinePolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 ManagedPolicies=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 RelayStateType=NOTHING, # type: Union[str, AWSHelperFn]
                 SessionDuration=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InstanceArn=InstanceArn,
            Name=Name,
            Description=Description,
            InlinePolicy=InlinePolicy,
            ManagedPolicies=ManagedPolicies,
            RelayStateType=RelayStateType,
            SessionDuration=SessionDuration,
            Tags=Tags,
            **kwargs
        )
        super(PermissionSet, self).__init__(**processed_kwargs)
