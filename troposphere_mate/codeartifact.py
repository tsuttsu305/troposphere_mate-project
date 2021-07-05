# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codeartifact

from troposphere.codeartifact import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Domain(troposphere.codeartifact.Domain, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 EncryptionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 PermissionsPolicyDocument=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            EncryptionKey=EncryptionKey,
            PermissionsPolicyDocument=PermissionsPolicyDocument,
            Tags=Tags,
            **kwargs
        )
        super(Domain, self).__init__(**processed_kwargs)


class Repository(troposphere.codeartifact.Repository, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DomainName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RepositoryName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DomainOwner=NOTHING, # type: Union[str, AWSHelperFn]
                 ExternalConnections=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 PermissionsPolicyDocument=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 Upstreams=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DomainName=DomainName,
            RepositoryName=RepositoryName,
            Description=Description,
            DomainOwner=DomainOwner,
            ExternalConnections=ExternalConnections,
            PermissionsPolicyDocument=PermissionsPolicyDocument,
            Tags=Tags,
            Upstreams=Upstreams,
            **kwargs
        )
        super(Repository, self).__init__(**processed_kwargs)
