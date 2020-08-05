# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.lakeformation

from troposphere.lakeformation import (
    Admins as _Admins,
    ColumnWildcard as _ColumnWildcard,
    DataLakePrincipal as _DataLakePrincipal,
    DataLocationResource as _DataLocationResource,
    DatabaseResource as _DatabaseResource,
    Resource as _Resource,
    TableResource as _TableResource,
    TableWithColumnsResource as _TableWithColumnsResource,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Admins(troposphere.lakeformation.Admins, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(Admins, self).__init__(**processed_kwargs)


class DataLakeSettings(troposphere.lakeformation.DataLakeSettings, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Admins=NOTHING, # type: _Admins
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Admins=Admins,
            **kwargs
        )
        super(DataLakeSettings, self).__init__(**processed_kwargs)


class DataLakePrincipal(troposphere.lakeformation.DataLakePrincipal, Mixin):
    def __init__(self,
                 title=None,
                 DataLakePrincipalIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataLakePrincipalIdentifier=DataLakePrincipalIdentifier,
            **kwargs
        )
        super(DataLakePrincipal, self).__init__(**processed_kwargs)


class DatabaseResource(troposphere.lakeformation.DatabaseResource, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(DatabaseResource, self).__init__(**processed_kwargs)


class TableResource(troposphere.lakeformation.TableResource, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseName=DatabaseName,
            Name=Name,
            **kwargs
        )
        super(TableResource, self).__init__(**processed_kwargs)


class DataLocationResource(troposphere.lakeformation.DataLocationResource, Mixin):
    def __init__(self,
                 title=None,
                 S3Resource=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Resource=S3Resource,
            **kwargs
        )
        super(DataLocationResource, self).__init__(**processed_kwargs)


class ColumnWildcard(troposphere.lakeformation.ColumnWildcard, Mixin):
    def __init__(self,
                 title=None,
                 ExcludedColumnNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludedColumnNames=ExcludedColumnNames,
            **kwargs
        )
        super(ColumnWildcard, self).__init__(**processed_kwargs)


class TableWithColumnsResource(troposphere.lakeformation.TableWithColumnsResource, Mixin):
    def __init__(self,
                 title=None,
                 ColumnNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ColumnWildcard=NOTHING, # type: _ColumnWildcard
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ColumnNames=ColumnNames,
            ColumnWildcard=ColumnWildcard,
            DatabaseName=DatabaseName,
            Name=Name,
            **kwargs
        )
        super(TableWithColumnsResource, self).__init__(**processed_kwargs)


class Resource(troposphere.lakeformation.Resource, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseResource=NOTHING, # type: _DatabaseResource
                 DataLocationResource=NOTHING, # type: _DataLocationResource
                 TableResource=NOTHING, # type: _TableResource
                 TableWithColumnsResource=NOTHING, # type: _TableWithColumnsResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseResource=DatabaseResource,
            DataLocationResource=DataLocationResource,
            TableResource=TableResource,
            TableWithColumnsResource=TableWithColumnsResource,
            **kwargs
        )
        super(Resource, self).__init__(**processed_kwargs)


class Permissions(troposphere.lakeformation.Permissions, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DataLakePrincipal=REQUIRED, # type: _DataLakePrincipal
                 Resource=REQUIRED, # type: _Resource
                 Permissions=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PermissionsWithGrantOption=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DataLakePrincipal=DataLakePrincipal,
            Resource=Resource,
            Permissions=Permissions,
            PermissionsWithGrantOption=PermissionsWithGrantOption,
            **kwargs
        )
        super(Permissions, self).__init__(**processed_kwargs)
