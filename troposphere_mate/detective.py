# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.detective


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Graph(troposphere.detective.Graph, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            **kwargs
        )
        super(Graph, self).__init__(**processed_kwargs)


class MemberInvitation(troposphere.detective.MemberInvitation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GraphArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 MemberEmailAddress=REQUIRED, # type: Union[str, AWSHelperFn]
                 MemberId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Message=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GraphArn=GraphArn,
            MemberEmailAddress=MemberEmailAddress,
            MemberId=MemberId,
            Message=Message,
            **kwargs
        )
        super(MemberInvitation, self).__init__(**processed_kwargs)
