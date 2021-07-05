# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.secretsmanager

from troposphere.secretsmanager import (
    GenerateSecretString as _GenerateSecretString,
    HostedRotationLambda as _HostedRotationLambda,
    ReplicaRegion as _ReplicaRegion,
    RotationRules as _RotationRules,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ResourcePolicy(troposphere.secretsmanager.ResourcePolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourcePolicy=REQUIRED, # type: Union[dict]
                 BlockPublicPolicy=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            ResourcePolicy=ResourcePolicy,
            BlockPublicPolicy=BlockPublicPolicy,
            **kwargs
        )
        super(ResourcePolicy, self).__init__(**processed_kwargs)


class HostedRotationLambda(troposphere.secretsmanager.HostedRotationLambda, Mixin):
    def __init__(self,
                 title=None,
                 RotationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 KmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MasterSecretArn=NOTHING, # type: Union[str, AWSHelperFn]
                 MasterSecretKmsKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 RotationLambdaName=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcSecurityGroupIds=NOTHING, # type: Union[str, AWSHelperFn]
                 VpcSubnetIds=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RotationType=RotationType,
            KmsKeyArn=KmsKeyArn,
            MasterSecretArn=MasterSecretArn,
            MasterSecretKmsKeyArn=MasterSecretKmsKeyArn,
            RotationLambdaName=RotationLambdaName,
            VpcSecurityGroupIds=VpcSecurityGroupIds,
            VpcSubnetIds=VpcSubnetIds,
            **kwargs
        )
        super(HostedRotationLambda, self).__init__(**processed_kwargs)


class RotationRules(troposphere.secretsmanager.RotationRules, Mixin):
    def __init__(self,
                 title=None,
                 AutomaticallyAfterDays=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AutomaticallyAfterDays=AutomaticallyAfterDays,
            **kwargs
        )
        super(RotationRules, self).__init__(**processed_kwargs)


class RotationSchedule(troposphere.secretsmanager.RotationSchedule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 HostedRotationLambda=NOTHING, # type: _HostedRotationLambda
                 RotationLambdaARN=NOTHING, # type: Union[str, AWSHelperFn]
                 RotationRules=NOTHING, # type: _RotationRules
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            HostedRotationLambda=HostedRotationLambda,
            RotationLambdaARN=RotationLambdaARN,
            RotationRules=RotationRules,
            **kwargs
        )
        super(RotationSchedule, self).__init__(**processed_kwargs)


class GenerateSecretString(troposphere.secretsmanager.GenerateSecretString, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeCharacters=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludeLowercase=NOTHING, # type: bool
                 ExcludeNumbers=NOTHING, # type: bool
                 ExcludePunctuation=NOTHING, # type: bool
                 ExcludeUppercase=NOTHING, # type: bool
                 GenerateStringKey=NOTHING, # type: Union[str, AWSHelperFn]
                 IncludeSpace=NOTHING, # type: bool
                 PasswordLength=NOTHING, # type: int
                 RequireEachIncludedType=NOTHING, # type: bool
                 SecretStringTemplate=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeCharacters=ExcludeCharacters,
            ExcludeLowercase=ExcludeLowercase,
            ExcludeNumbers=ExcludeNumbers,
            ExcludePunctuation=ExcludePunctuation,
            ExcludeUppercase=ExcludeUppercase,
            GenerateStringKey=GenerateStringKey,
            IncludeSpace=IncludeSpace,
            PasswordLength=PasswordLength,
            RequireEachIncludedType=RequireEachIncludedType,
            SecretStringTemplate=SecretStringTemplate,
            **kwargs
        )
        super(GenerateSecretString, self).__init__(**processed_kwargs)


class ReplicaRegion(troposphere.secretsmanager.ReplicaRegion, Mixin):
    def __init__(self,
                 title=None,
                 Region=REQUIRED, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Region=Region,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(ReplicaRegion, self).__init__(**processed_kwargs)


class Secret(troposphere.secretsmanager.Secret, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 GenerateSecretString=NOTHING, # type: _GenerateSecretString
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 ReplicaRegions=NOTHING, # type: List[_ReplicaRegion]
                 SecretString=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: Union[_Tags, list]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            GenerateSecretString=GenerateSecretString,
            KmsKeyId=KmsKeyId,
            Name=Name,
            ReplicaRegions=ReplicaRegions,
            SecretString=SecretString,
            Tags=Tags,
            **kwargs
        )
        super(Secret, self).__init__(**processed_kwargs)


class SecretTargetAttachment(troposphere.secretsmanager.SecretTargetAttachment, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 SecretId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetType=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            SecretId=SecretId,
            TargetId=TargetId,
            TargetType=TargetType,
            **kwargs
        )
        super(SecretTargetAttachment, self).__init__(**processed_kwargs)
