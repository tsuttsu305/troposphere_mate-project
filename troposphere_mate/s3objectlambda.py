# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.s3objectlambda

from troposphere.s3objectlambda import (
    ObjectLambdaConfiguration as _ObjectLambdaConfiguration,
    TransformationConfiguration as _TransformationConfiguration,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class TransformationConfiguration(troposphere.s3objectlambda.TransformationConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Actions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ContentTransformation=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            ContentTransformation=ContentTransformation,
            **kwargs
        )
        super(TransformationConfiguration, self).__init__(**processed_kwargs)


class ObjectLambdaConfiguration(troposphere.s3objectlambda.ObjectLambdaConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SupportingAccessPoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 TransformationConfigurations=REQUIRED, # type: List[_TransformationConfiguration]
                 AllowedFeatures=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 CloudWatchMetricsEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SupportingAccessPoint=SupportingAccessPoint,
            TransformationConfigurations=TransformationConfigurations,
            AllowedFeatures=AllowedFeatures,
            CloudWatchMetricsEnabled=CloudWatchMetricsEnabled,
            **kwargs
        )
        super(ObjectLambdaConfiguration, self).__init__(**processed_kwargs)


class AccessPoint(troposphere.s3objectlambda.AccessPoint, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 ObjectLambdaConfiguration=NOTHING, # type: _ObjectLambdaConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            ObjectLambdaConfiguration=ObjectLambdaConfiguration,
            **kwargs
        )
        super(AccessPoint, self).__init__(**processed_kwargs)


class AccessPointPolicy(troposphere.s3objectlambda.AccessPointPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ObjectLambdaAccessPoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 PolicyDocument=REQUIRED, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ObjectLambdaAccessPoint=ObjectLambdaAccessPoint,
            PolicyDocument=PolicyDocument,
            **kwargs
        )
        super(AccessPointPolicy, self).__init__(**processed_kwargs)
