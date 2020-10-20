# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.applicationinsights

from troposphere.applicationinsights import (
    Alarm as _Alarm,
    AlarmMetric as _AlarmMetric,
    ComponentConfiguration as _ComponentConfiguration,
    ComponentMonitoringSetting as _ComponentMonitoringSetting,
    ConfigurationDetails as _ConfigurationDetails,
    CustomComponent as _CustomComponent,
    Log as _Log,
    LogPattern as _LogPattern,
    LogPatternSet as _LogPatternSet,
    SubComponentConfigurationDetails as _SubComponentConfigurationDetails,
    SubComponentTypeConfiguration as _SubComponentTypeConfiguration,
    Tags as _Tags,
    WindowsEvent as _WindowsEvent,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Alarm(troposphere.applicationinsights.Alarm, Mixin):
    def __init__(self,
                 title=None,
                 AlarmName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Severity=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmName=AlarmName,
            Severity=Severity,
            **kwargs
        )
        super(Alarm, self).__init__(**processed_kwargs)


class AlarmMetric(troposphere.applicationinsights.AlarmMetric, Mixin):
    def __init__(self,
                 title=None,
                 AlarmMetricName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmMetricName=AlarmMetricName,
            **kwargs
        )
        super(AlarmMetric, self).__init__(**processed_kwargs)


class Log(troposphere.applicationinsights.Log, Mixin):
    def __init__(self,
                 title=None,
                 LogType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Encoding=NOTHING, # type: Union[str, AWSHelperFn]
                 LogGroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 LogPath=NOTHING, # type: Union[str, AWSHelperFn]
                 PatternSet=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogType=LogType,
            Encoding=Encoding,
            LogGroupName=LogGroupName,
            LogPath=LogPath,
            PatternSet=PatternSet,
            **kwargs
        )
        super(Log, self).__init__(**processed_kwargs)


class WindowsEvent(troposphere.applicationinsights.WindowsEvent, Mixin):
    def __init__(self,
                 title=None,
                 EventLevels=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 EventName=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 PatternSet=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            EventLevels=EventLevels,
            EventName=EventName,
            LogGroupName=LogGroupName,
            PatternSet=PatternSet,
            **kwargs
        )
        super(WindowsEvent, self).__init__(**processed_kwargs)


class ConfigurationDetails(troposphere.applicationinsights.ConfigurationDetails, Mixin):
    def __init__(self,
                 title=None,
                 AlarmMetrics=NOTHING, # type: List[_AlarmMetric]
                 Alarms=NOTHING, # type: List[_Alarm]
                 Logs=NOTHING, # type: List[_Log]
                 WindowsEvents=NOTHING, # type: List[_WindowsEvent]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmMetrics=AlarmMetrics,
            Alarms=Alarms,
            Logs=Logs,
            WindowsEvents=WindowsEvents,
            **kwargs
        )
        super(ConfigurationDetails, self).__init__(**processed_kwargs)


class SubComponentConfigurationDetails(troposphere.applicationinsights.SubComponentConfigurationDetails, Mixin):
    def __init__(self,
                 title=None,
                 AlarmMetrics=NOTHING, # type: List[_AlarmMetric]
                 Logs=NOTHING, # type: List[_Log]
                 WindowsEvents=NOTHING, # type: List[_WindowsEvent]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AlarmMetrics=AlarmMetrics,
            Logs=Logs,
            WindowsEvents=WindowsEvents,
            **kwargs
        )
        super(SubComponentConfigurationDetails, self).__init__(**processed_kwargs)


class SubComponentTypeConfiguration(troposphere.applicationinsights.SubComponentTypeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SubComponentConfigurationDetails=REQUIRED, # type: _SubComponentConfigurationDetails
                 SubComponentType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubComponentConfigurationDetails=SubComponentConfigurationDetails,
            SubComponentType=SubComponentType,
            **kwargs
        )
        super(SubComponentTypeConfiguration, self).__init__(**processed_kwargs)


class ComponentConfiguration(troposphere.applicationinsights.ComponentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfigurationDetails=NOTHING, # type: _ConfigurationDetails
                 SubComponentTypeConfigurations=NOTHING, # type: List[_SubComponentTypeConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfigurationDetails=ConfigurationDetails,
            SubComponentTypeConfigurations=SubComponentTypeConfigurations,
            **kwargs
        )
        super(ComponentConfiguration, self).__init__(**processed_kwargs)


class ComponentMonitoringSetting(troposphere.applicationinsights.ComponentMonitoringSetting, Mixin):
    def __init__(self,
                 title=None,
                 ComponentARN=NOTHING, # type: Union[str, AWSHelperFn]
                 ComponentConfigurationMode=NOTHING, # type: Union[str, AWSHelperFn]
                 ComponentName=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomComponentConfiguration=NOTHING, # type: _ComponentConfiguration
                 DefaultOverwriteComponentConfiguration=NOTHING, # type: _ComponentConfiguration
                 Tier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComponentARN=ComponentARN,
            ComponentConfigurationMode=ComponentConfigurationMode,
            ComponentName=ComponentName,
            CustomComponentConfiguration=CustomComponentConfiguration,
            DefaultOverwriteComponentConfiguration=DefaultOverwriteComponentConfiguration,
            Tier=Tier,
            **kwargs
        )
        super(ComponentMonitoringSetting, self).__init__(**processed_kwargs)


class CustomComponent(troposphere.applicationinsights.CustomComponent, Mixin):
    def __init__(self,
                 title=None,
                 ComponentName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ResourceList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComponentName=ComponentName,
            ResourceList=ResourceList,
            **kwargs
        )
        super(CustomComponent, self).__init__(**processed_kwargs)


class LogPattern(troposphere.applicationinsights.LogPattern, Mixin):
    def __init__(self,
                 title=None,
                 Pattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 PatternName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Rank=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pattern=Pattern,
            PatternName=PatternName,
            Rank=Rank,
            **kwargs
        )
        super(LogPattern, self).__init__(**processed_kwargs)


class LogPatternSet(troposphere.applicationinsights.LogPatternSet, Mixin):
    def __init__(self,
                 title=None,
                 LogPatterns=REQUIRED, # type: List[_LogPattern]
                 PatternSetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogPatterns=LogPatterns,
            PatternSetName=PatternSetName,
            **kwargs
        )
        super(LogPatternSet, self).__init__(**processed_kwargs)


class Application(troposphere.applicationinsights.Application, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceGroupName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AutoConfigurationEnabled=NOTHING, # type: bool
                 CWEMonitorEnabled=NOTHING, # type: bool
                 ComponentMonitoringSettings=NOTHING, # type: List[_ComponentMonitoringSetting]
                 CustomComponents=NOTHING, # type: List[_CustomComponent]
                 LogPatternSets=NOTHING, # type: List[_LogPatternSet]
                 OpsCenterEnabled=NOTHING, # type: bool
                 OpsItemSNSTopicArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceGroupName=ResourceGroupName,
            AutoConfigurationEnabled=AutoConfigurationEnabled,
            CWEMonitorEnabled=CWEMonitorEnabled,
            ComponentMonitoringSettings=ComponentMonitoringSettings,
            CustomComponents=CustomComponents,
            LogPatternSets=LogPatternSets,
            OpsCenterEnabled=OpsCenterEnabled,
            OpsItemSNSTopicArn=OpsItemSNSTopicArn,
            Tags=Tags,
            **kwargs
        )
        super(Application, self).__init__(**processed_kwargs)
