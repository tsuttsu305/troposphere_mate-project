# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.cassandra

from troposphere.cassandra import (
    BillingMode as _BillingMode,
    ClusteringKeyColumn as _ClusteringKeyColumn,
    Column as _Column,
    ProvisionedThroughput as _ProvisionedThroughput,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Keyspace(troposphere.cassandra.Keyspace, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyspaceName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyspaceName=KeyspaceName,
            **kwargs
        )
        super(Keyspace, self).__init__(**processed_kwargs)


class Column(troposphere.cassandra.Column, Mixin):
    def __init__(self,
                 title=None,
                 ColumnName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ColumnType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ColumnName=ColumnName,
            ColumnType=ColumnType,
            **kwargs
        )
        super(Column, self).__init__(**processed_kwargs)


class ClusteringKeyColumn(troposphere.cassandra.ClusteringKeyColumn, Mixin):
    def __init__(self,
                 title=None,
                 Column=REQUIRED, # type: _Column
                 OrderBy=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Column=Column,
            OrderBy=OrderBy,
            **kwargs
        )
        super(ClusteringKeyColumn, self).__init__(**processed_kwargs)


class ProvisionedThroughput(troposphere.cassandra.ProvisionedThroughput, Mixin):
    def __init__(self,
                 title=None,
                 ReadCapacityUnits=REQUIRED, # type: int
                 WriteCapacityUnits=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ReadCapacityUnits=ReadCapacityUnits,
            WriteCapacityUnits=WriteCapacityUnits,
            **kwargs
        )
        super(ProvisionedThroughput, self).__init__(**processed_kwargs)


class BillingMode(troposphere.cassandra.BillingMode, Mixin):
    def __init__(self,
                 title=None,
                 Mode=REQUIRED, # type: Any
                 ProvisionedThroughput=NOTHING, # type: _ProvisionedThroughput
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Mode=Mode,
            ProvisionedThroughput=ProvisionedThroughput,
            **kwargs
        )
        super(BillingMode, self).__init__(**processed_kwargs)


class Table(troposphere.cassandra.Table, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 KeyspaceName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PartitionKeyColumns=REQUIRED, # type: List[_Column]
                 BillingMode=NOTHING, # type: _BillingMode
                 ClusteringKeyColumns=NOTHING, # type: List[_ClusteringKeyColumn]
                 RegularColumns=NOTHING, # type: List[_Column]
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            KeyspaceName=KeyspaceName,
            PartitionKeyColumns=PartitionKeyColumns,
            BillingMode=BillingMode,
            ClusteringKeyColumns=ClusteringKeyColumns,
            RegularColumns=RegularColumns,
            TableName=TableName,
            **kwargs
        )
        super(Table, self).__init__(**processed_kwargs)
