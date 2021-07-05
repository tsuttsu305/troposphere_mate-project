# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.fis

from troposphere.fis import (
    ExperimentTemplateStopCondition as _ExperimentTemplateStopCondition,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ExperimentTemplateStopCondition(troposphere.fis.ExperimentTemplateStopCondition, Mixin):
    def __init__(self,
                 title=None,
                 Source=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Source=Source,
            Value=Value,
            **kwargs
        )
        super(ExperimentTemplateStopCondition, self).__init__(**processed_kwargs)


class ExperimentTemplate(troposphere.fis.ExperimentTemplate, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Description=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StopConditions=REQUIRED, # type: List[_ExperimentTemplateStopCondition]
                 Tags=REQUIRED, # type: dict
                 Targets=REQUIRED, # type: dict
                 Actions=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Description=Description,
            RoleArn=RoleArn,
            StopConditions=StopConditions,
            Tags=Tags,
            Targets=Targets,
            Actions=Actions,
            **kwargs
        )
        super(ExperimentTemplate, self).__init__(**processed_kwargs)
