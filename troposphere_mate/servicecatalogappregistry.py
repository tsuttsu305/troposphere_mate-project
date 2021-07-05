# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.servicecatalogappregistry

from troposphere.servicecatalogappregistry import (
    Attributes as _Attributes,
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Application(troposphere.servicecatalogappregistry.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)


class Attributes(troposphere.servicecatalogappregistry.Attributes, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(Attributes, self).__init__(**processed_kwargs)


class AttributeGroup(troposphere.servicecatalogappregistry.AttributeGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Attributes=REQUIRED, # type: _Attributes
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Attributes=Attributes,
            Name=Name,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(AttributeGroup, self).__init__(**processed_kwargs)


class AttributeGroupAssociation(troposphere.servicecatalogappregistry.AttributeGroupAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Application=REQUIRED, # type: Union[str, AWSHelperFn]
                 AttributeGroup=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Application=Application,
            AttributeGroup=AttributeGroup,
            **kwargs
        )
        super(AttributeGroupAssociation, self).__init__(**processed_kwargs)


class ResourceAssociation(troposphere.servicecatalogappregistry.ResourceAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Application=REQUIRED, # type: Union[str, AWSHelperFn]
                 Resource=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Application=Application,
            Resource=Resource,
            ResourceType=ResourceType,
            **kwargs
        )
        super(ResourceAssociation, self).__init__(**processed_kwargs)
