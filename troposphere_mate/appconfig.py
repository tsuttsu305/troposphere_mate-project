# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.appconfig

from troposphere.appconfig import (
    Monitors as _Monitors,
    Tags as _Tags,
    Validators as _Validators,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DeploymentStrategy(troposphere.appconfig.DeploymentStrategy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DeploymentDurationInMinutes=REQUIRED, # type: float
                 GrowthFactor=REQUIRED, # type: float
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ReplicateTo=REQUIRED, # type: Any
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FinalBakeTimeInMinutes=NOTHING, # type: float
                 GrowthType=NOTHING, # type: Any
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DeploymentDurationInMinutes=DeploymentDurationInMinutes,
            GrowthFactor=GrowthFactor,
            Name=Name,
            ReplicateTo=ReplicateTo,
            Description=Description,
            FinalBakeTimeInMinutes=FinalBakeTimeInMinutes,
            GrowthType=GrowthType,
            Tags=Tags,
            **kwargs
        )
        super(DeploymentStrategy, self).__init__(**processed_kwargs)


class Monitors(troposphere.appconfig.Monitors, Mixin):
    def __init__(self,
                 title=None,
                 AlarmArn=NOTHING, # type: Union[str, AWSHelperFn]
                 AlarmRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmArn=AlarmArn,
            AlarmRoleArn=AlarmRoleArn,
            **kwargs
        )
        super(Monitors, self).__init__(**processed_kwargs)


class Environment(troposphere.appconfig.Environment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Monitors=NOTHING, # type: List[_Monitors]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            Name=Name,
            Description=Description,
            Monitors=Monitors,
            Tags=Tags,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class Deployment(troposphere.appconfig.Deployment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConfigurationProfileId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ConfigurationVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeploymentStrategyId=REQUIRED, # type: Union[str, AWSHelperFn]
                 EnvironmentId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            ConfigurationProfileId=ConfigurationProfileId,
            ConfigurationVersion=ConfigurationVersion,
            DeploymentStrategyId=DeploymentStrategyId,
            EnvironmentId=EnvironmentId,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Deployment, self).__init__(**processed_kwargs)


class Validators(troposphere.appconfig.Validators, Mixin):
    def __init__(self,
                 title=None,
                 Content=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Content=Content,
            Type=Type,
            **kwargs
        )
        super(Validators, self).__init__(**processed_kwargs)


class ConfigurationProfile(troposphere.appconfig.ConfigurationProfile, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ApplicationId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LocationUri=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RetrievalRoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Validators=NOTHING, # type: List[_Validators]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ApplicationId=ApplicationId,
            LocationUri=LocationUri,
            Name=Name,
            Description=Description,
            RetrievalRoleArn=RetrievalRoleArn,
            Tags=Tags,
            Validators=Validators,
            **kwargs
        )
        super(ConfigurationProfile, self).__init__(**processed_kwargs)


class Application(troposphere.appconfig.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)
