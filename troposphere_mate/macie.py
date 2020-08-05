# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.macie

from troposphere.macie import (
    FindingCriteria as _FindingCriteria,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Session(troposphere.macie.Session, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FindingPublishingFrequency=NOTHING, # type: Any
                 Status=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FindingPublishingFrequency=FindingPublishingFrequency,
            Status=Status,
            **kwargs
        )
        super(Session, self).__init__(**processed_kwargs)


class CustomDataIdentifier(troposphere.macie.CustomDataIdentifier, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Regex=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 IgnoreWords=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Keywords=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaximumMatchDistance=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Regex=Regex,
            Description=Description,
            IgnoreWords=IgnoreWords,
            Keywords=Keywords,
            MaximumMatchDistance=MaximumMatchDistance,
            **kwargs
        )
        super(CustomDataIdentifier, self).__init__(**processed_kwargs)


class FindingCriteria(troposphere.macie.FindingCriteria, Mixin):
    def __init__(self,
                 title=None,
                 Criterion=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Criterion=Criterion,
            **kwargs
        )
        super(FindingCriteria, self).__init__(**processed_kwargs)


class FindingsFilter(troposphere.macie.FindingsFilter, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Action=NOTHING, # type: Any
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FindingCriteria=NOTHING, # type: _FindingCriteria
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Position=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Action=Action,
            Description=Description,
            FindingCriteria=FindingCriteria,
            Name=Name,
            Position=Position,
            **kwargs
        )
        super(FindingsFilter, self).__init__(**processed_kwargs)
