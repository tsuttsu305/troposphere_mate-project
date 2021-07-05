# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ce

from troposphere.ce import (
    Subscriber as _Subscriber,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AnomalyMonitor(troposphere.ce.AnomalyMonitor, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 MonitorName=REQUIRED, # type: Union[str, AWSHelperFn]
                 MonitorType=REQUIRED, # type: Union[str, AWSHelperFn]
                 MonitorDimension=NOTHING, # type: Union[str, AWSHelperFn]
                 MonitorSpecification=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            MonitorName=MonitorName,
            MonitorType=MonitorType,
            MonitorDimension=MonitorDimension,
            MonitorSpecification=MonitorSpecification,
            **kwargs
        )
        super(AnomalyMonitor, self).__init__(**processed_kwargs)


class Subscriber(troposphere.ce.Subscriber, Mixin):
    def __init__(self,
                 title=None,
                 Address=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Status=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Address=Address,
            Type=Type,
            Status=Status,
            **kwargs
        )
        super(Subscriber, self).__init__(**processed_kwargs)


class AnomalySubscription(troposphere.ce.AnomalySubscription, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Frequency=REQUIRED, # type: Union[str, AWSHelperFn]
                 MonitorArnList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Subscribers=REQUIRED, # type: List[_Subscriber]
                 SubscriptionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Threshold=REQUIRED, # type: float
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Frequency=Frequency,
            MonitorArnList=MonitorArnList,
            Subscribers=Subscribers,
            SubscriptionName=SubscriptionName,
            Threshold=Threshold,
            **kwargs
        )
        super(AnomalySubscription, self).__init__(**processed_kwargs)


class CostCategory(troposphere.ce.CostCategory, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RuleVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Rules=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RuleVersion=RuleVersion,
            Rules=Rules,
            **kwargs
        )
        super(CostCategory, self).__init__(**processed_kwargs)
