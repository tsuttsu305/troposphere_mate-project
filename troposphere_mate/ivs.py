# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.ivs

from troposphere.ivs import (
    Tags as _Tags,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Channel(troposphere.ivs.Channel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Authorized=NOTHING, # type: bool
                 LatencyMode=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Authorized=Authorized,
            LatencyMode=LatencyMode,
            Name=Name,
            Tags=Tags,
            Type=Type,
            **kwargs
        )
        super(Channel, self).__init__(**processed_kwargs)


class PlaybackKeyPair(troposphere.ivs.PlaybackKeyPair, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PublicKeyMaterial=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PublicKeyMaterial=PublicKeyMaterial,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(PlaybackKeyPair, self).__init__(**processed_kwargs)


class StreamKey(troposphere.ivs.StreamKey, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ChannelArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ChannelArn=ChannelArn,
            Tags=Tags,
            **kwargs
        )
        super(StreamKey, self).__init__(**processed_kwargs)
