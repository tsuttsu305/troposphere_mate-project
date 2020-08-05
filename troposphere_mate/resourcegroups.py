# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.resourcegroups

from troposphere.resourcegroups import (
    Query as _Query,
    ResourceQuery as _ResourceQuery,
    TagFilter as _TagFilter,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class TagFilter(troposphere.resourcegroups.TagFilter, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Values=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Values=Values,
            **kwargs
        )
        super(TagFilter, self).__init__(**processed_kwargs)


class Query(troposphere.resourcegroups.Query, Mixin):
    def __init__(self,
                 title=None,
                 ResourceTypeFilters=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 StackIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 TagFilters=NOTHING, # type: List[_TagFilter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceTypeFilters=ResourceTypeFilters,
            StackIdentifier=StackIdentifier,
            TagFilters=TagFilters,
            **kwargs
        )
        super(Query, self).__init__(**processed_kwargs)


class ResourceQuery(troposphere.resourcegroups.ResourceQuery, Mixin):
    def __init__(self,
                 title=None,
                 Query=NOTHING, # type: _Query
                 Type=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Query=Query,
            Type=Type,
            **kwargs
        )
        super(ResourceQuery, self).__init__(**processed_kwargs)


class Group(troposphere.resourcegroups.Group, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ResourceQuery=NOTHING, # type: _ResourceQuery
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            ResourceQuery=ResourceQuery,
            Tags=Tags,
            **kwargs
        )
        super(Group, self).__init__(**processed_kwargs)
