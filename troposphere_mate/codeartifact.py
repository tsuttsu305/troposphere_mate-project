# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codeartifact


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Domain(troposphere.codeartifact.Domain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PermissionsPolicyDocument=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            PermissionsPolicyDocument=PermissionsPolicyDocument,
            **kwargs
        )
        super(Domain, self).__init__(**processed_kwargs)


class Repository(troposphere.codeartifact.Repository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RepositoryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 ExternalConnections=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PermissionsPolicyDocument=NOTHING, # type: dict
                 Upstreams=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RepositoryName=RepositoryName,
            Description=Description,
            ExternalConnections=ExternalConnections,
            PermissionsPolicyDocument=PermissionsPolicyDocument,
            Upstreams=Upstreams,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)
