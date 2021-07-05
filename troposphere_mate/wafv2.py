# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.wafv2

from troposphere.wafv2 import (
    AllQueryArguments as _AllQueryArguments,
    AllowAction as _AllowAction,
    AndStatementOne as _AndStatementOne,
    AndStatementTwo as _AndStatementTwo,
    BlockAction as _BlockAction,
    Body as _Body,
    ByteMatchStatement as _ByteMatchStatement,
    CountAction as _CountAction,
    DefaultAction as _DefaultAction,
    ExcludedRule as _ExcludedRule,
    FieldToMatch as _FieldToMatch,
    ForwardedIPConfiguration as _ForwardedIPConfiguration,
    GeoMatchStatement as _GeoMatchStatement,
    IPSetForwardedIPConfiguration as _IPSetForwardedIPConfiguration,
    IPSetReferenceStatement as _IPSetReferenceStatement,
    ManagedRuleGroupStatement as _ManagedRuleGroupStatement,
    Method as _Method,
    NoneAction as _NoneAction,
    NotStatementOne as _NotStatementOne,
    NotStatementTwo as _NotStatementTwo,
    OrStatementOne as _OrStatementOne,
    OrStatementTwo as _OrStatementTwo,
    OverrideAction as _OverrideAction,
    QueryString as _QueryString,
    RateBasedStatementOne as _RateBasedStatementOne,
    RateBasedStatementTwo as _RateBasedStatementTwo,
    RegexPatternSetReferenceStatement as _RegexPatternSetReferenceStatement,
    RuleAction as _RuleAction,
    RuleGroupReferenceStatement as _RuleGroupReferenceStatement,
    RuleGroupRule as _RuleGroupRule,
    SingleHeader as _SingleHeader,
    SingleQueryArgument as _SingleQueryArgument,
    SizeConstraintStatement as _SizeConstraintStatement,
    SqliMatchStatement as _SqliMatchStatement,
    StatementOne as _StatementOne,
    StatementThree as _StatementThree,
    StatementTwo as _StatementTwo,
    Tags as _Tags,
    TextTransformation as _TextTransformation,
    UriPath as _UriPath,
    VisibilityConfig as _VisibilityConfig,
    WebACLRule as _WebACLRule,
    XssMatchStatement as _XssMatchStatement,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ExcludedRule(troposphere.wafv2.ExcludedRule, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(ExcludedRule, self).__init__(**processed_kwargs)


class RuleGroupReferenceStatement(troposphere.wafv2.RuleGroupReferenceStatement, Mixin):
    def __init__(self,
                 title=None,
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludedRules=NOTHING, # type: List[_ExcludedRule]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            ExcludedRules=ExcludedRules,
            **kwargs
        )
        super(RuleGroupReferenceStatement, self).__init__(**processed_kwargs)


class TextTransformation(troposphere.wafv2.TextTransformation, Mixin):
    def __init__(self,
                 title=None,
                 Priority=NOTHING, # type: int
                 Type=NOTHING, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Priority=Priority,
            Type=Type,
            **kwargs
        )
        super(TextTransformation, self).__init__(**processed_kwargs)


class SingleHeader(troposphere.wafv2.SingleHeader, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(SingleHeader, self).__init__(**processed_kwargs)


class SingleQueryArgument(troposphere.wafv2.SingleQueryArgument, Mixin):
    def __init__(self,
                 title=None,
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            **kwargs
        )
        super(SingleQueryArgument, self).__init__(**processed_kwargs)


class Body(troposphere.wafv2.Body, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(Body, self).__init__(**processed_kwargs)


class Method(troposphere.wafv2.Method, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(Method, self).__init__(**processed_kwargs)


class AllQueryArguments(troposphere.wafv2.AllQueryArguments, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(AllQueryArguments, self).__init__(**processed_kwargs)


class QueryString(troposphere.wafv2.QueryString, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(QueryString, self).__init__(**processed_kwargs)


class UriPath(troposphere.wafv2.UriPath, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(UriPath, self).__init__(**processed_kwargs)


class FieldToMatch(troposphere.wafv2.FieldToMatch, Mixin):
    def __init__(self,
                 title=None,
                 AllQueryArguments=NOTHING, # type: _AllQueryArguments
                 Body=NOTHING, # type: _Body
                 Method=NOTHING, # type: _Method
                 QueryString=NOTHING, # type: _QueryString
                 SingleHeader=NOTHING, # type: _SingleHeader
                 SingleQueryArgument=NOTHING, # type: _SingleQueryArgument
                 UriPath=NOTHING, # type: _UriPath
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllQueryArguments=AllQueryArguments,
            Body=Body,
            Method=Method,
            QueryString=QueryString,
            SingleHeader=SingleHeader,
            SingleQueryArgument=SingleQueryArgument,
            UriPath=UriPath,
            **kwargs
        )
        super(FieldToMatch, self).__init__(**processed_kwargs)


class RegexPatternSetReferenceStatement(troposphere.wafv2.RegexPatternSetReferenceStatement, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 TextTransformations=REQUIRED, # type: List[_TextTransformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            FieldToMatch=FieldToMatch,
            TextTransformations=TextTransformations,
            **kwargs
        )
        super(RegexPatternSetReferenceStatement, self).__init__(**processed_kwargs)


class XssMatchStatement(troposphere.wafv2.XssMatchStatement, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 TextTransformations=REQUIRED, # type: List[_TextTransformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            TextTransformations=TextTransformations,
            **kwargs
        )
        super(XssMatchStatement, self).__init__(**processed_kwargs)


class SqliMatchStatement(troposphere.wafv2.SqliMatchStatement, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 TextTransformations=REQUIRED, # type: List[_TextTransformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            TextTransformations=TextTransformations,
            **kwargs
        )
        super(SqliMatchStatement, self).__init__(**processed_kwargs)


class SizeConstraintStatement(troposphere.wafv2.SizeConstraintStatement, Mixin):
    def __init__(self,
                 title=None,
                 ComparisonOperator=REQUIRED, # type: Any
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 Size=REQUIRED, # type: int
                 TextTransformations=REQUIRED, # type: List[_TextTransformation]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComparisonOperator=ComparisonOperator,
            FieldToMatch=FieldToMatch,
            Size=Size,
            TextTransformations=TextTransformations,
            **kwargs
        )
        super(SizeConstraintStatement, self).__init__(**processed_kwargs)


class ByteMatchStatement(troposphere.wafv2.ByteMatchStatement, Mixin):
    def __init__(self,
                 title=None,
                 FieldToMatch=REQUIRED, # type: _FieldToMatch
                 PositionalConstraint=REQUIRED, # type: Any
                 SearchString=REQUIRED, # type: Union[str, AWSHelperFn]
                 TextTransformations=REQUIRED, # type: List[_TextTransformation]
                 SearchStringBase64=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FieldToMatch=FieldToMatch,
            PositionalConstraint=PositionalConstraint,
            SearchString=SearchString,
            TextTransformations=TextTransformations,
            SearchStringBase64=SearchStringBase64,
            **kwargs
        )
        super(ByteMatchStatement, self).__init__(**processed_kwargs)


class ForwardedIPConfiguration(troposphere.wafv2.ForwardedIPConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 FallbackBehavior=REQUIRED, # type: Union[str, AWSHelperFn]
                 HeaderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FallbackBehavior=FallbackBehavior,
            HeaderName=HeaderName,
            **kwargs
        )
        super(ForwardedIPConfiguration, self).__init__(**processed_kwargs)


class GeoMatchStatement(troposphere.wafv2.GeoMatchStatement, Mixin):
    def __init__(self,
                 title=None,
                 CountryCodes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 ForwardedIPConfig=NOTHING, # type: _ForwardedIPConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CountryCodes=CountryCodes,
            ForwardedIPConfig=ForwardedIPConfig,
            **kwargs
        )
        super(GeoMatchStatement, self).__init__(**processed_kwargs)


class IPSetForwardedIPConfiguration(troposphere.wafv2.IPSetForwardedIPConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 FallbackBehavior=REQUIRED, # type: Union[str, AWSHelperFn]
                 HeaderName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Position=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FallbackBehavior=FallbackBehavior,
            HeaderName=HeaderName,
            Position=Position,
            **kwargs
        )
        super(IPSetForwardedIPConfiguration, self).__init__(**processed_kwargs)


class IPSetReferenceStatement(troposphere.wafv2.IPSetReferenceStatement, Mixin):
    def __init__(self,
                 title=None,
                 Arn=NOTHING, # type: Union[str, AWSHelperFn]
                 IPSetForwardedIPConfig=NOTHING, # type: _IPSetForwardedIPConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            IPSetForwardedIPConfig=IPSetForwardedIPConfig,
            **kwargs
        )
        super(IPSetReferenceStatement, self).__init__(**processed_kwargs)


class ManagedRuleGroupStatement(troposphere.wafv2.ManagedRuleGroupStatement, Mixin):
    def __init__(self,
                 title=None,
                 ExcludedRules=NOTHING, # type: List[_ExcludedRule]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 VendorName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludedRules=ExcludedRules,
            Name=Name,
            VendorName=VendorName,
            **kwargs
        )
        super(ManagedRuleGroupStatement, self).__init__(**processed_kwargs)


class StatementThree(troposphere.wafv2.StatementThree, Mixin):
    def __init__(self,
                 title=None,
                 ByteMatchStatement=NOTHING, # type: _ByteMatchStatement
                 GeoMatchStatement=NOTHING, # type: _GeoMatchStatement
                 IPSetReferenceStatement=NOTHING, # type: _IPSetReferenceStatement
                 ManagedRuleGroupStatement=NOTHING, # type: _ManagedRuleGroupStatement
                 RegexPatternSetReferenceStatement=NOTHING, # type: _RegexPatternSetReferenceStatement
                 RuleGroupReferenceStatement=NOTHING, # type: _RuleGroupReferenceStatement
                 SizeConstraintStatement=NOTHING, # type: _SizeConstraintStatement
                 SqliMatchStatement=NOTHING, # type: _SqliMatchStatement
                 XssMatchStatement=NOTHING, # type: _XssMatchStatement
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ByteMatchStatement=ByteMatchStatement,
            GeoMatchStatement=GeoMatchStatement,
            IPSetReferenceStatement=IPSetReferenceStatement,
            ManagedRuleGroupStatement=ManagedRuleGroupStatement,
            RegexPatternSetReferenceStatement=RegexPatternSetReferenceStatement,
            RuleGroupReferenceStatement=RuleGroupReferenceStatement,
            SizeConstraintStatement=SizeConstraintStatement,
            SqliMatchStatement=SqliMatchStatement,
            XssMatchStatement=XssMatchStatement,
            **kwargs
        )
        super(StatementThree, self).__init__(**processed_kwargs)


class AndStatementTwo(troposphere.wafv2.AndStatementTwo, Mixin):
    def __init__(self,
                 title=None,
                 Statements=NOTHING, # type: List[_StatementThree]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statements=Statements,
            **kwargs
        )
        super(AndStatementTwo, self).__init__(**processed_kwargs)


class NotStatementTwo(troposphere.wafv2.NotStatementTwo, Mixin):
    def __init__(self,
                 title=None,
                 Statement=NOTHING, # type: _StatementThree
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statement=Statement,
            **kwargs
        )
        super(NotStatementTwo, self).__init__(**processed_kwargs)


class OrStatementTwo(troposphere.wafv2.OrStatementTwo, Mixin):
    def __init__(self,
                 title=None,
                 Statements=NOTHING, # type: List[_StatementThree]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statements=Statements,
            **kwargs
        )
        super(OrStatementTwo, self).__init__(**processed_kwargs)


class RateBasedStatementTwo(troposphere.wafv2.RateBasedStatementTwo, Mixin):
    def __init__(self,
                 title=None,
                 AggregateKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 ForwardedIPConfig=NOTHING, # type: _ForwardedIPConfiguration
                 Limit=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregateKeyType=AggregateKeyType,
            ForwardedIPConfig=ForwardedIPConfig,
            Limit=Limit,
            **kwargs
        )
        super(RateBasedStatementTwo, self).__init__(**processed_kwargs)


class StatementTwo(troposphere.wafv2.StatementTwo, Mixin):
    def __init__(self,
                 title=None,
                 AndStatement=NOTHING, # type: _AndStatementTwo
                 ByteMatchStatement=NOTHING, # type: _ByteMatchStatement
                 GeoMatchStatement=NOTHING, # type: _GeoMatchStatement
                 IPSetReferenceStatement=NOTHING, # type: _IPSetReferenceStatement
                 ManagedRuleGroupStatement=NOTHING, # type: _ManagedRuleGroupStatement
                 NotStatement=NOTHING, # type: _NotStatementTwo
                 OrStatement=NOTHING, # type: _OrStatementTwo
                 RateBasedStatement=NOTHING, # type: _RateBasedStatementTwo
                 RegexPatternSetReferenceStatement=NOTHING, # type: _RegexPatternSetReferenceStatement
                 RuleGroupReferenceStatement=NOTHING, # type: _RuleGroupReferenceStatement
                 SizeConstraintStatement=NOTHING, # type: _SizeConstraintStatement
                 SqliMatchStatement=NOTHING, # type: _SqliMatchStatement
                 XssMatchStatement=NOTHING, # type: _XssMatchStatement
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AndStatement=AndStatement,
            ByteMatchStatement=ByteMatchStatement,
            GeoMatchStatement=GeoMatchStatement,
            IPSetReferenceStatement=IPSetReferenceStatement,
            ManagedRuleGroupStatement=ManagedRuleGroupStatement,
            NotStatement=NotStatement,
            OrStatement=OrStatement,
            RateBasedStatement=RateBasedStatement,
            RegexPatternSetReferenceStatement=RegexPatternSetReferenceStatement,
            RuleGroupReferenceStatement=RuleGroupReferenceStatement,
            SizeConstraintStatement=SizeConstraintStatement,
            SqliMatchStatement=SqliMatchStatement,
            XssMatchStatement=XssMatchStatement,
            **kwargs
        )
        super(StatementTwo, self).__init__(**processed_kwargs)


class AndStatementOne(troposphere.wafv2.AndStatementOne, Mixin):
    def __init__(self,
                 title=None,
                 Statements=NOTHING, # type: List[_StatementTwo]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statements=Statements,
            **kwargs
        )
        super(AndStatementOne, self).__init__(**processed_kwargs)


class NotStatementOne(troposphere.wafv2.NotStatementOne, Mixin):
    def __init__(self,
                 title=None,
                 Statement=NOTHING, # type: _StatementTwo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statement=Statement,
            **kwargs
        )
        super(NotStatementOne, self).__init__(**processed_kwargs)


class OrStatementOne(troposphere.wafv2.OrStatementOne, Mixin):
    def __init__(self,
                 title=None,
                 Statements=NOTHING, # type: List[_StatementTwo]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Statements=Statements,
            **kwargs
        )
        super(OrStatementOne, self).__init__(**processed_kwargs)


class RateBasedStatementOne(troposphere.wafv2.RateBasedStatementOne, Mixin):
    def __init__(self,
                 title=None,
                 AggregateKeyType=NOTHING, # type: Union[str, AWSHelperFn]
                 ForwardedIPConfig=NOTHING, # type: _ForwardedIPConfiguration
                 Limit=NOTHING, # type: int
                 ScopeDownStatement=NOTHING, # type: _StatementTwo
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregateKeyType=AggregateKeyType,
            ForwardedIPConfig=ForwardedIPConfig,
            Limit=Limit,
            ScopeDownStatement=ScopeDownStatement,
            **kwargs
        )
        super(RateBasedStatementOne, self).__init__(**processed_kwargs)


class StatementOne(troposphere.wafv2.StatementOne, Mixin):
    def __init__(self,
                 title=None,
                 AndStatement=NOTHING, # type: _AndStatementOne
                 ByteMatchStatement=NOTHING, # type: _ByteMatchStatement
                 GeoMatchStatement=NOTHING, # type: _GeoMatchStatement
                 IPSetReferenceStatement=NOTHING, # type: _IPSetReferenceStatement
                 ManagedRuleGroupStatement=NOTHING, # type: _ManagedRuleGroupStatement
                 NotStatement=NOTHING, # type: _NotStatementOne
                 OrStatement=NOTHING, # type: _OrStatementOne
                 RateBasedStatement=NOTHING, # type: _RateBasedStatementOne
                 RegexPatternSetReferenceStatement=NOTHING, # type: _RegexPatternSetReferenceStatement
                 RuleGroupReferenceStatement=NOTHING, # type: _RuleGroupReferenceStatement
                 SizeConstraintStatement=NOTHING, # type: _SizeConstraintStatement
                 SqliMatchStatement=NOTHING, # type: _SqliMatchStatement
                 XssMatchStatement=NOTHING, # type: _XssMatchStatement
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AndStatement=AndStatement,
            ByteMatchStatement=ByteMatchStatement,
            GeoMatchStatement=GeoMatchStatement,
            IPSetReferenceStatement=IPSetReferenceStatement,
            ManagedRuleGroupStatement=ManagedRuleGroupStatement,
            NotStatement=NotStatement,
            OrStatement=OrStatement,
            RateBasedStatement=RateBasedStatement,
            RegexPatternSetReferenceStatement=RegexPatternSetReferenceStatement,
            RuleGroupReferenceStatement=RuleGroupReferenceStatement,
            SizeConstraintStatement=SizeConstraintStatement,
            SqliMatchStatement=SqliMatchStatement,
            XssMatchStatement=XssMatchStatement,
            **kwargs
        )
        super(StatementOne, self).__init__(**processed_kwargs)


class VisibilityConfig(troposphere.wafv2.VisibilityConfig, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchMetricsEnabled=NOTHING, # type: bool
                 MetricName=NOTHING, # type: Union[str, AWSHelperFn]
                 SampledRequestsEnabled=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchMetricsEnabled=CloudWatchMetricsEnabled,
            MetricName=MetricName,
            SampledRequestsEnabled=SampledRequestsEnabled,
            **kwargs
        )
        super(VisibilityConfig, self).__init__(**processed_kwargs)


class AllowAction(troposphere.wafv2.AllowAction, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(AllowAction, self).__init__(**processed_kwargs)


class BlockAction(troposphere.wafv2.BlockAction, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(BlockAction, self).__init__(**processed_kwargs)


class CountAction(troposphere.wafv2.CountAction, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(CountAction, self).__init__(**processed_kwargs)


class NoneAction(troposphere.wafv2.NoneAction, Mixin):
    def __init__(self,
                 title=None,
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            **kwargs
        )
        super(NoneAction, self).__init__(**processed_kwargs)


class RuleAction(troposphere.wafv2.RuleAction, Mixin):
    def __init__(self,
                 title=None,
                 Allow=NOTHING, # type: _AllowAction
                 Block=NOTHING, # type: _BlockAction
                 Count=NOTHING, # type: _CountAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Allow=Allow,
            Block=Block,
            Count=Count,
            **kwargs
        )
        super(RuleAction, self).__init__(**processed_kwargs)


# class OverrideAction(troposphere.wafv2.OverrideAction, Mixin):
#     def __init__(self,
#                  title=None,
#                  Count=NOTHING, # type: _CountAction
#                  None=NOTHING, # type: _NoneAction
#                  **kwargs):
#         processed_kwargs = preprocess_init_kwargs(
#             title=title,
#             Count=Count,
#             None=None,
#             **kwargs
#         )
#         super(OverrideAction, self).__init__(**processed_kwargs)


class WebACLRule(troposphere.wafv2.WebACLRule, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: _RuleAction
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 OverrideAction=NOTHING, # type: _OverrideAction
                 Priority=NOTHING, # type: int
                 Statement=NOTHING, # type: _StatementOne
                 VisibilityConfig=NOTHING, # type: _VisibilityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Name=Name,
            OverrideAction=OverrideAction,
            Priority=Priority,
            Statement=Statement,
            VisibilityConfig=VisibilityConfig,
            **kwargs
        )
        super(WebACLRule, self).__init__(**processed_kwargs)


class DefaultAction(troposphere.wafv2.DefaultAction, Mixin):
    def __init__(self,
                 title=None,
                 Allow=NOTHING, # type: _AllowAction
                 Block=NOTHING, # type: _BlockAction
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Allow=Allow,
            Block=Block,
            **kwargs
        )
        super(DefaultAction, self).__init__(**processed_kwargs)


class WebACL(troposphere.wafv2.WebACL, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Scope=REQUIRED, # type: Union[str, AWSHelperFn]
                 DefaultAction=NOTHING, # type: _DefaultAction
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Rules=NOTHING, # type: List[_WebACLRule]
                 Tags=NOTHING, # type: _Tags
                 VisibilityConfig=NOTHING, # type: _VisibilityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Scope=Scope,
            DefaultAction=DefaultAction,
            Description=Description,
            Name=Name,
            Rules=Rules,
            Tags=Tags,
            VisibilityConfig=VisibilityConfig,
            **kwargs
        )
        super(WebACL, self).__init__(**processed_kwargs)


class IPSet(troposphere.wafv2.IPSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Scope=REQUIRED, # type: Union[str, AWSHelperFn]
                 Addresses=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 IPAddressVersion=NOTHING, # type: Any
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Scope=Scope,
            Addresses=Addresses,
            Description=Description,
            IPAddressVersion=IPAddressVersion,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(IPSet, self).__init__(**processed_kwargs)


class RegexPatternSet(troposphere.wafv2.RegexPatternSet, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 RegularExpressionList=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Scope=REQUIRED, # type: Union[str, AWSHelperFn]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            RegularExpressionList=RegularExpressionList,
            Scope=Scope,
            Description=Description,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(RegexPatternSet, self).__init__(**processed_kwargs)


class RuleGroupRule(troposphere.wafv2.RuleGroupRule, Mixin):
    def __init__(self,
                 title=None,
                 Action=NOTHING, # type: _RuleAction
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Priority=NOTHING, # type: int
                 Statement=NOTHING, # type: _StatementOne
                 VisibilityConfig=NOTHING, # type: _VisibilityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            Name=Name,
            Priority=Priority,
            Statement=Statement,
            VisibilityConfig=VisibilityConfig,
            **kwargs
        )
        super(RuleGroupRule, self).__init__(**processed_kwargs)


class RuleGroup(troposphere.wafv2.RuleGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Capacity=NOTHING, # type: int
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Rules=NOTHING, # type: List[_RuleGroupRule]
                 Scope=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 VisibilityConfig=NOTHING, # type: _VisibilityConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Capacity=Capacity,
            Description=Description,
            Name=Name,
            Rules=Rules,
            Scope=Scope,
            Tags=Tags,
            VisibilityConfig=VisibilityConfig,
            **kwargs
        )
        super(RuleGroup, self).__init__(**processed_kwargs)


class WebACLAssociation(troposphere.wafv2.WebACLAssociation, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ResourceArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 WebACLArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ResourceArn=ResourceArn,
            WebACLArn=WebACLArn,
            **kwargs
        )
        super(WebACLAssociation, self).__init__(**processed_kwargs)
