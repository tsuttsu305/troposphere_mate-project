# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.timestream

from troposphere.timestream import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Database(troposphere.timestream.Database, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatabaseName=DatabaseName,
            KmsKeyId=KmsKeyId,
            Tags=Tags,
            **kwargs
        )
        super(Database, self).__init__(**processed_kwargs)


class Table(troposphere.timestream.Table, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RetentionProperties=NOTHING, # type: dict
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatabaseName=DatabaseName,
            RetentionProperties=RetentionProperties,
            TableName=TableName,
            Tags=Tags,
            **kwargs
        )
        super(Table, self).__init__(**processed_kwargs)
