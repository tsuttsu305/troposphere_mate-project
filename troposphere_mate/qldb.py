# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.qldb

from troposphere.qldb import (
    KinesisConfiguration as _KinesisConfiguration,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Ledger(troposphere.qldb.Ledger, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PermissionsMode=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeletionProtection=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PermissionsMode=PermissionsMode,
            DeletionProtection=DeletionProtection,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(Ledger, self).__init__(**processed_kwargs)


class KinesisConfiguration(troposphere.qldb.KinesisConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AggregationEnabled=NOTHING, # type: bool
                 StreamArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregationEnabled=AggregationEnabled,
            StreamArn=StreamArn,
            **kwargs
        )
        super(KinesisConfiguration, self).__init__(**processed_kwargs)


class Stream(troposphere.qldb.Stream, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 InclusiveStartTime=REQUIRED, # type: Union[str, AWSHelperFn]
                 KinesisConfiguration=REQUIRED, # type: _KinesisConfiguration
                 LedgerName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 StreamName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExclusiveEndTime=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            InclusiveStartTime=InclusiveStartTime,
            KinesisConfiguration=KinesisConfiguration,
            LedgerName=LedgerName,
            RoleArn=RoleArn,
            StreamName=StreamName,
            ExclusiveEndTime=ExclusiveEndTime,
            Tags=Tags,
            **kwargs
        )
        super(Stream, self).__init__(**processed_kwargs)
