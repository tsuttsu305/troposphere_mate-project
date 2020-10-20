# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cloudformation

from troposphere.cloudformation import (
    AutoDeployment as _AutoDeployment,
    DeploymentTargets as _DeploymentTargets,
    InitFileContext as _InitFileContext,
    OperationPreferences as _OperationPreferences,
    Parameter as _Parameter,
    StackInstances as _StackInstances,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Stack(troposphere.cloudformation.Stack, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 TemplateURL=REQUIRED, # type: Union[str, AWSHelperFn]
                 NotificationARNs=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Parameters=NOTHING, # type: dict
                 Tags=NOTHING, # type: Union[_Tags, list]
                 TimeoutInMinutes=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            TemplateURL=TemplateURL,
            NotificationARNs=NotificationARNs,
            Parameters=Parameters,
            Tags=Tags,
            TimeoutInMinutes=TimeoutInMinutes,
            **kwargs
        )
        super(Stack, self).__init__(**processed_kwargs)


class AutoDeployment(troposphere.cloudformation.AutoDeployment, Mixin):
    def __init__(self,
                 title=None,
                 Enabled=NOTHING, # type: bool
                 RetainStacksOnAccountRemoval=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Enabled=Enabled,
            RetainStacksOnAccountRemoval=RetainStacksOnAccountRemoval,
            **kwargs
        )
        super(AutoDeployment, self).__init__(**processed_kwargs)


class OperationPreferences(troposphere.cloudformation.OperationPreferences, Mixin):
    def __init__(self,
                 title=None,
                 FailureToleranceCount=NOTHING, # type: int
                 FailureTolerancePercentage=NOTHING, # type: int
                 MaxConcurrentCount=NOTHING, # type: int
                 MaxConcurrentPercentage=NOTHING, # type: int
                 RegionOrder=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FailureToleranceCount=FailureToleranceCount,
            FailureTolerancePercentage=FailureTolerancePercentage,
            MaxConcurrentCount=MaxConcurrentCount,
            MaxConcurrentPercentage=MaxConcurrentPercentage,
            RegionOrder=RegionOrder,
            **kwargs
        )
        super(OperationPreferences, self).__init__(**processed_kwargs)


class Parameter(troposphere.cloudformation.Parameter, Mixin):
    def __init__(self,
                 title=None,
                 ParameterKey=REQUIRED, # type: Union[str, AWSHelperFn]
                 ParameterValue=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ParameterKey=ParameterKey,
            ParameterValue=ParameterValue,
            **kwargs
        )
        super(Parameter, self).__init__(**processed_kwargs)


class DeploymentTargets(troposphere.cloudformation.DeploymentTargets, Mixin):
    def __init__(self,
                 title=None,
                 Accounts=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 OrganizationalUnitIds=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Accounts=Accounts,
            OrganizationalUnitIds=OrganizationalUnitIds,
            **kwargs
        )
        super(DeploymentTargets, self).__init__(**processed_kwargs)


class StackInstances(troposphere.cloudformation.StackInstances, Mixin):
    def __init__(self,
                 title=None,
                 DeploymentTargets=REQUIRED, # type: _DeploymentTargets
                 Regions=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 ParameterOverrides=NOTHING, # type: List[_Parameter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DeploymentTargets=DeploymentTargets,
            Regions=Regions,
            ParameterOverrides=ParameterOverrides,
            **kwargs
        )
        super(StackInstances, self).__init__(**processed_kwargs)


class StackSet(troposphere.cloudformation.StackSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AdministrationRoleARN=NOTHING, # type: Union[str, AWSHelperFn]
                 AutoDeployment=NOTHING, # type: _AutoDeployment
                 Capabilities=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ExecutionRoleName=NOTHING, # type: Union[str, AWSHelperFn]
                 OperationPreferences=NOTHING, # type: _OperationPreferences
                 Parameters=NOTHING, # type: List[_Parameter]
                 PermissionModel=NOTHING, # type: Union[str, AWSHelperFn]
                 StackInstancesGroup=NOTHING, # type: List[_StackInstances]
                 StackSetName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TemplateBody=NOTHING, # type: Union[str, AWSHelperFn]
                 TemplateURL=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AdministrationRoleARN=AdministrationRoleARN,
            AutoDeployment=AutoDeployment,
            Capabilities=Capabilities,
            Description=Description,
            ExecutionRoleName=ExecutionRoleName,
            OperationPreferences=OperationPreferences,
            Parameters=Parameters,
            PermissionModel=PermissionModel,
            StackInstancesGroup=StackInstancesGroup,
            StackSetName=StackSetName,
            Tags=Tags,
            TemplateBody=TemplateBody,
            TemplateURL=TemplateURL,
            **kwargs
        )
        super(StackSet, self).__init__(**processed_kwargs)


class WaitCondition(troposphere.cloudformation.WaitCondition, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Count=NOTHING, # type: int
                 Handle=NOTHING, # type: Union[str, AWSHelperFn]
                 Timeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Count=Count,
            Handle=Handle,
            Timeout=Timeout,
            **kwargs
        )
        super(WaitCondition, self).__init__(**processed_kwargs)


class WaitConditionHandle(troposphere.cloudformation.WaitConditionHandle, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            **kwargs
        )
        super(WaitConditionHandle, self).__init__(**processed_kwargs)


class InitFile(troposphere.cloudformation.InitFile, Mixin):
    def __init__(self,
                 title=None,
                 content=NOTHING, # type: Union[str, AWSHelperFn]
                 mode=NOTHING, # type: Union[str, AWSHelperFn]
                 owner=NOTHING, # type: Union[str, AWSHelperFn]
                 encoding=NOTHING, # type: str
                 group=NOTHING, # type: Union[str, AWSHelperFn]
                 source=NOTHING, # type: Union[str, AWSHelperFn]
                 authentication=NOTHING, # type: Union[str, AWSHelperFn]
                 context=NOTHING, # type: _InitFileContext
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            content=content,
            mode=mode,
            owner=owner,
            encoding=encoding,
            group=group,
            source=source,
            authentication=authentication,
            context=context,
            **kwargs
        )
        super(InitFile, self).__init__(**processed_kwargs)


class InitService(troposphere.cloudformation.InitService, Mixin):
    def __init__(self,
                 title=None,
                 ensureRunning=NOTHING, # type: bool
                 enabled=NOTHING, # type: bool
                 files=NOTHING, # type: list
                 packages=NOTHING, # type: dict
                 sources=NOTHING, # type: list
                 commands=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ensureRunning=ensureRunning,
            enabled=enabled,
            files=files,
            packages=packages,
            sources=sources,
            commands=commands,
            **kwargs
        )
        super(InitService, self).__init__(**processed_kwargs)


class InitConfig(troposphere.cloudformation.InitConfig, Mixin):
    def __init__(self,
                 title=None,
                 groups=NOTHING, # type: dict
                 users=NOTHING, # type: dict
                 sources=NOTHING, # type: dict
                 packages=NOTHING, # type: dict
                 files=NOTHING, # type: dict
                 commands=NOTHING, # type: dict
                 services=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            groups=groups,
            users=users,
            sources=sources,
            packages=packages,
            files=files,
            commands=commands,
            services=services,
            **kwargs
        )
        super(InitConfig, self).__init__(**processed_kwargs)


class AuthenticationBlock(troposphere.cloudformation.AuthenticationBlock, Mixin):
    def __init__(self,
                 title=None,
                 accessKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 buckets=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 password=NOTHING, # type: Union[str, AWSHelperFn]
                 secretKey=NOTHING, # type: Union[str, AWSHelperFn]
                 type=NOTHING, # type: Any
                 uris=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 username=NOTHING, # type: Union[str, AWSHelperFn]
                 roleName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            accessKeyId=accessKeyId,
            buckets=buckets,
            password=password,
            secretKey=secretKey,
            type=type,
            uris=uris,
            username=username,
            roleName=roleName,
            **kwargs
        )
        super(AuthenticationBlock, self).__init__(**processed_kwargs)
