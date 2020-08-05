# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.athena

from troposphere.athena import (
    EncryptionConfiguration as _EncryptionConfiguration,
    ResultConfiguration as _ResultConfiguration,
    ResultConfigurationUpdates as _ResultConfigurationUpdates,
    Tags as _Tags,
    WorkGroupConfiguration as _WorkGroupConfiguration,
    WorkGroupConfigurationUpdates as _WorkGroupConfigurationUpdates,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class DataCatalog(troposphere.athena.DataCatalog, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Type=Type,
            Description=Description,
            Parameters=Parameters,
            Tags=Tags,
            **kwargs
        )
        super(DataCatalog, self).__init__(**processed_kwargs)


class NamedQuery(troposphere.athena.NamedQuery, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Database=REQUIRED, # type: Union[str, AWSHelperFn]
                 QueryString=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Database=Database,
            QueryString=QueryString,
            Description=Description,
            Name=Name,
            **kwargs
        )
        super(NamedQuery, self).__init__(**processed_kwargs)


class EncryptionConfiguration(troposphere.athena.EncryptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionOption=NOTHING, # type: Any
                 KmsKey=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionOption=EncryptionOption,
            KmsKey=KmsKey,
            **kwargs
        )
        super(EncryptionConfiguration, self).__init__(**processed_kwargs)


class ResultConfiguration(troposphere.athena.ResultConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionConfiguration=NOTHING, # type: _EncryptionConfiguration
                 OutputLocation=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionConfiguration=EncryptionConfiguration,
            OutputLocation=OutputLocation,
            **kwargs
        )
        super(ResultConfiguration, self).__init__(**processed_kwargs)


class WorkGroupConfiguration(troposphere.athena.WorkGroupConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BytesScannedCutoffPerQuery=NOTHING, # type: int
                 EnforceWorkGroupConfiguration=NOTHING, # type: bool
                 PublishCloudWatchMetricsEnabled=NOTHING, # type: bool
                 RequesterPaysEnabled=NOTHING, # type: bool
                 ResultConfiguration=NOTHING, # type: _ResultConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BytesScannedCutoffPerQuery=BytesScannedCutoffPerQuery,
            EnforceWorkGroupConfiguration=EnforceWorkGroupConfiguration,
            PublishCloudWatchMetricsEnabled=PublishCloudWatchMetricsEnabled,
            RequesterPaysEnabled=RequesterPaysEnabled,
            ResultConfiguration=ResultConfiguration,
            **kwargs
        )
        super(WorkGroupConfiguration, self).__init__(**processed_kwargs)


class ResultConfigurationUpdates(troposphere.athena.ResultConfigurationUpdates, Mixin):
    def __init__(self,
                 title=None,
                 EncryptionConfiguration=NOTHING, # type: _EncryptionConfiguration
                 OutputLocation=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveEncryptionConfiguration=NOTHING, # type: bool
                 RemoveOutputLocation=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EncryptionConfiguration=EncryptionConfiguration,
            OutputLocation=OutputLocation,
            RemoveEncryptionConfiguration=RemoveEncryptionConfiguration,
            RemoveOutputLocation=RemoveOutputLocation,
            **kwargs
        )
        super(ResultConfigurationUpdates, self).__init__(**processed_kwargs)


class WorkGroupConfigurationUpdates(troposphere.athena.WorkGroupConfigurationUpdates, Mixin):
    def __init__(self,
                 title=None,
                 BytesScannedCutoffPerQuery=NOTHING, # type: int
                 EnforceWorkGroupConfiguration=NOTHING, # type: bool
                 PublishCloudWatchMetricsEnabled=NOTHING, # type: bool
                 RemoveBytesScannedCutoffPerQuery=NOTHING, # type: bool
                 RequesterPaysEnabled=NOTHING, # type: bool
                 ResultConfigurationUpdates=NOTHING, # type: _ResultConfigurationUpdates
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BytesScannedCutoffPerQuery=BytesScannedCutoffPerQuery,
            EnforceWorkGroupConfiguration=EnforceWorkGroupConfiguration,
            PublishCloudWatchMetricsEnabled=PublishCloudWatchMetricsEnabled,
            RemoveBytesScannedCutoffPerQuery=RemoveBytesScannedCutoffPerQuery,
            RequesterPaysEnabled=RequesterPaysEnabled,
            ResultConfigurationUpdates=ResultConfigurationUpdates,
            **kwargs
        )
        super(WorkGroupConfigurationUpdates, self).__init__(**processed_kwargs)


class WorkGroup(troposphere.athena.WorkGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RecursiveDeleteOption=NOTHING, # type: bool
                 State=NOTHING, # type: Any
                 Tags=NOTHING, # type: dict
                 WorkGroupConfiguration=NOTHING, # type: _WorkGroupConfiguration
                 WorkGroupConfigurationUpdates=NOTHING, # type: _WorkGroupConfigurationUpdates
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Description=Description,
            RecursiveDeleteOption=RecursiveDeleteOption,
            State=State,
            Tags=Tags,
            WorkGroupConfiguration=WorkGroupConfiguration,
            WorkGroupConfigurationUpdates=WorkGroupConfigurationUpdates,
            **kwargs
        )
        super(WorkGroup, self).__init__(**processed_kwargs)
