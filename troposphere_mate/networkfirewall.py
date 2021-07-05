# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.networkfirewall

from troposphere.networkfirewall import (
    ActionDefinition as _ActionDefinition,
    Address as _Address,
    CustomAction as _CustomAction,
    Dimension as _Dimension,
    Header as _Header,
    LogDestinationConfig as _LogDestinationConfig,
    MatchAttributes as _MatchAttributes,
    PortRange as _PortRange,
    PublishMetricAction as _PublishMetricAction,
    RuleDefinition as _RuleDefinition,
    RuleOption as _RuleOption,
    RuleVariables as _RuleVariables,
    RulesSource as _RulesSource,
    RulesSourceList as _RulesSourceList,
    StatefulRule as _StatefulRule,
    StatefulRuleGroupReference as _StatefulRuleGroupReference,
    StatelessRule as _StatelessRule,
    StatelessRuleGroupReference as _StatelessRuleGroupReference,
    StatelessRulesAndCustomActions as _StatelessRulesAndCustomActions,
    SubnetMapping as _SubnetMapping,
    TCPFlagField as _TCPFlagField,
    Tags as _Tags,
    integer as _integer,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class SubnetMapping(troposphere.networkfirewall.SubnetMapping, Mixin):
    def __init__(self,
                 title=None,
                 SubnetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SubnetId=SubnetId,
            **kwargs
        )
        super(SubnetMapping, self).__init__(**processed_kwargs)


class Firewall(troposphere.networkfirewall.Firewall, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 FirewallName=REQUIRED, # type: Union[str, AWSHelperFn]
                 FirewallPolicyArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SubnetMappings=REQUIRED, # type: List[_SubnetMapping]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeleteProtection=NOTHING, # type: bool
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FirewallPolicyChangeProtection=NOTHING, # type: bool
                 SubnetChangeProtection=NOTHING, # type: bool
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            FirewallName=FirewallName,
            FirewallPolicyArn=FirewallPolicyArn,
            SubnetMappings=SubnetMappings,
            VpcId=VpcId,
            DeleteProtection=DeleteProtection,
            Description=Description,
            FirewallPolicyChangeProtection=FirewallPolicyChangeProtection,
            SubnetChangeProtection=SubnetChangeProtection,
            Tags=Tags,
            **kwargs
        )
        super(Firewall, self).__init__(**processed_kwargs)


class Dimension(troposphere.networkfirewall.Dimension, Mixin):
    def __init__(self,
                 title=None,
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Value=Value,
            **kwargs
        )
        super(Dimension, self).__init__(**processed_kwargs)


class PublishMetricAction(troposphere.networkfirewall.PublishMetricAction, Mixin):
    def __init__(self,
                 title=None,
                 Dimensions=REQUIRED, # type: List[_Dimension]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Dimensions=Dimensions,
            **kwargs
        )
        super(PublishMetricAction, self).__init__(**processed_kwargs)


class ActionDefinition(troposphere.networkfirewall.ActionDefinition, Mixin):
    def __init__(self,
                 title=None,
                 PublishMetricAction=NOTHING, # type: _PublishMetricAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PublishMetricAction=PublishMetricAction,
            **kwargs
        )
        super(ActionDefinition, self).__init__(**processed_kwargs)


class CustomAction(troposphere.networkfirewall.CustomAction, Mixin):
    def __init__(self,
                 title=None,
                 ActionDefinition=REQUIRED, # type: _ActionDefinition
                 ActionName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ActionDefinition=ActionDefinition,
            ActionName=ActionName,
            **kwargs
        )
        super(CustomAction, self).__init__(**processed_kwargs)


class StatefulRuleGroupReference(troposphere.networkfirewall.StatefulRuleGroupReference, Mixin):
    def __init__(self,
                 title=None,
                 ResourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ResourceArn=ResourceArn,
            **kwargs
        )
        super(StatefulRuleGroupReference, self).__init__(**processed_kwargs)


class StatelessRuleGroupReference(troposphere.networkfirewall.StatelessRuleGroupReference, Mixin):
    def __init__(self,
                 title=None,
                 Priority=REQUIRED, # type: int
                 ResourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Priority=Priority,
            ResourceArn=ResourceArn,
            **kwargs
        )
        super(StatelessRuleGroupReference, self).__init__(**processed_kwargs)


class FirewallPolicy(troposphere.networkfirewall.FirewallPolicy, Mixin):
    def __init__(self,
                 title=None,
                 StatelessDefaultActions=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 StatelessFragmentDefaultActions=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 StatefulRuleGroupReferences=NOTHING, # type: List[_StatefulRuleGroupReference]
                 StatelessCustomActions=NOTHING, # type: List[_CustomAction]
                 StatelessRuleGroupReferences=NOTHING, # type: List[_StatelessRuleGroupReference]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StatelessDefaultActions=StatelessDefaultActions,
            StatelessFragmentDefaultActions=StatelessFragmentDefaultActions,
            StatefulRuleGroupReferences=StatefulRuleGroupReferences,
            StatelessCustomActions=StatelessCustomActions,
            StatelessRuleGroupReferences=StatelessRuleGroupReferences,
            **kwargs
        )
        super(FirewallPolicy, self).__init__(**processed_kwargs)


class LogDestinationConfig(troposphere.networkfirewall.LogDestinationConfig, Mixin):
    def __init__(self,
                 title=None,
                 LogDestination=REQUIRED, # type: dict
                 LogDestinationType=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogType=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogDestination=LogDestination,
            LogDestinationType=LogDestinationType,
            LogType=LogType,
            **kwargs
        )
        super(LogDestinationConfig, self).__init__(**processed_kwargs)


class LoggingConfiguration(troposphere.networkfirewall.LoggingConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 LogDestinationConfigs=REQUIRED, # type: List[_LogDestinationConfig]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogDestinationConfigs=LogDestinationConfigs,
            **kwargs
        )
        super(LoggingConfiguration, self).__init__(**processed_kwargs)


class RuleVariables(troposphere.networkfirewall.RuleVariables, Mixin):
    def __init__(self,
                 title=None,
                 IPSets=NOTHING, # type: dict
                 PortSets=NOTHING, # type: dict
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IPSets=IPSets,
            PortSets=PortSets,
            **kwargs
        )
        super(RuleVariables, self).__init__(**processed_kwargs)


class RulesSourceList(troposphere.networkfirewall.RulesSourceList, Mixin):
    def __init__(self,
                 title=None,
                 GeneratedRulesType=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetTypes=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Targets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GeneratedRulesType=GeneratedRulesType,
            TargetTypes=TargetTypes,
            Targets=Targets,
            **kwargs
        )
        super(RulesSourceList, self).__init__(**processed_kwargs)


class Header(troposphere.networkfirewall.Header, Mixin):
    def __init__(self,
                 title=None,
                 Destination=REQUIRED, # type: Union[str, AWSHelperFn]
                 DestinationPort=REQUIRED, # type: Union[str, AWSHelperFn]
                 Direction=REQUIRED, # type: Union[str, AWSHelperFn]
                 Protocol=REQUIRED, # type: Union[str, AWSHelperFn]
                 Source=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourcePort=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Destination=Destination,
            DestinationPort=DestinationPort,
            Direction=Direction,
            Protocol=Protocol,
            Source=Source,
            SourcePort=SourcePort,
            **kwargs
        )
        super(Header, self).__init__(**processed_kwargs)


class RuleOption(troposphere.networkfirewall.RuleOption, Mixin):
    def __init__(self,
                 title=None,
                 Keyword=REQUIRED, # type: Union[str, AWSHelperFn]
                 Settings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Keyword=Keyword,
            Settings=Settings,
            **kwargs
        )
        super(RuleOption, self).__init__(**processed_kwargs)


class StatefulRule(troposphere.networkfirewall.StatefulRule, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: Union[str, AWSHelperFn]
                 Header=REQUIRED, # type: _Header
                 RuleOptions=REQUIRED, # type: List[_RuleOption]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Header=Header,
            RuleOptions=RuleOptions,
            **kwargs
        )
        super(StatefulRule, self).__init__(**processed_kwargs)


class Address(troposphere.networkfirewall.Address, Mixin):
    def __init__(self,
                 title=None,
                 AddressDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AddressDefinition=AddressDefinition,
            **kwargs
        )
        super(Address, self).__init__(**processed_kwargs)


class PortRange(troposphere.networkfirewall.PortRange, Mixin):
    def __init__(self,
                 title=None,
                 FromPort=REQUIRED, # type: int
                 ToPort=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FromPort=FromPort,
            ToPort=ToPort,
            **kwargs
        )
        super(PortRange, self).__init__(**processed_kwargs)


class TCPFlagField(troposphere.networkfirewall.TCPFlagField, Mixin):
    def __init__(self,
                 title=None,
                 Flags=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Masks=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Flags=Flags,
            Masks=Masks,
            **kwargs
        )
        super(TCPFlagField, self).__init__(**processed_kwargs)


class MatchAttributes(troposphere.networkfirewall.MatchAttributes, Mixin):
    def __init__(self,
                 title=None,
                 DestinationPorts=NOTHING, # type: List[_PortRange]
                 Destinations=NOTHING, # type: List[_Address]
                 Protocols=NOTHING, # type: List[_integer]
                 SourcePorts=NOTHING, # type: List[_PortRange]
                 Sources=NOTHING, # type: List[_Address]
                 TCPFlags=NOTHING, # type: List[_TCPFlagField]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DestinationPorts=DestinationPorts,
            Destinations=Destinations,
            Protocols=Protocols,
            SourcePorts=SourcePorts,
            Sources=Sources,
            TCPFlags=TCPFlags,
            **kwargs
        )
        super(MatchAttributes, self).__init__(**processed_kwargs)


class RuleDefinition(troposphere.networkfirewall.RuleDefinition, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 MatchAttributes=REQUIRED, # type: _MatchAttributes
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            MatchAttributes=MatchAttributes,
            **kwargs
        )
        super(RuleDefinition, self).__init__(**processed_kwargs)


class StatelessRule(troposphere.networkfirewall.StatelessRule, Mixin):
    def __init__(self,
                 title=None,
                 Priority=REQUIRED, # type: int
                 RuleDefinition=REQUIRED, # type: _RuleDefinition
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Priority=Priority,
            RuleDefinition=RuleDefinition,
            **kwargs
        )
        super(StatelessRule, self).__init__(**processed_kwargs)


class StatelessRulesAndCustomActions(troposphere.networkfirewall.StatelessRulesAndCustomActions, Mixin):
    def __init__(self,
                 title=None,
                 StatelessRules=REQUIRED, # type: List[_StatelessRule]
                 CustomActions=NOTHING, # type: List[_CustomAction]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            StatelessRules=StatelessRules,
            CustomActions=CustomActions,
            **kwargs
        )
        super(StatelessRulesAndCustomActions, self).__init__(**processed_kwargs)


class RulesSource(troposphere.networkfirewall.RulesSource, Mixin):
    def __init__(self,
                 title=None,
                 RulesSourceList=NOTHING, # type: _RulesSourceList
                 RulesString=NOTHING, # type: Union[str, AWSHelperFn]
                 StatefulRules=NOTHING, # type: List[_StatefulRule]
                 StatelessRulesAndCustomActions=NOTHING, # type: _StatelessRulesAndCustomActions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RulesSourceList=RulesSourceList,
            RulesString=RulesString,
            StatefulRules=StatefulRules,
            StatelessRulesAndCustomActions=StatelessRulesAndCustomActions,
            **kwargs
        )
        super(RulesSource, self).__init__(**processed_kwargs)


class RuleGroup(troposphere.networkfirewall.RuleGroup, Mixin):
    def __init__(self,
                 title=None,
                 RulesSource=REQUIRED, # type: _RulesSource
                 RuleVariables=NOTHING, # type: _RuleVariables
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            RulesSource=RulesSource,
            RuleVariables=RuleVariables,
            **kwargs
        )
        super(RuleGroup, self).__init__(**processed_kwargs)
